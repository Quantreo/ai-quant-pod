---
type: reading-note
source: paper
title: An Update on Sector Rotation in the "Sell in May and Go Away" Strategy
authors: Dolvin, Foltice
affiliations: Butler University
year: 2024
venue: Journal of Finance Issues, Vol 22, No. 3, pp. 50-61
doi:
pdf: "[[2024 - Dolvin Foltice - Update on Sector Rotation in the Sell in May and Go Away Strategy.pdf]]"
version: published
tier: 1
read: full
tags: [seasonality-flows, equities, monthly]
date: 2026-10-25
---

# Sell in May with sector rotation (Dolvin and Foltice 2024)

## Summary

- **Finding**: long the S&P 500 from Nov to Apr and in the risk-free asset May to Oct earns a Fama-French 5-factor alpha of 0.31% a month, 1993-2023, gross (Table 3).
- **Mechanism**: Not stated by the authors. They cite seasonal affective disorder and vacations, and say these lack support as a full explanation (p. 51).
- **Where it works best**: the long-short version, long cyclical and short defensive sectors Nov to Apr and the reverse May to Oct. Alpha 0.37 to 0.50 a month, beta about 0 (Table 7).
- **Weak spots**: post-2008 base alpha 0.25 (p = .26). Long-only rotation adds no alpha over the base rule. Long-short alphas are not significant in either subperiod (Tables 3, 6, 7).
- **Main caveats**: no transaction, borrow or short-sale cost anywhere. Sector groups differ by source, none chosen by the authors. All in-sample.

Page numbers follow the journal pagination (50 to 61). Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Average market return is higher in Nov-Apr than in May-Oct. | S&P 500, 1993-2023: 1.23% vs 0.57% a month. | p. 53 |
| 2 | Cyclical sectors do better in strong market periods, defensive sectors in weak ones. Attributed to Doeswijk (2008). | Cited, not shown. Tested in the paper's own rotation strategies. | p. 51, 56 |
| 3 | Explanations in the literature: seasonal affective disorder, vacation timing. | Cited only. | p. 51 |

**Caveats raised by the authors**
- Anomalies may be data mined or confined to one period (p. 50).
- The effect has weakened in recent years (alpha lower and less significant) (p. 55).
- Peloton uses proprietary timing and rotation, so the Peloton column is only a high-level view (p. 58).

**Ruled out**
- Sector rotation without shorting does not beat the base rule (p. 58).
- Re-entering in October instead of November does not help (Table 8, p. 59-60).
- Adding the Carhart momentum factor changes little (unreported, p. 60).

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | S&P 500 and its sectors. Cyclical: Energy, Discretionary, Industrials, Materials (Technology for Pacer). Defensive: Staples, Utilities, Healthcare (Technology for Peloton). Communications, Financials, Real Estate excluded. | Table 1, p. 52 |
| Period | Jan 1993 to Dec 2023. Subperiods 1993-2007 and 2009-2023, 2008 left out. | p. 52-53 |
| Signal | Calendar month: Nov-Apr vs May-Oct. | p. 53-54 |
| Entry / exit | Switch on the first day of the month in the rule; not stated how. | Not stated |
| Horizon | Six months per leg. | p. 54 |
| Sizing | Equal weight inside each sector group (p. 56). Leg sizes of the long-short: not stated. | p. 56 |
| Rebalancing | Monthly returns, switch twice a year. | p. 54 |
| Costs | None. ETF expense ratios named only in the robustness check. | p. 60 |
| Data | Monthly index returns from YCharts, S&P 500 and its sectors. Sector definitions follow State Street sector ETFs. | p. 52, 56 |

Sector groups by source (Table 1): Doeswijk cyclical Energy, Discretionary, Industrials, Materials; defensive Staples, Utilities, Healthcare. Pacer cyclical Discretionary, Industrials, Materials, Technology; defensive Staples, Healthcare. Peloton: Doeswijk's cyclicals; defensive Staples, Utilities, Healthcare, Technology.

**Rule**
- Base: long S&P 500 in Nov-Apr, risk-free asset in May-Oct (p. 54).
- Rotation: long cyclicals Nov-Apr, long defensives May-Oct, fully invested (p. 56).
- Long-short: Nov-Apr long cyclicals and short defensives; May-Oct long defensives and short cyclicals (p. 58).
- October trigger: cyclicals Oct-Apr, defensives May-Sep (p. 59).

**Data provenance**
- Index returns, not traded ETF prices, as far as the text says: YCharts index returns (p. 52). The sector definitions come from the ETF segmentation (p. 56). Which series is traded is not stated.
- Factors and risk-free rate: Ken French's website (p. 55).
- Start date set at the first trading day of SPY, 1993 (p. 52-53).

## 3. Results

**Aggregate** (real data, in-sample, gross, no costs)
- S&P 500, 1993-2023: mean 0.90% a month, deviation 4.32, Sharpe 0.21 (Table 2).
- Base rule: mean 0.90, deviation 3.52, Sharpe 0.26, Sortino 0.39 (Table 2). Sharpe is the mean over the deviation, no risk-free subtracted (p. 54).
- Base rule alpha 0.31 (p = .032), market beta 0.50. The authors state 0.31 a month is 3.72% a year, gross (Table 3, p. 55).
- Long-only rotation, 1993-2023: gross 1.16 to 1.22, premium over S&P 0.26 to 0.32. Alpha 0.24 to 0.32, beta 0.86 to 0.94 (Tables 4, 5).
- Long-short: gross 0.52 to 0.55, premium -0.35 to -0.39. Alpha 0.37 to 0.50, beta -0.05 to 0 (Table 7).

