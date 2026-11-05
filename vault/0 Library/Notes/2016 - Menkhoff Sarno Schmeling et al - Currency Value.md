---
type: reading-note
source: paper
title: Currency Value
authors: Menkhoff, Sarno, Schmeling, Schrimpf
affiliations: Menkhoff (DIW Berlin and Humboldt University Berlin), Sarno (Cass Business School, City University London, and CEPR), Schmeling (Cass Business School, City University London), Schrimpf (Bank for International Settlements)
year: 2016
venue: Review of Financial Studies 30(2), 416-441 (2017)
doi: 10.1093/rfs/hhw067
pdf: "[[2016 - Menkhoff Sarno Schmeling et al - Currency Value.pdf]]"
version: accepted manuscript dated June 8, 2016 (City Research Online), Internet Appendix included
tier: 1
read: full
tags: [value, fx, monthly]
date: 2026-10-23
---

# Currency value (Menkhoff, Sarno, Schmeling, Schrimpf 2016)

## Summary

- **Finding**: sorting 22 currencies on their 5-year real exchange rate change earns Sharpe 0.44 to 0.51, 1976-2014, gross. Purging four macro fundamentals from the signal lifts Sharpe to 0.79-0.91.
- **Mechanism**: the real exchange rate mixes expected risk premia, expected real rate differentials and a long-run level; removing fundamentals tied to the last two isolates the premium. Who pays: not stated.
- **Where it works best**: residual signal with VAR or panel VAR expected fundamentals: Sharpe 0.85-0.91, alpha 4.62% a year (t 4.97) over carry and momentum.
- **Weak spots**: the gain is lower volatility, not higher mean. A two-quarter lag cuts residual Sharpe to 0.39-0.61. Standard value drawdown ≈-25% (1990-91). Authors concede no theory specifies the mechanism.
- **Main caveats**: no transaction costs; returns from T-bill differentials; revised, not real-time, macro data; no hold-out period; Table A.II repeats Table 4 exactly; Table 1 Δq column inconsistent.

Page numbers follow the manuscript's printed numbering (1-51; PDF page = printed + 3); the journal pagination is not in this version. Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | The log RER equals summed expected excess returns (risk premia), minus expected real interest rate differentials (RIDs), plus the long-run expected RER. Controlling for fundamentals driving the last two leaves a cleaner risk premium. | Present-value identity, Eq. 2-4. Adding fundamentals raises the predictive slope (Table 3) and the Sharpe ratio (Table 5). | p. 6-8; Tables 3, 5 |
| 2 | Higher productivity (Harrod-Balassa-Samuelson) and higher export quality mean a persistently stronger RER. | Both negative and significant on 5-year RER changes (Table 7). | p. 7; Table 7 |
| 3 | Indebted countries (low net foreign assets, NFA) have a weaker RER, via a risk premium or nontraded prices. | NFA not significant in Table 7; significant for RIDs at 1 year only (Table 2). | p. 7-8; Tables 2, 7 |
| 4 | Output gaps feed real rates through a Taylor rule. | Predict RIDs at 2-3 years (Table 2). | p. 8; Table 2 |
| 5 | High-inflation countries may earn a risk premium; currencies that appreciated over 5 years earn low premia. | Opposite-signed components (Table 8). | p. 19-20 |

**Caveats raised by the authors**
- No theoretical framework yet specifies why a weak RER goes with a high risk premium (p. 24).
- Fundamentals explain at most 33% of value signal dispersion (p. 18; Table 7).
- Tangency weights are ex post and do not prove an ex-ante gain (fn. 13, p. 18).
- Real-time macro data do not exist for the sample; the two-quarter lag is an approximation (fn. 18, p. 23).

**Ruled out**
- One influential currency driving results (Table A.III, p. 22).
- Base-year effect of relative PPP (Table A.II, p. 22).
- Home bias in trade or equity as a driver: insignificant (Table A.I, p. 21-22).
- Gain as an artefact of investing less: rank portfolios show it too (fn. 10, p. 16).
- Value spanned by carry, momentum or the global imbalance factor (Table 6).

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | 22 currencies vs USD, developed and emerging. France, Italy, Spain dropped in 1999, Germany kept. Unbalanced with macro data. | p. 9, 43-44; fn. 21 |
| Period | Data 1970Q1-2014Q1; analysis from 1976Q1 (1970-75 for initial growth rates). Adjusted runs end 2013Q4, start 1980-81 with expected fundamentals. | p. 43; Table 5; Fig. 2 |
| Signal | Standard: 5-year change of the log CPI-based RER, Δ(5y)q = q(t) - q(t-5y). Higher q means a cheaper foreign currency. Modified: residual of a cross-sectional regression of Δ(5y)q on fundamentals, each quarter. | p. 5, 11, 15 |
| Fundamentals | Real GDP per capita (HBS), IMF export quality index, NFA / GDP, output gap (recursive quadratic trend). Used raw, or as expectations: EWMA (φ = 0.98, truncated at 20 quarters), country VAR(1) recursive from 1970Q1-1975Q4, or panel VAR. | p. 15-16, 44-46 |
| Entry / horizon | Signal at end of quarter t, hold quarter t+1. No lag in main tables; 2-quarter lag in Table A.V. | p. 13, 23 |
| Exit | Next quarterly rebalance. | p. 13 |
| Sizing | Linear: weight proportional to the signal minus its cross-sectional mean, absolute weights sum to 1. Rank: same with ranks. Quartile sort: 4 equal-weight bins, HML = P4 - P1. | Eq. 7-8, p. 13-14 |
| Rebalancing | Quarterly. Quarterly turnover about 21% (modified), 18% (standard), 10% (carry), 60% (momentum). | fn. 17, p. 23 |
| Costs | None. Results gross. | whole paper |

