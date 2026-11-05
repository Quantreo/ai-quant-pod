---
type: diagnostic
kind: performance
aliases: [rolling 10-year P&L, drawdown duration check, is the recent drawdown normal]
sources: 1
---

# Rolling performance against history

> [!summary]
> Is a recent flat or losing stretch unusual given the strategy's own long history?

## How it works

- **How**: at each date, compute the P&L over the trailing window of W years. Compare the current value with the historical average and with past lows. Variant: compare a drawdown's length with the typical duration of 1/S² years for a strategy with Sharpe ratio S.
- **Reading**: a current value inside the historical range is read as compatible with a statistical fluctuation. A window that is never negative shows persistence.
- **Data needed**: a long P&L history of the strategy.

## What the sources say

### Parameters
- **Lempérière 2014**
	- W = 10 years, on two centuries of monthly trend P&L (p. 12; Fig. 7).

### Why
- **Lempérière 2014**: to test whether the plateau since 2011, which some attribute to crowding, is significant (p. 11-12).

### Evidence
- **Lempérière 2014**: real data, in-sample, gross of costs.
	- The 10-year P&L was never negative in two centuries (p. 12; Fig. 7).
	- The current value is slightly below the historical average (p. 12).
	- The 1940s were much worse than today (p. 12; Fig. 7).
	- At Sharpe 0.7, typical drawdowns last 2 years, and 4 years is not exceptional (p. 11).

### Limits
- **Lempérière 2014**
	- No formal test or p-value (p. 12).
	- 1/S² is taken from cited work, not derived or checked here (p. 11).
	- W = 10 is not argued; units are arbitrary (Fig. 7).

## Sources

- [[2014 - Lempérière Deremble Seager et al - Two centuries of trend following]] (Lempérière 2014)
