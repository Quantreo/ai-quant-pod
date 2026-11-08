---
type: data
dataset: rates
---

# Rates monthly

**Source**: FRED, OECD Main Economic Indicators, 3-month interbank rates (IR3TIB01xxM156N). **Build**: `poetry run python data/get_rates.py` (seconds). **Load**: `lab.data.load("rates", test_start=...)`.

## File (data/rates/)

| File | One row per | Columns |
| --- | --- | --- |
| rates_monthly.parquet | currency, month (first day) | rate, % a year |

## Coverage

2009-01 to 2026-09 for USD, CAD, CHF, NOK, NZD, SEK; AUD and JPY to 2026-08; **EUR and GBP stop in 2026-01** (series no longer updated by the OECD).

## Known issues

- A monthly average is known only after the month ends: lag it one month in any signal.
- An interbank rate approximates what an FX forward really pays; say so in any carry result.
- EUR and GBP after 2026-01: to complete with the overnight rates (euro short-term rate, SONIA), not done yet.
