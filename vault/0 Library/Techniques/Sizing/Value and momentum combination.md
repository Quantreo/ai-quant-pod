---
type: technique
brick: sizing
aliases: [50/50 value and momentum, COMBO, equal-weight value and momentum mix, value plus momentum]
sources: 1
tested_on: [multi-asset, fx, equities, commodities, rates]
---

# Value and momentum combination

> [!summary]
> Splits risk equally between a value strategy and a momentum strategy, and across markets by inverse volatility, to use their negative correlation.

## How it works

- **Rule**: fixed equal weights on the return series of a value strategy and a momentum strategy built on the same universe.
- **Risk estimate**: volatility of each market's strategy, used only to weight markets against each other; none inside the mix.
- **Aggregation**: half value plus half momentum in each market, then markets weighted by the inverse of their volatility.
- **Implied leverage**: set by the two component strategies; no scaling of the mix.

## What the sources say

### Parameters
- **Asness 2013**
	- r(COMBO) = 0.5 r(VALUE) + 0.5 r(MOM), on the spread (P3-P1) and the rank-weighted factor (Eq. 3, p. 10)
	- Across markets: weight each by the inverse of its full-sample volatility, so each adds about the same volatility (p. 12-13)
	- Ex ante version: each strategy scaled to 2% a year with a rolling three-year volatility, similar results, shown in the appendix (p. 31)

### Why
- **Asness 2013**: two positive premia with a correlation near -0.5 put the mix much closer to the efficient frontier than either alone (p. 3-4)

### Evidence
- **Asness 2013**: real data, in-sample, gross, 1972-2011
	- All classes: Sharpe 1.36 (spread) and 1.45 (factor), against 0.72 to 0.81 for value or momentum alone (Table I Panel B)
	- Currencies 1979-2011: 0.63 and 0.69, against 0.34 to 0.44 alone; correlation -0.42 and -0.43 (Table I Panel B)
	- Commodities: 0.71 and 0.77 against 0.26 to 0.53 alone (Table I Panel B)
	- Funding liquidity beta of the mix 0.0013 (t = 0.58), against -0.0094 and 0.0112 for the two parts (Table IV Panel B)

### Limits
- **Asness 2013**
	- No costs (p. 29)
	- Bonds: mix Sharpe 0.19 and 0.20, the parts are not significant (Table I Panel B)
	- Printed factor mix means exceed both components, and the text says 1.42 where the table says 1.36 and 1.45 (Table I, p. 13)
	- Full-sample volatility weights are not known in advance (p. 31)

## Sources

- [[2013 - Asness Moskowitz Pedersen - Value and Momentum Everywhere]] (Asness 2013)
