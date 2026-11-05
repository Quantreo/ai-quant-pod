---
type: diagnostic
kind: attribution
aliases: [state-conditional correlation, conditional comovement, residual covariance decomposition]
sources: 1
---

# Regime-conditional correlation

> [!summary]
> Does the correlation between two strategies hold in every state, and how much of it comes from their market exposures?

## How it works

- **How**: split periods into groups by an ex-ante state variable. In each group, compute the correlation and covariance of the two strategies. Regress each on the market (linear, or with a call-payoff term) and recompute on the residuals. Share explained by the market = 1 minus residual covariance over raw covariance. Double-sort on a second state variable to separate the two.
- **Reading**: a hedge present in one state only is a conditional hedge. The residual part points to another common factor.
- **Data needed**: both strategies' returns, market excess return, the state variable, same dates.

## What the sources say

### Parameters
- **Daniel 2012**
	- Tertiles of HMM turbulent probability, breakpoints 14% and 3% (Table 10)
	- Second sort: tertiles of formation-period market return (Table 10 A-1, A-2)
	- Covariance in %² a month (Table 11)

### Why
- **Daniel 2012**: correlation can mislead when residual variances also fall; covariance shows the share explained (p. 33)

### Evidence
- **Daniel 2012**: real data, in-sample, gross, US value and momentum 1927-2013
	- Corr(MOM, VMG) -0.57 in the high tertile, -0.07 in the others, -0.44 overall (Table 10A)
	- Market exposure explains 44% (linear) and 55% (with call term) of high-tertile covariance (p. 33-34; Table 11)
	- Residuals load on liquidity proxies only in the high tertile, significant for value only (Table 12)

### Limits
- **Daniel 2012**
	- Tertile breakpoints are full-sample (Table 10)

## Sources

- [[2012 - Daniel Jagannathan Kim - Tail Risk in Momentum Strategy Returns]] (Daniel 2012)
