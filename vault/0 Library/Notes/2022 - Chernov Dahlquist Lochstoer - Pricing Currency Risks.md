---
type: reading-note
source: paper
title: Pricing Currency Risks
authors: Chernov, Dahlquist, Lochstoer
affiliations: Chernov (UCLA Anderson, CEPR, NBER), Dahlquist (Stockholm address and hhs.se email, institution not named), Lochstoer (UCLA)
year: 2020
venue: NBER Working Paper 28260, December 2020
doi: not printed; http://www.nber.org/papers/w28260
pdf: "[[2022 - Chernov Dahlquist Lochstoer - Pricing Currency Risks.pdf]]"
version: NBER working paper w28260, December 2020 (not peer-reviewed, p. cover). The file name says 2022; the version read is the 2020 working paper.
tier: 1
read: full
tags: [carry, fx, monthly]
date: 2026-10-23
---

# Pricing currency risks (Chernov, Dahlquist, Lochstoer 2020)

## Summary

- **Finding**: a real-time mean-variance portfolio of nine G10 currencies vs USD, using carry, value and trend expected returns, has Sharpe 1.075 (1985-2020, gross) and prices all nine standard currency strategies.
- **Mechanism**: authors: most currency variation is unpriced; the priced part links to consumption growth. Carry's link to intermediary capital and volatility comes from its unpriced part.
- **Where it works best**: hedging out the unpriced part lifts strategy Sharpe ratios, CS-Carry from 0.469 to ≈1.1; optimal timing adds significant alpha to Dollar and momentum strategies.
- **Weak spots**: timing CS-Carry and CS-Value adds nothing; volatility-only timing mostly fails; carry-only expected returns are rejected; no costs anywhere.
- **Main caveats**: gross, no transaction costs; specification choices (lags, windows, λ) not tested for sensitivity; portfolio volatility and drawdowns not reported; G10 only.

Page numbers follow the paper's printed pagination (PDF page minus 2). Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | One conditional mean-variance portfolio (UMVE) built from currency returns prices currencies and strategies | GRS p = 0.470, multi-horizon test p = 0.247, no strategy alpha significant | Tables 2-3; p. 19-20 |
| 2 | Most common variation in currency returns is unpriced | Strategy R² on UMVE 0.000 to 0.163; nine currency PCs explain ≈10% of UMVE | Table 2B; Fig. 2C; p. 23 |
| 3 | Priced risk relates to consumption growth, weakly | Quarterly Δc t = 2.52 (R² 0.031); 3-year Δc t = 3.17 (R² 0.073) | Table 5A; p. 26 |
| 4 | Carry's link to intermediary capital and FX or equity volatility sits in its unpriced component | UMVE unrelated (t 1.07, -0.57, -1.49); CS-Carry and its idiosyncratic part related (t 3.48 to -6.74) | Table 5B; p. 27 |
| 5 | Price of risk trends down, mainly from falling interest differentials | Same decline in the random-walk-only model | Fig. 4; p. 25-26 |
| 6 | High uncertainty goes with lower currency Sharpe ratios | 3-year change in price of risk on consumption variance t = -3.93, FX variance t = -2.81 | Table 5C; p. 27-28 |

**Caveats raised by the authors**
- Consumption R² of 3% and 7%: other elements may matter (p. 26).
- HML and CMA significant but R² 0.6% and 1.3%: effectively no link with equity priced risk (p. 27).

**Ruled out**
- Crash risk as key for pricing: UMVE skewness -0.04, excess kurtosis 3.1 (p. 3).

Why each signal predicts returns is taken from prior literature (random walk, PPP, trend), not tested as a mechanism (p. 10-12).

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | G10: AUD, CAD, EUR (spliced with DEM), JPY, NZD, NOK, SEK, CHF, GBP vs USD. Emerging and other European currencies excluded, following Daniel, Hodrick, Lu (2017). | p. 17 |
| Period | Returns January 1985 to May 2020; spot data from 1976 give 10 years to start the estimates | p. 17-18 |
| Return | Forward excess return (S(t+1) - F(t)) / F(t), month-end one-month forwards | p. 10, 17 |
| Expected return | E = 1 x (S/F - 1) + δ x value signal + φ x S(t)/S(t-12). γ fixed at 1 (random walk); δ, φ from monthly panel regressions, expanding sample | p. 12, 18 |
| Value signal | Real exchange rate over its average 54 to 66 months ago (13 months centred on t-60), demeaned across currencies; CPI lagged 3 months | p. 11-12, 17 |
| Covariance | Monthly realized covariance of daily spot changes, Ledoit-Wolf (2020) shrinkage, EWMA λ = 0.94; rescaled by S/F | App. A.1, p. 37 |
| Sizing | Weights (1 + θ)^-1 E' V^-1, θ = maximal conditional squared Sharpe | Eq. 8-9, p. 13 |
| Rebalancing | Monthly | p. 18 |
| Costs | None mentioned. Results are gross. | whole paper |
| Data | Datastream spot and forwards; OECD CPI (AUD, NZD quarterly, forward filled) | p. 17 |

