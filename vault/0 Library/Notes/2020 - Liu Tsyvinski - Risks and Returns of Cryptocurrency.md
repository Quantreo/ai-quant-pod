---
type: reading-note
source: paper
title: Risks and Returns of Cryptocurrency
authors: Liu, Tsyvinski
affiliations: Yale University, Department of Economics; Tsyvinski also NBER
year: 2018
venue: NBER Working Paper 24877, August 2018
doi:
pdf: "[[2020 - Liu Tsyvinski - Risks and Returns of Cryptocurrency.pdf]]"
version: working paper (NBER, not peer-reviewed, p. 1)
tier: 1
read: full
tags: [trend, crypto, weekly]
date: 2026-10-24
---

# Risks and returns of crypto (Liu, Tsyvinski 2018)

## Summary

- **Finding**: Bitcoin, Ripple and Ethereum returns show no robust exposure to stock, currency, commodity or macro factors. Their own past return and Google or Twitter attention predict returns at 1 to 4 weeks (Tables 14-29). Gross.
- **Mechanism**: Not stated by the authors. They only conclude that crypto is not priced like stocks, currencies or precious metals.
- **Where it works best**: Bitcoin weekly returns. Top return quintile earns 11.22% the next week, Sharpe 0.45; top Google-attention quintile 11.20%, Sharpe 0.48 (Tables 15, 20).
- **Weak spots**: Ethereum momentum is weaker (negative at 5 days); price-to-"dividend", volatility and mining-supply proxies do not predict. Day-of-week and sub-period effects are small or shaky.
- **Main caveats**: 2011 to May 2018 only, huge returns (21.6% monthly mean), t-statistics for the daily and weekly regressions fall when bootstrapped; no costs, no trading rule tested.

Page numbers follow the printed pagination, which is the PDF page minus 1 from the first text page. Appendix pages restart at 1. Values marked ≈ are read from a chart (none used).

## 1. Mechanism (authors' claim)

Not stated by the authors. The paper tests exposures and predictors, and offers no explanation for momentum or attention effects.

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Crypto risk and return are distinct from stocks, currencies and precious metals | CAPM alpha 18.91% a month (Bitcoin); loadings on five currencies, gold, platinum and macro factors mostly insignificant | p. 9-19, Tables 5-13 |
| 2 | Only crypto-specific factors explain returns: momentum and attention | Predictive regressions and quintile sorts | p. 20-28 |
| 3 | Supply factors, price-to-"dividend" and volatility do not forecast | Tables 30-32; the exceptions are Ripple volatility at 4, 5, 7 days and Ethereum on AMD stock returns | p. 29-31 |

**Caveats raised by the authors**
- Bitcoin data start in 2011 because earlier years had little liquidity (p. 4).
- The 155-anomaly data end in 2016, so they are used for Bitcoin only (p. 18).
- Wallet users stand in for fundamental value; no data for Ripple and Ethereum (p. 3, 29).

**Ruled out**
- Currency, precious metal and macro exposures as sources of crypto returns (p. 13-18).
- Supply cost proxies and market volatility as predictors for Bitcoin (p. 29-31).

## 2. Strategy, brick by brick

No trading strategy is built. The predictors are tested in regressions and in quintile sorts of their own history.

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | Bitcoin from 1 Jan 2011, Ripple from 4 Aug 2013, Ethereum from 7 Aug 2015, all to 31 May 2018. CoinDesk prices. | p. 4 |
| Period | 2011 to May 2018, by coin as above. | p. 4 |
| Signal | Momentum: current daily or weekly return. Attention: Google search count for the coin name minus the average of the preceding four weeks, normalised. Twitter count the same. Negative attention: Google "Bitcoin hack" over "Bitcoin". | p. 20-28 |
| Entry | Quintiles of the signal over the sample; average next-period return per quintile. | Tables 15, 20 |
| Exit | Return over 1 to 4 weeks ahead (or 1 to 7 days). | Tables 14-31 |
| Horizon | Daily and weekly returns, measured from 11:59:59 UTC. | p. 20 |
| Sizing | Not stated by the authors. | |
| Portfolio | One coin at a time. | |
| Rebalancing | Not stated by the authors. | |
| Costs | Not addressed. | |
| Data and tools | CoinDesk; Google, Crimson Hexagon (Twitter); blockchain.info; CRSP, Fama-French, St. Louis Fed, Case-Shiller. | p. 4-5 |

**Rule** (p. 20): regress the return h periods ahead on the current return, `R(t+h) = a + b·R(t)`, for h = 1 to 7 days or 1 to 4 weeks. The one-day-ahead return is bought at 11:59:59 UTC today and sold at 11:59:59 UTC the next day.

**Data provenance**
- Two t-statistics are reported: regular errors in parentheses, bootstrapped errors in brackets (p. 9).
- The 1 to 4 week quintile tables also appear since 2013 (Table 16) and with cutoffs fixed on the first two years only (Table 17).

## 3. Results

All results use real data, in-sample unless stated, gross of costs.

**Aggregate** (Table 1, Bitcoin 2011 to Apr 2018)
- Mean return 0.52% a day, 3.79% a week, 21.60% a month. Standard deviation 5.55%, 16.64%, 69.46%. Sharpe 0.09, 0.23, 0.31 (p. 6-7).
- Daily skewness 0.80, kurtosis 15.21. Daily returns above 20% occur 0.95% of days, below -20% 0.48% (Table 1B).

