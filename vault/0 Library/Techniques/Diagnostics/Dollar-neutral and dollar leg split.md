---
type: diagnostic
kind: attribution
aliases: [dollar-neutral carry, pure dollar carry, EQ0 and EQ-minus decomposition, base currency exposure split]
sources: 1
---

# Dollar-neutral and dollar leg split

> [!summary]
> Does the strategy's return come from the cross-sectional bet, or from its net exposure to the base currency?

## How it works

- **How**: build a version of the strategy with zero net exposure to the base currency: rank the other assets on the same signal, long those above the median, short those below, at the same gross size. Subtract its positions from the original strategy's positions; what remains is the base-currency leg. Study the two legs separately: moments, factor regressions, alphas.
- **Reading**: if one leg carries the alpha and the other is explained by known factors, the source of the abnormal return is the first leg.
- **Data needed**: the strategy's positions per asset, the signal per asset, asset returns, factor returns.

## What the sources say

### Parameters
- **Daniel 2014**
	- Dollar-neutral leg (EQ0): long (short) the four currencies with rates above (below) the median of the nine non-USD rates, scaled to the size of EQ (p. 15-16).
	- Dollar leg (EQ-minus) = EQ minus EQ0 (p. 16-17).
	- Pure dollar portfolio (EQ-USD): long (short) USD vs all nine when the USD rate is above (below) the median (p. 15-18).

### Why
- **Daniel 2014**: isolates the source of the abnormal returns; the only difference between EQ and EQ0 is the dollar exposure (p. 16).

### Evidence
- **Daniel 2014**: real data, in-sample, gross of costs.
	- EQ0 1.61% a year, Sharpe 0.49; EQ-minus 2.35%, Sharpe 0.61; correlation -0.11 (p. 16-17; Table 8).
	- EQ0 on Fama-French 3 factors: alpha t 1.54; market and HML explain about 45% of its mean. EQ alpha 3.39, t 3.76 (p. 16; Table 9).
	- EQ-USD alpha 4.52% (t 2.79) with all factors at once (p. 18-19, 33; Table 12).

### Limits
- **Daniel 2014**
	- EQ-USD is "not strictly a carry trade"; its down-market return may come from currencies far from the median (p. 21, fn. 15).
	- EQ-minus is under-diversified, which may explain its large kurtosis (p. 18).

## Sources

- [[2014 - Daniel Hodrick Lu - The Carry Trade Risks and Drawdowns]] (Daniel 2014)
