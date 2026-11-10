"""
ETF TSMOM 12-Month: built from Pass 1 v1 (short) of vault/2 Strategies/Pipeline/ETF TSMOM 12-Month/Pass 1.md and its Data check.

Month-end book on 22 ETFs (SHY out): long the ETFs whose own 12-month excess return is positive, short the others, sized
s_i / sigma_i (EWMA com 60), scaled to 8% ex-ante vol (261-day covariance), gross cap 2. Excess return = adj_close return
minus cash (FRED TB3MS, Data check #1: signal uses cash months up to m-1). The P&L is the excess return: each position
is financed (long) or credited (short) at the T-bill rate, through the engine's funding path; shorts also pay a borrow fee.

Variants: base; control_long (all signs +1, same sizing); control_twin (every ETF takes the sign of the equal-risk basket's
12-month excess return): the two same-sized controls, reported as labels at the gate (Pass 1 1.11), never a kill there.
stress13 / stress9 (Data check #3) and A belong to the validation phase: not run at the gate.

    poetry run python strategies/etf_tsmom_12m.py --check-lookahead
    poetry run python strategies/etf_tsmom_12m.py --gate        # base + two controls (train), then the level gate and the labels

Costs per ETF by tier (1.5, Cost Assumptions): the engine has one cost_bp, so one engine run per tier group, added
(the engine is linear per name, no band), as FX Value did. Never a blended average.
"""
import argparse, json, sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lab.backtest import Result, backtest      # noqa: E402
from lab.checks import delay_test, truncation_test   # noqa: E402
from lab.data import ROOT, load                # noqa: E402
from lab.runs import save_run                  # noqa: E402

NAME = "ETF TSMOM 12-Month"

# 1.10 periods: train scored from 2006-01 (first rebalance 2006-01-31); validation 2018-2020
TRAIN = ("2006-01-01", "2017-12-31")
VALIDATION = ("2018-01-01", "2020-12-31")
TEST_START = "2021-01-01"                      # never read here: lab.data.load and the cash cut stop before it

# 1.4 universe: the 23 ETFs minus SHY; an ETF enters when it has a price at the month end 12 months back
EXCLUDE = ["SHY"]
LIQUID = ["SPY", "QQQ", "IWM", "EFA", "EEM", "TLT", "IEF", "LQD", "HYG", "GLD"]    # 1.5 / Cost Assumptions: 2 bp (SHY out)
LIQUID_BP, OTHER_BP = 2.0, 5.0                 # 1.5 Costs, one way
LOOKBACK_MONTHS = 12                           # 1.5 Signal, no skip
STRESS13_BEFORE = "2005-01-31"                 # Data check #3: 13 ETFs with a price from 2005-01
MIN_NAMES = 2                                  # not in Pass 1; only to compute a covariance (base has 13+ names)

# 1.5 / 1.5b base version
EWMA_COM = 60                                  # 1.5 Sizing
COV_WINDOW = 261                               # 1.5 Book
COV_MIN_OBS = 240                              # not in Pass 1: pairwise covariance needs this many common days
VOL_TARGET, GROSS_CAP = 0.08, 2.0              # 1.5 / 1.5b
PPY = 252                                      # annualisation of volatility
BORROW = 0.0025                                # 1.5 Borrow: 25 bp a year on short gross, all ETFs (Cost Assumptions), /365

VARIANTS = ["base", "control_long", "control_twin", "stress13", "stress9", "A"]
# 1.4 / 1.9 classes (VNQ counts with equities: equities 9, bonds 5, commodities 5, FX 3)
CLASS = {**{c: "equity" for c in "SPY QQQ IWM EFA EEM EWJ VGK FXI VNQ".split()}, **{c: "bonds" for c in "TLT IEF LQD HYG TIP".split()},
         **{c: "commodities" for c in "GLD SLV DBC USO DBA".split()}, **{c: "fx" for c in "UUP FXE FXY".split()}}

