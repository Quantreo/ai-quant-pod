# Crypto Funding Carry · Pass 1 (v5.3)

**Verdict: Go, on one condition: P1 must be recomputed residual on beta before any validation run (round 4, #1).** Gate #2 on run 20261025-151935-train-base: net 0.887 against a bar of 0.75 (6 tries), a pass. Raw P1 made t 1.77, but it is no longer the gate: residual P1 below t 1 on train is a kill. Two payers, both hypotheses: the weekend flow, paid in price on Monday and Tuesday, and leveraged longs, paid in funding. Known fragility: the train net falls under the luck line at 40 bp on the short side (0.659) and with both sides at 20 bp (0.738). v4: [[Pass 1 v4]].

**Stage: full.**

## 1.1 Mechanism

**Type**: constraint (weekend liquidity) plus risk premium (funding).

**Who pays.** Leveraged longs crowd into the high-funding perps over the weekend, while basis and market-making capital is thin. When that capital comes back on Monday, these names fall against the low-funding ones. Funding is the second payer: longs pay to hold their leverage [hypothesis, both].

**What the sources show.** Funding is set by the gap between mark and index [source: Ackerer 2024, Theorem 1, p. 7-12; theory]. Carry pays in nine asset classes, crypto not among them [source: Koijen 2013, Table II A]. No library note covers the weekend payer.

**Why it is not arbitraged away.** Supplying that liquidity means being short crowded names into squeezes (negative skew), and this capital is scarce at weekends.

**What it could secretly be.** 7-day reversal, BTC or alt beta, a few 2021 pumps. Not Crypto Weekend Clienteles: that one sorted on returns and was killed at gross 0.23.

**Predictions.**
- **P1** (kills, gate): over its first 48 h, the Sunday book's price P&L beats a Wednesday placebo over the placebo's own first 48 h, **residual on BTC and alt minus BTC** over the same windows (1.5b), t ≥ 1. The rival is a weekday beta effect: the short leg has the higher beta, and a market that falls on Monday and Tuesday would make the raw gap alone. Raw train figure: t 1.77; the residual is not yet computed.
- **P2** (kills, validation): the weekly **price** P&L of the full Sunday-to-Sunday book (funding reported apart) has an intercept t ≥ 1 on BTC, alt minus BTC, volatility and 7-day return (the factors of Pass 2). This checks that days 3 to 7 do not give back the 48 h gain.
- **P3** (read only): 2022 loses net. The loss sits in the Wednesday to Sunday price P&L and in the 10 worst weeks of the universe, while funding stays positive.
- **P4** (read only): the residual P1 gap sits in the short leg, with the same regression run per leg. Raw train figures: short +0.336% a week, long -0.033%.

## 1.2 Sources and crowding

Library: Koijen 2013, Ackerer 2024. Funding carry on perps is public [literature, not in library: Schmeling Schrimpf Todorov 2023; He Manela Ross von Wachter 2022]. There is no source on the weekend effect. Earlier attempt: v4 of this sheet.

## 1.3 Expected behaviour

It works when weekend leverage builds in bull markets (2021, 2024). It suffers in crashes (2022, LUNA, FTT) and in squeezes of the short leg. The payoff has negative skew (v4 weekly skew -0.59) and is carried by a few weeks: without the 5 largest weeks, raw P1 falls from t 1.77 to 1.52.

## 1.4 Universe

Top 30 Binance USDT perps by 30-day quote volume, point in time, listed at least 90 days, at least 20 names. Dead names are kept.

## 1.5 Base version

| Brick | Choice | Why | Basis |
| --- | --- | --- | --- |
| Signal, book, sizing, band, margin | v4 exactly ([[Build]] table, sha 8ada54c6f9b2) | The gated base | convention |
| Hold | Weekly, Sunday to Sunday | Funding pays all week; a 48 h hold doubles turnover | cost |
| Costs | Lab at cost_bp 0, `liquidation_cost_bp` 12.5. Per name and per trade with the `tier_cost` logic, swapped: short 20 bp, long 5 bp, delisting exit 12.5 bp | Thin Losers tier values. The data does not support a thin short tail: mean volume rank 17.1 for the top-funding quintile against 15.4 for the bottom one | cost [hypothesis] |

## 1.5b Free parameters

| Parameter | Value | Tested as |
| --- | --- | --- |
| Side with the thin tier | short | stress: both sides 20 bp (train net **0.738, under 0.75**) |
| Thin tier | 20 bp | stress: short 40 bp, long 5 bp (train net **0.659, under 0.75**) |
| Placebo day | Wednesday, the furthest from the weekend | follows from P1 |
| P1 horizon | 48 h, read off v4's Monday and Tuesday P&L, so seen: **counted as a try** | read-only stresses at 24 h and 72 h |
| P1 residual | Stacked regression of the 312 book-window price returns (Sunday and Wednesday) on a Sunday dummy, BTC and alt minus BTC (equal-weight point-in-time universe without BTC, minus BTCUSDT), slopes per book; P1 is the dummy; HC standard errors | convention: factors of Pass 2 |
| #3 exclusion | The 5 names with the largest total Monday-Tuesday price P&L on train plus validation, removed in every week (global, ex post) | strict |
| #3 fill | Sunday book filled at 04:00 UTC Monday on `mark_hourly`, price to Wednesday 04:00; TLMUSDT (no hourly mark) out | user's condition for unparking (Parked decision) |
| Missing Wednesday row | That pair is dropped, and the count is reported | convention |
| Stitched t | Newey-West, 5 lags on weekly net returns | convention: floor(4(T/100)^(2/9)) at T of about 300 weeks |

Other parameters as in v4 1.5b, with the v4 stress tests.

## 1.6 Horizon, trades and power

Weekly. 156 independent weeks on train, 208 on train plus validation. **Tries 6**: the base and V1 to V3 of 2026-10-23 (backfilled in Trials.csv), the v5 base, and the 48 h horizon (chosen on seen v4 data, round 4, #2). Crypto Weekend Clienteles is not counted: it is another family and asset row (seasonality-flows), it sorted on past weekend returns, and no choice here was taken from its result. Counting it would give 7 tries and a line of 0.80, and 0.887 would still pass. The placebo, the stresses and the read-only splits are not tries. The luck line is 0.75 (`budget.py`, 6 tries, 3 years).

Power (`budget.py`, one-sided), with the numbers of 1.11. #1 (residual P1): 84% at an effect of 0.16 sd, 50% at 0.08, 15.9% at zero (156 weeks; the effect is a hypothesis from v4, 2020-07 to 2023, on raw returns). #2: 67% at a true net Sharpe of 1.0, 9.7% at zero for one try. Only #5 is clean: #1 to #4 sit on seen data.

**Data already seen**: v4 was run on 2020-07 to 2024, gates, validation and stresses included. The v5 train is seen: net 0.887, gross 1.179, funding share 0.64, turnover 44.0 a year, P1 0.303% a week at t 1.77. Validation 2024 is seen through v4 (gross 2.08). The only clean sample is the sealed test, then paper trading.

## 1.7 Cost and capacity budget

Measured turnover is 44.0 a year, 22 per leg (`budget.py`): 4.40% a year at 20 bp plus 1.10% at 5 bp, 5.50% in all. Costs stay under half the edge at a gross Sharpe of 0.55 or more; train gross is 1.179. Fragility: train net is under the luck line at 40 bp on the short side (0.659) and with both sides at 20 bp (0.738). The repository has no bid and ask data, so the spread cannot be measured before the test. Capital needs a short-leg cost of 20 bp or less, measured on fills in paper trading at half weight, which comes before any money. Capacity: top-30 perps at about 1.1x gross. The short tail's depth limits it [hypothesis, not computed].

## 1.8 Instrument traps

| Trap | Handling |
| --- | --- |
| Funding | P&L split into price, funding and costs; funding at print level, prints after t paid by the new book |
| Liquidation, isolated margin | Mark high and low; maintenance 0.5% plus 12.5 bp. In the P1 books the liquidation loss counts, with no fee |
| Delisting | Liquidation first, else the last mark close plus 12.5 bp; never `last_day` |
| Survivorship | Point-in-time universe; today's top 30 as a read-only control |
| Funding gaps | A name with no print leaves both books that week |

## 1.9 Variants

**None.** 2024 is already seen through v4, so a variant would be a try with no clean sample to read it on, and would raise the luck line to 0.80 (7 tries). The open questions go to read-only diagnostics.

## 1.10 Test plan

Train 2021-01-01 to 2023-12-31. Validation 2024. Test from 2025-01-01, sealed, about 1.7 years.

| Diagnostic | Checks |
| --- | --- |
| Residual P1 by year and by leg, without the 5 largest weeks, without FTT and LUNA, at 24 h and 72 h | P1, P4 |
| P&L by day of the week; 2022 split Monday-Tuesday vs Wednesday-Sunday price; 10 worst universe weeks | P3 |
| Four-factor regression, weekly price P&L, train plus validation; funding apart | P2 |
| One-day delay, survivorship control, stresses | read only |

## 1.11 Kill criterion

| # | Criterion | Sample | Bar | Power (`budget.py`) |
| --- | --- | --- | --- | --- |
| 1 | P1 Sunday minus Wednesday, residual on BTC and alt minus BTC | train, 156 pairs | t ≥ 1 | 0.16 sd: 84%; 0.08: 50%; zero: 15.9%. To compute; raw t 1.77 |
| 2 | Net Sharpe, tiered | train | ≥ 0.75 | passed, 0.887 |
| 3 | Monday-Tuesday price P&L of the Sunday book filled at 04:00 UTC, without its 5 best names (1.5b), residual on BTC and alt minus BTC | train plus validation, 208 weeks | t ≥ 1 | 0.10 sd: 67%; 0.16: 90%; zero: 15.9% |
| 4 | P2 intercept, weekly price P&L | train plus validation, 208 weeks | t ≥ 1 | true price Sharpe 0.8: 73%; 0.5: 50%; zero: 15.9% |
| 5 | Test, three zones on net mean | test against train plus validation | confirms > half the earlier mean; ambiguous within ± half; contradicts < minus half with t < -1.5, kill | true 0.887 over 1.7 years: t > 1 56% |

#3 and #4 use 2024, already seen through v4. The effects of 0.10 and 0.16 sd for #3 are hypotheses. Money also needs a stitched net t (Newey-West) of at least 2 on train, validation and test; otherwise the strategy stays on paper.

## Pre-registered for the Developer

| # | Choice |
| --- | --- |
| 9 | Tiers swapped, in both stresses too |
| 10 | Delisting exit and liquidation fee 12.5 bp; every other trade pays its side tier |
| 11 | Placebo on the Wednesday row, trade at Wednesday close; signal prints in (t - 7d, t], t = Thursday 00:00; price from Wednesday close to Friday close |
| 12 | Both P1 books formed from zero, no band, 48 h, zero cost and funding; liquidation loss counted, no fee |
| 12b | Pairing: Sunday d with Wednesday d+3 of the same week. The last Sunday (2023-12-31) is out because its 48 h leave the train: 156 pairs |
| 13 | Funding gaps out of both books |
| 14 | Dying legs: liquidation first, else the last mark close, same rule in both books |
| 15 | P1 and #3 also reported without the 5 largest weeks, read only; P1 also raw, read only |
| 16 | Daily marks for P1 (hourly for #3 only); last-price fallback only on market-wide hole days |
