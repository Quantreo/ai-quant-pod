---
type: reading-note
source: paper
title: "The Impact of Volatility Targeting"
authors: Harvey, Hoyle, Korgaonkar, Rattray, Sargaison, Van Hemert
affiliations: Harvey (Duke University, advisor to Man Group plc); the other authors (Man Group plc)
year: 2018
venue: SSRN working paper 3175538
doi:
pdf: "[[2018 - Harvey Hoyle Korgaonkar et al - The Impact of Volatility Targeting.pdf]]"
version: June 25th, 2018, working paper, not peer-reviewed
tier: 2
read: full
tags: [low-vol, multi-asset, daily]
date: 2026-10-25
---

# The impact of volatility targeting (Harvey et al. 2018)

## Summary

- **Finding**: scaling to constant volatility lifts the Sharpe ratio of US equities from 0.40 to 0.48-0.51 (1927-2017, gross and net) and cuts the left tail, vol of vol and kurtosis in every asset class (Table 3, p. 8; abstract).
- **Mechanism**: only risk assets show a leverage effect (negative link between return and volatility change), so scaling adds time-series momentum; this explains 45% to 60% of the cross-section of Sharpe gains (p. 19-21).
- **Where it works best**: equities (+0.08 to +0.11), credit with fast estimates (0.30 to 0.49, 10-day half-life), balanced and risk parity portfolios (0.80 to 0.91) (Tables 3, 7-9).
- **Weak spots**: US bonds 1963-2017 fall from 0.25 to 0.05-0.09; Treasury futures, currencies, commodities show no Sharpe gain; equities do not improve in 1957-1987 (Tables 5-6; Fig. 4, 10).
- **Main caveats**: costs are post-2008 estimates applied to all years; scaling constant k set on the full sample; bonds are US only; no significance test except one regression (fn 15).

Page numbers follow the PDF, which equals the printed page. Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Volatility clusters, so recent volatility predicts near-term volatility | Quintile sort on last month's volatility: next-month volatility rises, equity mean return shows no clear pattern | p. 2, 7; Fig. 2 |
| 2 | Only risk assets (equity, credit) have a leverage effect: return and variance change are negatively correlated | Correlation of monthly return with variance change, equities, 10 industries, credit, 50 futures | p. 19-20; Fig. 13 |
| 3 | The leverage effect makes volatility scaling a momentum bet: smaller after losses, larger after gains. For other assets the correlation is mostly negative, a mean reversion bet | Correlation of 1/vol with past 21, 65, 130, 260-day returns | p. 20-21; Fig. 14 |
| 4 | Momentum-ness explains the Sharpe gain across assets | R-squared 45% (20-day half-life), 60% (90-day), on 1-month momentum | p. 21; Fig. 15 |
| 5 | Bonds gain nothing because high-volatility quintiles had higher returns, and 1960-1980 had negative returns with low volatility | Fig. 6, Table 5, Fig. 7 | p. 12-13 |

**Caveats raised by the authors**: US is an ex-post winner; bond result may change if bonds turn credit-like (p. 22). Bond volatility regimes before the mid-1980s may be structural breaks (p. 11, 13). Costs are current estimates applied to history (fn 13, 17). Maximum drawdown is "not a robust metric" (p. 25).

**Ruled out**: the Black (1976) leverage explanation is cited, with the reverse volatility-feedback story of Bekaert and Wu (fn 23); the authors do not choose between them.

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | US equities (Fama-French all-US, 10 industries), US bonds, S&P 500 and 10-year Treasury futures, US credit hedged with Treasuries, 50 futures and forwards (6 agricultural, 6 energy, 7 metal, 9 currencies against USD, 10 equity indices, 9 bonds, 3 interest rates) | Table 1, p. 3-4 |
| Period | Equities 1927-2017; bonds 1962/63-2017; futures, credit, portfolios 1988-2017 | Table 1 |
| Signal | Standard deviation of daily returns, exponential weights, zero mean; half-lives 10, 20, 40, 60, 90 days | p. 4 |
| Sizing | Excess return times target / estimate lagged to t-2, times k | p. 4 |
| Rebalancing | Daily; portfolios rebalanced daily to the target mix | p. 4, 16 |
| Costs | 1.0 bp equities, 0.5 bp bonds and credit, 1.0 gold, 2.0 oil, 3.5 copper, per notional traded | p. 5 |
| Target | 10% annualised | p. 4 |

