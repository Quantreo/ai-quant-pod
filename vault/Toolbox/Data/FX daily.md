---
type: data
dataset: fx_daily
---

# FX daily

**Source**: FRED (Federal Reserve Bank of St. Louis), H.10 release of the Federal Reserve: noon New York buying rates. **Build**: `poetry run python data/get_fx_daily.py` (seconds). **Load**: `lab.data.load("fx_daily", test_start=...)`.

## File (data/fx/)

| File | One row per | Columns |
| --- | --- | --- |
| fx_daily.parquet | pair, business day | close (noon New York) |

## Coverage

2008-01 to 2026-09, nine majors: EURUSD, GBPUSD, AUDUSD, NZDUSD (dollars per unit), USDJPY, USDCHF, USDCAD, USDNOK, USDSEK (units per dollar). Crosses are computed from them.

2026-10-25: START moved from 2010-01-01 to 2008-01-01 (FX Value needs the 2008 crisis). Rows from 2010-01-04 on are byte-identical to the old file; 2008-2009 adds 4,536 rows, no NaN, only holiday gaps (19 weekdays per pair).

## Conventions and known issues

- One price a day, at noon New York, not the 17:00 New York close of the FX market. A strategy trades at that price, the next day at the earliest.
- No bid and ask, no high and low: costs come from `vault/Toolbox/Cost Assumptions.md`; no intraday stop or path.
- US holidays have no rate (about 10 weekdays a year).
- A return in USD terms needs the inversion for USDJPY, USDCHF, USDCAD, USDNOK, USDSEK.
- Carry needs `data/get_rates.py`: price returns alone miss the interest differential.
- Why not Dukascopy: its public feed throttles hard (HTTP 429, timeouts of a minute); the hourly bid/ask script is kept in `data/optional/` for those who need intraday data.

## For the engine

`lab.fx.fx_bars(fx)` turns the pairs into nine currencies priced in dollars per unit (JPY = 1 / USDJPY), so a long is long the currency and every P&L is in dollars; `lab.fx.fx_carry(fx, rates)` gives the carry as daily prints (the rate differential, previous month, weekends included), to pass to `lab.backtest` as the funding. Rebalance on business days with a price.
