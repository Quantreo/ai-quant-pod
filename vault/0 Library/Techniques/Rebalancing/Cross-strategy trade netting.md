---
type: technique
brick: rebalancing
aliases: [trading diversification, netting of trades across factors, cross-factor trade netting]
sources: 1
tested_on: [equities]
---

# Cross-strategy trade netting

> [!summary]
> Nets the rebalancing trades of several sleeves of a portfolio at the asset level before charging costs, so opposite trades cancel.

## How it works

- **Frequency or trigger**: at each rebalance, compute every sleeve's target holding in each asset, add them, and trade only the difference from the current combined holding.
- **Band**: none; netting is exact.
- **Cost rationale**: a cost is paid on the net trade per asset, not on each sleeve's own trade. Sleeves that trade in opposite directions in the same asset pay nothing on the overlap.
- **Variant**: net only inside one sleeve and its managed version, or not at all, to measure how much comes from netting across sleeves.

## What the sources say

### Parameters
- **DeMiguel 2024**
	- Cost = sum over stocks of half the bid-ask spread times the absolute net trade; the netted trade is the sum over the nine factors of target weight minus drifted weight (Eq. 7-10, p. 9-10).
	- Un-netted alternative: charge each factor's trade before adding (Eq. 11, p. 10).
	- Half-spread from the two-day Abdi and Ranaldo estimator, monthly average (Eq. 12, p. 10).

### Why
- **DeMiguel 2024**: managed factors trade more, so netting helps the conditional portfolio more than the unconditional one (p. 3, 23).

### Evidence
- **DeMiguel 2024**: real data, out of sample, net, nine US equity factors, 1977-2020
	- Conditional multifactor Sharpe 0.739 with no netting, 0.783 netting within each factor, 1.062 netting across all factors (Table IV).
	- Cost of the conditional portfolio 0.358, 0.339, 0.213 in the three cases (Table IV).
	- Four of nine managed factors have negative net mean return without netting; all nine positive with it (p. 3, Fig. 5).

### Limits
- **DeMiguel 2024**
	- Stock-level trades from rebuilt factors, with estimated spreads; no price impact in the main text (p. 6, 10).
	- Gain measured on one portfolio, nine factors (Table IV).

## Sources

- [[2024 - DeMiguel Martin-Utrera Uppal - A Multifactor Perspective on Volatility-Managed Portfolios]] (DeMiguel 2024)