**Rule** (Eq. 9, p. 13):

$$R^U_{t+1} = (1+\theta_t)^{-1} E_t(R^e)^\top V_t^{-1} R^e_{t+1}$$

**Nine test strategies** (p. 15-16): Dollar (equal weight); Dollar Carry (long or short all currencies by sign of average forward discount); CS-Carry, CS-Mom 1, CS-Mom 12 (12 months skipping the last), CS-Value with rank weights, one dollar long and one short (Eq. 11); TS-Carry, TS-Mom 1, TS-Mom 12 with sign weights, TS-Mom 12 also scaled by inverse conditional volatility. CS dollar neutral, TS dollar exposed.

**Hedging** (p. 20-21): conditional beta β = w'Vw_U / w_U'Vw_U; hedged portfolio β R^U, hedging residual R^P - β R^U.

**Timing** (p. 24): Eq. 8 applied to each strategy using its known weights and the model's mean and covariance.

**Data provenance**: Datastream, "several providers" (p. 17). AUD and NZD forwards from December 1984 (p. 17). Consumption: BEA NIPA Table 7.1; factors: French library; intermediary capital: He, Kelly, Manela (App. A.2).

## 3. Results

Real data, January 1985 to May 2020, gross. UMVE, timing and hedging use expanding-window estimates (authors: out-of-sample); the specification itself was fixed by the authors, how is not stated.

**Aggregate**

| Metric | Value | Where |
| --- | --- | --- |
| UMVE Sharpe, full model | 1.075 | Table 1D |
| Carry only / Carry+Mom / Carry+Val | 0.871 / 0.871 / 0.998; all have significant alpha on the full UMVE, R² 0.515 to 0.796 | Table 1D |
| Mean only (identity covariance) / covariance only (constant mean) | 0.565 / 0.165; GRS rejects both, p = 0.000 | Table 3 |
| Forecast check: realized on predicted mean / variance | slopes 0.838 / 0.931 (currencies), 0.791 / 1.055 (strategies) | Table 1A-B |
| Std of conditional expected returns vs average | 3.4% vs 3.2% across strategies | Table 1C; p. 4 |
| UMVE skewness / excess kurtosis | -0.04 / 3.1 | p. 3 |

**By sub-group** (Table 2, Fig. 1)
- Currencies: Sharpe 0.054 (JPY) to 0.427 (NZD); only NZD mean significant (t 2.54); no alpha significant, largest t 1.67 (NZD).
- Strategies: Sharpe 0.175 (CS-Mom 12) to 0.685 (TS-Carry); no alpha significant, largest t 1.75 (Dollar Carry). Alphas ≈70% below mean returns.
- R² on UMVE: TS-Carry 0.163, CS-Carry 0.151, CS-Value 0.136; Dollar 0.000.
- Hedged Sharpe (≈ Fig. 1): CS-Carry ≈1.1, TS-Carry ≈1.07, CS-Value ≈0.92, Dollar ≈0.22 (below its original 0.258).
- Hedging residual Sharpe (≈ Fig. 1): ≈-0.15 (CS-Mom 12) to ≈0.33 (Dollar Carry); ≈0.16 or more for six strategies. GRS hedged p = 0.475 (Table 3).

**Timing** (Table 4, annualized alpha on the original strategy)
- Full timing: Dollar 3.75 (t 2.72), TS-Mom 1 2.66 (t 2.92), CS-Mom 12 2.69 (t 2.42), CS-Mom 1 2.40 (t 2.14), TS-Mom 12 2.18 (t 2.06), TS-Carry 1.40 (t 1.95). Text says six significant (p. 25); five clear t = 1.96.
- Worst: CS-Value -0.53 (t -0.62), CS-Carry 0.48 (t 0.46).
- Volatility-only timing: none positive and significant; Dollar -1.31 (t -2.13), CS-Value -0.76 (t -1.93).

**Model tests** (Table 3)
- Carry-only model, all strategies: GRS p = 0.010, MHR p = 0.000. On Dollar and carry strategies only: GRS p = 0.309 but MHR p = 0.023.

**Factor structure** (Fig. 2-3, p. 22-24)
- Currency PCs: 58%, 18%, 9%. PC1 correlates 0.998 with Dollar, PC2 0.718 with carry.
- Strategy PCs: first three explain 65% of strategy variance, ≈20% of UMVE; five or more ≈50%. UMVE alpha stays significant (Fig. 3D).

**Over time** (Fig. 4)
- Price of risk from about 4 (1992 ERM crisis) to about 0.5; declines in recessions (p. 25-26).
- UMVE returns smooth; global financial crisis small negative returns and one large positive spike (≈ late 2008). Volatility falls over the sample (p. 26).

**Link to other strategies**
- UMVE vs Fama-French 5: only HML (t 2.04) and CMA (t 2.72), R² 0.006 and 0.013 (Table 5A).

