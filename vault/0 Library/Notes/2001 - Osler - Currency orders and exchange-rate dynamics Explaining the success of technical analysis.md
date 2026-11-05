---
type: reading-note
source: paper
title: "Currency orders and exchange-rate dynamics: Explaining the success of technical analysis"
authors: Osler
affiliations: Federal Reserve Bank of New York
year: 2001
venue: Federal Reserve Bank of New York Staff Report No. 125
doi: "https://hdl.handle.net/10419/60582"
pdf: "[[2001 - Osler - Currency orders and exchange-rate dynamics Explaining the success of technical analysis.pdf]]"
version: working paper, March 2001
tier: 1
read: full
tags: [trend, fx, intraday]
date: 2026-10-25
---

# Currency orders and technical analysis (Osler 2001)

## Summary

- **Finding**: In a bank's book of 9,667 FX stop-loss and take-profit orders, requested rates cluster at round numbers; 9.3% of take-profit orders sit at 00 against 4.4% of stop-loss orders (p. 18).
- **Mechanism**: Take-profit orders reflect trends and cluster at round numbers; stop-loss orders intensify trends and sit just beyond them. Together they explain reversals at, and breakouts through, round numbers (p. 5-6).
- **Where it works best**: Real data: order placement only, no price test. Stop-loss buys: 14.4% at 01-10 against 7.4% at 90-99 (Table I). Price tests are in other papers.
- **Weak spots**: Price dynamics are shown only in the author's simulation. Take-profit asymmetries around 00 and 50 are not significant (Table I). Two-period bounce at 00 only: 7 of 10 series (Table III).
- **Main caveats**: One bank, 7 months, three pairs. No profit test: the paper is "silent" on efficiency (p. 31). Simulation parameters are set to make order flow dominate (p. 22, 28).

Page numbers follow the journal pagination printed on the page (PDF page minus 1). Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Exchange rates respond to order flow in the short run | Cited literature (Evans and Lyons 1999, Lyons 2001 and others) | p. 2, 5 |
| 2 | Take-profit orders reflect or reverse trends; stop-loss orders propagate them | Definition by direction and by position of the requested rate against the market rate | p. 5, 17 |
| 3 | Take-profit orders cluster more at 00 than stop-loss orders, so round numbers act as partial reflecting barriers | 9.3% against 4.4% at 00; bootstrap marginal significance 1.1% | p. 17-18 |
| 4 | Stop-loss buys sit just above round numbers, stop-loss sells just below, so trends gain speed after the level is crossed | Table I: 3 of 4 stop-loss asymmetries below 5%, the fourth 6.4%; none for take-profit | p. 19-20, Table I |
| 5 | Placing orders at these points may be rational because the resulting price behaviour rewards it (self-fulfilling) | Argument only | p. 21-22 |
| 6 | Why orders are used: slow execution, information overload, dealer overnight stop limits, self-discipline (disposition effect) | Argument and dealer interviews | p. 9-11 |
| 7 | Why round numbers: no settled cause. Tick sizes ruled out; negotiation simplicity, attraction of some integers and self-fulfilment are suggested | Discussion | p. 16-18 |

**Caveats raised by the authors**
- Comparable order data is not available, so representativeness cannot be proven (p. 6).
- The simulations are not meant to represent real rates; order flow is made to dominate (p. 22).
- Round-number clustering alone cannot answer why clustering began (p. 17-18).
- Results are silent on market efficiency and risk-adjusted profit (p. 31).

**Ruled out**
- Central bank intervention as the source of support and resistance success (p. 3, citing Neely 2000 and Osler 2001).
- Tick-size discreteness as the source of clustering: orders cluster on a subset of the available endings (p. 17).

## 2. Strategy, brick by brick

