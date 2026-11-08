"""
Crypto Low-MAX Long Leg: built from Pass 1 v2 of vault/2 Strategies/Pipeline/Crypto Low-MAX Long Leg/.

Long the 6 perps with the lowest 7-day maximum daily return (of the top 30 by volume, BTC out), short the
equal-weight universe at the 90-day beta of the leg, 20% vol target, weekly. The file decides the weights;
the lab loads, builds the universe, runs the P&L and saves.

    poetry run python strategies/crypto_low_max_long_leg.py --period train --variant base
    poetry run python strategies/crypto_low_max_long_leg.py --period train --variant base --check-lookahead
"""
import argparse, json, sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lab.backtest import backtest            # noqa: E402
from lab.checks import delay_test, truncation_test   # noqa: E402
from lab.data import load                    # noqa: E402
from lab.runs import save_run                # noqa: E402
from lab.universe import crypto_universe     # noqa: E402

NAME = "Crypto Low-MAX Long Leg"

# 1.10 periods
TRAIN = ("2021-01-01", "2023-12-31")
VALIDATION = ("2024-01-01", "2024-12-31")
TEST_START = "2025-01-01"                    # never read here: lab.data.load cuts before it

# 1.4 universe (Data check: min_names=30; BTC dropped after the ranking, issue 2)
TOP, VOLUME_WINDOW, MIN_AGE, MIN_NAMES = 30, 30, 60, 30
EXCLUDE = ["BTCUSDT"]

# 1.5 / 1.5b base version
MAX_WINDOW = 7                               # 1.5 signal: highest daily return of the last 7 days
QUINTILE = 0.2                               # 1.5 entry: bottom quintile (6 coins of 29), equal weight
BETA_WINDOW = 90                             # 1.5b
BETA_CLIP = (0.5, 1.5)                       # 1.5b
MIN_LEG = 5                                  # 1.5b min names in leg, else flat
VOL_TARGET = 0.20                            # 1.5 book
VOL_WINDOW = 60                              # 1.5b settled: past 60 daily returns of the current weights
GROSS_CAP = 2.0                              # 1.5b
COST_BP = 5.0                                # 1.7 central case
BAND = 0.0                                   # none in Pass 1
LEVERAGE = None                              # Pass 1 gives no per-position leverage (assumption A5): no liquidation check

VARIANTS = ["base"]


def rebalance_days(calendar):
    """1.5b: formation on the Monday 00:00 UTC close (the Sunday bar), fill at the Tuesday 00:00 close:
    the weight is dated Monday and trades at the close of Monday."""
    return [d for d in calendar if d.dayofweek == 0]


def build_weights(daily, funding, days, variant="base"):
    """Weights per Monday, in units of capital, using only data up to the close of the Sunday before."""
    universe = crypto_universe(daily, top=TOP, volume_window=VOLUME_WINDOW, min_age_days=MIN_AGE, min_names=MIN_NAMES)
    universe = universe.drop(columns=[c for c in EXCLUDE if c in universe.columns])
    px = daily.pivot(index="date", columns="symbol", values="mark_close").sort_index().asfreq("D")
    ret = px.pct_change(fill_method=None)
    rows = {}
    for d in days:
        d = pd.Timestamp(d)
        f = d - pd.Timedelta(days=1)                                 # formation bar: Sunday, closes Monday 00:00 UTC
        if f not in universe.index:
            continue
        members = [s for s in universe.columns if universe.loc[f, s]]
        if not members:
            continue
        win = ret.loc[f - pd.Timedelta(days=MAX_WINDOW - 1):f, members]
        full = win.notna().all()
        elig = sorted(win.columns[full])                             # all 7 returns, else out; symbol order for ties
        k = int(np.floor(QUINTILE * len(elig) + 0.5))
        if k < MIN_LEG:
            continue
        mx = win[elig].max().sort_values(kind="stable")              # stable sort on symbol-ordered index: ties by symbol
        leg = list(mx.index[:k])
        hist = ret.loc[f - pd.Timedelta(days=BETA_WINDOW - 1):f]
        y, x = hist[leg].mean(axis=1), hist[members].mean(axis=1)
        m = y.notna() & x.notna()
        if m.sum() < 30 or x[m].var() == 0:
            continue
        beta = float(np.clip(np.cov(y[m], x[m])[0, 1] / x[m].var(), *BETA_CLIP))
        unit = pd.Series(0.0, index=px.columns)
        unit[leg] += 1.0 / k
        unit[members] -= beta / len(members)
        vh = ret.loc[f - pd.Timedelta(days=VOL_WINDOW - 1):f].fillna(0.0) @ unit
        vol = float(vh.std() * np.sqrt(365))
        if vol <= 0:
            continue
        scale = min(VOL_TARGET / vol, GROSS_CAP / unit.abs().sum())
        rows[d] = unit * scale
    return pd.DataFrame(rows).T.reindex(columns=px.columns).fillna(0.0)