**By sub-group**
- Momentum, daily (Table 14): coefficient 0.06 on next day (t = 2.96, bootstrap 1.22); significant at 1, 3, 5 and 6 days.
- Momentum, weekly (Tables 14-15): coefficients 0.19, 0.22, 0.21, 0.09 at 1 to 4 weeks. Top quintile next week 11.22%, bottom 2.60%.
- Ripple, daily momentum significant at 1 to 5 days; Ethereum at 1 day (0.08) and at 5 days (-0.08) (Table 18).
- Google attention, Bitcoin weekly: 1.84 at one week (t = 2.17), 2.30 at two weeks (t = 2.81); Ripple 10.86 at one week; Ethereum 4.36, 3.45, 3.65 at 1, 3 and 6 weeks (Tables 19, 23, 24).
- Twitter, Bitcoin: 2.50 at one week (Table 26). Hack ratio: -2.75 at one week (Table 28).

**Horizon and parameters**
- Quintile spread, top minus bottom, next 1, 2, 3, 4 weeks: momentum 8.62, 11.28, 10.57, 5.18 (Table 15). Google 10.13, 8.66, 6.82, 2.89 (Table 20).
- Since 2013 the momentum spread is smaller: 4.35, 7.87, 6.09, 3.03 (Table 16).
- With cutoffs from the first two years: momentum spread 4.53, 8.23, 6.16, 2.42 (Table 17). Google 7.39, 6.94, 5.72, 4.49 (Table 22).

**Over time**
- Not addressed beyond the since-2013 and no-lookahead cuts.

**Link to other strategies**
- Unconditional alpha of Bitcoin 22.45% a month. CAPM alpha 18.91%; CAPM beta 3.34, not significant (p. 9). Alpha 38.15% a month for Ripple, 32.87% for Ethereum (p. 10, 12).
- Fama-French 5-factor loadings low; HML negative for Ripple and Ethereum (p. 9-13). Only four of 155 stock anomalies are significant for Bitcoin, with no pattern (p. 18).
- Black-Litterman with a view that Bitcoin beats the other assets by 30%, 50%, 100% or 200% a year gives Bitcoin weights of 1%, 1.6%, 3.1%, 6.1% (App. C, Table A.8).

**Inconsistencies in the source**
- p. 9 compares the Ethereum Saturday Sharpe of 0.03 with a daily average Sharpe of "0.03". Table 3 gives 0.11.
- Table 24 Panel B shows -2.22 with t = -2.29 at week 7 without significance stars. The same size elsewhere carries stars.
- Bootstrapped t-statistics are much lower than regular ones for daily momentum: 1.22 against 2.96 at one day (Table 14). The text reports the effect as "very strong".

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Findings cast doubt on the stake-in-technology, unit-of-account and store-of-value explanations | p. 39; only exposures were tested |
| Supply factors matter more in recent periods: no support | p. 31; results in an appendix not reproduced here |
| The index of industry exposures shows potential winners and losers of blockchain | p. 37-38; no out-of-sample test |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | Next-period return regressed on the current return; quintile sort of weekly returns into the next 1 to 4 weeks | technique | signal | Time-series momentum, after Moskowitz (p. 4). Card [[Time-series momentum signal]] | p. 20-23 |
| 2 | Attention signal: Google or Twitter count minus its previous four-week average, normalised | technique | signal | Attention predicts returns, after Da, Engelberg, Gao (p. 4). Card [[Search attention signal]] | p. 23-27 |
| 3 | Negative attention ratio: "Bitcoin hack" over "Bitcoin" searches | technique | signal | Negative attention. Card [[Search attention signal]] | p. 28 |
| 4 | Quintile cutoffs from the first two years, then forward | technique | evaluation | No lookahead. No card: standard practice | p. 22 |
| 5 | Factor loadings on stock, currency, commodity and macro factors | technique | evaluation | Compare with other asset classes. No card: standard practice | p. 10-19 |
| 6 | Price over wallet users as a price-to-"dividend" ratio | technique | signal | Gap to fundamental value. No card: no predictive power found | p. 29 |
| 7 | Industry exposure index: industry return on Bitcoin return, controlling for the market | technique | evaluation | Winners and losers. No card: standard regression | p. 38 |
| 8 | Black-Litterman allocation to Bitcoin under stated views | technique | sizing | How much to hold. No card: standard model with assumed views | App. C |

## 6. Regime observations

- Momentum effects are smaller since 2013 (Table 16).
- Day of week: Saturday returns are lower for all three coins; no Monday effect (p. 9, Table 4).
- Implied one-day disaster probability from the return level: 0 to 1.3% for Bitcoin (App. B).

## 7. Acknowledged limits

- Data are short and start when the market was illiquid (p. 4).
- Currency and commodity series for the shorter coin samples differ from the full Bitcoin sample, so Bitcoin is also shown over matched periods (p. 13, 18).

## 8. Not addressed

- Transaction costs, slippage, shorting and funding in crypto.
- A trading rule built from momentum or attention, with sizing and exit.
- Long-short or cross-sectional crypto sorts.
- Results on more coins or after 2018.
- A model explaining why attention and momentum predict returns.
