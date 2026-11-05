---
type: reading-note
source: paper
title: "Single-Asset Adaptive Leveraged Volatility Control"
authors: Devanathan, Rueter, Boyd, Candès, Hastie, Kochenderfer, Apoorv, Soronow, Zamkovsky
affiliations: Devanathan, Rueter, Boyd, Candès, Hastie, Kochenderfer (BlackRock AI Lab); Apoorv, Soronow, Zamkovsky (BlackRock Index Services)
year: 2026
venue: arXiv 2603.01298v2 (q-fin.PM), 30 March 2026, not peer-reviewed
doi: 
pdf: "[[2026 - Devanathan Rueter Boyd et al - Single-Asset Adaptive Leveraged Volatility Control.pdf]]"
version: arXiv preprint v2, dated April 1, 2026
tier: 2
read: full
tags: [low-vol, equities, daily]
date: 2026-10-25
---

# Single-asset adaptive leveraged volatility control (Devanathan et al. 2026)

## Summary

- **Finding**: a feedback term that corrects the weight with the index's own realized volatility cuts tracking error to 0.4% against 2.3% for the open-loop rule, on IVV 2000-2024, with 5 bp costs.
- **Mechanism**: open-loop rules lag true volatility, so tracking errors persist; feedback on realized index volatility corrects persistent over or under estimation. Not a return mechanism.
- **Where it works best**: IVV: Sharpe 0.42 against 0.31 buy-and-hold and 0.33 open-loop; max drawdown 37.1% against 55.3%. 44 ETFs 2010-2024: tracking error below 0.6%.
- **Weak spots**: turnover 1105% against 93% open-loop; a minority of ETFs lose Kalmar ratio (none below -0.15); the authors say illiquid assets may suit open-loop better.
- **Main caveats**: parameters tuned on IVV 2000-2009, then IVV 2000-2024 reported; ETF cohort filtered on future returns above 5%; cost model is one 5 bp spread; no significance tests.

Page numbers follow the PDF, which has no other pagination (16 pages). Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Open-loop rules built on a variance forecast lag the true volatility and keep a persistent tracking error. | IVV running volatility drifts from the 15% target far outside the Monte Carlo band for open-loop; stays inside it for control. | Fig. 2; p. 2, 8 |
| 2 | Feedback on the index's realized volatility fixes persistent over or under estimation of volatility. | Tracking error 5.2% (IVV), 2.3% (open-loop), 0.4% (control). | Table 1; p. 5, 9 |
| 3 | Volatility clusters, reacts asymmetrically to returns and shifts by regime. | Cited from references, no test in the paper. | p. 2 |

Why the volatility-managed portfolio earns more is not stated by the authors. The paper targets a volatility level, not a return.

**Caveats raised by the authors**
- High gain lowers tracking error but raises turnover (p. 9).
- High turnover suits very liquid assets; for less liquid ones open-loop may be preferable (p. 11).
- Estimates with short halflives are noisy; they recommend halflives of at least 63 days to judge performance (p. 16).
- Prior work finds out-of-sample benefits of open-loop volatility targeting can vanish with costs and rebalancing delays (p. 2).

**Ruled out**: nothing.

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | One risky asset (IVV in the baseline) and cash. Test: 44 ETFs with positive prices throughout 2010-2024 and annualized return above 5%. | p. 3, 7, 10 |
| Period | IVV 8 June 2000 to 31 December 2024. Tuning window 8 June 2000 to 31 December 2009. Test 1 January 2010 to 31 December 2024. | p. 7, 9, 10 |
| Signal | None on direction. Always invested in the risky asset. | p. 3 |
| Entry, exit | Not applicable. | |
| Horizon | Daily rebalancing. | p. 7 |
| Sizing | Weight on the risky asset = min(exp(kappa) x target vol / EWMA vol of the asset, L). Kappa from feedback on index volatility. | p. 5-6 |
| Target and leverage | Target volatility 15% a year. Leverage limit L = 1.5. No short. | p. 7 |
| Portfolio | Risky weight w, cash weight 1 - w; negative cash weight means borrowing. | p. 3 |
| Rebalancing | Every day at the close, same close as the return observed. | p. 7 |
| Costs | 5 bp bid-ask spread on each rebalancing trade. Cash earns the daily Federal Funds Effective Rate; borrowing pays interest on the borrowed cash, rate not stated separately. | p. 3, 7 |
| Data and tools | Close-to-close ETF returns, source not named. | p. 7, 10 |

**Rule**
1. Asset volatility: sigma_k = sqrt of EWMA of squared asset returns, halflife 126 days, beta = exp(-log 2 / h) (Eq. 1, p. 4).
2. Index volatility: same EWMA on the index's own returns (Eq. 2, p. 4).
3. Error: e_k = log(sigma_index_k / sigma_target) (Eq. 3, p. 4).
4. Control: kappa_k = (1 - theta) x clip(-g x e_k, [kappa_min, kappa_max]) + theta x kappa_(k-1), with kappa_0 = 0 (Eq. 6-7, p. 5-6).
5. Weight: w_k = min(exp(kappa_k) x sigma_target / sigma_k, L), cash c_k = 1 - w_k (Eq. 5, p. 5).
6. Index return: r_index_k = r_k x w_(k-1) + r_rf_k x c_(k-1) (p. 3).
7. Open-loop version: w_k = min(sigma_target / sigma_k, L) (Eq. 4, p. 5).
8. Parameters used: g = 55, kappa_min = -1, kappa_max = 1, theta = 0.6; open-loop rule run for the first 10 days before control starts (p. 7). Authors recommend running the open-loop rule until enough history exists (p. 6).

