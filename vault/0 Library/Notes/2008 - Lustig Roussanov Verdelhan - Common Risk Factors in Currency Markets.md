---
type: reading-note
source: paper
title: Common Risk Factors in Currency Markets
authors: Lustig, Roussanov, Verdelhan
affiliations: Lustig (UCLA Anderson, NBER), Roussanov (Wharton, University of Pennsylvania), Verdelhan (Boston University)
year: 2008
venue: NBER Working Paper 14082
doi: not printed in the PDF
pdf: "[[2008 - Lustig Roussanov Verdelhan - Common Risk Factors in Currency Markets.pdf]]"
version: working paper, June 2008, not peer-reviewed
tier: 1
read: full
tags: [carry, fx, monthly]
date: 2026-10-25
---

# Common risk factors in currency markets (Lustig, Roussanov, Verdelhan 2008)

## Summary

- **Finding**: 37 currencies vs USD, 11/1983-03/2008: long the highest forward-discount portfolio, short the lowest, earns 4.83% a year, Sharpe 0.54, net of bid-ask spreads. Gross: 8.83%, Sharpe 0.99.
- **Mechanism (authors)**: carry compensates exposure to one global risk factor, the high-minus-low return. Low-rate currencies hedge it; the model needs them to load more in bad times.
- **Where it works best**: real data, net: 37 currencies, Sharpe 0.54; 15 developed currencies 0.40. Currency momentum 5.42% net, Sharpe 0.50. Expected returns rise in downturns.
- **Weak spots**: costs cut HML from 8.83% to 4.83%. In crisis windows its market beta reaches 1.22, with negative alpha in two of four. Developed-only momentum is about zero net.
- **Main caveats**: one sample, in-sample, no out-of-sample test. Indicative Datastream quotes. The mechanism behind the loadings is left open. The model is tested by simulation only.

Page numbers follow the printed pagination (printed page = PDF page minus 1). Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Currency risk premia come from exposure to one global factor, HML_FX; interest rates measure that exposure | HML_FX and RX price the six portfolios: adjusted R² 69.28, RMSE 0.95%; alphas jointly zero not rejected; HML betas -0.39 to 0.61 | Table 3; p. 12-13 |
| 2 | Low-rate currencies hedge, high-rate currencies depreciate when carry returns are low | Spot-change betas on HML_FX mirror the return betas, 0.37 (P1) to -0.62 (P6) | Table 4; p. 14 |
| 3 | Sorting on beta to HML_FX gives the same pattern, so rates are not just a characteristic | Beta-sorted gross excess returns 0.66% to 3.32%; post-formation betas -0.31 to 0.28 | Table 6; p. 15 |
| 4 | Expected excess returns are counter-cyclical and rise with global risk | Corr with VIX -0.17 (P1) to 0.52 (P6); with payroll growth 0.02 (P1) to -0.70 (P2) | Table 9; p. 25-26 |
| 5 | The market risk of carry is large in crises, small on average | Carry CAPM beta 0.37 to 1.22 in three crisis windows, 0.62 before 8/2007 | Table 11; p. 27-29 |
| 6 | Risk, not a characteristic: the carry factor prices momentum portfolios sorted on past returns | Two factors, momentum test assets only: adjusted R² 50.98 | Table 15; p. 32-35 |
| 7 | Model: two-factor affine SDF, common global shock; low-rate currencies must load more on it when its price is high | Calibration gives HML 5.05% a year, Sharpe 0.44 (simulation) | p. 16-21; Table 13 |

**Caveats raised by the authors**
- The CAPM does not explain it: estimated market risk price 37% vs a 7.1% market premium, about 5 times too large (p. 27).
- Heterogeneity in loadings may come from risk aversion differences across investors or from goods-market integration. Left open (p. 35-36).
- The simulated stock market has too little volatility and a low equity premium (p. 31-32).
- Bid-ask spreads are charged every month: "conservative" (p. 9). Reuters spreads are about twice inter-dealer spreads (p. 7).

