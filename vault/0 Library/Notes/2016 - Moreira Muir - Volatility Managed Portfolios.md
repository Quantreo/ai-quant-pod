---
type: reading-note
source: paper
title: "Volatility Managed Portfolios"
authors: Moreira, Muir
affiliations: Moreira (Yale School of Management), Muir (Yale School of Management, NBER)
year: 2016
venue: NBER Working Paper 22208
doi: 10.3386/w22208
pdf: "[[2016 - Moreira Muir - Volatility Managed Portfolios.pdf]]"
version: NBER working paper, April 2016, revised June 2016, not peer-reviewed
tier: 1
read: full
tags: [low-vol, multi-asset, monthly]
date: 2026-10-23
---

# Volatility managed portfolios (Moreira, Muir 2016)

## Summary

- **Finding**: scaling a factor each month by the inverse of last month's realized variance gives positive alphas on the unscaled factor: market 4.86% a year, appraisal ratio 0.33, gross, 1926-2015.
- **Mechanism**: variance is forecastable at short horizons but barely moves expected returns, so mean over variance falls when volatility rises. Why investors leave this: left open, speculative only.
- **Where it works best**: momentum (alpha 12.51%), ROE (5.48%), market; combined factor portfolios, appraisal ratios 0.33 to 0.91; weakest period 1956-1985.
- **Weak spots**: SMB and CMA alphas near zero; FX carry alpha 2.78% (t 1.87, computed), and negative with a common volatility factor; market alpha falls to 0.18% against six factors.
- **Main caveats**: gross except a market-only cost test; scaling constant c and MVE weights from the full sample; carry tested only in Tables 1, 3, 7 and 8; P99 market weight 6.4.

Page numbers follow the printed pagination of the working paper (body p. 1-25, tables and figures p. 30-42, appendix p. 43-55). Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Changes in factor volatility are not offset by proportional changes in expected returns | Market months sorted by lagged realized volatility: next-month mean flat (≈6% to ≈10%), next-month standard deviation rising (≈11% to ≈30%), mean over variance falling (≈7 to ≈1) | p. 1; Fig. 1 |
| 2 | Alpha equals minus the covariance of the price of risk µ/σ² with variance, scaled; zero if µ = γσ² | Derivation in continuous time | Eq. 7-8, p. 18-19 |
| 3 | With constant expected returns, alpha rises with the volatility of volatility | Jensen term Jσ | p. 19 |
| 4 | Variance shocks fade faster than expected-return shocks, so a mean-variance investor cuts exposure ≈50% on impact, below average for ≈12 months | VAR impulse response | p. 16-17; Fig. 5 |

Why investors do not trade it (p. 24-25), all called speculation: slow trading or slow updating of volatility beliefs (Nagel et al. 2016 households), learning about structural parameters, changing composition of shocks (discount-rate volatility). "A definitive answer to this question is beyond the scope of this paper" (p. 24).

**Caveats raised by the authors**
- The VAR expected-return response should be read with caution; return predictability is poorly estimated (p. 17).
- Proposed explanations need quantitative work (p. 25).
- Single-factor alphas are economically meaningful only for systematic factors (p. 19; App. A.6.2).

**Ruled out**
- Business cycle risk: betas lower in NBER recessions for all factors (Table 3, p. 10-11).
- Leverage constraints: caps at 1 and 1.5, and option-based leverage keep significant alphas (Table 5, p. 12-14).
- Cross-sectional low-risk anomalies: risk parity and BAB controls leave alphas unchanged (Tables 6, 9, p. 14-15, 44).
- Variance risk premium, downside risk, disaster and jump risk (p. 43-44, mostly without numbers).
- Option-like payoffs: MPPM and return densities (p. 45-46; Fig. 9).
- Four structural models (habits, long run risk, disasters, intermediary) rarely produce the data alpha (p. 23-24; Fig. 7).

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | Factors: Mkt, SMB, HML, Mom, RMW, CMA (Ken French), ROE, IA (Hou et al. 2014), FX carry HML (Lustig et al. 2011). Also BAB, MVE combinations, 20 OECD indexes | p. 5, 15, 43 |
| Period | 1926-2015 Mkt, SMB, HML, Mom; 1963-2015 RMW, CMA; 1967-2015 ROE, IA; 1983-2015 FX carry | Table 1 |
| Signal | Previous month's realized variance from daily returns, 22 days | Eq. 2, p. 6 |
| Sizing | Weight c / RV²; c set so the managed factor has the full-sample standard deviation of the original | Eq. 1, p. 5-6, fn 5 |
| Portfolio | Single factor, or a static in-sample max-Sharpe (MVE) mix scaled as a whole | Eq. 5, p. 9 |
| Rebalancing | Monthly; extension holds T months | p. 16-17 |
| Leverage | Uncapped in the main test; market weight P50 0.93, P99 6.39 | Table 5A |
| Costs | None, except a market-only test at 1, 10, 14 bp per unit of weight change | Table 4 |
| Evaluation | Regress managed on original factor, annualised (x12) alpha, heteroscedasticity-robust SE; appraisal ratio α/σε x √12 | Eq. 3, p. 6-8 |

