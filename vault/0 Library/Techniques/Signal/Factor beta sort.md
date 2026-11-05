---
type: technique
brick: signal
aliases: [exposure sort, beta-sorted portfolios, sort on carry beta, rolling beta sort]
sources: 1
tested_on: [fx]
---

# Factor beta sort

> [!summary]
> Ranks assets on their past exposure to a factor and goes long the most exposed against the least exposed.

## How it works

- **Inputs**: asset excess returns and the return of the factor, same dates.
- **Formula**: each period, regress each asset's past excess return on a constant and the factor over a rolling window that ends the period before; the slope is the exposure.
- **Lookback / holding**: a rolling window in months; hold one period.
- **Output**: group membership, from lowest to highest exposure.
- **Direction**: long-short: long the highest exposure, short the lowest.
- **Tested on**: currencies against USD.

## What the sources say

### Parameters
- **Lustig 2008**
	- Factor: the carry factor, portfolio 6 minus portfolio 1 of the forward-discount sort (p. 15).
	- Window: 36 months ending at t-1; 12 months also run (p. 15).
	- Six groups; no bid-ask spreads, because the long or short side is not known in advance (p. 15).

### Why
- **Lustig 2008**: shows that forward discounts measure a currency's exposure to the risk factor (p. 15).

### Evidence
- **Lustig 2008**: real data, in-sample, gross, 37 currencies, 11/1983-03/2008.
	- Excess return 0.66% a year (lowest exposure) to 3.32% (highest); Sharpe 0.07 to 0.44 (Table 6).
	- Post-formation betas -0.31 to 0.28 (Table 6).
	- Highest minus lowest 2.66% a year, Sharpe 0.29, against 8.83% and 0.99 gross for the forward-discount sort (Tables 6, 1).
	- 12-month window: spread of about 300 bp, not shown (p. 15).

### Limits
- **Lustig 2008**
	- Text gives a top post-formation beta of 0.38, Table 6 gives 0.28 (p. 15).
	- Single sample, no costs.

## Sources

- [[2008 - Lustig Roussanov Verdelhan - Common Risk Factors in Currency Markets]] (Lustig 2008)
