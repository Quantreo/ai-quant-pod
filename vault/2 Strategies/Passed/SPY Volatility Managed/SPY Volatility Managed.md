---
type: strategy
name: SPY Volatility Managed
family: low-vol
asset: equities
horizon: monthly
status: passed
version: v1.3
stage: full
idea: "[[Idea Journal]] · 2026-10 · SPY: monthly exposure scaled by last month's realized variance, rest in T-bills"
---

# SPY Volatility Managed

SPY weight c / last month's realized variance, rest in T-bills. The payer is the investor who stays fully exposed through high-variance months (hypothesis).

| Seat | Date | Verdict | File |
| --- | --- | --- | --- |
| Economist | 2026-10-25 | Go (gate power 21%) | [[Pass 1]] |
| Data | 2026-10-25 | ready with reserves | [[Data check]] |
| Developer | 2026-10-25 | gate fail (G1 t 1.38, G2 t -0.66, bar 2) | [[Build]] |
| Economist | 2026-10-25 | new train gate pass (level t 2.66, bar 2); G1, G2 to validation | [[Gate reread]] |
| Economist | 2026-10-25 | Pass 1 full v1.2: to validation on level; V1, V2 pooled (power 23%, 20%) | [[Pass 1]] |
| Critic | 2026-10-25 | Revise (0 blocking, 5 major, 2 minor) | [[Review]] |
| Economist | 2026-10-25 | revised v1.3: 5 fixed, 2 partly fixed, base unchanged | [[Review]] |
| Developer | 2026-10-25 | validation: level pass (t 2.31), V1 t 1.49 fail, V2 t 0.59 fail | [[Build]] |
| Analyst | 2026-10-26 | test: keep, paper only (zone confirms; pooled alpha t 1.95 under 2; test alpha t 0.64) | [[Test]] |

[[Changelog]]
