# Answering objections

## Deciding

- **fixed**: the objection holds and Pass 1 now answers it. Say where: "1.11 #1 now requires...".
- **partly fixed**: the objection holds in part. Fix the part that holds, and say why the rest does not. Fixing everything an objection asks, when half of it is wrong, adds numbers and checks nobody needed: every addition is one more thing the Developer must build and one more way to kill by chance.
- **refused**: the objection is wrong (a fact, a page, a calculation), already answered in an earlier round, outside the Economist's job (data plumbing, code, the book), or against a house rule. Give the reason in a way anyone can check. "I disagree" is not a reason.

Severity does not decide for you: a blocking objection can be wrong, a minor one can be right. But a blocking objection that holds and cannot be fixed changes the verdict.

## Fixing

- Prefer a sharper prediction, a better control or a diagnostic to a new variant. Never add a kill criterion that kills on absence of evidence (`vault/Toolbox/Kill Policy.md`): a new control is a label. Each variant is a try and raises the luck line; there are still 3 at most.
- A fix that adds a number adds a row to 1.5b, with its basis.
- A fix must be able to change a result. A check that cannot fire in this design (a liquidation rule that needs a 90% loss) is not a fix: say so and propose what can.
- A fix that adds a gate or a prediction states its power on the sample where it applies, like every gate.
- A condition true by construction tests nothing (a book short the high-funding names collects funding as long as funding persists a week): do not add one to answer an objection.
- A fix that changes the number of tries, the turnover or the costs: re-run `budget.py` and update every figure that depends on it (1.6, 1.7, the verdict, 1.11).
- House rules are not negotiable in a round: strict gates (the bar is never lowered to raise the power, `method.md` 1.11); train, validation and test fixed in Pass 1; costs in from the first run.

## Counting tries

What counts is whether a result was seen when the change was decided.

- **Before any result** (critic rounds on Pass 1, a Developer question on the spec before the first run): the design is still being written. A change is not a try, but every variant it adds is, and the luck line counts them.
- **After a result** (a run, a diagnostic, a Developer report with numbers): any change to the strategy decided by looking at a result is a try. Write in "Decided on" which period the result came from: train, validation or test.
- **Decided on the test period**: the test is burned. Say so in the changelog and in "Data already seen": only paper trading can judge the strategy from then on.
- A bug fix that makes the code match Pass 1 is not a try. A change to Pass 1 itself is a strategy change.

## Changelog row

One row per version, not per objection.

| Version | Date | Change | Why | Triggered by | Decided on | Counts as a try |
| --- | --- | --- | --- | --- | --- | --- |
| v2 | 2026-10-23 | P1 now requires the funding component to carry most of the gross P&L (1a); P4 regresses on price-only momentum and alt-minus-BTC (2a, 2b); ... | Round 1 | Critic, round 1 | none (before any data) | no; tries 4 to 5 (V4 added) |

## Later

Remarks from the Developer (spec gaps, measured turnover, data problems) will arrive the same way: a round under `## Review`, signed by the Developer. The Developer reports; the Economist decides; the Developer builds what Pass 1 says.