# 1.11 gate
SCORED_FIRST_MONTH = "2006-02"                 # month of the first scored return (the first trade is 2006-01-31)
T_BAR = 2.0                                    # level gate: t 2, the train is over 5 years (method 1.11)


# ---------------------------------------------------------------- data
def etf_bars(open_test=False):
    d = load("etf_daily", test_start=TEST_START, open_test=open_test)
    d = d[d["symbol"].isin(list(CLASS)) & ~d["symbol"].isin(EXCLUDE)]   # 1.4: the 22 ETFs only (etf_daily holds more)
    return pd.DataFrame({"date": d["date"], "symbol": d["symbol"], "close": d["adj_close"], "high": d["adj_close"],
                         "low": d["adj_close"]}).reset_index(drop=True)


def cash_table(open_test=False):
    """Data check #1: monthly mean of TB3MS, % a year, stamped on day 1 of its month. 'time' = when the month's mean
    is known: day 1 of the next month (so the truncation test cuts it right)."""
    t = pd.read_parquet(ROOT / "data/rates/tbill.parquet")
    if not open_test:
        t = t[t["date"] < pd.Timestamp(TEST_START)]
    t = t.sort_values("date")
    return pd.DataFrame({"month": t["date"].to_numpy(), "rate": t["rate"].to_numpy(),
                         "time": (t["date"] + pd.DateOffset(months=1)).to_numpy()})


def cash_prints(cash, symbols, start, end):
    """Engine funding prints: the T-bill rate of the bar's month, per calendar day (/365), for every symbol. A long
    pays it, a short collects it (excess-return book)."""
    days = pd.date_range(start, end, freq="D")
    r = cash.set_index("month")["rate"]
    rate = r.reindex(days.to_period("M").to_timestamp()).to_numpy() / 100 / 365
    assert not np.isnan(rate).any(), "cash missing in the run window"
    return pd.DataFrame({"symbol": np.repeat(symbols, len(days)), "time": np.tile(days + pd.Timedelta(days=1), len(symbols)),
                         "rate": np.tile(rate, len(symbols))})


def cash_12m(cash, k_date):
    """Data check #1: 12-month cash return for a signal at the end of month m = the 12 monthly means of months m-12..m-1
    (compounded rate/12). Only rows known by k_date (time <= k_date) are used."""
    m = pd.Timestamp(k_date).to_period("M").to_timestamp()
    c = cash[(cash["month"] >= m - pd.DateOffset(months=LOOKBACK_MONTHS)) & (cash["month"] < m)]
    assert len(c) == LOOKBACK_MONTHS and (c["time"] <= pd.Timestamp(k_date)).all()
    return float(np.prod(1 + c["rate"].to_numpy() / 1200) - 1)


def rebalance_days(price_days, start, end):
    """1.5 Rebalance: the last trading day of each month in [start, end), SPY-like calendar of the file. A rebalance on the
    last day of the period would earn nothing: left out."""
    s = pd.Series(pd.DatetimeIndex(sorted(set(price_days))))
    me = s.groupby(s.dt.to_period("M")).max()
    return [d for d in me if pd.Timestamp(start) <= d < pd.Timestamp(end)]


