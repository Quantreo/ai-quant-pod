---
type: diagnostic
kind: attribution
aliases: [auto-covariance decomposition]
sources: 1
---

# Profit decomposition into persistence and mean return

> [!summary]
> Does the profit come from return persistence or from the average return of the assets over the sample?

## How it works

- **How**: split the strategy's profit into auto-covariance, cross-serial covariance and squared mean return components.
- **Reading**: a large auto-covariance share means persistence drives the profit. A large squared-mean share means the average drift does.
- **Data needed**: monthly returns of the assets and of the strategy.

## What the sources say

### Parameters
- **Moskowitz 2012**
	- 12 / 1 rule, by asset class (Table 5B).

### Why
- **Moskowitz 2012**: shows where the profit comes from (p. 241, 244).

### Evidence
- **Moskowitz 2012**: real data, in-sample, gross of costs.
	- Auto-covariance is the main component of the profit (p. 244).
	- Auto-covariance / squared mean / total: commodities 0.43 / 0.17 / 0.59, equity indexes 0.83 / 0.17 / 1.00, currencies 0.80 / 0.17 / 0.96 (Table 5B).
	- Bonds 0.35 / 0.70 / 1.05: squared mean is about two thirds of the total, computed from Table 5B.

### Limits
- **Moskowitz 2012**
	- The units of Table 5B are not stated.

## Sources

- [[2012 - Moskowitz Ooi Pedersen - Time Series Momentum]] (Moskowitz 2012)
