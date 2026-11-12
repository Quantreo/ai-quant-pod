## Data check (Pass 1 v5)

**Verdict: ready with reserves** · 2026-10-25 · data before 2025-01-01; test: coverage only (846 names, 2025-01 to 2026-09). Data unchanged since the v4 check: its issues 1 to 8 (Sunday row, no-print names, print-level funding, mark holes, delisting, churn, ties, multipliers) still hold. Below, what v5 adds.

**Load**: `crypto_daily`, `crypto_funding`, `crypto_mark_hourly`, `perps_meta` · `crypto_universe(daily, top=30, volume_window=30, min_age_days=90, min_names=20)` · train 2021-2023, validation 2024.
**Universe**: 30 names every week from 2021-01 (the 19 flat weeks are in 2020). Train: 157 Sunday rows, 156 Wednesday rows. 2021: 78 distinct names, 6 present all 52 weeks.

| # | Issue | Evidence | Instruction |
| --- | --- | --- | --- |
| 9 | `tier_cost` maps tiers the other way | `sign > 0` (long) gets `thin_bp` 20, short gets 5: Thin Losers buys thin losers. Here short 20, long 5. Volume rank 2021-23 (1 = most liquid): top funding quintile 17.1, bottom 15.4, no liquidity gap in the data | Swap the tiers before use; the stresses (both 20, thin 40) need the swapped version. Thin short tail stays a hypothesis |
| 10 | Forced 12.5 bp not in the tier | `forced` and `gone` are computed, never used; liquidation fee comes from the lab; a delisting exit pays the side tier | Charge delisting exits 12.5 bp or state they pay the tier |
| 11 | Wednesday row | Weight dated Wednesday trades at its close: use the Wednesday row. Wed row vs Tue row: 0.51 new names a week (max 2); vs Sunday row: 1.2 (max 3) | Rebuild on the Wednesday row, never Thursday's. Signal: prints in (t-7d, t], t = Thursday 00:00. Price: marks Wed close to Fri close |
| 12 | Placebo state | v4 has a 10% band: weights depend on the held book | Form each Wednesday book from zero, 48 h, zero cost, zero funding; liquidation on mark high and low |
| 13 | Funding gaps | No print in the window: 28 name-weeks Sunday, 30 Wednesday (ICPUSDT, TLMUSDT, BNXUSDT); over 21 prints (4h): 382 and 383 | Out of ranking and book (29 names); per print |
| 14 | Dying legs inside 48 h | FTTUSDT: Sunday row 2022-11-13, last bar 11-14. LUNAUSDT: Wednesday row 2022-05-11, last bar 05-12 (Sunday book 05-08 in v4 #5) | Same rule in both books: liquidation first, else mark_close of last bar; never `last_day`; report apart, P3 reads 2022 |
| 15 | Pumps can decide P1 | 48 h mark moves above 50%: Sunday 15 of 4709 name-windows, Wednesday 13 of 4679. Wednesday: DOGE 2021-01-27 +516%, 2021-04-14 +201%, BNB 2021-02-17 +102%. Sunday: BEL 2022-06-05 +124% | Report P1 and #3 without the top 5 weeks. The 50.9 of 61.9 points is a return: not checked here |
| 16 | Hourly mark | TLMUSDT is the only universe name (1 of 142) absent; daily mark missing in a 48 h window: 1 of 4710, 1 of 4680 | Daily marks for P1; last-price fallback on market-wide hole days only, logged |
| 17 | P1 calibration sample | "61.5 points over 182 weeks" is 2020-07 to 2023; train is 156 weeks | Recompute the 0.16 on 2021-2023 |

**Trials.csv, this sheet**: 3 rows, all 2026-10-25, the hourly fills (111314/111321/111328), counts no. The 4 earlier tries (base, V1 to V3, 2026-10-23) are in `Research Log.md` only; the file (+89 uncommitted lines) has no row for them. Cause not established, probably a backfill that took only the later diagnostics. Not edited. The count of 5 lives in Pass 1 text only. `results/crypto_funding_carry/` (43 runs): read only, not used.

**Harmless**: 37 one-bar moves above 80% and 521 funding prints above 1% (real pumps, squeezes); fingerprint file missing; ICPUSDT.2 enters after its own age.
