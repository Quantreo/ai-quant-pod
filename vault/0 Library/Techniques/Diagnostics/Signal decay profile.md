---
type: diagnostic
kind: performance
aliases: [local projections, impulse response of returns to a signal, predictive horizon profile, long-horizon predictive regression, holding-period alpha decay]
sources: 3
---

# Signal decay profile

> [!summary]
> For how many periods ahead does the signal still predict returns?

## How it works

- **How**: for each horizon h, regress the return h periods ahead on today's signal, with time fixed effects for a cross-sectional reading and optional controls. Plot the slopes and their confidence bands against h. Variant: hold the signal's position h periods and plot its alpha on the benchmark, from non-overlapping returns, against h.
- **Reading**: the horizon where the band first includes zero bounds how long the signal predicts returns.
- **Data needed**: a panel of signals, returns and controls.

## What the sources say

### Parameters
- **Menkhoff 2016**
	- h = 1 to 20 quarters, 5-year real exchange rate change as signal (Eq. 6, p. 12).
	- Controls: lagged returns; in the second version also real rate differential, GDP per capita, export quality, NFA, output gap (Fig. 1).
	- 95% bands, standard errors clustered by quarter (Fig. 1).
- **Moreira 2016**
	- Weights from one month's realized variance, held T months, up to 2.5 years; non-overlapping data (Eq. 6, p. 17).
	- Alpha of the managed portfolio on the unmanaged one; 90% bands (Fig. 6).
- **Menkhoff 2011**
	- Cumulative average return of the long-short portfolio 1 to 60 months after formation, for f = 1, 6, 12; portfolios formed each month, so horizons overlap (Fig. 4, p. 26)
	- Same for spot changes (Fig. A.1)

### Why
- **Menkhoff 2016**: the slopes trace the impulse response of returns to the signal holding fundamentals fixed, local projections as in Jorda 2005 (p. 12).
- **Moreira 2016**: tests whether the result holds at lower frequencies, as volatility forecasts weaken with horizon (p. 2, 16).
- **Menkhoff 2011**: follows Jegadeesh and Titman 2001; a rise then a fall indicates under- then over-reaction (p. 25-26)

### Evidence
- **Menkhoff 2016**: real data, in-sample panel regression, 1976-2014.
	- Without fundamentals: significant up to about one year (p. 12; ≈ Fig. 1).
	- With fundamentals: higher at every horizon, significant up to about two years (p. 12; ≈ Fig. 1).
	- First-quarter slope ≈0.027 without, ≈0.044 with fundamentals (≈ Fig. 1).
- **Moreira 2016**: real data, in-sample, gross
	- Market alpha significant at 10% up to 18 months, then decaying (p. 17).
	- Market appraisal ratio ≈0.3 at one month, ≈0 at 2.5 years (≈ Fig. 6).
	- Same pattern for the FF3 and FF3 plus momentum MVE mixes (p. 17; Fig. 6).
- **Menkhoff 2011**: real data, in-sample, gross
	- Cumulative return peaks after 8 to 12 months (p. 26)
	- f = 1: ≈4.5% near month 12, ≈1.3% at month 60; f = 12: ≈2.2% near month 8, ≈-5.3% at month 60 (≈ Fig. 4)

### Limits
- **Menkhoff 2016**
	- Results shown as a chart only (Fig. 1).
	- A regression, not a traded portfolio.
- **Moreira 2016**
	- Chart only, no table (Fig. 6).
	- FX carry not shown (Fig. 6).
- **Menkhoff 2011**
	- Chart only, no table and no confidence bands (Fig. 4)
	- Overlapping horizons (Fig. 4 caption)

## Sources

- [[2016 - Menkhoff Sarno Schmeling et al - Currency Value]] (Menkhoff 2016)
- [[2016 - Moreira Muir - Volatility Managed Portfolios]] (Moreira 2016)
- [[2011 - Menkhoff Sarno Schmeling Schrimpf - Currency Momentum Strategies]] (Menkhoff 2011)
