---
type: reading-note
source: paper
title: Tail Risk in Momentum Strategy Returns
authors: Daniel, Jagannathan, Kim
affiliations: Daniel (Columbia Graduate School of Business, NBER), Jagannathan (Kellogg School of Management, Northwestern University, NBER), Kim (Kellogg School of Management, Northwestern University)
year: 2012
venue: NBER Working Paper 18169 (http://www.nber.org/papers/w18169)
doi: not printed in the PDF
pdf: "[[2012 - Daniel Jagannathan Kim - Tail Risk in Momentum Strategy Returns.pdf]]"
version: NBER working paper, June 2012, revised February 2017, not peer-reviewed (cover). First titled "Risky Cycles in Momentum Returns".
tier: 1
read: full
tags: [trend, equities, monthly]
date: 2026-10-23
---

# Tail risk in momentum (Daniel, Jagannathan, Kim 2012)

## Summary

- **Finding**: a two-state hidden Markov model flags a "turbulent" state; all 13 US momentum losses worse than -20% (1927-2013) came with turbulent probability above 80%.
- **Mechanism**: after market falls, past losers become highly levered (financial and operating), so their equity behaves like a call on the market. Momentum, short the losers, is short that call.
- **Where it works best**: at the -20% crash threshold, 114 false positives vs 147 to 256 for volatility measures. Value hedges momentum only in high-probability months (correlation -0.57 vs -0.07).
- **Weak spots**: momentum alpha on the Hou et al. four-factor model 0.39% a month (t = 1.07). At the -10% threshold the HMM has more false positives than several market-volatility measures.
- **Main caveats**: crash counts, tertiles and the value hedge use full-sample estimates; only one chart is out-of-sample. Gross, no costs or turnover. US equities only.

Page numbers follow the paper's own pagination (1-59, appendix i-viii); PDF page = printed page + 2. Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Following Merton (1974), losers' equity turns into an out-of-the-money call on firm value after large losses; when the market rebounds, losers jump and momentum crashes | In the 13 crash months losers earn 45.69% vs winners 6.32%, market 16.14% (averages). Market down 37.23% over the prior 36 months; prior 12-month market volatility 36.39% vs 14.82% on average | p. 2, 8-9; Table 2 |
| 2 | The leverage is effective (operating plus financial), so book leverage misses it | Loser book debt / market equity 47.2 before the five post-1964 crashes vs 3.97 on average; but only 0.68 and 2.32 in the 2001 and 2002 crashes | p. 3, 9, 12; Table 2 |
| 3 | The option-like exposure is time-varying and causes the skewness | Call-payoff beta significant only after low 36-month market returns; momentum skewness -2.33 falls to -0.48 after removing it | Table 3A, 3D; p. 11-12 |
| 4 | Half of the value-momentum hedge comes from opposite market exposures in turbulent times; the rest from a hidden factor, "likely related to funding liquidity" | Market exposure explains 44% (linear) or 55% (with call term) of the high-state covariance; residuals load on liquidity proxies only in the high state | abstract; p. 33-34; Tables 11-12 |

**Caveats raised by the authors**
- Financial leverage does not proxy effective leverage; operating leverage is not measured (p. 3, 12).
- A state-variable model needs arbitrary window lengths, hence the HMM (p. 12-13).
- Hidden-state returns are "not directly achievable" (p. 18).
- Commodity and currency explanations are put as "likely", with no test (p. 2-3).

**Ruled out**
- Volatility alone as the tail-risk measure: more false positives than the HMM at the -20% threshold (Table 8).
- The HMM without the call term: 150 false positives vs 114 (Table 8 A-2).
- Formation-period market return alone as the driver of the value-momentum correlation (Table 10 A-1, A-2; p. 31-32).

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | CRSP common stocks, share codes 10 and 11, NYSE, AMEX, NASDAQ | p. 7 |
| Period | 1927:01-2013:12, 1044 months. Option tests 1996:01-2013:12 | p. 1, 27 |
| Signal | Cumulative return t-12 to t-2 (one month skipped) | p. 7 |
| Portfolio | MOM: value-weighted top decile minus bottom decile, NYSE breakpoints | p. 7, fn 3 |
| Rebalancing | Monthly | p. 7 |
| Risk model | Two-state HMM (calm, turbulent) on MOM and market excess returns; MOM residuals Normal, market residuals Student-t with 5 d.f. | Eq. 2-4; p. 13-19 |
| Hedge | "50/50-dyn": 0.5 MOM + 0.5 VMG when turbulent probability is in its top tertile, else 1.0 MOM. VMG: value-weighted top minus bottom B/M decile | p. 30, 35; Table 13 |
| Costs | None. All results gross | whole paper |

**Rule** (Eq. 2-3, p. 13-14), in state S_t ∈ {C, T}:

$$R_{MOM,t} = \alpha(S_t) + \beta_0(S_t) R^e_{MKT,t} + \beta^+(S_t)\max(R^e_{MKT,t},0) + \sigma_{MOM}(S_t)\varepsilon_{MOM,t}$$
$$R^e_{MKT,t} = \mu(S_t) + \sigma_{MKT}(S_t)\varepsilon_{MKT,t}$$

Markov transition between states; 14 parameters by maximum likelihood (Hamilton 1989); state probability Pr(S_t = T | F_t-1) updated by Bayes' rule, started at the steady state (Eq. 5-10, p. 14-17).

**Data provenance**
- Market, SMB, HML and VAL / GRO deciles: Kenneth French's library (fn 11, p. 30).
- Book debt from 1964 only (fn 6, Table 2).
- S&P 500 one-month at-the-money calls: OptionMetrics, 1996-2013 (Table 9, Fig. 3).
- Other factors and liquidity series: Frazzini, Pastor, FRED, CBOE, and series shared by other authors (fn 26).

## 3. Results

Real data, in-sample (full-sample parameters), gross, unless stated.

**Aggregate**

| Metric | Value | Where |
| --- | --- | --- |
| MOM mean / SD / Sharpe | 1.18% / 7.94% a month / 0.52 | Table 1 |
| Skewness / kurtosis | -2.43 / 21.22 | Table 1 |
| Worst / best month | -79.57% / 26.18%; six losses beyond 40% | Table 1; p. 2 |
| CAPM alpha; beta | 1.52% a month (t = 7.10); -0.52 | Table 1B |
| FF3 / FF5 alpha | 1.76% (t = 8.20) / 1.34% (t = 4.03) | fn 4 |
| Hou et al. four-factor alpha, 1967-2013 | 0.39% a month (t = 1.07) | fn 4 |

**HMM estimates** (Table 5)
- β+: -0.46 calm, -1.14 turbulent (t = -4.63). Up-market beta in turbulent state -1.45, down-market -0.32 (p. 17).
- σ_MOM: 4.31% vs 11.02%; σ_MKT: 4.04% vs 8.36% a month.
- Market: 13.3% a year, volatility 14.0% calm; -4.6%, 29.0% turbulent (p. 18).
- Persistence 0.98 calm, 0.94 turbulent.
- Simulation inside the HMM: only Normal / Student-t residuals put all four sample moments of MOM inside the 95% band (Table 6A; p. 18-19).

**Crash forecasting**
- Turbulent probability above 80% in 155 of 1044 months; all 13 losses below -20% fall there; mean MOM in those months -1.01% (p. 37-38; Table 7).
- Above 90%: 10 of 13 crashes, 108 months (Table 7).
- Gains above 20%: 8 of 12 also above 80%; 3 below 30% (p. 20; Table 7).
- False positives at -20% (1930-2013): HMM 114; without call term 150; MOM RV 147 (12m) to 227 (3m), GARCH 256; market RV 159 to 184; past market return 484 (36m) to 980 (3m) (Table 8).
- At -10% the HMM gives 902, more than market RV 12m (796), market GARCH (809), MOM GARCH (829) (Table 8).
- Real data, out-of-sample (expanding window from 1937, 1980:09-2013:12): all losses below -20% at probability ≈0.85 or above; gains above 20% spread from ≈0.33 to ≈0.80 (≈ Fig. 2B). No table.

**By sub-group** (state groups: top / bottom 20% of a state variable)
- Low past 36-month market: MOM β+ -1.01 (t = -3.17), loser β+ 0.72 (t = 3.60), adj. R² 0.48 vs 0.06 elsewhere; 11 of 13 crashes (Table 3).
- High 12-month market RV: all 13 crashes; low loser breakpoint: 12 of 13 (Table 14 B-2, C-2).
- 2000-2002: MOM β+ -1.35 (t = -1.26), not significant, 36 months (Table 4).

**Option-adjusted alpha** (1996-2013, full-sample HMM plus option prices)
- Mean 1.17% a month; significantly positive in 167 of 216 months (p. 27).
- Significantly negative only 2008:11, 2008:12, 2009:03; low point ≈-4.3% late 2008 (p. 27; ≈ Fig. 3).
- Residual loads on ROE (0.99, t = 2.99, R² 13%) and HML (-0.52, t = -1.97); no other factor significant (Table 9).
- FF3 alpha 1996-2013 1.25% (t = 2.22); Hou et al. alpha 0.04% (fn 27).

**Value-momentum comovement** (tertiles of turbulent probability, breakpoints 14% and 3%)
- Corr(MOM, VMG): -0.57 high, -0.07 med, -0.07 low, -0.44 all (Table 10A).
- Sorted on formation-period market return instead: -0.58, -0.44, -0.13 (Table 10 A-1).
- High tertile CAPM betas: MOM -0.89 (t = -6.83), VMG 0.58 (t = 4.56); residual correlation -0.25 (Table 10B).
- Liquidity proxies significant only in the high tertile, and only for VMG (TED -3.86, t = -2.17; Pastor-Stambaugh -16.06, t = -2.21) (Table 12A).

**Combined portfolios** (1927-2013, Table 13)

| Portfolio | Sharpe | Skew | Months < -10% |
| --- | --- | --- | --- |
| MOM | 0.52 | -2.43 | 56 |
| VMG | 0.28 | 2.62 | 27 |
| 50/50 static | 0.76 | -0.50 | 13 |
| 50/50-dyn | 0.91 | -0.33 | 8 |
| Conditional MVE (ex-post weights) | 1.05 | 0.35 | 8 |

The three combined portfolios show the same SD, 3.87%; no scaling is described (Table 13).

**Inconsistencies in the source**
- Months with negative option-adjusted alpha: 10 (p. 27, matching the four episodes listed) vs "49 out of the 216 months" (p. 38).
- Crash month: Table 2 lists 2002:11; text and fn 18 say 2002:12 (p. 12).

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Similar results grouping on 12-month market return, 6-month market RV, loser book leverage | fn 15 |
| Same optionality in commodity and currency momentum, from production costs, central banks, carry unwinds | p. 2-3 |
| HMM beats alternatives "even when estimated out-of-sample": only Fig. 2B, no false-positive count | p. 23 |
| Qualitatively similar with FF HML or AMP value; only covariances shown | fn 29; Table 15 |
| Loser operating leverage in 2000-2002 "likely quite high" | p. 12 |
| 50/50-dyn "close to the optimal strategy" | p. 36 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | 12-2 decile momentum, value weighted, NYSE breakpoints ([[Cross-sectional momentum]]) | technique | signal | Literature convention; skip month avoids microstructure and short-term reversal | p. 7, fn 10 |
| 2 | Two-state HMM turbulent probability with call-payoff term ([[Regime probability filter]]) | technique | signal | Summarises market conditions without choosing windows | p. 13-17 |
| 3 | Henriksson-Merton regression, max(R_m, 0) ([[Downside beta regression]]) | technique | evaluation | Measures convexity, exposure to a market call | Eq. 1, p. 10 |
| 4 | Group months on past 36m market return, 12m market RV, loser breakpoint ([[Market state filter]]) | technique | evaluation | Proxies for loser leverage | p. 10; Tables 3, 14 |
| 5 | Skewness of returns vs residuals of the option regression ([[Downside beta regression]]) | technique | evaluation | Shows skew comes from the call exposure | Table 3D |
| 6 | False positives at the threshold catching every crash ([[Crash forecast false positives]]) | technique | evaluation | Left tail need not move with volatility | p. 21; Table 8 |
| 7 | Option-adjusted alpha with index call prices ([[Option-adjusted alpha]]) | technique | evaluation | Linear-beta alpha can be spurious with option-like payoffs | p. 6, 23-27 |
| 8 | Correlation and covariance by tertile of state probability, raw and on residuals; double sorts ([[Regime-conditional correlation]]) | technique | evaluation | Locates the hedge and its source | Tables 10-11 |
| 9 | Add value hedge only in the high-probability tertile ([[Regime-conditional strategy combination]]) | technique | sizing | Correlation negative only in that state | p. 35; Table 13 |
| 10 | Choose residual distributions by simulated moment matching | technique | calibration | Misspecified likelihood can be inconsistent | p. 15, 18-19; App. A |
| 11 | Expanding-window re-estimation for out-of-sample probabilities | technique | calibration | Out-of-sample check | Fig. 2B |
| 12 | Regress residuals on factor list to check Assumption 1 | technique | evaluation | Validity of the alpha | Table 9 |

## 6. Regime observations

- Crash months: 1931-1933 (six), 1938, 1939, 2001:01, 2002, 2009:03, 04, 08 (Table 2).
- Option-adjusted alpha negative 1998:09-10, 2002:09-10, 2008:10-12, 2009:02-04 (p. 27).
- Market mean -4.6% a year in the turbulent state vs 13.3% calm; authors relate this to lower market Sharpe ratios when volatility is high (p. 18).
- Value-momentum correlation near zero in two thirds of months (abstract; Table 10).

## 7. Acknowledged limits

- Hidden-state returns are not achievable (p. 18).
- Option-adjusted alpha rests on Assumption 1; residuals correlate with HML and ROE (p. 26-28; Table 9).
- QML can be inconsistent under a wrong likelihood (App. A).
- Kolmogorov-Smirnov cannot reject any residual pair: low power (fn 21).
- Momentum betas of winners and losers in some groups left unexplained (fn 17).

## 8. Not addressed

- Costs, turnover, short-selling constraints, capacity.
- Out-of-sample crash counts and out-of-sample hedge results: tertile breakpoints, Tables 7-8 and 13 use full-sample information; whether Table 8 probabilities are full-sample is not stated.
- A trading rule that scales momentum by the turbulent probability.
- Markets other than US equities.
- Drawdowns of the combined portfolios; leverage of the conditional MVE.
