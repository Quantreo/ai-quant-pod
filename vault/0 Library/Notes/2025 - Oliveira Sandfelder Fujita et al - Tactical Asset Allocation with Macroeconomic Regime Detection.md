---
type: reading-note
source: paper
title: Tactical Asset Allocation with Macroeconomic Regime Detection
authors: Oliveira, Sandfelder, Fujita, Dong, Cucuringu
affiliations: University of São Paulo; Oxford-Man Institute of Quantitative Finance, University of Oxford; Kyushu University; UCLA
year: 2025
venue: arXiv:2503.11499v2 [q-fin.PM], 21 Mar 2025
doi:
pdf: "[[2025 - Oliveira Sandfelder Fujita et al - Tactical Asset Allocation with Macroeconomic Regime Detection.pdf]]"
version: preprint (v2)
tier: 1
read: full
tags: [trend, equities, monthly]
date: 2026-10-25
---

# Macro regime tactical allocation (Oliveira et al. 2025)

## Summary

- **Finding**: on 10 US equity ETFs, monthly, walk-forward to 2022, a long-only ridge model on macro regimes reaches Sharpe 1.505 (ridge_lo_3) against 0.818 for SPY and 0.838 equal weight (Tables 4, 6).
- **Mechanism**: macro data is steadier than returns, so regimes built on it give cleaner priors for asset returns (p. 2). No economic channel is tested.
- **Where it works best**: long-only versions and the ridge model. Long-short versions are weak: naive_lns_3 Sharpe 0.402, ridge_lns_2 0.666 (Tables 4, 6).
- **Weak spots**: regimes change maximum drawdown insignificantly (p. 17). Against random regimes, naive and BL gain in Sharpe only at the 10% level (Table 3). Plain mean-variance long-only scores 1.104 to 1.129 (Table 5).
- **Main caveats**: no costs, no separate hold-out, many configurations, k and PCA size picked on the full sample. The random-regime control is not described.

Page numbers follow the printed pagination, which equals the PDF page. Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Regimes built on macro data avoid the noise of return-based regimes | None beyond the results below | p. 2 |
| 2 | Regimes change risk and return profiles of assets, so they help allocation | Cited literature (Ang and Bekaert 2004, Guidolin and Timmermann 2007) | p. 1-3 |
| 3 | Regime information improves return generation, not drawdown control | Sharpe, Sortino and % positive improve; MaxDD changes insignificant | p. 17; Table 3 |
| 4 | Regime 0 (outliers) is economic difficulty | Lowest income, sentiment, fed funds rate, highest unemployment (Fig. 4) | p. 9 |
| 5 | Shorts pay only in regime 0 | Long-only beats long-short; the mixed rule is built on this | p. 15 |

**Caveats raised by the authors**: regime labels cannot be absolute given the approximate nature of k-means (p. 10); success is "not universal across all configurations" (p. 20); outperforming benchmarks is a formidable challenge (p. 20).

**Ruled out**: Not addressed.

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | SPY and 9 sector ETFs (XLB, XLE, XLF, XLI, XLK, XLP, XLU, XLV, XLY) | Table 2, p. 16 |
| Period | ETF returns Feb 2000 to Dec 2022; charts start ≈2004 | p. 16; Fig. 10 |
| Macro data | 127 FRED-MD series, group 6 (interest and exchange rates) removed, Dec 1959 to Jan 2023 | p. 7 |
| Signal | Regime probabilities from two-stage k-means, then regime-conditional forecast | p. 4-6, 13-15 |
| Horizon, rebalancing | Monthly, one month ahead | p. 16 |
| Estimation | Fixed 48-month window, walk-forward | p. 16 |
| Sizing | Weights proportional to forecasts of the l best (and worst) ETFs, l = 2, 3, 4 | p. 15 |
| Costs | Not mentioned | whole paper |

**Rule**
- Stage 1: transform each series by its FRED-MD t-code, standardize, PCA to 95% of variance (61 components) (p. 7).
- k-means with L2 distance, k = 2: the smaller cluster is Regime 0, outlier months. On the rest, k-means with cosine distance, k = 5 by the elbow heuristic (p. 5, 7).
- Probability of cluster i from centroid distances: P(Ci) = (1 - di/Σdj) / Σm(1 - dm/Σdj) (Eq. 1, p. 6). Regime 0 weight: -Pmax·log2(1 - P(Regime 0)), then renormalize (Eq. 4, p. 6).
- Transition matrix: counts of regime i to j over occurrences of i (Eq. 5, p. 6). Next-month distribution = current distribution times the matrix (Eq. 7, p. 13).
- Naive forecast: Sharpe ratio of the ETF in past months of the most likely next regime (Eq. 8-10, p. 14).
- Ridge forecast: per regime and ETF, ridge regression of returns on macro features of that regime, averaged with next-month probabilities (Eq. 12-14, p. 14-15).
- Black-Litterman: sample mean and covariance as prior, regime-conditional means as views (Eq. 11, 19, p. 14-16). Tau, the pick matrix and view uncertainty are not given.
- Weights: lns, long the l highest and short the l lowest forecasts; los, the l largest absolute forecasts; lo, the l highest only; mx, los if next regime is 0, else lo. Weight = forecast over sum of absolute forecasts of the chosen set (Eq. 15-18, p. 15).

**Data provenance**: FRED-MD (McCracken and Ng 2016), public, monthly, stamped first day of month (p. 7). Vintage not stated. ETF returns from WRDS, "beginning-of-the-month returns" (p. 16).

