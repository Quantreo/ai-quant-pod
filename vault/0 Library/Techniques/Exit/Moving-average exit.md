---
type: technique
brick: exit
aliases: [Death cross exit, Price below moving average exit, Dynamic MA exit, Partial exit at MA50]
sources: 1
tested_on: [equities]
---

# Moving-average exit

> [!summary]
> Leaves a long position, in part or in full, when the price or a short average falls below a longer moving average.

## How it works

- **Trigger**: price below a moving average, or the short average below the long one (death cross), at the decision date.
- **Link to entry**: the same averages can define the entry filter, so the position opens above and closes below the same line. Variant: the exit replaces other exits, or runs alongside them. Variant: partial exit first, full exit later.

## What the sources say

### Parameters
- **Unknown 2026**
	- Native exits: price below MA50 cuts the position to 50%, reversible if price recovers; MA50 below MA200 closes it for good (p. 8)
	- Dynamic exit: price below EMA of 5 weeks or SMA of 50, 100 or 200 days at the weekly close (Table 1 B)
	- Overlay: runs alongside the native exits. Replace: substitutes for them (Table 1 B)
	- Checked every Friday; 3,215 US ETFs (p. 6, 8)

### Why
- **Unknown 2026**: not argued beyond protection of the left tail (p. 20)

### Evidence
- **Unknown 2026**: real data, in-sample, net of 20 bp per side, 2001-2026
	- SMA200 overlay with TP100: Sharpe 1.320, CAGR 14.84%, drawdown -11.04%, 12.5 slot changes a year (Table 3 A)
	- Against no SL or TP: Sharpe +0.283 (p = 0.01), CAGR +1.92 pp (p = 0.08) (Table 3 B)
	- EMA 5-week replace version: Sharpe 1.39 but 51 slot changes a year, above the authors' cut (p. 16)

### Limits
- **Unknown 2026**
	- Best rules chosen from 144 on the full sample; no hold-out (p. 10)
	- Deeper drawdown and weaker CVaR95 than the 7% trailing stop (Table 3 A)
	- Effect of the partial exit alone not isolated (p. 8)

## Sources

- [[2026 - Unknown authors - Momentum Strategies in ETFs under Simple Operational Rules]] (Unknown 2026)
