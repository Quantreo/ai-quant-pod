"""
Download Binance USDT-margined perpetual futures, daily, from Binance's public dataset (data.binance.vision).

Builds, in data/crypto/ (never committed):
    perps_daily.parquet    one row per symbol and UTC day: open, high, low, close (last price), quote_volume,
                           mark_open, mark_high, mark_low, mark_close (mark price),
                           funding_rate (sum of the day's prints, NaN if none), funding_prints
    perps_funding.parquet  every funding print: symbol, time (UTC), rate, interval_hours
    perps_meta.csv         one row per symbol: ticker, first and last day, days, multiplier (1000SHIB -> 1000),
                           underlying_type (COIN, INDEX, EQUITY, COMMODITY...) and where that type comes from
    quality_report.md      names per year, gaps, outliers, funding intervals

Every symbol ever listed is included, dead ones too: the list comes from the dataset itself, not from
today's exchange. This is what makes a point-in-time universe possible. Three repairs are made, and counted
in the report:
    - days with no trade are dropped: a delisted contract keeps flat, zero-volume bars in the archive for years;
    - days missing from a monthly file are fetched from the daily files when they exist;
    - a ticker that stops trading for more than 30 days and comes back is a new listing (often a new token
      under an old name): it gets its own symbol, LITUSDT.2, so no return is computed across the gap. The raw monthly zips are kept in
data/crypto/raw/, so a second run only downloads the months it does not have yet.

Usage, from the repository root:
    python data/get_crypto_daily.py                              # full build
    python data/get_crypto_daily.py --symbols BTCUSDT,ETHUSDT    # quick test on two names
    python data/get_crypto_daily.py --check                      # compare with data/fingerprints/crypto_daily.json
    python data/get_crypto_daily.py --write-fingerprint          # after a build you trust

Mark price: Binance computes it from an index of spot exchanges and uses it for liquidations and unrealised
P&L. It ignores the wicks of a single order book, so signals, risk and liquidation checks are built on it; the
last price stays for what a trade would really get.

Source: Binance Vision public datasets (https://data.binance.vision), licensed CC BY-NC-SA 4.0 under the
Binance Vision Dataset Terms. You download it yourself, for your own non-commercial research and
backtesting. It is not redistributed here.
"""
import argparse, hashlib, io, json, re, time, zipfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import numpy as np
import pandas as pd
import requests

BASE = "https://data.binance.vision/"
LIST = "https://s3-ap-northeast-1.amazonaws.com/data.binance.vision?delimiter=/&prefix={prefix}"
KLINES = "data/futures/um/monthly/klines/{s}/1d/"
FUNDING = "data/futures/um/monthly/fundingRate/{s}/"
MARK = "data/futures/um/monthly/markPriceKlines/{s}/1d/"
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "crypto"
RAW = OUT / "raw"
FINGERPRINT = ROOT / "data" / "fingerprints" / "crypto_daily.json"
START, END = "2020-01-01", "2026-09-30"          # fixed, so that every user builds the same data; the archive starts in 2020-01
DAILY_KLINES = "data/futures/um/daily/klines/{s}/1d/{s}-1d-{d:%Y-%m-%d}.zip"
DAILY_MARK = "data/futures/um/daily/markPriceKlines/{s}/1d/{s}-1d-{d:%Y-%m-%d}.zip"
RELIST_GAP = 30                                   # days without trading after which a ticker counts as a new listing


# ---------- download ----------

def get(session, url, tries=5):
    for k in range(tries):
        try:
            r = session.get(url, timeout=30)
            if r.status_code == 404:
                return None
            r.raise_for_status()
            return r
        except requests.RequestException:
            time.sleep(1 + 2 * k)
    raise RuntimeError(f"failed after {tries} tries: {url}")


def list_s3(session, prefix, what):
    """Keys (.zip files) or sub-folders under a prefix. The listing is paginated by 1000."""
    pattern = r"<Key>([^<]+\.zip)</Key>" if what == "keys" else r"<CommonPrefixes><Prefix>([^<]+)</Prefix></CommonPrefixes>"
    found, marker = [], ""
    while True:
        r = get(session, LIST.format(prefix=prefix) + (f"&marker={marker}" if marker else ""))
        if r is None:
            return found
        page = re.findall(pattern, r.text)
        found += page
        if "<IsTruncated>true</IsTruncated>" not in r.text or not page:
            return found
        nxt = re.search(r"<NextMarker>([^<]+)</NextMarker>", r.text)
        marker = nxt.group(1) if nxt else page[-1]


