## Build

**Code**: `strategies/crypto_funding_carry.py` · sha `8ada54c6f9b2` · built 2026-10-23 on Pass 1 v4

**Gate (1.11 #1 and #2)**: luck line 0.56 + measured turnover 46.6/yr × 10 bp / 20% volatility (0.233) → bar 0.793; measured gross Sharpe 1.327 → **pass**. Funding share of gross P&L 0.581 (58.75% funding, 42.34% price, train) against at least 0.5 → **pass**.

| Choice | Pass 1 | Code | Data check |
| --- | --- | --- | --- |
| Periods | 1.10 | Train 2020-07-01 to 2023-12-31, validation 2024, `load(..., test_start="2025-01-01")` | Load line |
| Rebalance | 1.5b rebalance time | Weight dated Sunday, traded at its close (Monday 00:00 UTC) | #1 |
| Universe | 1.4, 1.5b | `crypto_universe(top=30, volume_window=30, min_age_days=90, min_names=20)`, Sunday row | #1 |
| Missing funding | 1.5b | A name with no print in the window leaves the ranking and the book that week | #2 |
| Signal | 1.5, 1.5b funding window | Sum of prints in (t - 7d, t], t = Monday 00:00, × 365/7, at print level | #3 |
| Ties | 1.5b tie rule | 7-day sums rounded to 1e-10, average rank | #7 |
| Portfolio | 1.5 | Rank minus its mean, long the lowest funding, short the highest | none |
| Per-name volatility | 1.5b | 60-day standard deviation of daily mark returns (last close where mark missing), 60 returns required | #4, #8 |
| Leg neutrality | 1.5, 1.5b | Rank weight / volatility; each leg scaled to the same notional | none |
| Book volatility | 1.5, 1.5b | 60-day sample covariance of daily returns on the target weights, scaled to 20% a year (×365) | #4 |
| Gross cap | 1.5b | Scaled down to 3× if above; never bound on train (max gross 2.15) | none |
| Band | 1.5b band width, band exit | `band=0.10`, `band_to="edge"` | none |
| Margin, liquidation | 1.5b margin reset, liquidation cost; 1.8 | `leverage="gross"`, margin reset at every rebalance; maintenance 0.5% plus 10 bp on the liquidated notional, charged by the lab | #4, #5 |
| Delisting | 1.8 | Lab: liquidation first, else exit at the last mark close; no filter on `last_day` | #5 |
| Costs | 1.7 | 10 bp one way, every trade from the first | none |
| V1 | 1.9, 1.5b V1 neutralisation | 60-day beta to BTCUSDT per name; long leg × (short beta exposure / long beta exposure), skipped if a leg beta is 0 or less; then target and cap | none |
| V2 | 1.9, 1.5b V2 threshold | Dispersion = cross-sectional std of the annualised signal over the eligible names, at every Sunday from the start of the data; trade only above the expanding median of past Sundays, current excluded | none |
| V3 | 1.9, 1.5b V3 hedge ratio | Short leg only, long BTCUSDT at the 60-day beta of the short leg, BTC netted; then target and cap | none |
| Survivorship control | 1.4, 1.9 | Top 30 of the last universe row in the loaded data (2024-12-31), names with a bar each day, flat below 20 | none |

**Data check instructions applied**: #1 Sunday row, prices and volatility up to Sunday's close; #2 names with zero prints dropped (and none dropped for a missing volatility); #3 print level, prints strictly after t paid by the new position (lab); #4 mark everywhere, last price only where the mark is missing; the lab counted 0 fallback days for held names (the market-wide days listed in #4 carry a mark in the current file); #5 LUNA long, rank-weighted 0.053 of capital from 2022-05-08 (ref 64.26), liquidated on 2022-05-11 at 9.70, about -4.5% of capital; FTT long 0.026 bought at the 2022-11-13 close, exited at the last mark close of 2022-11-14 (1.49), about 0 before cost, the actual settlement not in the data; #6 measured turnover put in the gate; #7 rounding and average rank; #8 returns as price ratios.

**Look-ahead checks**: file read against the Data check and the timing convention (a weight dated d uses the universe row, prices and volatility up to the close of d, prints up to 00:00 of d+1). Truncation test PASS on 12 trade days for base, v1, v2 and v3, on train and on validation.

| Run | Period | Variant | Gross Sharpe | Net Sharpe | Turnover/yr | Funding share | Liquidations |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20261023-095235-train-base | train | base (gate) | 1.327 | 1.098 | 46.6 | 0.581 | 25 |
| 20261023-095242-validation-base | validation | base | 2.195 | 1.908 | 48.5 | 0.170 | 5 |
| 20261023-095244-train+validation-base | train+validation | base | 1.469 | 1.231 | 46.8 | 0.472 | 30 |
| 20261023-095246-validation-v1 | validation | V1 BTC-beta neutral | 2.859 | 2.585 | 51.8 | 0.102 | 6 |
| 20261023-095248-validation-v2 | validation | V2 dispersion filter | 0.152 | -0.087 | 21.1 | 2.209 | 0 |
| 20261023-095250-validation-v3 | validation | V3 short leg + BTC | 2.192 | 2.076 | 21.3 | 0.009 | 3 |
| 20261023-095252-train+validation-base-cost5.0 | train+validation | stress: 5 bp | 1.469 | 1.343 | 46.8 | 0.472 | 30 |
| 20261023-095255-train+validation-base-cost20.0 | train+validation | stress: 20 bp | 1.469 | 1.005 | 46.8 | 0.472 | 30 |
| 20261023-095257-train+validation-base-top20 | train+validation | stress: top 20 | 1.587 | 1.380 | 39.7 | 0.385 | 6 |
| 20261023-095300-train+validation-base-top50 | train+validation | stress: top 50 | 1.790 | 1.508 | 57.2 | 0.451 | 83 |
| 20261023-095302-train+validation-base-age60 | train+validation | stress: listing age 60 | 1.450 | 1.219 | 45.7 | 0.466 | 26 |
| 20261023-095305-train+validation-base-age180 | train+validation | stress: listing age 180 | 1.270 | 1.047 | 45.4 | 0.511 | 28 |
| 20261023-095307-train+validation-base-fw3 | train+validation | stress: funding window 3 d | 1.516 | 1.253 | 52.6 | 0.442 | 28 |
| 20261023-095310-train+validation-base-fw30 | train+validation | stress: funding window 30 d | 1.118 | 0.985 | 25.2 | 0.566 | 24 |
| 20261023-095312-train+validation-base-band0.0 | train+validation | stress: band 0 | 1.538 | 1.276 | 54.2 | 0.451 | 33 |
| 20261023-095315-train+validation-base-band0.2 | train+validation | stress: band 20% | 1.418 | 1.203 | 40.3 | 0.480 | 22 |
| 20261023-095317-train+validation-base-todaytop | train+validation | control: today's top 30 | 0.388 | 0.182 | 40.4 | 0.860 | 29 |
| 20261023-095319-train-base-delay1 | train | control: one day late | 0.794 | 0.572 | 46.5 | 0.902 | 21 |

**Superseded runs**: 17 runs from 20261023-095104 to 20261023-095155 (the same list) charged the liquidation cost twice: the lab started charging it at 09:48 and the strategy file still added it. Fixed in the file (a bug fix, not a try), all rerun; saved, not used, logged as one grouped line (agreed by the user on 2026-10-23).

**Measured turnover**: 46.6/yr on train against 95.2/yr in 1.7. The mean gross book is 1.12× capital (1.7 reference 2×), which explains most of the gap; the bar of 1.11 #1 falls from 1.04 to 0.79.

**Not run**: the turnover cases of 1.7 (replaced by the measured turnover, as 1.9 says). Pass 1 does not say on which period the stress tests run: they ran on train plus validation, the whole period open to the desk; agreed by the user on 2026-10-23. The diagnostics of 1.10 and the criteria 1.11 #3 and #4 belong to the Analyst.

## 2026-10-25 · Diagnostic: fill at 01:00 and 04:00 UTC (Red team finding 1)

Read-only, not a gate, not a try (counts no in Trials.csv). Code `strategies/crypto_funding_carry_fill.py` (imports the base file, sha 8ada54c6f9b2, weights unchanged). Train 2020-07 to 2023-12 only; hourly mark file read with a filter below 2024-01-01. Test never opened. Status of the sheet unchanged.

| Fill (Monday UTC) | Run | Gross Sharpe | Net Sharpe (10 bp) | Funding share | Price P&L pts | Monday price pts (new book) | Tue | Wed to Sun |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00:00 daily close, daily bars (gate) | 20261023-095235-train-base | 1.327 | 1.098 | 0.581 | 42.3 | 39.2 | 22.3 | -19.2 |
| 00:00, hourly bars (calibration) | 20261025-111314-train-fill00h | 1.345 | 1.116 | 0.586 | 42.2 | 40.4 | 23.4 | -21.5 |
| 01:00 | 20261025-111321-train-fill01h | 1.372 | 1.146 | 0.580 | 43.7 | 44.0 (38.1 incl. old book -5.8 in hour 0) | 23.8 | -18.3 |
| 04:00 | 20261025-111328-train-fill04h | 1.333 | 1.109 | 0.591 | 41.5 | 37.9 (38.2 incl. old book) | 23.0 | -18.2 |

**Reading (facts only)**: the Monday price P&L survives both later fills: 44.0 and 37.9 points on the new book against 40.4 at 00:00, Tuesday unchanged (23 to 24). Gross Sharpe stays 1.33 to 1.37 and the funding share 0.58 to 0.59. So the Monday effect is not an artefact of the fill at 00:00 on the print: it is still there when the book is bought 1 and 4 hours later. It does not say what the effect is (finding 1, Economist side). The hourly engine replays the daily gate within 0.02 Sharpe (1.345 vs 1.327; hourly liquidation checks and hourly compounding).

**Limits**: (1) Costs: Pass 1 1.7 gives one flat 10 bp for every name and the lab takes one `cost_bp`; the desk's tier schemes (5 bp ranks 1 to 25, 10 bp beyond) belong to other sheets, so I did not invent one here. Net is flat 10 bp, the headline is gross, which carries no cost. If a per-leg tier is wanted, Pass 1 must write it. (2) One name (ICPUSDT.2) is weighted but has no hourly bar in the calibration run, so it was never traded there (absent in 01:00 and 04:00 runs); small. (3) Hours 1 to 4 of Monday are filled at the hourly mark close, with no spread or slippage beyond the flat cost. (4) Truncation test not rerun: weights are the same function, only dated later.

## 2026-10-25 · v5.1 train gate (Pass 1 v5.1)

**Code**: `strategies/crypto_funding_carry_v5.py` sha `41e5e4341000`; weights from `crypto_funding_carry.py`, unchanged (sha 8ada54c6f9b2). Lab sha 0fdde9124197 on all runs. Data cut at 2023-12-31 before any build; test never opened.
**Scored**: first weight Sunday 2021-01-03, last 2023-12-31, 157 weights, 2.99 years (warm-up before 2021 is signal only). P1: 156 pairs, Sunday d with Wednesday d+3 (my pairing; the last Sunday is out, its 48 h leave the train).
**Look-ahead**: truncation test PASS on 12 Sunday days and 12 Wednesday days. Tier rebuild checked against the engine's traded notional each day: max abs diff 0.0.

| Gate | Bar | Measured | Result |
| --- | --- | --- | --- |
| #1 net Sharpe, tiered (short 20, long 5, forced 12.5 bp) | 0.69 | 0.887 (gross 1.179, t 1.54) | **pass** |
| #2 P1 weekly difference, 156 weeks | t 1 | 0.303%/wk, t 1.77 | **pass** |

| Run | Counts | Gross | Net | Turnover/yr | Funding share | Liq. |
| --- | --- | --- | --- | --- | --- | --- |
| 20261025-151935-train-base | yes (try 5) | 1.179 | 0.887 | 44.0 | 0.64 | 22 |
| 20261025-151941-train-p1-sunday48, -p1-wed48 | no | sparse price-only series | | | | |
| 20261025-151943-train-stress-both20 | no | 1.179 | 0.738 | 44.0 | 0.64 | 22 |
| 20261025-151945-train-stress-short40 | no | 1.179 | 0.659 | 44.0 | 0.64 | 22 |

**P1 reads (read only)**: Sunday book 53.9 pts, Wednesday placebo 6.6 pts over 156 weeks. Without the 5 largest |diff| weeks (2021-01-24 -9.1, 2021-02-07, 2021-09-05, 2022-05-29, 2022-08-28): t 1.52. Without FTTUSDT and LUNAUSDT: t 1.45. FTT: Sunday 2022-11-13 +0.02 pts, Wednesday 2022-11-09 +1.26. LUNA: Sunday 2022-05-08 -4.33, Wednesday 2022-05-11 -2.67 (both a long leg, liquidation first). Legs, mean %/wk: Sunday long 0.118, short 0.227; Wednesday long 0.151, short -0.109; the difference sits in the short leg (+0.336, long -0.033). The short40 stress is below 0.69 (0.659), both20 above (0.738): read only.

**Choices**: tiers swapped in the file (sign < 0 pays short bp); delisting exit and liquidation fee 12.5 bp (lab `liquidation_cost_bp`); P1 books from zero, no band, gross leverage, 0.5% maintenance, liquidation on mark high and low with the trigger loss but no fee; dying names closed at the last mark close; 2 hole bars skipped (no market-wide hole day needed the last-price fallback). Funding gaps leave both books (shared `eligible`). Not run: validation criteria #3 and #4, validation period, delay control.
**Turnover**: 44.0/yr measured against 46.6/yr in 1.7 (v4).
**Note**: `lab/data.py` has uncommitted edits in git; all runs share one lab sha. Four earlier tries backfilled in Trials.csv from the Build.md table (runs 095235 base, 095246/248/250 V1 to V3, each unambiguous); the 3 hourly-fill rows untouched.

## 2026-10-25 · Pass 1 v5.3: residual P1, then validation

**Code**: `strategies/crypto_funding_carry_v53.py` (calls `crypto_funding_carry_v5.py` and the v4 weights, sha 8ada54c6f9b2). Nothing from 2025 on read. OLS with HC1 (1.5b says "HC"; my pick), Newey-West 5 lags for stitched t. Factors: BTCUSDT, equal-weight universe row without BTC minus BTC, over the same window; Pass 2 weekly factors from `analysis/factors_4.csv`.

**Step 1, train, saved books (no new base run). Residual P1 = t 1.86 >= 1: pass, no kill.**

| Read | Dummy %/wk | t |
| --- | --- | --- |
| 48 h residual (raw 0.303, t 1.77); slopes near zero (Sunday BTC 0.01, alt 0.03) | 0.332 | 1.86 |
| 24 h / 72 h (read only) | 0.230 / 0.284 | 1.86 / 1.28 |
| P4 short leg / long leg (residual) | 0.228 / 0.105 | 1.54 / 0.77 |
| Without 5 largest weeks / without FTT, LUNA | 0.248 / 0.273 | 1.47 / 1.57 |
| 2021 / 2022 / 2023 | 0.622 / 0.505 / -0.064 | 2.08 / 1.57 / -0.22 |
| P2 train, weekly price, 4 factors (funding apart 0.299%/wk) | 0.080 | 0.35 |

156 pairs, 0 dropped for a missing Wednesday row. The effect is absent in 2023.

**Step 2, train plus validation, 208 weeks (Sundays 2021-01-03 to 2024-12-22; the 2024-12-29 window leaves 2024).**

| Criterion | Bar | Measured | Result |
| --- | --- | --- | --- |
| #3 04:00 UTC fill, mark_hourly, TLMUSDT out, Monday-Tuesday price, residual, all names | | 0.307%/wk, t 2.66 | read |
| #3 without the 5 best names (SOLUSDT 11.4 pts, WLDUSDT 10.5, WAVESUSDT 8.0, 1000PEPEUSDT 7.7, MATICUSDT 6.8) | t >= 1 | 0.100%/wk, **t 0.98** | **fail** (raw t 0.97) |
| #4 P2 intercept, weekly price only, 4 factors (funding apart 0.257%/wk) | t >= 1 | 0.222%/wk, t 1.15 | **pass** |
| Stitched net, weekly, NW 5 lags | read | mean 0.417%/wk, t 1.69 (train 1.14, 2024 1.95) | |

Base on train plus validation (tiers 20/5/12.5): gross 1.383, net 1.077, turnover 44.9/yr, funding share 0.48, 27 liquidations; tier check 0.0. Short 40 bp stress: net 0.838, NW t 1.32.

| Run | Counts |
| --- | --- |
| 20261025-153405-train-p1-residual-48h | yes, try 6 (48 h horizon, 1.6) |
| 20261025-153304-train+validation-base, -153306 stress-short40 | no |
| 20261025-153353-train+validation-crit3-04h-all, -ex5 | no |

Tries in Trials.csv for this sheet: 6 counted (base, V1 to V3, v5 base, 48 h). **Superseded runs, not logged**: 20261025-153054/153055/153102, 153132/153134/153141 (identical base and stress; crit3 had NaN factors on the 2021-07-24 to 27 market-wide hole, fixed by a last-close entry fallback within 5 days, 17 name entries in the week of 2021-07-25, logged). I could not delete the folders.
**Not run**: test; any rescue of #3 (another SE, other names) is not done. #3 misses the bar by 0.02 and is a kill criterion at validation: the Analyst and Economist decide.

## Test entry point (2026-10-25)

**User decision**: the Analyst killed the sheet on Pass 1's own bar (criterion #3, t 0.98 vs 1). Lucas decided on 2026-10-25 to send it to the test anyway. The verdict and Pass 2 are unchanged.

`strategies/crypto_funding_carry_v5.py` (code sha 9368e6398542) gets `run(period, variant="base", open_test=False)`, the entry point of `lab/run_test.py`; the old `run(tiers)` is now `run_tiers(tiers, period, open_test)` (only caller: its own main). Command (human only): `poetry run python lab/run_test.py strategies/crypto_funding_carry_v5.py --variant base`.

| Check | Result |
| --- | --- |
| run("train","base") vs 20261025-151935-train-base | daily series max abs diff 0.0, traded 131.85 both, net Sharpe 0.887 |
| run("validation","base") | 20261025-154721-validation-base, net 1.83, gross 2.195, turnover 48.5 |
| run("test","base") without open_test | refused (SystemExit) before any load; load() cuts before 2025-01-01 without open_test |
| Test run | not run, by design |

Frozen config in all periods: tiers short 20 bp, long 5 bp, delisting 12.5 bp, lab liquidation fee, Sunday to Sunday, v4 weights sha 8ada54c6f9b2, band 0.10 to the edge. Differences at test: none in the rules; the test starts 2025-01-01 (first Sunday weight) with no end cut (data end), history before it feeds the universe as in validation. New runs 154720-train-base and 154721-validation-base are in Trials.csv, counts no.
