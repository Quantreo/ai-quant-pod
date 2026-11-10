---
type: strategy
name: ETF TSMOM 12-Month
family: trend
asset: multi-asset
horizon: monthly
status: passed
version: v2
stage: full
idea: "[[Idea Journal]] · 2026-11 · Multi-asset ETFs: 12-month time-series trend"
---

# ETF TSMOM 12-Month

Sign of each ETF's own 12-month excess return, risk-balanced over 22 ETFs in four classes; paid by investors who under-react then chase, and by commodity hedgers.

| Seat | Date | Verdict | File |
| --- | --- | --- | --- |
| Economist | 2026-11-09 | Go (short Pass 1, v1) | [[Pass 1]] |
| Data | 2026-11-09 | Ready with reserves | [[Data check]] |
| Developer | 2026-11-09 | Gate pass: monthly net Sharpe 0.626, t 2.16, bar 0.579. Labels: alpha t 1.83 on always-long, 1.48 on the twin | [[Build]] |
| Economist | 2026-11-09 | Pass 1 full v1.1: Go; K1 to K3, variant A | [[Pass 1]] |
| Critic | 2026-11-09 | Revise: 0 blocking, 3 major, 2 minor | [[Review]] |
| Economist | 2026-11-09 | v2: 4 fixed, 1 partly fixed, 0 refused; base unchanged; Go | [[Pass 1]] |
| Developer | 2026-11-09 | Validation runs done (pooled, variant A, stresses, controls). Validation monthly Sharpe -0.35; pooled 0.467 | [[Build]] |
| Analyst | 2026-11-09 | Candidate for the test: no kill fires; validation Sharpe -0.35; pooled 0.467 (t 1.80); alpha labels not shown | [[Pass 2]] |
| Red team | 2026-11-09 | Open the test: 0 blocking, 2 major (labels), no leak; placebo 1% | [[Red team]] |
| Analyst | 2026-11-09 | Test passed, zone confirms: test mean 0.371%/m vs 0.276% earlier; full-sample t 2.35; thin edge, short leg loses | [[Test]] |

[[Changelog]]
