---
type: reading-note
source: paper
title: Dynamic Asset Allocation with Asset-Specific Regime Forecasts
authors: Shu, Yu, Mulvey
affiliations: Department of Operations Research and Financial Engineering, Princeton University
year: 2024
venue: arXiv:2406.09578v2 (q-fin.PM), working paper
doi: Not stated in the paper
pdf: "[[2024 - Shu Yu Mulvey - Dynamic Asset Allocation with Asset-Specific Regime Forecasts.pdf]]"
version: arXiv v2, 19 August 2024 on the title page
tier: 1
read: full
tags: [trend, multi-asset, daily]
date: 2026-10-25
---

# Dynamic asset allocation with asset-specific regime forecasts (Shu, Yu, Mulvey 2024)

## Summary

- **Finding**: bull or bear regime forecasts made asset by asset lift 12-asset portfolios, 2007-2023, net of 5 bp one-way. MinVar Sharpe 0.70 to 1.12, MV 0.37 to 1.02, EW 0.51 to 0.91 (Table 6, p. 24).
- **Mechanism**: regimes are a smoothed version of returns, so they are easier to forecast than returns. Asset-specific regimes fit assets with different drivers better than macro regimes (p. 2-3, 8).
- **Where it works best**: HighYield 0/1 Sharpe 1.88 against 0.67 buy and hold; EM 0.85 against 0.20. Max drawdown cut for all assets (Table 4, p. 22).
- **Weak spots**: Gold 0/1 Sharpe 0.31 below buy and hold 0.43. Commodity 0.23 and Treasury 0.38 stay low. The authors say the Sharpe gain is hard because the strategy holds cash part of the time (Table 4, p. 23).
- **Main caveats**: walk-forward test only, no untouched hold-out. Many design choices are not explained. No significance test. Index returns, not ETF returns (p. 4, 29).

Page numbers follow the PDF, which is the arXiv layout and has no other pagination. Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Regimes have a better signal-to-noise ratio than direct return forecasts, because persistence makes them a heavily smoothed version of returns | Argued. Not tested on its own. | p. 8 |
| 2 | Asset-specific regimes fit better than a few macro regimes shared by all assets | Wealth curves show persistent bull or bear stretches for nearly all assets. REIT turned bearish before LargeCap in 2008. AggBond held the opposite regime in 2008 and 2020. | p. 6, 15, Fig. 1-2 |
| 3 | Splitting identification (jump model) and forecasting (XGBoost) allows different feature sets and gives better forecasts | JM-XGB beats JM alone on Sharpe for 11 of 12 assets (Table 4). Authors call the comparison "might not be fair enough" (no tuning, no macro-features in JM). | p. 7, 23 |
| 4 | Return forecasts matter more for the optimiser than covariance forecasts, so regimes enter through the return input | Cites Chopra and Ziemba (1993). | p. 19 |

**Caveats raised by the authors**
- Forecasts are late at turning points, for example the 2015-2016 LargeCap sell-off (p. 15).
- Wrong regime forecasts can be worse than none, citing Hess (2006) (p. 8).
- The 0/1 strategy cannot raise Sharpe for an asset it leaves out of the market more than 60% of the time, as for Gold (p. 23).
- The comparison across portfolio models is not a ranking; MinVar 1.12 against MV 1.02 proves nothing about which model is better (p. 24).

**Ruled out**: Not stated by the authors.

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | 12 risky assets: US large, mid, small cap; EAFE; EM; AggBond; long Treasury; HighYield; Corporate; REIT; Commodity; Gold. Plus the 3-month Treasury yield as risk-free rate. | p. 4, Table 1 |
| Period | Data 1991-2023. First training window 1991-2002, first validation 2002-2007, test 2007-2023. | p. 13-14 |
| Identification | 2-state statistical jump model per asset, 8 features from the asset excess return. Bull is the state with the higher cumulative excess return. | p. 9-10, Table 2 |
| Forecast | XGBoost, default parameters, trained to predict the next-day jump-model label from 8 return features and 5 macro-features. Probability above 0.5 means bull. Probability smoothed by EWMA, half-life 0, 2, 4 or 8 days by asset. | p. 11-12, Table 3, fn 14 |
| Refit | Every 6 months, 11-year lookback, for the jump model and the classifier. | p. 13 |
| Tuning | Jump penalty chosen every 6 months from 0 to 100 (log grid), by the Sharpe ratio of the 0/1 strategy over the previous 5 years. | p. 13-14 |
| Portfolios | MinVar, MV and EW, each with and without regime forecasts. | p. 17-20 |
| Rebalancing | Daily. Weights decided at the end of each day for the next period. | p. 17, 20 |
| Costs | One-way 5 bp, applied throughout. Optimiser adds a trading cost term. | p. 6, 17 |
| Benchmark | 60/40 fix-mix, rebalanced daily (Table 5). | p. 23 |