**By sub-group**
- Pacer: highest long-only alpha, 0.32 (p = .008) (Table 5). Doeswijk: lowest, 0.24 (p = .044) (Table 5).
- Long-short alpha: Pacer 0.50, Doeswijk 0.49, Peloton 0.37, all significant over the full period (Table 7B).

**Horizon and parameters**
- October re-entry: gross 1.13 to 1.20, alpha 0.13 to 0.26, lower than the November rule for each definition (Table 8).
- S&P 500 mean monthly return, Nov-Apr minus May-Oct:  0.66 (full), 0.53 (1993-2007), 0.66 as printed for 2009-2023 (p. 53).

**Over time**
- Base alpha: 0.32 in 1993-2007 (p = .091), 0.25 in 2009-2023 (p = .26) (Table 3).
- Base rule 2009-2023: mean 0.90 vs 1.19 for the S&P 500, Sharpe 0.22 vs 0.27 (Table 2).
- Rotation premium 2009-2023: 0.07 to 0.17, none significant. 1993-2007: 0.35 to 0.42 (Table 4).
- Long-short alpha 2009-2023: 0.34 to 0.46, none significant. 1993-2007: 0.19 to 0.55, none significant (Table 7B).
- 2008 alone, unreported: the Nov-Apr minus May-Oct gap is 3.55% a month (p. 54).
- Monthly chart: Nov is the highest bar in 1993-2023 (≈2.4%) and 2009-2023 (≈3.3%). October is high in all three (≈2.5% in 1993-2007). September is negative in two of three. July in 2009-2023 is ≈3.4% (Figure 1, p. 53-54).

**Link to other strategies**
- Controls: market, SMB, HML, RMW, CMA. Base rule loads on HML (0.31) and CMA (-0.17) (Table 3).
- Long-only rotation loads on RMW (0.15 to 0.19) (Table 5).
- Long-short beta about 0 (Table 7B).

**Inconsistencies in the source**
- 2009-2023 gap: 1.50 minus 0.89 is 0.61, the text says 0.66 (p. 53).
- Table 3 subperiod columns (1993-2007 and 2009-2023, 15 years each) show n = 372, the full-period count. Same in Table 5 (p. 56, 57).
- Text says the sector rotation alphas are "at the same level or lower" than the base 0.31 (p. 58). Pacer is 0.32 for the full period and 0.40 against 0.32 in 1993-2007 (Tables 3, 6).
- Text says the long-short alpha is "positive and significant across most time periods" (p. 59). Only the three full-period alphas are significant; none of the six subperiod alphas is (Table 7B).
- Text says the premium is significant for all strategies in 1993-2007 (p. 56). Doeswijk is p = .064 (Table 4B).
- The text cites "column 4 in Table 3" (p. 58). Table 3 has three columns. The base-rule alpha is column 1.
- The text describes Table 3 as covering "1992-2023" (p. 55), elsewhere 1993-2023.

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Results unchanged with the momentum factor added. | p. 60 |
| Cyclical only (May-Nov) or defensive only (May-Oct) variants have generally negative alphas. | p. 60 |
| Results unchanged with IVV and VOO instead of SPY, apart from expense ratios. | p. 60 |
| 2008 alone favours the rule by 3.55% a month. | p. 54 |
| Long-short sector rotation is best placed in a market-neutral fund structure. | p. 59 |
| Adding leverage to the base rule to match the rotation's beta would give a higher alpha. | p. 58 |
| Rule works in 36 of 37 developed markets and in futures and ESG indices (other authors, not tested). | p. 51 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | Hold the equity index Nov-Apr, risk-free May-Oct, [[Calendar seasonality signal]] | technique | signal | Documented seasonal pattern (Bouman 2002) | p. 54 |
| 2 | Hold cyclical sectors Nov-Apr, defensive sectors May-Oct, optionally short the other group, [[Seasonal sector rotation]] | technique | signal | Cyclicals do better in strong periods (Doeswijk 2008) | p. 56, 58 |
| 3 | Five-factor alpha of the strategy | principle | diagnostic | Control for known factors | p. 55 |
| 4 | Leave 2008 out of the subperiod split | principle | evaluation | Unusual year, would skew either half | p. 53 |
| 5 | Re-enter in October | technique | signal | Chart shows October high | p. 59 |

## 6. Regime observations

- Post-2008 the base rule trails the S&P 500 in mean and Sharpe (Table 2).
- The authors call 2008 an unusual year (p. 53).

## 7. Acknowledged limits

- Risk of data mining in calendar effects (p. 50).
- The effect appears weaker in recent years (p. 55).
- High-level view of Peloton, which uses proprietary timing (p. 58).

## 8. Not addressed

- Transaction costs, bid-ask, borrow cost, short-sale constraints, taxes.
- Out-of-sample test: no period is held out, and the rule was published before the sample.
- How sector returns are built (index or ETF, cap or equal weight) and how the long-short legs are sized.
- Why the sector groups are chosen as they are; the three lists were taken, not tested.
- Capacity, drawdowns, and results outside the US.
