---
type: reading-note
source: paper
title: Factor Timing
authors: Haddad, Kozak, Santosh
affiliations: Haddad (UCLA Anderson and NBER), Kozak and Santosh (University of Maryland)
year: 2020
venue: NBER Working Paper 26708, January 2020
doi:
pdf: "[[2020 - Haddad Kozak Santosh - Factor Timing.pdf]]"
version: working paper (NBER, not peer-reviewed, p. 1)
tier: 1
read: full
tags: [value, equities, monthly]
date: 2026-10-24
---

# Factor timing (Haddad, Kozak, Santosh 2020)

## Summary

- **Finding**: on 50 US stock anomalies, 1974-2017, the first and fourth principal components are predicted by their own book-to-market spread: out-of-sample monthly R² 4.82% and 3.52%. Pure anomaly timing: Sharpe 0.71 in sample, 0.77 out of sample, gross.
- **Mechanism**: no near-arbitrage means only the largest components can be predictable. Book-to-market stands for expected returns. Not tested beyond forecasts.
- **Where it works best**: PC1 and PC4 (Table 2). By anomaly, long-run reversals R² 5.7% in and 5.5% out; price 4.3 and 3.5; size 3.8 and 4.5 (Table 3).
- **Weak spots**: PC5 is not predictable. Under expanding and rolling windows PC2, PC3, PC5 and the market have negative R² (Table A.1). Sentiment adds only about 0.2% and factor momentum is negative out of sample.
- **Main caveats**: no transaction costs; turnover 41% a month; one split-sample test; one predictor (book-to-market).

Page numbers follow the printed pagination, which is the PDF page minus 1 from the first text page. Appendix pages are A1 onward. Values marked ≈ are read from a chart (none used).

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | The optimal factor timing portfolio equals the stochastic discount factor (SDF) | Derivation under Assumption 1 (SDF loads on a few characteristic factors with time-varying prices of risk) | p. 9-12, App. A |
| 2 | With no near-arbitrage, only the large principal components can be predictable; small ones would imply Sharpe ratios that are too high | Algebra on the Sharpe-ratio identity (Eq. 7); Figure 1 shows only large PCs predictable | p. 12-14, 24 |
| 3 | The book-to-market spread of a portfolio proxies its expected return | Cited: log book-to-market is a discounted sum of future expected returns (Vuolteenaho) | p. 19-20 |
| 4 | Risk-premium variation is multi-dimensional, not one common force | Sentiment predicts little, factor momentum fails, SDF correlations vary | p. 33-34, 47-49 |

**Caveats raised by the authors**
- Other predictors could add predictability; book-to-market is a simple choice (p. 20).
- Transaction costs are needed before calling the strategy implementable (p. 39, A13).
- The relations with macro variables are not causal (p. 46).

**Ruled out**
- Macro predictors (D/P, CAPE, volatility, term premium, credit spread, cay, GDP growth, sentiment) do not drive out book-to-market (Table A.3).
- Stambaugh bias for the PCs: bias is small next to the coefficients (Table 2, A.2).

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | 50 characteristic-sorted long-short stock portfolios (anomalies) from Kozak et al. 2019. CRSP and Compustat, NYSE, AMEX, NASDAQ. | p. 17, Table A.4 |
| Period | Monthly, January 1974 to December 2017. Out of sample: second half. | p. 17, 21 |
| Signal | Five largest PCs of the market-adjusted, rescaled anomaly returns, plus the market. Each PC is forecast by its own log book-to-market spread. | p. 15-20 |
| Entry | Weights on the components: Σ_Z^{-1} E_t[Z]. | Eq. 10-11, p. 15, 37 |
| Exit | Weights reset each month. | p. 35 |
| Horizon | One month. Also 3, 6, 12 months. | Table 4 |
| Sizing | Inverse covariance of the component forecast residuals, homoskedastic. Scale not stated. | p. 35 |
| Portfolio | Market plus five PCs, implicitly trading the 50 anomalies. | p. 36 |
| Rebalancing | Monthly. Quarterly, semi-annual, annual tested. | Table A.5 |
| Costs | None. Monthly turnover 41% (monthly rebalancing). | p. 39, A13 |
| Data and tools | Kozak et al. anomaly portfolios; Newey-West errors; Kelly-Pruitt placebo test. | p. 17, 20-23 |

