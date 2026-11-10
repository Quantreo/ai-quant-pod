## Build

**Code**: `strategies/bond_trend_demeaned.py` · sha `12528950f196` · lab sha `70e86da018e5` · built 2026-11-08 on Pass 1 v1 (short)

**Gate (1.11 #1)**: luck line 0.00, t bar 2 over 10.9 years (Sharpe bar 0.60); measured turnover 7.1/yr, tiered cost 2 to 15 bp → net Sharpe 0.60 needed; measured **-0.27** (t -0.88) → **FAIL**. Gross Sharpe -0.20: the base has no edge before cost either. Pass 1: a fail means "not shown", no retest on this data.

| Choice | Pass 1 | Code | Data check |
| --- | --- | --- | --- |
| Return | 1.5 | month-end adj_close to month-end, minus T-bill/12 | #3, #6 |
| Signal | 1.5 | sign(sum of last 12 monthly excess - 12 x expanding mean of monthly excess) (A1) | none |
| Entry | 1.4 | 36 months after first price in panel, prior-year tier not T5 (A4) | #2, #4 |
| Sizing | 1.5 | sign / EWMA vol (com 60, lagged 1 day) | none |
| Book | 1.5, 1.5b | scale = 10% / realized vol of raw book, past 60 days (A3); gross cap 2x | none |
| Costs | 1.5 | tier bp by ETF and prior year; short borrow 25 bp; gross above 1x pays 50 bp (A2) | #4 |

**Assumptions** (gate phase, written before the run; the Economist reads them if the gate passes)
- A1 12-month excess return = sum of 12 monthly excess returns (not compounded); expanding mean from the first month in the panel.
- A2 Book P&L is excess return over the T-bill on net exposure (cash-neutral); leverage cost is only the 50 bp spread on gross above 1x. T-bill of m-1 for month m.
- A3 Pass 1 gives no vol-target estimator: realized vol of the current raw weights on the past 60 trading days.
- A4 T5 / no-volume prior year = not tradable (Cost Assumptions rule). The 1%-of-volume cap is not applied: Pass 1 gives no capital.
- A5 Rebalance at the last trading day of each month, held a month, no band.

**Data check instructions applied**: #1 sub-periods below; #2 rule on panel as loaded; #3 T-bill m-1; #4 tier by name and year; #5 BWX (non-US govt) and TIP (inflation-linked) are in the book unsplit, no per-name P&L read at the gate; #6 adj_close, month ends on trading days.
**Look-ahead**: truncation test PASS (12 month-ends). Timing: weight dated month-end d uses data to d.
**Lab gap**: engine has one cost and no cash rate; costs, excess return and financing are settled in the file (`settle`) from the engine's positions. Sharpe in the table uses trading days (sqrt 252); the lab summary uses calendar days.

| Run | Period | Variant | Gross Sharpe | Net Sharpe | Turnover/yr | Funding share | Liquidations |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20261108-102539-train-base | 2008-01 to 2018-12 | base | -0.20 | -0.27 | 7.1 | n/a (financing -7.5% total) | 0 |

Sub-periods of net Sharpe (read from the same run): 2008-09 0.15 (3 names), 2010-18 -0.39. P&L over train in %: price -10.6, financing -7.5, cost -6.1. Max drawdown -42.6%, vol 7.9%.

**Measured turnover**: 7.1/yr against 2.4/yr in 1.7. The 2x gross cap binds most months (mean gross 1.83): at 10% vol with bond vol of 5 to 8%, the book is levered, which Pass 1 did not price (1.7 assumes 20% of capital rotated, no financing). Financing alone cost 7.5% over the train.

**Not run**: stress tests (mean warm-up, gross cap, 2x cost), raw-trend twin, validation: gate failed.
