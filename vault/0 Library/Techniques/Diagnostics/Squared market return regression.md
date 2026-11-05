---
type: diagnostic
kind: attribution
aliases: [straddle-like payoff test, quadratic CAPM]
sources: 2
---

# Squared market return regression

> [!summary]
> Is the strategy's payoff straddle-like, gaining when the market moves a lot in either direction?

## How it works

- **How**: regress the strategy return on the market return and the squared market return, on quarterly data.
- **Reading**: a positive, significant coefficient on the squared return means the largest gains come in extreme markets, up and down.
- **Data needed**: strategy and market returns over the same quarters.

## What the sources say

### Parameters
- **Moskowitz 2012**
	- Quarterly returns (Table 3C).
- **Ivanova 2014**
	- Variant: quadratic CAPM, strategy excess return on market and squared market return, monthly (Eq. 16, p. 17)
	- Run on 12 rank-sorted FX portfolios, June 1977 to December 2012 (Table 4)
### Why
- **Moskowitz 2012**: tests for a straddle-like payoff (p. 238).
- **Ivanova 2014**: tests whether the squared market return prices the technical returns (p. 17)
### Evidence
- **Moskowitz 2012**: real data, in-sample, gross of costs.
	- Squared market return coefficient 1.99, t = 3.88 (Table 3C).
	- Largest quarterly returns come with the biggest S&P 500 moves, up and down (≈ Fig. 4, p. 238-239).
	- No significant relation with TED spread, VIX or sentiment (Table 3C, p. 239-240).
- **Ivanova 2014**: real data, in-sample
	- Betas on the squared return mostly positive and significant; price of risk 0.17, t = 1.68, wrong sign for a risk premium (p. 19, Table 4)
	- R2 without a constant -0.13 (Table 4)
### Limits
- **Moskowitz 2012**
	- Not stated.
- **Ivanova 2014**
	- Betas on the market itself are negative, so the model deepens the puzzle (p. 18)

## Sources

- [[2012 - Moskowitz Ooi Pedersen - Time Series Momentum]] (Moskowitz 2012)
- [[2014 - Ivanova Neely Weller et al - Can risk explain the profitability of technical trading in currency markets]] (Ivanova 2014)
