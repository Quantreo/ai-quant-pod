---
type: reading-note
source: paper
title: Value and Momentum Everywhere
authors: Asness, Moskowitz, Pedersen
affiliations: Asness (AQR Capital Management), Moskowitz (Chicago Booth, NBER, consultant to AQR), Pedersen (NYU Stern, Copenhagen Business School, AQR, CEPR, NBER). AQR invests in value and momentum strategies (p. 1 footnote).
year: 2013
venue: Journal of Finance 68(3), 929-985
doi: 10.1111/jofi.12021
pdf: "[[2013 - Asness Moskowitz Pedersen - Value and Momentum Everywhere.pdf]]"
version: accepted author manuscript (post-print), dated June 2012
tier: 1
read: full
tags: [value, multi-asset, monthly]
date: 2026-10-25
---

# Value and momentum everywhere (Asness, Moskowitz, Pedersen 2013)

## Summary

- **Finding**: value and momentum earn positive returns in all eight markets, gross. The 50/50 mix across all of them has a Sharpe of 1.36 (spread) to 1.45 (factor).
- **Mechanism**: each style is correlated across markets, the two are negatively correlated. Funding liquidity risk explains a small part: momentum loads positively, value negatively.
- **Where it works best**: the combination, because correlation is about -0.5 within each market. Commodities, country indexes and Japanese stocks have the highest value or momentum Sharpe ratios (Table I).
- **Weak spots**: bond value and momentum not significant; currency value and momentum t-stats 1.8 to 2.6; Japan momentum not significant. Cross-market correlations rose after 1998.
- **Main caveats**: gross of costs; value is a past 5-year return outside stocks; bond alternatives tried after a weak result; the GRS test rejects the model.

Page numbers follow the page number printed on the manuscript (PDF page minus 3). Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

No single cause is claimed. The authors set out a pattern and test two partial links.

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Common global factors drive value and momentum | Value correlated with value across asset classes, momentum with momentum, value with momentum negatively. First principal component loads one way on all value strategies and the other way on all momentum strategies (54% of stock covariance, 23% of all-class covariance). | Table II, Fig. 1; p. 14-17 |
| 2 | Funding liquidity risk is a partial source | Global funding liquidity PC: value beta -0.0094 (t = -4.74), momentum 0.0112 (t = 3.58), 50/50 mix 0.0013 (t = 0.58). Liquidity risk premium among the 48 test portfolios 24 bp a month, about 3% a year. | Table IV Panel B, Table V; p. 20-26 |
| 3 | Crowding story, offered as "simple and intuitive" | Momentum holds the most popular trades; liquidations hit crowded trades first. Not tested, "beyond the scope" of the paper. | p. 4, 21-22 |
| 4 | Limited arbitrage capital, possibly increasing | Correlations among value strategies 0.31 to 0.71 and among momentum 0.46 to 0.77, first to second half. Liquidity shock effects appear only after August 1998. | Table VII; p. 32-34 |

**Caveats raised by the authors**
- Liquidity risk explains only a small fraction of premia and co-movement (p. 5, 27).
- Opposite signs on one factor cannot explain why both premia are positive; value's positive return is "an even deeper puzzle" (p. 21).
- The equal mix of value and momentum is immune to funding liquidity risk and still earns large returns (p. 22).
- Behavioural and rational firm-based models do not predict the cross-asset correlation (p. 3, 13).
- The GRS test rejects the three factor model in all cases (p. 29).

**Ruled out**
- Macro variables (consumption growth, recessions, GDP growth, default and term spreads): few significant links globally; momentum negative on recessions in non-stock classes (Table III; p. 19).
- Market liquidity shocks: little relation to either strategy (Table IV; p. 21).

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | Stocks in US, UK, Europe ex-UK, Japan: largest names holding 90% of market cap (about the largest 17% of firms), price above $1, no ADRs, REITs, financials. 18 equity index futures markets, 10 currencies vs USD, 10 government bond markets, 27 commodity futures. | p. 5-7 |
| Period | Stocks and commodities from 1972 (Europe, Japan stocks 1974), indexes 1978, currencies 1979, bonds 1982, all to July 2011. | p. 6-7 |
| Value signal | Stocks: book-to-market, book lagged 6 months. Indexes: value-weighted BE/ME of constituents. Currencies, bonds, commodities: minus the past 5-year return (currencies including interest earned, 3-month LIBOR). | p. 7-9 |
| Momentum signal | Past 12-month raw return skipping the latest month (MOM2-12), same in every class. | p. 8 |
| Portfolios | Rank in each class, three equal groups P1 to P3, P3 minus P1. Stocks value-weighted, other classes equal-weighted. | p. 10 |
| Factor | Weight = rank minus mean rank, scaled to one dollar long and one dollar short (Eq. 1-2). | p. 10 |
| Combination | 50/50 of the value and momentum returns (Eq. 3). | p. 10 |
| Across classes | Weight each class by the inverse of its full-sample volatility. | p. 12-13 |
| Rebalancing | Monthly, naively; yearly rebalancing to equal weights said to give similar results. | p. 10, 30 |
| Costs | None. Gross excess returns. | p. 29 |

