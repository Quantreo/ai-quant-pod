---
type: data
dataset: policy
---

# Policy rates

**Source**: FRED. ECB main refinancing rate (`ECBMRRFR`), ECB deposit facility rate (`ECBDFR`), effective Fed funds rate (`FEDFUNDS`). **Build**: `poetry run python data/get_rates.py` (same script as the rates and the CPI, seconds). **Load**: read `data/rates/policy.parquet` (not yet in `lab.data`).

## File (data/rates/)

| File | One row per | Columns |
| --- | --- | --- |
| policy.parquet | series, month (first day of month) | series (ECB_MRO, ECB_DFR, USD_FFR), rate (% a year, monthly average) |
| policy_quality_report.md | series | id, first, last, months, stale flag |

## Coverage (kept from 2009-01)

| Series | FRED id | Native freq | FRED span | Kept | Note |
| --- | --- | --- | --- | --- | --- |
| ECB_MRO | ECBMRRFR | daily | 1999-01 to 2026-10-23 | 2009-01 to 2026-10 (214) | daily step series, calendar-day fill, then monthly mean |
| ECB_DFR | ECBDFR | daily | 1999-01 to 2026-10-23 | 2009-01 to 2026-10 (214) | same |
| USD_FFR | FEDFUNDS | monthly | 1954-07 to 2026-09 | 2009-01 to 2026-09 (213) | already a monthly average of the effective rate |

## Known issues

- **Last month is partial** for the ECB series (2026-10 is a mean of the days so far).
- Monthly mean matches the "monthly average" convention of the OECD 3-month series, so the spread (3m minus policy) is on the same footing. The 3m EUR fixing is not the same instrument as MRO or DFR; which one to subtract (MRO, DFR, or the mid) is the Developer's choice, to be written before the run. In 2011-12 they differ by 75 bp.
- Probed and not used: `DFEDTARU`/`DFEDTAR` (Fed target, daily, upper bound only after 2008-12), `DFF`/`EFFR` (daily effective), `ECBMLFR` (marginal lending), `IRSTCI01EZM156N` (OECD EA immediate rate, monthly, stops 2026-01). `IRSTCB01*` ids did not return a CSV (not found).
- No publication dates, no vintages: policy rates are known in real time, so no lag is needed beyond the month-average convention.
