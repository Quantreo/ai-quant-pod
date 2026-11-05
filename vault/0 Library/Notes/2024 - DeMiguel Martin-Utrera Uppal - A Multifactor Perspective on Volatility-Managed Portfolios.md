---
type: reading-note
source: paper
title: "A Multifactor Perspective on Volatility-Managed Portfolios"
authors: DeMiguel, Martin-Utrera, Uppal
affiliations: DeMiguel (London Business School), Martin-Utrera (Iowa State University), Uppal (EDHEC Business School, CEPR)
year: 2024
venue: The Journal of Finance
doi: 10.1111/jofi.13395
pdf: "[[2024 - DeMiguel Martin-Utrera Uppal - A Multifactor Perspective on Volatility-Managed Portfolios.pdf]]"
version: Journal of Finance, accepted April 30, 2024; Internet Appendix not read (not in the PDF)
tier: 1
read: full
tags: [low-vol, equities, monthly]
date: 2026-10-25
---

# Multifactor volatility-managed portfolios (DeMiguel, Martin-Utrera, Uppal 2024)

## Summary

- **Finding**: out-of-sample and net of costs, a multifactor portfolio whose factor weights fall with market volatility has Sharpe 1.062 against 0.940 unconditional, 1977-2020 (Table II).
- **Mechanism**: the risk-return trade-off of all nine factors is lower in high market volatility months; the authors call this puzzling and give no cause.
- **Where it works best**: momentum, ROE and BAB timing; netting trades across factors cuts cost. Single factors: only UMD, IA, BAB beat unmanaged net and out of sample (Table I, E).
- **Weak spots**: the managed market has a lower Sharpe than the unmanaged market out of sample, 0.408 against 0.530, and net, 0.433 against 0.519 (Table I C, E).
- **Main caveats**: single factors fail out of sample and net of costs, as Cederburg and Barroso and Detzel found; the multifactor gain rests on netting stock-level trades; Internet Appendix not read.