**Rule** (Eq. 7, 9, p. 13, 15), signal x(j,t) = Δ(5y)q or its residual ε(q):

$$\Delta^{(5y)}q_{j,t} = \alpha_t + \beta_t X_{j,t} + \varepsilon^q_{j,t}, \qquad w_{j,t+1} = \frac{x_{j,t} - \bar{x}_t}{\sum_j |x_{j,t} - \bar{x}_t|}$$

**Data provenance** (p. 9, 43-46)
- Global Financial Database: end-of-quarter spot, CPI, 3-month T-bills, GDP, population; gaps from Datastream (fn. 22).
- Excess return: RX = S(t+1)/S(t) x (1+i*)/(1+i), with 3-month T-bill rates, not forwards (p. 46).
- RER normalised to 1 in 1970Q1 (relative PPP). Robustness: OECD absolute PPP, annual, fewer countries, built from the 1990s (fn. 20).
- Export quality: IMF index, zero in 1970; correlation 0.49 to 0.82 with a structural-model dataset, six countries, 2005-2010 (p. 45-46).
- NFA: Lane and Milesi-Ferretti (2007), updated to 2014.
- RID: T-bill minus inflation, ex post.

## 3. Results

Real data, gross, signals built from information up to t, revised macro data (fn. 18). Called out-of-sample by the authors (p. 4); no hold-out period.

**Aggregate**

| Result | Value | Where |
| --- | --- | --- |
| Predictive slope of Δ(5y)q, panel with time fixed effects | 0.027 (t 2.89), R² 0.81%; with all controls 0.039 (t 4.00), R² 5.38% | Table 3A |
| Standard value, 1976Q1-2014Q1 | HML 3.89% (SR 0.44); rank 3.65% (SR 0.50); linear 2.32% (SR 0.51) | Table 4 |
| Modified value ε(q), four schemes | linear SR 0.79-0.91, rank SR 0.79-0.91; t 4.71-5.32 | Table 5 |
| Same sample, standard value | SR 0.53-0.60 | Table 5 |
| Fitted part of the signal | SR 0.07-0.32, t 0.42-1.87, never significant | Table 5 |
| ε(q) alpha (panel VAR, rank) | 4.67% (t 5.26) alone; 4.62% with carry and momentum; 2.31% (t 2.92) adding standard value | Table 6A |

- Rank ε(q) means 4.12-4.86% vs 4.16-4.76% standard; volatility 5.19-5.85% vs 7.85-8.06% (Table 5).

**By sub-group**
- Quartiles: P1 1.11% (t 0.73), P2 1.00%, P3 2.92%, P4 5.00% (t 4.00). The two rich quartiles earn about the same (Table 4).
- Drop-one-currency, rank ε(q): mean 3.40% to 5.24%, SR 0.67 to 0.96. Lowest when Korea is dropped, highest when Italy or India is dropped (Table A.III).
- Average rank weights: long Sweden, Korea, Canada; short New Zealand, Hungary, Japan, Switzerland; weight volatility around 11% (Table A.IV, p. 22-23).

**Signal decomposition** (linear, exact, Table 8A)
- RER level q: 3.95% (SR 0.41) = lagged level q(t-5y) 1.62% (t 1.14, not significant) + 5-year change 2.32% (computed: about 59%, "around 60%" p. 19).
- 5-year change = inflation component -11.74% (SR -0.71) + spot component 14.07% (SR 0.81). Long high inflation and recently depreciated currencies.

**Horizon and parameters**
- Local projections: without controls the slope is significant to about one year; with controls it is higher at every horizon and lasts about two years (p. 12; ≈ Fig. 1).
- Two-quarter implementation lag: standard SR 0.30-0.35 (t 1.83-2.04); ε(q) SR 0.39-0.61 (t 2.41-3.53) (Table A.V).
- Absolute PPP, annual rebalancing: "similar" to Table 4 (Table A.II; see inconsistencies).

**Over time**
- Standard value, rank: drawdowns ≈-25% around 1990-91 and ≈-22% in 2001-02; ε(q) ≈-10% in 2001-02 (Fig. 3).
- Linear: standard ≈-14% in 2001, ε(q) ≈-4% (Fig. 3).
- Standard value cumulative return flat or falling ≈1986-1991 and ≈1999-2002 (Fig. 2).

