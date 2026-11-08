"""
Bond Trend Demeaned: built from Pass 1 (short) of vault/2 Strategies/Pipeline/Bond Trend Demeaned/.

Sign of the 12-month excess return minus 12 x the expanding mean monthly excess return, on six government bond
ETFs, inverse-vol sized, 10% vol target, monthly. The file decides the weights; the lab loads, runs the book
(positions) and saves. ETF costs (tier by name and year), T-bill excess return, borrow and leverage financing
are settled in settle(), because the lab engine has one cost for all names and no cash rate.

    poetry run python strategies/bond_trend_demeaned.py --period train --variant base
    poetry run python strategies/bond_trend_demeaned.py --period train --variant base --check-lookahead
"""
import argparse, json, sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from lab.backtest import backtest            # noqa: E402
from lab.checks import delay_test, truncation_test   # noqa: E402
from lab.data import load                    # noqa: E402
from lab.runs import save_run                # noqa: E402

NAME = "Bond Trend Demeaned"

# 1.10 periods
TRAIN = ("2008-01-01", "2018-12-31")
VALIDATION = ("2019-01-01", "2021-12-31")
TEST_START = "2022-01-01"                    # never read here: lab.data.load cuts before it

# 1.4 universe
SYMBOLS = ["IEI", "IEF", "TLH", "TLT", "TIP", "BWX"]
WARMUP_MONTHS = 36                           # 1.4 / 1.5b mean warm-up: entry 36 months after first price

# 1.5 / 1.5b base version
LOOKBACK = 12                                # 1.5 lookback (months), hold 1 month
VOL_COM = 60                                 # 1.5 sizing: EWMA centre of mass, days
VOL_TARGET = 0.10                            # 1.5 book
GROSS_CAP = 2.0                              # 1.5b gross cap
BOOK_VOL_WINDOW = 60                         # assumption A3: realized vol of the raw book, past 60 trading days
BORROW = 0.0025                              # 1.5 short borrow, per year (Cost Assumptions)
LEV_SPREAD = 0.005                           # 1.5 leverage above 1x: T-bill + 50 bp; the T-bill part is in the excess return
COST_MULT = 1.0                              # 1.7 central case; stress runs change it
TIER_BP = [(500, 2.0), (50, 4.0), (10, 8.0), (2, 15.0)]   # Cost Assumptions: median $m volume of prior year -> bp; under 2 m: not tradable

VARIANTS = ["base"]
LIQ = pd.read_csv(ROOT / "data" / "etf" / "etf_liquidity.csv").set_index("symbol")


def tier_bp(sym, year):
    """Cost in bp from the median dollar volume of the previous calendar year; nan = not tradable (T5 / no volume)."""
    v = LIQ.loc[sym, str(year - 1)] if str(year - 1) in LIQ.columns else np.nan
    if pd.isna(v):
        return np.nan
    for lo, bp in TIER_BP:
        if v >= lo:
            return bp
    return np.nan


def month_ends(dates):
    """Last bar of each calendar month, on trading-day positions (Data check #6)."""
    s = pd.Series(pd.DatetimeIndex(sorted(set(dates))))
    return pd.DatetimeIndex(s.groupby([s.dt.year, s.dt.month]).max().values)


def rebalance_days(dates):
    return list(month_ends(dates))


def build_weights(daily, tbill, days, variant="base"):
    """Weights per month-end trade day, in units of capital, using only data up to the close of each day."""
    d = daily[daily["symbol"].isin(SYMBOLS)]
    px = d.pivot(index="date", columns="symbol", values="adj_close").sort_index()   # Data check #6: adj_close only
    first = px.apply(lambda s: s.first_valid_index())
    me = month_ends(px.index)
    mpx = px.loc[me]
    mret = mpx / mpx.shift(1) - 1
    # T-bill of month m-1 for the return of month m (Data check #3); annual percent, /12 per month
    tb = tbill.set_index("date")["rate"] / 100 / 12
    rf_m = pd.Series([tb.get(pd.Timestamp(m.year, m.month, 1) - pd.DateOffset(months=1), np.nan) for m in me], index=me)
    mex = mret.sub(rf_m, axis=0)
    sig = mex.rolling(LOOKBACK, min_periods=LOOKBACK).sum() - LOOKBACK * mex.expanding().mean()   # A1
    dret = px.pct_change(fill_method=None)
    vol = dret.ewm(com=VOL_COM, min_periods=VOL_COM).std().shift(1) * np.sqrt(252)               # lagged one day (1.5)
    rows = {}
    for t in days:
        t = pd.Timestamp(t)
        if t not in sig.index:
            continue
        w = pd.Series(0.0, index=px.columns)
        ok = []
        for s in px.columns:
            if pd.isna(first[s]) or t < first[s] + pd.DateOffset(months=WARMUP_MONTHS):
                continue
            if pd.isna(tier_bp(s, t.year)) or pd.isna(sig.loc[t, s]) or pd.isna(vol.loc[t, s]) or vol.loc[t, s] <= 0:
                continue
            ok.append(s)
        if ok:
            raw = pd.Series({s: np.sign(sig.loc[t, s]) / vol.loc[t, s] for s in ok})
            hist = dret.loc[:t].tail(BOOK_VOL_WINDOW)[ok].fillna(0.0)
            bv = float((hist @ raw).std() * np.sqrt(252))
            if bv > 0 and raw.abs().sum() > 0:
                k = min(VOL_TARGET / bv, GROSS_CAP / raw.abs().sum())
                w[ok] = raw * k
        rows[t] = w
    return pd.DataFrame(rows).T.reindex(columns=px.columns).fillna(0.0)


