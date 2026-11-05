---
type: reading-note
source: paper
title: "The long-term efficiency of tactical asset allocation: Evidence from 86 systematic strategies (1995-2025)"
authors: Prior-Sanz, Vizuete-Luciano, Cruz-Zayash, Ferrer-Canteli
affiliations: IQS School of Management, Universitat Ramon Llull; Universitat de Barcelona
year: 2026
venue: International Review of Economics and Finance 111, 105748
doi: 10.1016/j.iref.2026.105748
pdf: "[[2026 - Prior-Sanz Vizuete-Luciano Cruz-Zayash et al - The long-term efficiency of tactical asset allocation Evidence from 86 systematic strategies (1995-2025).pdf]]"
version: published, open access
tier: 1
read: full
tags: [trend, multi-asset, monthly]
date: 2026-10-25
---

# Tactical allocation, 86 strategies (Prior-Sanz et al. 2026)

## Summary

- **Finding**: over 1995-April 2025, the 86 monthly allocation strategies have a higher mean Sharpe than the static group (0.61). Breadth-filtered dual momentum is best at 0.78 (p. 26).
- **Mechanism**: Not stated by the authors. Canary and breadth are called crash protection; a wider asset set is read as access to tail-hedging assets, not tested (p. 4, 9).
- **Where it works best**: Canary (+0.13) is the only positive significant feature over 30 years; optimised weighting is negative (Table 4). Group 3 (breadth) and Group 6 (absolute momentum only) cut drawdowns (p. 26).
- **Weak spots**: 10-year, 1-year, 2000-02 and tariff regressions are not jointly significant (Tables 5, 7, 8, 11). Dual momentum without filters is not significant against the static group (Table 13).
- **Main caveats**: 0.2% round trip only, no cost sensitivity run. Hold-out, bootstrap matrix and multiple-testing are "indicative" or left to a future revision (p. 24-25, 29). Per-strategy results are not tabulated.

Page numbers follow the journal pagination, which equals the PDF page. Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Static allocation assumes stable risk, return and correlations; tactical rules adapt | Literature only | p. 1-3 |
| 2 | Canary universe is the most reliable crash protection | Positive coefficient over 30, 10 and 5 years; negative in the 2000s window (Tables 4-6, 8) | p. 12, 30 |
| 3 | Breadth momentum helps in the long run and in 2008 | Boxplots; coefficient -0.04 (30y) and -0.36 (5y) in regressions (Tables 4, 6) | p. 12, 30 |
| 4 | More assets help because they proxy tail-hedging classes (gold, commodities, long volatility) | Pearson 0.33 over 30 years; loses significance once clustered | p. 9, 12-13 |
| 5 | Optimisation hurts through estimation error | Negative coefficient, 30y -0.06, 5y -0.14 (Tables 4, 6) | p. 15 |

**Caveats raised by the authors**: the strategy features overlap, so standard errors are clustered by group (10 clusters, p. 8); shorter windows are noise (p. 17, 31); the sample ends inside an atypical 2022 stock and bond sell-off (p. 31); public strategies carry publication bias (p. 29).

**Ruled out**: Not addressed.

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | 86 published monthly strategies, mostly US-listed ETFs; 6 static, 80 tactical | p. 2, 5, 30 |
| Period | Jan 1995 to Apr 2025; 1995-2014 replicated backtest, 2015 on "live tracked" | p. 6 |
| Signal | Coded 0/1: absolute, relative, dual, breadth momentum, canary, macro, optimised weighting | p. 7-8 |
| Execution | Month-end close, monthly | p. 6 |
| Costs | 0.1% per trade (0.2% round trip), dividends reinvested | p. 6 |
| Sizing | Equal weight versus "optimised" (volatility scaling, inverse volatility, covariance, risk parity, minimum correlation) | p. 8 |
| Metrics | Annual return, volatility, Sharpe against 3-month T-bill (FRED), MaxDD, return over MaxDD | p. 8 |

**Rule**: Not given. The paper lists no rule, lookback or threshold. It cites the published designs: 10-month moving average (Faber 2007), dual momentum (Antonacci), adaptive allocation, VAA and DAA (Keller and Keuning), DAAA (Kipnis) (p. 3). Breadth: share of assets with positive momentum, defensive when few remain (p. 3, 7). Canary: designated assets that trigger the defensive allocation (p. 7).

