---
type: strategy
name: FOMC Drift
family: event-driven
asset: fx
horizon: daily
status: pass 1
idea: "[[Idea Journal]] · 2024-06 · Pre-FOMC USD weakness"
---

# FOMC Drift · Pass 1

> **Example Pass 1 for the Economist.** Written as it should have been written in June 2024, before any test: later results are not used. Source: the hand-written sheet in `vault/_archive/stl-strategies/`. The FOMC papers are not yet in the new library: they are cited from the old notes, figures not checked.

**Verdict: Go, with two conditions, tested first.** The equity version is well documented; the FX version and the positioning story are ours. Before any tuning: the drift must beat the same 24 hours on ordinary days (P1), and it must happen before the announcement, not in reaction to it (P3). If either fails, kill.

---

## 1.1 Mechanism

**Type**: scheduled flow, paid as a liquidity premium.

**Who pays.** Before a scheduled FOMC decision, holders of large dollar exposure cut it so as not to carry the decision risk. They do it ahead, because their positions are too large to unwind at once and spreads widen as the announcement nears. Liquidity providers with risk limits take the other side and are paid for carrying it until the announcement. The de-risking pushes the dollar down over the run-up. We take the liquidity provider's side, short the dollar, and leave before the decision. [hypothesis: our construction]

**What the literature shows.**
- US equities earn a large share of their yearly premium in the 24 hours before scheduled FOMC announcements, with no accepted explanation. [literature, not in library: Lucca Moench 2015]
- Returns are higher on scheduled macro announcement days in general, not only the Fed's. [literature, not in library: Savor Wilson 2013]
- A premium can be earned when scheduled uncertainty is resolved. [literature, not in library: Ai Bansal 2018]
- Short USD earns more on FOMC days, and more when monetary uncertainty is high. [literature, not in library: Mueller Tahbaz-Salehi Vedolin 2017]
- None of these papers trades the dollar in the 24 hours before the meeting.

**Why it is not arbitraged away.**
- Eight events a year: a desk needs a decade of data to see the effect, and most do not wait. [hypothesis]
- The risk is concentrated on known days, when risk limits are tightest for everyone. [hypothesis]
- The equity version has been public since 2011: if it is traded away, the FX version may follow.

**What it could secretly be.**
- **A dollar trend**: if the dollar fell over the sample, a short-dollar basket wins on any day. The placebo test (P1) separates the two.
- **A risk-on day effect**: FOMC eves may coincide with equity rallies, and the dollar falls in risk-on. The control is P4.
- **A look-ahead artefact**: an exit glued to the announcement captures part of the reaction. P3 checks it.

**Predictions, to be checked by the Diagnostic.**
- **P1** The 24 hours before scheduled FOMC meetings beat the same 24-hour window on ordinary days, same basket. If FOMC windows do not sit above most placebo windows, there is no FOMC effect.
- **P2** Stronger when monetary uncertainty is high: more holders need to de-risk.
- **P3** The drift happens before the announcement: an exit 5 minutes before keeps most of it.
- **P4** It survives on FOMC eves when equities fall.
- **P5** Spread across meetings, not carried by a few. If a handful of meetings make the result, it is noise.

## 1.2 Sources and crowding

- **Sources**: the five FOMC papers listed in the old notes, to be read again with `reading-source` before Pass 2. The positioning story and the FX construction are ours.
- **Crowding**: the equity drift is widely known; the FX version is undocumented. Crowding in equities could spill over.

## 1.3 Expected behaviour

- **Works when**: the meeting is scheduled and watched, and its outcome is uncertain.
- **Suffers when**: the decision is fully priced; the dollar is bid for other reasons (risk-off, safe-haven flows).
- **Payoff**: small frequent gains, occasional larger losses on risk-off days. Few trades, close to binary.

## 1.4 Universe

- Short-USD basket, six legs: long EUR/USD, GBP/USD, AUD/USD, NZD/USD; short USD/CAD, USD/CHF.
- **Why a basket**: the mechanism is about the dollar. A basket isolates the dollar leg and averages out pair-specific news.
- **Why these six**: the most liquid dollar pairs, so the real bid/ask stays small. USD/JPY is left out, and nothing in the mechanism says why: a free choice, tested (V3).
- No survivorship issue: a fixed list of majors.

## 1.5 Base version, brick by brick

