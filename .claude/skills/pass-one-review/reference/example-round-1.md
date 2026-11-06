# Example: round 1 on Crypto Funding Carry, with the desk's verdict

Pass 1 v1 of `vault/2 Strategies/Pipeline/Crypto Funding Carry.md`, reviewed on 2026-10-22. The critic gave 10 objections, three of them bundles (1, 7, 9); the round in the sheet splits them, one fix per row. The desk checked every claim against the sheet and the notes, then judged each objection.

## Verdict on each objection

| # | Objection, short | Critic | Desk | Why |
| --- | --- | --- | --- | --- |
| 1a | Gross Sharpe above 0.98 implies funding plus price above zero; a price-only P&L passes | blocking | valid, blocking | Best find of the round: the key check could not separate carry from its rival |
| 1b | P2 true under short beta, P3 partly mechanical | blocking | valid, blocking | |
| 1c | Dispersion not defined | blocking (bundled) | valid, major | A definition is missing, the test is not broken |
| 2a | Momentum control contains 24% funding | blocking | valid | Carry controlled with carry |
| 2b | No alt-minus-BTC factor | blocking | valid, blocking | Known factor in disguise, no control |
| 3 | Turnover rests on a floating leverage | major | half | The estimate is replaced by a measurement after the first run, the sheet says so. The real gap is the missing leverage cap, a hidden choice (row 9) |
| 4 | "Slow the signal if turnover is high" is a fifth try | major | valid, major | Good find: escape hatches are future tries |
| 5 | Gate power about 66% on the in-sample | major | valid, major | Fix is to state the power. The bar stays: the desk keeps strict gates (method.md, 1.11), decided by Lucas |
| 6a | Two periods, not three | major | minor | The rule is newer than the sheet |
| 6b | Criterion 2 reads the out-of-sample | major | valid, major | |
| 7a | "Fewer than 5 names" cannot fire | major | valid, major | Checked against the archive: 69% in the top 5, never fired |
| 7b | No t-stat on the intercept | major | valid, major | |
| 7c | 0.3 redundant with the luck line 0.42 | major | valid, minor | |
| 8 | Liquidation never charged to the P&L | major | valid, major | |
| 9 | Hidden choices missing from 1.5b | major | valid, partly nitpick | The V1 and V2 windows are written in 1.9; the rest is missing |
| 10 | "5 bp" left in 1.1; Review and Changelog missing | minor | valid for the text | The missing sections were a template change, not the Economist's fault |

## What the critic did wrong

- **One-sided rival**. It wrote that carry and momentum overlap in the library, citing Koijen p. 24 and Gorton p. 21. Koijen p. 24 is about commodities only, and the same note says carry alphas stay positive after momentum in every class (Table IV). Cite both sides; never stretch a figure beyond its asset class.
- **Bundles**: three objections held several fixes. The Economist answers row by row: one objection, one fix.
- **Severity inflation**: 7 majors out of 10; rows 3, 6a, 7c and 10 were overrated.

## What it found that became checks in attack.md

- The power of a gate, computed on the sample where it applies.
- Escape hatches ("if X, we will change Y") are future tries.
- A control must not contain the effect it controls.
- A combined condition can hide a redundant part.
- A kill criterion is checked against the archive to see whether it could ever fire.