**Rule** (Eq. 1-2, p. 5-6)

$$f^{\sigma}_{t+1} = \frac{c}{RV^2_t(f)} f_{t+1}, \quad RV^2_t = \sum_{d} \left(f_{t+d} - \bar f_t\right)^2 \text{ over the 22 daily returns of month } t$$

**Data provenance**
- Equity factors: daily and monthly from Ken French and Hou, Xue, Zhang (p. 5).
- FX carry: Lustig, Roussanov, Verdelhan (2011) monthly high-minus-low forward-discount factor, from Verdelhan. Volatility from daily exchange rate changes of the high and low portfolios, not from daily carry returns (p. 5).
- OECD indexes: Global Financial Data, mostly price only, in USD over the US risk-free rate (Fig. 8 caption).
- Options: Constantinides et al. (2013) S&P 500 portfolios, 1986-2012 (Table 5B).

## 3. Results

All real data, in-sample, gross unless stated.

**Aggregate**
- Market: alpha 4.86% (SE 1.56), beta 0.61, Sharpe 0.42 to 0.52 (Tables 1, 2, 5A).
- Utility gain for a mean-variance investor on the market: 65% (p. 8-9); 60% in Fig. 4 (p. 12).
- MPPM: market 2.48%, managed 4.33% (p. 45).
- MVE mixes: alphas 1.34 to 4.99, all significant; appraisal 0.33 (Mkt) to 0.91 (HXZ) (Table 2A).

**By sub-group**
- Single factors (Table 1A): best Mom 12.51 (SE 1.71), ROE 5.48 (0.97); worst SMB -0.58 (0.91), CMA 0.38 (0.67).
- With FF3 controls: Mom 10.52, SMB -0.33, CMA -0.01 (Table 1B).
- Against four Carhart factors, market alpha 2.43 (SE 1.60); against six factors 0.18 (1.87). Authors: momentum holds some of the scaled market's pricing information (Tables 10-11; p. 44).
- Recession beta, market: 0.83 outside, 0.32 inside recessions; RMW interaction -0.08 (SE 0.13), not significant (Table 3).
- 20 OECD indexes: Sharpe up 0.15 on average, higher in 80% of cases (p. 43). Negative ≈Chile -0.29, Israel -0.21, UK -0.13, France -0.12 (≈ Fig. 8).
- BAB managed: alpha 5.67 (SE 0.98) (Table 6).