The paper is not a trading strategy. It describes order placement and a simulated price process. The trading rules it explains come from technical analysis.

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | USD/JPY, GBP/USD, EUR/USD (43%, 24%, 33% of orders) | p. 11 |
| Period | Orders from September 1, 1999 to April 11, 2000 | p. 4 |
| Signal | Round number as support or resistance: levels ending in 00 or 50 (or 00 only) | p. 13, 29 |
| Entry | Not addressed. Prediction 1: expect a reversal at the level. Prediction 2: expect a trend after the level is crossed | p. 2, 12-13 |
| Exit | Not addressed | |
| Horizon | Simulated observation is about 15 minutes; the tested horizons are one and two periods | p. 26-27 |
| Sizing, portfolio, rebalancing | Not addressed | |
| Costs | Not addressed | |
| Data and tools | Order book of one dealing bank; bootstrap tests; own simulation | p. 4, 18-20, 26-28 |

**Rule** (as tested in the simulation, p. 27)
- A level is "hit" when the rate comes within 0.01% of it.
- It "bounced" if the rate rises (falls) over the next one or two periods after a hit on a support (resistance).
- Bounce frequency = bounces / hits. Compared with arbitrary levels drawn inside the same 10-day range, interval by interval; the count of intervals where round numbers beat arbitrary ones is tested against a binomial with p = 1/2 (p. 27-28).
- Second measure: average rate move after a hit, conditional on no bounce (p. 27).
- Simulation: x(t+1) - x(t) = beta O(t), with O = lambda C + mu v + delta(x_bar - x), C the conditional orders executed at the two-digit levels just crossed, weighted by the observed distribution (p. 23-25).

**Data provenance**
- 9,667 conditional orders from a large dealing bank serving banks, non-bank financial firms, central banks, corporates, wealthy individuals, hedge funds and CTAs (p. 6, 11).
- Average order size $5.8 million, median $3.0 million. 92 new orders a day. Over 70% closed within one business day, median open time 0.4 days, mean 3.4 days. About one third executed (p. 11-12).
- Conditional orders are 5 to 10% of the bank's deal flow, informal estimate (p. 8).
- Distributions use requested rates of executed orders only (note 12). Quotes are in the market convention: yen per dollar, dollars per pound, dollars per euro (p. 13).
- The price results the paper relies on (minute quotes, Jan 1996 to Apr 1998, dollar-mark, dollar-yen, dollar-pound) are in Osler 2000 and 2001, not in this paper (p. 3, 12-13).

## 3. Results

**Aggregate** (real data, order book, no prices)
- Uniform null rejected for all three pairs, Anderson-Darling statistics 65.8 (yen), 137.6 (pound), 63.5 (euro) against 8.0 critical at 0.01% (p. 14, note 13).
- Largest cluster at 00, about 8.7% of orders; then 50, other multiples of 10, then 5. No tendency at 25 or 75 (p. 14).
- Order shares by type at 00 (Table I): stop-loss buy 3.5, stop-loss sell 5.2, take-profit buy 8.1, take-profit sell 10.5 (percent).

**By sub-group**
- Around 00, stop-loss buy: 90-99 is 7.4%, 01-10 is 14.4%, difference 7.0, marginal significance 0.029. Stop-loss sell: 10.0 and 5.1, difference -4.9, 0.064 (Table I).
- Around 50, stop-loss buy: 40-49 is 17.3%, 51-60 is 6.3%, difference 11.0, 0.002. Stop-loss sell: 8.0 and 16.9, difference -8.9, 0.004 (Table I).
- Take-profit orders, both sides, both levels: differences between -1.5 and 1.2, marginal significance 0.356 to 0.485 (Table I).
- Same pattern in the three pairs and with orders weighted by value (Fig. 1A, 1B, p. 15).
- Clustering stronger for the pound and euro pairs, the only two comparable in level (p. 15).
- Heuristic: at a round number reached from below, 2.8% of stop-loss buys and 10.5% of take-profit sells trigger. Just above, at 10, 4.5% of stop-loss buys and 2.7% of take-profit sells (p. 19-21). Amounts of the two order types are said to be roughly equal on average (p. 19).

