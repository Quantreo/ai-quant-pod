---
type: technique
brick: risk
aliases: [OTM option hedge, Crash hedge, Tail hedge]
sources: 1
tested_on: [fx]
---

# Protective option hedge

> [!summary]
> Buys out-of-the-money options alongside a position so that a large adverse move is partly paid back, at the cost of the option premium.

## How it works

- **What it limits**: the loss of the position in a crash, beyond the option strike.
- **Trigger / level**: the option strike; protection starts once the price crosses it.
- **How the level is set**: by the option delta (how far out of the money) and the option tenor, matched to the holding period. Further out of the money costs less and protects less.

## What the sources say

### Parameters
- **Daniel 2014**
	- 10-delta or 25-delta out-of-the-money USD options, bought with each monthly carry position (p. 7-8, 25)
	- JP Morgan quotes, eight currencies against the USD, 2000:09 to 2013:08; SEK excluded (p. 9, 25)

### Why
- **Daniel 2014**: puts a floor on losses from currency crashes (p. 7-8)

### Evidence
- **Daniel 2014**: real data, in-sample, gross, G10 carry 2000:10-2013:08
	- Cost: the hedge cuts the mean return by 34 to 61 bp (10-delta) and 87 to 145 bp (25-delta) (p. 25-26)
	- Hedged equal-weight carry not significant (p = .132 and .198); hedged spread-weighted carry still significant (p = .017 and .022) (Table 17, p. 26)
	- The worst month barely improves: spread-weighted -7.44% unhedged, -6.30% with 10-delta options (p. 26)

### Limits
- **Daniel 2014**
	- Short sample, and USD options only: the authors say this overstates the cost versus the 45 bilateral options (p. 25)
	- Table 17 Sharpe ratios do not match mean over volatility for some lines (Table 17, p. 25)
	- No transaction costs (p. 4)

## Sources

- [[2014 - Daniel Hodrick Lu - The Carry Trade Risks and Drawdowns]] (Daniel 2014)
