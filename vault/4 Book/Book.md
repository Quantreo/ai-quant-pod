---
type: portfolio
name: Desk book
book_vol_target: 10%
---

# Book

> **What this is** : the book you actually run, the one every new strategy of the desk is judged against. One row per strategy, weights in **risk**.
> **Open it** : at every monthly portfolio slot, and the day a strategy enters or leaves. Only you change it: the portfolio manager proposes, never writes here.

## Strategies

| Strategy | Family | Status | Risk weight now | Target | Entered | Halve at (DD) | Cut at (DD) | Next review |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Crypto Thin Losers | reversal | paper | 0% (no money) | 50% | 2026-11-10 | 23.0% | 30.6% | 2027-02 (quarterly re-run) |
| SPY Volatility Managed | low-vol | paper | 0% (no money) | 50% | 2026-11-10 | 18.2% | 24.2% | 2027-02 (quarterly re-run) |

Both strategies are on paper, tracked without capital (Test.md verdicts: Crypto Thin Losers in the ambiguous zone, SPY Volatility Managed pooled t 1.95 against a bar of 2). The risk weights are equal by family. ETF TSMOM 12-Month stays out, in the library (dropping it hurts in only 46% of histories). Source: `vault/4 Book/Reviews/Desk book - Book construction.pdf`.

Halve and cut levels follow the Lab rule (`lab/portfolio.py`): halve at 1.5 × the worst drawdown, cut at 2 × the worst drawdown. The worst drawdown is each strategy alone at 10% vol over the common window 2021-01-29 to 2026-09-30: Crypto Thin Losers -15.3%, SPY Volatility Managed -12.1%. The levels are read on the strategy's own drawdown.

## Returns of each strategy

Desk strategies are read from their runs (train, validation and the opened test of the frozen version). A strategy built outside the desk goes here, with its daily net returns file in `Returns/` (not committed).

| Strategy | Returns file | In `lab/portfolio.py` |
| --- | --- | --- |

## Risk rules of the book

| Rule | Level | Now | Last checked |
| --- | --- | --- | --- |
| Vol target | 10 % | 10.7% (backtest, common window) | 2026-11-10 |
| IDM cap | 2.5 | 1.43 | 2026-11-10 |
| Loss limit (everything halved) | worst book DD × 1.5 = 20.4% | worst book DD -13.6% (backtest) | 2026-11-10 |
| Bad-day correlation | measured, not assumed | all days:  · worst 10 %:  |  |
