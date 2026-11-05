---
type: diagnostic
kind: performance
aliases: [ASD, AFSD, ASSD, Almost first-order stochastic dominance, Almost second-order stochastic dominance, Stochastic dominance]
sources: 1
---

# Almost stochastic dominance test

> [!summary]
> Would almost every investor prefer this strategy to the benchmark, whatever the return distribution and their risk aversion?

## How it works

- **How**: compare the empirical cumulative return distributions of the strategy and the benchmark over a holding horizon. ε = area where the strategy's CDF lies above the benchmark's, divided by the total area between the two CDFs (first order); same on integrated CDFs for second order.
- **Reading**: ε = 0 is classic dominance; ε below a tolerance (5.9% first order, 3.2% second order, Levy et al. 2010) is almost dominance. ε = 1 means the benchmark dominates.
- **Data needed**: return series of strategy and benchmark over rolling horizons.

## What the sources say

### Parameters
- **Han 2023**
	- 4, 13, 26, 52 and 78-week rolling horizons (p. 1140)
	- Benchmarks: S&P 500, 10-year T-bond, 1-month T-bill, Bitcoin (p. 1131)
	- Critical ε: 5.9% (AFSD), 3.2% (ASSD) (p. 1134-1135)

### Why
- **Han 2023**
	- Crypto returns are highly non-normal, so mean-variance metrics mislead (p. 1126, 1130)
	- No assumption on the distribution or the utility function (p. 1126)

### Evidence
- **Han 2023**: real data, in-sample, gross
	- No factor portfolio dominates the S&P 500 at 4 weeks; 10 of 29 at 52 weeks (Table 5)
	- Eight factors dominate all four benchmarks at 52-78 weeks (p. 1142, 1146)
	- Bitcoin dominates five factor portfolios at 78 weeks (p. 1142)

### Limits
- **Han 2023**
	- Dominance counts depend on the horizon (Tables 5-6)
	- Several counts in the text do not match the tables (p. 1142, 1144)

## Sources

- [[2023 - Han Newton Platanakis et al - On the (almost) stochastic dominance of cryptocurrency factor portfolios]] (Han 2023)
