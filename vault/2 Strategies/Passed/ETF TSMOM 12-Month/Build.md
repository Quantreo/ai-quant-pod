## Build

**Code**: `strategies/etf_tsmom_12m.py` · sha `56ac41f76375` (gate sha `eb47178d5d98`; validation adds only CLI flags --cost-mult/--borrow and the delay shift, base weights unchanged) (lab sha `70e86da018e5`) · built 2026-11-09 on Pass 1 v1 · truncation test (20 trade days, base, twin, A): PASS, rerun after the edits · timing: weight dated d uses prices to d and cash to month m-1.

**Assumptions** (gaps in Pass 1 v1, simplest reading, written before the run):
- A rebalance on the last day of the period earns nothing: left out.
- Pairwise covariance needs 240 common days of the last 261 (the 12-month entry rule ensures it).
- At least 2 names to build a book (the base has 13 or more).
- Gate t computed on monthly net returns, t = Sharpe x sqrt(years); the first trade day's entry cost goes to the first scored month.

**Scored**: first trade 2006-01-31, first scored month 2006-02, last 2017-12: **143 months = 11.92 years**. t bar 2 means Sharpe 0.579. Tries: 1 (base); the two controls are logged as controls.

**Gate (1.11)**, train, 2/5 bp, borrow 25 bp:
- **Level: pass.** Monthly net Sharpe **0.626**, t 2.16, bar 0.579, luck line 0.00. Daily engine: gross 0.588, net 0.541, t 1.87.

| Choice | Pass 1 | Code | Data check |
| --- | --- | --- | --- |
| Return | 1.5 adj_close minus cash | P&L = excess return: the engine funding path pays rate/365 a day on longs, credits shorts | #1 |
| Signal | 1.5 sign of 12m excess, month end | month end to month end, 12 months; cash compounded over months m-12 to m-1 | #1 |
| Sizing | 1.5 1/sigma EWMA com 60 | EWMA std to day d, annualised 252 | none |
| Book | 1.5 8%, 261 days, cap 2 | pairwise covariance of the last 261 returns; cap 2 binds 44 of 144 months; gross 1.54 on average | none |
| Universe | 1.4 22 ETFs, 12 months of history | price at month end m-12 required; 13 / 15 / 19 / 22 names in Jan 2006 / 07 / 08 / 09 | #2 |
| Costs | 1.5 2 bp and 5 bp | one engine run per cost group, summed; no blended cost | none |
| Borrow | 1.5 25 bp on short gross | per calendar day from held shorts, charged as cost | none |
| Controls | 1.11 always-long, one-sign twin | same sizing, cap and costs, on the names alive at each month end | #2 |

**Data check applied**: #1 cash lag, no SHY. #2 point-in-time controls. #3 stress13, stress9 now run. #4 no roll term. #5 adj_close.

| Run | Period | Variant | Gross Sharpe | Net Sharpe (daily) | Turnover/yr | Liquidations |
| --- | --- | --- | --- | --- | --- | --- |
| 20261109-091945-train-base | train | base | 0.588 | 0.541 | 6.7 (3.2 at 2 bp, 3.5 at 5 bp) | 0 |
| 20261109-091946-train-control_long | train | always-long | 0.445 | 0.439 | 1.4 | 0 |
| 20261109-091947-train-control_twin | train | one-sign twin | 0.454 | 0.439 | 2.2 | 0 |

**Measured turnover**: 6.7x against 5.4x estimated in 1.7. Cost in budget.



## Validation runs (v2, base unchanged, no gate rerun)

Monthly = monthly net Sharpe on scored months (decides, 1.6); daily = engine. Folders in `results/etf_tsmom_12-month/`, prefix `20261109-`.

| Run | Period | Kind | Monthly net Sharpe (t) | Daily net Sharpe | Turnover/yr |
| --- | --- | --- | --- | --- | --- |
| 103847-validation-base | 2018-2020, 35 m | base | -0.35 (-0.60) | -0.31 (t -0.53) | 7.8 |
| 103855-train+validation-base | pooled, 179 m | base | 0.467 (1.80) | 0.409 (t 1.58) | 6.6 |
| 103857-...-control_long | pooled | control | 0.379 | 0.364 | 1.3 |
| 103858-...-control_twin | pooled | control | 0.137 | 0.132 | 2.7 |
| 103900-...-A | pooled | variant, try 2 | 0.415 (1.60) | 0.388 | 6.5 |
| 103902-...-stress13 | pooled | stress | 0.508 | 0.418 | 6.0 |
| 103904-...-stress9 | pooled, 168 m | stress | 0.216 | 0.212 | 6.7 |
| 103905-...-base-costx2 | pooled | stress | 0.433 | 0.379 | 6.6 |
| 103907-...-base-borrow100bp | pooled | stress | 0.403 | 0.353 | 6.6 |
| 103939-...-base-delay1 | pooled, 178 m | control | 0.397 | 0.349 | 6.7 |

**Delay control**: shifted to the next trading close (1.5b: "trade at close d+1"), on the price calendar in the strategy file; `lab.checks.delay_test` shifts calendar days, which lands month-end trades on weekends for ETFs. Tell the lab owner.
**Spec gaps**: none that change a result. Only gap, no CLI for stresses existed; flags added, numbers untouched.
**Not run**: test (sealed).
