---
type: data
dataset: crypto_daily, crypto_funding
---

# Crypto perps daily

**Source**: Binance Vision public archive (data.binance.vision), CC BY-NC-SA 4.0: each user downloads it for their own non-commercial research.
**Build**: `poetry run python data/get_crypto_daily.py` (15 to 45 minutes the first time, cached after). **Load**: `lab.data.load("crypto_daily", test_start=...)`.

## Files (data/crypto/)

| File | One row per | Columns |
| --- | --- | --- |
| perps_daily.parquet | symbol, UTC day | open, high, low, close (last price), quote_volume (USDT), mark_open, mark_high, mark_low, mark_close (mark price), funding_rate (sum of the day's prints, NaN if none), funding_prints |
| perps_funding.parquet | funding print | symbol, time (UTC), rate, interval_hours |
| perps_meta.csv | symbol | ticker, first_day, last_day, days, multiplier, underlying_type, type_source |

## Which price

The desk backtests on the **mark price**: signals, volatility, risk, liquidation and P&L. Binance builds it from an index of spot exchanges, uses it for liquidations and unrealised P&L, and it ignores the wicks of a single order book (2021-05-19: ETH last price low 1,400 for an open of 3,377). At a daily close the mark and the last price differ by a few basis points on liquid names; the cost assumption covers the spread and the slippage of the real fill.

The **last price** stays in the file: to measure the gap with the mark (a diagnostic), and as a fallback on the rare days with no mark price.

## Coverage

2020-01 to 2026-09, every USDT perpetual ever listed, dead ones included. Names with data per day: median about 30 in 2020, 117 in 2021, 143 in 2022, 197 in 2023, 284 in 2024, 484 in 2025 (first build, before repairs).

## Repairs made by the build

- Zero-volume days dropped: delisted contracts keep flat bars in the archive for years (161 dead names, not 31).
- Days missing from the monthly files filled from the daily files when they exist (2022-02-26 to 28, 2022-04-01 to 02, 2025-03-28 to 30 for about 50 names).
- A ticker silent for more than 30 days that comes back is a new listing: `SYMBOL.2` (LIT, CVX, ICP, TLM, AIA, CTK, CVC, MAVIA, SLP).

## Known issues

- **Not only coins**: since late 2025 Binance lists perps on stocks, metals, indices and pre-IPO names. `perps_meta.csv` has `underlying_type` (from the exchange for listed contracts; a delisted contract from before 2025-12 is assumed a coin) and `lab.universe.crypto_universe` keeps coins only by default.

- Funding interval of 8, 4, 2 or 1 hour, changing for many names: annualise per actual print.
- Some days with a price and no funding print (TLM, ICP, BNX before repairs): check the names a strategy holds.
- One-day moves above 80% are mostly real pumps of small alts; the relisted tickers are split.
- Daily bars only: the intraday path inside a day is unknown.

## Hourly mark price (optional)

`poetry run python data/get_crypto_hourly_mark.py --strategy <results folder>` downloads hourly mark candles for the names a strategy held only, into `data/crypto/mark_hourly.parquet` (time, symbol, open, high, low, close). Load with `lab.data.load("crypto_mark_hourly", test_start=...)`. For questions inside the day: a fill a few hours after 00:00, a liquidation path.

## Intraday bars (hourly, one-minute)

`poetry run python data/get_crypto_intraday.py --interval 1h --top 50` builds `data/crypto/perps_1h.parquet` (time, symbol, last-price OHLC, quote_volume, mark OHLC) for every coin ever in the top 50 by 30-day volume; `--interval 1m` builds `perps_1m.parquet`, 60 times larger: a few names and years at a time. Load with `lab.data.load("crypto_1h" | "crypto_1m", test_start=...)`. Bars with no trade are dropped. Funding stays in `crypto_funding`: most bars have no print.
