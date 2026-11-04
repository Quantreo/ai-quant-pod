"""
Download 3-month interbank rates for the G10 currencies from FRED (OECD series, monthly, % a year).

Builds, in data/rates/ (never committed):
    rates_monthly.parquet   one row per currency and month: date (first day of the month), currency, rate
    quality_report.md       first and last month per currency: a series that stops early is stale

What it is for: the interest differential of an FX position (carry), which a price series does not contain.
What it is not: forward points. A monthly interbank rate is an approximation of what a forward or a swap
really pays, good enough for research, to be said in any result built on it.

It also downloads the all-items consumer price indexes (NSA, index level) of the G10 economies, for the FX value
signal, into cpi.parquet and cpi_quality_report.md. Monthly except AUD and NZD (quarterly). Series that no longer
update on FRED (the OECD stopped for several economies) are flagged stale in the report, never replaced silently.
No publication dates: FRED gives no vintages here, so a signal must apply its own lag.

It also downloads policy rates, to split a 3-month fixing into policy and credit spread, into policy.parquet and
policy_quality_report.md: ECB main refinancing (ECBMRRFR) and deposit facility (ECBDFR) rates, daily on FRED, averaged
by calendar month (daily step series filled forward), and the effective Fed funds rate (FEDFUNDS, monthly average).

It also downloads the 3-month Treasury bill rate (TB3MS, secondary market, monthly average of the daily DTB3, % a year,
discount basis) as a cash return from 2004, into tbill.parquet and tbill_quality_report.md.

It also downloads the US Treasury constant-maturity yields (GS1, GS2, GS3, GS5, GS7, GS10, GS20, GS30: monthly average of the
daily DGS series, % a year, bond-equivalent) for a maturity ladder (bond carry), into ust_curve.parquet and
ust_curve_quality_report.md. Gaps or stale series are flagged in the report, never filled.

Usage, from the repository root:
    python data/get_rates.py

Data source: FRED, Federal Reserve Bank of St. Louis (https://fred.stlouisfed.org), series from the OECD Main
Economic Indicators. You download it yourself; FRED's terms of use apply.
"""
import io, time
from pathlib import Path

import pandas as pd
import requests

SERIES = {"USD": "IR3TIB01USM156N", "EUR": "IR3TIB01EZM156N", "GBP": "IR3TIB01GBM156N", "JPY": "IR3TIB01JPM156N",
          "CHF": "IR3TIB01CHM156N", "AUD": "IR3TIB01AUM156N", "NZD": "IR3TIB01NZM156N", "CAD": "IR3TIB01CAM156N",
          "NOK": "IR3TIB01NOM156N", "SEK": "IR3TIB01SEM156N"}
CPI = {"USD": ("CPIAUCNS", "M"), "EUR": ("CP0000EZCCM086NEST", "M"), "GBP": ("GBRCPIALLMINMEI", "M"),
       "JPY": ("JPNCPIALLMINMEI", "M"), "CHF": ("CP0000CHM086NEST", "M"), "CAD": ("CANCPIALLMINMEI", "M"),
       "NOK": ("CP0000NOM086NEST", "M"), "SEK": ("CP0000SEM086NEST", "M"),
       "AUD": ("AUSCPIALLQINMEI", "Q"), "NZD": ("NZLCPIALLQINMEI", "Q")}
CPI_START = "2007-01-01"
POLICY = {"ECB_MRO": "ECBMRRFR", "ECB_DFR": "ECBDFR", "USD_FFR": "FEDFUNDS"}
POLICY_START = "2009-01-01"
TBILL = {"USD_TB3M": "TB3MS"}
TBILL_START = "2004-01-01"
UST = {"UST_1Y": "GS1", "UST_2Y": "GS2", "UST_3Y": "GS3", "UST_5Y": "GS5", "UST_7Y": "GS7", "UST_10Y": "GS10", "UST_20Y": "GS20",
       "UST_30Y": "GS30"}
UST_START = "2004-01-01"
URL = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={series}"
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "rates"
START = "2009-01-01"


def download(session, series, tries=5):
    for k in range(tries):
        try:
            r = session.get(URL.format(series=series), timeout=30)
            r.raise_for_status()
            df = pd.read_csv(io.StringIO(r.text), na_values=".")
            df.columns = ["date", "rate"]                     # FRED names the first column DATE or observation_date
            return df.assign(date=pd.to_datetime(df["date"])).dropna()
        except requests.RequestException:
            time.sleep(1 + 2 * k)
    raise RuntimeError(f"failed after {tries} tries: {series}")


