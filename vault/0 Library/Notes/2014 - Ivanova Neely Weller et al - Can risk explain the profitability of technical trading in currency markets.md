---
type: reading-note
source: paper
title: Can risk explain the profitability of technical trading in currency markets?
authors: Ivanova, Neely, Weller, Famiglietti
affiliations: Ivanova (Promontory Financial Group), Neely and Famiglietti (Federal Reserve Bank of St. Louis), Weller (University of Iowa)
year: 2014
venue: Federal Reserve Bank of St. Louis Working Paper 2014-033I, revision of September 2020
doi: 10.20955/wp.2014.033
pdf: "[[2014 - Ivanova Neely Weller et al - Can risk explain the profitability of technical trading in currency markets.pdf]]"
version: working paper (2020 revision of a 2014 paper)
tier: 1
read: full
tags: [trend, fx, daily]
date: 2026-10-25
---

# Technical trading and risk in FX (Ivanova, Neely, Weller 2014)

## Summary

- **Finding**: ex ante top-ranked FX rule portfolios earn 4.41% a year (Sharpe 0.81), 1976-2012; only the top one stays profitable after about 1993. No risk model explains the returns.
- **Mechanism**: not a risk premium. The authors favour adaptive markets or limits to arbitrage, by elimination, not by test (p. 24, 26).
- **Where it works best**: portfolio p1 (top 25 pairs): USD and cross rates up to the mid 1990s, then Latin American and developing European currencies (Fig. 2, p. 11).
- **Weak spots**: lower-ranked portfolios go flat after about 1993 (Fig. 3). Authors concede VOL and SKEW factors explain up to 10-15% of returns in some variants (fn 20).
- **Main caveats**: costs are modelled but the net basis is not stated; rules and universe fixed by prior literature; sample ends 2012; no turnover or drawdown figures.

Page numbers follow the working paper pagination printed on the page (PDF page minus 2). Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Technical returns are not compensation for the risks tested | Every risk model fails: wrong-signed betas or prices of risk, negative cross-sectional R2 without a constant, constants as large as mean returns | Tables 3-7; p. 16-25 |
| 2 | Adaptive markets: profits fade as rules become known; less studied rules and emerging currencies still pay | Lower-ranked portfolios flat after about 1993; p1 and emerging currencies keep earning | Fig. 3; p. 12; cited from Neely 2009 |
| 3 | Limits to arbitrage as an alternative | Named only | p. 3, 26 |

Claims 2 and 3 are put as consistent with the failure of risk models. The paper does not test them.

**Caveats raised by the authors**
- The test is joint: an apparent inefficiency may come from a misspecified risk model (p. 1).
- The post-1993 decline is a separate question from whether risk explains the returns that existed before and after (p. 13).
- VOL1 and VOL2 explain 10-15% of returns for USD-only and G10-only portfolios; SKEW similar for baseline, return-sorted and Sortino-sorted variants (fn 20, p. 26).

**Ruled out**
- Central bank intervention as source, by Neely (2002), cited (p. 25).
- Data snooping, data mining and publication bias, by Neely, Weller and Ulrich (2009), cited (p. 25).
- Consumption risk, market risk, size, value, momentum, carry, dollar, volatility, skewness, unemployment skewness and FX liquidity as full explanations (Tables 4-7).

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | 21 USD rates and 19 cross rates, 24 to 40 available over time. Pairs enter when tradable (capital-control dates for 8 currencies). | Table 1; p. 4, 7 |
| Period | April 1973 to December 2012. First eligible trading date 7 April 1976. | p. 6, fn 8 |
| Signal | 16 rules per rate: 7 filters, 3 moving averages, 3 momentum, 3 channels. Long or short the foreign currency. | p. 4-5 |
| Selection | Every 20 business days, rank all rule-rate pairs by Sharpe ratio over the whole prior sample (at least 250 days). | p. 8-9 |
| Portfolio | Top 300 pairs form 12 equal-weight portfolios of 25 (p1 = ranks 1-25). | p. 10 |
| Horizon | Rules signal daily, so positions flip day by day. Pairs are swapped every 20 days. | p. 9 |
| Sizing | Equal weight within a portfolio. Leverage not stated. | p. 10 |
| Costs | One-way 5 bp (1970s), 4 bp (1980s), 3 bp (1990s) for advanced currencies; one third of average quoted spread for others; minimum 1 bp. | p. 7-8 |
| Data | Haver daily rates (mostly Fed H.10, noon New York), BIS overnight rates. | p. 7 |

**Rule**

