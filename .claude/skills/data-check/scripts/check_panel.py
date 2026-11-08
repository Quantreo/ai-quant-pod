"""
Generic checks on one dataset of the desk: the mechanical part of a data check.

    poetry run python .claude/skills/data-check/scripts/check_panel.py crypto_daily --until 2025-01-01
    poetry run python .claude/skills/data-check/scripts/check_panel.py crypto_daily --since 2025-01-01 --coverage-only

--until  checks the data strictly before this date (the start of the strategy's test period)
--since  with --coverage-only: counts rows and names in the test period, nothing else (no prices, no returns)
--symbols  restricts to a comma-separated list

Each line says OK or WARN, with counts and the worst cases. WARN is not a verdict: the agent decides what
it means for the strategy, with reference/checks.md.
"""
import argparse, sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
from lab.data import DATASETS                                         # noqa: E402

PRICE_COLS = {"crypto_daily": ["open", "high", "low", "close", "mark_open", "mark_high", "mark_low", "mark_close"],
              "fx_daily": ["close"],
              "fx_hourly": [f"{s}_{f}" for s in ["bid", "ask"] for f in ["open", "high", "low", "close"]]}
JUMP = {"crypto_daily": 0.8, "fx_daily": 0.05, "fx_hourly": 0.03}       # one-bar move worth listing
FREQ = {"crypto_daily": "D", "fx_daily": "B", "fx_hourly": "h", "rates": "MS"}


def line(ok, text, worst=None):
    print(f"{'OK  ' if ok else 'WARN'} {text}" + (f" | worst: {worst}" if worst else ""))


