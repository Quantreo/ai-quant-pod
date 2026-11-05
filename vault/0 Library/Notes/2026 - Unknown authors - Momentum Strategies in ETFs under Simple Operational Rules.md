---
type: reading-note
source: paper
title: "Momentum Strategies in ETFs under Simple Operational Rules: Economic Value and Conditional Predictability"
authors: Not stated in the PDF
affiliations: Not stated in the PDF
year: 2026
venue: SSRN 7379989, preprint, not peer reviewed (p. 1)
doi:
pdf: "[[2026 - Unknown authors - Momentum Strategies in ETFs under Simple Operational Rules.pdf]]"
version: preprint
tier: 1
read: full
tags: [trend, equities, weekly]
date: 2026-10-25
---

# Momentum in ETFs under simple operational rules (Unknown authors 2026)

## Summary

- **Finding**: pure cross-sectional momentum on 3,215 US ETFs, 2001-2026, has Sharpe -0.17 to +0.22 and drawdown -69% to -82%. The full rule set (TSL07) reaches Sharpe 1.336, drawdown -6.98%, net of 20 bp per side. All in-sample.
- **Mechanism**: not stated for momentum. The authors say value comes from the management layer (filters, diversification caps, exits), mostly as tail-risk reduction, not higher return.
- **Where it works best**: against SPY, drawdown is 47 pp smaller but the CAGR gain (3.45 pp) is not significant. Entry filters add nothing statistically. The 7% trailing stop is the best implementable exit.
- **Weak spots**: Sharpe turns negative when VIX is above 25 (17.8% of weeks). The authors state no active rule beats passive from monthly rebalancing on, with no table shown.
- **Main caveats**: no hold-out. Entry filter, exit rule and implementability cut were chosen on the full sample, best of 74 implementable rules out of 144. No selection adjustment. Decisions and fills at the same Friday close.

Page numbers are the PDF pages, which equal the printed pages. Values marked ≈ are read from a chart; the paper has no chart. The PDF names no author, affiliation or acknowledgement on any of its 28 pages.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | The alpha sits in the operational layer, not in the technical signal | 63 entry filters give two Sharpe values (0.945 and 0.881), not significantly different. Pure momentum fails (Sharpe -0.17 to +0.22). | Table 2, Table 3 Panel D; p. 15, 19-20 |
| 2 | The edge is tail protection, not extra return | Against SPY: drawdown -47.46 pp (p < 0.001), CVaR95 -3.83 pp, CAGR +3.45 pp (p = 0.31). | Table 3 Panel C; p. 19 |
| 3 | High-VIX weeks erase the alpha because correlations across categories converge | VIX above 25: weekly return falls 0.46 to 0.62 pp. Conditional Sharpe -0.83 to -1.20. | Table 4; p. 22-23 |

Claim 3 is the authors' interpretation; no correlation test is shown. They also frame the result with the Adaptive Markets Hypothesis (p. 20, 23).

**Caveats raised by the authors**: US ETFs only; alpha needs a review every one or two weeks; results rest on 20 bp per side; no internal hedge against systemic stress (p. 23-24).

**Ruled out**: NBER recessions, term spread and credit spread have no significant effect on any rule (Table 4).

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | 3,215 US ETFs after four filters: at least 52 weeks of history, 13-week median daily volume above USD 100,000, at least 90% non-null closes in 252 days, no leveraged or inverse funds (77 removed). | p. 6, fn 2 |
| Period | 31 Aug 2001 to 15 May 2026, 1,289 weeks. Start is when 8 slots can be filled. | p. 6 |
| Entry filter | C2 and C6: MA50 above MA200, and price above the highest price of the past 252 days. Chosen ex post from 63 subsets of six conditions. | Table 1; p. 7, 10 |
| Selection | Score = 0.35 rank(r26) + 0.35 rank(r13) + 0.20 rank(distance to 30-week average) + 0.10 rank(r4), ranks are cross-section percentiles. Weights follow "the consensus" in the literature. | Eq. 1; p. 7 |
| Portfolio | 8 slots, 12.5% each, long only. Fewer than 8 candidates: the rest is in cash at the 3-month T-bill. | p. 7 |
| Diversification | 11 super-categories. Cap 2 for US_LARGE_CAP and US_SECTORAL, cap 1 for the other nine. | Table 5; p. 8, fn 6 |
| Rebalancing | Entries every other Friday. Exits checked every Friday. | p. 6, 8 |
| Exit | Native: price below MA50 cuts the position to 50% (reversible); death cross closes it. Plus one of 144 SL/TP rules. | p. 8 |
| Costs | 20 bp per side in the returns; cash free; benchmarks at zero cost. | p. 9 |
| Data | Refinitiv DataStream daily prices adjusted for dividends and splits, aggregated to Friday closes. Macro series from FRED. | p. 6 |

