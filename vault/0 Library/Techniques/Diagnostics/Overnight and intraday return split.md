---
type: diagnostic
kind: attribution
aliases: [Close-to-open and open-to-close decomposition, Overnight vs intraday returns]
sources: 1
---

# Overnight and intraday return split

> [!summary]
> When in the 24-hour day does a return or a strategy's profit accrue: from close to open, or from open to close?

## How it works

- **How**: split each daily close-to-close return into an open-to-close (intraday) part and a close-to-open (overnight) part. Compound each part within the period. Run the same test or portfolio on each part.
- **Reading**: compare the premium, alpha or Sharpe ratio of the two parts. A profit that sits in one part tells when the position is exposed to it.
- **Data needed**: daily open and close prices for each asset, with a reliable open.

## What the sources say

### Parameters
- **Lou 2019**
	- Intraday return = close / open - 1 (p. 195).
	- Overnight return = (1 + close-to-close return) / (1 + intraday return) - 1 (p. 195).
	- Stocks: open is the volume-weighted average price of 9:30 to 10:00, observations under 1,000 shares excluded (p. 194).
	- Equity index futures: open is the busiest minute before noon, close the busiest minute after noon (Table 3).

### Why
- **Lou 2019**: shows when expected returns accrue (p. 195).

### Evidence
- **Lou 2019**: real data, US stocks 1993-2013, gross of costs
	- Market: 0.55% overnight (t = 3.62), 0.38% intraday (t = 1.87). The market is open about 27% of the 24 hours and earns about 40% of the premium (Table 2, p. 198).
	- Momentum long-short, overnight CAPM alpha 0.98%, intraday -0.02% (Table 2, p. 200).
	- Momentum overnight Sharpe ratio 0.77, close to close 0.31 (p. 199).

### Limits
- **Lou 2019**
	- Non-US open prices from Datastream "can be quite misleading" (p. 211, fn 22).
	- Results are gross of costs, which the authors expect to make the strategies "much less attractive" (p. 193).

## Sources

- [[2019 - Lou Polk Skouras - A Tug of War Overnight vs Intraday Returns]] (Lou 2019)
