---
type: diagnostic
kind: performance
aliases: [drawdown distribution vs bootstrap, pure drawdown test, maximum loss by horizon]
sources: 1
---

# Drawdown test against i.i.d. bootstrap

> [!summary]
> Are the strategy's drawdowns deeper or more frequent than independent returns with the same distribution would produce?

## How it works

- **How**: measure drawdowns (high-water mark to following low), pure drawdowns (runs of consecutive losing days) and the maximum loss over each horizon. Simulate many return series of the same length, either normal with the sample mean and volatility, or bootstrapped with replacement from the daily returns. For each observed drawdown, the p-value is the share of simulations with at least as many drawdowns that deep.
- **Reading**: low p-values mean losses come in persistent runs, not only from fat-tailed single days. Unlike the normal benchmark, the bootstrap keeps the skewness and kurtosis of daily returns.
- **Data needed**: daily strategy returns.

## What the sources say

### Parameters
- **Daniel 2014**
	- Daily excess returns, 10,000 simulated paths of the sample length (p. 29).
	- Benchmarks: i.i.d. normal and i.i.d. bootstrap with replacement (p. 29).
	- 20 worst drawdowns and pure drawdowns; maximum loss by horizon up to 180 days (Tables 22-24, p. 30-31).

### Why
- **Daniel 2014**: separates sudden crashes from persistent losses, to see where the negative monthly skewness comes from (p. 29).

### Evidence
- **Daniel 2014**: real data, in-sample, gross of costs.
	- EQ worst drawdown 12.0% over 94 days (p-b .13); two drawdowns worse than 10.8% p-b .018 (p. 30; Table 22).
	- SPD worst drawdown 21.5% over 163 days (p-b .023) (p. 30; Table 22).
	- Maximum loss beyond the bootstrap 5% bound for EQ past 3 days and SPD past 40 days; vol-scaled versions mostly within (p. 31; Table 23).
	- EQ worst pure drawdown 5.2% over 7 days (p-b .014) (p. 31-32; Table 24).

### Limits
- **Daniel 2014**
	- The normal benchmark fails at almost every horizon, so the bootstrap carries the reading (p. 30).
	- Benchmarks ignore volatility clustering; block bootstrap and jump-diffusion models not tried (p. 29, fn. 19, 21).

## Sources

- [[2014 - Daniel Hodrick Lu - The Carry Trade Risks and Drawdowns]] (Daniel 2014)
