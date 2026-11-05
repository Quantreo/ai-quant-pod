---
type: reading-note
source: paper
title: Relative and Absolute Momentum in Times of Rising/Low Yields, Bold Asset Allocation (BAA)
authors: Keller
affiliations: Not stated in the PDF
year: 2022
venue: SSRN working paper 4166845, v0.981, 18 July 2022
doi: SSRN 4166845
pdf: "[[2022 - Keller - Relative and Absolute Momentum in Times of Rising Low Yields Bold Asset Allocation (BAA).pdf]]"
version: working paper v0.981
tier: 1
read: full
tags: [trend, multi-asset, monthly]
date: 2026-10-25
---

# Bold Asset Allocation, BAA (Keller 2022)

## Summary

- **Finding**: Monthly ETF rotation, Dec 1970 to Jun 2022. BAA-G4: 21.0% a year, max monthly drawdown 14.6%, Sharpe 1.21; 60/40 benchmark 9.5% and 29.5% (p. 7). Costs 0.1% one way.
- **Mechanism**: Not stated by the authors. They describe the design (fast canary crash protection, bonds plus commodities as defensive assets) without an economic argument.
- **Where it works best**: Last 20 years (Jun 2002 to Jun 2022): BAA-G4 16.7%, drawdown 9.5%, against 7.6% for 60/40 (p. 7, Fig 6).
- **Weak spots**: Last decade (Jun 2012 to Jun 2022) is the weakest: 6.6% to 10.9% by variant. BAA-SPY earns less than SPY there (10.1% vs 12.6%) (Fig 11-12).
- **Main caveats**: The reported "out-of-sample" period is not a hold-out. Three choices are declared in-sample optimal. Proxy returns before the ETFs existed (p. 3, 6, 10).

Page numbers follow the PDF, which equals the printed number. Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Trend following (absolute momentum) limits drawdowns, so it is called crash protection | Fig 11 vs 12: max drawdown 16.2% for BAA-SPY against 50.8% for SPY | p. 1, 9-10 |
| 2 | Switching on one bad canary asset (B=1) protects earlier than the usual rule, which switches only when most offensive assets are bad | Example: Top3 of 12 assets switches only when at least 10 are bad | p. 1-2 |
| 3 | DBC and TIP in the defensive universe give a safe haven for low or rising yields and inflation | In-sample optimal on K/IS (note 8); the 2022 first half: 6.4% against about -16% for 60/40 | p. 2, 4, 5, 7 |
| 4 | Defensive mode is similar across all BAA variants (equal R and V) | Fig 3, 6, 9, 10 | p. 9 |

**Caveats raised by the authors**: BAA-G4 may be "too concentrated" with one offensive asset, and BAA-G12 "very diversified" (p. 8). The slow filters are too slow for the protective role (p. 11).

**Ruled out**: Not addressed.

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | 17 ETFs: 7 stocks (SPY, QQQ, IWM, VGK, EWJ, VWO, VEA), 3 alts (VNQ, DBC, GLD), 7 bonds (BIL, IEF, TLT, LQD, HYG, TIP, BND). Three universes: offensive, defensive, protective (canary) | p. 3 |
| Offensive | BAA-G12: SPY, QQQ, IWM, VGK, EWJ, VWO, VNQ, DBC, GLD, TLT, HYG, LQD (Top6). BAA-G4: QQQ, VWO, VEA, BND (Top1) | Fig 3, 6 |
| Defensive | TIP, DBC, BIL, IEF, TLT, LQD, BND (HYG excluded); Top3 | p. 4, Fig 3 |
| Canary | SPY, VWO, VEA, BND | p. 4, Fig 3 |
| Signal, canary | Absolute momentum 13612W; switch to defensive if at least one canary asset is negative (B=1) | p. 4, 12 |
| Signal, selection | Relative momentum p(t)/SMA(12) - 1 (SMA over 13 month-end prices); no absolute filter on offensive picks | p. 3-4, 12 |
| Defensive filter | Defensive picks with momentum below BIL are replaced by BIL | p. 4, 12 |
| Sizing | Equal weight 1/TopX in the active universe, fully invested | p. 12 |
| Rebalancing | Monthly, the whole portfolio, at the close of the last trading day | p. 12 |
| Costs | TC 0.1% one way, listed as a parameter of every strategy | p. 5, Fig 3 |
| Period | Dec 1970 to Jun 2022 (data from Dec 1969, one year of lag) | p. 3 |

