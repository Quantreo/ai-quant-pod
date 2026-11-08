"""
Download daily prices of about 220 US-listed ETFs across asset classes (equity indexes, sectors, styles, factors,
countries, bonds of every maturity, commodities, real estate, currencies) from Yahoo Finance, 2005 to 2026-09.

Builds, in data/etf/ (never committed):
    etf_daily.parquet      one row per ETF and trading day: date, symbol, asset_class, open, high, low, close,
                           adj_close (dividends and splits), volume
    etf_liquidity.csv      median daily dollar volume per ETF and year (USD million): input for the cost tiers
    quality_report.md      per ETF: class, first and last day, dollar volume, missing days, large moves; failed tickers

Why ETFs: twenty years of daily data, free, one script. A train of 12 years gives a gate with real power
(a t of 2 asks for a Sharpe of about 0.6, against 1.15 on 3 years of crypto). Open is kept for overnight and
intraday splits. Use adj_close for returns: close is the traded price, without dividends.
An ETF enters the universe on its first trading day: before it, it has no row (the universe is point in time).

Usage, from the repository root:
    python data/get_etf_daily.py                        # about 2 minutes

Data source: Yahoo Finance (https://finance.yahoo.com), public chart endpoint. You download it yourself, for
your own research; Yahoo's terms of use apply. Nothing downloaded here is ever committed or shared.
"""
import argparse, time
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import requests

ETFS = {
    "equity": ["SPY", "QQQ", "IWM", "EFA", "EEM", "EWJ", "VGK", "FXI"],
    "bonds": ["SHY", "IEF", "TLT", "LQD", "TIP", "HYG"],
    "commodities": ["GLD", "SLV", "DBC", "USO", "DBA"],
    "real_estate": ["VNQ"],
    "currency": ["UUP", "FXE", "FXY"],
}
# More ETFs, probed one by one: the ones Yahoo serves are kept, the others are listed in the report.
# Closed or delisted ETFs are mostly not served by Yahoo: the file is close to survivors only (say it in a Pass 1).
ETFS_MORE = {
    "sector": "XLB XLE XLF XLI XLK XLP XLU XLV XLY XLC XLRE XLG VDE VGT VHT VFH VIS VAW VCR VDC VPU VOX IYW IYH IYF IYZ IYC IYK IYJ IYM IYG IYT IYE IDU KBE KRE KIE XBI IBB SMH SOXX XHB XRT XOP OIH XES ITB IHI IGV XME PBE".split(),
    "size_style": "DIA MDY IJR IJH IWD IWF IWN IWO IWB IWV IWR IWP IWS IWM VTI VTV VUG VB VO VBR VBK IVE IVW IVV RSP SDY DVY VIG HDV".split(),
    "factor": "MTUM QUAL USMV VLUE SIZE PDP DWAS SPLV SPHB".split(),
    "country": "EWG EWU EWA EWC EWZ EWH EWS EWY EWT EWW EWI EWP EWQ EWL EWD EWN EWK EWO EWM INDA EPP EZA EIS THD TUR EPOL ECH EPU GREK RSX ERUS FEZ DEM SCZ VWO VEA VPL IEV ILF AAXJ".split(),
    "bonds": "SHV IEI IEF TLT TLH BND AGG MUB EMB MBB BWX VCSH VCIT VCLT BIL SHY BSV BIV BLV VGSH VGIT VGLT SCHO SCHR TFI CIU PCY EMLC SHYG JNK BKLN PFF LQDH MINT".split(),
    "commodities": "GDX GDXJ DBB DBE DBO DBP DBS DGL DBV UNG PPLT PALL CORN WEAT SOYB CPER JJC JJG JO NIB SGG BNO UGA USCI GSG IAU SIVR GLTR GLDI MOO PICK SLX COPX SIL REMX KOL USL UNL".split(),
    "real_estate": "IYR VNQI RWX RWR ICF REM REZ SCHH".split(),
    "currency": "FXA FXB FXC FXF UDN CYB BZF CEW AUNZ".split(),
}
FILE, REPORT, LIQ = "etf_daily.parquet", "quality_report.md", "etf_liquidity.csv"
URL = "https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
HEADERS = {"User-Agent": "Mozilla/5.0 (research script)"}
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "etf"
START, END = "2005-01-01", "2026-09-30"          # fixed, so that every user builds the same data


def epoch(day):
    return int(datetime.fromisoformat(day).replace(tzinfo=timezone.utc).timestamp())


