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

## ETF TSMOM 12-Month

2026-11-09 · train 2006-2017, base, 2/5 bp, borrow 25 bp → monthly net Sharpe 0.626 (t 2.16), daily net 0.541, turnover 6.7/yr · retained (gate: bar 0.579)
2026-11-09 · train, always-long, same sizing → net Sharpe 0.439; base alpha t 1.83 · control
2026-11-09 · train, one-sign twin → net Sharpe 0.439; base alpha t 1.48 · control
2026-11-09 · validation 2018-2020, base → net Sharpe daily -0.31 (t -0.53), monthly -0.35 (t -0.60), 35 months, turnover 7.8/yr · logged
2026-11-09 · pooled 2006-2020, base → net Sharpe daily 0.409, monthly 0.467 (t 1.80, 179 months), turnover 6.6/yr · logged
2026-11-09 · pooled, always-long → monthly net Sharpe 0.379 · control
2026-11-09 · pooled, one-sign twin → monthly net Sharpe 0.137 · control
2026-11-09 · pooled, variant A (equal risk per class) → monthly net Sharpe 0.415 (t 1.60), daily 0.388 · step (try 2)
2026-11-09 · pooled, stress13 → monthly net Sharpe 0.508 (daily 0.418) · logged
2026-11-09 · pooled, stress9 → monthly net Sharpe 0.216 (daily 0.212, 168 months) · logged
2026-11-09 · pooled, costs 2x → monthly net Sharpe 0.433 (daily 0.379) · logged
2026-11-09 · pooled, borrow 1% → monthly net Sharpe 0.403 (daily 0.353) · logged
2026-11-09 · pooled, delay 1 trading day → monthly net Sharpe 0.397 (daily 0.349), turnover 6.7/yr · control
2026-11-09 · Analyst: K1 K2 K3 pass (validation t -0.60; alpha on SPY+TLT t +1.51; ex top 2 net P&L +0.365) → candidate for the test; labels: alpha over always-long t 1.69, over twin 1.67, pooled t 1.80 · verdict
2026-11-09 · Red team: truncation 60 days x3 pass; placebo signs (200) real gross 0.46 vs 95th pct 0.38 (1%); weights equal across code shas; stress9 P&L on DBC, FXY, HYG → open the test · verdict
2026-11-09 · test 2021-02 to 2026-09, base (frozen) → net Sharpe daily 0.572 (t 1.36), monthly 0.603 (t 1.57), maxDD -17.48%, turnover 7.5/yr; price long +35.9, short -5.7 · logged
2026-11-09 · Analyst: three zones, test mean 0.371%/m vs 0.276%: confirms; full-sample net t 2.35 (247 months) → passed, paper at half weight, money for the user to decide · verdict

## Bond Trend Demeaned

2026-11-08 · train 2008-2018, base, central cost → gross Sharpe -0.20, net Sharpe -0.27 (t -0.88), turnover 7.1/yr, financing -7.5% total · dropped (gate: needs net Sharpe 0.60)

## Crypto Low-MAX Long Leg

2026-11-08 · train 2021-2023, base, 5 bp → gross Sharpe 0.24, net Sharpe 0.12 (price-only net 0.24, t 0.42), turnover 54.5/yr, funding share -0.49 · dropped (gate: luck 0.30, t 1)
