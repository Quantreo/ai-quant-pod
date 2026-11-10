# SPY Volatility Managed · Gate reread 2026-10-25

**Verdict: pass the new train gate (level).** Reading of the existing run `20261025-142825-train-base` under house rule 1.11 of 2026-10-25 ([[Gate power diagnostic 2026-10-25]]). No new run, no new try: tries stay 1. Figures from its `monthly.parquet` and `summary.json`.

## Level gate (the only kill on train)

| Figure | Value | Basis |
| --- | --- | --- |
| Train length | 143 gate months, 11.92 years (155 scored, 12.92) | Build |
| t bar | 2 (train over 5 years) | budget.py |
| Luck line | 0.00 (1 try) | budget.py |
| Measured cost | 1.98x/yr at 2 bp = 0.04%/yr; gross-net gap 0.002 Sharpe | Build, budget.py |
| Net Sharpe, monthly | 0.770 on 143 (t 2.66); 0.772 on 155 (t 2.77) | monthly.parquet |
| Net Sharpe, daily engine | 0.648 on 12.93 years, t 2.33 | summary.json |
| Less favourable reading | t 2.33 ≥ 2: **pass** | |
| Power of the gate | 30% at true Sharpe 0.43 (DeMiguel OOS managed market, net), 53% at 0.6; false pass 2.3% | budget.py |

The diagnostic's "t about 2.6" is the level t of the managed book (0.77 x sqrt(11.9)), not a t on the gap to SPY. The gap is tested by the alpha regressions below.

The two Sharpe samplings differ (0.648 daily, 0.772 monthly) with the same P&L: within-month daily volatility is higher than monthly. Both clear the bar. The Analyst should report both.

## Twins on the gate figures (143 months, net)

| Book | Sharpe | t | Beats the base? |
| --- | --- | --- | --- |
| Managed (base) | 0.770 | 2.66 | |
| SPY buy-and-hold | 0.518 | 1.79 | no |
| SPY 12-month trend twin | 0.459 | 1.58 | no (also below SPY) |

No twin replaces the base. Regression betas: SPY 0.85, twin 0.39 (the book loads on trend); mean weight 1.33, cap binds 105 of 143 months.

## Controls: power and place

| Control | Train value | Power at appraisal 0.33 / 0.2 | Place |
| --- | --- | --- | --- |
| Sign: alpha over SPY > 0 | 5.6%/yr, t 1.79 (>0) | 87% at 0.33 (false pass 50%) | qualifies (over 50%), but chosen after the run: reported, not counted as the gate |
| G1 alpha over SPY + twin, t ≥ 2 | t 1.38 | train 19% / 10%; pooled 14.9 yr 23% / 11% | validation criterion V1 |
| G2 same, without 2008-09 and 3 best | t -0.66 | train 17% / 8%; pooled 12.7 yr 20% / 10% | validation criterion V2 |
| SPY-only alpha, t ≥ 2 | t 1.79 | pooled 15.9 yr 25% / 11% | reported, read only |
| P3 tercile premise | not computed | | read only |

## Validation criteria it inherits (train + validation pooled, 2006-02 to 2020-12)

1. **V1 (key, P1)**: alpha over SPY and the trend twin, NW t ≥ 2. Power 23% at 0.33. Can kill.
2. **V2 (P2)**: same regression without the 24 months of 2008-09 and the 3 best signed residuals, t ≥ 2. Power 20%. Can kill. G2 at -0.66 on train is the warning: the train alpha rests on a few months.
3. Proof after test: net t on train, validation and test together ≥ 2 (analyze-backtest rule).

Prior against V1: DeMiguel Martin-Utrera Uppal 2024 find the managed market below the unmanaged market out of sample, net Sharpe 0.433 against 0.519 (Table I C, E), and single-factor management failing out of sample. Expect V1 to fail; a pass would contradict the paper.

## What the Critic should attack

- The level is mostly SPY's equity premium at 1.33x average leverage: the gate passes the market, not the overlay. Is a level pass on a long-only levered book informative at all?
- c fitted on the full train (source fn 5): in-sample vol match; real-time c is the known failure (Cederburg et al. 2020, not in library).
- G2 t -0.66: the alpha is three or four months (2011-09, 2012-06, 2016-03 dropped).
- Twin beta 0.39: part of the gain is trend timing already in the twin.
- Validation (2018-2020) holds 2020-03: one event can decide V1 and V2.
- Correlation with ETF TSMOM 12-Month and Bold Asset Allocation (same equity-timing family).
