## Build

**Code**: `strategies/etf_tsmom_12m.py` · sha `48f2a07884af` (lab sha `70e86da018e5`) · built 2026-10-25 on Pass 1 v1 · truncation test (20 trade days, base and twin): PASS · timing: weight dated d uses prices to d and cash to month m-1.

**Scored**: first trade 2006-01-31, first scored month 2006-02, last 2017-12: **143 months = 11.92 years**. t bar 2 means Sharpe 0.579 on that length (Pass 1 said 0.58). Tries: 1 (base); the two controls are logged as controls.

**Gate (1.11)**, train, tiers 2/5 bp, borrow 0.5%:
- **G1 FAIL**: base net monthly on controls, NW 4 lags, t bar 2. Over always-long alpha 0.33%/m, t 1.77; over the one-sign twin 0.25%/m, t 1.43; on both together t 1.45 (1 lag: 1.79, 1.48, 1.50). I fixed beforehand that all three must reach 2 (strictest reading): none does, so the verdict holds on any reading.
- **G2 pass**: net Sharpe 0.606 (monthly), t 2.09, bar 0.579. Daily engine Sharpe: gross 0.588, net 0.525 (control_long net 0.439, twin 0.433).
- Result: G1 kills (Pass 1: "Fail: kill"). Trend adds about 0.09 of Sharpe over the always-long book, not enough to separate from it on 12 years. The alpha reading is conditional on the survivor-selected list of 22 (Data check #3).

| Choice | Pass 1 | Code | Data check |
| --- | --- | --- | --- |
| Return | 1.5 adj_close minus cash | P&L = excess return: engine funding path pays rate/365 a day on longs, credits shorts | #1 |
| Signal | 1.5 sign of 12m excess, month end | month-end to month-end 12 months, cash compounded over months m-12..m-1 | #1 |
| Sizing | 1.5 1/sigma EWMA com 60, lagged | EWMA std to day d (the same convention as the sister crypto build), annualised 252 | none |
| Book | 1.5 8%, 261 days, cap 2 | pairwise covariance of the last 261 returns (min 240 common), cap 2 binds 44 of 144 months | none |
| Universe | 1.4 22 ETFs, 12 months of history | price at month end m-12 required; counts 13 / 15 / 19 / 22 in Jan 2006 / 07 / 08 / 09 | #2 |
| Costs | 1.5 2 bp liquid, 5 bp others | one engine run per tier, summed; no blended cost | brief |
| Borrow | 1.5 0.5% on short gross | per calendar day from held shorts, charged as cost | none |
| G1 controls | 1.11 always-long, one-sign twin | same sizing, cap and costs, rebuilt on names alive at each month end; twin sign from the 1/sigma basket of the members' 12m excess | #2 |
| G2 t | 1.11 net Sharpe t | monthly net returns, t = Sharpe x sqrt(years) | none |

**Data check instructions applied**: #1 cash lag in signal; SHY not used as cash. #2 controls on point-in-time names. #3 stress on the 13 present from 2005 and on the 9 later ones is coded (`stress13`, `stress9`) but is validation work: not run at the gate. #4 USO, DBC, DBA reported alone, no roll term (below). #5 trade at adj_close.

**By ETF, price P&L % of capital (train, base)**: USO +1.41, DBC +5.95, DBA -1.18 (cost -0.19, -0.32, -0.35). Largest: SPY +8.2, VNQ +5.9; worst: UUP -4.2. Total price +61.2, cash -4.1, costs and borrow -6.1.

| Run | Period | Variant | Gross Sharpe | Net Sharpe | Turnover/yr | Funding share | Liquidations |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20261025-140850-train-base | train | base | 0.588 | 0.525 | 6.7 (3.2 at 2 bp, 3.5 at 5 bp) | n/a (cash) | 0 |
| 20261025-140850-train-control_long | train | always-long | 0.445 | 0.439 | 1.4 | n/a | 0 |
| 20261025-140851-train-control_twin | train | one-sign twin | 0.454 | 0.433 | 2.2 | n/a | 0 |

**Measured turnover**: 3.2x (liquid) and 3.5x (others) against 3.0x and 4.0x in 1.7; borrow 0.27%/yr against about 0.3%. Cost in line.

**Not run**: stress13, stress9, borrow 1%, delay-1 control, validation (G1 failed).

---

## 2026-10-25 (later) · Pass 1 v1.3: train gate rerun at 25 bp

**Code**: `strategies/etf_tsmom_12m.py` sha `b770e74c1d23` (borrow 25 bp, stress options, variant A; the base logic is unchanged, the train part of the pooled base gives Sharpe 0.627 against 0.626) and `strategies/etf_tsmom_12m_validate.py` sha `333bb1d8d2e7`. Lab sha `0fdde9124197` on every run below (the 0.5% gate of the first section ran under `70e86da018e5`). Truncation test PASS (base, twin, A). Test never opened.

**Step 1, train gate at 25 bp (counted try)**: run 20261025-160749-train-base (code sha `3e33c03a4fce`, same base logic, before variant A was added). 143 scored months (2006-02 to 2017-12, 11.92 years). Monthly net Sharpe **0.626**, t 2.16, bar 0.579 → **pass**. Engine daily: gross 0.588, net 0.541, t 1.87 (0.525 and 1.81 at 0.5%); daily is under the bar, monthly decides (Pass 1 1.6). Borrow cost 1.64% over the train.

**Not run yet**: validation (Developer, phase validation, after the review).
