---
type: technique
brick: signal
aliases: [Interest rate based sector rotation, Cyclical and defensive rotation, Easing and tightening rotation, Fed-based sector rotation]
sources: 1
tested_on: [equities]
---

# Monetary policy sector rotation

> [!summary]
> Holds cyclical sectors when the central bank cuts rates and defensive sectors when it raises them.

## How it works

- **Inputs**: the policy rate of the central bank of the market, and a split of the sectors into a cyclical and a defensive basket.
- **Formula**: label each period easing (rate falling) or tightening (rate rising); invest in the basket that matches the label, usually the strongest sectors of that basket on past return.
- **Lookback / holding**: the regime lasts until the rate changes direction; the sector pick has its own lookback and holding period.
- **Output**: the basket, and the sectors held, for the period.
- **Direction**: long only.
- **Tested on**: sector ETFs, US and European large caps.

## What the sources say

### Parameters
- **Valach 2024**
	- US Fed Funds Target Rate, European ECB Refinancing Rate; falling rate is easing, rising rate is tightening (p. 23)
	- Easing: cyclical basket. Tightening: defensive basket (p. 23)
	- Cyclical and defensive "based on GICS"; Energy is defensive, Telecommunications cyclical (p. 23, Table 3)
	- Inside the basket: top 3 sectors on past J-month return, equal weight (see [[Cross-sectional momentum]]) (p. 23-24)
	- Regime dates: 6 US periods from 2000, 6 European from 2001 (Tables 1-2)

### Why
- **Valach 2024**: sectors perform differently across the economic cycle; the policy rate is the indicator that signals the shift (p. 22-23)

### Evidence
- **Valach 2024**: real data, in-sample, gross, zero costs, no hold-out, March 2004 to March 2023
	- US, tightening months: best portfolio 0.79% a month, Sharpe 0.25, risk 3.20%; S&P 500 0.74%, 0.21, 3.58% (Table 4)
	- US, easing months: none has lower risk than the S&P 500 (Table 4)
	- Europe, tightening months (50): portfolios -0.29% to 0.14% a month; STOXX 600 -0.36% (Table 5)
	- Europe, all months: portfolio ends ≈310 against ≈190 for STOXX 600, from 100 (≈ Fig. 2)

### Limits
- **Valach 2024**
	- No comparison with the same momentum ranking on all sectors, or with one basket only (not addressed)
	- Not stated how a month is assigned to a regime, or whether the regime is known at trade time (p. 23)
	- US benchmark is total return, European benchmark a price index (p. 23)
	- Costs set to zero; short sample; the best cell was chosen on the full sample (p. 24, 28)

## Sources

- [[2024 - Valach Paciga Bohdalova - Application of Sector Rotation in Active Portfolio Management for US and EU Stock Markets]] (Valach 2024)