Filter (Eq. 1): z = +1 if S(t) is at least n(t)(1+y), -1 if S(t) is at most x(t)(1-y), else z(t-1), with n and x the latest local minimum and maximum. y in {0.005, 0.01, 0.02, 0.03, 0.04, 0.05, 0.1}.
Channel (Eq. 2): +1 if S(t) is at least max of the previous n closes times (1+x), -1 if at most the min times (1-x); n in {5, 10, 20}, x = 0.001.
Moving average MA(S, L): MA(1,5), MA(5,20), MA(1,200). Momentum: sign of the n-day return, n in {5, 20, 60} (p. 5).
Daily log excess return (Eq. 4): ln S(t+1) - ln S(t) + (dt/365)[ln(1+i*) - ln(1+i)], times z. Round trip with cost c: sum of excess returns + ln(1 - c) - ln(1 + c) (Eq. 5, p. 6).

**Data provenance**
- Cross rates are built from dollar rates; cost is the larger of the two dollar costs (p. 8).
- Deliverable forwards exist for all but Russia, Brazil, Peru, Chile and Taiwan, which use non-deliverable forwards (p. 8).
- Japan's rate is spliced from three series. DEM spliced with EUR after 1 January 1999 (p. 6-7).
- Trading is restricted before: ZAR 1995, BRL 1999, MXN 1996, NZD 1987, TRY 2002, PEN 1996, ILS 1995, TWD 1998 (p. 7).
- Risk factors need non-FX data: consumption (annual 1978-2010), Carhart factors, Lustig et al. factors, unemployment gaps, Karnaukh et al. liquidity (Tables 3-7).

## 3. Results

All real data, in-sample for the sort ranks, ex ante for the rule selection. Net or gross is not stated for the portfolio returns.

**Aggregate**
- p1 mean excess return 4.41% a year, Sharpe 0.81; p12 0.69% a year, Sharpe 0.17 (p. 10, Fig. 1).
- All 12 portfolios have positive mean excess returns (p. 10).
- Exchange rate component gives almost all the expected return, not the interest differential (fn 12).
- Monthly mean excess return p1 0.37%, p12 0.06% (Table 4).
- An optimal trader would hold only N* = 18 or 19 top strategies (p. 13).

**By sub-group**
- Rules: channel rules dominate the top portfolio over the whole sample; momentum and MA rise after 1985 (p. 11, Fig. 2).
- Currencies: advanced only until the mid 1990s, Latin America prominent from the late 1990s, developing Europe most recently (p. 11).
- Most used pair in p1: CLP channel(20), 14.7% of the time, 38.8% in 2003-2012 (Table 2).
- Best single rules by Sharpe: RUB filter 0.005, Sharpe 1.19, mean 9.40% a year, 2000-2012; RUB MA(1,5) 0.93; CLP channel(5) 0.88 (Table 2).

**Horizon and parameters**
- Sorting by Sharpe, Sortino or mean return, 250-day instead of 20-day re-sort, USD-only or G10-only rates: inference "very similar"; detail in online appendices, not seen (fn 10, p. 25).
- Costs 25% or 50% higher: "results were similar" (fn 7).

**Over time**
- Return drop-off after the early 1990s in most portfolios; p1 still rising to 2012 at ≈155% cumulative, p2 ≈100%, p3 ≈75% (≈ Fig. 3).
- Portfolios 4-12 end between ≈25% and ≈75%, mostly flat since about 1994 (≈ Fig. 3).
- No visible fall in the crises of 1994-95, 1997-98, 2007-08; a small upward spike in 2008-2009 (p. 13, Fig. 3).

**Risk-model tests** (p1-p12 as test assets; none explains the returns)
- CAPM: betas about -0.04, mostly significant and negative; constant 0.40 for p1 against mean 0.37 (Table 4).
- Quadratic CAPM: price of squared-market risk 0.17 (t = 1.68), wrong sign; R2 without constant -0.13 (Table 4).
- Downside risk CAPM: betas significant, wrong sign; price of downside risk -3.35, t = -0.86 (Table 4).
- Carhart 4 factors: constant 0.41 for p1; implied prices of risk differ from factor means 0.58, 0.24, 0.29, 0.68% a month (p. 18, Table 4).
- C-CAPM, D-CAPM: second-stage R2 -1.23 and -0.49; EZ-DCAPM R2 0.60, price of nondurable risk -2.32, risk aversion negative (Table 5, p. 20).
- Calibrated models (Yogo values): R2 from -1.54 to -0.15 (Table 3).
- Lustig factors RX and HML(FX): HML betas negative; R2 -0.27 without constant (Table 6).
- Volatility factors: betas positive and significant, no pattern across portfolios; R2 -0.11 without constant (Table 6).
- Skewness factor: betas all about 0.07-0.11, not different from each other; constants within about 10% of means per authors (p. 23, Table 6).
- Unemployment-gap skewness: no significant beta; R2 -2.44 without constant (Table 7).
- FX liquidity: p1 and p12 significant at 10%; price significant only with a constant (Table 7).