## 3. Results

Test type: regime classification is real data, in-sample over the full history (Figs. 2-6). Portfolios are real data, walk-forward with a 48-month window, ex-ante forecasts, but k, the PCA size and l were chosen with the full sample in view. Gross, no cost mentioned.

**Aggregate** (Tables 4 to 6, 2004 to 2022)
- Ridge long-only: Sharpe 1.134 (l = 2), 1.505 (l = 3), 1.490 (l = 4); MaxDD about -4.4; Sortino up to 4.449.
- Naive long-only: Sharpe 0.899 to 1.065; MaxDD -5.9 to -6.7. BL long-only 1.071 to 1.177; MVO long-only 1.104 to 1.129.
- Benchmarks: SPY Sharpe 0.818, MaxDD -33.492; equal weight 0.838, -32.286; both 66.2% positive months.
- Regime vs random regimes (paired t-test, Nemenyi): ridge Sharpe p = 0.004 and 0.000; naive Sharpe 0.082 and Sortino 0.019; BL Sharpe 0.068, % positive 0.003 (Fig. 7-9, Table 3).

**By sub-group**
- Long-short fails: mvo_lns_2 Sharpe -0.516, MaxDD -35.806; bl_lns_3 0.023; naive_lns_3 0.402 (Tables 4, 5).
- Mixed and long-or-short sit between lo and lns (Table 6).
- Regime 0 detected in NBER recessions (Fig. 2, chart only).

**Horizon and parameters**: l = 2, 3 or 4 only. The authors say l = 2 or 3 beats l = 4 (p. 20); see inconsistencies.

**Over time**: Fig. 10 (log scale, 10% volatility scaling): ridge lines end ≈2.0 and SPY ≈1.7. Naive lines peak ≈2018 and fall to ≈1.2 to 1.5 by 2022. Long-short lines drift flat or down to ≈-1.0.

**Link to other strategies**: Not addressed.

**Inconsistencies in the source**
- 746 monthly observations "from 2000 to 2022" (p. 16); Feb 2000 to Dec 2022 is 275 months (computed).
- Equal-weight Sortino 1.445 in Table 4, 1.325 in Tables 5 and 6.
- p. 20: naive_lo_4 has "the lowest maximum drawdown" of naive strategies, -6.719; naive_lo_3 shows -5.859 (Table 4).
- p. 20: ridge_lo_2 has the lowest MaxDD of all, -4.389; ridge_lo_4 shows -4.368 and ridge_lo_3 -4.386 (Table 6).
- p. 20: l = 2 or 3 "consistently outperform" l = 4; naive_lo_4 Sharpe 1.065 beats lo_2 0.981 and lo_3 0.899 (Table 4).
- p. 20: long-only superior to long-short "across all strategies"; naive_lns_3 Sortino 3.533 beats naive_lo_3 2.630 (Table 4).
- Eq. 8 takes the argmax over regimes 1 to r+1, Eq. 14 sums over 1 to r, yet regimes run 0 to r and the mixed rule needs Regime 0 forecasts (p. 14-15).
- Table 3 Panel B is labelled BL random vs not random; Fig. 8 compares MVO with BL (p. 17-18).
- p. 7 sets 61 PCA components; a 48-month window cannot yield 61 components. Whether PCA and clustering run inside the window or on the full sample is not stated.

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Modified k-means probabilities are smoother and more useful than GMM probabilities | p. 8; Fig. 3 (≈0.45 to 0.49 all along, barely moves in recessions) |
| Regimes align with NBER recessions | p. 8; Fig. 2 chart only |
| Regime transitions with zero probability are what a good model should show | p. 10 |
| Stacking L2 then cosine isolates economic panic | p. 9; Fig. 4 |
| Ignoring regimes costs about 2% a year (cited from Tu 2010) | p. 3-4 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | [[Regime probability filter]]: macro regime clustering, PCA, L2 outlier split, cosine k-means, probabilities from centroid distances | technique | signal | Macro data is stabler than returns (p. 2) | p. 5-6 |
| 2 | [[Regime-conditional return forecast]]: next regime distribution times transition matrix, regime-conditional Sharpe or ridge | technique | signal | Uses uncertainty of the current regime (p. 13) | p. 13-15 |
| 3 | [[Long-short portfolio weighting]]: top-l and bottom-l forecast weights (lns, los, lo, mx) | technique | sizing | Shorts only help in regime 0 (p. 15) | p. 15 |
| 4 | Black-Litterman with regime views | technique | sizing | Not argued | p. 15-16 |
| 5 | Random-regime control | principle | evaluation | Tests that regimes carry information | p. 16-17 |

## 6. Regime observations

- Six regimes: difficulty, recovery, expansionary growth, stagflationary pressure, pre-recession, reflationary boom (Table 1, p. 12).
- Most transition mass is on the diagonal: regimes persist (p. 9).
- Shorts pay "substantial returns" in Regime 0 (p. 15).

## 7. Acknowledged limits

- Choice of macro features and of the clustering method left open (p. 24).
- Regime labels approximate (p. 10).

## 8. Not addressed

Transaction costs, slippage, turnover, capacity. A hold-out never touched in design. Real-time FRED-MD vintages and publication lag. How random regimes are drawn and how many times. Number of pairs in the tests. Sensitivity to the 48-month window, k and the PCA threshold. Whether tables are volatility scaled and the unit of MaxDD.
