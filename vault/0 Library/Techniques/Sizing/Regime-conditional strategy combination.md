---
type: technique
brick: sizing
aliases: [Regime rotation, State-to-asset allocation map, conditional hedge, 50/50-dyn, conditional value-momentum combination, state-dependent strategy weights]
sources: 2
tested_on: [equities, multi-asset]
---

# Regime-conditional strategy combination

> [!summary]
> Holds a main strategy alone in normal states and adds a hedging strategy only when an ex-ante state signal flags the risky state.

## How it works

- **Rule**: fixed weights per state: main strategy alone in the normal state, main plus hedge in the risky state.
- **Risk estimate**: an ex-ante state probability or score, cut into groups.
- **Aggregation**: fixed weights across the two strategies within each state.
- **Implied leverage**: set by the weights; no volatility scaling in the base rule.
- **Variant**: assets instead of strategies: in each regime hold the asset with the highest state-conditional mean (Top-1), or 60% of the best and 40% of the second.

## What the sources say

### Parameters
- **Daniel 2012**
	- 0.5 momentum + 0.5 value when the turbulent probability is in its top tertile, else 1.0 momentum (Table 13, p. 35)
	- Value: value-weighted top minus bottom B/M decile, NYSE breakpoints (p. 30)
	- US stocks, monthly, 1927-2013 (Table 13)
- **Verma 2026**
	- Top-1: 100% SPY in state 0, GLD in state 1, TLT in state 2; 60/40 pairs the best with the second-best (Table 4, p. 4)
	- Long-only, SPY, TLT, GLD, daily, one-day lag (p. 4-5)

### Why
- **Daniel 2012**: value and momentum are negatively correlated only in the high-probability state (p. 35)
- **Verma 2026**: asset payoffs differ by regime, SPY best when calm, safe assets in stress (p. 4)

### Evidence
- **Daniel 2012**: real data, in-sample, gross
	- Sharpe 0.91 vs 0.76 static 50/50 and 0.52 momentum alone (Table 13)
	- Months below -10%: 8 vs 13 static and 56 momentum (Table 13)
	- Conditional MVE with ex-post means and variances: Sharpe 1.05 (Table 13)
- **Verma 2026**: real data, 30% test window, gross, costs zero (p. 6)
	- Test Sharpe Top-1 0.79, 60/40 0.82, equal-weight 0.83, SPY 0.65 (Table 7)
	- Test drawdown Top-1 -21.8%, 60/40 -29.3%, SPY -35.7% (Table 7)

### Limits
- **Daniel 2012**
	- Tertile breakpoints are full-sample; whether the probabilities use full-sample parameters is not stated (Table 10, Table 13)
	- The three combined portfolios show the same SD, 3.87%; no scaling described (Table 13)
	- No costs (whole paper)
- **Verma 2026**
	- Rotation does not beat the equal-weight Sharpe in the test window (Table 7)
	- The map is the state means of Table 3, whose train-only estimation is not stated (p. 4-5)
	- Table 4 and the RL map in Table 5 disagree for states 1 and 2

## Sources

- [[2012 - Daniel Jagannathan Kim - Tail Risk in Momentum Strategy Returns]] (Daniel 2012)
- [[2026 - Verma Putri Lesupi - Regime-Based Portfolio Allocation Using Hidden Markov Models and Reinforcement Learning]] (Verma 2026)