**Data provenance**: all return series come from Allocate Smartly, total-return ETFs or mutual funds (p. 6). Authors rebuilt 15 strategies from Bloomberg data, correlation above 0.99 with the vendor series; detail "on request" (p. 6, Annex 2). Benchmark SPY from investing.com (p. 6). Data "on request" (p. 34).

## 3. Results

Test type: real data, vendor-run rules, gross of costs beyond 0.2% round trip.

**Aggregate** (group means, p. 26-27)

| Group (N) | Return | Vol | Sharpe | MaxDD |
| --- | --- | --- | --- | --- |
| 1 Static (6) | 7.41% | 8.58% | 0.61 | -23.6% |
| 2 Dual momentum, no filter (14) | 9.81% | 10.48% | 0.72 | -16.7% |
| 3 Dual momentum + breadth (17) | ≈9.83% | 9.95% | 0.78 | -15.6% |
| 4 Dual momentum + optimised (6) | n/a | 9.01% | 0.75 | -12.7% |
| 5 Macro or canary (2) | n/a | n/a | 0.59 | -17.7% |
| 6 Absolute only (5) | 8.03% | 7.49% | 0.76 | -10.2% |
| 7 Relative only (5) | 10.83% | 11.72% | 0.74 | n/a |
| 8 Risk based, no momentum (8) | n/a | 8.87% | 0.61 | -20.6% |
| 9 Three assets or fewer (12) | 9.71% | 11.17% | 0.69 | n/a |
| 10 Mixed (11) | 10.63% | ≈11.99% | 0.75 | ≈-23.6% |

- Sharpe gaps against Group 1 (computed from the means): Group 3 +0.17, Group 4 +0.14, Group 2 +0.11, Group 8 0.00 (Table 13, p. 29).
- Table 13 p-values (indicative, not computed from monthly series): Group 3 0.006, Group 4 0.041, Group 2 0.123, Group 8 0.982, Group 3 against Group 8 0.022.
- Cross-sectional regression of Sharpe on the 0/1 features, 86 strategies (Tables 4-11, clustered errors):

| Window | Joint F p-value | Canary | Optimised | Breadth |
| --- | --- | --- | --- | --- |
| 30 years | 0.017 | +0.13*** | -0.06** | -0.04 |
| 10 years | 0.107 | +0.16** | -0.12*** | -0.07 |
| 5 years | 0.0016 | +0.34*** | -0.14*** | -0.36*** |
| 1 year | 0.719 | not significant | not significant | not significant |
| 2000-02 | 0.110 | -0.51* | +1.24*** | +1.26** |
| 2008-09 | 0.00024 | +0.16 | +0.05 | +0.41 |
| 2020-23 | 0.012 | +0.28*** | -0.17** | -0.23** |
| Tariffs 2025 | 0.759 | not significant | not significant | +5.04* |

Adjusted R2 is 0.132 over 30 years (Table 4). Dual, absolute and relative momentum are not significant over 30 years (Table 4).

**By sub-group**
- Named strategies, no figures given: best over 30 years Financial Mentor's Optimum3 and Kipnis' Defensive Adaptive Asset Allocation; worst Predicting US Treasury Returns (p. 30).
- Best over 10 years Hybrid Asset Allocation; over 1 year All Weather Quad Momentum and Tactical Permanent Portfolio (p. 30).
- Best by crisis: Classical Asset Allocation Defensive (2000-02), Flexible Asset Allocation (2008-09), Paul Choi's Dividend and Growth (COVID) (p. 30).
- Benchmark correlation: Pearson -0.19 (30y), but +0.21 (10y), +0.28 (5y) (p. 13, 17). In crises it is -0.20 (2000s), -0.52 (2008), -0.50 (tariffs), 0.00 (COVID) (p. 20-25).

**Horizon and parameters**: gains fade as the window shortens; at 5 years many strategies do not beat 60/40 and some have negative Sharpe (p. 15-18, 30). No lookback or threshold sensitivity is shown.

**Over time**: the 60/40 drawdown is deeper in 2000-02 and 2008 (p. 11). Some Group 10 strategies show long drawdowns, bonds in 2022-23 (p. 11). All strategies had negative Sharpe in the 2025 two-month window (p. 30).

