## Test

**Verdict: passed, zone confirms** · 2026-11-09 · run 20261109-112907-test-base · code 56ac41f76375 · lab 70e86da018e5 · test 2021-02 to 2026-09 (68 months)

**Label: full-sample net t 2.35 (247 months, NW 4): money possible at half weight, after the user's decision. But the edge is thin (test t 1.36 to 1.57) and the short leg still loses on price.** Report: [[ETF TSMOM 12-Month - Backtest report]].

### Three-zone rule (1.11, monthly net, frozen base)

| Sample | Months | Mean/month | NW t | Net Sharpe |
| --- | --- | --- | --- | --- |
| Train + validation (frozen base) | 179 | 0.276% | 1.81 | 0.467 |
| Test | 68 | 0.371% | 1.57 | 0.603 (summary daily 0.572, t 1.36) |
| Full sample | 247 | 0.302% | 2.35 | 0.506 |

Test mean is 134% of the earlier mean, above the half line (0.138%): zone **confirms**. Full-sample t 2.35 is at or above 2: the edge is shown on the whole sample. No Kill Policy kill. Bootstrap net Sharpe on test, 5/50/95%: -0.05 / 0.55 / 1.17.

### What the test says, and does not say

| Item | Number | Reading |
| --- | --- | --- |
| Gross / net daily Sharpe | 0.632 / 0.572 | costs small: price 30.1%, funding -2.3%, costs -2.6% |
| Max drawdown | -17.48% | deeper than the validation pain, within a 7.8% vol book |
| By year (net daily) | 0.88, 1.14, -1.03, 0.27, 0.46, 1.37 | 2023 lost; five of six years positive. The 2018-20 decay did not continue |
| Legs | price long +35.9, short -5.7 | short leg loses on price again (train+val: -25.9). Funding: long -16.9, short +14.6 (cash rate) |
| Concentration | top 5 names 63% of P&L (FXY, DBC, QQQ, EWJ, SPY) | no single name over 4.2%; VNQ -3.0, IWM -2.2 |
| Turnover | 7.5/yr (6.6 pooled) | as written |

The P&L is price, as the mechanism says, and it is carried by the long side. The short side adds nothing in total over 20 years. A long-biased trend book is what was found; a long-only variant would be a new try, not part of this sheet.

### Red team findings (see [[Red team]]) and Pass 2

Noted, none changes the verdict: thin edge; short leg loses on price; stress9 rests on DBC, FXY, HYG; 2018-20 decay (the test did not repeat it). Two figures in [[Pass 2]] disagree with the Red team: stress9 top-five share (Pass 2: 116%, Red team: 131%) and the K2 read-only alpha t 0.78 with 2008-09 dropped (Red team did not reproduce it; it came from `analysis/k2_regress.py`, SPY+TLT regression, which is a different test from alpha over always-long, t 1.44). Pass 2 is a dated record and is left as written; both are flagged here. Neither touches a kill criterion (K2 pass at t +1.51 on the full sample). Not re-derived by me after the test: open for the user if it matters.

### Next

Keep, paper trading at half weight if the user adds it to the book (the book is the user's decision). Money only by the user, knowing t 2.35 is just over the bar and the test t is 1.57. Folder moved to Passed.
