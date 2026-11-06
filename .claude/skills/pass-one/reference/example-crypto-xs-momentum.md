---
type: strategy
name: Crypto XS Momentum
family: trend
asset: crypto
horizon: weekly
status: pass 1
idea: "[[Idea Journal]] · 2026-08 · Cross-sectional momentum, crypto top 20"
---

# Crypto XS Momentum · Pass 1

> **Example Pass 1 for the Economist.** Written as it should have been written before any test: only facts known before the backtest are used. Source: the hand-written sheet in `vault/_archive/stl-strategies/`.

**Verdict: Go, with one condition.** The mechanism is documented in other markets and plausible in crypto, not shown there yet. The condition: momentum must survive once the funding it collects is taken out (prediction P4). If it does not, this is a carry strategy and belongs with carry.

---

## 1.1 Mechanism

**Type**: behavioural bias (under-reaction), with a flow component.

**Who pays.** Investors who react slowly to news, and who sell recent winners too early and hold recent losers too long, so that prices adjust over weeks instead of days. Whoever holds the winners and shorts the losers is paid by that slow adjustment. [literature: disposition effect and slow diffusion, Shefrin Statman 1985, Frazzini 2006, Hong Stein 1999, as cited by Moskowitz 2012, p. 229]

**Why crypto.** Participation is mostly retail, and hundreds of names have no analyst coverage: news reaches prices slowly, and flows chase what has already moved. [hypothesis]

**Why it is not arbitraged away.**
- Shorting losers costs funding and borrow, and the smallest names are thin. [hypothesis]
- Momentum loses sharply at trend reversals, which keeps capital away. [source: Moskowitz 2012, p. 238, March to May 2009]
- Documented in crypto since 2019 [literature, not in library: Liu Tsyvinski Wu 2022, old note, figures not checked]: the effect may already be crowded.

**What it could secretly be.**
- **Funding carry**: a demeaned book tends to be short the names with the highest funding, and collects it.
- **Market beta**, if the book is not neutral: crypto names move together.
- **Size or liquidity**: if the profit sits in the smallest names, it is a liquidity premium that costs cannot reach.

**Predictions, to be checked by the Diagnostic.**
- **P1** Stronger when cross-sectional dispersion is high (sector rotations), weak when it is low.
- **P2** Loses when everything moves with BTC, and at sharp reversals of leadership.
- **P3** Behavioural, so stronger in less covered names; but not only in the smallest ones (see "secretly").
- **P4** Positive once funding is removed from the P&L.
- **P5** Weaker when the trade is crowded. [source, weak: Lou 2019, Table 7B, US stocks, differences not significant at 5%]

## 1.2 Sources and crowding

- **Sources**: [[2012 - Moskowitz Ooi Pedersen - Time Series Momentum]], derived on two bricks: universe (futures to crypto perps) and signal (time-series to cross-sectional). An earlier attempt on 29 CME futures failed (Sharpe -0.61, turnover 152× a year).
- **Crowding**: momentum is the most published factor in finance. In crypto it is documented and easy to build, so the edge may be smaller than older papers suggest.

## 1.3 Expected behaviour

- **Works when**: dispersion is high, leadership rotates across sectors, trends last weeks.
- **Suffers when**: BTC drives everything, liquidation cascades, V-shaped reversals.
- **Payoff**: many small losses, a few large gains; a handful of names and days make the year.

## 1.4 Universe

- Top 20 Binance USDT perpetuals by trailing 30-day volume, **point-in-time**, names listed for at least 180 days, leaving only below rank 25 so that membership does not flicker.
- **Why a cut-off**: beyond some rank, names are small and noisy, and a flat 5 bp cost understates what they really cost. This justifies a cut-off, not the number 20: the size of the universe is a free parameter, tested for robustness (see 1.5b).
- **Survivorship is measured**, not declared: the same code on today's top 20 applied to the past is the control.

## 1.5 Base version, brick by brick

Every choice has a basis, written before the test: **mechanism**, **cost**, **source**, **convention** (standard choice, reference given), **scale** (does not change the Sharpe) or **free** (nothing decides it: tested, see 1.5b).

