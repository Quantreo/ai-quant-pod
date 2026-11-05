---
type: diagnostic
kind: attribution
aliases: [drawdowns vs expansions, drawdown-conditional correlations]
sources: 1
---

# Conditioning on factor drawdowns

> [!summary]
> Do the strategies of a family lose together when their common factor is in a drawdown, even if their full-sample correlations are low?

## How it works

- **How**: compute the drawdown of a diversified factor (cumulative return minus its running maximum). Label every date with a negative drawdown as a drawdown period, every other date as an expansion. Report each strategy's mean, volatility and pairwise correlations separately in the two sets, and compare with the long-only version of each asset class.
- **Reading**: strategies that are all negative in the factor's drawdowns share a common risk that unconditional correlations hide. Correlations that rise in drawdowns point the same way.
- **Data needed**: returns of the common factor and of each strategy and passive portfolio, same dates.

## What the sources say

### Parameters
- **Koijen 2013**
	- Factor: global carry factor across nine asset classes (p. 30).
	- Drawdown D_t = cumulative excess return minus its maximum to date; drawdown periods where D_t < 0 (Eq. 29, p. 30-31).
	- Within-period timing: first vs second half of drawdowns and expansions lasting at least four months (p. 32).

### Why
- **Koijen 2013**: full-sample correlations can miss common dynamic movements, since much of carry's return is dynamic (p. 30).

### Evidence
- **Koijen 2013**: real data, in-sample, gross of costs.
	- All nine carry strategies negative in drawdowns, positive in expansions; only half the passive portfolios negative in drawdowns (Table VIII, p. 31).
	- Puts: carry -22% vs passive +132% a year in drawdowns (Table VIII, p. 31).
	- Global recession indicator 0.33 in drawdowns vs 0.19 in expansions (p. 31).
	- Correlations rise in drawdowns for some pairs, e.g. FX-credit 0.03 to 0.48 (Table IX).

### Limits
- **Koijen 2013**
	- Correlation evidence "not overwhelming": many stay near zero (p. 31).
	- Monthly correlations can mislead when asset classes react to the cycle at different speeds (p. 31-32).
## Sources

- [[2013 - Koijen Moskowitz Pedersen et al - Carry]] (Koijen 2013)