**Inconsistencies in the source**
- Coefficients estimated "on a rolling basis" (p. 2) and by "rolling panel regressions" (p. 28) vs "an expanding sample" (p. 12, 18).
- Abstract: unpriced fraction "at least 85%"; intro: carry priced at most 15% (p. 3). Table 2B: TS-Carry R² 0.163.
- Fig. 1 original Sharpe: TS-Mom 1 ≈0.47, TS-Mom 12 ≈0.44; Table 2B: 0.440 and 0.473. Bars look swapped. Table values used.
- p. 22: "GRS strongly rejects both" sub-optimal models; Table 3: mean-only model on Dollar and carry strategies, GRS p = 0.084.
- p. 25 cites "Panel A of Table 2" and "Table 2A" for timing alphas and strategy Sharpes; they are in Table 4A and Table 2B.
- "Hedged" is defined as the priced part β R^U, with high Sharpe (p. 21), yet the "GRS hedged" test is of average hedged returns equal to zero "as implied by the model" (p. 21; Table 3); the model implies that for the unpriced residual.
- Second currency PC: 18% in text (p. 22), ≈0.16 in Fig. 2A. Text value used.

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Estimating γ (carry loading) by regression too "does not change the results" | p. 12 |
| Reverse Barillas-Shanken regressions give no significant alphas ("unreported") | p. 19 |
| UMVE "is not explained by any existing factors" | p. 28 |
| Multi-horizon pricing tests "most, if not all" conditional misspecification (cited, not shown) | p. 14 |
| Compelling arguments to exclude emerging currencies (cited to Daniel, Hodrick, Lu) | p. 17 |
| All portfolios tradeable in real time; no costs or execution shown | p. 2-3, Fig. 1 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | Conditional mean-variance portfolio of currencies, weights (1+θ)^-1 E' V^-1 | technique | sizing | Projects the SDF; small FX cross-section makes it feasible. Card: [[Mean-variance weighting]] | Eq. 8-9, p. 13 |
| 2 | Expected return = carry (loading fixed at 1) + value + 12-month trend, panel regression, expanding window | technique | signal | Random walk is a robust forecaster; value and trend from literature. In card [[Mean-variance weighting]] as a parameter | p. 10-12 |
| 3 | Realized daily covariance, Ledoit-Wolf shrinkage, EWMA λ = 0.94 | technique | risk | Precision with short samples; RiskMetrics. In card [[Mean-variance weighting]] as a parameter | App. A.1 |
| 4 | Value: real exchange rate over its 13-month average five years ago, demeaned across currencies, CPI lagged 3 months | technique | signal | Long-run mean ill-defined; removes time and currency effects. Card: [[Currency value signal]] | p. 11-12, 17 |
| 5 | Hedge out the unpriced part with the conditional beta on the UMVE | technique | evaluation | Raises Sharpe (Daniel et al. 2020). Card: [[Priced and unpriced component split]] | p. 20-21 |
| 6 | Optimal timing of a single strategy by its conditional mean and variance | technique | sizing | Conditional premiums vary as much as their level. Card: [[Mean-variance weighting]] | p. 24 |
| 7 | Volatility-only timing of a strategy | technique | sizing | Isolates the role of the conditional mean. Card: [[Volatility targeting]] | Table 4B |
| 8 | CS strategies with rank weights, one dollar long and short | technique | sizing | Follows the literature. Card: [[Long-short portfolio weighting]] | Eq. 11, p. 15-16 |
| 9 | CS-Carry, TS-Carry, Dollar Carry | technique | signal | Leading strategies. Card: [[Carry signal]] | p. 15-16 |
| 10 | TS-Mom 1 and 12, CS-Mom 1 and 12 (skip last month) | technique | signal | Leading strategies. Cards: [[Time-series momentum signal]], [[Cross-sectional momentum]] | p. 16 |
| 11 | Regress realized returns and squared errors on forecasts (slope 1 check) | technique | evaluation | Checks the inputs are plausible | Table 1A-B |
| 12 | PCA of returns, then R² of the priced factor on the PCs | technique | evaluation | Shows variance factors are not priced factors | Fig. 2-3 |
| 13 | GRS, multi-horizon and Barillas-Shanken tests | technique | evaluation | Standard pricing tests | Tables 1D, 3 |

## 6. Regime observations

- 1992 ERM crisis: price of risk peaks; random-walk model UMVE return ≈-3 (≈ Fig. 4).
- Recessions associated with a lower price of risk (Fig. 4; p. 26).
- Global financial crisis: small negative UMVE returns, one large positive spike (p. 26).
- Lower Sharpe ratios when consumption and FX variance rise (Table 5C).

## 7. Acknowledged limits

- Consumption explains little of priced risk (p. 26).
- Factor-timing gains left unexplained by existing strategies (p. 24).

## 8. Not addressed

- Transaction costs, bid-ask spreads, turnover, capacity.
- Volatility, leverage and drawdowns of the UMVE or timed strategies: k(t) is "any positive constant" (p. 8).
- Sensitivity to λ = 0.94, the 5-year value window, the 3-month CPI lag, the 12-month trend lookback.
- Data after May 2020; currencies outside G10.
- How the specification was chosen; no hold-out sample.
