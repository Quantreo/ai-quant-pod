"""
Download daily prices of 23 US-listed ETFs across asset classes (equity, bonds, commodities, real estate, dollar)
from Yahoo Finance, 2005 to 2026-09.

Builds, in data/etf/ (never committed):
    etf_daily.parquet   one row per ETF and trading day: date, symbol, asset_class, open, high, low, close,
                        adj_close (dividends and splits), volume
    quality_report.md   first day per ETF, missing days, large moves

Why ETFs: twenty years of daily data, free, one script. A train of 12 years gives a gate with real power
(a t of 2 asks for a Sharpe of about 0.6, against 1.15 on 3 years of crypto). Open is kept for overnight and
intraday splits. Use adj_close for returns: close is the traded price, without dividends.
An ETF enters the universe on its first trading day: before it, it has no row (the universe is point in time).

Usage, from the repository root:
    python data/get_etf_daily.py
    python data/get_etf_daily.py --extended            # ~150 probed ETFs -> etf_extended.parquet (etf_daily untouched)
    python data/get_etf_daily.py --check               # compare with data/fingerprints/etf_daily.json
    python data/get_etf_daily.py --write-fingerprint   # after a build you trust

Data source: Yahoo Finance (https://finance.yahoo.com), public chart endpoint. You download it yourself, for
your own research; Yahoo's terms of use apply. Nothing downloaded here is ever committed or shared.
"""
import argparse, hashlib, json, time
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
# Extended list: probed one by one, the ones Yahoo serves are kept, the others are listed in the report.
# Includes ETFs closed or delisted that Yahoo may still serve (survivor bias). Never mixed into etf_daily.parquet.
ETFS_EXTENDED = {
    "sector": "XLB XLE XLF XLI XLK XLP XLU XLV XLY XLC XLRE XLG VDE VGT VHT VFH VIS VAW VCR VDC VPU VOX IYW IYH IYF IYZ IYC IYK IYJ IYM IYG IYT IYE IDU KBE KRE KIE XBI IBB SMH SOXX XHB XRT XOP OIH XES ITB IHI IGV XME PBE".split(),
    "size_style": "DIA MDY IJR IJH IWD IWF IWN IWO IWB IWV IWR IWP IWS IWM VTI VTV VUG VB VO VBR VBK IVE IVW IVV RSP SDY DVY VIG HDV".split(),
    "factor": "MTUM QUAL USMV VLUE SIZE PDP DWAS SPLV SPHB".split(),
    "country": "EWG EWU EWA EWC EWZ EWH EWS EWY EWT EWW EWI EWP EWQ EWL EWD EWN EWK EWO EWM INDA EPP EZA EIS THD TUR EPOL ECH EPU GREK RSX ERUS FEZ DEM SCZ VWO VEA VPL IEV ILF AAXJ".split(),
    "bonds": "SHV IEI IEF TLT TLH BND AGG MUB EMB MBB BWX VCSH VCIT VCLT BIL SHY BSV BIV BLV VGSH VGIT VGLT SCHO SCHR TFI CIU PCY EMLC SHYG JNK BKLN PFF LQDH MINT".split(),
    "commodities": "GDX GDXJ DBB DBE DBO DBP DBS DGL DBV UNG PPLT PALL CORN WEAT SOYB CPER JJC JJG JO NIB SGG BNO UGA USCI GSG IAU SIVR GLTR GLDI MOO PICK SLX COPX SIL REMX KOL USL UNL".split(),
    "real_estate": "IYR VNQI RWX RWR ICF REM REZ SCHH".split(),
    "currency": "FXA FXB FXC FXF UDN CYB BZF CEW AUNZ".split(),
}
EXT_FILE, EXT_REPORT, EXT_LIQ = "etf_extended.parquet", "quality_report_extended.md", "etf_extended_liquidity.csv"
URL = "https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
HEADERS = {"User-Agent": "Mozilla/5.0 (research script)"}
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "etf"
FINGERPRINT = ROOT / "data" / "fingerprints" / "etf_daily.json"
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


def fingerprint(df):
    return {"start": START, "end": END, "rows": len(df), "rows_by_symbol": {s: int(n) for s, n in df.groupby("symbol").size().items()},
            "hash": hashlib.sha256(pd.util.hash_pandas_object(df[["date", "symbol", "adj_close"]].round(4), index=False).values.tobytes()).hexdigest()[:16]}


def quality_report(df):
    d = df.sort_values(["symbol", "date"])
    ret = d.groupby("symbol")["adj_close"].pct_change()
    big = d.assign(ret=ret)[ret.abs() > 0.10].sort_values("ret", key=abs, ascending=False)
    spy_days = pd.DatetimeIndex(d.loc[d["symbol"] == "SPY", "date"])
    first = d.groupby("symbol")["date"].min()
    missing = {s: len(spy_days[spy_days >= first[s]].difference(pd.DatetimeIndex(g["date"]))) for s, g in d.groupby("symbol")}
    L = [f"# Quality report: ETF daily (Yahoo Finance), {START} to {END}", "",
         f"- ETFs: {d['symbol'].nunique()}; rows: {len(d):,}; last day: {d['date'].max():%Y-%m-%d}", "",
         "| ETF | Class | First day | Days missing vs SPY |", "| --- | --- | --- | --- |"]
    cls = d.groupby("symbol")["asset_class"].first()
    L += [f"| {s} | {cls[s]} | {first[s]:%Y-%m-%d} | {missing[s]} |" for s in first.sort_values().index]
    L += ["", f"## Daily moves above 10% (adjusted): {len(big)}", ""]
    L += [f"- {r.symbol} {r.date:%Y-%m-%d}: {r.ret:+.1%}" for r in big.head(25).itertuples()]
    (OUT / "quality_report.md").write_text("\n".join(L) + "\n")


