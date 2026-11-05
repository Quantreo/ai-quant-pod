---
type: reading-note
source: paper
title: Diversified reward-risk parity in portfolio construction
authors: Choi, Kim, Kim
affiliations: Goldman Sachs & Co. (New York); Citigroup, Inc. (New York); College of Business, Stony Brook University
year: 2021
venue: arXiv:2106.09055v3 [q-fin.PM], preprint submitted to Elsevier, 30 Sep 2022
doi: Not stated by the authors.
pdf: "[[2021 - Choi Kim Kim - Diversified reward-risk parity in portfolio construction.pdf]]"
version: arXiv v3, 29 Sep 2022
tier: 1
read: full
tags: [low-vol, equities, monthly]
date: 2026-10-25
---

# Diversified reward-risk parity (Choi, Kim, Kim 2021)

## Summary

- **Finding**: on the Dow Jones 1999-2020, long-only weights set by past reward-risk ratios or inverse risk beat equal weight on Sharpe: raw Calmar 0.5524, inverse variance 0.5402, against 0.4967 (Tables 3-4). Gross.
- **Mechanism**: the authors say the gain comes from taking less downside risk and link it to the low volatility anomaly (p. 16-19). No further mechanism given.
- **Where it works best**: inverse variance and inverse maximum drawdown cut maximum drawdown to 46.4% and 50.4% from 57.8% at 9.4% a year against 9.8% (Table 4, DJIA only).
- **Weak spots**: raw ratio rules turn over 58% to 69% against 6.7%, and their VaR and CVaR are worse than equal weight (Table 3). Raw Sharpe alpha falls 23.5% (Table 5, p. 17).
- **Main caveats**: no transaction costs, no significance test of the gap to equal weight, other universes and risk models not shown, 6-month window and rules fixed without a stated reason.

Page numbers follow the printed pagination of the arXiv preprint (same as the PDF pages, 1 to 27). Values marked ≈ are read from a chart. The paper has no figures.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Outperformance comes from less downside risk | Lower std, VaR, CVaR, max drawdown for many rules in the DJIA | Tables 3-4; p. 18 |
| 2 | The results are consistent with the low volatility anomaly | Better reward-risk profile at lower turnover; inverse-risk rules have the highest Carhart alpha | p. 16-17, 19; Table 5 |
| 3 | Part of the raw ratio rules' profit is factor exposure | Raw Sharpe alpha is 23.53% below equal weight; its momentum loading turns positive (+0.1253 against -0.0754) | Table 5; p. 17 |

**Caveats raised by the authors**
- Raw Sharpe and Calmar rules are the most profitable but carry heavy downside tails and high turnover that "imply expensive transaction costs" (p. 15).
- STAR and Rachev raw rules pay for the gain with higher turnover (p. 15).

**Ruled out**
- Not stated by the authors.

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | Dow Jones Industrial Average constituents (time-varying, 1999-01-01 to 2020-12-31); also global equity benchmarks, 13 mutual funds and 4 ETFs from the largest list, 9 SPDR sector ETFs, same period | p. 11-12; Table 1 |
| Data | Adjusted daily prices from Yahoo Finance. Risk-free: 91-day T-bill yield (^IRX) | p. 11-12 |
| Signal | Per-asset reward-risk or risk measure over the last 6 months of daily data | p. 12 |
| Measures | Sharpe, conditional Sharpe, Calmar (6-month window), STAR, Rachev (ratios); std, variance, conditional std and variance, VaR, CVaR, max drawdown (risks) | p. 7-10; Table 2 |
| Risk models | ARMA(1,1)-GARCH(1,1) with CTS or NTS innovations; ARMA(1,1)-DCC GARCH(1,1) with MNTS. Max drawdown and Calmar from raw returns | p. 10-12 |
| Sizing | Weight proportional to a function of the measure, normalised to sum to 1 (see Rule) | p. 4-7, 12 |
| Shorting | Not allowed: negative ratios floored at zero | p. 12 |
| Rebalancing | Hold 6 months; a sixth of the book is re-set each month ("6/6 monthly") | p. 12 |
| Costs | None applied. Turnover reported only | Tables 3-4 |
| Benchmark | Equal weight | p. 12 |

**Rule**
- Generic: w_i = Φ(ρ_i) / Σ Φ(ρ_j) (Eq. 5, p. 5).
- Ratio measures, two rules: ρ_i floored at 0, and 1 + ρ_i floored at 0 (Eq. 10 with a = 0 or 1, b = 1; Table 2, p. 12, 24).
- Risk measures, two rules: 1/ρ_i (Eq. 11) and 1 − ρ_i (Eq. 12) (p. 12, 24).
- Special cases: ρ = beta gives equal risk contribution (Eq. 1), ρ = σ gives inverse volatility (Eq. 2), ρ = σ² gives inverse variance (Eq. 3) (p. 4).
- Φ is limited to monotone functions and risk-averse investors (p. 5).

**Data provenance**
- Yahoo Finance adjusted prices (p. 11). The acknowledgement says the first draft used Bloomberg data in 2012 and the results were reproduced with newer data (p. 19).

## 3. Results

All numbers are DJIA, real data, in-sample, gross of costs (Tables 3-5), 6/6 monthly. Equal weight: mean 9.84% a year, std 19.82%, Sharpe 0.4967, Calmar 0.1702, max drawdown 57.81%, turnover 6.75%.

