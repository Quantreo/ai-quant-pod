---
type: reading-note
source: paper
title: Time series momentum
authors: Moskowitz, Ooi, Pedersen
affiliations: Moskowitz (University of Chicago Booth, NBER), Ooi (AQR Capital Management), Pedersen (AQR Capital Management, NYU, Copenhagen Business School, NBER, CEPR)
year: 2012
venue: Journal of Financial Economics 104, 228-250
doi: 10.1016/j.jfineco.2011.11.003
pdf: "[[2012 - Moskowitz Ooi Pedersen - Time Series Momentum.pdf]]"
version: published
tier: 1
read: full
tags: [trend, multi-asset, monthly]
date: 2026-10-21
---

# Time series momentum (Moskowitz, Ooi, Pedersen 2012)

## Summary

- **Finding**: own past 12-month return sign predicts next-month return in all 58 futures, 1985-2009. Diversified Sharpe ratio above 1, gross. Trend lasts a year, then partly reverses.
- **Mechanism**: under-reaction then delayed over-reaction, and/or speculators paid by hedgers for liquidity. Authors leave both open and do not rule out a rational explanation.
- **Where it works best**: 12-month lookback, 1-month hold, alpha t = 6.61 (best cell). Significant in all four asset classes. Largest quarterly gains in extreme S&P 500 quarters.
- **Weak spots**: alpha over always-long is significant for only 26% of contracts. Bond profit is mostly mean return. Currencies turn negative at long lookbacks. Losses at trend reversals.
- **Main caveats**: no costs. Specification chosen on the tested sample. Pre-futures history uses index and spot data. Several robustness claims shown without numbers.

Page numbers follow the journal pagination (228-250). Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Under-reaction, then delayed over-reaction to information | Returns continue about 12 months, then partly reverse. Reversal is partial, so under-reaction "appears to be part of the story". Only the spot-price component reverses. Cumulative response ≈3.9% near month 12, ≈3.7% at month 36. | Fig. 1, 6A, 7A-B; p. 245, 248-249 |
| 2 | Speculators earn a premium from hedgers for liquidity | Speculators sit with the trend in every CFTC contract except the S&P 500, build up to month 0 and unwind by about month 12. Roll-return shock keeps rising, ≈2.6% at month 36, no reversal. | Fig. 5, 6B, 7C; p. 244-248 |
| 3 | Positive auto-covariance of returns drives the profit | Main component of TSMOM and XSMOM profit. Squared mean return is smaller, except in bonds. | Table 5B; p. 244 |

Claim 2 is put as "One explanation might be" (p. 246). Authors' conjecture: hedging pressure acts on roll return, information diffusion on spot price (p. 247).

**Caveats raised by the authors**
- TSMOM is more correlated across asset classes than passive long positions. Behavioural models do not address this (p. 229, 240).
- Very different investors produce the same pattern at the same time (p. 229).
- No link with sentiment measures (p. 229, Table 3C).
- A rational theory cannot be ruled out (p. 230).
- Causality between positions and returns is indeterminate (p. 245-246).
- Speculators do not keep piling in. Any over-reaction from trading would come from hedgers (p. 245).
- Change in net speculator position loses significance once past return is added. Interaction terms are not significant (Table 6, p. 248).

**Ruled out**
- Crash-risk compensation: returns are largest in extreme markets, up and down (p. 238-239, Table 3C).
- Funding liquidity (TED), volatility (VIX), sentiment: no significant relation (Table 3C; p. 239-240).
- Illiquidity: Sharpe vs illiquidity correlation -0.16, so liquid contracts do slightly better (Fig. 2; p. 239).

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | 58 futures and forwards: 24 commodities, 12 currency pairs, 9 equity indexes, 13 government bonds. Among the most liquid contracts. | p. 230, Table 1 |
| Period | Data 1965-2009. Results from 1985, for breadth and liquidity. | p. 230, 236 |
| Signal | Sign of the past k-month excess return: long if positive, short if negative. Benchmark k = 12, no month skipped. | p. 233, 236 |
| Entry and exit | For h = 1, position reset each month from the new sign. No other exit rule stated. | p. 233 |
| Horizon | Hold h months. Grid k and h in {1, 3, 6, 9, 12, 24, 36, 48}. Benchmark h = 1. | Table 2 |
| Sizing | 40% / sigma per position. Sigma: EWMA of squared daily returns, centre of mass 60 days, annualised with 261, lagged one period. | p. 233, 236 |
| Portfolio | Equal weight across the S(t) contracts available at t. Volatility about 12% a year. Margin use about 5-20%. | p. 236, fn. 8 |
| Rebalancing | Monthly. For h above 1, average of the h active portfolios. | p. 233-234 |
| Costs | None stated. Sharpe ratios are called gross. | Fig. 2 |

