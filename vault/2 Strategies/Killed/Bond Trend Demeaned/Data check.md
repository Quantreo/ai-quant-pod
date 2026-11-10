## Data check

**Verdict: ready with reserves** · 2026-11-08 · data before 2022-01-01 only; test period: coverage counted, not read. Short Pass 1: only the base was checked.

**Load**: `load("etf_daily", test_start="2022-01-01")` (symbols IEI, IEF, TLH, TLT, TIP, BWX) · T-bill: `data/rates/tbill.parquet` (not in `lab.data` yet). No crypto universe.

| Need (Pass 1) | Dataset | Field | Period | Status |
| --- | --- | --- | --- | --- |
| Monthly total return | etf_daily | adj_close | 2005-01 to 2021-12 | ok (0 missing, 0 duplicates, 0 sort errors) |
| Inverse-vol sizing (60 d) | etf_daily | adj_close | same | ok, largest day move 7.5% (TLT) |
| Cost tier (liquidity) | etf_daily, etf_liquidity.csv | volume | same | ok, 0 zero-volume bars; TLH thin |
| Excess return (T-bill) | tbill | rate, USD_TB3M | 2004-01 to 2021-12 | ok, 274 months to 2026-09, not stale |
| Test period | etf_daily | all | 2022-01 to 2026-09 | coverage ok, 6 names every year |

**Universe** (36 months after first price): first price IEF, TLT, TIP 2005-01-03; IEI, TLH 2007-01-11; BWX 2007-10-11. Entries: 3 names from 2008-01, 5 from 2010-01, 6 from 2010-10. Largest gap between bars is 5 days (holiday weekends).

| # | Issue | Evidence | Effect on the test | Instruction to the Developer |
| --- | --- | --- | --- | --- |
| 1 | Few names early | 2008-01 to 2009-12: IEF, TLT, TIP only; 6 names from 2010-10 | 2008 (the stress the 36-month warm-up protects) is judged on 3 highly correlated names | Report the train result by sub-period (2008-09 / 2010-18); do not read the 2008-09 Sharpe alone |
| 2 | First price is the download cut | IEF, TLT, TIP start 2005-01-03 (real listings 2002-03, my knowledge, not in the card) | Point-in-time rule gives 2008-01 only because the panel starts 2005 | Apply the rule on the panel as loaded; do not extend the history from another source |
| 3 | T-bill timing | Monthly average, discount basis, month m not known at start of m | Small look-ahead in excess return | Use the T-bill of m-1 for the return of m; say it in the result |
| 4 | Thin ETF | TLH median volume 13,200 shares in 2008 against 345,100 (IEF) and 2,494,400 (TLT) | Cost tier may be wrong if one tier is applied to all | Take each ETF's tier from `etf_liquidity.csv` by year, not one tier |
| 5 | Not pure duration | BWX is non-US government bonds (currency risk); TIP is inflation-linked | The "two independent bets" and the P2 beta read are blurred | Label BWX and TIP in the split; no change to the rule |
| 6 | Adjustment and calendar | `adj_close` adjusted at download date; NYSE closures absent for all names | Returns from `close` would drop dividends | Use `adj_close` only; build month ends on trading-day positions |

**Harmless warnings**: SHY dropped by the sheet, nothing to check. No zero-volume or flat-bar problem in the six ETFs. Survivor bias (card): these ETFs are long-lived and chosen by type, not by later performance.

**New trap for `reference/checks.md`**: none.