**Link to other strategies**
- ε(q) loadings: carry 0.06-0.13, momentum -0.14 to 0.03, standard value 0.44-0.45 (t 7.48-8.70), IMB 0.01-0.07 not significant; IR 0.53-0.91 (Table 6A).
- Ex-post tangency weight: ε(q) 0.35-0.65, carry 0.22-0.32 (Table 6B).
- Sequential sorts: value SR 0.53 in low carry vs 0.46 in high carry; carry SR 0.45 in low value vs 0.57 in high value. Authors: largely unrelated (Table 9, p. 20).

**Inconsistencies in the source**
- Table A.II (absolute OECD PPP, annual rebalancing, fewer countries) prints the same 28 figures as Table 4 (CPI PPP, quarterly). Both cannot be right.
- Table 1: Δq σ is 21.91 to 57.33, while ΔS σ plus Δπ σ is at most 21.93 per country (computed, e.g. India 5.05 + 3.58 vs 28.15). With q = p - p* - s this cannot hold; Δq means also do not match ΔS and Δπ.
- Fig. 2 axis says "in %", but lines end ≈1.5-1.6, the sum of ≈4.1-4.9% a year over 33 to 38 years as a fraction (computed).
- Rank weights: scaling "analogous" to linear (absolute sum 1) and "one dollar long and dollar short" (p. 14); these differ by a factor of two.
- Home bias: text says more trade home bias goes with a higher value signal (p. 21); Table A.I measures it as the import share (higher share, less home bias) with a positive slope.

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| ETFs using RER valuation signals are "quite common" | fn. 1, p. 1 |
| The ex-ante frontier likely expands with modified value | fn. 13, p. 18 |
| The unexplained part of the value signal is "largely" expected excess returns | p. 18-19 |
| On RER levels, higher NFA goes with higher valuation | fn. 14, p. 18 |
| OECD absolute PPP results "qualitatively robust" | fn. 20, p. 43 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | [[Currency value signal]]: 5-year log RER change | technique | signal | Comparable with prior work; avoids non-stationarity and base-year effects | p. 11, fn. 8 |
| 2 | [[Currency value signal]]: residual after a per-quarter regression on fundamentals | technique | signal | Removes the part tied to expected real rates and long-run RER | p. 15 |
| 3 | [[Currency value signal]]: expected fundamentals by EWMA (φ = 0.98), country VAR or panel VAR | technique | calibration | Proxies long-run expectations; φ from Piazzesi and Schneider | fn. 9, p. 15-16 |
| 4 | [[Long-short portfolio weighting]]: linear in the de-meaned signal | technique | sizing | Allows exact return decomposition | p. 13 |
| 5 | [[Long-short portfolio weighting]]: rank weights | technique | sizing | Smaller weight on outliers | p. 14 |
| 6 | [[Long-short portfolio weighting]]: quartile sort, HML P4 - P1 | technique | sizing | Standard comparison | p. 14 |
| 7 | [[Signal component return decomposition]]: additive signal, linear weights | technique | evaluation | Splits predictability into signal components | p. 13, 19 |
| 8 | [[Conditional double sort]]: median split on one signal, rank on another | technique | evaluation | Tests whether two signals overlap | p. 20 |
| 9 | [[Leave-one-out asset exclusion]]: drop one currency at a time | technique | evaluation | Rules out one influential currency | p. 22 |
| 10 | [[Implementation lag test]]: two extra quarters | technique | evaluation | Macro data are published with a lag | p. 23 |
| 11 | [[Signal decay profile]]: local projections, h = 1 to 20 quarters | technique | evaluation | Impulse response holding fundamentals fixed | p. 12 |
| 12 | Exposure regression on carry, momentum, value, IMB; ex-post tangency weights | technique | evaluation | Not spanned by known factors | p. 17-18 |
| 13 | Drawdown as cumulative return minus running peak | technique | evaluation | Downside risk | Eq. 10, p. 17 |
| 14 | [[Currency exclusion filter]]: drop euro members at adoption, keep Germany | technique | universe | Not argued | fn. 21 |
| 15 | Granger-type panel test of fundamentals on future RIDs | technique | economic intuition | Justifies the controls | p. 10 |

## 6. Regime observations

- Standard value drawdowns ran ≈1986-1994 and ≈1999-2003; the modified signal cut both (≈ Fig. 3).
- No conditioning on volatility, crises or rate regimes.

## 7. Acknowledged limits

- No theory for the risk premium (p. 24-25).
- No real-time macro data (fn. 18).
- No alternative export quality dataset large enough for a full robustness check (p. 45).
- Linear decomposition: mean returns not directly comparable across signals (p. 13).

## 8. Not addressed

- Transaction costs, bid-ask spreads, capacity.
- Forward rates and covered interest parity deviations: returns use T-bills.
- Hold-out or post-2014 data.
- How the carry and momentum factors of Table 6 are built.
- Why Singapore and Taiwan are absent from Table A.IV.
- Per-currency and per-year strategy returns.
- Sensitivity to the 5-year window or to φ.