**Rule**: r_scaled(t) = r(t) x sigma_target / (sigma(t-2) x k_scaled), k about 1, set so that the full-sample volatility equals the target. Unscaled: r(t) x k_unscaled, same ex-post 10% (p. 4). Portfolio level: a second scaling on the portfolio's own volatility (p. 16). Evaluation on 1-month overlapping returns (30 calendar days or 21 weekdays) (p. 5).

**Data provenance**: French data library (calendar days, Saturdays before 1952, p. 5); US bond returns proxied from 10-year yields assumed par, semi-annual, repriced daily (p. 3-4, fn 7); credit from the BoA ML US Corporate Master index hedged with Treasuries, after Cook et al. (2017) (p. 4); futures and forwards, Man AHL data (Table 1). Roll turnover excluded (p. 6). Intraday: 5-minute returns, 9:15 to 14:00 Chicago, squared and summed daily, exponentially averaged (p. 5).

## 3. Results

All real data, in-sample, 10% full-sample volatility, excess returns. Sharpe on 1-month returns.

**Aggregate**
- Equities All US 1927-2017: Sharpe 0.40 unscaled, 0.48 (10-day) to 0.51 (60 and 90-day), gross equals net; vol of vol 4.6% to 1.7-2.2%; 1% left tail -11.4% to -8.3 / -10.1%; 99% right tail 11.8% to 7.3-7.7%; turnover 4.66 to 0.56 (Table 3, p. 8).
- Regression of scaled on unscaled daily returns (20-day): intercept 0.64 bp, t 3.05 (Newey-West, 30 lags), R-squared 0.73 (fn 15).
- Maximum drawdown, equities 1927-2017: -60.9% to -42.8% (Fig. A3, p. 25).

**By sub-group**
- Equities by period and 10 industries: Sharpe improves in all cases except 1957-1987; vol of vol and shortfall improve in all (Fig. 4, p. 10).
- S&P 500 futures 1988-2017: Sharpe 0.50 to 0.57-0.60 (daily vol), 0.60-0.63 (5-minute vol); net costs 0 to 0.01 (Table 4, p. 10).
- US bonds 1963-2017: Sharpe 0.25 to 0.05-0.09; 1% left tail -8.4% to -8.6 / -9.5% (worse); vol of vol 3.9% to 2.1-2.6% (Table 5, p. 12).
- 10-year Treasury futures 1988-2017: Sharpe 0.64 to 0.63 (0.63-0.66 intraday); left tail slightly worse (-7.3% to -7.5%); vol of vol 2.5% to 1.2-1.6% (Table 6, p. 14).
- US credit 1988-2017: Sharpe 0.30 to 0.49 (10-day, 0.46 net), 0.41 (20), 0.30 (40), 0.24 (60), 0.18 (90); left tail better only with fast estimates (Table 7, p. 15).
- 50 futures and forwards: Sharpe slightly better for equity indices, similar for other sectors; vol of vol and shortfall better for almost all (Fig. 10, p. 16, chart reading).
- Balanced 60-40 (risk terms), 1988-2017: Sharpe 0.80 unscaled, 0.87 asset-level, 0.91 asset and portfolio level (0.90 net); 1% left tail -9.7% to -7.3% (Table 8, p. 17).
- Risk parity 25-25-25-25 (equity, bond, credit, gold-copper-oil), 1988-2017: Sharpe 0.80, 0.89, 0.91 (0.89 net); 1% left tail -12.8% to -8.2%; mean notional 268% to 402% (Table 9, p. 18).
- Maximum drawdown: balanced -28.1% to -22.2%; risk parity -42.1% to -32.1% (p. 25).

