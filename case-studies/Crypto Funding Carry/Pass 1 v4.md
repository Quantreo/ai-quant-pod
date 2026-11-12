# Crypto Funding Carry · Pass 1

**Verdict: Go with a check.** The payer can be named (leveraged longs paying funding), but the library shows carry only outside crypto, and the cross-sectional version may hand back in price what it collects in funding, or earn in price what carry does not explain. **Check first, on the train period only, base version, before any tuning**, two criteria (1.11 #1 and #2): a gross Sharpe of at least 0.56 (luck line) plus cost / volatility, which is 1.04 at the base turnover and central cost; **and** funding at least half of the gross P&L (price plus funding). If either fails, kill. **Warning**: at 95.2× a year and 10 bp, costs are 9.52% of capital a year; the gates use the measured turnover, and a slower version is not planned.

---

## 1.1 Mechanism

**Type**: risk premium (leverage demand), with a constraint component on the short side.

**Who pays.** Traders who want leveraged long exposure to a coin, and use the perpetual rather than borrowing to buy spot. When long demand exceeds short supply, the perp trades above the index and the funding rate turns positive: longs pay shorts every funding interval. Whoever holds the short side is paid to supply the leverage the longs want, and to carry the risk that the coin keeps rising. [hypothesis] The book is long the perps with the lowest trailing funding and short those with the highest: it collects the funding spread if prices do not move against it by as much. [hypothesis: our transposition of the carry signal]

**What the sources show.**
- Carry, defined as what a position earns if prices stay unchanged, has a positive Sharpe in all nine asset classes tested, 0.37 to 1.80, gross, monthly, rank-weighted. [source: Koijen 2013, Table II A] Crypto is not among them.
- Carry predicts returns with a coefficient positive in every class, though not significant for commodities and calls. [source: Koijen 2013, Table VI]
- Every carry strategy loses in global carry drawdowns, which coincide with recessions. [source: Koijen 2013, p. 31, Table VIII]
- Whether the premium is macro risk or limits to arbitrage and funding squeezes is left open by the authors. [source: Koijen 2013, p. 4]
- Crypto carry and perpetual funding are studied in papers not yet in the library; figures not checked. [literature, not in library: Schmeling Schrimpf Todorov 2023; He Manela Ross von Wachter 2022; Christin Routledge Soska Zetlin-Jones 2023]
- The desk's own Crypto XS Momentum book collected funding for 24% of its P&L on the point-in-time universe [source: vault/_archive/stl-strategies/Crypto XS Momentum.md]: a hint that funding is large enough to matter, not a test of this idea.

**Why it is not arbitraged away.**
- The clean arbitrage (short perp, long spot) needs spot inventory, capital on two venues and margin, and has no spot short for negative funding names. [hypothesis]
- The short side of a hyped coin can be squeezed far and fast; margin calls force shorts out at the worst moment, which keeps capital away. [hypothesis]
- Counterparty and exchange risk on collateral. [hypothesis]
- Studied in the literature since at least 2022: the premium may already be thinner than in early data. [literature, not in library: Schmeling Schrimpf Todorov 2023]

**What it could secretly be.**
- **Short momentum or short lottery**: high funding follows sharp rallies; the short leg may be a bet against recent winners, which is not carry.
- **Short beta**: high-funding names are likely the high-beta ones; a capital-neutral book can be net short the crypto market, or short alts against BTC.
- **Short volatility / crash risk**: small, steady funding gains, paid back in squeezes.
- **Liquidity premium**: if the profit sits in the thinnest names, costs not captured by a flat 10 bp take it.

**Predictions, to be checked by the Diagnostic.** P1, P4 and P5 separate carry from the rival (short momentum, short alts, one regime); P2 and P3 do not, and are read as checks of the risk.
- **P1** Funding carries the gross P&L: on the train period, the funding component is at least half of price plus funding. Under carry, the price spread between high and low funding names stays small [hypothesis]; under the rival, price carries the P&L.
- **P2** Returns are negatively skewed, and the worst weeks fall in sharp altcoin rallies (squeezes of the short leg). Also true under short beta: a check of the risk, not of the mechanism.
- **P3** Funding plus price is higher in weeks of high funding dispersion than in weeks of low dispersion: the extra funding collected is not handed back in price. Dispersion is the cross-sectional standard deviation of the 7-day annualised funding rates across the eligible universe, at the rebalance. The extra funding alone is mechanical and is not the test.
- **P4** The intercept stays positive, with a t-stat of at least 2, after regressing on BTC, on an alt-minus-BTC factor, on a high-minus-low volatility factor, on a 7-day return factor and on the price-only returns of Crypto XS Momentum.
- **P5** The gross Sharpe on train plus validation without 2022 stays at least 0.56 (luck line, 3.5 years) plus cost / volatility, 1.04 at the base turnover and central cost: the result is not one regime (the 2022 alt crash, when the short leg fell).

## 1.2 Sources and crowding

- **Sources**: [[2013 - Koijen Moskowitz Pedersen et al - Carry]], derived on two bricks: [[Carry signal]] (futures basis becomes the perpetual funding rate) and [[Long-short portfolio weighting]] (rank weights, Eq. 23), applied to Binance USDT perpetuals.
- **Earlier attempts**: none on carry by the desk. Crypto XS Momentum flagged funding as its hidden carry component.
- **Crowding**: funding rates are public, real time, and shown on every aggregator; cash-and-carry is a standard trade for crypto funds. The cross-sectional version is less common but easy to build. [hypothesis]

## 1.3 Expected behaviour

- **Works when**: leverage demand is high and spread unevenly across names, prices drift sideways, funding dispersion is wide.
- **Suffers when**: a short squeeze lifts the high-funding names; the whole market rallies with alts leading; a liquidation cascade hits the long leg.
- **Payoff**: many small weekly gains, rare large losses. A few squeeze weeks and a few names will decide the year.

## 1.4 Universe

- Top 30 Binance USDT perpetuals by trailing 30-day quote volume, **point-in-time**, listed for at least 90 days.
- **Why a cut-off**: the payer exists in every perp, but the highest funding sits in the smallest, thinnest names, where a flat 5 bp cost is too low. This justifies a cut-off, not the number 30: tested as a stress test (1.5b). 30 rather than the 20 of Crypto XS Momentum because a ranking on funding needs enough names in each tail.
- **Why a listing age**: the first weeks after listing have wild funding and thin books. 90 days is free.
- **Survivorship**: measured, not declared. Control: today's top 30 applied to the past, same code.

## 1.5 Base version, brick by brick

| Brick | Choice | Why | Basis | Card |
| --- | --- | --- | --- | --- |
| Signal | Trailing 7-day average funding rate, annualised, known at the rebalance | Funding is what a perp position earns if the price stays unchanged: the carry of a perp | source (Koijen 2013, p. 6-7, transposed) | [[Carry signal]] |
| Signal | Average over several funding prints, not the last one | A single print is noisy; the mechanism is persistent leverage demand | mechanism | [[Carry signal]] |
| Portfolio | Cross-sectional rank weights, rank minus its mean, long the lowest funding, short the highest | The premium is the funding spread between names | source (Koijen 2013, Eq. 23, p. 18) | [[Long-short portfolio weighting]] |
| Sizing | Rank weight times inverse volatility per name; long and short legs scaled separately to the same notional, sides set by the rank (1.5b) | Volatilities differ widely across names; equal risk per name; the side comes from funding, not from volatility | convention (house default); source for the sides (Koijen 2013, Eq. 23, p. 18) | [[Volatility targeting]] |
| Sizing | Strategy volatility target 20% on the book's ex-ante volatility (60-day covariance, 1.5b), gross book capped at 3× capital | Sets the size of the book; the cap bounds the leverage per position in isolated margin (1.8) | scale (target); risk (cap, 1.5b) | [[Volatility targeting]] |
| Rebalancing | Weekly, trade only outside a no-trade band | The signal window is a week; the band cuts turnover | cost | [[No-trade band]] |
| P&L | Split into price, funding and costs from the first run | The edge is funding; the risk is price | convention (house default) | none |
| Costs | 10 bp one way central, 5 bp favourable, 20 bp stress, from the first run; 10 and 20 bp to confirm | [[Cost Assumptions]] gives 5 bp for top names, but the short leg sits in the tail of the top 30, so the central case is set above it | cost | none |

## 1.5b Free parameters

| Parameter | Value | Why this value | Tested as |
| --- | --- | --- | --- |
| Universe size | top 30 | Enough names in each tail, still tradable at the central 10 bp | stress test: 20, 30, 50 |
| Listing age | 90 days | Skips the wild post-listing weeks; leaves 60 days for the volatility estimate after the signal window | stress test: 60, 90, 180 days (60 is the floor set by the volatility window) |
| Funding window | 7 days | 21 prints at 8 hours: smooths noise, matches the weekly rebalance | stress test: 3, 7, 30 days |
| Rebalance frequency | weekly | Matches the 7-day funding window | none: follows from the window |
| Rebalance time | Monday 00:00 UTC, right after the funding print | At a funding time, so no position holds a partial interval; the print at 00:00 goes to the old position and is the last one the signal uses. The day is free | none: free, fixed now |
| Band width | 10% of the target position | Same as Crypto XS Momentum; cost budget | stress test: 0, 10, 20% |
| Band exit | Outside the band, trade to the edge of the band, not to the target | The band exists to trade as little as possible ([[No-trade band]]); lab default; the 40% rotation of 1.7 already assumes the band | none: follows from the band |
| Volatility window | 60 days | Convention for daily crypto risk estimates | none: convention |
| Volatility estimator | Standard deviation of daily close-to-close returns, equal weights, over the window | The plainest estimator; nothing in the mechanism asks for another | none: convention |
| Book volatility estimator | 60-day sample covariance of daily mark returns, equal weights, applied to the target weights | Target set on the whole book from a covariance, as in Daniel 2014 ([[Volatility targeting]], p. 10-11); correlations matter in a long-short book; same window and estimator as per name | follows from the volatility window and estimator |
| Leg neutrality | Long and short legs each scaled to half the gross book; a name's side is that of its rank | Capital-neutral without letting a mid-ranked name switch side for a volatility reason, which would not be carry (Koijen 2013, Eq. 23). The short leg, in the more volatile names, carries more risk: accepted, read in P2 | none: follows from the signal |
| Volume window | trailing 30 days | A monthly view of liquidity | none: convention |
| Minimum names | 20 eligible names; below that the book is flat and the week counts as zero | Both tails need enough names for a rank to mean something; matters only in the thin months of 2020 | none: data condition, fixed now |
| Funding input caps | none | Rank weights: an extreme print moves a name by one rank, not its weight | follows from rank weights |
| Tie rule | Average rank for names with equal 7-day funding | Koijen Eq. 23 does not define ties; Binance funding may sit at its interest component for many names [hypothesis, to check in data]. Free | none: free, fixed now |
| Margin reset | Isolated margin re-allotted pro rata to notional at every rebalance, for every position, inside the band or not; no top-up between rebalances | Keeps the leverage per position at the gross book; a margin transfer is not a trade and costs nothing | none: risk rule, fixed now |
| Gross book cap | 3× capital | Leverage per position equals the gross book in isolated margin (1.8); at 3× a +32% squeeze liquidates a short ([[Instrument Traps]]), beyond it a common week would | none: risk limit, fixed now |
| Funding dispersion | Cross-sectional standard deviation of the 7-day annualised funding, at the rebalance | Measures the spread the book collects (P3, V2) | follows from the signal |
| V1 beta window | 60 days | Same as the volatility window | follows from the volatility window |
| V1 neutralisation | Long leg notional multiplied by (beta exposure of the short leg / beta exposure of the long leg), no BTC hedge; no scaling in a week where a leg has a beta of 0 or less; then the 20% target and 3× cap applied again | The variant changes the portfolio brick only, sizing stays that of the base so risks compare | none: follows from 1.9 |
| V3 hedge ratio | Long BTC notional = 60-day beta of the short leg × its notional, BTC netted if it sits in the short leg; then the 20% target and 3× cap applied again | Hedges the market, not just the notional, so the short leg's own funding is what is read; same window as V1 | follows from the V1 beta window |
| Liquidation cost | Maintenance margin lost plus 10 bp (cost_bp) on the liquidated notional | A forced close is a trade ([[Instrument Traps]]: margin plus fees); Binance's own liquidation fee is not in the library [to confirm] | follows from the cost assumption |
| V2 threshold | Median of past dispersion, expanding window | The median splits the weeks in two without a tuned number | follows from P3 |
| Alt-minus-BTC factor | Top 30 excluding BTC, equal weights, price only, minus BTC | Equal weights so the thin alts, where the rival sits, count; free | none: free, fixed now |
| Volatility factor (P4) | Top 30, top tercile of 60-day volatility minus bottom tercile, equal weights, price only, weekly at the rebalance | Controls short volatility and short lottery; same window as the sizing; terciles free | none: free, fixed now |
| 7-day return factor (P4) | Top 30, top tercile of past 7-day price return minus bottom tercile, equal weights, price only, weekly at the rebalance | Controls the bet against recent winners on the signal's own window; contains no funding; terciles free | follows from the funding window |
| Intercept threshold (P4) | t-stat of 2 | House significance level (`budget.py`) | none: kill threshold |
| Concentration flag | top 5 names above 60% of the gross P&L | 5 names are a sixth of the universe; 60% is more than three times their equal share. Free | diagnostic only, not a kill |

## 1.6 Horizon, trades and statistical power

- **Holding period**: one week, positions often rolled over several weeks.
- **Turnover**: 95.2× a year as the base, 53.6× and 32.8× as alternatives (1.7).
- **Observations**: 2020-07 to 2026-09, about 6.2 years, about 320 weekly periods. Train 3.5 years (182 weeks), train plus validation 4.5 years (234 weeks), train plus validation without 2022 3.5 years (182 weeks). Before 2021 the number of perps is thin.
- **Years counted**: only the weeks in which the book trades (at least 20 eligible names). The Data check counts them before the first run; if they are fewer than above, `budget.py` is re-run and every gate in 1.6 and 1.11 updated.
- **Luck line** (`budget.py`): best of 4 tries (base plus 3 variants) reaches a Sharpe of 0.56 with no skill over 3.5 years (the train, and train plus validation without 2022).
- **Power of the gates, on the sample where each applies** (Sharpe standard error about 1 / sqrt(years)):
  - **1.11 #1** (train, gate 1.04): a true gross Sharpe of 1.2 passes 62% of the time, 1.0 passes 47%, zero passes 2.6%.
  - **1.11 #2** (train): if the price component has a true mean of zero and funding is 24% a year (gross Sharpe 1.2 at 20% volatility), the gate passes about 99% of the time; under a rival with funding 8% and price 16% a year, it still passes about 23% of the time (price mean standard error 20% / sqrt(3.5) = 10.7%). [hypothesis: the split of the rival]
  - **1.11 #3** (train plus validation, t of 2 on 234 weeks, a mean of at least 0.13 of its standard deviation, `budget.py`): a residual Sharpe of 1.0 passes 55% of the time, 1.5 passes 88%, zero passes 2.3%.
  - **1.11 #4** (train plus validation without 2022, 3.5 years, gate 1.04): a true gross Sharpe of 1.2 passes 62% of the time, zero passes 2.6%; a book whose gross P&L comes only from 2022 passes about 2.6%. #1 and #4 share 2.5 years, so both together pass less often than either.
  - Low power is accepted: the bars are not lowered (house rule, strict gates).

**Data already seen**: the desk has used Binance perps from 2020-07 to 2026-08, funding included, for Crypto XS Momentum, and knows that book collected funding (24% of its P&L, about 11 points in 2023). None of the three periods is clean: the true out-of-sample starts with paper trading.

## 1.7 Cost and capacity budget

**Turnover definition.** Turnover counts everything traded, sales and purchases, over the capital. The gross book follows from the volatility target: 2× capital is the reference [hypothesis: to be replaced by the measured spread volatility], capped at 3×; turnover scales with it. Three sources at each weekly rebalance:
- **Signal rotation**: 40% of the gross book replaced, sale and purchase, 0.4 × 2 × 2 = 1.6× capital. The 40% is an assumption from the persistence of a 7-day funding average and the 10% band. [hypothesis]
- **Universe churn**: about one name in and one out of the top 30 a week, at an average position of 1/15 of capital, sale and purchase: about 0.13×. [hypothesis]
- **Volatility rescaling**: the gross book moves about 5% a week with the 60-day volatility estimate: about 0.10×. [hypothesis]

The Developer measures the real figure on the first run.

**Turnover cases** (`budget.py`, 52 weekly rebalances):
- **Base**: 1.83× capital per rebalance (1.6 + 0.13 + 0.10), **95.2× a year**.
- **Alternative A**: signal rotation of 20% of the gross book, both ways, 0.2 × 2 × 2 = 0.8, plus 0.23 = 1.03× per rebalance, 53.6× a year.
- **Alternative B**: signal rotation of 10% of the gross book, both ways, 0.1 × 2 × 2 = 0.4, plus 0.23 = 0.63× per rebalance, 32.8× a year.

**Costs**: 10 bp one way central, 5 bp favourable, 20 bp stress; 10 and 20 bp to confirm ([[Cost Assumptions]] lists only top names).

**Two thresholds, both on gross Sharpe at 20% volatility.**
- **Break-even** = yearly cost / volatility: the gross Sharpe at which the net Sharpe is zero.
- **House budget** = 2 × yearly cost / volatility, printed by `budget.py`. This is deliberate: `reference/method.md` of the pass-one skill requires costs to take **less than half the expected edge**, so the gross Sharpe must be at least twice the break-even. A strategy just above break-even nets almost nothing and has no margin for a cost estimate that is wrong.

| Turnover | Cost | Yearly cost (`budget.py`) | Break-even Sharpe | House budget (`budget.py`) |
| --- | --- | --- | --- | --- |
| **95.2× (base)** | 5 bp | 4.76% | 0.24 | 0.48 |
| **95.2× (base)** | **10 bp (central)** | **9.52%** | **0.48** | **0.95** |
| **95.2× (base)** | 20 bp | 19.03% | 0.95 | 1.90 |
| 53.6× | 5 bp | 2.68% | 0.13 | 0.27 |
| 53.6× | 10 bp | 5.36% | 0.27 | 0.54 |
| 53.6× | 20 bp | 10.71% | 0.54 | 1.07 |
| 32.8× | 5 bp | 1.64% | 0.08 | 0.16 |
| 32.8× | 10 bp | 3.28% | 0.16 | 0.33 |
| 32.8× | 20 bp | 6.55% | 0.33 | 0.66 |

Break-even is half the `budget.py` figure (cost / volatility), rounded to two decimals.

**Gate of 1.11 #1**: gross Sharpe on the train period at least 0.56 (luck line, 4 tries over 3.5 years, `budget.py`) plus cost / volatility. On the base turnover: 0.80 at 5 bp, **1.04 at 10 bp**, 1.51 at 20 bp. The measured turnover replaces the estimate once known.

**What this means.** In the central case, the house budget asks for a gross Sharpe of 0.95, above every carry Sharpe in Koijen except puts (1.80) and the diversified GCF (1.10) [source: Koijen 2013, Table II A]. If the measured turnover makes 1.11 #1 fail, the strategy is killed: a slower signal or a wider band decided after that result would be a new try on seen data, and is not planned.

**Capacity**: limited by the short leg, which sits in the most speculative and thinnest names of the top 30. Realistic for a small account, untested above.

## 1.8 Instrument traps

- **Funding**: here it is the edge, not the trap. Timing matters: funding is paid to whoever holds the position at the funding time; the signal uses only prints before the rebalance, the P&L only prints after it.
- **Funding interval**: some Binance symbols may have moved from 8 hours to other intervals. [hypothesis, to check in the data] Annualise per actual interval, never assume 3 prints a day.
- **Costs**: the short leg sits in the tail of the universe, where the 5 bp of [[Cost Assumptions]] is too low: central case 10 bp, stress 20 bp, both to confirm.
- **Survivorship and look-ahead**: membership from volume known at the date; delisted perps kept until their last price, with the settlement price as exit.
- **Tickers and multipliers**: relisted tokens under an old ticker; contracts quoted per 1000 units (1000SHIB type): funding and returns per unit must match.
- **Margin**: isolated margin, allotted pro rata to notional, so the leverage per position equals the gross book over capital (about 2×, at most 3×). Liquidation is simulated on daily highs for shorts and daily lows for longs ([[Instrument Traps]]): margin is re-allotted at every rebalance, band or not, and never topped up in between (1.5b); a position liquidates when the move against it reaches about 1 / leverage minus the maintenance margin; the loss is the maintenance margin plus 10 bp (cost_bp) on the liquidated notional (1.5b), and the position stays closed until the next rebalance. At 3× a +32% squeeze is enough, so the rule can fire.

## 1.9 Variants (written before the test)

Each variant changes one brick and counts as a try. Variants are read on the validation period, against the prediction they test.

| # | Brick | Change | Why | Expected effect |
| --- | --- | --- | --- | --- |
| V1 | Portfolio | BTC-beta neutral: long leg scaled so the ex-ante beta to BTC, on past 60 days, is zero, then target and cap applied again (1.5b) | Tests P4: is it short beta? | Sharpe similar or lower, smaller losses in rallies |
| V2 | Condition | Trade only when funding dispersion (defined in P3) is above its own past median (expanding window) | Tests P3 | Higher Sharpe, fewer weeks traded, lower turnover |
| V3 | Portfolio | Short leg only, hedged with a long BTC perp at its 60-day beta, then target and cap applied again (1.5b) | Tests the mechanism: the payer should sit in the high-funding names | Most of the funding P&L, fatter left tail |

Stress tests, not tries: costs at 5, 10 and 20 bp; turnover cases 95.2×, 53.6× and 32.8× (measured turnover replaces them after the first run); universe of 20, 30 and 50; listing age 60, 90, 180 days; funding window 3, 7, 30 days; band 0, 10, 20%; today's top 30 as the survivorship control.

## 1.10 Test plan

- **Sample**: 2020-07 to 2026-09, three periods fixed now.
  - **Train**: 2020-07-01 to 2023-12-31. The check (1.11 #1 and #2) runs here first.
  - **Validation**: 2024-01-01 to 2024-12-31. Variants read against their predictions; revisions decided here count as tries.
  - **Test**: 2025-01-01 to 2026-09-30. Looked at once, at the very end.
- **Order**: the check on the train period first, base version only, at 10 bp: gross Sharpe at least 0.56 plus cost / volatility, and funding at least half of the gross P&L. Nothing else runs if either fails.
- **Diagnostics required**:
  - P&L split into price, funding and costs, by leg and by year (P1).
  - Gross Sharpe on train plus validation without 2022 (P5).
  - Skewness, worst 10 weeks and what BTC and the alt index did in them (P2).
  - Funding plus price by tercile of past funding dispersion (P3).
  - Regression of weekly gross returns on BTC, the alt-minus-BTC factor, the volatility factor, the 7-day return factor and the price-only Crypto XS Momentum returns: intercept and its t-stat (P4).
  - Liquidations: count, loss, by leg (1.8).
  - Contribution by name, with the concentration flag (top 5 above 60%), turnover, breakeven cost.

## 1.11 Kill criterion (backtest)

1. **Gross Sharpe on the train period**, base version, below 0.56 plus cost / volatility (1.04 at 95.2× and 10 bp; with the measured turnover once known). Kill before anything else.
2. **Funding below half of the gross P&L** (price plus funding) on the train period, base version: the P&L is price, not carry. Kill before anything else.
3. Intercept t-stat below 2, weekly gross returns on train plus validation, after regressing on BTC, the alt-minus-BTC factor, the volatility factor, the 7-day return factor and the price-only Crypto XS Momentum returns: it is beta, alts, volatility or momentum, not carry.
4. Gross Sharpe on train plus validation without 2022, base version, below 0.56 plus cost / volatility (1.04 at 95.2× and 10 bp; with the measured turnover once known): the result is one regime (P5).
5. Test period: the three-zone rule.
