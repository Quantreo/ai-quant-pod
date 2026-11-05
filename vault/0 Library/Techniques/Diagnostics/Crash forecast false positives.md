---
type: diagnostic
kind: performance
aliases: [false positive count, tail risk measure comparison]
sources: 1
---

# Crash forecast false positives

> [!summary]
> Which ex-ante risk measure flags all past crashes while raising the fewest false alarms?

## How it works

- **How**: fix a loss threshold X. Over the months that lost more than X, take the lowest value Y reached by the risk measure. Count the months with the measure at or above Y that did not lose more than X. Repeat for each measure and threshold.
- **Reading**: the measure with fewer false positives separates crash months from the rest more sharply.
- **Data needed**: the ex-ante value of each risk measure and the strategy return, same dates.

## What the sources say

### Parameters
- **Daniel 2012**
	- X = 10%, 20%, 30%, 40% (Table 8)
	- Measures: HMM turbulent probability; GARCH(1,1) and 3, 6, 12, 36-month RV of momentum and of the market; past 3 to 36-month market return (p. 22)
	- US momentum, 1930-2013 (p. 22)

### Why
- **Daniel 2012**: left-tail risk relates to skewness and need not move with volatility (p. 21)

### Evidence
- **Daniel 2012**: real data, gross; whether probabilities use full-sample parameters is not stated
	- At -20%: HMM 114, HMM without call term 150 (Table 8)
	- At -20%: momentum RV 147 (12m) to 227 (3m), GARCH 256; market RV 159 to 184 (Table 8)
	- At -10%: HMM 902, market RV 12m 796, market GARCH 809 (Table 8)

### Limits
- **Daniel 2012**
	- 13 crashes at the -20% threshold (Table 7)
	- No out-of-sample count (p. 23; Fig. 2B)

## Sources

- [[2012 - Daniel Jagannathan Kim - Tail Risk in Momentum Strategy Returns]] (Daniel 2012)
