---
type: strategy
name: ETF TSMOM 12-Month
family: trend
asset: multi-asset
horizon: monthly
status: reviewed
version: v1.4
stage: full
idea: "[[Idea Journal]] · 2026-10 · Multi-asset ETFs: 12-month time-series trend"
---

# ETF TSMOM 12-Month

Sign of each ETF's own 12-month excess return, risk-balanced over 22 ETFs in four classes; paid by investors who under-react then chase, and by commodity hedgers.

| Seat | Date | Verdict | File |
| --- | --- | --- | --- |
| Economist | 2026-10-25 | Go | [[Pass 1]] |
| Data | 2026-10-25 | Ready with reserves | [[Data check]] |
| Developer | 2026-10-25 | Gate: G1 fail (t 1.77 / 1.43 / 1.45), G2 pass | [[Build]] |
| Developer | 2026-10-25 | Rerun at 25 bp: gate pass (monthly 0.626) | [[Build]] |
| Economist | 2026-10-25 | Re-read v1.1: new train gate pass (net Sharpe 0.606, t 2.09 vs 0.579); controls to validation | [[Pass 1]] |
| Economist | 2026-10-25 | Pass 1 full v1.2: Go; K1 to K5 pooled, variant A | [[Pass 1]] |
| Economist | 2026-10-25 | v1.3: borrow 25 bp in the base, one try, gate to rerun | [[Pass 1]] |
| Economist | 2026-10-25 | v1.4: round 1, 3 fixed, 2 partly fixed; Go | [[Review]] |
| Critic | 2026-10-25 | Revise: 0 blocking, 3 major, 2 minor | [[Review]] |

[[Changelog]]
