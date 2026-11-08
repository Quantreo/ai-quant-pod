## Data check

**Verdict: ready with reserves** · 2026-10-25 · data before 2018-01-01 only for the looks; the test (2021-01-01) was not read. Cards reused: [[ETF daily]], [[T-bill rate]].

**Load**: `load("etf_daily", test_start="2021-01-01")`, drop SHY; cash: `pd.read_parquet("data/rates/tbill.parquet")` (not in `lab.data` yet).

| Need (Pass 1) | Dataset | Field | Period | Status |
| --- | --- | --- | --- | --- |
| 22 ETF returns | etf_daily | adj_close | 2005-01 to 2017-12 | ok |
| Cash | tbill (TB3MS) | rate, % a year, monthly mean | 2004-01 to 2026-09, 0 NaN | ok with issue 1 |
| Sign of 12m excess return | derived | adj_close, cash | from 2006-01 | ok |
| Cost tiers 2 bp / 5 bp | Cost Assumptions | per ETF | | ok (estimate, Lucas to confirm) |
| Volume (capacity) | etf_daily | volume | | ok: thinnest median dollar volume FXY 18m, DBA 20m, UUP 30m a day |
| Borrow 0.5%, Reg T cap 2 | none | | | hypothesis and rule, no data to check |

**Universe** (12 months of rows, month end, SHY out): 2006-01: 13 ETFs; 2007-01: 15; 2008-01: 19; from 2009-01: 22.

| # | Issue | Evidence | Effect on the test | Instruction to the Developer |
| --- | --- | --- | --- | --- |
| 1 | Cash is a monthly mean of a discount-basis rate, stamped on day 1 | tbill.parquet: 168 months to 2017-12, 0 NaN; rate 0.01 to 5.03 | The mean of month m is known only after month m. Discount rate sits a few % (relative) under the bond-equivalent yield: negligible at ~0%, about 10 bp at 5% in 2006-07 | Cash return of a month = rate/12 of that month; at a month-end signal use months up to m-1 (the window shifts by one month for cash only). Say it in Build. Not SHY as cash |
| 2 | Book is small and tilted early | 13 ETFs in 2006, equity, bonds, VNQ and GLD only; no currency before 2006-12, no oil/silver/agri before 2007-04; four classes only from 2008-04 | Equal-risk basket and the one-sign twin are built on a different mix each year; 2006-07 is a bonds and equity book. 8% target at 13 names may hit the cap more | Rebuild the control baskets on the names alive at each month end, not on the final 22. |
| 3 | Survivor list | The 23 are 2026 picks, all alive, large and liquid today. No dead or delisted ETF in the file by construction (not searched: no download) | Winners of the 2005-2026 period (QQQ, GLD, IWM, VNQ) are in; collapsed funds that a trend book would have shorted are not. Both the long and short sides are tilted, direction not signed. The alpha over a same-universe always-long control cancels most of the long tilt, not the missing short winners | Keep the 13 present from 2005 stress already in Pass 1. Add the same stress on the 9 launched after 2005. State in the result that the trend alpha is conditional on this list |
| 4 | Commodity ETFs and roll | USO, GLD, SLV: adj_close = close (ratio 1.0 all years, no distributions); DBC, DBA: ratio 0.79-0.83 at start, 0.85-0.86 at 2026, so yearly distributions. No jump above 30% in close (no split artefacts before 2018) | Roll is inside the ETF price (contango paid in NAV), so the signal sees the investor's return, not spot. USO changed what it holds over time [memory, not checked], so its roll cost is not stable | Treat USO as a product, not as oil. Report USO, DBC, DBA separately in the by-ETF table. Do not add a roll term |
| 5 | Open, high, low not adjusted; EWJ opens stale | Card: EWJ open = close on 219 days of 2005-2017 | None for close-to-close | Trade at close, adj_close only (matches Pass 1) |

**Harmless warnings**: UUP 1 zero-volume bar (2007-03-15, launch week). 10%+ moves before 2018 (EEM, FXI, VNQ, SLV, USO) are Sept-Dec 2008, real. Days missing vs SPY: 0. adj_close changes at each re-download (dividend adjusted as of download). Borrow 0.5% and Reg T cap 2 are not checkable with data.

**Proposed checks.md line**: "Survivor list: an ETF file picked today has no dead funds; compare a trend book on the names alive at launch, and build control baskets point in time."