**Rule**

Jump model (Eq. 1, p. 9): minimise over parameters and states the sum of the loss between features and state centre, plus lambda times the number of state changes. The loss is half the squared distance.

0/1 strategy: 100% in the asset when the forecast regime is bull, else 100% in the risk-free asset (p. 13).

Optimiser (Eq. 2-4, p. 17): maximise w'mu minus gamma_risk w'Sigma w minus gamma_trade times a times the L1 distance to previous weights. Long-only, weight cap 40%, leverage at most 1, the rest in cash.

- MinVar: mu = 10 bp for bull assets, 0 for bear (p. 18-19).
- MV: mu = average past return of the periods in the forecast regime, as labelled by the jump model; bear forecasts capped at minus 10 bp (p. 19).
- EW: equal weight on the bull assets (p. 20).
- All three: 100% cash if three or fewer assets are bull (p. 19-20).
- Sigma: EWM covariance, half-life 252 days. gamma_risk 10 (5 for plain MV); gamma_trade 1 (0 for plain MV; plain MinVar has no cost term) (p. 19).

Features: EWM downside deviation (log), half-lives 5 and 21; EWM average return and EWM Sortino, half-lives 5, 10, 21 (Table 2). Macro: 2-year yield change, curve slope level and change, VIX log-change, 1-year stock-bond correlation (Table 3).

**Data provenance**
- Daily total return indexes in USD from Bloomberg, each tied to an ETF in Table 10. The ETFs themselves are not used (p. 4, 29).
- Commodity is an excess return index; Gold is the LBMA PM price (p. 29).
- Backfills: Treasury before 1994-03-02, HighYield before 1999-01-04 (a mutual fund), REIT before 1992-01-03 (p. 29, fn 17-19).
- Macro series from FRED; stock-bond correlation from LargeCap and AggBond (p. 12).

## 3. Results

All results are real data, walk-forward 2007-2023, net of 5 bp one-way unless the authors say otherwise.

**Aggregate** (Table 6, p. 24; annual excess figures, risk-free 1.1%)

| Portfolio | Sharpe | MDD |
| --- | --- | --- |
| 60/40 | 0.57 | -31.5% |
| MinVar to MinVar JM-XGB | 0.70 to 1.12 | -19.3% to -7.1% |
| MV to MV JM-XGB | 0.37 to 1.02 | -25.6% to -13.5% |
| EW to EW JM-XGB | 0.51 to 0.91 | -37.5% to -17.6% |

- MinVar JM-XGB return 3.9%, volatility 3.5%, leverage 0.91. MV JM-XGB return 8.9%, volatility 8.7%.
- Turnover rises: MinVar 0.49 to 2.06, MV 3.40 to 9.12, EW 0.81 to 11.70. The unit is not defined.

**By sub-group** (0/1 strategy per asset, Table 4, p. 22)
- Sharpe, JM-XGB against buy and hold: LargeCap 0.79/0.50, EM 0.85/0.20, EAFE 0.56/0.20, HighYield 1.88/0.67, AggBond 0.67/0.46.
- Below buy and hold: Gold 0.31/0.43. Corporate 0.76 is above buy and hold 0.54 but below JM 0.83.
- JM alone is below buy and hold on SmallCap (0.28/0.36), AggBond, Treasury and Gold.
- Max drawdown falls for every asset; LargeCap -55.25% to -17.69%, Commodity -75.54% to -47.90%.
- Forecast-return correlation (Table 7, p. 25): overall 2.43% for JM-XGB against -1.04% for the 5-year EWMA. Range 0.32% (Gold) to 10.54% (HighYield).
- Bear share of days: LargeCap 20.9%, REIT 18.4%, AggBond 41.5% (Fig. 2). Regime shifts: 46, 46, 97.

**Horizon and parameters**
- Without the trade cost term (gamma_trade 0), MinVar JM-XGB Sharpe falls from 1.12 to 1.02, MDD -7.1% to -12.8%, turnover 2.06 to 11.80 (Table 8, p. 27).
- gamma_risk 5, 10, 20 for MV JM-XGB: Sharpe 1.01, 1.02, 0.96; return 10.1%, 8.9%, 6.7% (Table 9, p. 27-28).
- No sensitivity on features, number of states, windows, the 10 bp input, the cap or the four-asset rule.

