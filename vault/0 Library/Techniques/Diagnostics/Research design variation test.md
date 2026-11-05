---
type: diagnostic
kind: performance
aliases: [Nonstandard errors, Design choice grid, Specification curve, Multiverse analysis]
sources: 1
---

# Research design variation test

> [!summary]
> Where does the chosen specification sit among all reasonable ways of building the same strategy?

## How it works

- **How**: list the design choices (outlier treatment, filters, weighting, breakpoints, estimation window, lag, estimator) and their options; rebuild the strategy for every combination; plot the distribution of Sharpe ratios and report the median per option.
- **Reading**: a baseline near the middle of a mostly positive distribution supports robustness; a baseline at the top, or many negative variants, shows dependence on choices.
- **Data needed**: the full pipeline, rerun for each combination.

## What the sources say

### Parameters
- **Fieberg 2025**
	- 55,296 combinations: outliers, stablecoins, size and price filters, weighting, quintile or tercile, rolling or expanding window, 26-104 weeks, 0 or 1-day lag, volume indicators, estimator, validation split (Table 6, p. 3135-3137)
	- Significance of each Sharpe ratio by the Lo (2002) test (p. 3138)

### Why
- **Fieberg 2025**: seemingly minor methodological choices can change conclusions (nonstandard errors, Menkveld et al. 2024) (p. 3135)

### Evidence
- **Fieberg 2025**: real data
	- CTREND Sharpe: median 1.34, range -1.45 to 10.92; significant in 79% of variants (p. 3138-3139)
	- CSMB significant in 56%, CMOM in 49% (p. 3139)
	- Median Sharpe 1.17 value weight vs 1.47 equal weight; 1.24 with a 1-day lag (Table 6)

### Limits
- **Fieberg 2025**
	- Extreme Sharpe ratios come from variants that emphasise small, volatile coins (p. 3138-3139)
	- Baseline sits at the upper edge of the distribution (p. 3138)

## Sources

- [[2025 - Fieberg Liedtke Poddig et al - A Trend Factor for the Cross Section of Cryptocurrency Returns]] (Fieberg 2025)