PERIODS = {"train": TRAIN, "validation": VALIDATION, "train+validation": (TRAIN[0], VALIDATION[1])}


def _inputs(open_test=False):
    daily = load("etf_daily", test_start=TEST_START, open_test=open_test)
    daily = daily[daily["symbol"].isin(SYMBOLS)]
    tb = pd.read_parquet(ROOT / "data" / "rates" / "tbill.parquet")
    if not open_test:
        tb = tb[tb["date"] < pd.Timestamp(TEST_START)]
    tb = tb.assign(time=tb["date"] + pd.DateOffset(months=1))        # month m-1 is known on the first day of month m
    return daily, tb


def settle(result, daily, tbill, weights, cost_mult):
    """Replace the engine's P&L by the ETF book: excess return over the T-bill, tiered cost per name, borrow and
    leverage financing. The engine supplies the held positions; trades are measured against the drifted holdings."""
    pos = result.positions
    px = daily.pivot(index="date", columns="symbol", values="adj_close").reindex(columns=pos.columns).sort_index()
    px = px.reindex(pos.index)
    ret = (px / px.ffill().shift(1) - 1).fillna(0.0)
    tb = tbill.set_index("date")["rate"] / 100 / 365
    rf = pd.Series([tb.get(pd.Timestamp(t.year, t.month, 1) - pd.DateOffset(months=1), np.nan) for t in pos.index], index=pos.index).ffill().fillna(0.0)
    h = pos.fillna(0.0)
    price = (h * ret).sum(axis=1) - h.sum(axis=1) * rf
    fin = -(h.clip(upper=0).abs().sum(axis=1) * BORROW / 365 + (h.abs().sum(axis=1) - 1).clip(lower=0) * LEV_SPREAD / 365)
    cost = pd.Series(0.0, index=pos.index)
    traded = pd.Series(0.0, index=pos.index)
    for t in weights.index:
        if t not in pos.index:
            continue
        tr = (weights.loc[t, pos.columns] - h.loc[t] * (1 + ret.loc[t])).abs()
        bp = pd.Series({s: tier_bp(s, t.year) for s in pos.columns}).fillna(0.0) * cost_mult
        cost[t] = -float((tr * bp).sum() / 1e4)
        traded[t] = float(tr.sum())
    d = result.daily
    d["price"], d["funding"], d["cost"], d["traded"] = price, fin, cost, traded
    d["total"] = d["price"] + d["funding"] + d["cost"] + d["liquidation"]
    return result


def run(period, variant="base", cost_bp=None, delay=0, open_test=False, cost_mult=COST_MULT):
    """One run of the frozen configuration. cost_bp is unused (tiers by name and year); cost_mult scales them."""
    if period == "test":
        if not open_test:
            raise SystemExit("The sealed period is opened only by the lab runner, approved by the user.")
        start, end = TEST_START, None
    else:
        start, end = PERIODS[period]
    daily, tbill = _inputs(open_test)
    days = [t for t in rebalance_days(daily["date"].unique()) if pd.Timestamp(start) <= t and (end is None or t <= pd.Timestamp(end))]
    w = build_weights(daily, tbill, days, variant)
    if delay:
        w = delay_test(w, delay)
    bars = daily.assign(high=daily["adj_close"], low=daily["adj_close"], close=daily["adj_close"])
    result = backtest(w, bars, None, cost_bp=0.0, leverage=None, end=end)
    result = settle(result, daily, tbill, w, cost_mult)
    name = variant + (f"-delay{delay}" if delay else "") + (f"-cost{cost_mult:g}x" if cost_mult != 1 else "")
    folder, s = save_run(NAME, period, name, result, params={"cost_mult": cost_mult, "delay": delay}, code_file=__file__)
    # trading-day figures (the lab summary annualises calendar days, weekends included)
    d = result.daily
    d = d.loc[d.index >= result.trades.index.min()]
    d = d[d.index.isin(pd.DatetimeIndex(daily["date"].unique()))]
    sh = lambda r: float(r.mean() / r.std() * np.sqrt(252))
    gross = d["price"] + d["funding"]
    s.update({"gross_sharpe_td": round(sh(gross), 3), "net_sharpe_td": round(sh(d["total"]), 3),
              "net_t_td": round(sh(d["total"]) * np.sqrt(len(d) / 252), 2), "years_td": round(len(d) / 252, 2),
              "vol_td_pct": round(float(d["total"].std() * np.sqrt(252) * 100), 2)})
    (folder / "summary.json").write_text(json.dumps(s, indent=2))
    return folder, s


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--period", choices=list(PERIODS), required=True)
    ap.add_argument("--variant", choices=VARIANTS, default="base")
    ap.add_argument("--cost-mult", type=float, default=COST_MULT)
    ap.add_argument("--check-lookahead", action="store_true")
    ap.add_argument("--delay", type=int, default=0)
    a = ap.parse_args()
    if a.check_lookahead:
        start, end = PERIODS[a.period]
        daily, tbill = _inputs()
        days = [t for t in rebalance_days(daily["date"].unique()) if pd.Timestamp(start) <= t <= pd.Timestamp(end)]
        truncation_test(build_weights, daily, tbill, days, variant=a.variant)
        return
    folder, s = run(a.period, a.variant, delay=a.delay, cost_mult=a.cost_mult)
    print(folder)
    for k, v in s.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()
