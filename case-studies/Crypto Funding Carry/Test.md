## Test (v5.3)

**Verdict: kill (stays killed). Zone: ambiguous.** · 2026-10-25 · run 20261025-154903-test-base (variant base, code sha 9368e6398542, lab 0fdde9124197), 2025-01-05 to 2026-09-30, 1.74 years, 91 Sundays. The lock TEST_DONE was written by the human at 15:49.

Why kill when the zone alone says paper: Pass 2 killed the sheet on criterion #3 (t 0.98 < 1). A failed kill criterion kills, and the zone rule decides only between keep, paper and kill for a strategy that is still alive. The test cannot lift a kill. If the human overrides Pass 2, the test would allow paper only, no money (see the two lines under the zone table).

### Zone (1.11 #5, net mean, weekly, daily series summed by week)

| | Train+validation (153054) | Test |
| --- | --- | --- |
| Weeks | 209 | 91 |
| Net mean per week | +0.414% | -0.045% |
| Net Sharpe | 1.077 | -0.138 (t -0.18) |
| Half of the earlier mean | 0.207 | |

Test mean -0.045 lies between -0.207 and +0.207: **ambiguous**. Contradicts needs below -0.207 and t < -1.5; neither holds (t -0.18). Confirms needs above +0.207: no.

Stitched net t (Newey-West, 4 weekly lags, train+validation+test, 300 weeks): mean 0.275%/wk, **t 1.53**, Sharpe 0.75. Under 2: not shown. Paper only, no money, whatever the zone. (5 daily lags: 1.71.) Note: the train+validation run and the test run carry different code_sha values (b99dae28bd5f, 9368e6398542); I did not check that the signal code is identical (weights_from says sha 8ada54c6f9b2 in the test).

### Predictions of Pass 1

| Item | Written | Measured | Result |
| --- | --- | --- | --- |
| Test power | true net 0.887 over 1.7 y gives t > 1 with 56% | t -0.18 | not met; a 44% outcome, but the point estimate is below zero, not just under 1 |
| Luck line | 0.75 | net -0.138 | below by 0.89 |
| #3 Mon-Tue price, residual | t >= 1 | not run on test (Pass 1 lists no post-test diagnostic) | Pass 2 fail stands |
| #4 price intercept, weekly | t >= 1, positive | test price -0.36%/wk, total -32.99% | price is negative; no factor regression run |
| 1.3 negative skew, crashes | suffers in crashes | max drawdown -19.95%, 17 liquidations, 5 delisting exits | consistent |
| Cost | 20 bp short, 5 bp long | costs -8.69%, break-even 6.9 bp | edge is below the assumed cost; gross 0.164 does not cover it |

### What the two payers did

| Per week, % | Train+val | Test |
| --- | --- | --- |
| Price | +0.274 | -0.363 |
| Funding | +0.256 | +0.416 |
| Costs + liquidations | -0.117 | -0.098 |

- **Funding paid.** +37.8% in 1.74 years, more per week than in train+validation. The carry payer is alive.
- **The weekend price effect did not pay.** Price flipped from +57% to -33%. By leg in the test: long -68.2, short +35.2 (train+val: long +126.7, short -69.3), the opposite of the earlier pattern. The long leg, which carried the train+validation price, lost.
- Funding minus costs and liquidations is about +28.9%; price took -33.0%. The book is a funding carry with a price book on top whose sign is not stable. Price and funding are not the two independent payers written: the price leg offset the carry.
- Descriptive only, not criterion #3 (all names, no residual): Monday-Tuesday price in the test -17.3 pts, other days -15.6 pts. No fast Monday-Tuesday edge appears. The Monday-Tuesday split and the Sunday-Wednesday placebo are not listed in Pass 1 as post-test diagnostics, so they were **not run**.

### Next seat

Economist: nothing to reopen. A funding-only version would be a new sheet with new tries, and one test period is now used. Nothing goes to the book.
