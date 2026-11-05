---
type: reading-note
source: paper
title: "Volatility Targeting Is Trendy: How Trend Following Explains Alpha in Volatility-Managed Strategies"
authors: Hood, Raughtigan
affiliations: Parametric (both authors; Hood in Minneapolis, Raughtigan in Boston)
year: 2024
venue: Working paper, current draft dated 11/29/2024
doi: Not stated
pdf: "[[2024 - Hood Raughtigan - Volatility Targeting Is Trendy How Trend Following Explains Alpha in Volatility-Managed Strategies.pdf]]"
version: working paper draft 11/29/2024
tier: 1
read: full
tags: [trend, multi-asset, daily]
date: 2026-10-25
---

# Volatility targeting is trendy (Hood, Raughtigan 2024)

## Summary

- **Finding**: US market factor 1927-2023: volatility targeting alpha over buy-and-hold is 3.07% a year; with a simple trend control it falls to 1.25%, not significant (Exhibit 4).
- **Mechanism (authors)**: the equity leverage effect (returns and volatility move oppositely) makes a volatility-targeted position and a trend position point the same way, so the targeting book holds trend exposure.
- **Where it works best**: equities only. Trend loading 0.35 for the equity panel against 0.04 to 0.08 elsewhere; equity alpha 1.57% falls to 0.65% (Exhibit 8).
- **Weak spots**: commodities, bonds and currencies show no trend loading and no alpha to explain; currency alpha is negative; no single-asset alpha is significant after trend.
- **Main caveats**: no out-of-sample test; one trend rule (1, 3, 12 months); broad sample 2000-2023 has no significant alpha; no proof of the link.

Page numbers follow the PDF, which matches the printed page numbers. Values marked ≈ are read from a chart. All tests are real data, in-sample, net of a 2 bp cost per unit traded unless stated.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Vol targeting is underweight when volatility is high, and high volatility comes with falling prices in equities (leverage effect), so its positions line up with trend positions | Mkt-Rf leverage effect -0.31. Average trailing return ≈-5% where the position is below 0.75, ≈+4% to +6% where it is above 1.0 | Exhibit 4, 5; p. 10-12 |
| 2 | Where return direction and magnitude are not negatively related, the two strategies are not linked | Trend beta against leverage effect across 50 assets: every equity beta above the highest non-equity beta (WTI crude); S&P 500 future alpha 2.55% falls to 0.62%, 10-year bond future alpha unchanged | Exhibit 7, D.1; p. 14 |
| 3 | The alpha is paid because trend has a positive risk premium | Cited (Moskowitz 2012, Hurst 2013, 2017), not tested here. Own result: simple trend Sharpe 0.37 on Mkt-Rf | p. 3; Exhibit 1B |
| 4 | Equity leverage effect comes from default risk rising as prices fall | Cited (Black 1976, Geske 1979) | fn 11, p. 10 |

**Caveats raised by the authors**
- The exact mathematical link is highly non-linear and its proof is "beyond the scope" (p. 10).
- Trend does not remove all outperformance: vol targeting still beats buy-and-hold (p. 9).
- Broad-sample alphas are not significant, even in panels; only 3 of 50 single-asset alphas have |t| above 2, and none keeps it after trend (Exhibit 6 notes; p. 16).
- A single-asset trend rule gives little return and noisy estimates; an investor wanting trend should hold a diversified trend fund (p. 16).
- Negative currency alpha (-77 bp on average) is "a bit of a puzzle" (fn 19). Energies load on trend like equities (fn 20).

