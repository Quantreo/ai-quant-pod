---
type: diagnostic
kind: attribution
aliases: [signal saturation test, predictive regression on the signal, nonlinear signal fit]
sources: 1
---

# Signal response curve

> [!summary]
> How does the next-period move depend on the size of the signal: linearly, or does it saturate for strong signals?

## How it works

- **How**: pool every instrument and date and regress the next-period change on the signal. Compare a linear fit, a cubic fit and a saturating fit Δ = a + b s* tanh(s / s*). Plot a running average of the next change along the sorted signal.
- **Reading**: the intercept is the long bias and the slope is the predictability. A finite s* means strong signals add little beyond weak ones. A negative cubic term would predict reversal for large signals.
- **Data needed**: the signal and the next-period change, per instrument and date.

## What the sources say

### Parameters
- **Lempérière 2014**
	- 5-month trend signal, monthly, futures only, 240,000 points (Fig. 5).
	- Running average over 5,000 consecutive points along the signal axis (Fig. 5).

### Why
- **Lempérière 2014**
	- A linear relation between move and signal is not obvious a priori (p. 11).
	- The cubic fit's strong reversal for large signals is judged suspicious, hence the tanh (p. 11).

### Evidence
- **Lempérière 2014**: real data, in-sample, futures only.
	- Linear: a = 0.018 ± 0.003, b = 0.038 ± 0.002 (p. 10).
	- Cubic: very small s² term, clearly negative s³ term (p. 11).
	- Tanh: best fit, s* ≈ 0.89, b ≈ 0.075 (p. 11; Fig. 5).
	- a, b and s* hardly change for n from 2.5 to 10 months, numbers not shown (p. 11).

### Limits
- **Lempérière 2014**
	- No fit statistic for the comparison; the cubic coefficients are not reported (p. 11).
	- How Δ is normalised across instruments is not stated (p. 10).
	- No trading rule is built or tested on the saturated signal (whole paper).

## Sources

- [[2014 - Lempérière Deremble Seager et al - Two centuries of trend following]] (Lempérière 2014)