**Horizon and parameters** (own simulation, 250,000 periods, 10 starting values, lambda = mu = 0.5, delta = 3.0, beta = 0.00015, conditional orders about 74% of order flow)
- Levels 00 and 50, bounce frequency above arbitrary levels in 10 of 10 series at one period and at two periods; average gap 3.47 and 3.41 points of percent (Table III).
- Significance at two periods: 5 series at 0.01%, 5 at 1% (Table III).
- Move after a hit with no bounce, larger at round numbers in 10 of 10 series, average 4.2 against arbitrary 4.7 points at one period; 3.7 against 4.5 at two periods (Table IV; "average difference" and "average MVAN" as printed).
- Level 00 only: bounce above arbitrary in 10 of 10 series at one period, 7 of 10 at two; gap 2.15 and 1.80; 1 and 3 series significant at 0.01% and 1% at one period (Table III).
- For comparison, actual rates in Osler 2001: bounce gap 4.6 points averaged over three pairs; post-hit move 0.0014% larger than at arbitrary levels, base 0.0063% (p. 30). These are quoted from another paper.

**Over time**
- Not addressed. One 7-month sample of orders.

**Link to other strategies**
- Related to filter rules and trend-following algorithms, head-and-shoulders and genetic algorithms, described as successful in FX (p. 2). Round-number clustering is compared with stock limit orders (p. 15-16).

**Inconsistencies in the source**
- Stop-loss buy orders at 00: text gives 2.8% (p. 19) and Theta(sb,00) = 0.0284 (p. 25); Table I gives 3.5.
- p. 30 says the round-number bounce result is significant at 0.01% "in all cases" (20 cases); Table III shows five two-period series at 1%.
- p. 30 says the post-hit move gap is significant at 1% or better in all 20 cases; Table IV for levels 00 only shows 2 one-period series at 5%.
- p. 30 says the 0.0037% larger move is "quite a bit bigger" than the arbitrary-level move of 0.0045%. 0.0037 is smaller than 0.0045. Table IV gives moves in points, the text in percent.
- Fig. 2 panels A and B are both labelled "Stop-loss" and C and D "Take-profit"; the buy or sell side is given only in the text (p. 18).

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| The bank's patterns are representative of all FX dealers | p. 6 |
| Tendencies like the simulated ones "will likely be present" in actual rates, to a lesser degree | p. 22-23 |
| Results "quite consistent" across many parameter sets | p. 29 |
| Clustering of conditional orders induces excess kurtosis in order flow ("can be shown") | p. 32 |
| Clustering implies path dependence and may explain the exchange-rate disconnect | p. 32 |
| Practitioners place stop-losses just beyond support and resistance because they believe the two predictions | p. 22 |
| One simulated period is about 15 minutes (the author says it cannot be justified empirically) | p. 26, note 18 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | Round numbers (00, 50) as support and resistance: expect a bounce, or a trend after a break ([[Round number support and resistance]]) | technique | signal | Order clusters at round numbers (take-profit reflecting, stop-loss intensifying) | p. 2, 29 |
| 2 | Stop-loss placed just beyond a support or resistance level | principle | risk | Practitioner advice, based on the two predictions; stop-loss buys cluster just above round numbers | p. 21-22 |
| 3 | Bounce frequency at a level against arbitrary levels in the same range, binomial test over intervals ([[Level placebo test]]) | technique | evaluation | Removes sensitivity to the number of hits | p. 27-28, note 20 |
| 4 | Average move after a hit with no bounce, against arbitrary levels (same card: [[Level placebo test]]) | technique | evaluation | Tests whether trends gain momentum after the cross | p. 27 |
| 5 | Distribution of the last two digits of prices or orders against a uniform | technique | evaluation | Detects clustering | p. 14 |

## 6. Regime observations

- Not addressed. The author notes that exchange rates are path dependent at high frequency (p. 22).

## 7. Acknowledged limits

- Representativeness of one bank cannot be proven (p. 6).
- Simulations exaggerate the effect of conditional orders on purpose (p. 22).
- Order clustering is not fully explained (p. 17-18).
- No test of risk-adjusted profit (p. 31).

## 8. Not addressed

- Any trading rule, return, Sharpe ratio, costs, slippage, drawdowns or capacity.
- Price data in this paper: all price tests are in Osler 2000 and 2001.
- Daily or monthly horizons; the tested horizons are 15 and 30 simulated minutes.
- Stability over time of the clustering; out-of-sample test.
- Pairs other than yen, pound and euro against the dollar.