**Ruled out**
- Exposure to short volatility: an earlier paper found about zero loading (Hood 2019, fn 13). Not retested.

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | Long history: Fama-French Mkt-Rf, also SMB, HML, MOM. Broad set: 50 futures, 25 commodity, 6 bond, 6 currency, equity indexes (text says 14; 13 are named in Exhibits 6 and E.1) | p. 4, 12; Exhibit 6, E.1 |
| Period | Mkt-Rf 5/4/1927 to 12/31/2023. Futures from April 2001 (first 12 months kept for signals) to end 2023 | p. 4, 12; fn 16 |
| Signal (vol targeting) | Buy-and-hold return scaled by the inverse of trailing 3-month volatility | Exhibit 1A |
| Signal (simple trend) | Average of the sign of the trailing 1-, 3-, 12-month returns: +1, +1/3, -1/3 or -1 of notional | p. 6; Exhibit 1A |
| Entry, exit | 1-day lag: volatility through close t sizes the position at close t+1, first return marked t+2 | p. 4 |
| Sizing | Target = full-period buy-and-hold volatility (17.2% on Mkt-Rf). No leverage cap in the main version. Mean leverage 1.49x, max 5.18x (1964), min 0.24x (2008); above 2.5x 5.5% of the time | p. 4-6; fn 4, 7; Exhibit 2 |
| Rebalancing | Not stated by the authors. Statistics use daily returns | Exhibit 1B notes |
| Costs | 2 bp per unit of notional traded; 0 to 10 bp tested | p. 4; App. A |
| Data and tools | Single-series regressions: OLS, Newey-West, 10 lags. Panels: time-clustered standard errors (Rogers 1993) | fn 10; p. 15 |

**Rule**: trendPosition(k) is about the sign of the sum of the last k returns; volPosition(k) is about target / sqrt(mean of squared last k returns) (p. 10, simplified forms). Test: R(vol targeting) = a + b R(buy-and-hold) + c R(trend) + e, alpha a annualised (Exhibit 4).

**Data provenance**
- Equity factors: Kenneth French's website, excess of the 3-month T-bill (p. 4, 12).
- Futures: Refinitiv prices, one rolled series per asset. Front month held to 7 days before expiry, rolled at that close. Commodities use only contracts in the BCOM roll schedule (fn 17). Futures returns carry financing implicitly (fn 15).
- The authors differ from Moreira and Muir: inverse volatility, not variance; not monthly rebalancing (implied by fn 5; their own frequency is not stated); target set on full-period buy-and-hold volatility, not ex-post scaling (fn 5). They report that the original method gives the same results (fn 5).

## 3. Results

**Aggregate** (Mkt-Rf 1927-2023, net of 2 bp; Exhibit 1B, 4)
- Return, volatility, Sharpe: buy-and-hold 7.6%, 17.2%, 0.44; vol targeting 10.2%, 18.7%, 0.54; trend 4.9%, 13.2%, 0.37.
- Skewness -0.2 against -0.9 for vol targeting. Excess kurtosis 16.4 against 8.5. Rolling 3-month volatility error from target 9.3% against 4.5%.
- Regression on buy-and-hold alone: beta 0.94, alpha 3.07% (t 2.9), adjusted R² 0.75.
- With trend: trend beta 0.30 (t 12.0), alpha 1.25% (t 1.3), R² 0.79. Alpha falls 59%.
- Leverage caps 1x, 1.5x, 2.5x, none: Sharpe 0.50, 0.53, 0.55, 0.54; return 6.7%, 8.9%, 10.2%, 10.2% (Exhibit 3A).

**By sub-group**
- Equity factors, alpha before and after trend (Exhibit B.2): SMB -0.43% to -0.44%, HML 1.82% to 1.80%, MOM 9.30% to 9.16%. Trend betas 0.00, 0.00 and 0.20 for SMB, HML, MOM.
- Panels 2000-2023 (Exhibit 8): equities alpha 1.57% (t 1.0) to 0.65% (t 0.5), trend beta 0.35. Bonds 0.22% to 0.17%, beta 0.08. Currencies -0.87% to -0.91%, beta 0.08. Commodities -0.11% to -0.21%, beta 0.04. All assets 0.23% to 0.04%, beta 0.10.
- Single assets: equity alpha falls 65% on average; other assets mostly unchanged (Exhibit 6; p. 13). Commodities: 15 of 16 with negative leverage effect have a positive trend beta, 7 of 9 with positive leverage effect have a negative one (p. 14).
- Average leverage effect by panel: equities -0.31, commodities -0.07, bonds -0.03, currencies -0.16, all -0.14 (Exhibit 8).

