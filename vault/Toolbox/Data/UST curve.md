---
type: data
dataset: ust_curve
---

# US Treasury curve

**Source**: FRED, constant-maturity Treasury yields, monthly series GS* (monthly average of the daily DGS*). **Build**: `poetry run python data/get_rates.py` (same script as the rates, CPI, policy and T-bill rates, seconds). **Load**: read `data/rates/ust_curve.parquet` (not yet in `lab.data`).

## File (data/rates/)

| File | One row per | Columns |
| --- | --- | --- |
| ust_curve.parquet | series, month (first day of month) | series (UST_1Y ... UST_30Y), rate (% a year, monthly average) |
| ust_curve_quality_report.md | series | id, first, last, months, stale and gap flags |

## Coverage (kept from 2004-01; 273 months each, no gap, last 2026-09)

| Series | FRED id | FRED span (monthly) | Series | FRED id | FRED span (monthly) |
| --- | --- | --- | --- | --- | --- |
| UST_1Y | GS1 | 1953-04 | UST_10Y | GS10 | 1953-04 |
| UST_2Y | GS2 | 1976-06 | | | |
| UST_3Y | GS3 | 1953-04 | UST_20Y | GS20 | 1953-04 (801 obs, gap 1987-01 to 1993-09) |
| UST_5Y | GS5 | 1953-04 | UST_30Y | GS30 | 1977-02 (596 obs, no gap) |
| UST_7Y | GS7 | 1969-07 | 3-month | TB3MS | in `tbill.parquet` |

## Probe (daily ids, all to 2026-10-22)

| Id | First | Decision |
| --- | --- | --- |
| DGS1MO | 2001-07 | not used |
| DGS3MO, DGS6MO | 1981-09 | not used: 3M is TB3MS (already stored), 6M outside the ladder |
| DGS1, DGS3, DGS5, DGS10 | 1962-01 | monthly GS twin used |
| DGS2 | 1976-06 | GS2 used |
| DGS7 | 1969-07 | GS7 used |
| DGS20 | 1962-01 (gap 1987-93) | GS20 used |
| DGS30 | 1977-02 | GS30 used |

## Known issues

- Monthly average of the month, not end of month: the value for month m is not known at the start of m. Use m-1 in a signal.
- Constant-maturity yields (par, bond-equivalent), not returns of a bond or ETF: no price, roll-down or convexity. Duration and ladder returns must be approximated and said so in any result.
- The 20Y has a source gap 1987-1993, outside the kept window.
- No vintages; not revised in practice.
