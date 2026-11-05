---
type: technique
brick: risk
aliases: [Beta hedge, Market-neutral hedge, Ex-ante beta hedge, Rolling beta hedge]
sources: 1
tested_on: [equities]
---

# Market beta hedge

> [!summary]
> Offsets a strategy's estimated market beta with an opposite position in the market, to remove its market exposure.

## How it works

- **What it limits**: the strategy's exposure to the market return.
- **Trigger / level**: hedge ratio equal to minus the estimated beta, reset at each rebalance.
- **How the level is set**: a rolling regression of strategy returns on market returns over a past window. The beta must be estimated ex ante: a beta measured over the holding period uses future data.

## What the sources say

### Parameters
- **Daniel 2016**
	- Ex-ante beta from the past 42 days of daily returns (p. 19)
	- Market return plus 10 daily lags, coefficients summed (fn 2, p. 12; p. 19)
	- Ex-post comparison: the future 42-day beta, following Grundy and Martin (2001) (p. 19)

### Why
- **Daniel 2016**: momentum betas swing widely after market moves, so a hedge looks like a cure for crashes (p. 2, 13)

### Evidence
- **Daniel 2016**: real data, US equity WML, gross
	- 1927-1939: the ex-post hedge avoids the 1932 crash; the ex-ante hedge does not and ends below the unhedged portfolio (Fig. 4, p. 19)
	- 1927-2013: the ex-ante hedge does no better than unhedged (Fig. 4, p. 19)
	- In bear markets WML beta is much more negative when the market rises (-0.815 increment, t = -4.5), which biases ex-post hedges upward (Table 3, p. 14-16)

### Limits
- **Daniel 2016**
	- Results shown as charts only, on a log scale, no table (Fig. 4)
	- Tested on US equity momentum only

## Sources

- [[2016 - Daniel Moskowitz - Momentum crashes]] (Daniel 2016)
