---
type: reading-note
source: paper
title: Weekly momentum in the commodity futures market
authors: Kwon, Kang, Yun
affiliations: Kwon (University of Strathclyde), Kang and Yun (KAIST)
year: 2019
venue: not stated in the PDF
doi:
pdf: "[[2019 - Kwon Kang Yun - Weekly momentum in the commodity futures market.pdf]]"
version: working paper (the references cite 2019 work as forthcoming)
tier: 1
read: full
tags: [trend, commodities, weekly]
date: 2026-10-24
---

# Weekly momentum in commodities (Kwon, Kang, Yun 2019)

## Summary

- **Finding**: in 32 commodity futures, 1979-2015, last week's return predicts next week's. Long-short quintile: 0.20% a week (t = 4.49), 0.20% after controls (t = 4.30). Gross.
- **Mechanism**: not settled. Speculators chase last week's winners and unwind after two weeks; weekly momentum co-moves with their position changes. Authors say this is not a full explanation.
- **Where it works best**: the 1-week window, after controlling for AVG and CARRY. Unrelated to equity momentum (UMD) and to hedging pressure.
- **Weak spots**: half-yearly and yearly momentums lose significance after controls (t < 1.5). No sector, sub-period or long/short-leg results shown.
- **Main caveats**: no costs, no Sharpe ratio; spanning and sector tests untabulated; text claims about Table 6 contradict the table.

Page numbers follow the PDF (20 pages). The text pages carry no printed number. Values marked ≈ are read from a chart (none used).

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Weekly momentum is specific to commodities | Not significantly related to UMD (0.01, t = 0.99). Monthly, half-yearly, yearly are (t = 2.68, 4.44, 2.02). | p. 6, Table 3A |
| 2 | Hedging pressure does not explain it | Weekly intercept stays significant with HP in the regression (0.14, t = 2.60). The other three intercepts are not (t from 0.57 to 1.21). | p. 7, Table 4 |
| 3 | Speculators chase last week's return | Position change of speculators on past return: 0.49 (j = 0), 0.28 (j = 1), 0.07 (j = 2), then -0.02 to -0.08 for j = 3 to 11. Hedgers show the mirror image. | p. 9, Table 5 |
| 4 | Weekly momentum is tied to speculative activity | ΔDP loads positively on the weekly momentum (0.30, t = 4.83). ΔSP loads negatively (-0.45, t = -2.67). | p. 10-11, Table 6A-B |

The authors write that their results "cannot provide a factor that can fully explain" weekly momentum and only "shed light on its possible source" (p. 3).

**Caveats raised by the authors**
- Non-reportable traders (10-30% of open interest) are left out because their identity is unclear (p. 4, fn 5).
- The link between spreading positions and momentum is "rather unclear" (p. 9).
- The ΔSP coefficients weaken when ΔDP is added; the authors suggest ΔSP and ΔDP are related (p. 10, fn 16).

**Ruled out**
- Carry, for the weekly and monthly momentums: CARRY loadings 0.01 (t = 0.24) and 0.06 (t = 1.08) (Table 2B).
- Equity momentum (UMD) for the weekly one (Table 3).
- Hedging pressure for the weekly one (Table 4).

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | 32 commodity futures: 5 metals, 7 softs, 7 grains, 6 meats, 7 energies. Table 1A lists them. | p. 3, Table 1 |
| Period | January 1979 to June 2015. Start dates per commodity not stated. | p. 3 |
| Signal | Past return over one of four non-overlapping windows: week t-1 (weekly), t-4 to t-2 (monthly), t-26 to t-5 (half-yearly), t-52 to t-27 (yearly). | p. 4 |
| Entry | Long the top quintile, short the bottom quintile. | p. 4, fn 8 |
| Exit | Not stated by the authors. Return is measured in week t. | p. 4 |
| Horizon | One week, implied by the weekly return series. Not stated as a holding rule. | p. 3-4 |
| Sizing | Not stated by the authors (weights inside the quintiles not given). | not given |
| Portfolio | Long-short quintile portfolio per window. | p. 4 |
| Rebalancing | Weekly, implied. | p. 4 |
| Costs | None. Results are gross. | p. 16, Table 2 |
| Data and tools | Datastream daily settlement prices; CFTC Commitments of Traders for positions; UMD from Ken French's website. | p. 3, 6 |

**Rule** (notation of the paper): in week t, rank the commodities on their return over weeks t-k1 to t-k2, buy the top quintile, sell the bottom quintile, and record the week-t return as CMOM(k1,k2). The four portfolios are CMOM(1,1), CMOM(4,2), CMOM(26,5), CMOM(52,27) (p. 4).

**Data provenance**
- Returns: each period holds the nearest contract that does not expire in the next month (p. 3).
- Positions: CFTC groups commercial (hedgers), noncommercial (speculators), non-reportable. Reports are weekly since 1992. Weekly returns are computed on Tuesdays to match the position date (p. 3-4, fn 6).
- Whether Tuesday returns are used for Tables 2-4 as well is not stated.
- Risk factors: AVG is the equal-weighted average excess return of all available commodities. CARRY is long the top backwardation quintile, short the top contango quintile (p. 5). Both follow Bakshi et al. (2019), without their momentum factor (p. 5, fn 9).

## 3. Results

All results below are real data, in-sample, gross of costs. The window choice (four sub-periods of 52 weeks) was set once by the authors and not tuned.

**Aggregate** (Table 2A, mean weekly return in %, t in brackets)