# ---------------------------------------------------------------- weights
def build_weights(bars, cash, days, variant="base"):
    """Weights of the ETFs per month-end d, in units of capital, with data up to the close of d (cash up to month m-1)."""
    px = bars.pivot(index="date", columns="symbol", values="close").sort_index()
    ret = px.pct_change(fill_method=None)
    vol = ret.ewm(com=EWMA_COM, min_periods=EWMA_COM).std() * np.sqrt(PPY)
    first = px.apply(lambda s: s.first_valid_index())
    idx = pd.Series(px.index, index=px.index)
    me = idx.groupby(idx.dt.to_period("M")).max()                     # month-end trading days present in the data
    px_f = px.ffill()
    rows = {}
    for d in days:
        d = pd.Timestamp(d)
        k = d.to_period("M")
        if k not in me.index or me[k] != d or (k - LOOKBACK_MONTHS) not in me.index:
            continue
        d0 = me[k - LOOKBACK_MONTHS]
        mem = [c for c in px.columns if pd.notna(first[c]) and first[c] <= d0 and pd.notna(px.at[d, c])
               and np.isfinite(vol.at[d, c]) and vol.at[d, c] > 0]
        if variant == "stress13":
            mem = [c for c in mem if first[c] <= pd.Timestamp(STRESS13_BEFORE)]
        elif variant == "stress9":
            mem = [c for c in mem if first[c] > pd.Timestamp(STRESS13_BEFORE)]
        if len(mem) < MIN_NAMES:
            continue
        exc = px_f.loc[d, mem] / px_f.loc[d0, mem] - 1 - cash_12m(cash, d)
        if variant == "control_long":
            s = np.ones(len(mem))
        elif variant == "control_twin":
            iv = 1 / vol.loc[d, mem]
            s = np.sign(float((iv / iv.sum() * exc).sum())) * np.ones(len(mem))
        else:
            s = np.sign(exc.to_numpy())
        w = s / vol.loc[d, mem].to_numpy()
        if variant == "A":                                            # 1.9 A: equal risk per class alive, 1/sigma within
            n_c = pd.Series([CLASS[c] for c in mem]).map(pd.Series([CLASS[c] for c in mem]).value_counts()).to_numpy()
            w = w / n_c
        if not (w != 0).any():
            continue
        R = ret.loc[:d, mem].iloc[-COV_WINDOW:]
        cov = R.cov(min_periods=COV_MIN_OBS).to_numpy() * PPY
        ex_ante = float(np.sqrt(w @ cov @ w)) if np.isfinite(cov).all() else np.nan
        assert np.isfinite(ex_ante) and ex_ante > 0, f"covariance problem at {d.date()}"
        w = w * VOL_TARGET / ex_ante
        gross = np.abs(w).sum()
        if gross > GROSS_CAP:
            w = w * GROSS_CAP / gross
        rows[d] = pd.Series(w, index=mem)
    if not rows:
        return pd.DataFrame(columns=list(px.columns))
    return pd.DataFrame(rows).T.reindex(columns=list(px.columns))


# ---------------------------------------------------------------- engine, costs by tier, borrow
def tiered_backtest(w, bars, cash, end, borrow_rate=BORROW, cost_mult=1.0):
    cols = [c for c in w.columns if (w[c] != 0).any()]
    tier = {c: (LIQUID_BP if c in LIQUID else OTHER_BP) * cost_mult for c in cols}
    parts, traded = [], {}
    for bp in sorted(set(tier.values())):
        g = [c for c in cols if tier[c] == bp]
        fund = cash_prints(cash, g, w.index.min(), end)
        parts.append(backtest(w[g], bars, fund, cost_bp=bp, band=0.0, leverage=None, end=end))
        traded[f"{bp:g}bp"] = float(parts[-1].daily["traded"].sum())
    assert all(p.daily.index.equals(parts[0].daily.index) for p in parts)
    daily = sum(p.daily for p in parts)
    trades = parts[0].trades.copy()
    for col in ["traded", "gross", "net", "names_long", "names_short"]:
        trades[col] = sum(p.trades[col] for p in parts)
    pos = pd.concat([p.positions for p in parts], axis=1)
    # borrow: BORROW a year on short gross, per calendar day, charged as a cost
    short = (-pos.clip(upper=0.0))
    borrow = short * borrow_rate / 365
    daily["cost"] = daily["cost"] - borrow.sum(axis=1).reindex(daily.index).fillna(0.0)
    daily["total"] = daily[["price", "funding", "cost", "liquidation"]].sum(axis=1)
    by_name = pd.concat([p.by_name for p in parts])
    by_name["cost"] = by_name["cost"] - borrow.sum().reindex(by_name.index)
    notes = dict(parts[0].notes); notes["cost_bp"] = {"liquid": LIQUID_BP * cost_mult, "others": OTHER_BP * cost_mult}
    res = Result(daily=daily, positions=pos, trades=trades, liquidations=pd.concat([p.liquidations for p in parts], ignore_index=True),
                 by_name=by_name, notes=notes)
    return res, tier, traded, float(borrow.sum().sum())


