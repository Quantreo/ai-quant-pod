---
type: diagnostic
kind: performance
aliases: [Round number vs arbitrary level test, Bounce frequency test]
sources: 1
---

# Level placebo test

> [!summary]
> Does the price react at the chosen levels more than at arbitrary levels in the same range?

## How it works

- **How**: cut the sample into intervals. In each, measure the bounce frequency (bounces over hits) at the chosen levels and at many sets of arbitrary levels drawn in the same range with the same number of digits. Also measure the average move after a hit that does not bounce.
- **Reading**: count the intervals where the chosen levels beat the arbitrary average; under no effect the count follows a binomial with p = 1/2.
- **Data needed**: high-frequency prices, the level definition, a hit band.

## What the sources say

### Parameters
- **Osler 2001**
	- 347 intervals of about 10 trading days; 10,000 sets of arbitrary levels per interval (p. 26-27)
	- Arbitrary level = interval maximum minus a uniform draw times the range, rounded to the quote digits (note 21)
	- Only intervals with hits for both sets count (p. 28)

### Why
- **Osler 2001**: comparing interval by interval removes the sensitivity of the test to the number of hits (note 20)

### Evidence
- **Osler 2001**: simulated rates, not real data
	- Bounce frequency above arbitrary levels in 10 of 10 series at levels 00 and 50 (Table III)
	- Move after a hit with no bounce larger at round numbers in 10 of 10 series (Table IV)

### Limits
- **Osler 2001**
	- Applied only to the author's simulation in this paper; the real-data version is in Osler 2000 and 2001, not read here (p. 26)
	- Intervals are treated as independent trials (p. 28)

## Sources

- [[2001 - Osler - Currency orders and exchange-rate dynamics Explaining the success of technical analysis]] (Osler 2001)
