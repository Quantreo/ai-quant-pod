---
type: diagnostic
kind: performance
aliases: [conditional option-adjusted alpha, Glosten-Jagannathan alpha, alpha net of embedded option]
sources: 1
---

# Option-adjusted alpha

> [!summary]
> Does the strategy still earn alpha once its option-like market exposure is priced at traded option prices?

## How it works

- **How**: regress the strategy return on the market excess return and the excess return of a one-month at-the-money index call (payoff over price, minus the gross risk-free return). The intercept is the alpha. Conditional version: coefficients each month from a regime model, weighted by the state probabilities.
- **Reading**: positive alpha means the strategy pays more than its embedded option exposure is worth; months with negative alpha are months it does not.
- **Data needed**: strategy and market excess returns, risk-free rate, one-month index call prices.

## What the sources say

### Parameters
- **Daniel 2012**
	- α* = α + (1 + Rf)·β+·Vc, Vc the call price (Eq. 14-16, p. 25)
	- Coefficients from HMM moments mixed by Pr(turbulent) (p. 25)
	- S&P 500 one-month at-the-money calls, OptionMetrics, 1996-2013 (Fig. 3)
	- 95% band from 10,000 parameter draws (p. 27)

### Why
- **Daniel 2012**: market-model alphas can show spurious value for payoffs that contain options (p. 6)

### Evidence
- **Daniel 2012**: real data, full-sample HMM, gross, US momentum
	- Mean 1.17% a month; significantly positive in 167 of 216 months (p. 27)
	- Significantly negative in 2008:11, 2008:12, 2009:03 (p. 27)
	- Low point ≈-4.3% a month in late 2008 (≈ Fig. 3)

### Limits
- **Daniel 2012**
	- Needs the residual uncorrelated with the pricing kernel residual (Assumption 1, p. 26); it loads on ROE (t = 2.99) and HML (t = -1.97) (Table 9)
	- Negative months: 10 (p. 27) vs 49 (p. 38), inconsistent in the source

## Sources

- [[2012 - Daniel Jagannathan Kim - Tail Risk in Momentum Strategy Returns]] (Daniel 2012)
