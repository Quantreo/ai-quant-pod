---
type: strategy
name: Crypto Funding Carry
family: carry
asset: crypto
horizon: weekly
status: killed
version: v5.3
stage: full
idea: "[[Idea Journal]] · 2026-10 · Funding carry on crypto perpetuals"
---

# Crypto Funding Carry

| Seat | Date | Verdict | File |
| --- | --- | --- | --- |
| Economist | | Go with a check. | [[Pass 1]] |
| Critic | 2026-10-22 | revise | [[Review]] |
| Data | 2026-10-25 | ready with reserves (v5) | [[Data check]] |
| Developer | | train gate: pass | [[Build]] |
| Analyst | | inconclusive | [[Pass 2]] |
| Red team | | fix first | [[Red team]] |
| Economist | 2026-10-25 | Go (v5, fast-effect sheet, Wednesday placebo at the gate) | [[Pass 1]] |
| Economist | 2026-10-25 | v5.1: Data check #9 to #17 pre-registered, ready for the Developer | [[Pass 1]] |
| Developer | 2026-10-25 | v5.1 train gate: pass (net Sharpe 0.89, P1 t 1.77) | [[Build]] |
| Developer | 2026-10-25 | v5.3: residual P1 t 1.86 pass; validation: #4 t 1.15 pass, #3 t 0.98 FAIL | [[Build]] |
| Economist | 2026-10-25 | v5.2: Pass 1 full after the passed gate, ready for the Critic | [[Pass 1]] |
| Economist | 2026-10-25 | v5.3: round 4 answered (4 fixed, 3 partly fixed, 1 refused); residual P1 to compute on train before validation | [[Review]] |
| Critic | 2026-10-25 | revise (v5.2, round 4: 1 blocking, 5 major, 2 minor) | [[Review]] |
| Analyst | 2026-10-25 | kill (v5.3: #3 t 0.98 < 1; #1, #2, #4 pass) | [[Pass 2]] |
| Analyst | 2026-10-25 | kill (test: zone ambiguous, net -0.14, stitched t 1.53; Pass 2 kill stands) | [[Test]] |

[[Changelog]]

## Decision

**Parked** · 2026-10-23 · by the user, at the human gate, before any test.
- Why: the returns are not stable enough (the P&L comes in bursts, a few days and names carry it), and the price P&L is a fast effect in the first two days after the trade, not the weekly carry written in Pass 1. The carry part alone sits at the gate's bar.
- What would bring it back: a mechanism rewritten around the fast price effect, checked on hourly mark prices (fill a few hours after 00:00), as a new try; or a carry-only version with a stability rule the desk does not have yet.
- The test period was never opened.
