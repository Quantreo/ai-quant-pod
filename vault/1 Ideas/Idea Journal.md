---
type: journal
---

# Idea Journal

> **What this is** : one entry per idea, the day you meet it. Not a to-do list: a queue, newest first.
> **Open it** : at the end of every reading slot (add an entry), at the start of every derivation slot (pick an entry that is a week old and still looks good).
> **Rule** : write the mechanism in one sentence, or do not write the idea at all. Here the sentence is a filter, not an analysis: the full answer (when it works, when it breaks, what kills it) belongs to Pass 1 of the strategy sheet.

**Entry format** : date · title / mechanism in one sentence / `family` · source · **status** · revisit date · sheet
**Status** : new → reading → derived → sheet → dropped, or **parked** (no payer found yet, with a revisit date)

The entries marked **new** or **reading** are open: nobody has built them. Pick one, and it is yours.

### 2026-11 · G10 carry with a volatility switch to the funding legs
Carry pays a premium for carrying crash risk, and the crash comes when FX volatility spikes; stepping out (or flipping) in the top-volatility state keeps the premium and turns the unwind into a gain. [source: Clarida 2009, note] and [source: Brunnermeier 2008, Table 2]
- **Operator**: condition
- **What's new**: Clarida 2009 documents that baskets lose in the top volatility quartile and stops there → trade G10 carry only when realized FX vol is not in its top state, and in that state hold the funding legs (long JPY, CHF vs USD) instead. One brick changed: the state rule.
- **Bricks**: [[Market state split]] applied to [[Carry]]
- **Evidence**: G10 carry baskets earn 2.38% to 5.66% a year 1990-2009, and in the top realized-vol quartile 1v1 loses -9.75% (Clarida 2009, note; gross, pre-2009 sample). Carry loses when VIX rises; Sharpe 0.784 for 3v3 quarterly (Brunnermeier 2008, Table 2, 8 currencies, gross). Carry crisis-window market beta reaches 1.22 (Lustig 2008, in-sample, not out of sample).
- **First kill**: crisis-window market beta of the switched strategy vs SPY (Crisis-window market beta card): if it stays above 0.3 in 2008, 2020, 2025, the idea is dead. Then the net Sharpe with the vol rule against plain carry on 2008-2026 train.
- **Data**: fx_daily (9 USD pairs from 2008) and rates_monthly 3-month rates; have it. Rate differential is an interbank proxy, not forward points. Assumption: Defaults.md costs, 2x stress, signal lag one month.
`carry` · [[2009 - Clarida Davis Pedersen - Currency Carry Trade Regimes Beyond the Fama Regression]] · **new** · revisit 2027-05

### 2026-11 · FX value: five-year real exchange rate, G10 vs USD
Currencies that became cheap in real terms earn a premium for being held when carry crashes; value is a different bet from carry and is negatively related to it. [source: Menkhoff 2016, note] and [source: Asness 2013, note]
- **Operator**: replicate
- **What's new**: Menkhoff 2016 sorts 22 currencies on the 5-year real rate change → the same sort on the 9 G10 pairs vs USD with desk CPI and FX spot, dollar-neutral, monthly, no purge of fundamentals (one brick, the plain signal).
- **Bricks**: [[Cross-sectional value signal]] applied to [[Dollar-neutral and dollar leg split]]
- **Evidence**: Sharpe 0.44 to 0.51, 1976-2014, gross; the purged version reaches 0.79-0.91 but a two-quarter lag cuts it to 0.39-0.61; standard drawdown about -25% in 1990-91 (Menkhoff 2016, note). Value and momentum correlate about -0.5 within a market (Asness 2013, note); currency value t-stats 1.8 to 2.6.
- **First kill**: rank IC and Sharpe with the CPI lag of one quarter on 2008-2026 train. Several CPI series are flagged stale in cpi_quality_report: drop them and see if fewer than 7 pairs remain. Then the equity beta in stress windows.
- **Data**: cpi.parquet, fx_daily; have it. Quarterly AUD and NZD CPI, no vintages, so own lag. Assumption: Defaults.md.
`value` · [[2016 - Menkhoff Sarno Schmeling et al - Currency Value]] · **new** · revisit 2027-05

