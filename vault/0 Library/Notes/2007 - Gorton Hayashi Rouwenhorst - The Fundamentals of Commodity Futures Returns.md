---
type: reading-note
source: paper
title: The Fundamentals of Commodity Futures Returns
authors: Gorton, Hayashi, Rouwenhorst
affiliations: Gorton (The Wharton School, University of Pennsylvania, and NBER), Hayashi (NBER), Rouwenhorst (Yale School of Management)
year: 2007
venue: NBER Working Paper 13249, July 2007
doi: 10.3386/w13249
pdf: "[[2007 - Gorton Hayashi Rouwenhorst - The Fundamentals of Commodity Futures Returns.pdf]]"
version: working paper (NBER w13249). A later journal version exists (Review of Finance, 2012); this note reads the NBER version only.
tier: 1
read: full
tags: [carry, commodities, monthly]
date: 2026-10-22
---

# The fundamentals of commodity futures returns (Gorton, Hayashi, Rouwenhorst 2007)

## Summary

- **Finding**: monthly sorts of 31 commodity futures into halves, 1969-2006: high basis beats low by 10.23% p.a., high 12-month momentum by 13.36%, low inventories beat high by 8.06%. Gross.
- **Mechanism**: Theory of Storage. Low inventories raise stock-out risk and future spot volatility, so the risk premium rises. Basis and past returns proxy inventories. Hedging pressure rejected.
- **Where it works best**: spot and futures momentum sorts (t = 4.95, 4.93), stronger in 1990-2006 (16.03%, 15.36%). Basis slope on inventories steepest for Energy and Meats.
- **Weak spots**: direct inventory-on-return regressions mostly insignificant; volatility barely differs across sorts; basis and momentum earn a premium orthogonal to inventories, which the authors leave unexplained.
- **Main caveats**: no costs; inventory publication lags not controlled; HP smoothing and spline knots chosen on the data; only three overlapping sub-periods; no drawdowns.

Page numbers follow the printed pagination of the NBER working paper (p. 1 = PDF page 3). Tables and figures (PDF pages 48-63) carry no page number and are cited by number. Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

Theory of Storage extended with risk-averse speculators and hedging inventory holders (model in Appendix A, two periods, theory only).

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Basis falls with inventories, at an increasing rate as inventories drop | Slope of basis on I/I* negative for 30 of 31 commodities at I/I* = 1; steeper at 0.75 for many Metals, Grains, Softs | p. 13-15, Table 3, Fig. 3A, 4 |
| 2 | Low inventories raise the futures risk premium (more stock-out risk, more future spot variance) | Low-inventory half beats high half by 8.06% p.a. (t = 3.19) | p. 8, 16, Table 5 |
| 3 | Basis, prior futures returns and prior spot returns carry information on inventories, hence on premiums | Sorted portfolios on these signals hold low-inventory commodities (t up to -17.08) | p. 18-21, Tables 6-8 |
| 4 | Momentum follows from slow inventory rebuilding: a spot spike from a shock is followed by high expected returns | Prediction from the model's logic, not formally modelled | p. 8 |

Who pays: inventory holders hedging bankruptcy costs pay risk-averse speculators (p. 7, App. A).

**Caveats raised by the authors**
- Model cannot say whether the number of contracts rises or falls when inventories fall (p. 22, 33).
- Inventory data are lagged and revised; this can create return predictability unrelated to premiums (p. 2, 17).
- I/I* does not allow comparison across commodities (p. 18).
- Energy slopes at I/I* = 0.75 are polynomial extrapolations, inventories rarely go that low (p. 15).
- Part of basis and momentum returns is orthogonal to inventories: measurement noise, missed cross-sectional dynamics, or an omitted common risk factor (p. 25).
- The paper "sheds little light" on reconciling premiums with asset pricing theory (p. 4).

**Ruled out**
- Hedging pressure (Keynes, Hicks) as a driver of ex-ante premiums: lagged commercial positions do not predict returns (p. 24-25, Table 10).
- Cross-sectional storability alone as the source of basis returns: de-meaned basis sort gives 10.13% (t = 3.52), unreported (p. 20).

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | 31 commodity futures with monthly inventory data (33 minus Sugar and Rough Rice). Gold, silver, electricity excluded. 7 available in Dec 1969, count grows over time. | p. 9, 12, 16 |
| Period | Dec 1969 to Dec 2006. Sub-periods 1986/1-2006/12 and 1990/12-2006/12. Start per commodity: latest of inventory start, 12th month of trading, Dec 1969. | p. 9, Tables 5-8 |
| Signals | (a) basis; (b) prior 12-month futures return; (c) prior 12-month spot return (nearest futures price); (d) normalized inventory I/I*. | p. 16-21 |
| Horizon | 1 month. 12-month lookback chosen to proxy slow inventories, not optimised. | p. 20-21 |
| Entry | End of each month, rank available commodities on the signal. | p. 16, 19 |
| Portfolio | Top half vs bottom half, equally weighted. Reported in excess of the equal-weight index, plus High minus Low. | p. 19, Tables 5-8 |
| Sizing | Equal weight. No volatility scaling. | p. 19 |
| Rebalancing | Monthly. | p. 19 |
| Costs | None mentioned. Results are gross. | whole paper |
| Return series | Fully collateralized excess return of the nearest contract that does not expire next month, rolled monthly. | p. 9 |

