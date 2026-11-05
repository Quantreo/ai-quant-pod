---
type: diagnostic
kind: performance
aliases: [random pairs benchmark, bootstrap of random pairs]
sources: 1
---

# Random pairs placebo

> [!summary]
> Does choosing the pairs add anything, or does any pair earn the same with the same trading rule?

## How it works

- **How**: form pairs at random from the same universe, trade them with the identical rule, costs and windows, repeat several times and average.
- **Reading**: if random pairs earn about as much as the selected ones, the profit comes from simple mean reversion in the trading stage, not from the pair selection.
- **Data needed**: price history of the universe and the full pairs trading setup.

## What the sources say

### Parameters
- **Fil 2020**
	- 30 random runs per frequency, results averaged; setup identical to the distance method (p. 172647)
	- Idea taken from Gatev (p. 172647)

### Why
- **Fil 2020**: to decouple the added value of pair formation from simple mean reversion in the trading stage (p. 172647)

### Evidence
- **Fil 2020**: real data, in-sample, net of costs
	- Daily: random -0.59% a month, below distance -0.07% and cointegration 1.36% (Table 2)
	- Hourly: random 1.97% against distance 3.10%, cointegration 1.11% (Table 2)
	- 5-minute: random 6.54% against distance 11.61%, cointegration 4.16%; Sharpe 12 for random and cointegration (Table 2)

### Limits
- **Fil 2020**
	- Only 30 runs per frequency; no dispersion reported (p. 172647)
	- Authors read the intraday result as a sign of mean reversion and market inefficiency, not tested further (p. 172649)

## Sources

- [[2020 - Fil Kristoufek - Pairs Trading in Cryptocurrency Markets]] (Fil 2020)
