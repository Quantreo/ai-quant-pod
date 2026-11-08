---
type: data
dataset: etf_daily
---

# ETF daily

**Source**: Yahoo Finance. **Build**: `poetry run python data/get_etf_daily.py` (about 2 minutes). **Load**: `lab.data.load("etf_daily", test_start=...)`. Quality report: `data/etf/quality_report.md`.

## Files (data/etf/)

| File | Content |
| --- | --- |
| etf_daily.parquet | One row per ETF and trading day, from its first day (point in time): date, symbol, asset_class, open, high, low, close, adj_close, volume. |
| etf_liquidity.csv | Median daily dollar volume (close x volume, USD million) per ETF and year: input for the cost tiers. |
| quality_report.md | Per ETF: class, first and last day, median dollar volume 2008 / 2015 / 2025, missing days, moves above 10%. Plus the failed tickers. |

## Coverage

2005-01-03 to 2026-09-30. About 220 tickers probed, a little over 200 kept. Classes: equity (the core indexes), sector, size_style, factor, country, bonds (every maturity: SHV, SHY, IEI, IEF, TLH, TLT, plus TIP, credit, munis, emerging debt, BWX...), commodities, real_estate, currency. About 100 ETFs start by 2005, about 150 by 2008, the others launch 2008 to 2018.

**Survivors only**: the tickers that fail are the closed or delisted ones (Russia ETFs, DB single metals, iPath ETNs, Chinese yuan, Brazil real). Yahoo does not serve dead ETFs, so the survivor bias is not removed: say it in any Pass 1 that picks ETFs by later performance or size.

## Conventions and known issues

- `adj_close` is dividend adjusted as of the download date; use it close to close. `open`, `high`, `low`, `close` are not adjusted: no returns across a dividend from them.
- Calendar is the NYSE one. Closures such as 2007-01-02 and 2012-10-29/30 are absent for all names; build windows on trading-day positions, never calendar offsets.
- An ETF has no row before its first trading day: the universe is point in time.
- Thin ETFs have zero-volume and flat bars (CPER, SIZE, LQDH); CPER has bad prints. EWJ has stale opens (open = close) on about 200 days of 2005-2017: irrelevant close to close, an issue for any open-based signal.
- 2008 has many 10%+ days in EEM, FXI, EFA, EWJ (real, Sept and Oct 2008).
- Asset class is the group in the script, not Yahoo's category (a ticker listed twice keeps its first group).
- Costs: tiers by liquidity in `vault/Toolbox/Cost Assumptions.md`.
