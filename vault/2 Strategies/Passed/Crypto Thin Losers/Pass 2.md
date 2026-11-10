## Pass 2

**Verdict: candidate for the test, with a warning** · 2026-10-23 · runs read: 20261023-164156-train-base-tiered, 164200 and 164203 (train diagnostics), 164211 (validation base), 164216 (V1), 164220 (V2), 164225 (delay 1), stress runs 164230 to 164257 · lab fd8ce652344b (all runs share it) · code c7814558d546 · report [[Crypto Thin Losers - Backtest report]]

The four kill criteria of 1.11 pass on train, so by the rules the strategy goes forward. The worst news is outside 1.11: on 2024 the edge shrinks to a third of the train figure. Gross Sharpe 0.87 (train 1.75), net 0.33 (train 1.38), break-even cost 20 bp, exactly the 20 bp assumed for the thin leg. At 40 bp on the thin leg the net Sharpe is -0.07. The 2024 market-adjusted intercept is +0.00048 a day, NW t 0.85. The bootstrap of the net Sharpe on 2024 runs from -1.66 to 1.39. Nothing in 1.11 kills on validation, so I do not kill; I do not claim the edge survived either.

### Kill criteria (1.11)

| # | Criterion | Threshold | Measured | Pass |
| --- | --- | --- | --- | --- |
| 1 | Intercept NW t (14 lags), train, base, market today + 5 lags and depth spread | t >= 2 | my replication (analysis/regress_daily.py): +0.00112/day, t 3.01 with the depth control (3.03 on market alone); Developer's gate: 3.04 | pass |
| 2 | Net Sharpe, train, measured turnover 79.6/yr, tiered cost, funding, liquidations | >= 0.49 | 1.377 | pass |
| 3 | Losers minus winners intercept NW t, train | t >= 2 | +0.00107/day, t 2.58 (Developer 2.50); winners alone t 0.10 | pass |
| 4 | Price share of gross P&L, train | >= 0.5 | 1.03 (funding share -0.027) | pass |

All four pass, with margins that are modest on #1 and #3 (power at Sharpe 1.0 is only 39%, so a pass is weak evidence). #3 was set knowing t 2.50 (written in 1.11): no new evidence. The Developer's and my t differ by 0.01 to 0.08 only from the start day of the series.

### Predictions (1.1)

| P | Prediction | Separates from the rival? | Measured | Confirmed |
| --- | --- | --- | --- | --- |
| P1 | Positive intercept beyond market and depth of fall | yes: stale-beta bounce (a) and depth of fall (d) | t 3.01 on train; the depth spread alone earns nothing (gross Sharpe -0.05). Validation: intercept t 0.85, same sign, not significant | confirmed on train; not confirmed on 2024 |
| P2 | Premium sits among losers, not winners | yes: beta and size would lift both rows | winners intercept +0.00004/day (t 0.10), losers minus winners t 2.58; winners spread gross Sharpe 0.22 | confirmed |
| P3 | Pays its costs | no | train net 1.38 vs 0.49; validation net 0.33 (cost -11.8% a year against price +20.4%) | confirmed on train; validation below the line |
| P4 | Price at least half of gross | yes: carry rival (c) | 1.03 train, 1.04 validation; long-leg funding -16.5%, short-leg funding +12.9% on train: carry is nil | confirmed |
| P5 | Front-loaded (days 1 to 7 above 8 to 14); V1 same sign | read only | event-time split not computed (no script; the saved runs do not carry it). V1 on validation: same sign, gross 0.81 vs 0.87, net 0.26 vs 0.33. V2 (7 days): gross 1.09, net 0.37, turnover 129/yr | V1 confirmed; front-loading not measurable. The hint is favourable (V2 gross above base) |

Rival (d), depth of fall, is the one a failing prediction could have left open: V1 keeps the sign, and the depth spread earns nothing, so it is not carrying the base. V1 is smaller, as written.

### Luck

Tries 3 (base, V1, V2), N_eff 1.05 (validation return correlation 0.89 to 0.95), years 3. Luck line 0.49 with 3 independent tries (Pass 1 figure), about 0.0 with N_eff 1.05. Gross Sharpe 1.75, above the 0.49 line by 1.26; net 1.38, above by 0.89. Desk-wide (trials report, 7 counted tries, N_eff 2.3, 3.5 years): luck line 0.35, best gross 1.75, above by +1.40. Luck does not explain train. It does not explain 2024 either: 2024 is simply a weak year for a strategy whose train years were 1.4 to 2.0 gross.

### Controls

| Control | Base | Control | Reading |
| --- | --- | --- | --- |
| One-day delay (validation) | gross 0.87, net 0.33 | gross 0.84, net 0.32 | No collapse: not a fast effect and no leak visible here. The d+1 fill stress is the same run. Train delay was not run |
| Survivorship (today's universe) | | not run | Pass 1 builds the universe point in time with dead names kept; no survivorship run exists. Not measurable; the Red team should check the delisting exits (13 on train) |

### Stress tests (validation, logged, not tries)

| Stress | Net Sharpe | Reading |
| --- | --- | --- |
| base | 0.33 | |
| independent sort | -0.06 (gross 0.44) | Sort order carries half the gross: the sequential cells are a real choice |
| beta window 30 | -0.02 (gross 0.58) | Hedge window matters |
| beta window 120 | 0.64 (gross 1.17) | Better; the 60-day choice was not the best |
| beta lags 10 | 0.38 | Same |
| hedge on equal-weight top 20 | -0.11 (gross 0.43) | Hedge with a BTC beta vs a basket loses half the gross: the P&L depends on the hedge |
| thin leg 40 bp | -0.07 | Dies at twice the assumed thin cost |
| minimum 5 a leg | 0.33 | No effect in 2024 |

The result is fragile on the sort order, the hedge and the thin-leg cost, three of the choices Pass 1 marked as free.

### P&L by period and by leg

| Run | Price % | Funding % | Costs % | Liq % | Net Sharpe |
| --- | --- | --- | --- | --- | --- |
| 2021 | 42.9 | 1.1 | -6.4 | -0.02 | 1.21 |
| 2022 | 49.9 | -3.3 | -9.4 | -0.06 | 1.58 |
| 2023 | 47.0 | -1.5 | -13.0 | -0.34 | 1.45 |
| 2024 (validation) | 20.4 | -0.7 | -11.8 | -0.34 | 0.33 |

By leg on train (% of capital): long thin price +228.5, short liquid price -88.7, funding long -16.5, short +12.9. The long leg makes the money and the liquid short is a net cost of about 89 points, so the spread depends on the hedge and the short removing the market. Concentration: top 5 names 41% of train P&L (DOGE 21.1%, mostly one day, 2021-01-28, +24.9% of long-leg P&L terms per the Build); top 5 75% on 2024. Train costs rise with turnover (79.6 to 98.1/yr in 2024). Weekly skew +1.94 on train, -0.31 on 2024: the positive skew of train came from a few large recoveries.

### For the next seat

- Red team: attack first (1) the DOGE episode of 2021-01-28 and the top-5 concentration on train (what are train gate #1 and #3 without them?); (2) the sensitivity to the hedge and the sort order, both of which halve the gross on 2024; (3) the thin-leg cost of 20 bp against what a 6 to 30M USDT a day name really costs, since break-even on 2024 is 20 bp; (4) delisting exits and survivorship; (5) whether the 2024 drop is a regime or the end of the pattern.
- Economist: no rewrite required. A note for the test zones: the earlier mean (train plus validation) is dominated by train, so half of it is a bar the 2024 level (about a third of train gross) would fail. Pass 1 fixed this rule, so I apply it as written.