**Link to other strategies**: Group 8 shows risk-based weighting without timing does not lift Sharpe above static (p. 27).

**Inconsistencies in the source**
- Table 13 is labelled "60/40", but its gaps equal group mean Sharpe minus the Group 1 mean of 0.61 (computed, p. 26, 29).
- Section 4.9 reports a live-window breadth coefficient ≈+0.11 (t ≈2.34, 2015-2025); Table 5 gives -0.07, not significant, for 10 years (p. 14, 24).
- Conclusions call breadth beneficial and number of assets influential; Table 4 shows breadth -0.04 and assets not significant (p. 12, 30).
- Conclusions call optimised weighting the least favourable feature, yet Optimum3 (Group 4) is named a top strategy and Group 4 has the shallowest drawdown (p. 26, 30).
- Text on the 2000s crisis names Canary a strongest defensive feature; Table 8 gives -0.51 (p. 20, 19).
- Section 4.1 puts Group 4 in the lower left quadrant; Section 4.2 says Group 4 stood out in the upper left over 30 years (p. 11, 13).
- 2015 is called ex ante live tracking for all strategies, but the cited designs date from 2017-2023 (p. 6, 34).
- Tables 4-11 notes cite a cost sensitivity in Section 6.2; that section only proposes one (p. 12, 29).

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Parameter sensitivity, subperiod and walk-forward tests were run | p. 5 |
| Live window (2015-2025) confirms the features; full re-estimation "left for a future revision" | p. 25 |
| Backtest versus live split expected to show no decay; not estimated | p. 25 |
| Group 3 and 4 gains expected to survive Romano-Wolf; not run | p. 29 |
| 20 bp cost "would modestly dampen" Sharpe; turnover 120-180% a year stated, no table | p. 29 |
| Lasso, weighted least squares and state-dependent regressions "planned" | p. 8-9, 28 |
| Acute-COVID window refinement "to be implemented" | p. 7 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | [[Dual momentum]]: absolute filter plus relative ranking across asset classes | technique | signal | Pairing harvests premia better than either alone (cited) | p. 3, 7 |
| 2 | [[Canary universe switch]] (breadth momentum and canary universe): switch to safe assets when few assets, or the canary assets, lose momentum | technique | signal | Recognises falling market health before drawdowns (cited) | p. 3, 7 |
| 3 | Absolute momentum only, see [[Time-series momentum signal]] (trend filter, moving average or threshold) on asset classes | technique | signal | Faber 2007: trend rules cut crisis drawdowns (cited) | p. 3, 7 |
| 4 | Relative momentum only, see [[Cross-sectional momentum]] (rank by lookback return) | technique | signal | Not argued | p. 7 |
| 5 | No card (rule not specified, heterogeneous). Optimised weighting: volatility scaling, inverse volatility, covariance, risk parity, minimum correlation | technique | sizing | Not argued; negative result attributed to estimation error | p. 8, 15 |
| 6 | No card (table is indicative only). Studentised circular block bootstrap for Sharpe differences (Ledoit-Wolf) | technique | evaluation | Parametric tests distort with fat tails | p. 9 |
| 7 | No card (research design, not a strategy rule). Regression of strategy Sharpe on 0/1 design features, errors clustered by group | principle | evaluation | Strategies in a family are not independent | p. 8 |

## 6. Regime observations

- Breadth coefficient is positive in 2000-02 and weak or negative in 5-year and COVID windows (Tables 5, 6, 8, 10).
- Canary is significantly positive over 30, 10 and 5 years and in 2020-23, negative in 2000-02, not significant elsewhere (Tables 4-11).
- 2022: stocks and bonds fell together, atypical for the sample (p. 31).

## 7. Acknowledged limits

- Few clusters (10), so inference is conservative; small groups (Group 5 has N = 2) (p. 8, 26).
- Features abstract from lookbacks, rebalancing and weighting details (p. 31).
- Third-party data, not reproducible exactly; US-centred ETF universe (p. 29-31).
- Publication bias: results are an upper bound for public rules (p. 29).

## 8. Not addressed

- Per-strategy Sharpe, return and drawdown tables; the rules of each strategy.
- Cost sensitivity, turnover per strategy, taxes, capacity.
- Clean hold-out and multiple-testing results; live-window regression output.
- Number of strategies considered before the 86 were kept.
