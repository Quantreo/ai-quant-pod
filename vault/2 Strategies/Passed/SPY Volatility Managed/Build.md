## Build (train, 2026-10-25)

**Code**: `strategies/spy_volatility_managed.py` · sha `6f0c03eed524` · built 2026-10-25 on Pass 1 v1.1. Look-ahead (truncation, 20 trade days, base and twin): PASS.

**Scored**: held months 2005-02 to 2017-12 = 155 months (day 1 of m+1 is not in RV of m and is earned by the old weight); gates on 143 (2006-02 to 2017-12). The 2017-12 month ends at the first close of 2018-01 (2018-01-02): one validation price used as an end mark, no signal reads it. Test never opened.

**Gate (1.11)**: bar t >= 2 (NW, 4 lags), file as is, net, regression on SPY excess and twin. G1 (143 months): alpha 2.4%/yr, **t 1.38 → fail**. G2 (116 months, dropped 2011-09, 2012-06, 2016-03 with residuals 8.8%, 7.2%, 4.4%): **t -0.66 → fail**. With 2008-10-13 at +11.6%: 1.45 and -0.65 (also fail; the file as is is the less favourable and decides). Not rescued by either reading. Power was 19% / 17%: a fail is logged "not shown on SPY 2005-2017".

| Choice | Pass 1 | Code | Data check |
| --- | --- | --- | --- |
| RV2 | 1.5 | sum of squared daily returns of month m, no demeaning (Pass 1 silent, small effect) | none |
| Weight | 1.5 | min(c/RV2, 1.5); trades first close of m+1 | #2 |
| c | 1.5, fn 5 | bisection, managed gross vol = SPY vol on the 155 train months, refit in the +11.6% run (0.00370 file; 0.00388 patched) | none |
| Cash | 1.5 | held month M uses TB3MS of M-2 (signal month m = M-1 uses m-1), rate/1200; read literally | #3 |
| Borrow | 1.5 | (w-1)+ at cash + 50 bp via a second leg SPY_LEV; stress 100 bp | #3 |
| Cost | 1.7 | 2 bp, engine cost_bp, both legs | none |
| Twin | 1.5 | sign of SPY 12-month excess (no skip), +-1, same timing, no cost (Time-series momentum note; Pass 1 gives no more) | #2 |
| Newey-West | 1.11 | Bartlett, 4 lags = floor(4(n/100)^(2/9)); Pass 1 gives none (sister sheets' rule) | none |
| Kill 2 | 1.11 | residuals of G1, drop 2008-2009 months, 3 largest signed, earlier first on ties, refit | #4 |
| Data | 1.11 | 2008-10-13 patched in memory by scaling later levels; file untouched | #1 |

Train runs: 142825 base (G1 t 1.38, G2 -0.66, net Sharpe 0.772 monthly), 142830 +11.6% (1.45, -0.65), 142835 borrow 100 bp (1.27, -0.87), 142811 superseded aggregation bug.

## Validation build 2026-10-25 · Pass 1 v1.3

**Code**: sha `716445a634ed`, lab_sha `0fdde9124197` (same as train). Truncation PASS (all four). Base unchanged: pooled run matches the train months to 0.0 (max diff). Test never opened (`run` refuses it; loader cuts at 2021-01-01).

**Scored**: held months 2005-02 to 2020-12 = 191; gates on 179 (2006-02 to 2020-12; V2 152). The last month (2020-12) ends at the last close of 2020, not the first close of 2021 (sealed): a few days short. 1-month twin: sign of SPY excess over the last month, cash of m-1. c is the train value 0.00370. Lag runs trade 1 or 2 trading days later, same signals.

**Criteria (net, NW 4 lags)**: level monthly Sharpe 0.678 (t 2.62), engine daily 0.599 (t 2.31): less favourable t 2.31 over bar 2, above luck line 0.13 + cost 0.04: **pass (floor)**. **V1 alpha 2.16%/yr, t 1.49: fail**. **V2 alpha 0.84%/yr, t 0.59: fail** (dropped 2012-06, 2011-09, 2015-10). Betas SPY 0.86, 12m 0.34, 1m 0.18.

| Run (read only unless noted) | Level t m / d | V1 t | V2 t | SPY-only t |
| --- | --- | --- | --- | --- |
| base 160847 | 2.62 / 2.31 | 1.49 | 0.59 | 1.39 |
| 2008-10-13 +11.6% | 2.61 / 2.31 | 1.49 | 0.59 | 1.41 |
| borrow 150 bp | 2.54 / 2.24 | 1.22 | 0.28 | 1.26 |
| borrow 25 bp | 2.64 / 2.33 | 1.55 | 0.66 | 1.42 |
| cost 4 bp | 2.61 / 2.31 | 1.45 | 0.56 | 1.37 |
| lag 2 days | 2.66 / 2.25 | 0.98 | 0.00 | 1.36 |
| lag 1 day (control) | 2.53 / 2.22 | 0.90 | -0.35 | 1.14 |
| variant 1 (3m RV), counts | 2.07 / 1.81 | -0.22 | -1.55 | 0.41 |

**P3** (mean/variance by tercile low, mid, high): pooled 12.5, 3.2, 1.7 → passes (low > high), so variant 1 was run; train alone 15.3, 1.3, 1.6 (mid below high). **2020-03**: w 0.77 (Feb 1.5, cap), net -15.5% against SPY excess -20.0%; without it V1 alpha 1.38%/yr, t 0.92 (178 months). Validation alone (36 months): net Sharpe 0.42, SPY 0.64. Months at cap 138 of 191; turnover 2.32/yr (estimate 3.96).

**Not run**: cap 1, 10% target stresses.