| Momentum | Raw | Intercept after AVG and CARRY |
| --- | --- | --- |
| Weekly CMOM(1,1) | 0.20 (4.49) | 0.20 (4.30) |
| Monthly CMOM(4,2) | 0.16 (2.44) | 0.14 (2.22) |
| Half-yearly CMOM(26,5) | 0.14 (1.76) | 0.06 (0.83) |
| Yearly CMOM(52,27) | 0.23 (3.19) | 0.09 (1.46) |

Computed: 0.20% a week is about 10.4% a year, simple (0.20 x 52). The paper gives no annual figure and no Sharpe ratio.

**By sub-group**
- By sector, long or short leg, or period: Not addressed in the PDF. Sector-momentum and double-sort tests are said to be in an online Supplementary Material, which was not read (p. 5-6, fn 10).
- Commodity summary statistics: Table 1B (weekly average, stdev, skew, kurtosis per commodity). Sector averages of the mean run from 0.01 (softs) to 0.19 (energies). The unit is not stated.

**Horizon and parameters**
- Shorter ranking windows give larger risk-adjusted returns (p. 5).
- CARRY loads on the half-yearly (0.42, t = 6.19) and yearly (0.80, t = 18.65) momentums, not on the weekly one (Table 2B).
- UMD loading: 0.01 weekly, 0.07 monthly, 0.12 half-yearly, 0.05 yearly (Table 3A). Controlled intercepts: 0.19 (t = 4.17), 0.13 (1.92), 0.03 (0.41), 0.08 (1.19) (Table 3B).
- HP loading: 0.09 weekly (t = 3.07), the smallest of the four (Table 4).
- Speculator position change on past return (Table 5): positive for j = 0 to 2, negative from j = 3 on. Hedgers: negative for j = 0 to 2, positive from j = 3 on.

**Over time**
Not addressed. No sub-period, drawdown or cumulative return shown.

**Link to other strategies**
- Equity momentum (UMD): no link for the weekly one (Table 3).
- Carry and hedging pressure: see above.
- Regressing the monthly on the weekly momentum leaves an insignificant intercept (t = -0.40). The weekly one is not spanned by the others. Both untabulated (p. 5).

**Inconsistencies in the source**
- p. 10 says only CMOM(1,1) and CMOM(4,2) load positively on ΔDP. Table 6A also shows CMOM(26,5) at 0.30 (t = 2.90).
- p. 10 says CMOM(52,27) has a significantly negative ΔDP relation. Table 6A gives 0.02 (t = 0.26); Table 6C gives -0.19 (t = -0.21). Neither is significant.
- Table 6C, ΔDP on CMOM(26,5): 0.003 with t = 3.11. The same cell in 6A is 0.30 with t = 2.90. The 0.003 looks like a misprint (computed: it implies a standard error near 0.001, against about 0.1 in neighbouring cells).
- Table 5 caption cites Eq. (3) and Table 6 caption cites Eq. (6). The regressions in the text are Eq. (2) and Eq. (5).
- Table 1 caption says "monthly returns" in one sentence and "weekly returns" in the next. The text says weekly.
- p. 6 calls the monthly intercept significant after controls. Table 3B gives t = 1.92. Loose wording, not a contradiction.

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Weekly momentum "fully spans" monthly momentum | p. 2; test untabulated, p. 5 |
| Weekly momentum is not fully spanned by the others (significant intercepts in all regressions) | p. 5, untabulated |
| Results hold with sector-momentum portfolios and sector double sorts | p. 5-6, fn 10, in the online Supplementary Material |
| The 12-month momentum profit "mainly stems" from the past week's return | Abstract, p. 11 |
| Speculators are momentum traders (prior literature) | p. 8, citations only |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | Split the past 52 weeks into four non-overlapping ranking windows and test each alone (no card: variant inside [[Cross-sectional momentum]]) | technique | signal | Shows the marginal profit of each window, after Novy-Marx (2012) | p. 4, fn 7 |
| 2 | Cross-sectional quintile long-short on past return, one-week window | technique | signal | Not argued | p. 4, fn 8; card [[Cross-sectional momentum]] |
| 3 | Risk-adjust with AVG and CARRY time-series factors | technique | evaluation | Follows Bakshi et al. (2019) | p. 5 |
| 4 | Hedging pressure = minus hedgers' net long over open interest | technique | economic intuition | Tests the hedging-pressure hypothesis | p. 7, Eq. 1 |
| 5 | Fama-MacBeth regression of group position changes on lagged returns | technique | evaluation | Shows who trades the trend and for how long | p. 8-9, Eq. 2 |
| 6 | Speculative-activity factors ΔDP and ΔSP from CFTC positions | technique | economic intuition | Links momentum to speculators, after Bakshi et al. (2019) and Boons and Prado (2019) | p. 9-10, Eq. 3-4 |

## 6. Regime observations

Not addressed. The authors cite Boons and Prado for a view that speculators prefer spreading positions in times of high uncertainty (p. 9); they do not test it by period.

## 7. Acknowledged limits

- No complete explanation of weekly momentum (p. 3, 11).
- The sign of the spreading-position effect is only a guess (p. 9).

## 8. Not addressed

- Transaction costs, slippage, turnover of a weekly strategy.
- Sharpe ratio, volatility, drawdowns, annualised return.
- Weights inside the quintiles, number of commodities available per week, start date of each series.
- Results by sector, by long and short leg, by sub-period, out-of-sample.
- Sample period of the position-based tests (CFTC weekly reports start in 1992, p. 4, fn 6).
- Capacity and market impact.
