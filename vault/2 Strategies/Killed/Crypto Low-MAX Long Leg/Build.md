## Build

**Code**: `strategies/crypto_low_max_long_leg.py` · sha `3690ec3e3017` · lab sha `70e86da018e5` · built 2026-11-08 on Pass 1 v2 (short)

**Gate (1.11 #1)**: price-only net Sharpe (price minus cost, funding excluded), luck line 0.30 (2 tries), t bar 1 over 3.0 years (Sharpe bar 0.58); cost measured at 54.5 turnover/yr x 5 bp = 2.7%/yr → measured **0.24** (t 0.42) → **FAIL** on both the luck line and the t bar. Price-only gross Sharpe 0.36 (bar to clear cost: 0.30 + 0.13 on estimate, 0.30 + 0.14 measured).

| Choice | Pass 1 | Code | Data check |
| --- | --- | --- | --- |
| Universe | 1.4 | `crypto_universe` top 30, 30 d, age 60, min_names 30 (mean volume), BTC dropped after ranking | #1, #2 |
| Signal | 1.5 | max of 7 daily mark-close returns, all 7 needed | none |
| Leg | 1.5, 1.5b | lowest 6 (floor(0.2 n + 0.5), A1), ties by symbol, below 5 flat | none |
| Hedge | 1.5, 1.5b | short equal-weight universe x beta of equal-weight leg on 90 d, clip 0.5 to 1.5 | none |
| Book | 1.5, 1.5b | 20% target on 60 d realized vol of the weights, gross cap 2x | none |
| Timing | 1.5b | weight dated Monday, formation data to Sunday bar, trades Tuesday 00:00 close | #5 |
| Cost | 1.7 | 5 bp one way; funding by print, engine | #3, #4, #5 |

**Assumptions** (gate phase)
- A1 Quintile size: floor(0.2 x eligible + 0.5) (29 names gives 6).
- A2 Beta falls back to flat week if under 30 valid return pairs (never hit in practice, not counted).
- A3 Hedge divides by the number of universe names at formation (29), each short at beta / 29.
- A4 Vol target scales the whole spread (leg and hedge) to 20% by one factor.
- A5 Pass 1 gives no per-position leverage: no liquidation check (0 liquidations by construction).
- A6 Gate is computed from price + cost + liquidation columns of the run.

**Data check instructions applied**: #1 function as is, "mean" volume ranking; #2 BTC dropped after ranking; #3 days without a print are 0 in the engine, counted: 234 held name-days without a print, flagged, not read; #4 mark price, LUNA and FTT kept (3 delisting exits); #5 print-level funding by the engine, Tuesday fill.
**Look-ahead**: truncation test PASS (12 Mondays).

| Run | Period | Variant | Gross Sharpe | Net Sharpe | Turnover/yr | Funding share | Liquidations |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20261108-102634-train-base | 2021-01 to 2023-12 | base | 0.24 (price+funding), 0.36 price only | 0.12 all-in, 0.24 price only | 54.5 | -0.49 (funding negative) | 0 |

P&L over train in %: price +25.0, funding -8.2, cost -8.2. Max drawdown -34.9%, net vol 23.3%.

**Measured turnover**: 54.5/yr against 26/yr in 1.7. Cost 8.2% over 3 years, 3x the 1.30%/yr estimate. Breakeven cost 10.3 bp on all-in P&L. Funding is a cost here (-8.2%), not the credit Pass 1 expected from the short hedge; shown in the split, not counted in the gate.

**Not run**: P2 twin (low-vol), P3 profile, stress tests, validation: gate failed.