**Rule** (Eq. 5, p. 236), per contract s, then averaged over the S(t) available:

$$r^{TSMOM,s}_{t,t+1} = \text{sign}(r^s_{t-12,t}) \cdot \frac{40\%}{\sigma^s_t} \cdot r^s_{t,t+1}$$

**Data provenance** (p. 230-231, 239, App. A)

| Item | Source | Before futures existed |
| --- | --- | --- |
| Equity indexes | Datastream futures | MSCI country index returns |
| Bonds | Datastream futures, constant duration (2, 4, 7, 20 years) | JP Morgan country bond index returns |
| Currencies | Citigroup spot and forward rates from 1989 (CAD 1992, NZD 1996) | Datastream spot, Bloomberg IBOR |
| Commodities | LME, ICE, CME, CBOT, NYMEX, COMEX, TOCOM | Not stated |
| Positions | CFTC, 1986-2009. 25 contracts in App. A.5, 29 in Table 1. | Not applicable |

Returns: daily excess return of the most liquid contract, compounded. Start dates run Jan-65 to Dec-98 (Table 1).

## 3. Results

Real data, in-sample, 1985-2009, gross of costs, unless stated. The 12 / 1 rule was chosen "based on" Fig. 1 and Table 2, the same sample (p. 236).

**Aggregate**

| Metric | Value | Where |
| --- | --- | --- |
| Diversified Sharpe ratio | "Greater than one", about 2.5 times the equity market. No exact figure, sample not stated. | p. 230 |
| Contracts with positive profit | 58 of 58. 52 significant at 5%. | p. 236 |
| Alpha over always-long, per contract | Positive in 90%. Significant in 26%. | p. 236 |
| Alpha vs MSCI World, SMB, HML, UMD | 1.58% per month (t = 7.99), 4.75% per quarter (t = 7.73) | Table 3A |
| Alpha vs value and momentum "everywhere" | 1.09% per month (t = 5.40) | Table 3B |
| Squared market return, quarterly | 1.99 (t = 3.88) | Table 3C |

**By sub-group**

| Class | Alpha t, 12 / 1 | Sharpe per contract, gross (≈) | Auto / mean squared / total, in % | Within-class correlation, TSMOM / passive |
| --- | --- | --- | --- | --- |
| Commodities | 4.66 | 0.02 (corn) to 0.78 (zinc) | 0.43 / 0.17 / 0.59 | 0.07 / 0.19 |
| Equity indexes | 3.77 | 0.34 (ASX, FTSE 100) to 0.83 (FTSE/MIB) | 0.83 / 0.17 / 1.00 | 0.37 / 0.60 |
| Bonds | 3.53 | 0.13 (3Y Australia) to 1.05 (2Y US) | 0.35 / 0.70 / 1.05 | 0.38 / 0.63 |
| Currencies | 3.41 | 0.05 (EUR-SEK) to 0.53 (USD-JPY) | 0.80 / 0.17 / 0.96 | 0.10 / -0.04 |
| Where | Table 2B-E | Fig. 2 | Table 5B | Table 4A |

- Bonds: mean squared is 0.70 of 1.05, about two thirds (computed from Table 5B). Units of Table 5B are not stated.
- Weakest contracts (≈ Fig. 2): corn 0.02, natural gas 0.05, EUR-SEK 0.05, AUD-NZD 0.09, soybeans about 0.1.
- 6 of 58 contracts not significant at 5% (58 minus 52, p. 236).
- Across classes TSMOM correlation is 0.05 to 0.21, above passive long (Table 4B).

**Horizon and parameters** (Table 2, alpha t-stats)
- All assets: best cell 12 / 1, t = 6.61. Lookbacks 1 to 12 with holds 1 to 12 all have t of at least 2.85 (computed from Table 2A).
- Fades with horizon: 24 / 24 gives 0.20. 24 / 36 gives -0.09, 24 / 48 gives -0.33.
- Currencies: 48-month lookback negative at every hold (-0.55 to -2.34). Lowest cell -2.42 at 36 / 48 (Table 2E).
- Commodities: six slightly negative cells at lookbacks 24 and 36, lowest -0.60. Equities and bonds: none negative.
- Sign regression: 12 positive lags, nine significant (Fig. 1B, p. 233). Most later lags negative.

**Over time and in extreme markets**
- 1966-1985: Sharpe ratio 1.1, "statistically significant". Authors call it out-of-sample. Fewer contracts, added at a referee's request (p. 237-238, fn. 9).
- Q3 2008 losses, Q4 2008 large gains, March to May 2009 sharp losses at the end of the crisis (p. 238).
- Quarterly returns ≈ -11% to ≈ +25%, largest with the biggest S&P 500 moves, up and down (Fig. 4).
- Fig. 3 (log scale) shows a steady rise, well above a passive long portfolio at the same ex-ante risk. No end value in the text.