**Rule**: each Friday, rank eligible ETFs (C2 and C6 true) by score, fill free slots from the top while respecting category caps (entry Fridays only); close any position that breaks its exit (every Friday). TSL07 exits when price falls below the highest price since entry times (1 - 0.07) (Table 1 Panel B).

**144 exit rules**: 23 stops x 6 take-profit settings (none, TP30, 50, 60, 100, 200 = +30% to +200% over entry) + 5 take-profit alone + 1 baseline. Stops: fixed 5 to 20%; trailing 7 to 20%; rolling weekly low over 10, 20, 40 weeks; chandelier ATR(14 weeks) x 2, 3, 4; price below a moving average (EMA 5 weeks, SMA 50, 100, 200), as overlay or replacing the native exits (Table 1; p. 8, 10).

**Data provenance**: ETF list, sector class and leveraged marker from Refinitiv. Delisted funds, backfills and survivorship are not discussed.

## 3. Results

All results: real data, in-sample, net of 20 bp per side. Tests: Jobson-Korkie with Memmel correction (Sharpe), HAC t (CAGR), block bootstrap (drawdown, CVaR).

**Aggregate**
- Pure cross-sectional momentum, N = 8, no filters, caps or exits: Sharpe +0.215 (1 month), -0.008, -0.043, -0.167 (12 months). Drawdown -69.5% to -81.9%. SPY buy-and-hold: Sharpe 0.459, CAGR 9.81%, drawdown -54.44% (Table 3 D).
- TSL07: Sharpe 1.336 (CI 1.26 to 1.41), CAGR 13.26%, drawdown -6.98%, CVaR95 1.83%, 16.8 slot changes a year, 19.0% in cash (Table 3 A).
- Best of the other family, MA_SMA200_OV_TP100: Sharpe 1.320, CAGR 14.84%, drawdown -11.04%, 12.5 slot changes (Table 3 A). Not different from TSL07 on Sharpe (p = 0.51).
- Take-profit adds nothing to TSL07: Sharpe 1.316 to 1.336 across five levels (Table 3 A; p. 18).
- Versus no SL/TP baseline: TSL07 Sharpe +0.299 (p = 0.01), drawdown +7.10 pp, CAGR +0.34 pp (p = 0.83) (Table 3 B).
- Cost toll: about 0.7 to 0.9 pp a year for TSL07 (p. 19).

**By sub-group**
- Entry filters: C1, C2, C3, C4, C6 give identical Sharpe 0.881, drawdown -13.81%, CVaR 2.80%. Adding C5 (13-week higher highs and lows) gives 0.945. Difference not significant (p = 0.31) (Table 2). The five filters pick the same ETFs in 99% of weeks (p. 14).
- Versus benchmarks, TSL07 Sharpe gain: SPY +0.812, IEF +1.171, VTI+EFA +0.885, 60/40 +0.744, all p < 0.001. CAGR gain significant only against IEF (+9.93 pp) and 60/40 (+5.28 pp) (Table 3 C).
- 70 of 144 rules exceed 20 slot changes a year and are dropped. Their top: chandelier ATR2 Sharpe 1.42 (40 slots), EMA 5-week 1.39 (51 slots) (p. 16).
- The cut at 20 slot changes a year is the authors' own rule.

**Horizon and parameters**
- Pure momentum Sharpe falls as the lookback rises, from +0.215 to -0.167 (Table 3 D).
- Rebalancing frequency (weekly to annual, 30 simulations): described only. See section 4.

**Over time**
- Regime regression, full sample: alpha +0.29 to +0.35 pp a week. VIX above 25 adds -0.46 (TSL07) to -0.62 (baseline) pp, t about -4.3 to -4.9 (Table 4 A).
- Split halves (2001-2013, 2014-2026): same signs; the VIX effect is more negative in the second half, -0.56 to -0.80 vs -0.40 to -0.57 (Table 4 B-C).
- 519 rolling 260-week windows: VIX coefficient significant in 80% to 92% of them (Table 4 D).
- Conditional Sharpe over the full sample 1.27 to 1.66; below zero when VIX above 25; near zero in NBER recessions; 1.5 to 2.0 in low term spread and high credit spread (p. 22-23).
- No equity curve or yearly table is shown.

**Link to other strategies**: none beyond the four passive benchmarks.