def main_cpi():
    with requests.Session() as s:
        cpi = pd.concat([download(s, sid).rename(columns={"rate": "cpi"}).assign(currency=c, freq=f)
                         for c, (sid, f) in CPI.items()], ignore_index=True)
    cpi = cpi[cpi["date"] >= CPI_START][["date", "currency", "freq", "cpi"]].sort_values(["currency", "date"]).reset_index(drop=True)
    cpi.to_parquet(OUT / "cpi.parquet", index=False)
    span = cpi.groupby("currency").agg(first=("date", "min"), last=("date", "max"), n=("date", "size"), freq=("freq", "first"))
    now = pd.Timestamp.today().normalize()
    L = ["# Quality report: consumer price indexes (FRED), NSA index level", "",
         "| Currency | Series | Freq | First | Last | Obs | |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for c, r in span.iterrows():
        gap = pd.Series(cpi.loc[cpi["currency"] == c, "date"]).diff().dt.days.max()
        stale = r["last"] < now - pd.DateOffset(months=6)
        L.append(f"| {c} | {CPI[c][0]} | {r['freq']} | {r['first']:%Y-%m} | {r['last']:%Y-%m} | {r['n']} | "
                 f"{'stale' if stale else ''}{' gap' if gap > (100 if r['freq'] == 'Q' else 35) else ''} |")
    (OUT / "cpi_quality_report.md").write_text("\n".join(L) + "\n")
    print("Saved CPI. Read data/rates/cpi_quality_report.md.")


def main_policy():
    with requests.Session() as s:
        raw = {k: download(s, sid).set_index("date")["rate"] for k, sid in POLICY.items()}
    rows = []
    for k, x in raw.items():
        if k != "USD_FFR":                                    # daily step series: calendar-day fill, then monthly mean
            x = x.resample("D").last().ffill().resample("MS").mean()
        rows.append(x.rename("rate").rename_axis("date").reset_index().assign(series=k))
    pol = pd.concat(rows, ignore_index=True)
    pol = pol[pol["date"] >= POLICY_START][["date", "series", "rate"]].sort_values(["series", "date"]).reset_index(drop=True)
    pol.to_parquet(OUT / "policy.parquet", index=False)
    span = pol.groupby("series")["date"].agg(["min", "max", "size"])
    L = ["# Quality report: policy rates (FRED), monthly average, % a year", "",
         "| Series | FRED id | First | Last | Months | |", "| --- | --- | --- | --- | --- | --- |"]
    L += [f"| {k} | {POLICY[k]} | {r['min']:%Y-%m} | {r['max']:%Y-%m} | {r['size']} | "
          f"{'stale' if r['max'] < pd.Timestamp.today() - pd.DateOffset(months=3) else ''} |" for k, r in span.iterrows()]
    (OUT / "policy_quality_report.md").write_text("\n".join(L) + "\n")
    print("Saved policy rates. Read data/rates/policy_quality_report.md.")


def main_tbill():
    with requests.Session() as s:
        raw = {k: download(s, sid) for k, sid in TBILL.items()}
    tb = pd.concat([d.assign(series=k) for k, d in raw.items()], ignore_index=True)
    tb = tb[tb["date"] >= TBILL_START][["date", "series", "rate"]].sort_values(["series", "date"]).reset_index(drop=True)
    tb.to_parquet(OUT / "tbill.parquet", index=False)
    span = tb.groupby("series")["date"].agg(["min", "max", "size"])
    L = ["# Quality report: 3-month Treasury bill rate (FRED), monthly average, % a year", "",
         "| Series | FRED id | First | Last | Months | |", "| --- | --- | --- | --- | --- | --- |"]
    L += [f"| {k} | {TBILL[k]} | {r['min']:%Y-%m} | {r['max']:%Y-%m} | {r['size']} | "
          f"{'stale' if r['max'] < pd.Timestamp.today() - pd.DateOffset(months=3) else ''} |" for k, r in span.iterrows()]
    (OUT / "tbill_quality_report.md").write_text("\n".join(L) + "\n")
    print("Saved T-bill rate. Read data/rates/tbill_quality_report.md.")


def main_ust():
    with requests.Session() as s:
        raw = {k: download(s, sid) for k, sid in UST.items()}
    u = pd.concat([d.assign(series=k) for k, d in raw.items()], ignore_index=True)
    u = u[u["date"] >= UST_START][["date", "series", "rate"]].sort_values(["series", "date"]).reset_index(drop=True)
    u.to_parquet(OUT / "ust_curve.parquet", index=False)
    span = u.groupby("series")["date"].agg(["min", "max", "size"])
    L = ["# Quality report: US Treasury constant-maturity yields (FRED), monthly average, % a year", "",
         "| Series | FRED id | First | Last | Months | |", "| --- | --- | --- | --- | --- | --- |"]
    for k, r in span.iterrows():
        gap = u.loc[u["series"] == k, "date"].diff().dt.days.max()
        L.append(f"| {k} | {UST[k]} | {r['min']:%Y-%m} | {r['max']:%Y-%m} | {r['size']} | "
                 f"{'stale' if r['max'] < pd.Timestamp.today() - pd.DateOffset(months=3) else ''}{' gap' if gap > 35 else ''} |")
    (OUT / "ust_curve_quality_report.md").write_text("\n".join(L) + "\n")
    print("Saved UST curve. Read data/rates/ust_curve_quality_report.md.")


def main():
    with requests.Session() as s:
        rates = pd.concat([download(s, sid).assign(currency=c) for c, sid in SERIES.items()], ignore_index=True)
    rates = rates[rates["date"] >= START][["date", "currency", "rate"]].sort_values(["currency", "date"]).reset_index(drop=True)

    OUT.mkdir(parents=True, exist_ok=True)
    rates.to_parquet(OUT / "rates_monthly.parquet", index=False)
    span = rates.groupby("currency")["date"].agg(["min", "max", "size"])
    last = span["max"].max()
    L = ["# Quality report: 3-month interbank rates (FRED, OECD), monthly", "",
         "| Currency | Series | First | Last | Months | |", "| --- | --- | --- | --- | --- | --- |"]
    L += [f"| {c} | {SERIES[c]} | {r['min']:%Y-%m} | {r['max']:%Y-%m} | {r['size']} | {'stale' if r['max'] < last - pd.DateOffset(months=3) else ''} |"
          for c, r in span.iterrows()]
    (OUT / "quality_report.md").write_text("\n".join(L) + "\n")
    print(f"Saved {len(rates):,} rows for {rates['currency'].nunique()} currencies. Read data/rates/quality_report.md.")
    main_cpi()
    main_policy()
    main_tbill()
    main_ust()


if __name__ == "__main__":
    main()
