---
type: reading-note
source: paper
title: Cryptocurrency return reversals
authors: Kozlowski, Puleo, Zhou
affiliations: Dolan School of Business, Fairfield University; College of Business, University of New Haven
year: 2021
venue: Applied Economics Letters 28:11, pp. 887-893
doi: 10.1080/13504851.2020.1784831
pdf: "[[2021 - Kozlowski Puleo Zhou - Cryptocurrency return reversals.pdf]]"
version: author manuscript posted on SSRN (abstract 4256709), journal reference printed on p. 1
tier: 1
read: full
tags: [reversal, crypto, daily]
date: 2026-10-24
---

# Cryptocurrency return reversals (Kozlowski, Puleo, Zhou 2021)

## Summary

- **Finding**: on 199 coins, 2015 to mid-2019, equal-weighted loser-minus-winner quintiles earn 7.37% a day, 10.03% a week, 28.22% a month, gross (Table 1).
- **Mechanism**: authors read the reversal as market inefficiency (overreaction) plus compensation for liquidity provision, because it is largest in small and illiquid coins (p. 2, 6, 8).
- **Where it works best**: small-cap, low-liquidity coins: 18.63% a day, 36.31% a week, 64.05% a month (Table 3, Panel A).
- **Weak spots**: large and liquid coins show only 0.44% a day, -1.58% a week (n.s.), 1.25% a month (n.s.) (Table 3, Panel B). Monthly spread loses in 10 of 54 months.
- **Main caveats**: no transaction costs, no shorting constraints, CoinMarketCap volume-weighted closes, coin list fixed by size at end-2014. Spreads are gross and in-sample.

Page numbers follow the printed pagination of the SSRN manuscript (1 to 11). Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Reversals come from investor overreaction, a sign of inefficiency | Literature cited (Lehmann, Cooper). The effect does not decline over time, so behavioral factors "likely still contribute". | p. 1, 8 |
| 2 | Reversals are compensation for liquidity provision: buyers absorb excess selling only at a discount | Reversal is larger in low-liquidity subsamples within both size groups. | Table 3, Panels A-B; p. 6-8 |
| 3 | Size matters: inattention and biases weigh more on small assets | Small-cap spreads exceed large-cap spreads at every frequency. | Table 3; p. 6 |

**Caveats raised by the authors**
- Lack of significance for small liquid coins at monthly horizon may reflect low power of subsample tests (fn 5, p. 6).

**Ruled out**
- A short-run effect driving the longer horizons: the daily spread is "roughly one-quarter" of the monthly spread (p. 4).
- Dependence on market stress (VIX) or on calendar period: "no meaningful effect" (p. 8, Table 3 Panels C-D).
- Outliers: excluding observations beyond 2.24 SD keeps spreads at 6.78%, 8.69%, 15.72% (fn 4, p. 4).

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | 200 largest coins by market cap on 28 Dec 2014 (final 199, Vertacoin excluded as an outlier). About 99.96% of listed market cap at start. | p. 2-3, fn 3, Table A1 |
| Period | January 2015 to June 2019 (54 months) | p. 2, Table 1 |
| Signal | REV = return over the prior period t (day, week or month) | p. 2 |
| Entry | Sort into five equal-weighted quintiles on REV at the end of each period | p. 3 |
| Exit | Hold one period, then re-sort | p. 3 |
| Horizon | Daily, weekly, monthly rebalancing | p. 3 |
| Sizing | Equal weight within quintile | p. 3 |
| Portfolio | Long quintile 1 (losers), short quintile 5 (winners) | p. 3 |
| Rebalancing | Every period | p. 3 |
| Costs | Not stated by the authors | |
| Liquidity filter | Drop coin-periods with monthly turnover below 1% (or the daily and weekly equivalent) | fn 2, p. 3 |
| Data and tools | CoinMarketCap daily volume-weighted prices and aggregate volume; Fama-MacBeth regressions with Newey-West t-stats; regressors winsorised at 1% and 99% | p. 2-4 |

**Rule** (p. 2-3): R(i,t+1) = (P(i,t+1)/P(i,t) - 1) x 100. Long the bottom quintile of R(i,t), short the top quintile, equal weights, hold one period.

Regression (Eq. 2, p. 3): R(i,t+1) = b0 + b1 REV + b2 log(SIZE) + b3 TURN + b4 ILLIQ. ILLIQ is the Amihud ratio, mean of |R|/VOL x 100 over the period (Eq. 1).

**Data provenance**
- Prices are CoinMarketCap volume-weighted averages across exchanges, not exchange closes (p. 2, fn 1).
- Treatment of coins that stop trading: not stated.
- Sample sizes: 6,782 coin-months, 29,952 coin-weeks, 261,377 coin-days (p. 3).