**Inconsistencies in the source**
- SPY Sharpe: Table 3 gives 0.459. Table 2 ΔSh +0.483 for a rule at 0.881 implies SPY about 0.398 (computed). Panel C gives +0.408 for the same rule vs SPY.
- TSL07 Sharpe 1.336 minus SPY 0.459 is 0.877 (computed), but Table 3 C reports +0.812.
- Text calls the five TP variants of TSL07 "indistinguishable to the third decimal" (p. 18). TSL07_TP30 differs: drawdown -7.91% vs -6.98%, CAGR 13.59% vs 13.26% (Table 3 A).
- Table 2 note says C5 raises Sharpe by 6.3%; 0.943 vs 0.881 is 7.0% (computed).
- Abstract and p. 3 claim a "statistically and economically significant" win; CAGR gain vs SPY is not significant (Table 3 C).

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| From monthly rebalancing on, no active rule beats passive; the 5 x 6 frequency matrix has no table | p. 11, 23-24 |
| Under higher costs, the core with Sharpe above 1.3 keeps its advantage | p. 24 |
| If the strategy works with C2 and C6, the other 62 filters work at least as well | p. 16 |
| Time-series momentum gives near-identical results (omitted) | Table 3 note, p. 18 |
| Full frontier of 144 rules and the conditional Sharpe table are supplementary, not in the PDF | p. 18, 22 |
| Weights 0.35/0.35/0.20/0.10 and the category caps follow "consensus"; no test | p. 7, fn 6 |
| Correlations converge to one in 2002, 2008, 2011, 2020, 2022 | p. 23 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | [[Cross-sectional momentum]]: weighted rank score over four horizons, top 8, long only | technique | signal | Weights follow the 3 to 12 month consensus | Eq. 1; p. 7 |
| 2 | [[Time-series momentum signal]]: golden cross (MA50 above MA200) as entry filter | technique | signal | Canonical in the technical literature | Table 1; p. 15 |
| 3 | [[Channel breakout]]: price above the 252-day high as entry filter | technique | signal | Same | Table 1; p. 15 |
| 4 | [[Minimum price and size filter]]: age, median volume, data coverage, no leveraged funds | technique | universe | Operational viability; volatility decay of leveraged funds | p. 6, fn 2 |
| 5 | [[Category exposure cap]]: at most 1 or 2 positions per super-category | technique | risk | Avoids three slots on the same S&P 500 factor | p. 8, fn 6 |
| 6 | [[Trailing stop]]: exit when price falls a fixed share below its high since entry | technique | risk | Closes positions quickly in corrections | p. 18, 22 |
| 7 | [[Moving-average exit]]: partial exit below MA50, full exit on death cross, or price below SMA200 | technique | exit | Not argued beyond protection | p. 8 |
| 8 | [[Asymmetric entry and exit cadence]]: entries biweekly, exits weekly | technique | rebalancing | Filters weekly false positives, cuts overtrading | p. 8 |
| 9 | [[Rule ablation]]: all 63 subsets of six conditions, with a no-exit control and a pure-momentum replication | technique | evaluation | Isolates the contribution of each layer | p. 10, 12 |
| 10 | [[Sharpe ratio difference test]]: Jobson-Korkie with Memmel correction | technique | evaluation | Tests whether Sharpe gaps exceed noise | Eq. 2; p. 10-11 |
| 11 | [[Market state split]]: regression on four regime dummies, split halves, 260-week rolling windows, conditional Sharpe | technique | evaluation | Tests whether alpha depends on the macro regime | Eq. 3; p. 11-12 |
| 12 | [[Slower rebalancing test]]: weekly to annual, fully discrete | technique | evaluation | Finds the frequency where alpha vanishes | p. 11 |

Not carded: take-profit levels (no gain over the trailing stop), slot-change cap of 20 (the authors' own setting), cash at T-bill when slots are empty (detail), block bootstrap and HAC errors (standard).

## 6. Regime observations

High VIX is the only regime that matters (Table 4). The authors tie it to the convergence of the eleven categories (p. 23). Recession, term spread and credit spread show no effect (Table 4).

## 7. Acknowledged limits

US ETFs only. Needs a review every one or two weeks. Results depend on 20 bp per side. Fragility to high VIX is structural and unhedged (p. 23-24).

## 8. Not addressed

- Hold-out or any out-of-sample test of the full rule.
- Selection adjustment for 63 filters, 144 exits, 30 frequency runs.
- Execution lag: signals and fills use the same Friday close (p. 8, fn 5).
- Spread and impact beyond a flat 20 bp, capacity, taxes.
- Delisted ETFs and survivorship.
- Yearly returns, equity curve, drawdown dates.
- Zero cost for benchmarks.
- Authors, affiliations, code and data availability.