def build_extended():
    """Probe every ticker of ETFS_EXTENDED; keep what returns data. Does not touch etf_daily.parquet."""
    frames, failed, seen = [], [], set()
    with requests.Session() as s:
        for cls, symbols in ETFS_EXTENDED.items():
            for sym in symbols:
                if sym in seen:
                    continue
                seen.add(sym)
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
    df.to_parquet(OUT / EXT_FILE, index=False)
    df = df.assign(dv=df["close"] * df["volume"], year=df["date"].dt.year)
    liq = (df.groupby(["symbol", "year"])["dv"].median() / 1e6).round(2).unstack()
    liq.to_csv(OUT / EXT_LIQ)
    g = df.groupby("symbol")
    first, last = g["date"].min(), g["date"].max()
    v08 = df[df["year"] == 2008].groupby("symbol")["volume"].median()
    ref = df[df["symbol"] == "SPY"] if (df["symbol"] == "SPY").any() else None
    days = pd.DatetimeIndex(sorted(df["date"].unique()))
    miss = {s_: int(len(days[(days >= first[s_]) & (days <= last[s_])].difference(pd.DatetimeIndex(x["date"])))) for s_, x in g}
    big = df.sort_values(["symbol", "date"]).assign(ret=df.sort_values(["symbol", "date"]).groupby("symbol")["adj_close"].pct_change())
    nbig = big[big["ret"].abs() > 0.10].groupby("symbol").size()
    dead = [s_ for s_ in first.index if last[s_] < pd.Timestamp("2026-09-01")]
    cls = g["asset_class"].first()
    L = [f"# Quality report: ETF extended (Yahoo Finance), {START} to {END}", "",
         f"- Probed: {len(seen)}; kept: {len(first)}; failed: {len(failed)}; rows: {len(df):,}",
         f"- Dead (last bar before 2026-09-01): {len(dead)}: {', '.join(f'{s_} (last {last[s_]:%Y-%m-%d})' for s_ in dead) or 'none'}",
         f"- Failed (no data from Yahoo): {', '.join(failed) or 'none'}",
         f"- Median dollar volume by year for each ETF: {EXT_LIQ} (USD million, median of close x volume)", "",
         "| ETF | Class | First | Last | Med vol 2008 | Med $vol 2008 (M) | Med $vol 2015 (M) | Med $vol 2025 (M) | Missing days | Moves >10% |",
         "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    def cell(y, s_):
        return f"{liq.loc[s_, y]:.2f}" if y in liq.columns and pd.notna(liq.loc[s_, y]) else "-"
    for s_ in first.sort_values().index:
        v = v08.get(s_)
        L.append(f"| {s_} | {cls[s_]} | {first[s_]:%Y-%m-%d} | {last[s_]:%Y-%m-%d} | {'-' if v is None else f'{v:,.0f}'} | "
                 f"{cell(2008, s_)} | {cell(2015, s_)} | {cell(2025, s_)} | {miss[s_]} | {int(nbig.get(s_, 0))} |")
    (OUT / "quality_report_extended.md").write_text("\n".join(L) + "\n")
    print(f"Saved {len(df):,} rows, {len(first)} ETFs kept of {len(seen)} probed; failed: {' '.join(failed)}; dead: {' '.join(dead)}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--extended", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--write-fingerprint", action="store_true")
    args = ap.parse_args()

    if args.extended:
        OUT.mkdir(parents=True, exist_ok=True)
        build_extended()
        return
    if args.check or args.write_fingerprint:
        fp = fingerprint(pd.read_parquet(OUT / "etf_daily.parquet"))
        if args.write_fingerprint:
            FINGERPRINT.parent.mkdir(parents=True, exist_ok=True)
            FINGERPRINT.write_text(json.dumps(fp, indent=2))
            print(f"Fingerprint saved to {FINGERPRINT}")
        else:
            ref = json.loads(FINGERPRINT.read_text())
            diff = {k: (ref.get(k), v) for k, v in fp.items() if ref.get(k) != v}
            print("Same data as the reference." if not diff else "Differences (reference, yours):")
            for k, (a, b) in diff.items():
                print(f"  {k}: {a} | {b}")
        return

    frames = []
    with requests.Session() as s:
        for cls, symbols in ETFS.items():
            for sym in symbols:
                frames.append(download(s, sym).assign(symbol=sym, asset_class=cls))
                time.sleep(0.5)
    df = pd.concat(frames, ignore_index=True)
    df = df[(df["date"] >= START) & (df["date"] <= END)]
    df = df[["date", "symbol", "asset_class", "open", "high", "low", "close", "adj_close", "volume"]]
    df = df.sort_values(["symbol", "date"]).drop_duplicates(["symbol", "date"]).reset_index(drop=True)
    OUT.mkdir(parents=True, exist_ok=True)
    df.to_parquet(OUT / "etf_daily.parquet", index=False)
    quality_report(df)
    print(f"Saved {len(df):,} rows for {df['symbol'].nunique()} ETFs. Read data/etf/quality_report.md.")


if __name__ == "__main__":
    main()
