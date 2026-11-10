## Build

## Phase validation (validation 2024, code `c7814558d546`, lab `fd8ce652344b`)

The code gained the validation options (V1, V2, six stress options, diagnostics) after the v2 gate; the base logic is unchanged. The gate was rerun on this code first: identical (gross 1.75, net 1.377, #1 NW t 3.04, #3 NW t 2.50, #4 1.03). Truncation test PASS on 12 trade days for base, V1, V2 and each of the six stress options. All runs use the 1.5b cost tier (thin 20 bp, liquid and BTC 5 bp, forced trades 12.5 bp) except thin40. Stress tests ran on validation, as 1.10 says.

| Run | Period | Variant | Gross Sharpe | Net Sharpe | Turnover/yr | Funding share | Liquidations |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20261023-164211-validation-base | validation | base | 0.87 | 0.33 | 98.1 | -0.04 | 23 |
| 20261023-164216-validation-v1 | validation | V1 median volume | 0.81 | 0.26 | 96.3 | -0.04 | 13 |
| 20261023-164220-validation-v2 | validation | V2 7 days | 1.09 | 0.37 | 128.8 | -0.05 | 13 |
| 20261023-164225-validation-base-delay1 | validation | control, one day late (= d+1 fill stress) | 0.84 | 0.32 | 96.5 | -0.03 | 22 |
| 20261023-164230-validation-base-sort_ind | validation | stress independent sort | 0.44 | -0.06 | 93.5 | -0.02 | 18 |
| 20261023-164234-validation-base-beta30 | validation | stress beta window 30 | 0.58 | -0.02 | 122.5 | -0.09 | 31 |
| 20261023-164239-validation-base-beta120 | validation | stress beta window 120 | 1.17 | 0.64 | 93.4 | -0.03 | 16 |
| 20261023-164243-validation-base-lags10 | validation | stress beta lags 10 | 0.92 | 0.38 | 98.7 | -0.05 | 23 |
| 20261023-164248-validation-base-hedge_ew20 | validation | stress hedge on equal-weight top 20 | 0.43 | -0.11 | 94.1 | -0.02 | 23 |
| 20261023-164252-validation-base-thin40 | validation | stress thin leg 40 bp | 0.87 | -0.07 | 98.1 | -0.04 | 23 |
| 20261023-164257-validation-base-minleg5 | validation | stress under 5 a leg skipped | 0.87 | 0.33 | 98.1 | -0.04 | 23 |

The gate rerun runs are 20261023-164156-train-base-tiered, 164200 (winners) and 164203 (depth). Earlier gate runs (a809d54981c7, aa8ebf462b93) stand as history.

**Interpretations the Developer made (stress options Pass 1 names without a recipe)**: hedge on the equal-weight top 20 = the 20 largest names by 14-day average quote volume at day d (crypto_universe ranking, age 180), beta of the book on that basket's returns today plus lags with today's composition, short split equally, 5 bp; "under 5 a leg" = a formation is skipped if the thin or the liquid leg has fewer than 5 names; independent sort = losers (bottom 30% on return among all ranked names) intersected with the top or bottom 30% of Amihud among all ranked names; the d+1 fill stress is the `--delay 1` control (same run, logged once as control). Moving any of these changes only that stress test, not the base. Not a result-changing gap for the base, flagged for the Economist if the stress reading matters.

**Read-only diagnostics** (`--diag`, base runs)
- P4 price share of gross: validation 1.037 all names, 1.032 excluding ICP, TLM, BNX; train 1.027 and 1.026. Same pass either way; all names is the figure used.
- Held name-days without a funding print, by year (long / short of held name-days): 2021 1 / 42 of 8,519 / 8,049; 2022 29 / 204 of 13,383 / 11,280; 2023 6 / 19 of 14,837 / 14,391; 2024 20 / 4 of 21,668 / 20,444. Train: ICP 147, TLM 74, BNX 68 name-days held.
- Liquidity-cell changes inside a holding (13 days after formation, same sequential sort): a formed name is in its original cell on 42% of the following days on train and 43% in 2024, in the opposite cell on 0.1% and 0%; 92% of names leave their cell at least once (mostly to the middle or out of the losers), 0.4% (train) and 0.2% (2024) sit in the opposite cell at least once. The positions themselves are fixed for the 14 days: tranches do not re-sort.
- Largest single-name day: train long leg +24.9% of capital-weight P&L terms (DOGE 2021-01-28 at +0.2487), worst -0.022 (ATA 2023-06-10); short leg worst -0.037 (XLM 2021-01-06), best +0.024. 2024: long best +0.023 (PEOPLE), worst -0.012 (BTC hedge); short worst -0.025 (BCH). Largest single-name weight in the book (hedge included): 0.40 (train, 2023-05-27) and 0.27 (2024-02-29) on the long side, 0.39 and 0.30 short; median daily maximum about 0.05 to 0.07.
- Measured turnover on validation 98.1/yr, above train 79.6 and the 54.8 of the first 1.7.

**Not run**: the test period (sealed); the P5 event-time and V1-vs-base reading, regimes and luck line belong to the Analyst.

## Gate rerun on Pass 1 v2 (#1 with the depth control, #2 with the cost tier)

Truncation test PASS on 12 trade days, base and depth. Train, base. Gross is identical to v1 (Sharpe 1.75, price +139.81%), so the min-cell rule written in v2 (skip under 4 losers ranked; smallest loser group on train is 10, 0 formations skipped) does not bind.
- **#1** intercept of the base's gross daily return (price plus funding) on the equal-weight market today plus 5 lags and on the depth-of-fall spread today: +0.00113/day, Newey-West t (14 lags) **3.04** (OLS 2.78), bar 2 → **pass**. Depth beta 0.011. The depth spread (lowest minus highest 30% of losers, built like the base: tranches, hedge, vol target) earns about nothing alone (intercept t -0.08, gross Sharpe -0.05), so depth of fall does not carry the base.
- **#2** net Sharpe **1.377** with the tier (v1 blended 12.5 bp: 1.362), bar 0.49 → **pass**. Costs -28.82% over 3 years (v1: -29.86%). Turnover 79.6/yr, average gross 1.45.
- **#3** (NW t 2.50) and **#4** (price share 1.03) stand as in v1, unchanged by the rerun (identical weights and gross).

**Cost tier as coded**: the engine runs at zero cost, then cost = per-name traded notional x tier. A name's trade is |target - held after the day's return|, rebuilt from the saved positions (sum checked against the engine's traded notional: max difference 3e-16). Tier by the sign of the target (of the held position when closed): net-long name 20 bp (thin leg), net-short name 5 bp (liquid leg), BTC 5 bp. Netting: a name long in one tranche and short in another nets before the tier. Forced trades (liquidation fee) keep 12.5 bp; delisting exits take the tier of the held side. Pass 1 gives no tier for forced trades: 23 liquidations cost -0.42% over 3 years, 13 delisting exits, so not material. Saved summaries show the tiered cost; their engine notes show cost_bp 0 and the tier.

| Run | Period | Variant | Gross Sharpe | Net Sharpe | Turnover/yr | Funding share | Liquidations |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20261023-163421-train-base-tiered | train | base, tier | 1.75 | 1.38 | 79.6 | -0.03 | 23 |
| 20261023-163425-train-winners-diagnostic-tiered | train | winners spread | 0.22 | n/a (diagnostic) | 69.3 | | |
| 20261023-163428-train-depth-diagnostic-tiered | train | depth spread | -0.05 | n/a (diagnostic) | 105.5 | | |

The v1 runs below stand as history; the v2 runs above replace them for gates #1 and #2.

### v1 gate (history)

**Code**: `strategies/crypto_thin_losers.py` · sha `aa8ebf462b93` (v2 gate; v1 gate was `a809d54981c7`) · lab_sha `fd8ce652344b` · built 2026-10-23, gate rerun on Pass 1 v2

**Gate v1 (1.11 #1 to #4, train, base, 12.5 bp blended)**: all four pass. Truncation test on 12 trade days: PASS.
- #1 intercept of gross daily return on the equal-weight universe return today plus 5 lags (Dimson, 6 regressors, 1090 days): +0.00113/day, t 2.79 OLS, 3.06 Newey-West (14 lags). Bar 2 → **pass** (both).
- #2 net Sharpe 1.362, bar 0.49 (luck line) → **pass**. Measured turnover 79.6/yr, cost 12.5 bp blended, vol 25.9% realised.
- #3 losers minus winners intercept +0.00104/day (t 2.31 OLS, 2.50 NW), winners intercept +0.00009 (t 0.24) → **pass**.
- #4 price share of gross 1.03 (all names), 1.03 excluding ICP, TLM, BNX; funding share -0.03 → **pass**. The all-names figure is the one used.

| Choice | Pass 1 | Code | Data check |
| --- | --- | --- | --- |
| Universe | 1.4 | `crypto_universe(top=1000, volume_window=14, min_age_days=180, min_names=1)`, USDCUSDT dropped (close asserted inside 0.97 to 1.03) | #1 |
| Prices | 1.8 | mark OHLC everywhere (signals, P&L, liquidation) | #2 |
| Return signal | 1.5 | mark close(d) / mark close(d-14 calendar days) - 1, by dates, NaN across a gap | harmless warning BNX |
| Amihud | 1.5 | mean of abs 1-day mark return / quote volume over 14 calendar days, all 14 days required | #5 plain mean, harmless warning BNX |
| Sort | 1.5 | universe names of row d with both signals; losers = return <= 30th pct; thin = Amihud >= 70th pct of losers, liquid = <= 30th pct; no minimum cell size; no formation if a leg is empty or fewer than 4 ranked names | none |
| Book | 1.5 | long thin 1/n each, short liquid 1/n each (each leg sums to 1) | none |
| Holding | 1.5 | formation every day, book = mean of the last 14 formations, fixed weights per tranche | none |
| Hedge | 1.5, 1.5b | BTCUSDT weight = minus the sum of 6 coefficients (today + 5 lags) of the book's past 60 daily returns on BTC returns, with intercept; book returns use current weights on past returns | none |
| Sizing | 1.5 | scale so the std of the hedged book's past 60 days (current weights) is 20% a year; gross capped at 3 | none |
| Cost | 1.7 | 12.5 bp one way on every trade (the blended central case of 1.7), not tiered per name | see spec note |
| Margin | 1.5 | isolated, leverage = gross of each rebalance (engine "gross"), reset daily at each rebalance | none |
| Funding | 1.8 | engine print level, paid to the holder at the print time; no print = no funding | #3, #4 |
| Band | 1.5 | none | none |

**Data check instructions applied**: #1 USDCUSDT dropped with a peg assert; #2 mark prices, price fallback days 0; #3 no funding charged without a print, P4 reported with and without ICP, TLM, BNX (same pass), name-days without a print by year and leg not reported yet; #4 engine handles prints at 00:00 for the old holder, universe row of d for a fill at the close of d; #5 plain mean, cell switches inside a holding not yet reported; harmless warnings: gaps by dates, cell counts by year reported.

**Spec notes (not gaps that change the gate verdict, for the Analyst to read)**: (1) the engine has one cost_bp, so the tiered 5/20 bp cost is the 12.5 bp blend of 1.7; the hedge leg is charged 12.5 bp instead of about 5. Break-even cost is 57 bp, so the verdict does not depend on it. (2) Pass 1 does not say how the P1 t-stat treats overlap; both OLS and Newey-West are given, they agree. (3) Pass 1 does not say how the winners spread is sized for #3; the same code with the winners group, same vol target and hedge, sign only. (4) Thin cell on train: median 7 (2021), 12 (2022), 13 (2023), mean 12.0 over all days; loser group mean 35.8 on train, which is the loser cell of the precondition before the Amihud split.

| Run | Period | Variant | Gross Sharpe | Net Sharpe | Turnover/yr | Funding share | Liquidations |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20261023-162549-train-base | train | base | 1.75 | 1.36 | 79.6 | -0.03 | 23 |
| 20261023-162553-train-winners-diagnostic | train | winners spread | 0.22 | -0.15 | 69.3 | -0.32 | n/a |

**Measured turnover**: 79.6/yr against 54.8/yr in 1.7 (average gross 1.45 against 1.4 estimated).

**Not run**: V1, V2, stress tests, the one-day delay control, validation (phase gate only). V1 and V2 are coded and not truncation-tested; the independent sort, beta window 30/120, 10 lags, equal-weight hedge and d+1 fill stress options are not coded. Largest single-name day, cell switches and funding name-days without a print are not yet reported. A Pandas4Warning on a fillna in the file is harmless.