PERIODS = {"train": TRAIN, "validation": VALIDATION, "train+validation": (TRAIN[0], VALIDATION[1])}


def monthly_net(result):
    d = result.daily.loc[result.trades.index.min():, "total"]
    m = d.groupby(d.index.to_period("M")).sum()
    m.iloc[1] += m.iloc[0]                       # the entry cost of the first trade day goes to the first scored month
    return m.iloc[1:]


def run(period, variant="base", cost_bp=None, delay=0, open_test=False, borrow_rate=BORROW, cost_mult=1.0):
    """One run of the frozen configuration. cost_bp must stay None: costs are the tiers of 1.5."""
    assert cost_bp is None, "costs are per tier (1.5); a stress is a validation-phase decision"
    if period == "test":
        if not open_test:
            raise SystemExit("The test period is opened only by lab/run_test.py, by the user.")
        start, end = TEST_START, None
    else:
        start, end = PERIODS[period]
    bars, cash = etf_bars(open_test), cash_table(open_test)
    price_days = pd.DatetimeIndex(sorted(bars["date"].unique()))
    end_ts = pd.Timestamp(end) if end else price_days.max()
    days = rebalance_days(price_days, start, end_ts)
    w = build_weights(bars, cash, days, variant)
    if delay:
        # 1.5b delay stress: signal at close d, trade at the next trading close. lab delay_test shifts calendar days
        # (weekend dates, run 103909 turnover 14), so the shift is on the price calendar here.
        pos = price_days.searchsorted(w.index) + delay
        w = w.set_axis(price_days[np.minimum(pos, len(price_days) - 1)])
    res, tier, traded, borrow = tiered_backtest(w, bars, cash, end_ts, borrow_rate, cost_mult)
    m = monthly_net(res)
    names = w.notna().sum(axis=1)
    name = variant + (f"-delay{delay}" if delay else "") + (f"-borrow{borrow_rate*1e4:g}bp" if borrow_rate != BORROW else "") + (f"-costx{cost_mult:g}" if cost_mult != 1 else "")
    years = len(res.daily.loc[res.trades.index.min():]) / 365
    params = {"tiers_bp": tier, "turnover_per_year_by_tier": {k: round(v / years, 2) for k, v in traded.items()},
              "borrow_cost_pct": round(borrow * 100, 3), "borrow_rate": borrow_rate, "cost_mult": cost_mult, "vol_target": VOL_TARGET, "gross_cap": GROSS_CAP,
              "first_trade": str(w.index.min().date()), "last_trade": str(w.index.max().date()),
              "rebalances": int(len(w)), "scored_months": int(len(m)), "first_scored_month": str(m.index.min()),
              "names_min": int(names.min()), "names_max": int(names.max()),
              "gross_mean": round(float(w.abs().sum(axis=1).mean()), 3), "gross_max": round(float(w.abs().sum(axis=1).max()), 3),
              "cap_binding": int((w.abs().sum(axis=1) > GROSS_CAP - 1e-9).sum())}
    folder, s = save_run(NAME, period, name, res, params=params, code_file=__file__)
    m.rename("net").to_frame().to_parquet(folder / "monthly.parquet")
    w.to_parquet(folder / "weights.parquet")
    return folder, s, params