**Rule** (Eq. 1-3, p. 10), for security i with signal S, N securities:

$$w_{it}^{S} = c_t\,(\text{rank}(S_{it}) - \tfrac{1}{N}\textstyle\sum_i \text{rank}(S_{it})),\qquad r_t^{COMBO} = 0.5\,r_t^{VALUE} + 0.5\,r_t^{MOM}$$

**Data provenance** (p. 6-7)

| Class | Source |
| --- | --- |
| Stocks | CRSP and Compustat (US); Datastream and Worldscope (other) |
| Equity indexes | MSCI returns, prices and book values. Returns have no collateral return, so they act as excess returns. |
| Currencies | Datastream spot rates. Returns from forwards, dollar denominated, including the interest differential. Germany spliced with the Euro. |
| Bonds | Datastream bond index returns; Bloomberg short rates and 10-year yields; Consensus Economics inflation forecasts |
| Commodities | LME, ICE, CME, CBOT, NYMEX, COMEX, NYBOT, TOCOM. Daily excess return of the most liquid contract, compounded. No collateral return. |

## 3. Results

Gross, real data, in-sample, monthly series reported as annual numbers, to July 2011. All numbers are from Table I unless stated.

**Aggregate**

| Market | Value spread Sharpe (P3-P1 / factor) | Momentum spread Sharpe (P3-P1 / factor) | 50/50 Sharpe (P3-P1 / factor) | Value-momentum correlation (P3-P1 / factor) |
| --- | --- | --- | --- | --- |
| Global all classes | 0.72 / 0.73 | 0.76 / 0.81 | 1.36 / 1.45 | -0.46 / -0.55 |
| Global stocks | 0.58 / 0.52 | 0.54 / 0.68 | 1.01 / 1.21 | -0.54 / -0.64 |
| Global other classes | 0.54 / 0.57 | 0.67 / 0.65 | 1.11 / 1.20 | -0.40 / -0.47 |

Detail by market: Table I, p. 50-52. Excess return alphas against each class's market index: global all classes value 3.5% (t = 4.67), momentum 4.3% (t = 4.85) for P3-P1.

**By sub-group** (Table I Panel A and B)
- Currencies, 1979-2011, spread / factor: value mean 3.3% (t = 1.89) / 3.9% (t = 2.47), Sharpe 0.34 / 0.44. Momentum 3.5% (t = 1.90) / 3.0% (t = 1.77), Sharpe 0.34 / 0.32. 50/50 mix 3.4% (t = 3.51) / 5.6% (t = 3.89), Sharpe 0.63 / 0.69. Correlation -0.42 / -0.43.
- Currency value low, mid, high portfolio means: -0.5%, 0.3%, 2.8%. Momentum: -0.7%, 0.3%, 2.8%. The premium sits in the top third.
- Country indexes: value Sharpe 0.61 / 0.60; momentum 0.73 / 0.63; mix 1.16 / 1.00.
- Commodities: value 0.26 / 0.31 (t = 1.61 / 1.92); momentum 0.53 / 0.51; mix 0.71 / 0.77.
- Bonds, five-year yield change value: Sharpe 0.18 / 0.07, t = 0.97 / 0.39. Momentum 0.06 / 0.17, t = 0.35 / 0.88. Mix 0.19 / 0.20.
- Stocks: value Sharpe 0.29 (US) to 0.79 (Japan); momentum 0.33 (US) to 0.55 (Europe), Japan 0.09 (t = 0.57).
- Bond alternatives for value (Panel C, p. 52): real yield Sharpe 0.73, term spread 0.55, composite of three 0.91 (spread) and 1.10 (factor); composite alpha t = 4.40 and 5.48.

**Co-movement** (Table II, quarterly returns, p. 53)
- Stock value with other stock markets' value 0.68; with non-stock value 0.15. Stock momentum 0.65 and 0.37.
- Stock value against stock momentum -0.53; against non-stock momentum -0.26; non-stock value against stock momentum -0.16.

