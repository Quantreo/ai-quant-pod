---
type: diagnostic
kind: performance
aliases: [Holdout test, Train-test split, Pure out-of-sample test, Best in-sample rule out of sample, Expanding-window out-of-sample test]
sources: 4
---

# Chronological holdout test

> [!summary]
> Does the rule picked on an early period still work on a later period that played no part in the choice?

## How it works

- **How**: run the whole selection (rule, parameters, cutoffs) on the first period only, freeze the choice, then measure it on the following period against the benchmark.
- **Reading**: a frozen choice that keeps beating the benchmark supports a stable effect; a choice that changes or fails points to selection on noise.
- **Data needed**: the full candidate set and a later period kept apart.
- **Variant**: expanding window: re-estimate on all data up to each month, trade the next month, and compute the in-sample figures over the same dates for a fair comparison.

## What the sources say

### Parameters
- **Hudson 2019**
	- Best rule per coin to 31 Dec 2017, tested January to June 2018 (p. 212-213)
- **Wu 2026**
	- Select among 300 candidates on 2016-2020, test on 2021-2025 at 0, 1, 2 bps (p. 13, Table 13)
- **Verma 2026**
	- Daily 2004-2025, first 70% train, last 30% test; HMM and policy fit on train, one-day execution lag (p. 5)

- **DeMiguel 2024**
	- Expanding window, first estimation window 120 months from January 1967; out-of-sample 1977-2020 (p. 6).
	- In-sample results computed over the same 1977-2020 dates (p. 6, 14).

### Why
- **Hudson 2019**: another guard against data snooping; rule performance tends to fade over time and after publication (p. 212)
- **Wu 2026**: stricter than applying full-sample choices to sub-periods (p. 13)
- **Verma 2026**: "mitigating backtest overfitting concerns" (p. 5)

- **DeMiguel 2024**: same design as Cederburg et al. (2020), to compare with their out-of-sample finding (p. 14).

### Evidence
- **Hudson 2019**: real data, out of sample, gross
	- Annualised return as printed: Bitcoin best rules -0.0010 and -0.0091; Litecoin, Ripple, Ethereum 0.0546 to 0.0775 (Table 9)
- **Wu 2026**: real data, out of sample
	- Bitcoin: the training pick changes to 11:00 Momentum/Long and ends at 23.6% of buy-and-hold wealth (Table 13)
	- Ethereum: the same 05:00 Long/Reversal is picked again; wealth ratio 13.4 (0 bps), 6.4 (2 bps) (Table 13)
- **Verma 2026**: real data, out of sample, gross, costs zero (p. 6)
	- RL Sharpe 0.83 against equal-weight 0.83 and SPY 0.65 (Table 7)

- **DeMiguel 2024**: real data, gross unless stated
	- Market Sharpe 0.530 unmanaged, 0.585 managed in-sample, 0.408 managed out of sample (Table I A, C).
	- Out-of-sample Sharpe below in-sample for all nine managed factors (Table I C, p. 15).

### Limits
- **Hudson 2019**
	- Six months, one rule per coin, bear market (p. 212-213)
- **Wu 2026**
	- One historical split, not a rolling or live test (p. 24)
- **Verma 2026**
	- One split of about 6.3 years (computed), number of variants tried not stated (p. 5)
	- Tables 1-3 are not said to be train-only (p. 3-4)

- **DeMiguel 2024**
	- One expanding-window design; gamma = 5 and one-month volatility fixed beforehand, other settings only in the Internet Appendix (p. 14, fn 16, 28).

## Sources

- [[2019 - Hudson Urquhart - Technical trading and cryptocurrencies]] (Hudson 2019)
- [[2026 - Wu Pinsky - Lagged Momentum and Reversal Across Daytime and Overnight Sessions in Bitcoin and Ethereum]] (Wu 2026)
- [[2026 - Verma Putri Lesupi - Regime-Based Portfolio Allocation Using Hidden Markov Models and Reinforcement Learning]] (Verma 2026)
- [[2024 - DeMiguel Martin-Utrera Uppal - A Multifactor Perspective on Volatility-Managed Portfolios]] (DeMiguel 2024)