Every choice has a basis: **mechanism**, **cost**, **source**, **convention**, **scale** or **free** (tested, see 1.5b).

| Brick | Choice | Why | Basis |
| --- | --- | --- | --- |
| Signal | None: pure calendar, every scheduled FOMC | The flow comes from the schedule itself | mechanism |
| Entry | 24 hours before the announcement | The equity drift sits in the 24 hours before | source (Lucca Moench 2015, not checked) |
| Exit | 5 minutes before the announcement | We are paid to carry the run-up, not the decision | mechanism |
| Portfolio | Short-USD basket, six legs | Isolates the dollar | mechanism |
| Sizing | Equal weight across legs | Simplest; legs differ in volatility | free (V1) |
| Sizing | Volatility target 10% | Sets the size of the book | scale |
| Costs | Real bid/ask at entry and exit, minute data | Spreads widen near the announcement | cost |

## 1.5b Free parameters

| Parameter | Value | Why this value | Tested as |
| --- | --- | --- | --- |
| Window length | 24 hours | The equity drift window | stress test: 12 and 48 hours |
| Exit offset | 5 minutes before | Out before the decision, with a margin for the clock | stress test: 0 and 15 minutes (also P3) |
| Leg weights | equal | Simplest | V1: inverse volatility |
| Pairs | six majors, no JPY | Liquidity | V3: add USD/JPY |
| Minimum legs with data | 5 of 6 | A trade needs most of the basket | none: data rule |

## 1.6 Horizon, trades and statistical power

- **Holding period**: 24 hours, 8 trades a year.
- **Observations**: about 100 meetings from 2012. With 100 trades, a t-stat of 2 needs a mean per trade of at least a fifth of its standard deviation (2 / √100, computed). Only a large effect can be detected; a small one will look like noise for years.
- **Data already seen**: first use of this FX minute data by the desk. The equity version of the effect has been public since 2011, so the idea itself was chosen knowing it worked somewhere.
- **Luck line**: with about 12 years of data, the best of 4 independent tries reaches a Sharpe of about 0.30 with no skill (computed from [[Deflated Sharpe]]).

## 1.7 Cost and capacity budget

- One round trip per meeting, 8 a year: costs are small in a year, large per trade. The mean per trade must be at least twice the round-trip spread on the basket, measured at the actual entry and exit times.
- Spreads widen as the announcement nears; a flat cost per trade understates AUD and NZD.
- Capacity: large for majors at these times, untested for size.

## 1.8 Instrument traps

- **Bid/ask**: buy the ask, sell the bid, at the minute of the trade.
- **Clock**: the calendar is rebuilt from scheduled meetings at 14:00 New York time, with daylight saving.
- **Look-ahead**: no future bar is ever used; a gap in minute data takes the last bar at or before the time.
- **Rollover**: a position held through 17:00 New York pays or earns the swap points.

## 1.9 Variants (written before the test)

Each variant changes one brick and counts as a try for the [[Deflated Sharpe]].

| # | Brick | Change | Why | Expected effect |
| --- | --- | --- | --- | --- |
| V1 | Sizing | Inverse-volatility legs | AUD and NZD should not dominate a dollar bet | Lower volatility, similar mean, higher t-stat |
| V2 | Condition | Only meetings with high monetary uncertainty, measured on past data only | Tests P2 | Higher mean per trade, fewer trades. Needs a free measure; if none exists, drop V2 |
| V3 | Universe | Add USD/JPY | Tests the free choice of pairs | If the mean falls sharply, the yen behaves as a haven on these days: note it |

Stress tests, not tries: window of 12 and 48 hours; exit at 0 and 15 minutes; mid prices against bid/ask; EUR/USD alone.

## 1.10 Test plan

- **Sample**: 2012-01 to the latest meeting. **In-sample**: before 2019. **Out-of-sample**: 2019 to 2024, fixed now. Later meetings are a fresh sample, added as they come.
- **Diagnostics required**: placebo distribution of ordinary-day windows (P1), returns by uncertainty level (P2), exit-offset curve (P3), FOMC eves with falling equities (P4), contribution by meeting (P5).

## 1.11 Kill criterion (backtest)

- Basket t-stat below 2 in-sample, or a result carried by one pair.
- FOMC windows not above most placebo windows (P1), or the drift gone with an exit before the announcement (P3).
- Out of sample: the three-zone rule.
