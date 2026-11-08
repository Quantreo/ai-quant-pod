---
type: data
dataset: cpi
---

# CPI

**Source**: FRED. OECD MEI all-items CPI (`*CPIALLMINMEI`, `*CPIALLQINMEI`), Eurostat HICP (`CP0000..M086NEST`), BLS (`CPIAUCNS`). **Build**: `poetry run python data/get_rates.py` (same script as the rates, seconds). **Load**: read `data/rates/cpi.parquet` (not yet in `lab.data`).

## File (data/rates/)

| File | One row per | Columns |
| --- | --- | --- |
| cpi.parquet | currency, observation (first day of month, or of quarter for AUD, NZD) | freq (M or Q), cpi (index level, NSA) |
| cpi_quality_report.md | currency | series, first, last, obs, stale and gap flags |

## Coverage (from 2007-01)

| Currency | Series | Freq | Last | State |
| --- | --- | --- | --- | --- |
| USD | CPIAUCNS | M | 2026-09 | 2025-10 missing (not published) |
| EUR | CP0000EZCCM086NEST | M | 2026-09 | HICP, euro area in changing composition |
| CHF, NOK, SEK | CP0000{CH,NO,SE}M086NEST | M | 2026-09 | Eurostat HICP, not the national CPI |
| GBP | GBRCPIALLMINMEI | M | 2025-03 | **stale** |
| CAD | CANCPIALLMINMEI | M | 2025-03 | **stale** |
| JPY | JPNCPIALLMINMEI | M | 2021-06 | **stale** |
| AUD, NZD | AUSCPIALLQINMEI, NZLCPIALLQINMEI | Q | 2025-01 | **stale** |

## Known issues

- **GBP, CAD, JPY, AUD, NZD stop in 2021 to 2025**: the OECD no longer updates them on FRED. No FRED series found that continues them (UK HICP `CP0000GBM086NEST` stops 2020-11). Needs another source, to be chosen by the human gate: ONS, Statistics Canada, e-Stat Japan, ABS, Stats NZ.
- **No publication dates**: FRED gives no vintages in this script. Apply a fixed lag in the signal (the sheet uses one quarter). Real lags (not checked here): about 2 weeks (US, EA, SE, NO, CH, CA, JP, UK), one quarter for AUD, NZD.
- CHF, NOK, SEK are HICP, not the national CPI named in the sheet.
- Revision policy not recorded; NSA all-items indexes are revised little [hypothesis].
