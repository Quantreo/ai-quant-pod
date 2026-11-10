## Data check

**Verdict: ready with reserves** · 2026-10-25 · data before 2018-01-01 read (train only); validation and test not read. `check_panel.py etf_daily --until 2021-01-01`: 0 missing, 0 inf, 0 duplicates, 0 backwards, 1 zero-volume bar (UUP, irrelevant).

**Load**: `load("etf_daily", test_start="2021-01-01")`, SPY rows, `adj_close` close to close. T-bill: `data/rates/tbill.parquet` (date, series USD_TB3M, rate % a year), not yet in `lab.data`: read the file and cut at the test start.

| Need (Pass 1) | Dataset | Field | Period | Status |
| --- | --- | --- | --- | --- |
| SPY daily return, RV of month m | etf_daily | adj_close | 2005-01-03 to 2017-12-29, 3272 bars, 156 months of 19-23 days | ok (issue 1) |
| Cash and borrow rate | tbill | rate, TB3MS monthly mean | 2004-01 to 2026-09, no gap 2004-12 to 2017-12 | ok (issue 3) |
| 12-month trend twin | etf_daily | adj_close month-ends | first 13th month-end 2006-01 | issue 2 |
| 2008-09 months | etf_daily | adj_close | 24 months, 19-23 bars each | ok |
| 3 largest residual months | strategy returns | | | not a data item (issue 4) |
| Cost | Cost Assumptions | SPY 2 bp | | ok, estimate to confirm by Lucas |
| Borrow above 1x | none | | | unsourced (issue 3) |

| # | Issue | Evidence | Effect on the test | Instruction to the Developer |
| --- | --- | --- | --- | --- |
| 1 | SPY 2008-10-13 looks too large | adj_close +14.5% (close 88.50 to 101.35); same day IWM +8.6%, QQQ +12.2%, EFA +15.9%. Also 10-15 -9.8%, 10-28 +11.7%. I recall the S&P 500 at about +11.6% on 10-13 (unverified, no index in the repo) | 2008-10 RV is 0.0713 (92% annualised) and sets the 2008-11 weight; a 3-point error moves RV by 10-20% | Keep the data (do not patch). Run P2 and report w for 2008-11 with and without the 10-13 return set to 11.6%. Lucas can check against a second source |
| 2 | Trend twin has no full first year | History starts 2005-01-03: no close of 2004-12. 12-month return needs 13 month-ends, first at 2006-01 | The common sample for the P1 regression is 2006-02 to 2017-12 = 143 months, not 155. Power (21%) is stated for 13 years: lower | Score vol rule and twin on the same 143 months, or state the 155-month vol-only sample separately. Say the N in the result |
| 3 | Rate conventions and unsourced borrow | TB3MS is a monthly mean, annual %: monthly cash = rate/1200. 33 of 157 months under 0.05% (2009-2015), min 0.01 (2011-09), max 5.03. Borrow = bill + 50 bp is the Economist's number, no source in the vault; a broker margin rate is usually above a bill | Net alpha is sensitive to the spread when w>1 (the cap 1.5 binds often: RV median 0.00123, min 0.00017, 7x lower) | Lag: signal at end of month m uses TB3MS of m-1 (Feb 2005 uses 2004-12 or 2005-01 per the m-1 rule, both present). Charge borrow only on (w-1)+ . Run 50 and 100 bp and the count of months with w>1 |
| 4 | "3 largest residual months" cannot be named by Data | They come from the P1 regression, a result | Risk of choosing them after seeing the P&L | Fix the rule in code before the run: absolute residuals of the P1 regression, outside 2008-09, top 3, listed in the output. 2008-09 read as calendar 2008 and 2009 (24 months; 13 years minus 2 = 10.8 as in 1.11) |

**Scored months**: signal at month-end m = 2005-01 to 2017-11, weight held in m+1: 2005-02 to 2017-12, 155 months (143 with the twin). Execution at the first close of m+1: the Developer states that day 1 of m+1 is excluded.

**Harmless warnings**:
- 12 flat adj_close days, all with volume above 42M and no run of 3: dividend-adjusted rounding, not a dead name.
- `adj_close` as of the download date: ratio to close 0.67 to 0.88. Use returns only, never levels or `close` (26 days differ by over 0.5%, dividend days).
- Cost 2 bp: 0.08% a year, small next to the borrow spread.

**Proposed line for checks.md** (equity ETFs): a 10%+ day should be compared with a sister ETF the same day; a gap of 3 points or more on SPY is a doubt for a second source, not a patch.
