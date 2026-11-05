---
type: diagnostic
kind: attribution
aliases: [signal decomposition, exact decomposition with linear weights, component portfolios]
sources: 1
---

# Signal component return decomposition

> [!summary]
> Which part of a composite signal carries the strategy's return?

## How it works

- **How**: write the signal as a sum of parts. For each part, build a portfolio with weights proportional to the part minus its cross-sectional mean, using the same scaling factor as the full signal. The returns of the part portfolios add up exactly to the return of the full-signal portfolio.
- **Reading**: the part with the large, significant return carries the predictability; parts with opposite signs offset each other inside the full signal.
- **Data needed**: the signal and each of its parts per asset and date, next-period returns.

## What the sources say

### Parameters
- **Menkhoff 2016**
	- Real exchange rate level = level 5 years ago + 5-year change (p. 19).
	- 5-year change = minus the 5-year inflation differential + minus the 5-year spot change (p. 19).
	- Linear weights, quarterly; rank weights as a check (Eq. 7, p. 13; Table 8).

### Why
- **Menkhoff 2016**: tells whether lagged levels or changes drive predictability, and whether the spot or the inflation part does (p. 19).

### Evidence
- **Menkhoff 2016**: real data, 1976-2014, 22 currencies, gross.
	- Level 3.95% a year = lagged level 1.62% (t 1.14) + change 2.32% (t 3.15) (Table 8A).
	- Change 2.32% = inflation part -11.74% (t -4.39) + spot part 14.07% (t 5.01) (Table 8A).
	- Rank portfolios give the same signs, without an exact sum (Table 8B).

### Limits
- **Menkhoff 2016**
	- The absolute amount invested differs across parts, so mean returns are not directly comparable (p. 13).
	- Exact only with linear weights; rank weights do not decompose (p. 14).

## Sources

- [[2016 - Menkhoff Sarno Schmeling et al - Currency Value]] (Menkhoff 2016)