### 2026-11 · Treasury curve carry: duration-neutral roll-down across maturities
Maturities with high yield per unit of duration (steep part of the curve) earn their carry, and a duration-neutral long-short keeps rate level and equity beta out. [source: Koijen 2013, note]
- **Operator**: transpose
- **What's new**: Koijen 2013 builds bond carry across countries and slopes → here across the US maturity ladder only (1Y to 30Y), long steepest roll-down, short flattest, DV01-neutral. It also differs from Bond Trend Demeaned (a signal on past returns, killed): this one uses the curve, not past return.
- **Bricks**: [[Carry signal]] applied to [[Dollar-neutral and dollar leg split]]
- **Evidence**: bond carry strategies have Sharpe below passive long (level 0.52 vs 0.74; slope 0.66 vs 0.71) and all carry strategies lose in global carry drawdowns (Koijen 2013, note, gross). Bond value and momentum not significant (Asness 2013, note). So the prior is weak; it enters for the payoff profile, not the evidence.
- **First kill**: the Sharpe of the long-short against zero and its beta to IEF-TLT and SPY, on monthly ladder returns from ust_curve (average-of-month yields smooth the series: treat the Sharpe as upward biased and say so). If net Sharpe is under 0.3 or the equity beta is not under 0.1, dead. Expect the likely result is dead.
- **Data**: ust_curve.parquet (1Y to 30Y, 2004-2026, monthly average); have it. Returns built from yields by a duration approximation, not tradable ETFs for all maturities (SHY, IEF, TLT only). Assumption: Defaults.md.
`carry` · [[2013 - Koijen Moskowitz Pedersen et al - Carry]] · **new** · revisit 2027-05

### 2026-11 · Commodity cross-sectional momentum on liquid ETFs
Commodities that rose over 12 months keep rising because inventories adjust slowly and speculators extrapolate; the long-short is dollar-neutral and its pay is unrelated to equities. [source: Gorton 2007, note]
- **Operator**: transpose
- **What's new**: Gorton 2007 sorts 31 futures into halves → sort the liquid commodity ETFs (GLD, DBC, USO, GSG and sector ETFs from the 34 in the desk set), long top third, short bottom third. ETFs bring roll cost and contango the futures sort did not.
- **Bricks**: [[Cross-sectional momentum]] applied to [[Always-long benchmark comparison]]
- **Evidence**: high 12-month momentum beats low by 13.36% a year, t = 4.93, 1969-2006, gross, no costs (Gorton 2007, note); Zaremba 2016: 0.74% a month, t = 2.79, 1987-2013, gross; Lempérière 2014: commodity t falls from 4.5 long-only to 3.1 de-biased.
- **First kill**: net Sharpe at the ETF cost and 25 bp short borrow, and loser-leg ETF decay (USO-type contango). If the short leg's return is only roll decay, dead. Then beta to SPY in 2008, 2020, 2025.
- **Data**: etf_daily (34 commodity ETFs, some short-lived, survivorship must be checked in quality_report); have it. Assumption: Defaults.md.
`trend` · [[2007 - Gorton Hayashi Rouwenhorst - The Fundamentals of Commodity Futures Returns]] · **new** · revisit 2027-05

### 2026-11 · Multi-asset ETFs: 12-month time-series trend
Investors under-react to news and chase it later, so an asset's own 12-month excess return predicts its next month. [source: Moskowitz 2012, p. 245, 248-249]
- **Operator**: transpose
- **What's new**: Moskowitz 2012 traded 58 futures → the same rule on 22 liquid ETFs across four classes, with ETF costs and borrow.
- **Bricks**: [[Time-series momentum signal]] applied to [[Always-long benchmark comparison]]
- **Evidence**: 12/1 is the best cell, t 6.61 (Moskowitz 2012, Table 2A); alpha over always-long significant for only 26% of contracts (p. 236). Flat since 2011 (Lempérière 2014, Fig. 6).
- **First kill**: net Sharpe on train under the t 2 bar after costs and borrow.
- **Data**: ETF daily and T-bill from the repo; have it.
`trend` · [[2012 - Moskowitz Ooi Pedersen - Time Series Momentum]] · **sheet** · [[ETF TSMOM 12-Month]]

### 2026-11 · FX currency momentum with a no-trade band
Currencies under-react to news and then over-react, with limits to arbitrage; the band cuts the spread cost that eats the edge. [source: Menkhoff 2011, p. 27-29]
- **Operator**: swap
- **What's new**: Menkhoff 2011 rebalances fully each month (turnover 74% a month) → replace that brick with the no-trade band, which trades only when the signal moves enough.
- **Bricks**: [[No-trade band]] applied to [[Cross-sectional momentum]]
- **Evidence**: 1-month momentum earns 9.46% a year gross and 3.92% net of full quoted spreads (Menkhoff 2011, Tables 8, 9; the authors say quoted spreads are too high). On the 15 developed currencies only 0.79% net, t = 0.44 (Tables A.12, A.13). Gross is near zero after 2007 (≈ Fig. 7).
- **First kill**: yearly cost from turnover and spread, before any signal test. If the net is still near zero after the band, or the post-2007 gross is flat, the idea is dead.
- **Data**: FX spot and forward or minute bid/ask from Dukascopy; have it.
`trend` · [[2011 - Menkhoff Sarno Schmeling Schrimpf - Currency Momentum Strategies]] · **parked** · revisit 2027-05 · Economist 2026-11-06: the band fixes a cost that does not bind on our FX data (9 G10 pairs vs USD from 2008: full monthly rebalance costs about 0.1% a year, budget.py), and the payer the source names lives in risky minor currencies we do not have (developed net 0.79%, t 0.44). Plain G10 momentum has 11% gate power at the source's developed edge. Reopen when EM spot plus rates data is on the machine.