**Over time**
- Authors show protection in 2008, March 2020 and 2022 (Fig. 3, p. 25-26).
- In March 2020 MinVar JM-XGB held 35% average leverage; in 2022, 43%, against full leverage for plain MinVar (p. 25).
- In 2022 plain MinVar held AggBond 40%, HighYield 39%, Corporate 13%, which lost 15%, 13% and 17% that year; JM-XGB kept the portfolio flat (p. 25).
- Year-by-year results are not tabulated.

**Link to other strategies**: only the 60/40 benchmark. Reference to a risk-parity portfolio is made in text without numbers (p. 25).

**Inconsistencies in the source**
- Data start: "our data begins in 2002" (p. 14) against data from 1991 (p. 4, 13).
- Section 3.4 says the grid runs from 0.0 to 100.0 "evenly on a logarithmic scale" (p. 13); zero has no log.
- JM "generally maintains or enhances" Sharpe against buy and hold (p. 23), but Table 4 shows four assets below.
- Weight cap named w_ub in Eq. 3 and "wlb = 40%" in text (p. 17).

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Halflife choices cluster by similar fundamentals ("robust") | fn 14, p. 12 |
| XGBoost needs minimal tuning, "based on our experience" | p. 11 |
| Optimal lambda is good on cumulative return, Sortino and information ratio too | p. 14 |
| Daily rebalancing frequency does not matter for the EW benchmark | p. 20 |
| Risk features dropped for AggBond, Treasury, Gold after "preliminary in-sample analysis" | fn 13, p. 10 |
| Longer prediction horizons make forecasting "substantially" harder | p. 11 |
| Adding a regime filter on covariance left to future work | p. 19 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | Statistical jump model: 2-state temporal clustering of return features with a penalty per state change [[Regime probability filter]] | technique | signal | Persistent, stable labels, fewer false alarms than HMM | p. 8-10 |
| 2 | Cluster then classify: boosted-tree forecast of the next-day jump-model label from return and macro features [[Regime probability filter]] | technique | signal | Different feature sets for each step | p. 7, 11-12 |
| 3 | Jump penalty chosen by rolling validation Sharpe of the 0/1 strategy (no card: tuned parameter) | technique | calibration | Financial metric over accuracy; separate validation period | p. 13-14 |
| 4 | 0/1 strategy: asset when forecast bull, else risk-free [[Regime probability filter]] | technique | entry | Tests the money value of the forecasts | p. 13 |
| 5 | Regime forecast as the return input of a mean-variance optimiser, fixed 10 bp for bull and 0 for bear (MinVar), or past regime mean (MV) [[Mean-variance weighting]] | technique | sizing | Return input matters more than covariance | p. 18-19 |
| 6 | Cash when three or fewer assets are bull (no card: parameter of the sizing rule, in [[Mean-variance weighting]]) | technique | risk | Avoid concentration | p. 19 |
| 7 | L1 trading cost term in the optimiser objective [[Trading cost penalty in the optimizer]] | technique | rebalancing | Limits trading and noise sensitivity | p. 17-18 |
| 8 | Forecast-return correlation by asset (no card: standard practice) | diagnostic | evaluation | Statistical quality of forecasts | p. 25 |

## 6. Regime observations

- Bear share differs by asset: 21% LargeCap, 18% REIT, 42% AggBond. The authors tie the AggBond figure to features built on excess return, when the risk-free rate is high (p. 15).
- 2022: stocks and bonds fell together, unlike earlier crises (p. 6).
- Forecasts lagged the 2015-2016 sell-off (p. 15).

## 7. Acknowledged limits

- Forecasts are imperfect and late (p. 15).
- The JM versus JM-XGB comparison is not like for like (p. 23).
- Trading costs treated with a single-period term; multi-period models would be better (p. 18, 28).
- Feature selection could be tuned per asset and over time (p. 28).

## 8. Not addressed

- Hold-out: no period kept away from design choices. Sensitivity runs use the test period (Table 8-9).
- Statistical significance of Sharpe differences, luck adjustment, number of configurations tried.
- How features, 11-year window, 6-month refit, 10 bp, cap 40%, four-asset rule and gamma values were picked.
- Cost beyond the flat 5 bp: slippage, ETF spreads, the cash leg, cost of switching to the risk-free asset.
- Turnover definition, execution price, capacity, tax.
- Results by sub-period; contribution of each asset to the portfolio gain.
- Comparison with a simple rule (trend filter, volatility scaling) at the same exposure.
- Whether returns come from ETFs: the study uses indexes and some backfills.
