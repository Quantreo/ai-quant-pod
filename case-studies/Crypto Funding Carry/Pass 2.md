## Pass 2 (v5.3)

**Verdict: kill** · 2026-10-25 · runs read: 20261025-151935-train-base, -153304-train+validation-base, -153306 and -151945 (short 40), -151943 (both 20), -153405 (P1 residual), -153353 crit3 all and ex5 · lab 0fdde9124197 on all · report: [[Crypto Funding Carry - Backtest report]]

Criterion #3 fails: Monday-Tuesday price P&L without the 5 best names, residual, 04:00 fill, 208 weeks: 0.100%/wk, t 0.98 against a bar of 1. With all names it is t 2.66, so the effect is carried by five names (SOL, WLD, WAVES, 1000PEPE, MATIC). Rules: a failed kill criterion kills, no "almost". The miss is 0.02, but the bar was written before the result and is not moved.

### Kill criteria (1.11)

| # | Criterion | Bar | Measured | Pass |
| --- | --- | --- | --- | --- |
| 1 | Residual P1, train, 156 pairs | t 1 | 0.332%/wk, t 1.86 (raw 1.77) | pass |
| 2 | Net Sharpe tiered, train | 0.75 | 0.887 (+0.14 over the line) | pass |
| 3 | Mon-Tue price, ex 5 best names, residual, 208 wk | t 1 | 0.100%/wk, **t 0.98** (raw 0.97) | **FAIL** |
| 4 | P2 intercept, weekly price, 4 factors, 208 wk | t 1 | 0.222%/wk, t 1.15 | pass |
| 5 | Test | | not opened | |

HC: Pass 1 says only "HC". HC1 gives 0.98. HC0 removes the n/(n-k) factor, about 0.99 by arithmetic, still under 1; HC2 and HC3 are lower. Raw t is 0.97. No reading reaches 1, so the ambiguity does not change the verdict (stricter reading applied).

**What Pass 1 says a miss means.** 1.11 is headed "Kill criterion", the table lists #3 as a bar, and the header says a residual P1 under 1 is a kill. Pass 1 does not say a #3 miss is softer than a #1 miss. 1.3 warned the payoff is "carried by a few weeks", and 1.6 gave #3 only 67% power at 0.10 sd: a true small effect fails this bar one time in three.
**What it does not say.** It does not say the weekend effect is absent (all names t 2.66; the miss is about its breadth). It gives no right to a second exclusion, other SE, other names or horizon: Build.md notes none was run, and none is run here.

### Predictions (1.1)

| P | Measured | Confirmed |
| --- | --- | --- |
| P1 (separates from beta) | residual t 1.86, slopes near zero | yes; absent in 2023 (-0.06, t -0.22) |
| P2 (validation) | t 1.15 on 208 weeks (train alone 0.35) | yes, thin; rests on 2024 |
| P3 (read only) | 2022 price -26 pts in v4 reads; not recomputed in v5.3 | not measurable here |
| P4 (read only) | residual short 0.228 (t 1.54), long 0.105 (t 0.77) | partly: short leg larger, not alone |

### Luck, costs, controls

- Tries 6, years 3, luck line 0.75; train net 0.887, above by 0.14. N_eff not computed (v4 correlation 0.51 across 4 runs). Pooled train+validation net 1.077, NW t 1.69 (<2: paper only even without the kill).
- Fragility confirmed: train net 0.659 at short 40 bp and 0.738 with both legs at 20 bp, both under 0.75. Pooled short 40: 0.838, t 1.32.
- Delay and survivorship controls exist only for v4 (095319 delay: price P&L 42.3 to 6.0; 095317 today's top 30: Sharpe 1.47 to 0.39); not re-run on v5. A fast effect and a universe effect, consistent with #3.
- P&L: pooled price 57.4, funding 53.6, costs -23.3 (funding share 0.48; train 0.64). 2023 price negative: two payers, and the written second one is the fragile one.

### For the next seat

- Economist: the sheet is dead on its own bar. A new idea needs a new sheet and new tries; do not reopen #3.
- Red team: none needed before a test that will not run.