**Link to other strategies**
- Monthly returns of Menkhoff et al. (2012) cross-sectional momentum rules: correlation with these portfolios as low as 0, median 0.13 (fn 3).

**Where it does not work**
- Lower-ranked portfolios p4-p12 have Sharpe 0.14 to 0.50 and flat cumulative returns after about 1994 (Fig. 1, 3).

**Inconsistencies in the source**
- Text says Sharpe ranges from 0.81 (p1) to 0.17 (p12), p. 10; Fig. 1 shows p6 at 0.14.
- Text says skewness constants are within 10% of mean returns (p. 23); Table 6 shows p2 constant 0.20 against mean 0.15 and p5 0.16 against 0.10.
- Fig. 3 note says 1977 to 2012; axes start 1976 and the first eligible date is April 1976 (p. 8, p. 41).

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Reasonable variations of rule selection "unlikely to substantially change inference" | p. 4 |
| Results similar with Sortino, mean-return sort, 250-day re-sort, USD-only, G10-only; appendices C and D | fn 10, p. 25 |
| Results similar with 25% and 50% higher costs | fn 7 |
| Quoted Bloomberg spreads overstate those traders get, per a commercial bank | p. 7 |
| Reduced profitability of low-ranked strategies is irrelevant as the trader uses N* = 18 or 19; the N* optimisation is not shown | p. 13 |
| Channel, ARIMA, genetic programming and Markov rules probably still earn returns (cited from Neely 2009) | p. 12 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | [[Filter rule]] | technique | signal | Studied in the academic literature | p. 4-5, Eq. 1 |
| 2 | [[Channel breakout]] | technique | signal | Studied in the academic literature | p. 5, Eq. 2 |
| 3 | [[Time-series momentum signal|Moving average crossover MA(S, L)]] | technique | signal | Studied in the academic literature | p. 5 |
| 4 | [[Time-series momentum signal|Sign of n-day return, n = 5, 20, 60]] | technique | signal | Studied in the academic literature | p. 5 |
| 5 | [[Trailing Sharpe rule selection|Re-rank rule-rate pairs every 20 days by past Sharpe; trade the top 25 equal weight]] | technique | signal | Mimics a trader who backtests, avoids data mining | p. 8-10 |
| 6 | [[Trailing Sharpe rule selection|Sort by Sharpe, not return]] | technique | signal | Removes the leverage illusion: a more volatile rate gives a larger return to the same rule | fn 9 |
| 7 | Twelve rank-bucket portfolios as test assets | technique | evaluation | Customary in asset pricing | p. 9-10 |
| 8 | Fama-MacBeth and GMM risk-price tests, with and without a constant | technique | evaluation | Joint test of efficiency and a risk model | p. 16-17 |
| 9 | [[Squared market return regression|Quadratic CAPM (squared market return)]] | technique | evaluation | Tests a straddle-like exposure | p. 17, Eq. 16 |
| 10 | [[Downside beta regression|Downside risk CAPM, threshold one standard deviation below the mean]] | technique | evaluation | Price of risk depends on the market state | p. 18, Eq. 17 |
| 11 | Transaction cost schedule by decade and currency, one third of quoted spread | technique | evaluation | Quoted spreads overstate what traders pay, per a bank consultation | p. 7-8 |

No card: #7 (standard sorted-portfolio practice), #8 (needs factor data the desk does not hold), #11 (data plumbing). Table links: #3-4 file under Time-series momentum signal.

## 6. Regime observations

- Emerging-market currencies enter the top portfolio only after capital controls ease, early 1990s (p. 11).
- Developing-European rates become more common in p1 most recently (p. 11).
- Technical returns tend to be high when carry returns are low (negative HML(FX) betas, p. 22).

## 7. Acknowledged limits

- Rule selection is by Sharpe over the whole past sample, with a 1020-day start window (fn 8).
- Betas on market factors are not identified: equality of betas cannot be rejected (p. 18).

## 8. Not addressed

- Whether reported returns are net of the stated costs.
- Turnover, number of trades, drawdowns.
- Position size, leverage and capacity.
- Data after 2012.
- Break-even costs.