**Data provenance**: IVV is an iShares ETF, close-to-close. No data vendor named. The cash rate is the Fed Funds Effective Rate, daily. Not stated by the authors: adjustments for dividends.

## 3. Results

All results are real ETF data, net of the 5 bp spread and of cash interest as described in section 2, with no other cost. The paper calls the baseline a "simulation" (p. 7).

**Aggregate** (IVV, 2000-2024, in-sample for the tuned parameters; Table 1, p. 9)
- Annualized return: 7.8% IVV, 6.8% open-loop, 8.2% control.
- Annualized volatility: 19.1%, 14.9%, 14.9%.
- Sharpe: 0.31, 0.33, 0.42. Kalmar: 0.14, 0.18, 0.22.
- Maximum drawdown: 55.3%, 38.6%, 37.1%.
- Turnover (sum of absolute weight changes over the period): 0%, 93%, 1105%. Computed: 1105% over about 24.6 years is about 45% a year.
- Volatility tracking error: 5.2%, 2.3%, 0.4%.

**By sub-group** (44 ETFs, 2010-2024, parameters fixed from IVV 2000-2009, out-of-sample in time; Fig. 4-5, p. 10-11)
- Control: tracking error mostly below 0.4%, all below 0.6%. Change in Kalmar vs the asset positive for most, up to 0.25, minority negative, none below -0.15. Turnover 800% to 1800%.
- Open-loop: tracking error 1% to 3%. Change in Kalmar from -0.1 to 0.2, most mass slightly below zero. Turnover 70% to 100%.
- No result by ETF is shown, only histograms. The 44 names include equity, sector, country, IAU (gold) funds. The paper says "commodities" without naming more than IAU.

**Horizon and parameters** (IVV 2000-2009; Fig. 3, p. 9-10)
- Grid: g in {0, e^0, e^0.5, ..., e^5}, theta in {0, 0.1, ..., 0.9}.
- Tracking error 0.29% to 2.52%, falls with g, little change with theta.
- Change in Kalmar vs IVV from -0.056 to +0.066, positive for nearly all cells. Ridge between (148, 0.8) and (55, 0.6).
- Turnover 108% to 3558%, rises with g, falls with theta.
- Halflife of the volatility estimate: only 126 days used (21 and 126 shown only for estimator noise, Fig. 7).

**Over time**: Fig. 2 (p. 8): IVV running volatility ≈ 40% after 2008-2009 and ≈ 35% in 2020; open-loop ≈ 25% at the peaks; control stays close to 15% with dips to ≈ 11-12%. Fig. 1 (p. 8, log-type axis, cumulative value from 1): control ends ≈ 7, IVV ≈ 6, open-loop ≈ 4 to 5 (values ≈). Control leads from about 2009. No year-by-year table.

**Link to other strategies**: compared with open-loop volatility targeting after Moreira and Muir (p. 2). No other factor comparison.

**Inconsistencies in the source**
- The abstract says the method is shown "in simulation" (p. 1); the data are real ETF returns, with an in-sample tuning window inside the reported 2000-2024 period.
- Figure 1 (p. 8) has an unevenly spaced vertical axis (0.5 to 8), a logarithmic scale, labelled "Cumulative Return". No numeric contradiction with Table 1.

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Open-loop approaches have turnover, leverage spikes and sensitivity to the estimator ("highlight practical issues") | p. 2 |
| Robustness across "a wide range" of gain and smoothing values | p. 3, 9 |
| Log-space control suits volatility because it moves multiplicatively (2X and X/2 equally likely) | p. 5 |
| The controller generalizes beyond the tuning asset | p. 3, 10 |
| The high turnover is "appropriate" where rebalancing costs are minimal | p. 11 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | [[Volatility targeting]], open-loop: w = min(target / EWMA vol, L), halflife 126 | technique | sizing | Natural way to set expected index variance to the target | Eq. 4; p. 5 |
| 2 | [[Volatility targeting]], feedback variant: scale the target by exp(kappa), kappa smoothed and clipped from log error of realized index volatility | technique | sizing | Corrects persistent over or under estimation of volatility | Eq. 3, 5-7; p. 5-6 |
| 3 | Leverage cap L = 1.5, weight bounded to [0, L] (inside [[Volatility targeting]], no own card) | principle | risk | Constraint of index construction | p. 3 |
| 4 | Monte Carlo band for the running volatility estimate of an asset with true volatility at target | technique | evaluation | Shows how much deviation a perfect tracker would show | App. A; p. 13 |
| 5 | Volatility tracking error: mean absolute gap between running volatility and target | technique | evaluation | Measures the control objective | p. 4, 7 |

## 6. Regime observations

- IVV volatility spikes in 2008-2009 and 2020 are where open-loop volatility departs most from the target (Fig. 2, p. 8). No regime test.

## 7. Acknowledged limits

- Turnover cost of high gain (p. 9, 11).
- Open-loop may suit less liquid assets (p. 11).
- Short-halflife volatility estimates are noisy (p. 16).
- The method needs some index history before control starts (p. 6).

## 8. Not addressed

- Significance tests or confidence intervals on Sharpe, Kalmar or drawdown.
- Costs beyond one 5 bp spread; borrowing spread above the Fed Funds rate; financing cost shown separately.
- Dividends, taxes, capacity, borrowing availability.
- Leverage actually used: time spent at the cap of 1.5, distribution of weights.
- Results on bonds, FX or crypto. Results by ETF.
- Any comparison of control against buy-and-hold at equal volatility or equal leverage, or a plain constant-leverage portfolio.
- Sensitivity to the volatility halflife and the target level.
- Selection effect of the cohort filter (annualized return above 5% over 2010-2024).