**Rule**

Basis (footnote 6, p. 10), with F1 nearest and F2 next contract, D the days to last trading date:

$$\text{Basis} = \left(\frac{F_1}{F_2} - 1\right) \cdot \frac{365}{D_2 - D_1}$$

Monthly excess return from end of t to t+1 (p. 9): $(F_{t+1,T} - F_{t,T}) / F_{t,T}$, with T after the end of month t+1.

Normal inventory I*: HP filter on log inventories, smoothness 160,000 x 81 for monthly data, chosen by visual inspection (footnote 8, p. 12).

Each month: long the half with the highest signal (lowest I/I* for inventories), short the other half, equal weights.

**Data provenance** (p. 8-9, 12, App. B)

| Item | Source | Notes |
| --- | --- | --- |
| Futures prices | Commodities Research Bureau and LME, as in Gorton and Rouwenhorst (2006) | Monthly |
| Metals inventories | LME and NYMEX warehouse stocks | Exchange stocks only, not off-exchange |
| Energy inventories | US Department of Energy, Monthly Energy Review | Crude: US non-SPR stocks |
| Grains | USDA stocks at selected terminals and elevators; early Soybeans and Wheat from CRB yearbooks | Weekly, rounded backfill |
| Meats, dairy, OJ | USDA cold storage reports | First-of-month data shifted to prior month end |
| Feeder Cattle | Live Cattle (frozen beef) inventory taken 3 months ahead | Assumes 3 months in feedlots |
| Gaps | Lumber Jun-Dec 2006 set to May 2006; Coal Dec 2006 set to Nov 2006; Tin used from June 1990 | |
| Positions | CFTC Commitments of Traders, 1986-2006; no LME, Butter, Coal | Table 9, footnote 15 |

## 3. Results

All results: real data, in-sample, gross. No out-of-sample test. The model in Appendix A is theory only, no simulation.

**Aggregate**

| Sort (1969/12-2006/12) | H-L % p.a. | t | % months H-L > 0 | Where |
| --- | --- | --- | --- | --- |
| Inventories (low minus high) | 8.06 | 3.19 | 56.53 | Table 5 |
| Basis | 10.23 | 3.73 | 57.88 | Table 6 |
| Prior 12m futures return | 13.36 | 4.93 | 58.11 | Table 7 |
| Prior 12m spot return | 13.85 | 4.95 | 57.88 | Table 8 |

H-L volatility 15.5% to 17.2% p.a. (Tables 5-8). H-L mean over volatility, computed: 0.52 (inventories), 0.66 (basis), 0.79 (futures momentum), 0.81 (spot momentum).

Equal-weight long index: 5.48% p.a. arithmetic, 13.5% volatility, average basis -2.10% (Table 1).

**By sub-group**

- Basis vs inventories: slope negative everywhere except Soybean Meal (+3.5). Pooled slope at I/I* = 1 from -5.1 (Metals) to -154.6 (Energy) (Table 3, p. 14).
- Nonlinearity significant for Metals (difference 6.7, t = 4.70) and Softs (6.4, t = 4.93); weak for Grains (t = 1.39), Meats (t = 0.12), Energy (t = -0.16) (Table 3).
- Returns on I/I*: group slopes significant only for Meats (t = -2.22); Energy t = -1.75, Metals t = -0.09. Positive (wrong-sign) coefficients for Palladium, Aluminum, Tin, Corn (Table 4).
- Low basis in high-inventory months for every commodity; t of the difference ≈1.1 (Coal) to ≈7.0 (Propane) (Fig. 3A).
- Low-inventory months have higher prior 12-month returns for most commodities; Palladium shows the reverse, Soybeans and Soybean Oil ≈0 (Fig. 3B).
- Cross-section of average returns on average basis, 1990/12-2006/12: RP = 7.13 + 0.73 Basis, R² = 0.52. Authors say this ex-post link does not prove a premium (Fig. 1, p. 11).
- Portfolio characteristics: High Basis holds inventories at -14.87 vs +15.31 (t = -17.08); High Momentum -9.30 vs 9.88 (t = -8.26); High Spot Momentum -3.00 vs 3.27 (t = -2.77) (Tables 6-8).
- Volatility difference between halves small: t from -1.15 (inventories) to 2.13 (basis) (Tables 5-8).

**Horizon and parameters**

- One lookback (12 months) and one holding period (1 month) only.
- Longer lookbacks widen inventory differences between momentum halves; unreported (p. 21).

**Over time**