PERIODS = {"train": TRAIN, "validation": VALIDATION, "train+validation": (TRAIN[0], VALIDATION[1])}


def run(period, variant="base", cost_bp=COST_BP, delay=0, open_test=False):
    """One run of the frozen configuration."""
    if period == "test":
        if not open_test:
            raise SystemExit("The sealed period is opened only by the lab runner, approved by the user.")
        start, end = TEST_START, None
    else:
        start, end = PERIODS[period]
    daily = load("crypto_daily", test_start=TEST_START, open_test=open_test)
    funding = load("crypto_funding", test_start=TEST_START, open_test=open_test)
    calendar = pd.date_range(daily["date"].min(), daily["date"].max(), freq="D")
    days = [d for d in rebalance_days(calendar) if pd.Timestamp(start) <= d and (end is None or d <= pd.Timestamp(end))]
    w = build_weights(daily, funding, days, variant)
    if delay:
        w = delay_test(w, delay)
    result = backtest(w, daily, funding, cost_bp=cost_bp, band=BAND, leverage=LEVERAGE, end=end)
    name = variant + (f"-delay{delay}" if delay else "") + (f"-cost{cost_bp:g}bp" if cost_bp != COST_BP else "")
    folder, s = save_run(NAME, period, name, result, params={"cost_bp": cost_bp, "delay": delay}, code_file=__file__)
    # gate figures: price only, net of cost, funding excluded (1.11)
    d = result.daily.loc[result.daily.index >= result.trades.index.min()]
    po = d["price"] + d["cost"] + d["liquidation"]
    sh = float(po.mean() / po.std() * np.sqrt(365))
    pg = d["price"]
    # held name-days with no funding print (Data check #3): booked as 0 by the engine, flagged here
    pos = result.positions
    f = funding[funding["time"] >= pd.Timestamp(start)].copy()
    f["day"] = (f["time"] - pd.Timedelta(microseconds=1)).dt.floor("D")
    have = set(zip(f["symbol"], f["day"]))
    miss = sum(1 for t in pos.index for c in pos.columns if pos.loc[t, c] != 0 and (c, t) not in have)
    s.update({"price_only_net_sharpe": round(sh, 3), "price_only_gross_sharpe": round(float(pg.mean() / pg.std() * np.sqrt(365)), 3),
              "price_only_net_t": round(sh * np.sqrt(len(po) / 365), 2), "years": round(len(po) / 365, 2),
              "held_days_without_funding_print": int(miss)})
    (folder / "summary.json").write_text(json.dumps(s, indent=2))
    return folder, s


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--period", choices=list(PERIODS), required=True)
    ap.add_argument("--variant", choices=VARIANTS, default="base")
    ap.add_argument("--cost-bp", type=float, default=COST_BP)
    ap.add_argument("--check-lookahead", action="store_true")
    ap.add_argument("--delay", type=int, default=0)
    a = ap.parse_args()
    if a.check_lookahead:
        start, end = PERIODS[a.period]
        daily = load("crypto_daily", test_start=TEST_START)
        funding = load("crypto_funding", test_start=TEST_START)
        calendar = pd.date_range(daily["date"].min(), daily["date"].max(), freq="D")
        days = [d for d in rebalance_days(calendar) if pd.Timestamp(start) <= d <= pd.Timestamp(end)]
        truncation_test(build_weights, daily, funding, days, variant=a.variant)
        return
    folder, s = run(a.period, a.variant, cost_bp=a.cost_bp, delay=a.delay)
    print(folder)
    for k, v in s.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()