def top(s, n=5):
    return ", ".join(f"{k} {v}" for k, v in s.head(n).items())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dataset", choices=sorted(DATASETS))
    ap.add_argument("--until")
    ap.add_argument("--since")
    ap.add_argument("--symbols")
    ap.add_argument("--coverage-only", action="store_true")
    a = ap.parse_args()

    path, tcol, key = DATASETS[a.dataset]
    name_col = key[0]
    f = ROOT / path
    if not f.exists():
        print(f"MISSING {path}: run the download script (data/README.md)")
        return
    df = pd.read_parquet(f)
    if a.symbols:
        df = df[df[name_col].isin(a.symbols.split(","))]
    if a.until:
        df = df[df[tcol] < pd.Timestamp(a.until)]
    if a.since:
        df = df[df[tcol] >= pd.Timestamp(a.since)]
    print(f"# {a.dataset}: {len(df):,} rows, {df[name_col].nunique()} names, {df[tcol].min()} to {df[tcol].max()}")

    by_year = df.groupby(df[tcol].dt.year).agg(rows=(tcol, "size"), names=(name_col, "nunique"))
    print("Coverage by year: " + "; ".join(f"{y}: {r.rows:,} rows, {r.names} names" for y, r in by_year.iterrows()))
    if a.coverage_only:
        return

    # structure
    num = df.select_dtypes("number")
    nan = df.isna().sum()
    nan = nan[nan > 0]
    line(nan.empty, f"missing values: {int(nan.sum()):,}", top(nan.sort_values(ascending=False)))
    inf = np.isinf(num).sum()
    inf = inf[inf > 0]
    line(inf.empty, f"infinite values: {int(inf.sum()):,}", top(inf))
    dup = df.duplicated(key).sum()
    line(dup == 0, f"duplicated keys {key}: {dup:,}")
    back = (df.groupby(name_col)[tcol].diff() <= pd.Timedelta(0)).sum()
    line(back == 0, f"time going backwards within a {name_col}: {back:,} rows (sort by {', '.join(key)} before any rolling window)")

    # prices
    cols = [c for c in PRICE_COLS.get(a.dataset, []) if c in df]
    if cols:
        bad = (df[cols] <= 0).any(axis=1)
        line(not bad.any(), f"zero or negative prices: {int(bad.sum()):,}", top(df[bad][name_col].value_counts()))
        for side in ["", "mark_", "bid_", "ask_"]:
            o, h, l, c = (f"{side}{x}" for x in ["open", "high", "low", "close"])
            if all(x in df for x in [o, h, l, c]):
                inc = (df[h] < df[[o, c]].max(axis=1)) | (df[l] > df[[o, c]].min(axis=1)) | (df[h] < df[l])
                line(not inc.any(), f"inconsistent {side or 'mid '}bars (high below open/close, low above): {int(inc.sum()):,}")
        if {"bid_close", "ask_close"} <= set(df):
            neg = df["ask_close"] < df["bid_close"]
            line(not neg.any(), f"ask below bid at the close: {int(neg.sum()):,}")
        pc = "close" if "close" in df else "bid_close"
        d = df.sort_values(key)
        ret = d.groupby(name_col)[pc].pct_change()
        big = d.assign(ret=ret)[ret.abs() > JUMP[a.dataset]].sort_values("ret", key=abs, ascending=False)
        line(big.empty, f"one-bar moves above {JUMP[a.dataset]:.0%}: {len(big):,}",
             ", ".join(f"{r[name_col]} {r[tcol]:%Y-%m-%d} {r.ret:+.0%}" for _, r in big.head(5).iterrows()))
        flat = d.groupby(name_col)[pc].transform(lambda s: s.groupby((s != s.shift()).cumsum()).transform("size"))
        runs = d[flat >= 5].groupby(name_col).size().sort_values(ascending=False)
        line(runs.empty, f"names with the price unchanged 5 bars or more in a row: {len(runs)}", top(runs))

    # volume
    vc = [c for c in ["quote_volume", "volume", "bid_volume"] if c in df]
    if vc:
        z = df[df[vc[0]] <= 0]
        line(z.empty, f"bars with zero volume: {len(z):,} in {z[name_col].nunique()} names", top(z[name_col].value_counts()))

    # gaps inside each name's span
    if a.dataset in FREQ:
        miss = {}
        for s, x in df.groupby(name_col):
            t = pd.DatetimeIndex(x[tcol])
            full = pd.date_range(t.min(), t.max(), freq=FREQ[a.dataset])
            if a.dataset == "fx_hourly":
                full = full[full.dayofweek < 5]
            n = len(full.difference(t))
            if n:
                miss[s] = n
        miss = pd.Series(miss, dtype=int).sort_values(ascending=False)
        line(miss.empty, f"names with missing {FREQ[a.dataset]} bars inside their span: {len(miss)}, {int(miss.sum()):,} bars", top(miss))

    # funding
    if a.dataset == "crypto_funding":
        iv = df["interval_hours"].value_counts(dropna=False)
        odd = iv[~iv.index.isin([1, 2, 4, 8])]
        line(odd.empty, "funding intervals (hours): " + ", ".join(f"{k}: {v:,}" for k, v in iv.items()))
        changed = df.groupby(name_col)["interval_hours"].nunique()
        print(f"INFO names whose funding interval changed: {int((changed > 1).sum())}")
        ext = df[df["rate"].abs() > 0.01]
        line(ext.empty, f"prints above 1% in absolute value: {len(ext):,}", top(ext[name_col].value_counts()))
        per_day = df.groupby([name_col, df[tcol].dt.normalize()]).agg(n=("rate", "size"), iv=("interval_hours", "min"))
        wrong = per_day[per_day["n"] > 24 / per_day["iv"]]
        line(wrong.empty, f"days with more prints than the interval allows: {len(wrong):,}")
    if "funding_prints" in df:
        nf = df[df["funding_prints"] == 0]
        line(nf.empty, f"days with a price but no funding print: {len(nf):,} in {nf[name_col].nunique()} names", top(nf[name_col].value_counts()))

    # stale series
    if a.dataset == "rates":
        last = df.groupby(name_col)[tcol].max()
        stale = last[last < last.max() - pd.DateOffset(months=3)]
        line(stale.empty, f"series that stop more than 3 months before the others: {len(stale)}",
             ", ".join(f"{k} {v:%Y-%m}" for k, v in stale.items()))


if __name__ == "__main__":
    main()
