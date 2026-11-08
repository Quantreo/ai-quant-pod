---
type: log
---

# Research Log

> **What this is** : one line per variant you actually ran, grouped by strategy. The count tells you how much to discount your best Sharpe.
> **Open it** : during every test slot, after every run. Not at the end of the day: after every run.
> **Rule** : a variant you ran and forgot still counts. Write it while the cell is executing.

**How it is organised** : one section per strategy, newest strategy first. Inside a section, runs in the order you ran them: read top to bottom, it is the story of the research. The count at the top of each section feeds box 2.7 of the strategy sheet.

**Line format** : `date · what changed → result · verdict`

**Verdicts** : baseline · step · insight · dropped · retained · control · logged

---

## Bond Trend Demeaned

2026-11-08 · train 2008-2018, base, central cost → gross Sharpe -0.20, net Sharpe -0.27 (t -0.88), turnover 7.1/yr, financing -7.5% total · dropped (gate: needs net Sharpe 0.60)

## Crypto Low-MAX Long Leg

2026-11-08 · train 2021-2023, base, 5 bp → gross Sharpe 0.24, net Sharpe 0.12 (price-only net 0.24, t 0.42), turnover 54.5/yr, funding share -0.49 · dropped (gate: luck 0.30, t 1)