| Sort | 1986-2006 H-L (t) | 1990-2006 H-L (t) | Where |
| --- | --- | --- | --- |
| Inventories | 7.25 (2.34) | 8.75 (2.82) | Table 5 |
| Basis | 9.74 (3.36) | 11.57 (4.08) | Table 6 |
| Futures momentum | 13.84 (4.34) | 15.36 (4.60) | Table 7 |
| Spot momentum | 17.37 (4.94) | 16.03 (4.47) | Table 8 |

Sub-periods overlap with the full sample. No yearly results, no cumulative return chart, no drawdowns.

**Link to other strategies**

- Return correlation of High Basis and High Momentum portfolios: 0.87 (p. 21).
- High Basis on Low Inventory portfolio: intercept 2.4% p.a. (t = 1.58). High Momentum: 4.0% p.a. (t = 2.27) (p. 25).
- Parts of basis and momentum returns orthogonal to inventories explain each other (intercept insignificant); no number shown (p. 25).
- Positions: commercials net short about 10% of open interest on average (p. 24). Contemporaneous commercial positions explain returns (R² about 10% on average), lagged ones do not (below 1%) (p. 24, Table 10).
- Non-commercials hold larger longs in high momentum commodities (9.02% vs 1.58% of open interest, t = 9.81) (Table 7).

**Inconsistencies in the source**

- p. 25 describes the 2.4% intercept as significant, with t = 1.58; the paper uses the 5% level elsewhere (p. 13).
- Figure 2 caption names two panels (Natural Gas, Corn); the figure shows three (Natural Gas, Wheat, Corn), as does the text (p. 12).

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| De-meaned basis sort returns 10.13% (t = 3.52), not different from raw basis | p. 20 |
| Longer lookbacks widen inventory dispersion of momentum portfolios | p. 21 |
| Table 3 not altered with interest-adjusted basis | p. 15, footnote 11 |
| Sorts on lagged hedging pressure do not spread returns | p. 24, footnote 16 |
| Orthogonal parts of basis and momentum returns share a common priced source | p. 25 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | [[Carry signal]]: Annualized basis from the two nearest contracts | technique | signal | Shape of the curve reflects inventories | p. 10, fn. 6 |
| 2 | [[Carry signal]], [[Long-short portfolio weighting]]: Cross-sectional half/half sort, equal weight, monthly | technique | signal | Controls cross-sectional dependence; nonparametric | p. 16, 19 |
| 3 | [[Cross-sectional momentum]]: Prior 12-month futures return as inventory proxy | technique | signal | Inventories slow to adjust; covers annual seasonality | p. 20-21 |
| 4 | [[Cross-sectional momentum]]: Year-on-year spot change (nearest futures) as signal | technique | signal | Removes seasonality of spot prices | p. 21 |
| 5 | [[Normalized inventory signal]]: Normalized inventory I/I* with HP trend on log inventories | technique | signal | Remove trend; measure deviation from normal | p. 12, fn. 8 |
| 6 | [[Static and dynamic return decomposition]]: De-mean a signal per commodity before sorting | technique | evaluation | Separate time-series from cross-sectional effect | p. 20 |
| 7 | Report portfolio characteristics (inventory, basis, prior returns, CFTC positions) of each sort | technique | evaluation | Shows what the sort really selects | Tables 5-8 |
| 8 | Contemporaneous vs lagged regressions to test causality of positions | principle | evaluation | Contemporaneous fit can be traders reacting to prices | p. 23-24 |
| 9 | Newey-West t-statistics, bandwidth 12, pooled OLS on unbalanced panel | technique | evaluation | Serial and cross-sectional error correlation | Tables 3-4, App. C |

## 6. Regime observations

- Low-inventory states coincide with backwardation and high prior returns (Fig. 3, Tables 5-8).
- Inventory seasonality differs by commodity: grains lowest before harvest; Natural Gas lowest in March; metals little seasonality (p. 12-13, Fig. 2, Table 2).
- Inventories persistent: median first-order autocorrelation above 0.90, lowest 0.71 (Soybean Meal) (p. 12, Table 2).

## 7. Acknowledged limits

- Inventory data: poor quality, unclear relevant definition, publication lags and revisions (p. 2, 11).
- Trading-rule test on inventories does not control for publication delays (p. 17).
- I/I* not comparable across commodities (p. 18).
- Energy nonlinearity results are extrapolations (p. 15).
- Single-factor explanation may miss part of the premium; left to future research (p. 25).
- Spline knot count J = 1 chosen by experimenting on the data (fn. 10); HP smoothness by visual inspection (fn. 8).

## 8. Not addressed

- Transaction costs, roll costs, slippage, capacity.
- Drawdowns, worst months, year-by-year returns.
- Whether I* is estimated in real time or on the full sample.
- Whether the 3-month-ahead Live Cattle value used for Feeder Cattle (p. 12) is known at portfolio formation.
- Treatment of an odd number of commodities in the half/half split.
- Out-of-sample test or data after 2006.
- Other lookbacks or holding periods than 12 and 1 months.
- Questions for the desk: the Review of Finance (2012) version may differ in sample and numbers; this note does not cover it.
