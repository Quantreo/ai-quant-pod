# SPY Volatility Managed · Test (2026-10-26)

**Verdict: keep, paper only, no money.** No kill fires under [[Kill Policy]]. The zone confirms, but the final proof is 1.95 against a bar of 2, so paper only whatever the zone (Pass 1 1.11 point 4). Label at the top: **premium shown on level, alpha over SPY and both twins not shown (pooled t 1.95; test alone t 0.64)**.

Run `20261026-085632-test-base`, frozen base (code sha f132027c06b1, lab_sha 0fdde9124197, as train and validation), 69 months 2021-01 to 2026-09, lock TEST_DONE. Net of fees. Scripts: `results/spy_volatility_managed/analysis/test_pooled.py`, `test_pooled2.py`.

## Numbers

| Figure | Train + validation | Test | Pooled |
| --- | --- | --- | --- |
| Net Sharpe monthly (t) | 0.683 (2.72), 191 m | 0.923 (2.21), 69 m | 0.749 (3.49), 260 m |
| Net Sharpe daily engine (t) | 0.599 (2.39) | 0.819 (1.96) | 0.547 (3.07) |
| SPY Sharpe monthly | 0.549 | 0.835 | 0.613 |
| Alpha over SPY + both twins, %/month (NW t) | 0.175 (1.49), 179 m | 0.102 (0.64), 69 m | **0.196 (1.95), 248 m** |
| Betas SPY / 12m twin / 1m twin | 0.86 / 0.34 / 0.18 | 1.12 / 0.20 / -0.02 | 0.90 / 0.34 / 0.15 |

Pooled alpha is 2.35%/yr. Pass 1 power for this proof was 26% at 0.3, so a miss at 1.95 is weak evidence of no edge.

## Criteria (1.11)

| Criterion | Number | Result |
| --- | --- | --- |
| 4 Final proof, alpha NW t >= 2 on all three | 1.95 (bar 2) | **not met: paper only** |
| 4 House floor, level net t >= 2 on all three | 3.07 daily (less favourable), 3.49 monthly | met |
| 5 Zone, test alpha vs train+validation alpha (train+val betas applied) | 0.366 vs 0.175 %/month, 2.1x, above half | **confirms** |
| 5 Same with test's own betas | 0.102 vs 0.175, 58%, above half | confirms |
| 5 Contradicts (below minus half and t < -1.5) | test alpha t +0.64 to +1.83 | no |
| Kill Policy 1 to 3 (level, control contradicts, construction) | none fires | no kill |

Raw net monthly mean: test 1.38% against 1.00% earlier. Both zone readings agree, so the choice of reading does not matter.

## What the result is

- **Not the written mechanism.** In the test the book holds SPY at beta 1.12 and beats it by 0.39%/month, but alpha over SPY and the twins is 0.10%/month (t 0.64). Test Sharpe 0.82 (daily) against SPY 0.84 (monthly 0.92 against 0.84): about SPY with leverage in a strong bull market, not a variance-timing edge. Max drawdown -30.4%.
- Costs are nothing (2 bp, turnover 2.0/yr, 0.23% of P&L). Funding is -27% of the price P&L: the borrow above 1x and cash.
- Earlier labels stand: V1 t 1.49 and V2 t 0.59 (positive, under 2) are labels under the Kill Policy; the one-day delay lowered V1 to 0.90 and V2 to -0.35 (not at or below -1). Variant 1 was dropped.
- Money rule: level t is above 2, but the alpha proof is not, and the sheet says paper only. The sheet's own "equity timing, one risk unit" note applies for the PM.

## Questions for the user

1. The folder is `Killed` and the index status is `killed` (set on V1 and V2 failing, a kill by absence of evidence the Kill Policy reads as a label). My verdict is keep on paper; moving it out of `Killed` is yours. Done since: the user moved it to `Passed`, status `passed`.
2. Criterion 5 does not say which betas the zone uses. Both readings confirm, so no kill or zone depends on it.
