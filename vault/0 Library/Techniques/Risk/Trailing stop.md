---
type: technique
brick: risk
aliases: [Trailing stop loss, TSL, Chandelier exit, Fixed stop loss, Rolling low stop]
sources: 1
tested_on: [equities]
---

# Trailing stop

> [!summary]
> Closes a position when its price falls a set distance below the highest level reached since entry.

## How it works

- **What it limits**: the give-back from the best price of the trade, and so the loss on one position.
- **Trigger / level**: price below the running maximum since entry times (1 - a), checked at each decision date.
- **How the level is set**: the distance a is a parameter, in percent of price. Variants: fixed stop from the entry price; lowest low of the last N periods; running maximum minus a multiple of the ATR (chandelier).

## What the sources say

### Parameters
- **Unknown 2026**
	- Trailing: a in 7%, 10%, 15%, 20% (TSL07 to TSL20), on weekly closes, checked every Friday (Table 1 B, p. 8)
	- Fixed stop from entry: 5%, 7%, 10%, 15%, 20% (Table 1 B)
	- Rolling weekly low over 10, 20 or 40 weeks; chandelier with a 14-week ATR times 2, 3 or 4 (Table 1 B)
	- Long-only ETF portfolio, 8 slots, exit goes to cash at the T-bill rate (p. 7-8)

### Why
- **Unknown 2026**: the trailing stop closes positions quickly in corrections and realizes right-tail gains dynamically, so a fixed take-profit adds nothing (p. 18, 22)

### Evidence
- **Unknown 2026**: real data, in-sample, net of 20 bp per side, 3,215 US ETFs, 2001-2026
	- TSL07: Sharpe 1.336, drawdown -6.98%, CVaR95 1.83%, 16.8 slot changes a year (Table 3 A)
	- Against the same design without stop or take-profit: Sharpe +0.299 (p = 0.01), drawdown +7.10 pp (p = 0.02), CAGR +0.34 pp (p = 0.83) (Table 3 B)
	- TSL07 against TSL10: Sharpe +0.060 (p = 0.38), not distinguishable (Table 3 B)
	- Least hit by weeks with VIX above 25: -0.46 pp a week against -0.62 without a stop (Table 4 A)

### Limits
- **Unknown 2026**
	- 7% is the best of 144 SL/TP rules, 74 of them implementable, picked on the full sample; no hold-out (p. 10, 16)
	- Rules above 20 slot changes a year were dropped by the authors' own cut (p. 16)
	- Exit at the same Friday close that triggers it (p. 8, fn 5)

## Sources

- [[2026 - Unknown authors - Momentum Strategies in ETFs under Simple Operational Rules]] (Unknown 2026)
