---
type: strategy
name: Bond Trend Demeaned
family: trend
asset: rates
horizon: monthly
status: killed
version: v1
stage: short
idea: "[[Idea Journal]] · 2026-11 · Bond trend on demeaned returns"
---

# Bond Trend Demeaned

Trend on government bond ETFs, net of an ex-ante drift: pays only if bond holders under-react to persistent rate cycles beyond the average return.

| Seat | Date | Verdict | File |
| --- | --- | --- | --- |
| Economist | 2026-11-06 | Go | [[Pass 1]] |
| Data | 2026-11-08 | Ready with reserves | [[Data check]] |
| Developer | 2026-11-08 | Gate failed (net Sharpe -0.27) | [[Build]] |

[[Changelog]]
