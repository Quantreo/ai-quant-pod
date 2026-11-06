# Bond Trend Demeaned · Pass 1

**Verdict: Go.** Bond trend profit is mostly drift [source: Moskowitz 2012, Table 5B]; trend net of an ex-ante mean asks whether persistence is left. Payer named as a hypothesis, P1 can show it wrong. Gate power is low (16%): a fail means "not shown", and no retest on this data.

**Stage: short** (before the train gate).

---

## 1.1 Mechanism

**Type**: behavioural bias (under-reaction), hedging pressure as rival [source: Moskowitz 2012, p. 245-248]. · **Who pays**: bond holders who under-react to persistent policy cycles [hypothesis]. · **Why not arbitraged**: cycles last years, trend loses at reversals [hypothesis]. · **Could secretly be**: the drift, or one rate cycle seen once.

**Predictions**:
- **P1** Demeaned trend earns a positive net Sharpe on train. Failure: kill (level gate).
- **P2** Beta to the always-long basket near zero. Read only.
- **P3** Auto-covariance share of profit positive (decomposition card); at t -1 or below: label after the gate.

## 1.4 Universe

IEI, IEF, TLH, TLT, TIP, BWX: government rates only (credit is another risk). SHY dropped (1 to 2% vol needs extreme leverage). An ETF enters 36 months after its first price, point in time. About two independent bets.

## 1.5 Base version, brick by brick

| Brick | Choice | Why | Basis |
| --- | --- | --- | --- |
| Return | Monthly total return minus T-bill | Trend predicts excess return | source |
| Signal | Sign of 12-month excess return minus 12 x expanding mean | Removes drift, known at t | mechanism |
| Lookback | 12 months, 1-month hold | Best cell | source (Moskowitz 2012, Table 2) |
| Sizing | Inverse vol, EWMA centre of mass 60 days, lagged | Unlike durations | source (p. 233) |
| Book | 10% vol target, gross cap 2x | House default; caps leverage cost | convention, cost |
| Costs | Tier cost, borrow 25 bp, leverage T-bill + 50 bp | Cost Assumptions | convention |

## 1.5b Free parameters

| Parameter | Value | Why | Tested as |
| --- | --- | --- | --- |
| Mean warm-up | 36 months | Stable mean, keeps 2008 in train | stress test (24, 60) |
| Gross cap | 2x | Leverage cost small | stress test (1.5x, 3x) |

## 1.7 Cost budget

About 20% of capital rotated monthly (sign flips plus resizing): 2.4x a year at 4 bp = 0.10% a year (budget.py). Gross Sharpe needed: 0.02 at 10% vol. Still small at 3x the estimate. Capacity not binding.

## 1.10 Periods

Train 2008-01 to 2018-12, validation 2019-01 to 2021-12, test 2022-01 to 2026-09 (sealed). **Data already seen**: the desk ran ETF TSMOM 12-Month on these bond ETFs, and 2022 is known. True out-of-sample starts with paper trading.

## 1.11 Train gate

Level only: net Sharpe above luck line plus measured cost, t of 2 (11-year train). Tries: 0 (no Trials summary) + 1 = 1. Luck line 0.00; false pass 2.3%; pass at true Sharpe 0.3: 16% (budget.py). No control at the gate (alpha over always-long is low power: a label). Raw trend is the simpler twin: if it beats the base by difference t of 1 or more, it becomes the candidate, one try.

## 1.2, 1.3, 1.6, 1.8, 1.9, rest of 1.10 and 1.11 · *after the gate*
