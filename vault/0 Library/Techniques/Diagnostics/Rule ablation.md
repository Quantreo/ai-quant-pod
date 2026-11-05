---
type: diagnostic
kind: performance
aliases: [Filter ablation, Layer ablation, Condition subset grid, Jaccard overlap of filters]
sources: 1
---

# Rule ablation

> [!summary]
> Which layer of the rule carries the result, and which conditions only repeat each other?

## How it works

- **How**: run every non-empty subset of the candidate conditions with all other layers fixed, plus a stripped control (no exit, no filter, no cap). Compare each against the control and against the others. Measure how much the selected sets overlap week by week (Jaccard).
- **Reading**: subsets with identical metrics are redundant. A layer that does not beat the control by a significant margin adds nothing. The gap between the stripped version and the full version shows where the result comes from.
- **Data needed**: strategy returns for each subset and each control, and the sets of assets selected at each date.

## What the sources say

### Parameters
- **Unknown 2026**
	- 63 non-empty subsets of six trend conditions, no SL or TP (p. 10, Table 2)
	- Control: same design without SL or TP; stripped version: pure momentum, no filter, cap or exit (Table 3 B, D)
	- Jaccard overlap of selected ETFs, raw universe and under the filter (p. 14)

### Why
- **Unknown 2026**: shows which condition matters and warns against over-parameterizing the filter (p. 10)

### Evidence
- **Unknown 2026**: real data, in-sample, net of 20 bp per side
	- 63 subsets give two Sharpe values, 0.945 and 0.881; Sharpe difference not significant (p = 0.30), nor CAGR, drawdown or CVaR (Table 2 C)
	- Five of six filters pick the same ETFs in 99% of weeks, Jaccard above 0.99, against 0.50 to 0.78 on the raw universe (p. 14)
	- Pure momentum Sharpe -0.17 to +0.22 against 1.336 for the full design (Table 3 D)

### Limits
- **Unknown 2026**
	- The caps and the score are not ablated (p. 8, 20)
	- The adopted subset was picked after the grid, on the same sample (Table 1 note)

## Sources

- [[2026 - Unknown authors - Momentum Strategies in ETFs under Simple Operational Rules]] (Unknown 2026)
