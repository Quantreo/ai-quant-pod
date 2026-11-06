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
