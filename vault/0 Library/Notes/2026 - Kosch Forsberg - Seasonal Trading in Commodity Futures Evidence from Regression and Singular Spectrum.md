---
type: reading-note
source: paper
title: Seasonal Trading in Commodity Futures, Evidence from Regression and Singular Spectrum Signals
authors: Kosch, Forsberg
affiliations: Kosch (University of Zurich), Forsberg (University of Zurich and University of Helsinki)
year: 2026
venue: arXiv:2609.12227v1 [q-fin.PM], 10 Sep 2026
doi:
pdf: "[[2026 - Kosch Forsberg - Seasonal Trading in Commodity Futures Evidence from Regression and Singular Spectrum.pdf]]"
version: preprint (v1)
tier: 1
read: full
tags: [seasonality-flows, commodities, monthly]
date: 2026-10-24
---

# Seasonal trading in commodities (Kosch, Forsberg 2026)

## Summary

- **Finding**: three seasonal signals (calendar regression, SSA, robust SSA) on 15 commodity futures, 2016-2024, net of 8.6 bps per trade, do not robustly beat an equal-weight long benchmark. None of 18 Holm-adjusted Sharpe tests rejects (p. 14).
- **Mechanism**: seasonality is plausibly rooted in harvests, weather, storage and demand (p. 2). The paper does not test it, and says the patterns can shift across regimes.
- **Where it works best**: historical DVR long: cumulative return 29.66%, Sharpe 0.245 against 14.30% and 0.183 for the benchmark (Table 2). Classical SSA is best on bootstrap averages (Sharpe 0.131).
- **Weak spots**: SSA medians are negative (-11.30%), drawdowns deep, DVR shorts lose money. Gains sit in single subperiods (Tables 9-10).
- **Main caveats**: one contract held per month, no financing, bootstrap keeps the timing of returns, so it is not a test against no seasonality (p. 11).

Page numbers follow the PDF, which matches the printed pagination. Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Commodity returns may show calendar structure through harvest cycles, planting, storage, weather, extraction, transport and seasonal demand | Stated as plausible; literature cited. Not tested. | p. 2 |
| 2 | Seasonal effects can shift across regimes and weaken after shocks | Literature: Li 2024 finds effects weaker in recent periods. Here: model rankings change across 2016-2018, 2019-2021, 2022-2024. | p. 2, 15-16 |
| 3 | SSA may gain over DVR when uncertainty changes seasonal amplitude or period | Offered as "one possible explanation" for the 2019-2021 shift. | p. 17 |
| 4 | Robust SSA can remove real information, since extreme moves in commodities are not always noise | Offered as an explanation for classical SSA beating RLSSA. | p. 18 |
| 5 | Amplitude can carry economic information, so volatility normalisation can hurt | Offered as an explanation of mixed normalisation results. | p. 18-19 |

**Caveats raised by the authors**
- Positive SSA means coexist with negative medians: a subset of paths drives the average (p. 13).
- Strong 2019-2021 SSA results may reflect a few extreme moves under Top-1 (p. 18).
- MEB keeps the temporal ranks, so it tests conditional path sensitivity, not a timing-destroying null (p. 11).
- Short-side comparisons against a long benchmark are not a pure test of short selection (p. 10, 14).
- Non-rejection means inconclusive, not equivalent (p. 12).

**Ruled out**
- Not stated by the authors.

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | 15 futures: cocoa, coffee, WTI crude, copper, cotton, gold, lean hogs, heating oil, live cattle, natural gas, sugar, silver, corn, soybeans, wheat. Fixed before 2016: monthly average daily volume at least 1,000 contracts in every month of 2006-2015. Palladium and platinum dropped. | p. 4 |
| Period | Panel from Jan 2001. Estimation from Jan 2006. Out of sample Jan 2016 to Dec 2024, 108 months. | p. 5, 12 |
| Signal | One-step-ahead seasonal score per contract from monthly log returns, rolling 120 months. Three estimators: DVR, SSA, RLSSA. Classical or volatility-normalised returns. | p. 6-9 |
| Entry | Long: the contract with the highest score. Short: the contract with the lowest score. Top 1 only. DVR also needs the sign of β and a Newey-West p-value of 0.10 or less; otherwise cash. | p. 9-10 |
| Exit | End of the month. | p. 10 |
| Horizon | One month. | p. 4, 10 |
| Sizing | Unit notional, one contract. | p. 10 |
| Portfolio | Long and short portfolios evaluated separately. | p. 9-10 |
| Rebalancing | Monthly. | p. 10 |
| Costs | One-way 0.00086 (8.6 bps), applied twice per month. Excludes collateral yield, margin, financing, market impact. Cash earns zero. | p. 10 |
| Data and tools | TradingCharts contract histories. Code and monthly panels in a public repository. | p. 4 |

**Rule** (p. 7, Eq. 1): within each 120-month window, r(i,t) = α(i,m) + β(i,m) · D(m,t) + ε, with D(m,t) = 1 in calendar month m. Long candidate: β > 0 and p ≤ 0.10. Short candidate: β < 0 and p ≤ 0.10. Rank by β.

**SSA** (p. 7): N = 120, embedding L = 36, first r = 12 components kept, diagonal averaging, recurrent one-step forecast.
**RLSSA** (p. 7-8): same N, L, r. The SVD is replaced by Hawkins' alternating L1 robust SVD.
**Volatility normalisation** (p. 8-9): EWMA variance with λ = 0.97 inside each window, return minus its expanding mean, divided by volatility.

**Data provenance**
- Delivery-avoidance return: the nearest contract that expires at least two calendar months after the observation month and has prices to at least 14 days after month-end. Monthly simple return from first-day open to last-day close (p. 4). Not a front-month series.