def all_usdt_perps(session):
    """Every USDT perpetual that ever had daily klines, dead ones included. Dated futures (BTCUSDT_230331) are left out."""
    folders = list_s3(session, "data/futures/um/monthly/klines/", "folders")
    names = [f.rstrip("/").split("/")[-1] for f in folders]
    return sorted(n for n in names if re.fullmatch(r"[A-Z0-9]+USDT", n))


def fetch(session, key):
    """Raw zip from the local cache, or downloaded and cached. None if the file does not exist."""
    path = RAW / key
    if path.exists() and path.stat().st_size > 0:
        return path.read_bytes()
    r = get(session, BASE + key)
    if r is None:
        return None
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(r.content)
    return r.content


def run(session, jobs, parse, workers, label):
    t0, out, n = time.time(), [], len(jobs)
    with ThreadPoolExecutor(workers) as ex:
        futs = {ex.submit(fetch, session, key): sym for sym, key in jobs}
        for i, f in enumerate(as_completed(futs), 1):
            content = f.result()
            if content is not None:
                out.append(parse(content).assign(symbol=futs[f]))
            if i % 500 == 0 or i == n:
                el = time.time() - t0
                print(f"\r  {label}: {i:,}/{n:,} files, {el:,.0f} s, ~{el / i * (n - i):,.0f} s left", end="", flush=True)
    print()
    return pd.concat(out, ignore_index=True) if out else pd.DataFrame()


# ---------- parsing ----------

def read_zip_csv(content, names):
    with zipfile.ZipFile(io.BytesIO(content)) as z:
        raw = z.read(z.namelist()[0]).decode()
    first = raw.split("\n", 1)[0].split(",")[0]
    skip = 0 if first.strip().lstrip("-").isdigit() else 1          # newer files carry a header row
    return pd.read_csv(io.StringIO(raw), header=None, skiprows=skip, names=names)


