---
type: technique
brick: risk
aliases: [Mandatory diversification, Super-category cap, Sector cap, Concentration limit]
sources: 1
tested_on: [equities]
---

# Category exposure cap

> [!summary]
> Limits how many positions of the portfolio may sit in the same category, so that a ranking cannot fill every slot with the same exposure.

## How it works

- **What it limits**: concentration on one factor or asset class when the top-ranked assets are near copies.
- **Trigger / level**: each asset belongs to one category. When a candidate's category is full, the candidate is skipped and the next one in the ranking is considered.
- **How the level is set**: the category map and one cap per category. The caps can differ by category and should sum to more than the number of slots.

## What the sources say

### Parameters
- **Unknown 2026**
	- 11 super-categories from the Refinitiv sector classification (Table 5)
	- Cap 2 for US large cap and US sector funds; cap 1 for nine others; caps sum to 13 for 8 slots (Table 5, fn 6, p. 8)
	- Applied on entry Fridays, scanning candidates by score (p. 8)

### Why
- **Unknown 2026**: avoids SPY, IVV and VOO taking three slots on the same S&P 500 factor (p. 8)
- **Unknown 2026**: caps are larger where the supply is deeper and, for sector funds, more varied (fn 6)

### Evidence
- **Unknown 2026**: real data, in-sample, net of 20 bp per side
	- The cap is only tested inside the full design, Sharpe 1.336 (Table 3 A)
	- In VIX above 25 weeks the categories move together and the 8 positions fall together (p. 23)

### Limits
- **Unknown 2026**
	- No run with and without the caps (p. 8, 20)
	- Cap values set by the authors without a test (fn 6)

## Sources

- [[2026 - Unknown authors - Momentum Strategies in ETFs under Simple Operational Rules]] (Unknown 2026)
