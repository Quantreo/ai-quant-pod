---
type: technique
brick: signal
aliases: [Inventory signal, I/I*, Inventory deviation from normal]
sources: 1
tested_on: [commodities]
---

# Normalized inventory signal

> [!summary]
> Compares each commodity's inventory with its normal level and goes long the commodities whose stocks are short.

## How it works

- **Inputs**: inventory level of each commodity, from exchange or government reports.
- **Formula**: inventory divided by a normal inventory taken from a smooth trend of past inventories.
- **Lookback / holding**: the trend is fitted on the inventory history; positions are held for a set period, in months.
- **Output**: a ratio, below 1 when stocks are short.
- **Direction**: long low-inventory commodities, short high-inventory ones.
- **Tested on**: commodity futures.

## What the sources say

### Parameters
- **Gorton 2007**
	- Normal inventory I* from an HP filter on log inventories, smoothness 160,000 x 81 for monthly data, chosen by visual inspection (p. 12, fn. 8)
	- Monthly sort into halves, long the lowest I/I*, equal weight (p. 16, 19)

### Why
- **Gorton 2007**
	- Low inventories raise stock-out risk and future spot volatility, so the risk premium rises (p. 8, 16)
	- The trend is removed to measure the deviation from normal (p. 12)

### Evidence
- **Gorton 2007**: real data, in-sample, gross, low minus high half
	- 1969-2006: 8.06% a year, t = 3.19, positive in 56.53% of months (Table 5)
	- 1990-2006: 8.75% a year, t = 2.82 (Table 5)
	- Direct regressions of returns on I/I*: significant only for Meats (t = -2.22) (Table 4)

### Limits
- **Gorton 2007**
	- Publication lags and revisions of inventory data are not controlled in the sort (p. 2, 17)
	- I/I* is not comparable across commodities, yet the sort ranks across them (p. 18)
	- HP smoothness picked by eye; whether I* is estimated in real time is not stated (fn. 8)
	- Wrong-sign coefficients for Palladium, Aluminum, Tin, Corn (Table 4)

## Sources

- [[2007 - Gorton Hayashi Rouwenhorst - The Fundamentals of Commodity Futures Returns]] (Gorton 2007)
