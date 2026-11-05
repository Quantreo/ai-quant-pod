---
type: technique
brick: signal
aliases: [Round number levels, Psychological levels, Support and resistance levels]
sources: 1
tested_on: [fx]
---

# Round number support and resistance

> [!summary]
> Treats round price levels as partial barriers: expects a reversal when the price reaches one, and a stronger trend when it crosses one.

## How it works

- **Inputs**: price series quoted in the market convention, and a list of round levels inside the recent range.
- **Formula**: levels are prices whose last two digits are 00 and 50 (or 00 only). A level is hit when the price comes within a small band of it. A bounce is a move back away from the level over the next one or two periods after the hit.
- **Lookback / holding**: a few periods after the hit.
- **Output**: bounce side (reversal) or continuation side (after a cross).
- **Direction**: against the move at the level, with the move after a cross.
- **Tested on**: currencies.

## What the sources say

### Parameters
- **Osler 2001**
	- Round numbers: last two digits 00 and 50, or 00 only (p. 29)
	- Hit: the rate comes within 0.01% of the level (p. 28)
	- Horizons: one and two periods after the hit (p. 27)
	- Order book data: Sept 1999 to April 2000, three pairs (p. 4)

### Why
- **Osler 2001**: take-profit orders cluster at 00 and reflect trends; stop-loss orders cluster just beyond round numbers and intensify trends (p. 5-6, 18-21)

### Evidence
- **Osler 2001**: order placement on real data; price behaviour in the author's own simulation, not on real prices
	- 9.3% of take-profit orders at 00 against 4.4% of stop-loss orders (p. 18)
	- Stop-loss buys: 14.4% at 01-10 against 7.4% at 90-99 (Table I)
	- Simulated bounce frequency at 00 and 50: +3.47 points over arbitrary levels at one period, in 10 of 10 series (Table III)
	- Real-price results are in Osler 2000 and 2001, quoted: +4.6 points on average over three pairs (p. 30)

### Limits
- **Osler 2001**
	- No real-price test and no trading result in the paper (p. 31)
	- Level 00 only: gap 1.80 points at two periods, bounce above arbitrary in 7 of 10 series (Table III)
	- One bank, seven months (p. 6)

## Sources

- [[2001 - Osler - Currency orders and exchange-rate dynamics Explaining the success of technical analysis]] (Osler 2001)