**Over time** (Table VII, p. 60)
- Before then after August 1998: correlation among value 0.16 then 0.64; among momentum 0.43 then 0.71.
- After 1998, value Sharpe 0.85 when funding liquidity worsens, 0.28 when it improves. Momentum 0.19 and 0.77. Mix 0.88 and 1.07.

**Asset pricing tests** (p. 23-29, Fig. 5-6, Table VI)
- Value and momentum of one market priced by those of the others: cross-sectional R2 0.55, average absolute alpha 22.6 bp a month (Fig. 5).
- Three factor model (market, VAL everywhere, MOM everywhere), 48 test portfolios: GRS 2.66, average absolute alpha 18 bp, cross-sectional R2 0.72, covariance share 74% (Table VI). Global CAPM: 35 bp, 57%.
- Fama-French four factor on the same assets: 35 bp, R2 0.55 (Table VI).

**Inconsistencies in the source**
- Text gives the all-class 50/50 Sharpe as 1.42 (p. 13). Table I gives 1.36 (spread) and 1.45 (factor).
- Text gives an average value-momentum correlation of -0.54 for non-stock classes (p. 13). Table I: -0.17 to -0.42 (spread), -0.35 to -0.46 (factor).
- Table I factor 50/50 means exceed both components: country indexes 10.6% against 5.7% and 7.4%; commodities 17.1% against 7.3% and 11.5%. An equal average cannot do that. Spread means are consistent.
- Text says the three factor model captures 84% of covariation (p. 28). Table VI says 74%.

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Value and momentum premia are larger in smaller, less liquid stocks, so results are conservative | p. 5-6, fn 5 |
| Momentum in currencies and indexes is stronger without skipping the latest month | p. 9 |
| Weighting non-stock classes by ex ante volatility, or rebalancing annually, gives similar results | fn 8 |
| Decile sorts, other weightings, ex ante 2% volatility scaling and market hedging give similar conclusions | p. 31 (Tables A6 to A8 in the appendix) |
| Real world trading costs of these strategies are much lower than model estimates; net returns of non-stock classes would be closer to equities | p. 29-30 |
| Long-only value and momentum still earn abnormal returns | p. 31 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | Momentum: past 12-month return skipping the latest month, same in every class | technique | signal | Avoids one-month reversal; uniform across classes to limit data snooping. [[Cross-sectional momentum]] | p. 8-9 |
| 2 | Value as minus the past 5-year return (with interest for currencies) | technique | signal | Simple and uniform; correlated 0.83 with book-to-market in US stocks. [[Currency value signal]] | p. 9, Table A1 |
| 3 | Rank-minus-mean weights, one dollar long and short; three-group sort | technique | sizing | Rank limits outliers. [[Long-short portfolio weighting]] | Eq. 1, p. 10-11 |
| 4 | Equal 50/50 mix of value and momentum, classes weighted by inverse volatility | technique | sizing | Negative correlation and two positive premia. [[Value and momentum combination]] | Eq. 3, p. 10, 13 |
| 5 | Regression of strategy returns on funding liquidity shocks (AR(2) residuals of spreads) | principle | evaluation | Tests exposure to funding liquidity. [[Funding liquidity beta regression]] | p. 19-22, Table IV |
| 6 | Alternative bond value measures: real yield, term spread, composite | technique | signal | Weak result with the simple measure; composite diversifies measurement error. No card: bonds only, tried after the weak result | p. 14, Table I C |
| 7 | Book-to-market value for stocks and index constituents | technique | signal | Standard. No card: needs fundamentals the desk does not hold | p. 7-9 |
| 8 | Averaging value and momentum series across all markets before testing common exposure | principle | evaluation | Averages out market noise: average t-stat of liquidity betas -0.95 and 1.81 vs -3.25 and 4.43 on the average series. No card | p. 22, Fig. 4 |

## 6. Regime observations

- Value does better when funding liquidity worsens, momentum when it improves, but only after August 1998 (Table VII).
- Correlations among value strategies and among momentum strategies rise after 1998 and in recessions (Table VII Panel B, p. 33).

## 7. Acknowledged limits

- Gross returns only; costs and capacity left to other papers (p. 29).
- Measures are intentionally simple; bonds do not produce significant premia (p. 13-14, 32).
- Value measure for non-stock classes is a past return, not a fundamental (p. 9).
- Liquidity proxies are noisy; the GRS test rejects every model (p. 27, 29).
- Premia have declined slightly over time (p. 32).

## 8. Not addressed

- Transaction costs, slippage and capacity of the strategies themselves.
- Currency value from price levels (CPI): not tested; value is a 5-year past return only.
- Drawdown depth and crash behaviour of the combination (cumulative returns only in Fig. 2, sum of log returns).
- Currency results on a sub-period basis or leaving a currency out.
