# Crypto Thin Losers · Pass 1

**Verdict: Go.** Payer named as a hypothesis: sellers of thin coins after a fall, paying whoever absorbs them. The library shows only the gross in-sample pattern (Begušić 2019). Precondition (8 names a cell) passed at the Data check. Rivals gated: a stale-beta bounce (Liquidation Reversal kill) by #1 and #3, a depth-of-fall reversal by the depth control in #1 (v2).

---

## 1.1 Mechanism

**Type**: risk premium (liquidity provision).

**Who pays.** Sellers of a thin coin after a fall (retail, unlock recipients, market makers) meet few buyers and push it below value; the holder for two weeks carries the risk of further falls and is paid by the recovery [hypothesis; the authors name no payer]. On perps the payer is reached through the mark, an index of spot venues [hypothesis].

**What the sources show.** Illiquid minus liquid: losers 0.52% a day, significant, IR 1.05; winners -0.07%, not significant [source: Begušić 2019, Table 1]. Gross, in-sample, spot coins, 2015-2019; spread inconsistent with cell means (0.76); 3x3 cells of unstated sort order (p. 3), so not the base's sequential cells. Authors expect bid-ask costs to hurt the illiquid leg [source: Begušić 2019, p. 5].

**Why it is not arbitraged away.** Tiny capacity; dying coins, concentrated in crashes [hypothesis].

**What it could secretly be.** (a) Market beta: thin names have high, stale betas (Liquidation Reversal kill). (b) Size: thin beats thick whatever the past return. (c) Funding: thin losers may pay longs. (d) Depth-of-fall reversal: Amihud contains abs R. (e) Survivorship: dead names kept.

