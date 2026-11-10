## Red team

**Recommendation: open the test** · 2026-11-09 · code sha 56ac41f76375 (current file; pooled runs carry ed3a686172a3) · lab 70e86da018e5

No leak, no data artefact, no kill evidence. The edge is thin: a label, not a block.

| # | Finding | Severity | Evidence | Fix, and who |
| --- | --- | --- | --- | --- |
| 1 | Hash mismatch is cosmetic: base weights identical across code versions | minor | train run (eb47) vs pooled (ed3a) on 144 shared months: max abs diff 5.6e-17; validation run vs pooled, 35 months: 0.0; delay run (56ac) equals the pooled weights shifted, diff 0.0. Current file hashes to 56ac41f76375, so ed3a was an intermediate edit (CLI flags). | Developer: one line in Build.md, "weights checked equal to eb47 and ed3a" |
| 2 | Shorts destroy value: net short leg is negative, the book is a long-biased trend | major (label) | price long +0.856, short -0.259, funding long -0.161, short +0.116 (net long +0.695, net short -0.143). 2018-20: long +0.107, short -0.122. Beta on always-long only 0.04, so it is not plain drift, but the short sign adds nothing in total. | User: expect a thin, not-shown edge; a long-only variant is a new try, not for the test |
| 3 | The 2008-09 to 2009-12 window does not carry the Sharpe, it carries the alpha over always-long | minor | Sharpe 0.467 with, 0.465 without (163 months). Alpha over always-long NW4: t 1.69 all, 1.44 without; always-long Sharpe rises 0.38 to 0.53 without it. The Analyst's 0.78 is the SPY+TLT regression (k2_regress.py), not replicated here. | none |
| 4 | Survivor stress9 rests on three names | major (label) | stress9 net P&L 0.245: DBC 42%, FXY 41%, HYG 27% (top 5 = 131%, Pass 2 says 116%). stress13 P&L 0.525, top 5 only 65% (IEF, SPY, QQQ, GLD, LQD), Sharpe 0.508 above base. | none, read as "conditional on the 2026 list" |
| 5 | SPY and QQQ matter but are not the result | minor | SPY +0.080, QQQ +0.068 price; P&L without them 0.365 of 0.494 (74%). Top 5 names (SPY QQQ IEF GLD DBC) 54% of by-name P&L. 22 names, no single one over 7%. | none |
| 6 | Top P&L days are real moves | minor | 2008-09-29 +3.4%, 09-17, 10-15, 09-15, 09-22 (Lehman weeks), 2011-08-09, 2016-06-24 (Brexit), 2020-03-23, 2006-06-15. No gaps vs SPY in any ETF's life; moves above 8% outside 2008-09/2009-05 are SLV, USO, FXI, EM and the Mar-2020 cluster, all known events. | none |
| 7 | Trials.csv pooled base row marked "no" is correct | minor | Same code, weights equal to the train row, only the period extends (rows 8 vs 4). The Analyst's edit is consistent with the rule; A is counted. Cosmetic: why column of rows 12-16 repeats "delay1: control, rerun 103939" (copy-paste). | Analyst: tidy the why text |

**Fill**: signal close = trade close; delay1 keeps 85%.

**Code audit**: no `shift(-k)`, centred window, full-sample normalisation or bfill. Signal at line 136 uses `px_f` at d and d0 (past), cash months up to m-1 (line 98, asserted known by d); vol (116) and covariance (150-151) cut at d; membership at d0 (128) uses a first date, not a future one. Cash prints (cash_prints) feed P&L only, never the signal.

**Tests run**: truncation (60 days, seed 7, base, twin, A): pass x3; placebo signs, pooled, 200 shuffles: real gross 0.46, shuffled median 0.17, 95th pct 0.38, 1.0% of shuffles at or above; costs x2: read Developer run 103905 (same code behaviour): gross 0.457, net daily 0.379 (monthly 0.433), costs about 10% of gross P&L.

**Against Pass 2**: agree with the verdict, the thin edge and the long-leg reading. Differences: the 2008-09 window leaves the Sharpe intact, only the alpha over always-long weakens (t 1.44); stress9 concentration is 131% not 116%, three names (DBC, FXY, HYG). The hash worry is resolved. The 2018-20 decay (monthly -0.35) stays the main risk.

**Lessons**: (1) A hash mismatch is settled by comparing saved weights.parquet between runs. (2) For a long/short trend book, split price P&L by leg early: the short leg can lose while the book is "alpha".
