---
type: reading-note
source: paper
title: "Extreme returns: The case of currencies"
authors: Osler, Savaser
affiliations: Osler (Brandeis International Business School), Savaser (Williams College)
year: 2010
venue: Working paper, November 2010
doi:
pdf: "[[2010 - Osler Savaser - Extreme returns The case of currencies.pdf]]"
version: working paper
tier: 1
read: full
tags: [seasonality-flows, fx, intraday]
date: 2026-10-25
---

# Extreme returns, the case of currencies (Osler, Savaser 2010)

## Summary

- **Finding**: simulations calibrated on RBS stop-loss and take-profit orders give 1-hour return excess kurtosis equal to 52% to 69% of the observed one in EUR, JPY, GBP (concave impact). Not a trading strategy.
- **Mechanism (authors)**: price-contingent orders have four properties (fat-tailed sizes, time-of-day clustering, round-number price clustering, feedback) that interact and produce fat tails without news.
- **Where it works best**: real data only show high kurtosis below one hour (EUR 23.8 at 15 min), falling to 3.5 to 4.7 at 48 hours (Table 2A).
- **Weak spots**: every attribution comes from simulation. Linear impact gives kurtosis far above observed (EUR 945.8 against 18.7). No test of any trading rule.
- **Main caveats**: one dealer's orders (47,312, 1999 to 2002), market share guessed at 4%, nothing out of sample, news limited to eight US releases.

Page numbers follow the PDF, which matches the printed pages. Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Extreme returns can occur without news, because price-contingent trading (algorithmic, technical, dynamic option hedging) makes order flow extreme | Simulations only. Extreme hourly returns "statistically inevitable" | p. 3-4, 31 |
| 2 | Order sizes are fat-tailed and spiky at round numbers | EUR order-size kurtosis 725 (31 without the largest order); JPY 26; GBP 21. Spikes at 1, 2, 3, 5, 10, 20 million | p. 13-14; Fig. 1 |
| 3 | Order execution clusters by time of day | Share of EUR orders executed per hour from about 0 (20 to 23 GMT) to about 10% (about 15 GMT) | p. 16-17; Fig. 2A |
| 4 | Trigger rates cluster at round levels, and stop-loss and take-profit cluster differently | Almost 6% of executed orders end in 00. Stop-loss sells are rarer just above 00 (5.9%) than stop-loss buys (10.9%) | p. 18-19; Fig. 3; Table 4A |
| 5 | Feedback: stop-loss orders cause price cascades, take-profit orders cause price halts | Cited from Osler (2005). Cascades "perhaps a few times per week" per market participants | p. 23-24 |
| 6 | The four properties interact and amplify each other | EUR half-hour order-flow kurtosis 305.3 with three factors, against a summed direct effect of 138.2 | p. 21-22; Table 5 |

**Caveats raised by the authors**
- Share of stop-loss and take-profit in all FX order flow is "five percent or less" per dealers, and no data exist to check it (p. 11).
- Orders per half hour (4 EUR, 5 JPY, 3 GBP) come from a "back-of-the-envelope" guess using a bank share of about 4% (p. 16).
- The concave (square root) impact form is borrowed from other work, "in the absence of other evidence" (p. 27).
- News covers only eight scheduled US releases (p. 29).
- Much price-contingent trading is never placed as orders (p. 10-11).

**Ruled out**
- News alone: with simulated news added, kurtosis rises little and mostly below 6 hours (Table 8, p. 30).
- A fixed return distribution: the authors say the distribution may shift over time (p. 5-6).

## 2. Strategy, brick by brick

No trading strategy is tested. The paper is a model of order flow. Its inputs are listed here.

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | EUR/USD, USD/JPY, GBP/USD | p. 10 |
| Period | Orders: 8 Sep 1999 to 11 Apr 2000 and 12 Jun 2001 to 20 Sep 2002, called 24 months. Quotes: 2 Jan 2000 to 9 Nov 2002, 13 Sep to 8 Oct 2001 excluded | p. 9-11 |
| Signal | None | n/a |
| Horizon | Returns from 15 minutes to 48 hours (72 hours in Fig. 6) | Table 2A |
| Sizing, costs | None | n/a |

**Rule**: none. Order definitions (p. 8). Stop-loss buy: buy Q at market if the rate rises to S. Take-profit buy: buy Q at market if the rate falls to S. Sells are mirrored.

Simulation recipe (p. 15, 19-20, 24-27):
- One period is half an hour. 30 series of 62,400 periods per currency.
- Order flow is the sum of signed order sizes executed in the period, drawn from the observed size distribution.
- Number of orders per period follows the observed intraday pattern. The trigger-rate digit follows the observed round-number frequencies. 43% of orders are stop-loss.
- Return: change in log rate = f(order flow), with f linear or square root.

**Data provenance**
- Orders: all stop-loss and take-profit orders processed by the Royal Bank of Scotland desk, 47,312 orders worth $253.9 billion, 27% executed. Only executed orders are used (p. 10; Table 1).
- Quotes: Reuters indicative mid-quotes every 5 minutes, from the Federal Reserve Bank of New York. Weekend defined as Friday 4 p.m. to Sunday 4 p.m. EST (p. 11).
- Interdealer trade sizes: EBS, 1999, kurtosis 98.8 (p. 30).

## 3. Results