Page numbers follow the journal pagination, which equals the PDF page. Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | The factor risk-return trade-off (next-month return over this month's realized variance) weakens with market volatility, for all nine factors | Tercile sort on realized market volatility: low tercile above high tercile for every factor (≈ MKT 15 vs 3, UMD 56 vs 5, BAB 69 vs -2, CMA 14 vs 12) | p. 4, 27; Fig. 1 |
| 2 | Same result as a price of risk: slope on inverse market volatility positive for every factor | Table V, Newey-West t: significant for MKT 2.36, HML 2.27, RMW 2.24, UMD 3.84, ROE 2.62, BAB 7.20, IA 1.98; not for SMB 0.42, CMA 0.75 | Table V, p. 29 |
| 3 | Conditional weights falling with volatility beat unconditional ones, so the link between expected returns and covariance weakens with volatility | Weights satisfy mu = gamma x Sigma x w (footnote 1) | p. 2, fn 1 |

The authors expect the price of risk of systematic factors to stay constant or rise with volatility, and call the result counterintuitive (p. 4, 29). Cause: Not stated by the authors.

**Caveats raised by the authors**
- Fitted price of risk is positive every month for SMB, RMW, CMA, ROE, IA; more than 95% of months for UMD, BAB; more than 85% for MKT; about 70% for HML (fn 40, p. 30).
- Trade-off values above 50 look large; Sharpe ratios stay below one in every tercile (fn 37, p. 27).

**Ruled out**
- Estimation error and transaction costs as explanations of the multifactor gain (p. 2).
- Sentiment (high versus low sentiment periods), Internet Appendix only (fn 3, p. 3).

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | Nine US equity factors: MKT, SMB, HML, RMW, CMA, UMD (French), ROE, IA (Hou, Xue, Zhang), BAB (Frazzini, Pedersen) | p. 6 |
| Period | Data 1967-2020; first window 120 months; out of sample and in-sample compared over Jan 1977 to Dec 2020 | p. 6 |
| Signal | Realized variance: sample variance of daily returns of the previous month (factor, or market volatility for the multifactor case) | p. 7-8 |
| Sizing, single factor | Weight c / variance; investor holds the optimal mix of unmanaged and managed factor, gamma = 5, expanding window | Eq. 1, p. 7, fn 7 |
| Sizing, multifactor | Weight on factor k = a_k + b_k / market volatility, a_k and b_k at least 0, chosen by mean-variance utility net of costs | Eq. 3, 6, p. 8-9 |
| Rebalancing | Monthly | p. 6-9 |
| Costs | Stock-level half bid-ask spread from the Abdi and Ranaldo two-day estimator; trades netted across factors before charging | Eq. 10, 12, p. 10 |
| Evaluation | Out-of-sample net Sharpe ratio, one-sided p-value from a stationary block bootstrap (10,000 draws, mean block 5), alpha on the unconditional portfolio | fn 15, p. 12-13, 17 |

**Rule** (Eq. 1 and 3-4, p. 7-8)

$$r^{\sigma}_{k,t+1} = \frac{c}{\sigma^2_{k,t}}\, r_{k,t+1}, \qquad r_{p,t+1} = \sum_k r_{k,t+1}\Big(a_k + \frac{b_k}{\sigma_t}\Big)$$

c makes the managed factor's volatility equal to the unmanaged one's (p. 7). The unconditional portfolio is the same problem with b_k = 0 (p. 17). The footnote 7 argument says the optimal mix does not depend on c.

**Data provenance**
- Factor returns downloaded from the authors' websites. The authors also rebuild value-weighted factors from CRSP and Compustat (NYSE, AMEX, NASDAQ), correlation with the originals above 90%, to price stock-level trades (p. 6, fn 5).
- The factors are zero-cost portfolios (p. 6).

## 3. Results

All real data, 1977-2020. Out-of-sample means expanding window.

**Aggregate** (Table II, out of sample, net, trading diversification)
- UMV: mean 0.430, sd 0.458, Sharpe 0.940, cost 0.163. CMV: mean 0.477, sd 0.449, Sharpe 1.062, cost 0.213. P-value 0.006.
- Alpha of CMV on UMV 0.066, t 3.637 (p. 18). Figure 4: CMV above UMV steadily, ≈21 against ≈19 cumulative dollars at the end.
- Table III, Moreira and Muir fixed-weight version (CFW): Sharpe 0.984, or 1.026 if optimised for costs, against UMV 0.891 or 0.940 (Panel D).
- Table III, gross out of sample: UMV 1.299, CFW 1.506, CMV 1.625 (Panel B). Net without netting trades: UMV 0.710, CFW 0.601, CMV 0.613 (Panel C).

**By sub-group: single factors** (Table I, Sharpe unmanaged then managed mix)
- MKT: in-sample gross 0.530 then 0.585, p 0.242 (A); out-of-sample gross 0.408, p 0.899 (C); net with netting 0.433 against 0.519, p 0.917 (E).
- In-sample gross, managed above unmanaged for all nine, significant at 10% for RMW, UMD, ROE, IA, BAB (A, p. 14).
- Out of sample, gross: significant for UMD, ROE, IA, BAB; lower than unmanaged for MKT, SMB, CMA (C, p. 15).
- Out of sample, net with netting: significant for UMD (p 0.097), IA (0.029), BAB (0.064); five of nine higher (E, p. 15-16).
- Net of cost without netting, in-sample: managed gets zero weight for SMB, HML, RMW, CMA, IA (B, p. 14-15). Out of sample, five managed Sharpe ratios are negative (D).

**Where it does not work**
- MKT, SMB, CMA out-of-sample Sharpe below unmanaged even before costs (Table I C). Figure 3: managed MKT ends below unmanaged (≈).
- Price of risk slope not significant for SMB, CMA (Table V).

**Horizon and parameters**
- Four sources of gain: netting trades across factors, optimising for cost, letting factor weights differ, and market volatility as the conditioning variable (p. 3, 20-26).
- Table IV: CMV Sharpe 0.739 with no netting, 0.783 netting only within a factor, 1.062 netting across factors; UMV without netting 0.758.
- Four managed factors have negative net mean return without netting: SMB, HML, CMA, IA (Fig. 5, p. 23).
- Six factors timed strongly (HML, RMW, UMD, ROE, IA, BAB); MKT, SMB, CMA nearly constant weight; average HML weight about 0.35 (Fig. 6, p. 26). In-sample weights.
- Single factors, equal weight on managed and unmanaged and a six-month volatility window: significant outperformers rise from three to five (fn 22, p. 16); Internet Appendix.

**Over time**
- Figure 4: CMV leads steadily over the whole sample (p. 19).
- Weights on six factors drop in the Great Recession and after the early 2000s recession, rise in 1992-1997 (p. 26).

**Link to other strategies**
- Single-factor results confirm Moreira and Muir in-sample and Barroso and Detzel (costs) and Cederburg et al. (out of sample) (p. 14-17).
- Market and size factors are moderately negatively correlated with the other seven (fn 33, p. 25).

**Inconsistencies in the source**
- Fig. 1 caption text: weak weakening for SMB and CMA (p. 4); same sentence on p. 27 adds MKT.
- Introduction: "four of the nine managed factors" negative net (p. 3); Table I B text: five of nine get zero weight (p. 14). Different tests, not a contradiction.

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Results hold for 66 factors, in both halves, ex each factor, in crises, with leverage cap | fn 4, 6, 10, 28 (Internet Appendix) |
| CMV is less risky on VaR, drawdown, skewness, kurtosis | fn 27 |
| Gains hold at horizons up to 18 months | fn 10 |
| Timing each factor by its own volatility does better | p. 7 |
| Longer volatility windows (3, 6, 12 months) improve CMV | fn 28 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | [[Volatility targeting]] variant: mix of unmanaged and variance-scaled factor, weights chosen on an expanding window | technique | sizing | Mean-variance combination, as Moreira and Muir | p. 7, fn 7 |
| 2 | [[Volatility targeting]] variant: factor weights affine in inverse market volatility, nonnegative | technique | sizing | Lets each factor load differently on volatility | p. 8-9 |
| 3 | [[Cross-strategy trade netting]]: net trades across factors, then charge costs per stock | technique | rebalancing | Managed factors are costly; netting cuts the cost | p. 10, Table IV |
| 4 | [[Volatility regime filter]] variant: tercile sort on market volatility, read next-month return over variance | technique | evaluation | Shows the trade-off weakens with volatility | Fig. 1 |
| 5 | [[Risk price regression on inverse volatility]]: factor return over its variance on demeaned inverse market volatility | technique | evaluation | Tests how the price of risk moves | Eq. 17, Table V |
| 6 | [[Maximum entropy bootstrap Sharpe test]] variant: stationary block bootstrap of the Sharpe gap, one-sided p | technique | evaluation | Inference on managed against unmanaged | fn 15 |
| 7 | [[Chronological holdout test]] variant: expanding window, first 120 months, same period in-sample for comparison | technique | evaluation | Follows Cederburg et al. | p. 14 |
| 8 | Half bid-ask spread from daily close, high, low (Abdi, Ranaldo) | technique | evaluation | Stock-level cost parameter | Eq. 12 |

## 6. Regime observations

- Price of risk lower in high market volatility months (Fig. 1, Table V).
- Stock costs are largest in NBER recessions (Fig. 2, p. 12).

## 7. Acknowledged limits

- Single-factor gains do not survive out-of-sample and net of costs (p. 17).
- Nonnegativity constraints and one-month volatility chosen to match the literature (p. 9, fn 28).
- Conditional multifactor portfolio has higher transaction costs than the unconditional one: 0.213 against 0.163 (Table II).

## 8. Not addressed

- Why the risk-return trade-off weakens with volatility.
- Data after 2020, markets other than US stocks, ETFs or futures as the traded instrument.
- Capacity, short-selling and financing costs, leverage of the managed market (leverage cap only in the Internet Appendix, p. 9).