### 2026-11 · Bond trend on demeaned returns
Persistence in bond returns pays only if it exceeds the sample's drift, and bond trend profit is mostly the mean return. [source: Moskowitz 2012, Table 5B]
- **Operator**: fix a weakness
- **What's new**: Moskowitz 2012 traded the sign of the past return on raw bond returns → trade the sign of trend on returns demeaned with an ex-ante (expanding) mean.
- **Bricks**: [[Time-series momentum signal]] applied to [[Profit decomposition into persistence and mean return]]
- **Evidence**: in bonds, mean squared return is 0.70 of 1.05, about two thirds (computed in the note from Table 5B; units of the table not stated). Alpha over always-long is significant for only 26% of contracts (Moskowitz 2012).
- **First kill**: demeaned bond trend against always-long on bond ETFs. If the Sharpe edge over always-long disappears, bond trend was only the drift.
- **Data**: bond ETF prices from `yfinance`; have it. Bond futures are paid.
`trend` · [[2012 - Moskowitz Ooi Pedersen - Time Series Momentum]] · **sheet** · [[Bond Trend Demeaned]]

### 2026-11 · Crypto cross-sectional momentum, panic-state filter
After bear markets the losers carry a high, convex market beta, so winner-minus-loser behaves like a short call on the market; in crypto, losers being the high-beta coins is a [hypothesis]. [source: Daniel Moskowitz 2016, p. 19, 40]
- **Operator**: transpose
- **What's new**: Daniel Moskowitz 2016 tested equities and FX → stand aside from crypto momentum after a negative 24-month market return plus high market variance.
- **Bricks**: [[Market state filter]] applied to [[Cross-sectional momentum]]
- **Evidence**: panic-state coefficient negative and significant in EU, JP, UK, US, GE equities (Table 8 D). Outside equities and FX the coefficients are mostly insignificant (Daniel Moskowitz 2016).
- **First kill**: market state split of crypto momentum on BTC's 24-month return and variance. Crypto history is thin before 2019, so few observations.
- **Data**: Binance/ccxt OHLCV; have it.
`trend` · [[2016 - Daniel Moskowitz - Momentum crashes]] · **dropped** · user's reason: none given · revisit 2027-11

### 2026-11 · Crypto trend factor only in low-volatility weeks
Trend signals are noisier when volatility is high, so the factor should pay less then; this is a [hypothesis], the paper gives no mechanism for the split.
- **Operator**: condition
- **What's new**: Fieberg 2025 trades the 28-indicator factor every week → trade it only in low-volatility weeks.
- **Bricks**: [[Technical indicator combination signal]] applied to [[Volatility targeting]]
- **Evidence**: 5.46% a week in low-volatility weeks against 2.27% in high ones, gross (Fieberg 2025; the note gives no table). Weekly turnover 68%; net 2.35% to 2.90% a week (Table 8).
- **First kill**: cost. Check that the low-volatility split holds net of 68% weekly turnover and that the volatility threshold is not fitted.
- **Data**: Binance/ccxt OHLCV; have it.
`trend` · [[2025 - Fieberg Liedtke Poddig et al - A Trend Factor for the Cross Section of Cryptocurrency Returns]] · **dropped** · user's reason: none given · revisit 2027-11

### 2026-11 · Long-only low-MAX crypto basket
Investors pay up for coins with extreme recent daily gains (lottery demand), so high-MAX coins are overpriced and low-MAX coins should hold up better; the paper borrows this from equity MAX work and does not test it directly. [source: Grobys 2021, p. 3, 11]
- **Operator**: test a claim
- **What's new**: Grobys 2021 ran long low-MAX / short high-MAX on 20 coins and suggested a long-only version without testing it (p. 11); this idea tests the long-only leg against an equal-weight basket of the same coins, on a point-in-time universe, net of costs and funding.
- **Bricks**: [[Maximum daily return signal]] applied to [[Minimum price and size filter]]
- **Evidence**: low-MAX quintile earns 1.33% a week and high-MAX -0.22%, gross (Grobys 2021, Table 1). The H-L spread is not significant with standard t-statistics (t = -1.57, Table A8), quintiles hold four coins each, and the cumulative H-L falls steadily from mid-2017 (Fig. 1). Ozdamar 2021 finds the opposite sign, read as continuation (p. 11). Long leg against a benchmark: not reported.
- **First kill**: low-MAX minus the equal-weight basket of the same coins, net of costs. Estimate the yearly cost from weekly turnover and spread first. If the edge sits in the short leg, or fades after 2017, the idea is dead.
- **Data**: Binance/ccxt OHLCV and klines volume for a point-in-time universe; have it.
`low-vol` · [[2021 - Grobys Junttila - Speculation and lottery-like demand in cryptocurrency markets]] · **sheet** · [[Crypto Low-MAX Long Leg]]
