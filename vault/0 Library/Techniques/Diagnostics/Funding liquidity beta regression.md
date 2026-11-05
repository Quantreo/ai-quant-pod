---
type: diagnostic
kind: attribution
aliases: [liquidity risk exposure regression, TED spread beta, funding liquidity shock regression, liquidity beta]
sources: 1
---

# Funding liquidity beta regression

> [!summary]
> Does the strategy gain or lose when funding liquidity tightens or loosens?

## How it works

- **How**: take funding spreads (TED, LIBOR minus repo, swap minus T-bill), sign them so a higher value means more liquidity, and keep the residuals of an AR(2) as shocks. Regress the monthly strategy return on each shock, with macro variables as controls. Variant: one index, the first principal component of the shocks.
- **Reading**: a positive coefficient means the strategy does well when funding liquidity improves; a negative one, when it worsens. A zero beta for a mix of two strategies with opposite signs means the mix is immune.
- **Data needed**: monthly interbank and government short rates, the strategy's monthly returns, macro controls.

## What the sources say

### Parameters
- **Asness 2013**
	- Shocks: residuals of an AR(2) on each spread, funding series from January 1987 (p. 19)
	- Funding index: first principal component of the correlation matrix of the shocks, four markets (p. 20)
	- Regressors: the shock alone, plus consumption growth, recession, GDP growth, market, TERM, DEF (p. 18-20)
	- Test the average return series across markets, not each strategy alone (p. 22)

### Why
- **Asness 2013**
	- Funding liquidity may drive value and momentum through leveraged arbitrageurs under funding constraints (p. 4)
	- AR(2) has no special reason; AR(1), AR(3) or first differences give similar results (fn 15, p. 19)

### Evidence
- **Asness 2013**: real data, in-sample, gross, 1987-2011
	- Funding liquidity PC beta: value -0.0094 (t = -4.74), momentum 0.0112 (t = 3.58), 50/50 mix 0.0013 (t = 0.58) (Table IV Panel B)
	- All-liquidity index: value t = -3.25, momentum t = 4.43 on the averaged series (Fig. 4, p. 22)
	- Individual strategies: average t-stats -0.95 and 1.81 (Fig. 4)

### Limits
- **Asness 2013**
	- Market liquidity shocks show little relation to either strategy (Table IV, p. 21)
	- Single strategies show weak betas; the pattern appears only on the average across markets (p. 22)
	- The effect shows up only after August 1998 (Table VII, p. 33)
	- Liquidity explains a small fraction of the premia (p. 27)

## Sources

- [[2013 - Asness Moskowitz Pedersen - Value and Momentum Everywhere]] (Asness 2013)
