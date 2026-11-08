"""
Download daily FX rates for the nine majors against USD from FRED (Federal Reserve H.10, noon New York).

Builds, in data/fx/ (never committed):
    fx_daily.parquet    one row per pair and business day: date, pair, close (noon New York buying rate)
    quality_report.md   rows per year, missing weekdays, large moves, stale series

Pairs are quoted the market way: EURUSD, GBPUSD, AUDUSD, NZDUSD in dollars per unit; USDJPY, USDCHF, USDCAD,
USDNOK, USDSEK in units per dollar. One price a day, no bid and ask: costs come from
vault/Toolbox/Cost Assumptions.md. Interest rates for carry are in data/get_rates.py.

Usage, from the repository root:
    python data/get_fx_daily.py

Data source: FRED, Federal Reserve Bank of St. Louis (https://fred.stlouisfed.org), series from the Federal
Reserve's H.10 release. You download it yourself; FRED's terms of use apply.
"""
import argparse, io, time
from pathlib import Path

import pandas as pd
import requests

SERIES = {"EURUSD": "DEXUSEU", "GBPUSD": "DEXUSUK", "AUDUSD": "DEXUSAL", "NZDUSD": "DEXUSNZ", "USDJPY": "DEXJPUS",
          "USDCHF": "DEXSZUS", "USDCAD": "DEXCAUS", "USDNOK": "DEXNOUS", "USDSEK": "DEXSDUS"}
URL = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={series}"
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "fx"
START, END = "2008-01-01", "2026-09-30"          # fixed, so that every user builds the same data


def download(session, series, tries=5):
    for k in range(tries):
        try:
            r = session.get(URL.format(series=series), timeout=30)
            r.raise_for_status()
            df = pd.read_csv(io.StringIO(r.text), na_values=".")
            df.columns = ["date", "close"]                     # FRED names the first column DATE or observation_date
            return df.assign(date=pd.to_datetime(df["date"])).dropna()
        except requests.RequestException:
            time.sleep(1 + 2 * k)
    raise RuntimeError(f"failed after {tries} tries: {series}")


def quality_report(fx):
    d = fx.sort_values(["pair", "date"])
    ret = d.groupby("pair")["close"].pct_change()
    big = d.assign(ret=ret)[ret.abs() > 0.05].sort_values("ret", key=abs, ascending=False)
    days = pd.bdate_range(START, d["date"].max())
    missing = {p: len(days.difference(pd.DatetimeIndex(g["date"]))) for p, g in d.groupby("pair")}
    last = d.groupby("pair")["date"].max()
    stale = last[last < last.max() - pd.Timedelta(days=10)]
    L = [f"# Quality report: FX daily (FRED H.10, noon New York), {START} to {END}", "",
         f"- Pairs: {d['pair'].nunique()}; rows: {len(d):,}",
         "- Weekdays with no rate (US holidays, about 10 a year, are normal): " + ", ".join(f"{p} {n}" for p, n in missing.items()),
         f"- Series that stop more than 10 days before the others: {len(stale)}" + (f" ({', '.join(stale.index)})" if len(stale) else ""), "",
         f"## Daily moves above 5%: {len(big)}", ""]
    L += [f"- {r.pair} {r.date:%Y-%m-%d}: {r.ret:+.1%}" for r in big.head(20).itertuples()]
    (OUT / "quality_report.md").write_text("\n".join(L) + "\n")


def main():
    ap = argparse.ArgumentParser()
    args = ap.parse_args()

    with requests.Session() as s:
        fx = pd.concat([download(s, sid).assign(pair=p) for p, sid in SERIES.items()], ignore_index=True)
    fx = fx[(fx["date"] >= START) & (fx["date"] <= END)][["date", "pair", "close"]]
    fx = fx.sort_values(["pair", "date"]).reset_index(drop=True)
    OUT.mkdir(parents=True, exist_ok=True)
    fx.to_parquet(OUT / "fx_daily.parquet", index=False)
    quality_report(fx)
    print(f"Saved {len(fx):,} rows for {fx['pair'].nunique()} pairs. Read data/fx/quality_report.md.")


if __name__ == "__main__":
    main()
