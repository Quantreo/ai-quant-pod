---
type: diagnostic
kind: attribution
aliases: [CAPM in crisis, conditional market beta, rolling market beta, correlation spread test]
sources: 1
---

# Crisis-window market beta

> [!summary]
> Does a strategy with a small average market beta become exposed to the market when stress hits?

## How it works

- **How**: regress the strategy, or each portfolio, on the market excess return over a rolling window and over the months before chosen crisis dates. Report beta, alpha and R² per window. Also track the correlation with the market of the top portfolio minus that of the bottom portfolio.
- **Reading**: a near-zero average beta with large betas in stress windows means the premium is paid for market risk that shows up when it hurts. Alpha per window shows whether the premium survives each episode.
- **Data needed**: strategy or portfolio returns, market excess return, same dates, daily observations for short windows.

## What the sources say

### Parameters
- **Lustig 2008**
	- Rolling 12-month window, monthly returns observed daily, for the correlation spread and the carry beta (p. 28; Fig. 5).
	- Six-month windows (129 days) ending 26 May 1998, 2 Aug 1995, 10 Oct 1999, 31 Aug 2007; Newey-West with 20 lags (p. 28; Table 11).
	- Market: CRSP value-weighted US return (p. 27; Table 11).

### Why
- **Lustig 2008**: the average beta is too small to explain carry premia, but the conditional beta varies a lot through time (p. 27).

### Evidence
- **Lustig 2008**: real data, in-sample, net of bid-ask, 11/1983-03/2008.
	- Carry factor market beta 1.11, 1.22, 0.37, 0.62 in the four windows; alpha -2.71%, -3.82%, +0.96%, +0.29% over six months (Table 11).
	- Correlation spread between top and bottom portfolios jumps by 0.5 to 0.9 in crises (p. 28).
	- Average portfolio market betas only -0.05 to 0.08 (p. 27).

### Limits
- **Lustig 2008**
	- No rule for choosing the crisis dates is stated (p. 28).
	- Table 11 note says portfolios are sorted on past returns; the text says forward discounts (p. 28).
	- Overlapping monthly returns observed daily.

## Sources

- [[2008 - Lustig Roussanov Verdelhan - Common Risk Factors in Currency Markets]] (Lustig 2008)