**Rule**: at month-end t, relative momentum = p(t)/mean(p(t..t-12)) - 1. Canary momentum 13612W = 12·RET(1) + 4·RET(3) + 2·RET(6) + 1·RET(12) (p. 4, note 7). If any canary asset has 13612W below 0, hold the Top3 defensive assets by relative momentum, 1/3 each, each replaced by BIL if its momentum is below BIL's. Else hold the TopX offensive assets by relative momentum, 1/X each. Positions held to the next month-end (p. 12). Signal and trade are on the same close.

**Parameters printed**: NO, ND, NP, LO, LD, LP, B, TO, TD, TC, ten values per model (Fig 3).

**Data provenance**: monthly total return proxies from Dec 1969 for the 17 ETFs. The construction is in Appendix A of Keller 2016 (PAA), not in this paper and not read (p. 3, fn 4).

## 3. Results

All real data (including proxy series), in-sample or labelled OS by the authors. R is CAGR, D is max monthly drawdown. The text does not say that R is net of TC; TC is listed as a parameter (p. 5).

**Aggregate** (FS, Dec 1970 to Jun 2022, Fig 15)
- BAA-G12/T6: R 14.6%, D 8.7%, V 8.5%, Sharpe 1.19.
- BAA-G4/T1: R 21.0%, D 14.6%, V 13.6%, Sharpe 1.21.
- BAA-G12/T3: R 16.4%, D 11.4%. BAA-G4/T2: R 17.7%, D 12.7%, Sharpe 1.25.
- 60/40 (SPY/IEF): R 9.5%, D 29.5% (p. 5).
- Turnover one-sided 472% (G12/T6) to 523% (G4/T1); 6.6 to 8.2 trading months a year; defensive 57.2% of months (Fig 3, 6).
- Cost drag at 0.1% one way: about 0.5% a year (computed from turnover).

**By sub-group**
- Periods: IS1 Dec 70 to Dec 80, IS2 Jun 12 to Jun 22, OS Dec 80 to Jun 12, RS Jun 02 to Jun 22.
- G4/T1 R: IS1 25.0%, OS 22.8%, RS 16.7%, IS2 10.9%. G12/T6 R: IS1 19.2%, OS 15.3%, RS 12.2%, IS2 7.8% (Fig 3, 6).
- G12/T6 and G12/T3 are below 60/40 in IS2 on return: 7.8% and 6.6% against 8.8% (computed from Fig 3, 9).
- BAA-SPY (Fig 11), FS: R 11.4%, D 16.2%, Sharpe 0.72. IS1: R 11.3%, D 12.6%, Sharpe 0.42. SPY alone (Fig 12): R 10.4%, D 50.8%.
- SMA10 on SPY switching to IEF: R 11.8%, D 23.3% on FS (fn 11, p. 9).

**Horizon and parameters**
- Fig 13 (G12) and Fig 14 (G4): K/FS over six filters for offensive/defensive and six for protective, 36 cells each (p. 11).
- G12: best cell SMA(12) with 13612W, K 11.6%. RET(12) as selection filter is the worst, 5.0% to 6.7%.
- G4: best cell SMA(9) with 13612W, 12.6%; the paper's choice SMA(12) gives 12.3%. All 18 cells with a protective SMA(9), SMA(12) or RET(12) show 0.0% (K is 0 when D exceeds 25%).
- Varying the number of offensive picks (T6 to T3, T1 to T2) lowers R and D together (Fig 15).

