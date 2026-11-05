---
type: diagnostic
kind: performance
aliases: [Data-snooping correction, Bonferroni, Holm, Benjamini-Hochberg, Benjamini-Yekutieli, False discovery rate, FWER, Superior Predictive Ability test, SPA, Reality check]
sources: 2
---

# Multiple testing adjustment

> [!summary]
> After searching many rules or parameters, does the best result still beat the benchmark once the number of tries is counted?

## How it works

- **How**: compute a p-value for every rule tried (often by bootstrap), then apply a correction for the whole set: family-wise error (Bonferroni, Holm), false discovery rate (Benjamini-Hochberg, Benjamini-Yekutieli), or a joint test that the best of all candidates beats the benchmark (Hansen SPA, White reality check).
- **Reading**: the share of rules still significant, or the SPA p-value. A best rule that does not survive is consistent with selection luck.
- **Data needed**: return series of every rule tried, and the benchmark.

## What the sources say

### Parameters
- **Hudson 2019**
	- 14,919 rules; individual p-values from a stationary bootstrap, 1,000 draws (p. 200, fn 12)
	- Bonferroni, Holm, BH, BY at 5% (p. 199-200)
- **Wu 2026**
	- Hansen consistent SPA over 300 cutoff-strategy pairs vs buy-and-hold, daily log differential (p. 14)
	- 5,000 stationary bootstrap draws, 7-day expected blocks; Holm within test families (p. 14)

### Why
- **Hudson 2019**: many rules tested raise the chance of false rejections (p. 198-199)
- **Wu 2026**: both the session boundary and the rule are picked by maximising terminal wealth, so the pick is biased (p. 12, 14)

### Evidence
- **Hudson 2019**: real data, in-sample
	- Share of rules significant: none 27.96% to 58.64%; Bonferroni 20.35% to 33.61% (Table 8)
- **Wu 2026**: real data, in-sample
	- SPA p = 0.899 to 0.996 (Bitcoin), 0.656 to 0.771 (Ethereum): no rejection (Table 12)
	- Paired tests of the chosen rules vs buy-and-hold: Holm p 0.50 to 1.00 (Table 11)

### Limits
- **Hudson 2019**
	- Bonferroni and Holm ignore the correlation between rules (p. 199)
- **Wu 2026**
	- Low power: ≈ two decades of data to detect the Ethereum gap (p. 22-23)

## Sources

- [[2019 - Hudson Urquhart - Technical trading and cryptocurrencies]] (Hudson 2019)
- [[2026 - Wu Pinsky - Lagged Momentum and Reversal Across Daytime and Overnight Sessions in Bitcoin and Ethereum]] (Wu 2026)
