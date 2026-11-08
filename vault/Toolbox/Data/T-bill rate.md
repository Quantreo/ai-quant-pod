---
type: data
dataset: tbill
---

# T-bill rate

**Source**: FRED, 3-month Treasury bill, secondary market (`TB3MS`). **Build**: `poetry run python data/get_rates.py` (same script as the rates, CPI and policy rates, seconds). **Load**: read `data/rates/tbill.parquet` (not yet in `lab.data`).

## File (data/rates/)

| File | One row per | Columns |
| --- | --- | --- |
| tbill.parquet | series, month (first day of month) | series (USD_TB3M), rate (% a year, monthly average) |
| tbill_quality_report.md | series | id, first, last, months, stale flag |

## Coverage (kept from 2004-01)

| Series | FRED id | Native freq | FRED span | Kept |
| --- | --- | --- | --- | --- |
| USD_TB3M | TB3MS | monthly | 1934-01 to 2026-09 | 2004-01 to 2026-09 (273) |

## Probe

| Id | Freq | First | Last | Decision |
| --- | --- | --- | --- | --- |
| DTB3 | daily | 1954-01-04 | 2026-10-22 | not used: TB3MS is its monthly average, same convention as the other monthly rates |
| TB3MS | monthly | 1934-01 | 2026-09 | used |

## Known issues

- Discount basis, % a year, not a bond-equivalent yield: slightly below the investment yield (a few bp at low rates, more at high rates). Fine as a cash proxy, to be said in any result.
- Monthly average of the month, so the value for month m is not known at the start of m. For a cash return earned over month m, use the value of m-1 (or accept the small look-ahead and say it).
- No vintages; the series is not revised in practice.
- Kept from 2004 to leave a margin before a 2005 start.