**Predictions.**
- **P1** (key) Positive intercept of the base's gross daily return (price plus funding, before costs) on the equal-weight universe return today plus 5 lags summed [literature, not in library: Dimson 1979] and on the depth-of-fall spread (1.5b): thinness pays beyond the depth of the fall. Failure: kill (#1).
- **P2** The premium sits among losers: the same spread on winners has a lower intercept. Beta and size predict both rows alike, so this separates them. Failure: kill (#3).
- **P3** Pays its costs: net Sharpe on train at least the luck line. Failure: kill (#2).
- **P4** Price is at least half of gross P&L, else it is funding carry. Failure: kill (#4).
- **P5** Front-loaded (event days 1 to 7 above 8 to 14) and same sign with a volume-only sort (V1). Read only: depth of fall is gated in #1, this only says which brick carries it.

## 1.2 Sources and crowding

[[2019 - Begušić Kostanjčar - Momentum and liquidity in cryptocurrencies]]; bricks [[Liquidity-conditioned momentum]], [[Conditional double sort]], [[Minimum price and size filter]], [[Long-short portfolio weighting]], [[Market beta hedge]], [[Break-even transaction cost]]. Amihud [literature, not in library: Amihud 2002]. Desk: Crypto Daily Reversal ranks 11 to 20 beat 1 to 10 on train (seen). Crowding low: arXiv preprint, no capacity.

## 1.3 Expected behaviour

Works after selling waves in recovering alt markets; suffers in long alt bears (2022) and delistings. Left tail on the long leg.

## 1.4 Universe

Binance USDT perps, underlying COIN, stablecoins out, listed at least 180 days (source 26 weeks, p. 2), point-in-time, dead names kept and closed at last mark. No volume floor: the listing is the tradability floor; thin-side cost handled in 1.7. About 21 eligible names in 2020, 79 to 155 in 2021 to 2023: train starts 2021.

## 1.5 Base version, brick by brick

| Brick | Choice | Why | Basis | Card |
| --- | --- | --- | --- | --- |
| Return signal | 14-day return, no skip | Source | source (Eq. 1) | [[Liquidity-conditioned momentum]] |
| Liquidity signal | 14-day Amihud, abs return over USDT quote volume | Source | source (Eq. 2) | [[Liquidity-conditioned momentum]] |
| Sort | Momentum 30/70, then Amihud 30/70 within each momentum group | Breakpoints from source; sequential balances cells | source; free (order) | [[Conditional double sort]] |
| Book | Long illiquid losers, short liquid losers, equal weight, dollar-neutral | Payer in thin losers; short removes the loser-wide move | mechanism; source | [[Long-short portfolio weighting]] |
| Holding | 14 days in 14 daily tranches | Source horizon; no start-day choice | source; convention | none |
| Hedge | BTC perp at minus ex-ante beta, 60 days, today plus 5 lags summed | Stale prices of thin names | mechanism (rival a) | [[Market beta hedge]] |
| Sizing | Vol target 20%, 60-day covariance, gross cap 3x | Desk standard; cap bounds leverage | scale; risk | none |
| Execution | Filled at daily close 00:00 UTC | 14-day horizon | convention | none |
| Margin | Isolated, leverage = gross, liquidation on daily mark highs and lows | [[Instrument Traps]] | convention | none |
| P&L | Price, funding, costs, liquidations, by leg and year | House default | convention | none |

## 1.5b Free parameters

| Parameter | Value | Why | Tested as |
| --- | --- | --- | --- |
| Sort order | Sequential | Balanced cells | Stress: independent |
| Beta window | 60 days | About 4 holds | Stress: 30, 120 |
| Beta lags | 5 | A week of staleness | Stress: 10 |
| Hedge | BTC perp | Cheapest | Stress: equal-weight top 20 |
| Fill | Day d close | Convention | Stress: d+1 close |
| Holding | 14 days | Source | Variant V2 |
| Vol target, cap | 20%, 3x | Scale, risk | Follows |
| Depth-of-fall spread (#1 control) | Within losers, lowest 30% minus highest 30% on 14-day return, built like the base | Source's 30/70 | Follows |
| Cost tier | Thin leg 20 bp [hypothesis; thin cell 6 to 30M USDT a day, Data check], liquid leg and hedge 5 bp | Cost Assumptions: top names only | Stress: thin 40 bp |
| Minimum cell | Skip a formation (tranche in cash) if a leg is empty or under 4 losers ranked | Free (as coded) | Stress: under 5 a leg |
| Amihud gaps, ties | 14 days with volume required; ties inclusive | Convention | Follows |
| Hedge timing | Reset daily; beta on the book's past returns at current weights | Daily tranches | Follows |
| Dead or liquidated name | Last mark, or margin plus fees lost; cash until the next rebalance | [[Instrument Traps]] | Follows |

## 1.6 Horizon, trades and statistical power

About 78 non-overlapping 14-day periods on train. Tries 3 (base, V1, V2): luck line 0.49; a t of 2 needs 0.23 standard deviations per period, about 1.17 Sharpe a year (`budget.py`). Gates #1 and #3 use a Newey-West t, 14 lags (the tranche overlap), so power is on the same 78-period basis: a true Sharpe of 1.0 passes about 39%, 0.5 about 13%, zero about 2.3% (normal, t mean = Sharpe x √3). Gate #2 (net Sharpe standard error about 1/√3): true net 1.0 passes about 81%, 0.5 about 51%, zero about 20%. Gate #4, a ratio: no power stated. Joint pass at most #1's.

**Data already seen**: all periods used by five crypto sheets, and this base's train gate run (v1). True out-of-sample starts with paper trading.

## 1.7 Cost and capacity budget

The v1 gross (1.4) rested on 20 to 40 names a leg, which was wrong (cells 7 to 13); the gates use the measured train figures (Build v1): gross 1.45, turnover 79.6x. `budget.py --turnover 79.6`: at 12.5 bp blended (tier in 1.5b) 9.95% a year, gross Sharpe needed 0.99 at 20% volatility. Funding charged as paid. Capacity a few $M gross [hypothesis]; Data check reports the thin cell's median quote volume.

## 1.8 Instrument traps

Funding (apart, P4); isolated-margin liquidation on mark lows and highs; bid/ask (tier, 40 bp stress); survivorship and membership look-ahead (point-in-time).

## 1.9 Variants (written before the test)

| # | Brick | Change | Why | Expected effect |
| --- | --- | --- | --- | --- |
| V1 | Liquidity signal | 14-day median quote volume | Amihud mixes in depth of fall (P5, rival d) | Same sign, smaller; near zero means depth-of-fall reversal |
| V2 | Holding | 7 days, 7 tranches | Price pressure reverts fast (P5) | Higher gross per day, double turnover, net about equal |

A variant replaces the base only if P5 comes out as written.

## 1.10 Test plan

- **Train** 2021-01-01 to 2023-12-31; **Validation** 2024; **Test** 2025-01-01 to 2026-09-30, once.
- **Precondition** (Data check, not a try): both loser cells average at least 8 names per formation on train, else Park.
- **Order**: base on train, gates #1 to #4; nothing else if one fails. Then V1, V2 and stress tests on validation.
- **Diagnostics**: #1 regression (P1); lagged-market regression for the winners spread and losers minus winners (P2); P&L split by leg and year, measured turnover and gross, break-even cost (P3, P4); event-time price P&L days 1 to 7 vs 8 to 14, V1 vs base (P5); cell counts and quote volume per formation; largest single-name weight per leg and day (read only).

## 1.11 Kill criterion (backtest)

1. **Intercept Newey-West t (14 lags) below 2**, train, base, gross daily return on the equal-weight universe today plus 5 lags summed and on the depth-of-fall spread (P1). Power 39% at Sharpe 1.0, 2.3% at zero.
2. **Net Sharpe below 0.49**, train, base, measured turnover, tiered cost (1.5b), funding, liquidations (P3).
3. **Losers minus winners intercept Newey-West t below 2**, train, same regression without the depth control, winners spread built like the base (P2). Same power as #1. Train value (t 2.50, Build v1) seen before this bar: no new evidence on train.
4. **Price share of gross P&L below 0.5**, train, base (P4).
5. Test period, three zones on the test mean against the train-plus-validation mean: above half, paper at half weight; between minus half and half, paper only; below minus half with t under -1.5, kill.