**Aggregate** (all values gross, no trading involved)
- Real data, return kurtosis, Table 2A: EUR 23.8 at 15 min, 18.7 at 30 min, 13.8 at 1 hour, 4.1 at 24 hours. JPY 18.1, 14.4, 11.9, 3.9. GBP 13.3, 10.5, 8.8, 3.7.
- Real data, half-hour EUR returns beyond 3.5 standard deviations: 19.4 times the normal frequency (Table 2C).
- Simulation, concave impact, comprehensive: 1-hour return kurtosis EUR 10.5, JPY 7.7, GBP 6.8. These are 69%, 52%, 65% of observed excess kurtosis (p. 27; Table 6C).
- Simulation, 1-hour returns of 3.5 to 4.5 standard deviations occur 4.8 to 7.6 times more often than under the normal (p. 27-28; Table 7).
- Authors' illustration: a 5.5 standard deviation 1-hour move in EUR (0.6%) about 26 times a year, in JPY (0.7%) about 115 times a year (p. 28).

**By sub-group** (simulation, one factor at a time, half-hour order-flow kurtosis)
- Order sizes alone, at 4, 5, 3 orders per period: EUR 129.8, JPY 9.5, GBP 10.3 (p. 16; Table 3).
- Time-of-day alone: 4.0, 3.8, 4.4 (p. 18).
- Round-number levels alone, 6 levels crossed: 3.9, 3.8, 4.0 (p. 21; Table 4B).
- Feedback alone, linear, half-hour return kurtosis: 12.5, 11.0, 14.0 (p. 25; Table 6A).
- All three order-flow factors together: 305.3, 20.3, 23.8 (Table 5).

**Horizon and parameters**
- Order-flow kurtosis falls with more orders per period: EUR 513.0 at 1, 54.6 at 10, 8.2 at 100 (Table 3).
- It falls with horizon, still above 3 at 48 hours (EUR 5.8, Table 5).
- With concave impact, return kurtosis rises from half hour to 1 hour (EUR 7.8 to 10.5) then falls (p. 27; Table 6C).
- Hill tail index, OLS: half-hour 3.25 to 3.76, 12-hour 4.01 to 5.38, so kurtosis exists at 12 hours, not at half hour (p. 12; Table 2B).
- 11 orders per period instead of 4 (EUR): half-hour kurtosis about 20% lower, long-horizon kurtosis higher (p. 28-29; Fig. 6).

**Over time**: not addressed. Simulations assume stationary order flow.

**Link to other strategies**: the authors say stop-loss orders may add to crash risk linked to carry trade returns, as an equilibrium argument, with no test (p. 6, 32).

**Inconsistencies in the source**
- p. 14: orders within 1.5 to 2.5 standard deviations "15 percent, less than one-third the 48 percent under the normal". Table 2C gives 12.1% for that band under the normal. 48.4% is the 0.5 to 1.5 band.
- p. 28: returns above 5.5 standard deviations "80 and 90 times more frequently" than normal. Table 7 gives 18.7 to 75.9 for 4.5 to 5.5 and 843.5 to 5060.8 for 5.5 to 6.5.

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Jump processes in option pricing may come from price-contingent trading | p. 6, 32 |
| Analysis "potentially relevant" to equity and futures markets (stop orders in the May 2010 flash crash) | p. 7, 31 |
| Price cascades happen about a few times a week | p. 23 |
| Non-price-contingent trading "could" add substantially to kurtosis | p. 31 |
| Carry returns partly compensate crash risk fed by stop-loss orders | p. 6, 32 |
| Large dollar-yen and sterling-dollar orders not executed by chance, kurtosis would match EUR on a longer sample | p. 15 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | OLS Hill estimator of the tail index, regressing estimates on k = 0.10, 0.20 | technique | evaluation | Check whether kurtosis exists | p. 12, fn. 5; Table 2B |
| 2 | Fraction of returns by standard deviation band, as a ratio to the normal | technique | evaluation | Show excess mass in the tails and near the mean | Table 2C, 7 |
| 3 | Adaptive breakout: stop orders placed beyond the range of the first 14 trading hours of Monday | technique | entry | Quoted from a trading magazine, not tested | p. 8, fn. 2 |
| 4 | Monte Carlo of order flow with calibrated size, time-of-day and level clustering | technique | evaluation | Measure each factor and their interactions | p. 15-27 |

No card from these four (see the reply).

## 6. Regime observations

- Order execution is almost nil from 20 to 23 GMT and peaks near 15 GMT, with volatility showing the same shape (Fig. 2A, 2C; p. 16-17).
- Euro-dollar crosses about 3 pip levels per half hour overnight and up to 12 at mid-afternoon in London (p. 17).

## 7. Acknowledged limits

- No test of order-flow data beyond one bank, and no measure of the real share of price-contingent trading (p. 11).
- Simulated kurtosis stays below the observed one with concave impact, "leaving room for contributions from other factors" (p. 27).
- Sample kurtosis is used "purely as a descriptive device" (p. 12).

## 8. Not addressed

- Any trading rule, return, Sharpe ratio, costs or drawdown.
- Daily or monthly data, the 2008 to 2021 period, carry or rate data.
- Out-of-sample check of the calibration.
- Whether the round-number or time-of-day patterns can be traded.
- Capacity.
