---
type: log
---

# Gate power diagnostic · 2026-10-25

Question: do the train gates kill ideas that have no edge, or ideas whose edge the sample cannot show? Read from the 1.11 of every sheet judged on 2026-10-24 and 25 (no run, no try) and the measured gate values in `_Index.md`.

## Two kinds of failure

**Dead on level** (net mean at or below zero, or far under any bar): the kill is right whatever the power.
G10 FX Rule Selection (net t -0.51), G10 FX Rate Shock (-0.07), Country ETF Dividend Yield (-0.99), Country ETF Momentum (-0.13), Sector ETF Momentum (-0.99), UST Ladder Carry (-1.27), FX Value (0.14 vs 0.36), ETF Turn of the Month (window excess t 0.07, below the placebo), and most crypto sheets.

**Positive level, killed by a control with low power** ("not shown", the sheets say so themselves):

| Sheet | Level (train, net) | Level gate | Killing criterion | Its power at a plausible edge |
| --- | --- | --- | --- | --- |
| ETF TSMOM 12-Month | Sharpe 0.61, t 2.09 | pass | alpha over always-long t 1.77 (bar 2) | not stated; about 17 to 25% |
| ETF Bold Asset Allocation | Sharpe 0.92, t 3.18 | pass | alpha over SPY-sign twin + IEF t 0.99; the twin itself makes 0.98 | not stated; about 17% |
| SPY Volatility Managed | Sharpe 0.77 (SPY 0.53) | not a gate | alpha t 1.38, then 116-month rerun | 19%, then 17% (joint lower) |
| ETF Sector Sell in May | Sharpe 0.48, t 1.62 | fail (bar 2) | also alpha t 1.30 | 17 to 33% |
| ETF Cross-Asset Momentum | Sharpe 0.45, t 1.30 | fail (bar 2) | twin beta 0.92: it is the TSMOM twin | 17% |
| ETF Inverse Variance | spread t 0.98 | fail | a bond tilt | 17 to 41% |

## Finding

- Most sheets stack two or three criteria at t 2, and the alpha or twin criteria have 17 to 27% power at a plausible edge (stated in the sheets). Jointly, a real premium of Sharpe 0.4 to 0.6 passes about one time in ten. Over 13 ETF and FX ideas, even if all were real, the desk would keep one.
- A failed low-power criterion is "not shown", not "no edge", and the sheets write it, but the gate treats it as a kill.
- When a simpler twin beats the base (Bold Asset Allocation: twin 0.98 against base 0.92), the desk kills the base and drops the twin, which is the better strategy by Occam.
- Turnover was underestimated in Pass 1 every time, by 1.2 to 2.8x (Rule Selection 145 vs 78, Country Momentum 12.8 vs 4.5, Dividend Yield 5.7 vs 2.2, Sector Momentum 12.9 vs 7.3).

## Proposed rules (to decide by Lucas)

1. At the train gate, kill only on level: net Sharpe above luck line plus cost, at the t bar of the train's length. At most one control at the gate, and only if its power is 50% or more at a plausible edge.
2. A control with less than 50% power never kills on train. It is computed again on train plus validation pooled and read by the Analyst and the Red team; it can still kill there, with its power stated.
3. A twin that beats the base becomes the candidate in its place (one more try in the family).
4. Pass 1 turnover: estimate it from a signal-only dry run on train (no returns), not by hand.

Under rules 1 to 3, read on the existing runs (not tries): ETF TSMOM 12-Month (t 2.09), ETF Bold Asset Allocation or its twin (t 3.18), SPY Volatility Managed (Sharpe 0.77 over 11.9 years, t about 2.6, computed) would go to validation. All three are equity-trend or volatility timing: expect them to be correlated with each other.
