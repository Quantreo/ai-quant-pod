---
type: technique
brick: signal
aliases: [Canary universe, Breadth momentum, Protective universe switch, Crash protection switch, Offensive and defensive universe rotation, Bold Asset Allocation, Canary crash protection, Vigilant asset allocation breadth, Defensive asset allocation breadth]
sources: 2
tested_on: [multi-asset]
---

# Canary universe switch

> [!summary]
> Moves the whole portfolio from a risky universe to a defensive one when assets of a small protective ("canary") universe show negative absolute momentum.

## How it works

- **Inputs**: month-end prices of a small protective universe, of an offensive universe and of a defensive universe.
- **Formula**: absolute momentum of each canary asset; count the bad ones (negative); the share held in the defensive universe grows with that count up to a breadth threshold B.
- **Lookback / holding**: a fast momentum filter for the canary; a slower one to rank assets inside each universe; monthly decision, held to the next month.
- **Output**: weights: the Top N of the active universe, equal weight; defensive picks below cash are replaced by cash.
- **Direction**: long only; the defensive side can be bonds, commodities or cash.
- **Tested on**: ETFs across stocks, bonds and commodities.
- **Variant**: B=1, the switch is 100% as soon as one canary asset is bad; a larger B scales the defensive share in proportion.
- **Variant**: breadth over the whole universe instead of a canary set: count the assets with positive momentum and go defensive when too few remain.

## What the sources say

### Parameters
- **Keller 2022**
	- Canary: SPY, VWO, VEA, BND; B=1; absolute momentum 13612W, weights 12, 4, 2, 1 on the 1, 3, 6, 12-month returns (p. 4, 12)
	- Offensive: 12 assets Top6 (G12) or QQQ, VWO, VEA, BND Top1 (G4); rank on p/SMA(12) - 1 (p. 3-4, 7)
	- Defensive: TIP, DBC, BIL, IEF, TLT, LQD, BND, Top3, picks below BIL replaced by BIL (p. 4)
	- Monthly, at the last close, 17 ETFs, proxy data from Dec 1969 (p. 3, 12)

- **Prior-Sanz 2026**
	- Count threshold, lookbacks and canary assets are not stated; they come from the cited designs (Keller and Keuning 2017, 2018; Kipnis 2019) (p. 3, 7).
	- Breadth coded 1 when exposure depends on the share of assets with positive momentum; Canary coded 1 when designated canary assets trigger the defensive allocation (p. 7).
	- Monthly, 0.2% round trip (p. 6).

### Why
- **Keller 2022**: not argued economically; with B=1 the protection is faster than the usual rule, which switches only when most offensive assets are bad (p. 1-2)
- **Prior-Sanz 2026**: when too few asset classes keep positive momentum, the strategy moves to treasuries; read as early detection of weak market health (p. 3).

### Evidence
- **Keller 2022**: real data, in-sample, 0.1% one-way cost listed as a parameter (net not stated), Dec 1970 to Jun 2022
	- BAA-G4 R 21.0%, D 14.6%, Sharpe 1.21; BAA-G12 R 14.6%, D 8.7%; 60/40 R 9.5%, D 29.5% (p. 5, 7)
	- Defensive in 57.2% of months (Fig 3)
	- SPY only offensive: D 16.2% against 50.8% for SPY alone (Fig 11-12)
	- Last decade: R 6.6% to 10.9% by variant; BAA-SPY 10.1% against 12.6% for SPY (Fig 3, 6, 9-12)
- **Prior-Sanz 2026**: real data, vendor-run rules, 1995-April 2025, net of 0.2% round trip
	- Group 3 (17 strategies, dual momentum plus breadth): mean Sharpe 0.78, the highest of ten groups; MaxDD -15.6%; gap +0.17 against the static group, p = 0.006, indicative (p. 26, Table 13).
	- Canary coefficient on strategy Sharpe: 30 years +0.13***, 10 years +0.16**, 5 years +0.34***, 2000-02 -0.51* (Tables 4-6, 8).
	- Breadth coefficient: 30 years -0.04, 5 years -0.36***, 2000-02 +1.26** (Tables 4, 6, 8).

### Limits
- **Keller 2022**
	- QQQ for SPY, DBC in the defensive set and the filter pair are in-sample optimal (notes 6, 8, 10)
	- The "out-of-sample" period is not a hold-out; no significance tests (p. 4, whole paper)
	- Ten parameters per model; the number of variants tried is not stated (Fig 3)
	- Turnover 472% to 523% a year (Fig 3, 6)
- **Prior-Sanz 2026**
	- Group averages, no rule or per-strategy result; breadth sits in the same group as dual momentum.
	- Breadth weakens over 10 and 5 years and in COVID; a live-window coefficient of +0.11 (t ≈2.34) is reported without full estimation (p. 14-17, 25).
	- Few strategies carry the canary flag (p. 12).

## Sources

- [[2022 - Keller - Relative and Absolute Momentum in Times of Rising Low Yields Bold Asset Allocation (BAA)]] (Keller 2022)
- [[2026 - Prior-Sanz Vizuete-Luciano Cruz-Zayash et al - The long-term efficiency of tactical asset allocation Evidence from 86 systematic strategies (1995-2025)]] (Prior-Sanz 2026)