**Horizon and parameters**
- Equity Sharpe barely depends on half-life (0.48 to 0.51); left-tail gain is largest for the fastest estimate (Table 3).
- Credit reverses with slow estimates (Table 7). Bonds and Treasury futures are flat across half-lives (Tables 5-6).
- Intraday volatility gives slightly better Sharpe, vol of vol and left tail at similar turnover (p. 11).
- Equal-weight windows and 3- or 5-day overlapping returns: "similar results", not reported (p. 4).

**Over time**
- Equities: scaled outperforms except mid-sample (Fig. 3, p. 9). Bond underperformance is solely pre-1980 (p. 13).
- Equity volatility autocorrelation about 0.6 at lag 1, about 0.2 at 12 months; 1958-1987 lower. Bond variance much more persistent (p. 28; Fig. B1-B2). Futures sectors: about 0.5 at lag 1, 0.1-0.2 at lag 12 (p. 15; Fig. 9).

**Link to other strategies**: scaling is likened to a time-series momentum overlay (p. 2, 19). A trend overlay is suggested for long portfolios, not tested here (p. 22).

**Inconsistencies in the source**
- Table 3 title says 1927-2017, its caption 1927-2016. Table 4 and Table 6 captions say 1988-2016, their titles 1988-2017.
- Figure 2 and Figure 6 captions say "sorting on the previous month's return"; the text says previous month's volatility (p. 7, 12).
- Table 5 title 1963-2017, caption 1963-2016; the data start in 1962 (p. 3).

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Similar results with equal-weight window or 3-5 day returns | p. 4 |
| Similar results at a 3-month evaluation frequency | p. 8 |
| Net results in figures "very similar" to gross | p. 5 |
| Volatility scaling may help bonds that turn credit-like | p. 22 |
| A trend overlay may further improve a long portfolio | p. 22 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | [[Volatility targeting]]: scale returns by target / EWMA volatility lagged to t-2, k fixed on the full sample | technique | sizing | Volatility clusters; expected return does not rise with it | p. 4, 7 |
| 2 | [[Volatility targeting]] variant: volatility from 5-minute returns | technique | sizing | More precise estimate | p. 5, 11 |
| 3 | [[Volatility targeting]] variant: scaling at asset level, then again at portfolio level | technique | sizing | Adjusts for time-varying correlation | p. 16-17 |
| 4 | [[Volatility scaling momentum check]]: correlation of 1/vol with past returns, and of return with variance change | technique | evaluation | Tells which assets gain from scaling | p. 19-21 |
| 5 | [[Volatility regime filter]] read: quintiles of last month's volatility, next-month mean and volatility | technique | evaluation | First sign of whether scaling can raise Sharpe | p. 7, 12 |
| 6 | Vol of vol, mean shortfall, mean exceedance, tail kurtosis | technique | evaluation | Left tail matters more than skewness | p. 5-6, 24 |
| 7 | Both versions scaled to the same full-sample volatility, k fixed ex post | technique | evaluation | Comparability across assets | p. 4 |

## 6. Regime observations

- Equity volatility was high in the 1930s, early 2000s and 2007-2009; Black Monday is the worst day (p. 6).
- Bonds: low volatility before 1967 and in 1964-1980, then structural change, inflation targeting from the mid-1980s (p. 11-13).

## 7. Acknowledged limits

US assets only; US bond result may not carry over (p. 22). Costs reflect the post-2008 environment (fn 13). Intraday data only for S&P 500 and Treasury futures (p. 22). Drawdown is path-dependent (p. 25).

## 8. Not addressed

Significance of the Sharpe gains beyond one equity regression; out-of-sample or real-time scaling (k is full-sample); leverage limits and financing cost of the scaled exposures (mean notional up to 510% for credit, Table 7); non-US equities beyond index futures; ETF implementation.
