# Crypto Low-MAX Long Leg · Pass 1

**Verdict: Go.** The source edge sits in the short leg; the long leg's edge is a [hypothesis] (untested, Grobys 2021, p. 11; section 8). "Long-only" is built as that leg: long low-MAX perps, short the equal-weight basket at its beta. A bare long basket would test crypto beta. Gate on the price component only: funding cannot pass it.

**Stage: short** (before the train gate).

---

## 1.1 Mechanism

**Type**: behavioural bias. · **Who pays**: [hypothesis] traders who chase coins after extreme up days overprice them, so the quiet coins are relatively cheap; borrowed from equity, not tested in crypto (Grobys 2021, p. 3, 11). · **What the source shows**: quintile means low to high MAX 1.33, 1.38, 0.55, 1.08, -0.22% a week, not monotonic; Q1 is +0.51 over the mean of 0.82, no t for the legs; H-L t = -1.57 with plain errors, 20 coins, 2016-2019, gross [source: Grobys 2021, Tables 1, A8]. · **Why not arbitraged**: [hypothesis] the arbitrage is short the lottery coins, and their jumps make it a margin and squeeze risk (H-L worst week +59.87% against the short [source: Grobys 2021, Table 1]); the long leg alone is a small, dull relative edge. · **Could secretly be**: low volatility (past vol rises with MAX [source: Grobys 2021, Table 1]), low beta, a large-coin tilt, funding collected by the short hedge (P&L split; gate on price only). · **Opposite sign**: [source: Ozdamar 2021, Table 2] uses 28-day MAX on up to 523 coins incl. small ones and reads continuation. [hypothesis] a 28-day window and small coins catch momentum; 7 days on 30 liquid perps is closer to Grobys. If P1 has the wrong sign on train, the stated reading is Ozdamar's continuation, and no window is retried.

**Predictions**:
- **P1** Beta-hedged low-MAX leg earns a positive price-only net Sharpe on train (funding shown in the split, not counted). Failure: kill (level gate, 1.11).
- **P2** Low-MAX beats the low-vol twin (bottom quintile of 7-day realized vol, same hedge and sizing). If the twin wins by difference t of 1 or more, it becomes the candidate (one more try, counted). Low-MAX not ahead: label "low-vol, MAX not shown". Power: 32% at a difference Sharpe of 0.3 (budget.py).
- **P3** Hedged quintile profile on train: Q1 above the mean of Q2 to Q4. Read only: power 28% at the source's gap of 0.033 sd a week (budget.py), the test can barely tell.

## 1.4 Universe

Binance USDT perps, type COIN, BTC excluded (as the source). Top 30 by median quote volume of the prior 30 days, listed 60 days or more, point in time, dead names kept.

## 1.5 Base version, brick by brick

| Brick | Choice | Why | Basis |
| --- | --- | --- | --- |
| Signal | Highest daily return of the last 7 days | Source rule | source (Grobys 2021, p. 6) |
| Entry | Weekly, bottom quintile (6 coins), equal weight | Source sort | source |
| Hedge | Short equal-weight universe (leg included) x 90-day beta of the leg | Removes market and low-beta; excluding the leg only rescales the spread (leg minus beta x basket = (1 - 0.2 beta) leg minus 0.8 beta x rest; the vol target absorbs the scale) and adds hedge turnover | mechanism, cost |
| Book | 20% vol target, gross capped at 2x capital | House default; cap stops leverage in calm spells | convention |
| Execution | Next daily close after formation (skips one day) | No same-bar fill; skip kept the effect [source: Grobys 2021, Table 3] | convention |
| P&L | Price, funding, costs, split | Perps charge funding | convention |

## 1.5b Free parameters

| Parameter | Value | Why | Tested as |
| --- | --- | --- | --- |
| Universe size | 30 | Liquid at 5 bp | stress test (20, 50) |
| Beta window | 90 days | Stable in crypto | stress test (60, 180) |
| Listing age | 60 days | Skip listing pumps | stress test (30, 120) |
| Beta clip | 0.5 to 1.5 | Stops a noisy 90-day beta from flipping the hedge | follows from beta window |
| Gross cap | 2x capital | Bounds leverage at the vol target | free; stress test (1.5x) |
| Min names in leg | 5, else flat | Below that the leg is a coin bet | free |

Spec gaps, settled (round 1):
- Sort ties: broken by symbol order (free; rare with float returns).
- Daily close: 00:00 UTC, Binance daily candle (convention).
- Beta: OLS of daily returns of the 6 current leg coins, equal weight, on the equal-weight universe, their own past 90 days; clipped as above (mechanism).
- Funding: booked at each 8h settlement on the positions held then (instrument).
- Delisted coin mid-week: closed at last price, cash until next rebalance, no replacement (convention).
- Rebalance: formation on the Monday 00:00 UTC close, fill on the Tuesday 00:00 UTC close (free day; skip from source).
- Vol target: realized vol of the current weights on the past 60 daily returns, reset weekly (convention).
- Signal history: a coin needs all 7 daily returns, else out that week (source rule).
- P2 twin: 7-day realized vol of daily returns (same window as MAX, only the statistic changes), same hedge, sizing, cap (mechanism).

## 1.7 Cost budget

Gross book: leg minus basket vol about 60% a year [estimate: H-L weekly SD 14.21% x sqrt(52) = 102% for 4 vs 4 coins, one leg about /sqrt(2), 6 coins x sqrt(4/6); to measure, 2016-19 coins were wilder]. Leg = 0.20 / 0.60 = 0.33 of capital, hedge about 0.27 (beta 0.8 [estimate]), gross 0.6, far under the cap. Rotation: 27% of low-MAX coins stay low [source: Grobys 2021, Table 5; 20 coins, may differ at 30], so 73% of the leg sold and bought: 2 x 0.73 x 0.33 = 0.48; hedge resizing about 0.02 [estimate]; 0.5 of capital a week. 26x a year at 5 bp = 1.30% a year (budget.py). Gross Sharpe needed: 0.13 at 20% vol. Stress at 2x cost. Capacity: the sixth coin's volume.

## 1.10 Periods

Train 2021-01 to 2023-12, validation 2024-01 to 2024-12, test 2025-01 to 2026-09 (sealed). Under 80 names before 2021. **Data already seen**: the desk ran several crypto sheets on these perps; true out-of-sample starts with paper trading.

## 1.11 Train gate

Level only: price-only net Sharpe (price minus measured cost, funding excluded) above luck line, t of 1 (3-year train). Tries: 0 (no Trials summary row for low-vol crypto) + 2 (base, P2 twin) = 2. Luck line 0.30; false pass 15.9%; pass at true Sharpe 0.5: 45% (budget.py). P2 is a twin, not a kill; P3 read only.

## 1.2, 1.3, 1.6, 1.8, 1.9, rest of 1.10 and 1.11 · *after the gate*
