---
type: technique
brick: signal
aliases: [Comomentum filter, Institutional active weight conditioning, speculator share split, financialization split]
sources: 2
tested_on: [equities, commodities]
---

# Momentum crowding filter

> [!summary]
> Splits a momentum strategy by how crowded or institutionally traded it is, to see when its return is larger or turns negative.

## How it works

- **Inputs**: a momentum portfolio, a comomentum measure, and institutional ownership data.
- **Formula**: sort periods or stocks into terciles or quintiles of comomentum or of institutional active weight. Read the momentum return in each group.
- **Lookback / holding**: by year after formation for comomentum.
- **Output**: momentum return per crowding group.
- **Direction**: the paper links low comomentum and high active weight to a larger momentum return.
- **Tested on**: US stocks.
- **Variant**: crowding measured at market level by the non-commercial share of open interest, and applied to a term structure signal as well as momentum.

## What the sources say

### Parameters
- **Lou 2019**
	- Comomentum in terciles, results for year 1 and year 2 after formation (Table 7B-C).
	- Institutional active weight in quintiles, top minus bottom (Table 8B).
- **Zaremba 2016**
	- Speculator share = (non-commercial long + short + spread positions) / all reported positions, CFTC, end of the previous month (Eq. 2, p. 35).
	- Median split on the share, then median split on past return inside each half; 26 commodity futures, 1987-2013 (p. 36).

### Why
- **Lou 2019**: proxies for momentum crowding and for rebalancing by institutions (p. 207-210). Institutions as a class trade against momentum (p. 206-208).
- **Zaremba 2016**: more speculators may mean crowding of momentum followers using the same signals, which wears momentum out (p. 33).

### Evidence
- **Lou 2019**: real data, US stocks 1993-2013, gross of costs, long-short momentum
	- Overnight by comomentum tercile, year 1 / year 2: low 1.20% / 0.86%, high 0.17% / -1.28% (Table 7B).
	- Intraday by comomentum tercile, year 1 / year 2: low -0.90% / -0.70%, high -0.18% / 0.41% (Table 7C).
	- Active weight, top minus bottom quintile: overnight 1.15% (t = 5.39), intraday -0.76% (t = -2.70) (Table 8B).
- **Zaremba 2016**: real data, in-sample, excess return, no costs.
	- Low vs high share: 1 month 0.65% vs 0.15%, difference 0.50% (t = 0.99) (Table 4).
	- 12 months 0.93% vs 0.66%, difference 0.26% (t = 0.52) (Table 4).

### Limits
- **Lou 2019**
	- The year-1 comomentum differences are called significant in the text. Their t-statistics are -1.82 and 1.68, below 1.96 (p. 207, Table 7).
	- Institutional trading can both drive and follow returns. The authors give three arguments against reverse causality (p. 207).
	- Value-weighted institutional coefficient -0.260 (s.e. 0.119). None when equal-weighted (Table 7A, p. 206-208).
- **Zaremba 2016**
	- No momentum difference is significant (p. 43).
	- The share is the author's own measure, no standard exists (p. 35).
	- CFTC data start between 1986 and 2011 by commodity (Table 1).

## Sources

- [[2019 - Lou Polk Skouras - A Tug of War Overnight vs Intraday Returns]] (Lou 2019)
- [[2016 - Zaremba - Strategies Based on Momentum and Term Structure in Financialized Commodity Markets]] (Zaremba 2016)