**Ruled out**
- Bid-ask spreads as the cause of the UIP failure (p. 10).
- Country-specific loadings as the source of cross-sectional premia (p. 5, 18).
- A characteristic-only explanation, per the momentum test (p. 35).

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | 37 currencies vs USD, some pegged and kept. Turkey and UAE dropped (forwards disconnected from spot). Robustness set: 15 developed. | p. 7-8 |
| Period | End-of-month series 11/1983-03/2008. | p. 7 |
| Signal | Forward discount f - s at the end of the month, equal to the interest differential under covered parity. | p. 2, 7-8 |
| Portfolios | Six, rank 1 lowest to 6 highest rate. Developed set: five (Tables 1, 2, 6). | p. 8 |
| Entry | Buy or sell one-month forwards at month end; unwind at next month's spot. | p. 6-7 |
| Exit | One month later; portfolios rebalanced monthly. | p. 8 |
| Sizing | Equal weight within a portfolio. No volatility scaling. | p. 8 |
| Portfolio | Zero cost: portfolio 6 minus portfolio 1 (HML_FX). RX: average over all foreign currencies. 9 currencies in 1983, 26 in 2008, maximum 34. | p. 8, 17 |
| Turnover | 6.01 switches a month, 29.32% of currencies; P1 19.9%, P6 13.4%, P4 43.4%. | p. 8 |
| Costs | Bid and ask quotes on spot and forward, every month, on all legs. | p. 7-8 |

**Rule** (p. 6-8), log excess return per currency, then averaged by portfolio:

$$rx_{t+1} = f_t - s_{t+1}, \qquad HML_{FX} = rx^{6}_{t+1} - rx^{1}_{t+1}$$

Net, long foreign: f^b_t - s^a_{t+1}. Net, short foreign: -f^a_t + s^b_{t+1}. For net returns, all foreign currencies of portfolio 1 are shorted, all others long (p. 7-8). Only currencies with spot and forward in the current and the next period enter (p. 8).

**Data provenance**
- Spot and forward, bid and ask: Barclays and Reuters via Datastream (p. 7).
- Business cycle and risk series: IMF IFS industrial production, BEA payroll, Conference Board Help Wanted, Fama-Bliss yields (CRSP), VIX and bond yields from Global Financial Data (fn 6, p. 25). VIX starts 2/1990 (fn 7).
- Market: CRSP value-weighted; Fama-French monthly excess return for the equity benchmark (p. 9, 27).
- Portfolio data on the authors' website; extra results in an online appendix, not in the PDF (p. 6).

## 3. Results

Real data, in-sample, annualised log excess returns, 11/1983-03/2008. Net means with bid-ask.

**Aggregate**

| Metric | Value | Where |
| --- | --- | --- |
| HML net, 37 currencies | 4.83%, Sharpe 0.54 (gross 8.83%, 0.99) | Table 1 |
| HML net, developed | 3.46%, Sharpe 0.40 | Table 1 |
| P1 net (short) / P6 net | -1.70% (SR -0.21) / 3.14% (SR 0.34) | Table 1; p. 9 |
| US equity market, no costs | 7.11%, Sharpe 0.48 | p. 9 |
| Spot depreciation vs forward discount | P1: discount -3.90, spot change -0.97; P6: 7.78 and 1.88 | Table 1 |
| Principal components | PC1 70.07% of variance (level), PC2 12.25% (slope) | Table 2 |
| Price of HML risk | 5.46% (GMM SE 2.34, FMB 1.83); sample mean 5.37 | Table 3 |

**By sub-group**
- Net HML by long portfolio j vs P1: 0.75% (P2, SR 0.14) to 4.83% (P6); best Sharpe 0.60 at P4 (Table 1).
- Portfolio 4 alpha 1.62%, significant at 10% only (Table 3; p. 13).
- Developed sample: price of HML risk 3.56%, adjusted R² 71.06 (Table 3); results said to be comparable (p. 13).
- Momentum net: P1 -1.98 (short), P6 3.44; HML 5.42%, SR 0.50 (gross 9.32%, 0.86). Developed: spreads -1.76 to 1.49, SR -0.25 to 0.18 (Table 14).
- Foreign investors (UK, Japan, Switzerland): HML risk price 5.50% to 5.79% (p. 16).

**Horizon and parameters**
- One-month return on the own forward discount: R² 1.61% (P3) to 5.98% (P4). On the average forward discount: 2.68% to 7.85% (Table 7).
- Twelve months, average forward discount: R² 17.54% (P6) to 32.57% (P1), overlapping data (Table 8).
- Residual predictability after the average: at most 1.18% (Table 8).
- Beta sort window 36 months; 12 months gives a spread of about 300 bp (p. 15, not shown).

**Over time**
- Rolling 12-month carry beta to the US market ≈ -0.5 (1993) to ≈ 0.6 (1998, 2007-08); P6 minus P1 correlation spread ≈ -0.4 to ≈ 1.0 (Fig. 5).
- Fig. 3: expected return on P2 ≈ -15% to ≈ 8%, moving against US industrial production.
- Crisis windows of six months, HML market beta and alpha (alpha over six months): LTCM 1.11, -2.71; Tequila 1.22, -3.82; Brazil/Argentina 0.37, +0.96; subprime 0.62, +0.29 (Table 11).
- Fig. 4: HML and MSCI correlation 0.78; at the end of the plotted window HML ≈ -0.15 vs MSCI ≈ -0.33.

