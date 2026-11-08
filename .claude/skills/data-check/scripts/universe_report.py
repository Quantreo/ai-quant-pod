"""
The point-in-time universe of a crypto strategy, with the parameters of its Pass 1, before any code is written.

    poetry run python .claude/skills/data-check/scripts/universe_report.py --top 30 --volume-window 30 \
        --min-age 90 --min-names 20 --rebalance MON --test-start 2025-01-01

It calls lab.universe.crypto_universe, the same function the Developer will call, on data before the test
period, and prints what the strategy will trade: names per rebalance, weeks too thin to trade, how many names
enter and leave, and which names in the universe carry known data issues (relisted tickers, missing funding,
large one-day moves, missing days). It prints no return and no performance.
"""
import argparse, sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
from lab.data import load                                             # noqa: E402
from lab.universe import crypto_universe                              # noqa: E402

DAYS = {"MON": 0, "TUE": 1, "WED": 2, "THU": 3, "FRI": 4, "SAT": 5, "SUN": 6, "DAILY": None}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, required=True)
    ap.add_argument("--volume-window", type=int, default=30)
    ap.add_argument("--min-age", type=int, default=90)
    ap.add_argument("--min-names", type=int, default=0)
    ap.add_argument("--rebalance", default="MON", choices=sorted(DAYS))
    ap.add_argument("--test-start", required=True, help="start of the test period: nothing from it is read")
    a = ap.parse_args()

    daily = load("crypto_daily", test_start=a.test_start)
    uni = crypto_universe(daily, top=a.top, volume_window=a.volume_window, min_age_days=a.min_age, min_names=a.min_names)
    if DAYS[a.rebalance] is not None:
        uni = uni[uni.index.dayofweek == DAYS[a.rebalance]]
    size = uni.sum(axis=1)
    live = size[size > 0]
    print(f"# Universe: top {a.top} by {a.volume_window}-day volume, listed {a.min_age}+ days, min {a.min_names} names, "
          f"rebalance {a.rebalance}, data before {a.test_start}")
    print(f"Rebalances: {len(size)}, of which flat (too few names): {int((size == 0).sum())}; first traded: "
          f"{live.index.min():%Y-%m-%d}" if len(live) else "No rebalance has enough names.")
    print("Names per rebalance, by year: " + "; ".join(
        f"{y}: min {int(s.min())}, median {int(s.median())}, max {int(s.max())}, flat {int((s == 0).sum())}"
        for y, s in size.groupby(size.index.year)))

    prev = uni.shift().fillna(False).astype(bool)
    enter, leave = (uni & ~prev).sum(axis=1), (~uni & prev).sum(axis=1)
    print(f"Names entering per rebalance: mean {enter[size > 0].mean():.1f}; leaving: mean {leave[size > 0].mean():.1f}")

    members = uni.columns[uni.any()]
    print(f"Distinct names ever in the universe: {len(members)}")
    relisted = [m for m in members if "." in m]
    print(f"Relisted tickers in the universe (SYMBOL.2 ...): {len(relisted)}" + (f" ({', '.join(relisted)})" if relisted else ""))

    d = daily[daily["symbol"].isin(members)].sort_values(["symbol", "date"])
    held = uni.stack()
    held = held[held].reset_index()[["date", "symbol"]]
    d_in = d.merge(held, on=["date", "symbol"])
    nf = d_in[d_in["funding_prints"] == 0]
    print(f"Rebalance days in the universe with no funding print: {len(nf)}" + (f" ({', '.join(nf['symbol'].value_counts().head(5).index)})" if len(nf) else ""))
    d["ret"] = d.groupby("symbol")["close"].pct_change()
    d["gap"] = d.groupby("symbol")["date"].diff().dt.days
    big = d[(d["ret"].abs() > 0.8)]
    print(f"Days with a move above 80% among universe names (any day, not only held): {len(big)}" +
          (f" ({', '.join(f'{r.symbol} {r.date:%Y-%m-%d}' for r in big.head(5).itertuples())})" if len(big) else ""))
    gaps = d[d["gap"] > 1]
    print(f"Gaps of more than one day inside universe names' spans: {len(gaps)}" +
          (f" ({', '.join(f'{r.symbol} {r.date:%Y-%m-%d} after {int(r.gap)} days' for r in gaps.head(5).itertuples())})" if len(gaps) else ""))


if __name__ == "__main__":
    main()