**Rule** (p. 17-20): for each anomaly, sort stocks into 10 value-weighted portfolios with NYSE breakpoints. The anomaly is decile 10 minus decile 1. Its bm is log book-to-market of decile 10 minus that of decile 1. Subtract β times the market return and β times the market bm. Rescale returns and bm to equal variance. Compute PCs on the first half. Regress each PC's next-month return on its own bm, `PC_i,t+1 = a + b·bm_i,t`, with `bm_i,t = q_i' bm_F,t`.

**Choice of five PCs** (p. 18-19): prior total R² of 75 bp (market, monthly) and a maximum annual squared Sharpe ratio of 1 (8.3% monthly) give at most five PCs.

**Data provenance**
- Betas, variances and eigenvectors are estimated on the first half only (p. 18).

## 3. Results

Real data. Split-sample out of sample unless marked. Gross of costs.

**Aggregate**
- Table 2, own bm on next-month return, coefficient and out-of-sample R² %: market 0.76 and 1.00; PC1 4.32 and 4.82; PC2 1.62 and 0.97; PC3 1.80 and 0.47; PC4 4.86 and 3.52; PC5 1.56 and 0.55.
- Total out-of-sample R² for the 50 anomalies: 0.93% (in sample 1.03%) (p. 25).

**By sub-group**
- Table 3: about half the anomalies have out-of-sample R² above 1%; two are below -1%. Gross profitability -2.2% in and -4.7% out; F-score -0.2% out (Table 3).
- Table 6, Sharpe in sample / out of sample: factor investing 1.27 / 0.76; market timing 1.23 / 0.63; factor timing 1.19 / 0.87; anomaly timing 1.19 / 0.96; pure anomaly timing 0.71 / 0.77.
- Information ratio against the static portfolio, in / out: 0.36 / 0.42 (factor timing), 0.37 / 0.60, 0.35 / 0.59.
- Mean-variance utility (full sample): factor investing 1.66, market timing 1.69, factor timing 2.96, pure anomaly timing 1.26 (Table 6).

**Horizon and parameters**
- Number of PCs 1 to 7: out-of-sample total R² 0.57 (one PC), 0.93 (five), 0.97 (six); the count of significant PCs rises from 1 to 5 (Table 4).
- Holding period 3, 6, 12 months: total out-of-sample R² 2.69, 5.42, 10.05 (Table 4), with PCs estimated on monthly returns.
- Without market adjustment or rescaling: 1.18 to 1.27 (Table 4).
- Alternative forecasting methods (Table 5): 50 anomalies on 50 bm by OLS -133.73%; own bm of each of 50 anomalies 0.50%; ridge 0.01%; Lasso then OLS 0.76%; three-pass filter 0.32%; sentiment 0.17% to 0.19%; factor momentum -0.49% and -0.08%.

**Over time**
- Expanding window out-of-sample R² (Table A.1): PC1 4.43, PC4 2.59; market -0.53, PC2 -0.32, PC3 -0.30, PC5 -1.31. Rolling 240-month: PC1 3.04, PC4 2.47; others negative.
- Slower rebalancing, pure anomaly timing (Table A.5): Sharpe 0.71 (monthly), 0.72, 0.82, 0.79 (annual); turnover 0.41, 0.20, 0.13, 0.08.

**Link to other strategies**
- SDF variance: factor investing 1.67, market timing 1.71, factor timing 2.96 (Table 7).
- Sentiment (Stambaugh): moderate out-of-sample R² (p. 34). Factor momentum (Ehsani, Linnainmaa): not predictive here (p. 34).

**Inconsistencies in the source**
- p. 37 gives out-of-sample Sharpe ratios "between 0.63 and 0.87". Table 6 shows 0.96 for anomaly timing.
- Table 6 expected utility for factor investing and market timing is 1.66 and 1.69. Table 7 variance is 1.67 and 1.71. The text equates the two.
- p. 22 gives bootstrap p-values of 11% and 7% for PC2 and PC3. Table 2 gives 0.10 and 0.07.
- p. 20 says a large valuation spread suggests low future returns. All Table 2 coefficients on own bm are positive.
- p. 45 says the SDF variance is higher after low GDP growth and low sentiment. Table 8 factor timing: GDP -0.37 (t = 1.60), sentiment -0.15 (t = 0.60), both not significant.
- p. 46 gives the average SDF variance as 2.97, elsewhere 2.96.
- The abstract calls the predictability "robust". Table A.1 shows it only for PC1 and PC4 under expanding and rolling windows.

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| SDF variance averages 4.9 in recessions, 2.7 in expansions | p. 44 |
| Same coefficients (-0.33, 0.45) when expected market return is constant | p. 45 |
| GARCH(1,1) volatility forecasts give similar conclusions | A14 |
| Strategies are implementable at annual rebalancing | A13; no cost model |
| The loadings of size and value on the SDF are procyclical, momentum countercyclical | p. 5, 49; chart only |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | Time the five largest PCs of many factors, each forecast by its own book-to-market spread | technique | signal | Dimension reduction under no near-arbitrage. Card [[Factor timing on dominant components]] | p. 15-20 |
| 2 | Choose the number of PCs from prior bounds on total R² and Sharpe | technique | calibration | Economic anchor. Inside card [[Factor timing on dominant components]] | p. 18-19, A3 |
| 3 | Weights Σ^{-1} E_t[Z]; pure anomaly timing with zero average weights | technique | sizing | Mean-variance timing. Card [[Mean-variance weighting]] | p. 36-37 |
| 4 | Placebo AR(1) predictors with the same moments; parametric bootstrap of a restricted VAR(1) | technique | evaluation | Rules out Stambaugh bias. Card [[Placebo predictor R2 test]] | p. 20-23 |
| 5 | Rebalance monthly to annually; turnover and correlation with the monthly version | technique | evaluation | Is the timing fast? Card [[Slower rebalancing test]] | p. 39, A12-A13 |
| 6 | Split sample, expanding and rolling out-of-sample R² | technique | evaluation | No look-ahead. No card: standard practice | p. 21, A3 |
| 7 | Market-adjust and rescale factors using first-half betas | technique | universe | Comparability. Inside card [[Factor timing on dominant components]] | p. 17-18 |
| 8 | Lasso, ridge, three-pass filter comparison | technique | calibration | Alternatives. No card: they did worse | p. 29-30 |

## 6. Regime observations

- Value and size have high correlation with the SDF in recessions, momentum is negative then (p. 49, chart).
- The SDF variance spikes do not coincide with stress in the financial sector (p. 43).
- The first-half and second-half predictive coefficients of PC2 differ (1.37 against 7.68, Table A.1).

## 7. Acknowledged limits

- The method uses only book-to-market; other predictors could add (p. 20).
- Costs are not modelled (p. 39).
- Causal reading of macro relations is not possible (p. 46).

## 8. Not addressed

- Transaction costs and capacity.
- Leverage or volatility scale of the timing portfolio.
- Shorting costs and market impact for the 50 long-short portfolios.
- Sub-period Sharpe ratios of the timing portfolio.
- Data after 2017.