def download(session, symbol, tries=5):
    params = {"period1": epoch(START), "period2": epoch(END) + 86400, "interval": "1d", "events": "div,split",
              "includeAdjustedClose": "true"}
    for k in range(tries):
        try:
            r = session.get(URL.format(symbol=symbol), params=params, headers=HEADERS, timeout=30)
            r.raise_for_status()
            res = r.json()["chart"]["result"][0]
            q = res["indicators"]["quote"][0]
            adj = res["indicators"]["adjclose"][0]["adjclose"]
            tz = res["meta"].get("exchangeTimezoneName", "America/New_York")
            dates = pd.to_datetime(res["timestamp"], unit="s", utc=True).tz_convert(tz).normalize().tz_localize(None)
            return pd.DataFrame({"date": dates, "open": q["open"], "high": q["high"], "low": q["low"],
                                 "close": q["close"], "adj_close": adj, "volume": q["volume"]}).dropna(subset=["close", "adj_close"])
        except (requests.RequestException, KeyError, IndexError, TypeError, ValueError):
            time.sleep(2 + 3 * k)
    raise RuntimeError(f"failed after {tries} tries: {symbol}")


def universe():
    """The core 23 first, then the others; a ticker listed twice keeps its first class."""
    seen, out = set(), []
    for group in (ETFS, ETFS_MORE):
        for cls, symbols in group.items():
            for sym in symbols:
                if sym not in seen:
                    seen.add(sym)
                    out.append((sym, cls))
    return out


def build():
    frames, failed, probed = [], [], universe()
    with requests.Session() as s:
        for sym, cls in probed:
            try:
                d = download(s, sym, tries=2)
                d = d[(d["date"] >= START) & (d["date"] <= END)]
                if len(d) < 20:
                    raise RuntimeError("too few rows")
                frames.append(d.assign(symbol=sym, asset_class=cls))
            except RuntimeError:
                failed.append(sym)
            time.sleep(0.4)
    df = pd.concat(frames, ignore_index=True)[["date", "symbol", "asset_class", "open", "high", "low", "close", "adj_close", "volume"]]
    df = df.sort_values(["symbol", "date"]).drop_duplicates(["symbol", "date"]).reset_index(drop=True)
    OUT.mkdir(parents=True, exist_ok=True)
    df.to_parquet(OUT / FILE, index=False)
    quality_report(df, len(probed), failed)
    print(f"Saved {len(df):,} rows, {df['symbol'].nunique()} ETFs kept of {len(probed)} probed; failed: {' '.join(failed) or 'none'}. "
          f"Read data/etf/{REPORT}.")


def quality_report(df, n_probed, failed):
    df = df.assign(dv=df["close"] * df["volume"], year=df["date"].dt.year)
    liq = (df.groupby(["symbol", "year"])["dv"].median() / 1e6).round(2).unstack()
    liq.to_csv(OUT / LIQ)
    g = df.groupby("symbol")
    first, last = g["date"].min(), g["date"].max()
    days = pd.DatetimeIndex(sorted(df["date"].unique()))
    miss = {s_: int(len(days[(days >= first[s_]) & (days <= last[s_])].difference(pd.DatetimeIndex(x["date"])))) for s_, x in g}
    srt = df.sort_values(["symbol", "date"])
    ret = srt.groupby("symbol")["adj_close"].pct_change()
    nbig = srt[ret.abs() > 0.10].groupby("symbol").size()
    dead = [s_ for s_ in first.index if last[s_] < pd.Timestamp(END) - pd.Timedelta(days=30)]
    cls = g["asset_class"].first()
    L = [f"# Quality report: ETF daily (Yahoo Finance), {START} to {END}", "",
         f"- Probed: {n_probed}; kept: {len(first)}; failed: {len(failed)}; rows: {len(df):,}",
         f"- Dead (last bar more than 30 days before the end): {', '.join(f'{s_} (last {last[s_]:%Y-%m-%d})' for s_ in dead) or 'none'}",
         f"- Failed (no data from Yahoo): {', '.join(failed) or 'none'}",
         f"- Median dollar volume by year for each ETF: {LIQ} (USD million, median of close x volume)", "",
         "| ETF | Class | First | Last | Med $vol 2008 (M) | Med $vol 2015 (M) | Med $vol 2025 (M) | Missing days | Moves >10% |",
         "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]

    def cell(y, s_):
        return f"{liq.loc[s_, y]:.2f}" if y in liq.columns and pd.notna(liq.loc[s_, y]) else "-"
    for s_ in first.sort_values().index:
        L.append(f"| {s_} | {cls[s_]} | {first[s_]:%Y-%m-%d} | {last[s_]:%Y-%m-%d} | {cell(2008, s_)} | {cell(2015, s_)} | "
                 f"{cell(2025, s_)} | {miss[s_]} | {int(nbig.get(s_, 0))} |")
    (OUT / REPORT).write_text("\n".join(L) + "\n")


def main():
    argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter).parse_args()
    build()


if __name__ == "__main__":
    main()
