---
type: reference
updated: 2026-10-25
---

# Cost Assumptions

> **What this is** : the cost per unit traded the desk assumes by market, before any test. The Economist uses it for the cost budget of Pass 1; the Developer for the first backtest.
> **Rule** : a market not in this table gets an assumption written in the sheet and marked "to confirm". A human adds it here once checked.

| Market | Cost, one way | Source | Note |
| --- | --- | --- | --- |
| Crypto perps, Binance USDT, top names | 5 bp | Crypto XS Momentum sheet | The tail of the universe costs more |
| FX majors, spot | real bid/ask from minute data | FOMC Drift sheet | Spreads widen around announcements; a flat cost understates AUD and NZD |
| Futures | to fill | | |
| ETFs, very liquid (SPY, QQQ, IWM, EFA, EEM, TLT, IEF, SHY, LQD, HYG, GLD) | 2 bp | confirmed by Lucas 2026-10-25 | Half spread about 0.5 to 1 bp plus commission and slippage at the close; trades at the close (auction) |
| ETFs, others (EWJ, VGK, FXI, TIP, VNQ, SLV, DBC, USO, DBA, UUP, FXE, FXY) | 5 bp | confirmed by Lucas 2026-10-25 | Wider spreads; DBA, FXY and UUP are the thinnest. Stress at 2x |

## ETF financing

| Item | Cost | Source | Note |
| --- | --- | --- | --- |
| Short borrow, liquid ETFs | 25 bp a year | confirmed by Lucas (Desk log 2026-10-25) | Hard-to-borrow names cost more: none in the 23 |
| Leverage above 1x | T-bill + 50 bp a year | desk estimate, to confirm by Lucas | Stress at T-bill + 150 bp (a retail broker's rate) |

## ETF extended (203 ETFs): cost tiers by era

Proposed by the Data seat 2026-10-25; T1 to T4 confirmed by Lucas 2026-10-25. The 23-ETF lines above keep their own costs. Tier of an ETF at date t = median daily dollar volume of the previous calendar year (`data/etf/etf_extended_liquidity.csv`, USD million), so the tier is point in time and an ETF moves between tiers as it grows. No volume yet (launch year) = not tradable.

| Tier | Median $ volume, prior year | Cost, one way | Source | Note |
| --- | --- | --- | --- | --- |
| T1 | 500 m or more | 2 bp | confirmed by Lucas 2026-10-25 | Same as the "very liquid" line |
| T2 | 50 to 500 m | 4 bp | confirmed by Lucas 2026-10-25 | |
| T3 | 10 to 50 m | 8 bp | confirmed by Lucas 2026-10-25 | |
| T4 | 2 to 10 m | 15 bp | confirmed by Lucas 2026-10-25 | Position capped at 1% of daily volume (rule below) |
| T5 | under 2 m | excluded from the universe, no cost priced | confirmed by Lucas 2026-10-25 | No 30 bp cost: a T5 ETF is never traded. Many zero-volume days (CPER, SIZE, LQDH) |

**Rules confirmed by Lucas 2026-10-25 for every ETF strategy:**
- Position capped at 1% of daily volume (as given; read it on the previous calendar year's median daily dollar volume of the tier table, to stay point in time, unless Lucas says otherwise).
- T5 is excluded from the universe, with no cost at 30 bp.
- Every ETF strategy runs a stress at 2x all costs.

Number of the 203 ETFs per tier, by volume year (from the csv; 155 have a volume in 2008):

| Volume year | T1 | T2 | T3 | T4 | T5 | No volume |
| --- | --- | --- | --- | --- | --- | --- |
| 2008 | 9 | 41 | 40 | 48 | 17 | 48 |
| 2015 | 13 | 52 | 62 | 44 | 31 | 1 |
| 2025 | 32 | 78 | 40 | 30 | 23 | 0 |

Median dollar volume of the whole set: 12.7 m (2008), 24.8 m (2015), 58.9 m (2025). A flat 2 bp or 5 bp on the full set in 2008 would understate costs for about half of it. Stress at 2x. The bp figures are estimates, not measured spreads.