def to_utc(x):
    x = pd.to_numeric(x)
    return pd.to_datetime(np.where(x > 1e14, x // 1000, x), unit="ms", utc=True).tz_localize(None)   # some files use microseconds


def klines(content):
    df = read_zip_csv(content, ["open_time", "open", "high", "low", "close", "volume", "close_time", "quote_volume",
                                "count", "taker_buy_volume", "taker_buy_quote_volume", "ignore"])
    out = pd.DataFrame({"date": to_utc(df["open_time"]).normalize()})
    for c in ["open", "high", "low", "close", "quote_volume"]:
        out[c] = df[c].astype(float)
    return out


def mark(content):
    df = klines(content)[["date", "open", "high", "low", "close"]]
    return df.rename(columns={c: f"mark_{c}" for c in ["open", "high", "low", "close"]})


def funding(content):
    df = read_zip_csv(content, ["calc_time", "funding_interval_hours", "last_funding_rate"])
    return pd.DataFrame({"time": to_utc(df["calc_time"]).round("min"),
                         "rate": df["last_funding_rate"].astype(float),
                         "interval_hours": pd.to_numeric(df["funding_interval_hours"], errors="coerce")})


def multiplier(symbol):
    """Contracts quoted per 1000 or per million units (1000SHIBUSDT, 1MBABYDOGEUSDT). Inferred from the name."""
    m = re.match(r"(1000000|100000|10000|1000|1M)(?=[A-Z])", symbol)
    return 1 if m is None else (1_000_000 if m.group(1) == "1M" else int(m.group(1)))


# ---------- checks ----------

def frame_hash(df):
    return hashlib.sha256(pd.util.hash_pandas_object(df, index=False).values.tobytes()).hexdigest()[:16]


def fingerprint(daily, fund):
    return {"start": START, "end": END,
            "daily_rows": len(daily), "funding_rows": len(fund), "symbols": int(daily["symbol"].nunique()),
            "symbols_by_year": {str(y): int(n) for y, n in daily.groupby(daily["date"].dt.year)["symbol"].nunique().items()},
            "daily_hash": frame_hash(daily), "funding_hash": frame_hash(fund)}


def quality_report(daily, fund, meta, repairs):
    d = daily.sort_values(["symbol", "date"])
    ret = d.groupby("symbol")["close"].pct_change()
    big = d.assign(ret=ret)[ret.abs() > 0.8].sort_values("ret", key=abs, ascending=False)
    bad_bar = d[(d["high"] < d[["open", "close"]].max(axis=1)) | (d["low"] > d[["open", "close"]].min(axis=1))]
    span = (meta["last_day"] - meta["first_day"]).dt.days + 1
    gaps = (span - meta["days"]).rename("missing_days")
    gaps = meta.assign(missing_days=gaps)[gaps > 0].sort_values("missing_days", ascending=False)
    no_fund = d[d["funding_prints"] == 0].groupby("symbol").size().sort_values(ascending=False)
    per_day = d.groupby("date")["symbol"].nunique()
    by_year = per_day.groupby(per_day.index.year).agg(["min", "median", "max"])
    intervals = fund["interval_hours"].value_counts(dropna=False).sort_index()
    changed = fund.dropna(subset=["interval_hours"]).groupby("symbol")["interval_hours"].nunique()
    changed = changed[changed > 1]
    extreme = fund[fund["rate"].abs() > 0.01]
    alive = (meta["last_day"] == meta["last_day"].max()).sum()

    L = [f"# Quality report: crypto daily, {START} to {END}", "",
         f"- Symbols: {len(meta)} ({alive} trading on the last day, {len(meta) - alive} dead)",
         f"- Daily rows: {len(d):,}; funding prints: {len(fund):,}",
         "- Underlying types: " + ", ".join(f"{k} {v}" for k, v in meta["underlying_type"].value_counts().items())
         + f" ({int((meta['type_source'] == 'assumed').sum())} assumed, the others from the exchange)", "",
         "## Repairs", "",
         f"- Zero-volume bars dropped (delisted contracts keep flat bars in the archive): {repairs['zero_volume_dropped']:,}",
         f"- Days missing inside a trading span: {repairs['missing_days']:,}, filled from the daily files: {repairs['missing_days_filled']:,}",
         f"- Days with no mark price in the monthly files: {repairs['mark_days_missing']:,}, filled from the daily files: {repairs['mark_days_filled']:,}",
         f"- Tickers relisted after more than {RELIST_GAP} days, split into SYMBOL.2 ...: {len(repairs['relisted_tickers'])}"
         + (f" ({', '.join(repairs['relisted_tickers'])})" if repairs["relisted_tickers"] else ""), "",
         "## Names with data, per day", "", "| Year | Min | Median | Max |", "| --- | --- | --- | --- |"]
    L += [f"| {y} | {int(r['min'])} | {r['median']:.0f} | {int(r['max'])} |" for y, r in by_year.iterrows()]
    L += ["", f"## Gaps left: {len(gaps)} symbols with missing days between their first and last day", ""]
    L += [f"- {r.symbol}: {r.missing_days} days missing" for r in gaps.head(20).itertuples()]
    L += ["", f"## Daily moves above 80%: {len(big)} (a relisted ticker or a redenomination looks like this)", ""]
    L += [f"- {r.symbol} {r.date:%Y-%m-%d}: {r.ret:+.0%}" for r in big.head(20).itertuples()]
    L += ["", f"## Inconsistent bars (high below open or close, low above): {len(bad_bar)}", ""]
    no_mark = d[d["mark_close"].isna()]
    L += [f"## Days with no mark price: {len(no_mark):,} in {no_mark['symbol'].nunique()} symbols"
          + (f" (most: {', '.join(f'{s} {n}' for s, n in no_mark['symbol'].value_counts().head(5).items())})" if len(no_mark) else ""), ""]
    L += ["## Funding", "", "Prints by interval (hours): " + ", ".join(f"{k}: {v:,}" for k, v in intervals.items()),
          f"- Symbols whose interval changed: {len(changed)}" + (f" ({', '.join(changed.index[:15])}{', ...' if len(changed) > 15 else ''})" if len(changed) else ""),
          f"- Prints above 1% in absolute value: {len(extreme)}",
          f"- Days with a price but no funding print: {int(no_fund.sum()):,}, in {len(no_fund)} symbols"
          + (f" (most: {', '.join(f'{s} {n}' for s, n in no_fund.head(5).items())})" if len(no_fund) else ""), ""]
    (OUT / "quality_report.md").write_text("\n".join(L))


# ---------- underlying type ----------

EXCHANGE_INFO = "https://fapi.binance.com/fapi/v1/exchangeInfo"
TRADFI_START = pd.Timestamp("2025-12-01")        # Binance's first non-crypto perps (gold, then stocks) came after this


def underlying_types(meta):
    """Since 2026 Binance lists perps on stocks, metals and indices next to the coins. The exchange says which is
    which for the contracts it still lists; a delisted contract from before the first TradFi perp is a coin."""
    try:
        info = requests.get(EXCHANGE_INFO, timeout=30).json()["symbols"]
        types = {s["symbol"]: s.get("underlyingType", "unknown") for s in info}
    except (requests.RequestException, KeyError, ValueError):
        print("  Could not reach the exchange for the underlying types: every type is inferred.")
        types = {}
    known = meta["ticker"].map(types)
    assumed = np.where(meta["first_day"] < TRADFI_START, "COIN", "unknown")
    meta["underlying_type"] = known.fillna(pd.Series(assumed, index=meta.index))
    meta["type_source"] = np.where(known.notna(), "exchange", "assumed")
    return meta


# ---------- repairs ----------

def missing_days(kl):
    """(symbol, day) pairs missing inside a trading span, for gaps short enough not to be a relisting."""
    out = []
    for sym, x in kl.groupby("symbol"):
        dates = x["date"].sort_values()
        gap = dates.diff().dt.days
        for prev, g in zip(dates.shift()[(gap > 1) & (gap <= RELIST_GAP)], gap[(gap > 1) & (gap <= RELIST_GAP)]):
            out += [(sym, prev + pd.Timedelta(days=k)) for k in range(1, int(g))]
    return out


def split_relistings(daily, fund):
    """A ticker silent for more than RELIST_GAP days that trades again becomes SYMBOL.2, SYMBOL.3 ..."""
    d = daily.sort_values(["symbol", "date"]).copy()
    seg = (d.groupby("symbol")["date"].diff().dt.days > RELIST_GAP).groupby(d["symbol"]).cumsum()
    d["ticker"] = d["symbol"]
    d["symbol"] = np.where(seg == 0, d["symbol"], d["symbol"] + "." + (seg + 1).astype(str))
    spans = d.groupby("symbol").agg(ticker=("ticker", "first"), start=("date", "min"), last=("date", "max")).reset_index()
    spans["ticker"] = spans["ticker"].astype(str)
    f = pd.merge_asof(fund.sort_values("time").rename(columns={"symbol": "ticker"}).astype({"ticker": str}), spans.sort_values("start"),
                      left_on="time", right_on="start", by="ticker", direction="backward")
    # a print outside every trading span (before the first bar, in a silent gap, after the last bar) pays nobody: dropped.
    # The print at 00:00 the day after the last bar still belongs to the position held on that last day.
    inside = f["symbol"].notna() & (f["time"] <= f["last"] + pd.Timedelta(days=1))
    f = f[inside][["symbol", "time", "rate", "interval_hours"]].sort_values(["symbol", "time"]).reset_index(drop=True)
    return d, f


# ---------- main ----------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--symbols", help="comma-separated list, for a quick test; default: every USDT perp ever listed")
    ap.add_argument("--workers", type=int, default=12, help="parallel downloads; keep it moderate (Binance rate limits)")
    ap.add_argument("--check", action="store_true", help="compare the files in data/crypto/ with the fingerprint")
    ap.add_argument("--write-fingerprint", action="store_true", help="save the fingerprint of the files in data/crypto/")
    args = ap.parse_args()

    if args.check or args.write_fingerprint:
        fp = fingerprint(pd.read_parquet(OUT / "perps_daily.parquet"), pd.read_parquet(OUT / "perps_funding.parquet"))
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

    t0, start, end = time.time(), pd.Timestamp(START), pd.Timestamp(END)
    month = lambda key: pd.Timestamp(key[-11:-4] + "-01")
    with requests.Session() as s:
        syms = args.symbols.split(",") if args.symbols else all_usdt_perps(s)
        print(f"Listing monthly files for {len(syms)} symbols ...")
        with ThreadPoolExecutor(args.workers) as ex:
            k_keys = dict(zip(syms, ex.map(lambda x: list_s3(s, KLINES.format(s=x), "keys"), syms)))
            f_keys = dict(zip(syms, ex.map(lambda x: list_s3(s, FUNDING.format(s=x), "keys"), syms)))
            m_keys = dict(zip(syms, ex.map(lambda x: list_s3(s, MARK.format(s=x), "keys"), syms)))
        k_jobs = [(x, k) for x, ks in k_keys.items() for k in ks if start <= month(k) <= end]
        f_jobs = [(x, k) for x, ks in f_keys.items() for k in ks if start <= month(k) <= end]
        m_jobs = [(x, k) for x, ks in m_keys.items() for k in ks if start <= month(k) <= end]
        kl = run(s, k_jobs, klines, args.workers, "klines ")
        fu = run(s, f_jobs, funding, args.workers, "funding")
        mk = run(s, m_jobs, mark, args.workers, "mark   ")

    kl = kl[(kl["date"] >= start) & (kl["date"] <= end)].drop_duplicates(["symbol", "date"], keep="last")
    zero = int((kl["quote_volume"] <= 0).sum())
    kl = kl[kl["quote_volume"] > 0]
    holes = missing_days(kl)
    if holes:
        with requests.Session() as s:
            extra = run(s, [(x, DAILY_KLINES.format(s=x, d=dd)) for x, dd in holes], klines, args.workers, "missing days")
        if len(extra):
            kl = pd.concat([kl, extra[extra["quote_volume"] > 0]]).drop_duplicates(["symbol", "date"], keep="first")
    repairs = {"zero_volume_dropped": zero, "missing_days": len(holes), "missing_days_filled": len(holes) - len(missing_days(kl))}
    fu = fu[(fu["time"] >= start) & (fu["time"] < end + pd.Timedelta(days=1))].drop_duplicates(["symbol", "time"], keep="last")
    fu = fu[["symbol", "time", "rate", "interval_hours"]].sort_values(["symbol", "time"]).reset_index(drop=True)

    if len(mk):
        kl = kl.merge(mk.drop_duplicates(["symbol", "date"], keep="last"), on=["symbol", "date"], how="left")
    else:
        kl = kl.assign(mark_open=np.nan, mark_high=np.nan, mark_low=np.nan, mark_close=np.nan)
    holes = kl.loc[kl["mark_close"].isna(), ["symbol", "date"]]          # the monthly mark files miss whole days too
    if len(holes):
        with requests.Session() as s:
            extra = run(s, [(x, DAILY_MARK.format(s=x, d=dd)) for x, dd in holes.itertuples(index=False)], mark, args.workers, "missing mark")
        if len(extra):
            kl = kl.set_index(["symbol", "date"])
            kl.update(extra.drop_duplicates(["symbol", "date"]).set_index(["symbol", "date"]))
            kl = kl.reset_index()
    repairs["mark_days_missing"] = len(holes)
    repairs["mark_days_filled"] = len(holes) - int(kl["mark_close"].isna().sum())
    day = fu.assign(date=fu["time"].dt.normalize()).groupby(["symbol", "date"])["rate"].agg(funding_rate="sum", funding_prints="size")
    daily = kl.merge(day.reset_index(), on=["symbol", "date"], how="left")
    daily["funding_prints"] = daily["funding_prints"].fillna(0).astype(int)      # funding_rate stays NaN when no print
    daily = daily[["date", "symbol", "open", "high", "low", "close", "quote_volume",
                   "mark_open", "mark_high", "mark_low", "mark_close", "funding_rate", "funding_prints"]]
    daily, fu = split_relistings(daily, fu)
    daily = daily.drop(columns="ticker").sort_values(["date", "symbol"]).reset_index(drop=True)

    meta = daily.groupby("symbol")["date"].agg(first_day="min", last_day="max", days="size").reset_index()
    meta.insert(1, "ticker", meta["symbol"].str.split(".").str[0])
    meta["multiplier"] = meta["ticker"].map(multiplier)
    meta = underlying_types(meta)
    repairs["relisted_tickers"] = sorted(meta.loc[meta["symbol"].str.contains(r"\."), "ticker"].unique().tolist())

    OUT.mkdir(parents=True, exist_ok=True)
    daily.to_parquet(OUT / "perps_daily.parquet", index=False)
    fu.to_parquet(OUT / "perps_funding.parquet", index=False)
    meta.to_csv(OUT / "perps_meta.csv", index=False, date_format="%Y-%m-%d")
    quality_report(daily, fu, meta, repairs)
    print(f"Saved {len(daily):,} daily rows and {len(fu):,} funding prints for {len(meta)} symbols "
          f"in {time.time() - t0:,.0f} s. Read data/crypto/quality_report.md.")


if __name__ == "__main__":
    main()