**FX carry specifically**
- Univariate: alpha 2.78 (SE 1.49), t 1.87 computed, beta 0.71, R² 0.33, N 360 (Table 1A).
- With FF3 controls: 2.54 (SE 1.65), t 1.54 computed (Table 1B).
- Appraisal ratio stated 0.44 (p. 8); see inconsistencies.
- Recession interaction -0.26 (SE 0.15): beta 0.73 outside, 0.47 inside (computed), less significant than equity factors except RMW (Table 3).
- Common volatility factor (PC1 of all factors' realized variance): alpha -1.28 (SE 1.21). Authors: carry volatility differs from the mostly equity factors (Table 7; p. 15-16).
- Expected variance (three lags of log RV): alpha 1.77 (SE 0.90), beta 0.89, R² 0.81, rmse 13.66; appraisal 0.45 computed (Table 8; p. 43).
- Carry is absent from the MVE mixes, subsamples, costs, leverage, BAB and multifactor tests and Fig. 9 (Tables 2, 4-6, 9-11).

**Horizon and parameters**
- Market variants (Table 5A): realized vol alpha 3.30, Sharpe 0.53, P99 weight 3.36; expected variance 3.85, Sharpe 0.51; cap 1: 2.12, Sharpe 0.52; cap 1.5: 3.10, Sharpe 0.53.
- Costs, market, net (Table 4): at 14 bp alpha 3.63%; break-even 56 bp (variance), 84 bp (vol), 74 bp (expected variance), 110 bp (cap 1), 161 bp (cap 1.5). Mean |Δw| 0.73 for the base rule, 0.16 with caps.
- Options for leverage, 1986-2012: Sharpe 0.39 buy and hold, 0.59 managed, 0.54 calls, 0.60 calls plus puts (Table 5B).
- Holding T months: market alpha significant at 10% up to 18 months, decaying; appraisal ≈0.3 at one month to ≈0 at 2.5 years (p. 17; ≈ Fig. 6).
- Utility with caps: ≈45% for a 100% equity target under a 1.5 cap; ≈50% for 60/40 with no leverage (p. 13; Fig. 4).

**Over time**
- Subsamples, market: 8.11 (1926-1955), 2.06 (SE 2.82, 1956-1985), 4.22 (1986-2015). FF5 1956-1985: 0.13 (SE 0.43). All point estimates positive (Table 2B; p. 10).
- Losses relative to the market concentrated in low-volatility times such as the 1960s (p. 8).
- Market drawdown worst ≈-83% (1930s); managed worst ≈-55% (≈1940) and ≈-50% (≈1970) (≈ Fig. 3).

**Link to other strategies**
- Distinct from risk parity (rolling 3-year vol, cross-sectional) and BAB: alphas unchanged with them as controls; BAB loads insignificantly (Tables 6, 9).
- Simulated equilibrium models: Bansal-Yaron reaches the data alpha in 0.2% of samples, the others less (p. 23; Fig. 7). Simulation in the models, not market evidence.
- Constant price-of-risk simulation: managed MPPM beats the market 0.2% of the time; median alpha ≈10 bp (p. 45).

**Inconsistencies in the source**
- Carry appraisal ratio 0.44 (p. 8) vs 2.78 / 25.34 x √12 = 0.38 from Table 1 (computed).
- Table 4 gives alpha 3.85% for realized volatility and 3.30% for expected variance; Table 5A gives the reverse (3.30 and 3.85).
- VAR with one lag (p. 16) vs two lags (Fig. 5 caption).
- Carry labelled 1983-2015 but N = 360 months, 30 years (Table 1); end date not stated. Question left open.

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Results survive costs for all factors (only the market is tested) | p. 11-12 |
| Managed factors less exposed to volatility shocks; no numbers | p. 43 |
| Downside beta of managed market 0.11, "in unreported results" | p. 43 |
| Jump and disaster risk lower; argued, no test shown | p. 44 |
| Other variance forecasts (Andersen-Bollerslev) behave similarly | p. 43 |
| Equal-weight average of RVs, or market RV, give similar common-vol results | fn 13, p. 15 |
| MPPM not sensitive to risk aversion | p. 45 |
| Strategy worked in the Depression, 1987, 2008 (chart only) | p. 2; Fig. 3 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | [[Volatility targeting]]: scale a factor by c / last month's realized variance | technique | sizing | Mean-variance weight ∝ µ/σ²; volatility forecastable, does not predict returns | p. 5-6 |
| 2 | [[Volatility targeting]] variants: inverse vol, AR log-variance forecast, caps at 1 and 1.5, common volatility factor | technique | sizing | Less trading and leverage; common factor tests co-movement | Tables 4-5, 7-8 |
| 3 | Vol-manage a static MVE mix as a whole, keeping relative weights | technique | sizing | Isolates time-series timing | p. 9 |
| 4 | [[Volatility regime filter]]: sort months by lagged realized volatility, read next-month mean, sd, mean/variance | technique | evaluation | Shows the risk-return trade-off in time series | Fig. 1 |
| 5 | Alpha of managed on unmanaged factor, appraisal ratio, SR_new = √(SR_old² + AR²) | technique | evaluation | Measures expansion of the frontier | p. 6-8 |
| 6 | [[Downside beta regression]] (recession variant): interact the original factor with an NBER recession dummy | technique | evaluation | Tests business cycle risk | Table 3 |
| 7 | [[Break-even transaction cost]]: cost per unit of weight change that sets alpha to zero | technique | evaluation | Survival to realistic costs | Table 4 |
| 8 | [[Signal decay profile]]: alpha by holding horizon T, non-overlapping | technique | evaluation | Persistence of the volatility forecast | Eq. 6; Fig. 6 |
| 9 | Option portfolio (beta 7) for embedded leverage | technique | sizing | Removes the leverage objection | Table 5B |
| 10 | Manipulation-proof performance measure (Goetzmann et al. 2007) | technique | evaluation | Cannot be gamed by non-linear payoffs | p. 45 |
| 11 | Mean-variance utility gain (SR_new² - SR_old²) / SR_old² | technique | evaluation | Economic size of the gain | Eq. 4, p. 8 |
| 12 | Simulation under a constant price of risk | technique | evaluation | Null distribution for alpha and MPPM | p. 45 |

## 6. Regime observations

- Volatility of all factors rises in NBER recessions; high-volatility quintile has recession probability ≈0.42 vs ≈0.10 in the lowest (Fig. 1, 2).

## 7. Acknowledged limits

- MVE weights in sample, so original Sharpe ratios are overstated (p. 10).
- c from the full sample, said not to affect Sharpe ratios (fn 5).
- No good cost measures for factors other than the market (p. 11-12).
- Factor returns are hard for typical investors to trade, e.g. momentum (fn 7).
- OECD Sharpe levels unreliable (price indexes) (Fig. 8 caption).

## 8. Not addressed

- Costs of trading the carry factor and its volatility-managed version.
- Leverage distribution and drawdowns for carry.
- Out-of-sample or ex-ante test after 2015.
- Capacity, slippage, financing cost of leverage.