## 3. Results

All results are real data, in-sample, gross of any cost.

**Aggregate** (Table 1, Panel A)
- Loser minus winner: 7.37% daily (t = 24.23), 10.03% weekly (t = 7.03), 28.22% monthly (t = 3.28).
- Losers: 6.25%, 12.57%, 39.72%. Winners: -1.11%, 2.55%, 11.49%. Returns fall almost monotonically from quintile 1 to 5.
- Monthly long-short (Panel B): median 15.39%, max 346.93%, min -61.35%, SD 63.14%, skew 3.05, positive in 81.48% of months (44 of 54).
- Regressions (Table 2): REV coefficient -0.27 daily, -0.17 to -0.13 weekly, -0.12 monthly, all significant with and without controls. log(SIZE) negative and significant. TURN and ILLIQ not significant.

**By sub-group** (Table 3, Panels A-B, loser minus winner)
- Small cap, low liquidity: 18.63% daily, 36.31% weekly, 64.05% monthly.
- Small cap, high liquidity: 4.48%, 7.97%, 12.15% (monthly t = 1.45).
- Large cap, low liquidity: 5.69%, 11.00%, 19.08%.
- Large cap, high liquidity: 0.44% (t = 2.96), -1.58% (t = -1.61), 1.25% (t = 0.10).
- Losers carry the spread: in Table 1 losers have the lowest size and the highest ILLIQ mean (Panel C).

**Horizon and parameters**
- Spread rises with holding period in level (Table 1). Daily is the most significant.
- Turnover filter: results "robust" to no filter or higher filters, not shown (fn 2).

**Over time**
- First half vs second half: daily 7.96% vs 6.77%, weekly 7.58% vs 12.47%, monthly 32.98% vs 23.46% (t = 1.73) (Table 3, Panel D).
- Low vs high VIX: daily 7.55% vs 7.17%, weekly 10.82% vs 9.18%, monthly 31.22% vs 25.22% (Panel C).
- Monthly spread is dominated by a few large months: ≈ 340% early 2018, ≈ 200% late 2016, ≈ 170% mid 2015. Largest loss ≈ -60% in early 2016 (Fig. 1).

**Link to other strategies**
- Size: log(SIZE) negative in all regressions (Table 2).

**Inconsistencies in the source**
- The notes to Tables 1-3 say ***, ** and * denote significance at 10%, 5% and 1%. The text calls *** coefficients significant "at the one percent level" (p. 4). Both cannot hold.
- The text says Panels C and D show "no meaningful effect" (p. 8), yet the monthly second-half spread is only marked * (t = 1.73) against *** in the first half.

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Results robust to no turnover filter or higher filters | fn 2, p. 3 |
| Results robust to including Vertacoin | fn 3, p. 3 |
| Large reversal after both high and low Economic Policy Uncertainty | fn 6, p. 8 |
| First to run predictive cross-sectional regressions on crypto returns | p. 2 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | Prior-period return quintile sort, long losers short winners | technique | signal | Standard reversal test (Jegadeesh). Card [[Cross-sectional mean reversion]] | p. 3 |
| 2 | Double sort by size then by Amihud illiquidity and prior return | technique | evaluation | Isolates size and liquidity effects. Card [[Conditional double sort]] | p. 6, Table 3 |
| 3 | Split by median VIX | technique | evaluation | Nagel: reversal profits track VIX as a liquidity premium proxy. Card [[Market state split]] | p. 8 |
| 4 | Minimum turnover filter (1% a month) | technique | universe | Limits microstructure effects. Card [[Minimum price and size filter]] | fn 2 |
| 5 | Fama-MacBeth with size, turnover, illiquidity controls | technique | evaluation | Controls known return correlates | p. 3 |
| 6 | Outlier trimming at 2.24 SD (Aguinis et al.) | technique | evaluation | Checks outliers do not drive the result | fn 4 |

## 6. Regime observations

- Reversal stays significant at daily and weekly horizons in both VIX regimes and both halves (Table 3, Panels C-D).
- Large monthly payoffs cluster in crypto boom periods (≈ Fig. 1).

## 7. Acknowledged limits

- Subsample tests have reduced power (fn 5).

## 8. Not addressed

- Transaction costs, bid-ask spreads, slippage.
- Ability to short the winners, borrow costs.
- Value-weighted portfolios.
- Out-of-sample test.
- Drawdowns and Sharpe ratio of the long-short.
- Delisted coins and how missing prices are handled.
- Long and short legs reported separately against a benchmark.