**Over time**
- Fig 5, 8: monthly drawdowns of BAA stay within about -15% ≈ against about -29% for 60/40 in 2008 (≈ charts).
- Fig 4: BAA-G12 relative to 60/40 is ≈ flat to lower in the 1990s and the last decade (p. 6).
- Equity charts are on a log scale (Fig 4, 7).

**Link to other strategies**: builds on PAA (Keller 2016), VAA (2017), DAA (2018). PAA-G12 for comparison: R 12.1%, D 11.2%, turnover 284% (Fig 1).

**Inconsistencies in the source**
- 60/40 YTD 2022 is -16% on p. 5 and -15% on p. 7.
- p. 8 says only TO changes in the T3 and T2 variants and all universes stay constant; Fig 10 (G4/T2) lists ND=9 with BIL2 and BIL3, against ND=7 elsewhere. No reason given.
- p. 10 says the two momentum filters were not tuned; note 6 and note 12 say the pair is in-sample optimal on K/IS.

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Robustness of the results to the choices of TO and universe, called "robust" | p. 10 |
| Momentum deviations "nearly flat around the optimum" | p. 11 |
| ">= 20% return with <= 15% drawdown" holds only for the aggressive G4/T1; T6 gives 14.6% | p. 1, 5 |
| 13612W weighting and K formula chosen "elsewhere" (Keller 2017, 2018, TrendXplorer) | p. 4, notes 7, 9 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | Canary universe: switch the whole portfolio to defensive if any of 4 protective assets has negative absolute momentum (B=1) ([[Canary universe switch]]) | technique | signal | Faster crash protection than per-asset absolute momentum | p. 2, 4, 12 |
| 2 | Defensive mode: Top3 defensive assets by relative momentum, those below BIL replaced by BIL ([[Canary universe switch]]) | technique | universe | Enriches the defensive side beyond cash | p. 4 |
| 3 | 13612W: weighted 1, 3, 6, 12-month returns, weights 12, 4, 2, 1 ([[Time-series momentum signal]]) | technique | signal | Fast filter for the canary role | p. 4, note 7 |
| 4 | Relative momentum p/SMA(12) - 1, Top-N equal weight, rank only ([[Cross-sectional momentum]]) | technique | signal | Slow filter for selection | p. 3, 12 |
| 5 | K ratio: R(1 - 2D/(1 - 2D)), zero if D at least 25% | principle | evaluation | Return corrected for drawdown, same unit as R | p. 5, fn 9 |
| 6 | Grid of momentum filters (L, LP) on K/FS | principle | evaluation | Check robustness to filters | p. 10-11 |

## 6. Regime observations

- Defensive fraction is 59.5% in IS1 and IS2, 55.4% in OS, 53.5% in RS (Fig 3).
- Jan to Jun 2022: fully defensive (33% DBC, 67% BIL); +6.4% for every BAA variant (p. 7).
- IS1 (1970s) is the best period for all variants; IS2 the weakest (Fig 3, 6, 9, 10).

## 7. Acknowledged limits

- The offensive universe of BAA-G4 uses QQQ in place of SPY, in-sample optimal on K/IS (note 10).
- DBC in the defensive universe is in-sample optimal on K/IS (note 8).
- The (SMA(12), 13612W) pair is in-sample optimal on K/IS (notes 6, 12).
- BAA-G4 is concentrated (p. 8).

## 8. Not addressed

- Confidence intervals, t-statistics, any significance test.
- Whether R is net of the 0.1% cost; slippage, ETF spreads, taxes, capacity.
- How many variants, universes or parameters were tried in this and the earlier PAA, VAA and DAA papers.
- Whether the "OS" period played any part in choosing the earlier papers' filters.
- Execution at the same close as the signal.
- Intra-month drawdowns (D is monthly).
- Construction of the pre-ETF proxy series (Appendix A of another paper).
- Mechanism: why the canary assets should predict the offensive ones.