| Brick | Choice | Why | Basis | Card |
| --- | --- | --- | --- | --- |
| Signal | Rank names on past returns, cross-sectionally | The mechanism is relative: winners keep beating losers | mechanism | [[Time-series momentum signal]], cross-sectional version (no card yet) |
| Signal | Returns divided by their volatility before ranking | Otherwise the ranking is a ranking of volatility | mechanism | [[Volatility targeting]] |
| Signal | Three speeds (7, 30, 90 days), averaged | The speed of diffusion is unknown; averaging avoids picking one speed on the data | free | none |
| Signal | EMA smoothing of each speed | Cuts turnover on the fast speed | cost | none |
| Portfolio | Demeaned long-short, sum of positions zero | Crypto names move together: a long-only book is a BTC bet | mechanism | none |
| Sizing | Inverse volatility per name | Volatilities differ by a factor of five across names; equal risk per name | source | [[Volatility targeting]] |
| Sizing | Strategy volatility target 20% | Sets the size of the book | scale | [[Volatility targeting]] |
| Sizing | Diversification multipliers for speeds and names, past data only | Averaging lowers risk; the multiplier brings it back to target | convention (Carver 2023, not yet in library) | none |
| Rebalancing | Daily, trade only outside a band | Keeps turnover under the cost budget | cost | [[No-trade band]] |

## 1.5b Free parameters

Each one is fixed before the test, then either tested as a variant (a try, counted) or as a stress test (not a try, but the result must hold).

| Parameter | Value | Why this value | Tested as |
| --- | --- | --- | --- |
| Universe size | top 20 | Small enough to trade at 5 bp | stress test: top 10, 20, 30 |
| Entry age | listed 180 days or more | Enough history for the slowest speed (90 days) and the volatility estimate | none: follows from the slowest speed |
| Exit rank | leave below rank 25 | Stops names flickering in and out | none: a band, same logic as the no-trade band |
| Volume window | trailing 30 days | Matches a monthly view of liquidity | none: convention |
| Speeds | 7, 30, 90 days | A week, a month, a quarter: spans the plausible diffusion speeds | stress test: drop one speed at a time |
| EMA span | a quarter of each speed | Convention (Carver 2023, not yet in library) | none |
| Band width | 10% of the target position | Cost budget | V3 (no band) |

## 1.6 Horizon, trades and statistical power

- **Holding period**: days to weeks.
- **Turnover target**: under 50× a year.
- **Observations**: daily data since mid-2021, about five years: enough for the signal, one crypto cycle for regimes.
- **Data already seen**: first use of crypto perps by the desk; the earlier momentum attempt used CME futures. The split is clean for the desk, but crypto momentum is published since 2019: others have looked at this data.
- **Luck line**: with about 5 years of data, the best of 4 independent tries reaches a Sharpe of about 0.46 with no skill (computed from [[Deflated Sharpe]]). A result below that line means nothing.

## 1.7 Cost and capacity budget

- At 50× a year and 5 bp one way, costs are about 2.5% of capital a year.
- At a 20% volatility target, the strategy needs a **gross Sharpe of at least 0.25** for costs to take less than half the edge. Below that, slow the signal or widen the band before testing further.
- Funding can be larger than the price edge (0.03% per 8 hours is 33% a year, [[Instrument Traps]]): the P&L is split into price, funding and costs from the first run.
- Capacity: 20 names, daily trading; realistic for a small account, untested above.

## 1.8 Instrument traps

- **Funding**: separate price P&L from funding P&L.
- **Costs**: the tail of the universe costs more than 5 bp.
- **Survivorship and look-ahead**: membership uses volume known at the date; no multiplier is back-filled for names listed mid-sample.
- **Tickers**: some tokens were relisted under an old ticker.

## 1.9 Variants (written before the test)

Each variant changes one brick and counts as a try for the [[Deflated Sharpe]].

| # | Brick | Change | Why | Expected effect |
| --- | --- | --- | --- | --- |
| V1 | Signal | Rank on price returns only, funding excluded | Tests P4: is it momentum or carry? | Lower Sharpe, much lower correlation with any carry book |
| V2 | Condition | Stand aside when last month's dispersion is in the bottom third, threshold on past data only | Tests P1 directly | Higher Sharpe, lower turnover, fewer months traded |
| V3 | Rebalancing | No band | Measures what the band buys | Turnover up by a third or more, Sharpe flat or lower |

Stress tests, not tries: costs at 1, 5, 10 and 20 bp; universe of 10, 20 and 30 names; each speed dropped in turn; today's top 20 as the survivorship control.

## 1.10 Test plan

- **Sample**: 2020-07 to 2026-08. **In-sample / out-of-sample split**: 2023-01-01, fixed now.
- **Diagnostics required**: P&L split (price, funding, costs), turnover and breakeven cost, returns by dispersion tercile (P1), BTC-driven months (P2), contribution by name (P3, concentration).

## 1.11 Kill criterion (backtest)

- Net Sharpe below 0.3 on the point-in-time universe, or below the luck line.
- A 95% bootstrap interval containing zero **and** a P&L made by fewer than 5 names.
- Turnover above 60× a year at 5 bp.
- V1 Sharpe at or below zero: the strategy is carry, not momentum. Move it to the carry family.
- Out of sample: the three-zone rule.