**Link to other strategies**
- Carry factor prices 12 carry and momentum portfolios: adjusted R² 83.23, RMSE 0.70% with a momentum factor; 68.13 and 1.02% without (Table 15).
- Carry risk price 9.96% to 10.05% whatever the test assets (Table 15).
- Third principal component of the 12 portfolios correlates 0.75 with HML_FX (p. 33-34).
- Momentum portfolios: interest spread between P1 and P6 under 300 bp, against over 11 points for carry (p. 33).

**Inconsistencies in the source**
- Sort date: p. 8 says forward discounts at the end of period t; the Table 1 note says end of period t-1.
- Developed HML Sharpe 0.39 in text (p. 10), 0.40 in Table 1.
- Table 7: R² range 1.61 to 5.98, text says 1.8 to 6.4; slopes 3.47 and 0.71, text says 357 and 72 bp (p. 22).
- Post-formation betas -0.31 to 0.28 in Table 6; text says 0.38 (p. 15).
- Table 11 note says portfolios are sorted on past excess return; the text says forward discounts. Russian default HML beta 1.11 in table, 1.14 in text (that is P6) (p. 28).
- Fig. 4 caption: 07/02/07 to 03/31/08; chart title and axis run to 10/2008. Text names the US stock market; legend says MSCI (p. 27, 59).
- Unconditional alpha of HML: "more than 500 bp" (p. 28) and "4.46 percent" (p. 29).
- Principal-component weights called zero cost sum to -0.10 (computed, p. 14). The p. 34 text says RMSE "1.02 basis points"; Table 15 gives 1.02 in percent.

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Similar results in the Burnside et al. sample, in sub-samples from 1983 and 1995, and with the Treasury-bill sample; HML correlation above .95 across base currencies | p. 15-16 |
| Business-cycle results "very similar" with real-time vintage data | p. 25 |
| CAPM alphas jointly zero rejected at 5% ("available upon request") | p. 27, fn 8 |
| Carry-momentum return correlations small, sometimes negative | p. 33 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | Six portfolios on forward discount, long top, short bottom, monthly ([[Carry signal]]) | technique | signal | Easy to trade in forwards, spreads available, low counterparty risk | p. 2, 6-8 |
| 2 | Equal-weight portfolios, average of currency excess returns ([[Long-short portfolio weighting]]) | technique | sizing | Not argued | p. 8 |
| 3 | Average forward discount across portfolios as one forecaster of all returns ([[Carry signal]]) | technique | signal | Drops country-specific inflation (p. 24) | p. 22-24 |
| 4 | Sort on 36-month rolling beta to the carry factor ([[Factor beta sort]]) | technique | signal | Shows rates measure risk exposure | p. 15 |
| 5 | Six portfolios on past return, same machinery ([[Cross-sectional momentum]]) | technique | signal | Tests risk vs characteristic | p. 32-33 |
| 6 | Price portfolios sorted on one variable with the factor built from another sort ([[Cross-sort factor pricing test]]) | technique | evaluation | Same test | p. 33-35 |
| 7 | Rolling 12-month correlation spread, and 6-month pre-crisis regression on the market ([[Crisis-window market beta]]) | technique | evaluation | Shows carry beta moves with global risk | p. 27-29 |
| 8 | Net return with bid on the way in and ask on the way out | technique | evaluation | Real costs | p. 7 |
| 9 | Principal components of portfolio returns as level and slope factors | technique | evaluation | Not argued | p. 10-11 |
| 10 | Cross-sectional factor pricing, GMM and Fama-MacBeth, no constant | technique | evaluation | Not argued | p. 11-13 |

## 6. Regime observations

- Expected returns on medium and high-rate portfolios are counter-cyclical with US industrial production and payroll (p. 25-26).
- Carry beta to the stock market and the correlation spread jump 0.5 to 0.9 in crises (p. 28).
- Low-rate currencies earn a lower premium when VIX is high (p. 26).

## 7. Acknowledged limits

- Spreads are charged on every rebalance, so net estimates are "conservative" (p. 9).
- Pegged currencies kept because forwards were accessible (p. 7).
- The model does not specify preferences or technologies (p. 16).

## 8. Not addressed

- Out-of-sample or post-2008 results.
- Capacity, slippage beyond quoted spreads, funding or margin.
- Drawdowns and skewness of HML_FX.
- Volatility scaling and leverage.
- Which currencies sit in each portfolio over time (only the yen is described, p. 8).