**Link to other strategies**

| Regression | Result | Where |
| --- | --- | --- |
| TSMOM on cross-sectional momentum (XSMOM) | beta 0.66 (t = 15.17), R² 44%, alpha 0.76% (t = 5.90) | Table 5A |
| TSMOM by class on own-class XSMOM | R² 56% (FX) to 14% (FI). Alphas t of 2.79 or more. | Table 5A |
| XSMOM on TSMOM | Alphas not significant. Equity indexes 0.29% (t = 1.86). | Table 5C |
| UMD on TSMOM | loading 0.49 (t = 6.56), alpha -0.28% (t = -0.93) | Table 5C |
| Managed futures index, 1994-2009 | loading 0.55 (t = 9.60), alpha -0.30% (t = -1.37) | Table 5C |

**Inconsistencies in the source**
- Text (p. 240) gives 0.10 for commodities and 0.07 for currencies. Table 4A gives 0.07 and 0.10. Table values used.
- Text (p. 248) says spot and roll coefficients are "almost the same" in the multivariate regression. Table 6 gives 0.017 or 0.014 for spot, 0.030 for roll.
- Text (p. 233) says all 12 recent lags are positive "in both cases". Fig. 1A (≈) shows lag 12 slightly negative. Chart reading, to check.
- Table 1 lists 9 currency forwards against USD. Text and Fig. 2 count 12 pairs.
- App. A.5 omits the US Treasury futures that Table 1, Fig. 5 and p. 231 include.

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Robust among illiquid contracts (feeder cattle, lumber, tin, emerging markets, others). "(not reported)" | fn. 4, p. 230 |
| Far contract: slightly stronger for commodities, almost unchanged for financials | p. 231 |
| Robust to richer volatility models. OLS without scaling similar. | p. 233, fn. 7 |
| Robust "across a number of subsamples". Only 1966-1985 Sharpe is shown. | p. 228, 238 |
| Pre-1985 data "similar (and generally more significant)" | p. 236 |
| Equity results almost identical with cash indexes | p. 236 |
| Same pattern in each asset class. Chart only; bonds look weaker at lags 2 to 7 (≈ Fig. 1C). | p. 233-234 |
| Linear TSMOM (Eq. 7) has significant alpha to XSMOM | p. 244 |
| VAR robust to lag lengths 12 to 24 and to Cholesky ordering | p. 246 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | [[Time-series momentum signal]]: sign of own past 12-month excess return | technique | signal | Convention of the literature, Fig. 1, Table 2 | p. 236 |
| 2 | [[Volatility targeting]]: size 40% / sigma | technique | sizing | Aggregates unlike contracts; stable volatility | p. 233, 236 |
| 3 | [[Volatility targeting]]: EWMA volatility, centre of mass 60 days, lagged | technique | sizing | Simple, no look-ahead | p. 233 |
| 4 | [[Volatility targeting]]: equal weight across available contracts | technique | sizing | Not argued | p. 236 |
| 5 | Average of h overlapping portfolios | technique | rebalancing | No overlapping observations | p. 233 |
| 7 | [[Always-long benchmark comparison]]: always-long on the same contract | technique | evaluation | Return beyond a passive long | p. 236 |
| 8 | [[Squared market return regression]] | technique | evaluation | Straddle-like payoff test | p. 238 |
| 9 | [[Profit decomposition into persistence and mean return]]: auto-covariance, cross-serial, mean | technique | evaluation | Shows where profit comes from | p. 241, 244 |
| 10 | [[Spot and roll return decomposition]]: split futures return into spot change and roll | technique | economic intuition | Separates information from hedging pressure | p. 247 |
| 11 | Net speculator position, (long - short) / open interest | technique | economic intuition | Shows who sits with the trend | p. 231 |

No turnover-reduction technique is given.

## 6. Regime observations

- Losses at crisis turning points, gains while markets keep falling (p. 238).
- No relation with TED spread, VIX or sentiment (Table 3C).

## 7. Acknowledged limits

- CFTC classification is noisy. Positions cover only US stock and bond futures (p. 231, fn. 6).
- Results shown from 1985 only. Earlier contracts are fewer and less liquid (p. 236).
- Illiquidity measured on one June 2010 volume snapshot (p. 239).
- Roll return and positions are imperfect proxies of hedging pressure (p. 248).

## 8. Not addressed

- Costs, turnover, slippage, capacity.
- Drawdowns. Exact portfolio Sharpe ratio and its sample.
- Out-of-sample choice of 12 / 1: grid and chosen cell share the 1985-2009 sample.
- Data after 2009. Roll schedule and execution timing.
- Results split by data type: bond, equity and currency histories before futures use index and spot data.
- Per-contract figures as numbers. Only Fig. 2 shows them.