## 3. Results

Real data, out of sample 2016-2024, net of cost. Benchmark: equal-weight long of all available contracts, same cost.

**Aggregate** (Table 2, historical path)

| Strategy (classical) | Direction | CumRet | Sharpe | MaxDD |
| --- | --- | --- | --- | --- |
| DVR | Long | 29.66% | 0.245 | -0.308 |
| DVR | Short | -19.94% | 0.018 | -0.494 |
| SSA | Long | -32.41% | 0.014 | -0.605 |
| SSA | Short | -35.83% | 0.119 | -0.799 |
| RLSSA | Long | -57.64% | -0.088 | -0.721 |
| RLSSA | Short | -0.54% | 0.184 | -0.825 |
| Benchmark | Long | 14.30% | 0.183 | -0.415 |

Volatility normalisation lowers cumulative return in 5 of the 6 model and direction pairs. DVR short improves, from -19.94% to -9.72% (Table 2).

**Bootstrap, 500 MEB paths** (Tables 3 and 5, average / median cumulative return)
- Benchmark: 16.81% / 15.64%, Sharpe 0.191, MaxDD -0.414.
- SSA classical long: 12.96% / -11.30%, Sharpe 0.131, MaxDD -0.682. SSA classical short: 3.81% / -24.75%, Sharpe 0.161.
- DVR classical long 1.01%, short -36.63%. RLSSA classical long -49.00%.

**By sub-group**
- Long and short are shown separately above.
- Per contract: Not addressed, except Top-1 selection shares (Table 7: leading contract chosen 53% to 77% of months on average).

**Horizon and parameters**
- Only one setting is run: N = 120, L = 36, r = 12, 10% p-value filter. The authors list contract-specific rank and a signal threshold as untested extensions (p. 19).

**Over time** (Tables 9-10, mean over paths)
- Long, 2016-18 / 2019-21 / 2022-24: DVR classical +8.16% / -14.89% / +9.66%. SSA classical -55.48% / +109.59% / +19.06%. Benchmark -13.55% / +19.22% / +12.51%.
- Short: DVR classical -44.08% / +63.56% / -31.17%. SSA classical -4.81% / -23.85% / +42.98%.
- Median paths (≈ Fig. 2): wide 50% and 90% bands; SSA and RLSSA long medians drift below the start value.

**Link to other strategies**
- Equal-weight long benchmark only.

**Inconsistencies in the source**
- p. 13 says classical DVR long has a shallower drawdown than the benchmark. Table 2 also shows -0.366 for volatility-normalised DVR long, against -0.415. Both are shallower.
- p. 4 says the evaluation uses 15 contracts "from 2006 to 2024". Out-of-sample months begin in Jan 2016 (p. 5, 12). Loose wording.
- The liquidity screen is on 2006-2015 (p. 4). Appendix Table 8 reports volume over 2001-2024. Not a conflict, since the table is described as descriptive.

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Volatility normalisation improves cross-contract comparability | p. 8-9; only a doubling-of-returns example (Table 1) |
| Seasonality varies with market uncertainty (COVID-19, Russia-Ukraine) | p. 15, 17; no test, the authors say it does not prove the point |
| An ex-ante uncertainty-based switch between DVR and SSA would help | p. 17, 19; future work |
| Raising the volume cutoff from 500 to 1,000 contracts removed no ticker | p. 4; "in the underlying thesis" |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | Calendar-month dummy regression with Newey-West filter, rolling 120 months | technique | signal | Transparent test of calendar effects. Card [[Calendar seasonality signal]] | p. 7 |
| 2 | Singular spectrum and robust SSA seasonal forecast | technique | signal | Flexible, multi-frequency seasonality. Card [[Calendar seasonality signal]] | p. 7-8 |
| 3 | Standardise returns by EWMA volatility before ranking | technique | signal | Raw scores scale with volatility (Table 1). Card [[Volatility-normalised signal]] | p. 8-9 |
| 4 | Hold only the top-ranked and bottom-ranked contract | technique | sizing | Transparent baseline. Card [[Long-short portfolio weighting]] | p. 9-10 |
| 5 | Volume screen fixed before the out-of-sample period | technique | universe | Implementability. Card [[Minimum price and size filter]] | p. 4 |
| 6 | Equal-weight long benchmark for both directions | technique | evaluation | Hard to overfit. Card [[Always-long benchmark comparison]] | p. 10-11 |
| 7 | Maximum entropy bootstrap, paired Sharpe test, Holm correction | technique | evaluation | Path sensitivity for dependent data. Card [[Maximum entropy bootstrap Sharpe test]] | p. 11-12 |
| 8 | Delivery-avoidance contract choice | technique | universe | Avoids near expiries. No card: data construction | p. 4 |
| 9 | Subperiod split into three windows | technique | evaluation | Stability. No card: standard practice | p. 15 |

## 6. Regime observations

- Rankings of the models change with the subperiod (p. 15-16).
- The later subperiods include COVID-19 and the Russia-Ukraine war, which the authors call less stable environments (p. 15).
- Benchmark negative in 2016-2018, positive afterwards (Table 9).

## 7. Acknowledged limits

- Top-1 forces a position even when forecasts are small or have the wrong sign (p. 9-10).
- MEB is run contract by contract and does not keep cross-contract dependence (p. 11).
- The p-value filter is a trading screen, not a discovery test (p. 7).
- Rank r = 12 is fixed for all contracts (p. 7).

## 8. Not addressed

- Results by contract or sector.
- Sensitivity to the window length, L, r, the 10% filter or the cost level.
- A timing-randomised null for seasonality.
- Financing, margin, market impact, capacity.
- Whether the 14-day post-month-end price rule can be known at the trade date.
- Short-side benchmark that is short or cash.