**Aggregate**
- Raw (floored) ratio rules, mean 9.59% to 10.32%, Sharpe 0.50 to 0.55, turnover 13% to 69% (Table 3, range computed).
- Raw Calmar best: mean 10.32%, Sharpe 0.5524, max drawdown 39.46%, CVaR 1.99 against 1.26, turnover 66.07% (Table 3).
- Raw Sharpe: mean 9.59%, Sharpe 0.5136, max drawdown 44.02%, turnover 58.46% (Table 3).
- Linear (1 + ρ) ratio rules stay close to equal weight: Sharpe 0.497 to 0.516 (Table 3).
- Inverse risk rules (1/ρ): mean 9.36% to 9.54%, Sharpe 0.517 to 0.540, max drawdown 46.1% to 50.4%, turnover 9.0% to 18.7% (Table 4, range computed).
- Inverse variance: mean 9.42%, std 17.44%, Sharpe 0.5402, max drawdown 46.41%, turnover 12.87% (Table 4).
- Linear risk rules (1 − ρ) are almost equal weight; only max drawdown differs (mean 9.45%, drawdown 53.85%, turnover 5.49%) (Table 4).

**By sub-group**
- Other universes (global indexes, funds and ETFs, sector ETFs) and the NTS and MNTS models: described in words only, no table (p. 15-16). The authors say all beat equal weight and that raw Calmar and Sharpe are the most profitable in many universes (p. 15).

**Horizon and parameters**
- One window (6 months) and one holding scheme (6/6 monthly). Not varied. Only confidence levels of VaR, CVaR and STAR (90%, 95%, 99%) vary, with little effect on the mean (Tables 3-4).

**Over time**
- Not addressed. Only full-sample statistics.

**Link to other strategies**
- Carhart four-factor regression, monthly, DJIA (Table 5). Equal-weight alpha 0.2129 per month, market beta 0.94, R² 0.9165.
- Inverse risk rules: alpha 0.2263 to 0.2838, significant at 1%, market beta 0.81 to 0.88, momentum beta close to 0 (Table 5).
- Raw Sharpe: alpha 0.1628, not significant; momentum beta +0.1253, R² 0.8390 (Table 5).
- Alphas are tested against zero. No test of the gap with equal weight.

**Inconsistencies in the source**
- p. 14 says linear rules for Sharpe, STAR, max drawdown, std, variance, VaR and CVaR have turnover of 5.49% to 6.69%, below 6.75%. Table 3 gives linear STAR 6.96% to 8.04%.
- p. 13 says all STAR and Rachev rules are more profitable than equal weight (Rachev "9.80% to 9.87%"). Table 3 gives raw Rachev 9.73% to 9.88%, with R(50%,95%) at 9.80% and R(50%,99%) at 9.73%, both below 9.84%.
- Abstract says turnover is lowered. Table 3 shows turnover above equal weight for the raw rules and for most linear ratio rules.

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| The rules outperform equal weight in every market | p. 15, 18 |
| Results do not depend on the risk model (NTS, MNTS) | p. 16 |
| Linear STAR rules are less volatile and less risky in all universes | p. 15 |
| The gain is evidence of the low volatility anomaly | p. 19 |
| The rules are "simple and straightforward" as equal weight; no computation time or fit failure reported | p. 3 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | Weights proportional to a floored reward-risk ratio (Sharpe, Calmar, STAR, Rachev), normalised, long-only | technique | sizing | Favour assets with better reward per unit of risk. Card: [[Reward-risk parity weighting]] | Eq. 6-10, p. 6, 12 |
| 2 | Inverse risk weights, 1/ρ for std, variance, VaR, CVaR, max drawdown; linear 1 − ρ variant. Card: [[Volatility targeting]] | technique | sizing | Penalise risky assets; the investor is risk averse | Eq. 2-3, 11-12; p. 4, 7 |
| 3 | Fraction of the book re-set each month, 6 months hold (6/6) | technique | rebalancing | Not argued | p. 12 |
| 4 | Tail-based ratios: STAR (return over CVaR), Rachev (upper-tail CVaR over lower-tail CVaR) | technique | signal | Remove upside from the risk measure and downside from the reward | Eq. 19-20, p. 9-10 |
| 5 | ARMA-GARCH-CTS risk model to estimate the measures | technique | calibration | Captures autocorrelation, clustering, skew, heavy tails | p. 10-11 |
| 6 | Carhart four-factor regression of portfolio returns | principle | evaluation | See what profit is factor exposure | Eq. 22, p. 17 |

## 6. Regime observations

- Not addressed.

## 7. Acknowledged limits

- High turnover of the raw ratio rules erodes performance (p. 15).
- Raw Sharpe and Calmar rules are exposed to downside tails (p. 15).
- Linear risk rules give "slightly lower volatility" and comparable returns, not a larger return (p. 16).

## 8. Not addressed

- Transaction costs and slippage, short-selling, capacity, taxes.
- Subperiods, crisis behaviour, statistical tests of the gap to equal weight.
- Sensitivity to the 6-month window and to the 6/6 scheme.
- Tables for the other universes and risk models.
- Whether Table 3 turnover is per rebalance or annual (called "percentage scale", p. 25).
