## Data check

**Verdict: ready with reserves** · 2026-11-08 · data before 2025-01-01 only; test period: coverage counted, not read. Short Pass 1: only the base was checked. Review round 1 rows are all answered (fixed or partly fixed), Pass 1 v2 is stable.

**Load**: `load("crypto_daily", test_start="2025-01-01")` · `crypto_universe(daily, top=30, volume_window=30, min_age_days=60, min_names=30)` (types COIN by default) · funding for the P&L split: `crypto_funding`.

| Need (Pass 1) | Dataset | Field | Period | Status |
| --- | --- | --- | --- | --- |
| 7-day max daily return, 90-day beta | crypto_daily | mark_close | 2020-10 to 2024-12 | ok, 0 missing bar on universe names after 2021 |
| Volume rank | crypto_daily | quote_volume | same | issue 1 |
| Funding in the split | crypto_daily, crypto_funding | funding_rate | 2021-01 to 2024-12 | issue 3 |
| Delisted names | crypto_daily | all | same | ok, kept (LUNA, FTT) |
| Test period | crypto_daily | all | 2025-01 to 2026-09 | coverage ok (587 then 797 names) |

**Universe** (top 30, 30 d, age 60, min 30): 2021 to 2024 exactly 30 names on every Monday, 0 flat weeks (the 34 flat Mondays are all 2020, before train). Entries 2.5 and exits 2.3 per rebalance. 189 names ever in, all COIN, 1 relisted ticker (ICPUSDT.2). Weakest rank-30 volume: USD 44 to 69 million a day by year. 8 multiplier names (1000SHIB, 1000PEPE...). Generic check: 0 inconsistent bars, 0 flat price runs, 0 zero volume.

| # | Issue | Evidence | Effect on the test | Instruction to the Developer |
| --- | --- | --- | --- | --- |
| 1 | Pass 1 says median volume, `crypto_universe` ranks by mean | Mondays 2021-24: overlap of the two top-30 sets min 21, median 27 of 30 | Up to 9 names differ; the mean lets one volume spike in | Use the function as is and write "mean" in the result, or ask the Economist to change Pass 1. Do not write a private median ranking |
| 2 | BTC and the top 30 | BTCUSDT is in the universe all 1461 days; the function has no exclusion | Pass 1 excludes BTC but does not say top 30 before or after | Drop BTC after the ranking (29 names) unless Economist says otherwise; min 5 names in the leg and quintile of 6 need the rule stated |
| 3 | Missing funding on held names | 237 universe days with no print: ICPUSDT 172 (2021-07-10 to 2022-02-26), BNXUSDT 29 (2022-12 to 2023-01), TLMUSDT 36 (2021-09 to 12) | Funding split silently short on those days (gate is price-only, so the gate is not hit) | Book those days as NaN funding, flag them in the split, never zero |
| 4 | Dead name crashes | LUNAUSDT 2022-05-12 mark vs last close gap 96%; FTTUSDT 2022-11-14 gap 6% | A delisted mid-week leg coin, or a crash, sets the P&L of that week | Use the mark price, close at last mark price per Pass 1; keep both names, do not drop the weeks |
| 5 | Funding timing and intervals | Prints every 8 h (557k), 4 h (89k), 2 h (246) on universe names | Daily sum mixes old and new position on the Tuesday fill day | Fill at the Tuesday 00:00 close: prints before it belong to the old position; use `crypto_funding` at print level, per actual interval |

**Harmless warnings**: 37 moves above 80% (UNFIUSDT +450%, DOGEUSDT 2021-01-28): in the universe, DOGE is real; 29 universe-name days, real pumps, kept by the sheet's rule. BNXUSDT 10-bar hole 2023-02-22: one name, handled by "needs all 7 returns". USDCUSDT 1 day without funding: not in the universe. Thin 2020: before train.

**New trap for `reference/checks.md`**: none new. Suggested sharpening: "Pass 1 volume statistic (median or mean) must match `crypto_universe`, which uses the mean".