# ---------------------------------------------------------------- train gate, Pass 1 1.11
def nw_ols(y, X, lags):
    """OLS y = a + X b with Newey-West (Bartlett) standard errors; t of the intercept."""
    X = np.column_stack([np.ones(len(y)), X])
    b = np.linalg.lstsq(X, y, rcond=None)[0]
    e = y - X @ b
    XtXi = np.linalg.inv(X.T @ X)
    u = X * e[:, None]
    S = u.T @ u
    for L in range(1, lags + 1):
        G = u[L:].T @ u[:-L]
        S += (1 - L / (lags + 1)) * (G + G.T)
    V = XtXi @ S @ XtXi
    return {"alpha_m": float(b[0]), "betas": [float(x) for x in b[1:]], "t_nw": float(b[0] / np.sqrt(V[0, 0]))}


def gate(f_base, f_long, f_twin):
    mo = {k: pd.read_parquet(Path(f) / "monthly.parquet")["net"] for k, f in [("b", f_base), ("l", f_long), ("t", f_twin)]}
    j = pd.concat(mo, axis=1).dropna()
    n = len(j)
    lags = int(np.floor(4 * (n / 100) ** (2 / 9)))                  # standard Newey-West rule; Pass 1 gives no lag
    y = j["b"].to_numpy()
    labels = {"n_months": n, "lags": lags,
          "on_always_long": nw_ols(y, j[["l"]].to_numpy(), lags), "on_twin": nw_ols(y, j[["t"]].to_numpy(), lags),
          "on_both": nw_ols(y, j[["l", "t"]].to_numpy(), lags)}
    labels["t_lag1"] = {k: nw_ols(y, j[c].to_numpy(), 1)["t_nw"] for k, c in [("always_long", ["l"]), ("twin", ["t"]), ("both", ["l", "t"])]}
    years = n / 12
    sh = float(y.mean() / y.std(ddof=1) * np.sqrt(12))
    level = {"scored_start": str(j.index.min()), "scored_end": str(j.index.max()), "n_months": n, "years": round(years, 3),
          "net_sharpe_monthly": round(sh, 3), "t": round(sh * np.sqrt(years), 2), "sharpe_bar": round(T_BAR / np.sqrt(years), 3)}
    level["pass"] = bool(level["t"] >= T_BAR)                       # the only kill at the gate; labels are reported
    return level, labels


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--period", choices=list(PERIODS), default="train")
    ap.add_argument("--variant", choices=VARIANTS, default="base")
    ap.add_argument("--check-lookahead", action="store_true", help="truncation test only, no run")
    ap.add_argument("--delay", type=int, default=0, help="control, validation phase")
    ap.add_argument("--cost-mult", type=float, default=1.0, help="stress, 1.9: costs 2x")
    ap.add_argument("--borrow", type=float, default=BORROW, help="stress, 1.9: borrow 1% = 0.01")
    ap.add_argument("--gate", action="store_true", help="base + control_long + control_twin on train, then the level gate and the labels")
    a = ap.parse_args()
    start, end = PERIODS[a.period]
    if a.check_lookahead:
        bars, cash = etf_bars(), cash_table()
        pdays = pd.DatetimeIndex(sorted(bars["date"].unique()))
        for v in ["base", "control_twin", "A"]:
            truncation_test(build_weights, bars, cash, rebalance_days(pdays, start, end), n=20, variant=v)
        return
    if a.gate:
        out = {}
        for v in ["base", "control_long", "control_twin"]:
            folder, s, p = run("train", v)
            out[v] = folder
            print(v, folder.name, {k: s[k] for k in ["gross_sharpe", "net_sharpe", "turnover_per_year", "net_vol_pct", "max_drawdown_pct"]})
            print("  ", p)
        level, labels = gate(out["base"], out["control_long"], out["control_twin"])
        (out["base"] / "gate.json").write_text(json.dumps({"level": level, "labels": labels}, indent=2))
        print("LEVEL", json.dumps(level)); print("LABELS", json.dumps(labels))
        return
    folder, s, p = run(a.period, a.variant, delay=a.delay, borrow_rate=a.borrow, cost_mult=a.cost_mult)
    print(folder); print(s); print(p)


if __name__ == "__main__":
    main()
