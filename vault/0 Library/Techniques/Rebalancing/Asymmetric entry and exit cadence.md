---
type: technique
brick: rebalancing
aliases: [Biweekly entries, weekly exits, Slow in, fast out]
sources: 1
tested_on: [equities]
---

# Asymmetric entry and exit cadence

> [!summary]
> Opens new positions on a slow calendar and checks exits on a faster one.

## How it works

- **Frequency or trigger**: entries only on every k-th review date; exit conditions checked at every review date.
- **Band**: none. The asymmetry is in the calendar.
- **Cost rationale**: a slower entry calendar filters false signals and cuts turnover while exits still act at once.

## What the sources say

### Parameters
- **Unknown 2026**
	- Entries every other Friday (freq = 2); exits (native, stops, take-profit) every Friday (p. 8, 10)
	- 20 bp per side; free slots wait for the next entry date (p. 7-9)

### Why
- **Unknown 2026**: biweekly entries filter false positives of weekly momentum and reduce overtrading; weekly exits cut losses (p. 8)

### Evidence
- **Unknown 2026**: real data, in-sample, net of 20 bp per side
	- Full design: 16.8 slot changes a year, cost toll about 0.7 to 0.9 pp a year (Table 3 A, p. 19)
	- A fully discrete run (entries and exits at the same date) at six frequencies is described, not shown (p. 11, 23-24)

### Limits
- **Unknown 2026**
	- No run of the asymmetric calendar against a symmetric one at the same entry date (p. 8, 11)
	- Exit fills at the same close that triggers them (p. 8, fn 5)

## Sources

- [[2026 - Unknown authors - Momentum Strategies in ETFs under Simple Operational Rules]] (Unknown 2026)