**Horizon and parameters** (Exhibit C.1, C.2)
- Mkt-Rf alpha reduction by trend rule: simple 59%, CTAmom (weights approximated from Hamill 2016) 60%, 1-month 21%, 3-month 40%, 6-month 49%, 9-month 40%, 12-month 39%. Only the 1-month rule leaves alpha significant.
- Equity panel 2000-2023: simple 59%, CTAmom 57%, 1-month 10%, 3-month 17%, 6, 9, 12-month 103%, 91%, 91%.
- Costs 0 to 10 bp: alpha before trend 3.17% to 2.68%, after 1.21% to 1.39%; trend Sharpe falls from 0.40 to 0.24 (Exhibit A.1, A.2).

**Over time**: not addressed beyond the full sample.

**Link to other strategies**: trend is the only control tested; Fama-French SMB and HML are cited as not explaining the alpha (Moreira and Muir, p. 4).

**Inconsistencies in the source**
- Key findings, abstract and conclusion say trend absorbs "around 2/3" of the alpha. The tables give 59% (Exhibit 4, C.1, equity panel in C.2); 65% is the single-asset average (p. 13).
- Equity contracts: "14 global equity index futures" (p. 1, 16) against 13 equity names in Exhibits 6 and E.1 (computed count).
- Appendix C caption: 3 to 12-month rules reduce alpha by "40% to 50%"; the table gives 39% to 49%.

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Results are robust to the trend model used | fn 6 (Appendix C shows only Mkt-Rf and four panels) |
| Original Moreira-Muir method gives the same results as theirs | fn 5 |
| 21 lags in place of 10 change standard errors only slightly | fn 10 |
| Vol targeting mainly helps through the shape of returns (volatility of volatility, kurtosis), not through return | p. 16 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | Volatility targeting on trailing 3-month volatility, target equal to full-period volatility, 1-day lag, optional leverage cap | technique | sizing | Practitioner version, easy to replicate [[Volatility targeting]] | p. 4-8; fn 2, 5 |
| 2 | Simple trend: average sign of 1-, 3-, 12-month returns | technique | signal | After Hurst 2013 [[Time-series momentum signal]] | p. 6 |
| 3 | Regress the managed return on buy-and-hold and a trend twin, read the alpha change | technique | evaluation | Tests whether alpha is trend exposure [[Trend-adjusted alpha]] | p. 8-9 |
| 4 | Leverage effect: correlation of 1-month return with 1-month change in the volatility estimate | technique | evaluation | Predicts the trend loading [[Volatility scaling momentum check]] | p. 10; Exhibit 4 |
| 5 | Average trailing return by volatility-targeting position bucket | technique | evaluation | Shows the position link [[Volatility scaling momentum check]] | p. 11-12 |
| 6 | Rolling 3-month volatility error from target | technique | evaluation | Measures how well risk is held | Exhibit 1B |

## 6. Regime observations

- Vol targeting cut leverage to 0.24x in 2008 and ran 5.18x in 1964 (p. 6). No regime analysis of alpha.

## 7. Acknowledged limits

- Short broad sample: the investment horizon of a targeting investor is shorter than the sample, so alphas are not significant (p. 16).
- Volatility estimation, leverage access and costs are outside scope; they keep simple, replicable rules (fn 2).
- Target volatility needs the full-period volatility in advance; the authors say it affects only beta size, not t-stats (fn 4).

## 8. Not addressed

- Out-of-sample or real-time use of the trend control.
- Costs of leverage in the Fama-French sections (excess returns of the factor; no borrowing spread).
- Rebalancing frequency of both rules.
- Statistical test that the alpha reductions differ from zero.
- Capacity, drawdowns, subsample stability.
