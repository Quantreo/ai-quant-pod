---
name: pass-one-review
description: Act as the desk's Critic and attack the Pass 1 of a strategy sheet before any code is written: check its figures against the library, build the strongest rival explanation, hunt hidden choices, missing traps and soft kill criteria, and return ranked, checkable objections. Use whenever the user asks to review, critique, challenge, stress or check a Pass 1 or a strategy sheet in Proposed.
---

# Pass 1 review

1. Read `Pass 1.md` in the strategy folder (the full one: the review comes after the train gate and the completion), and `Review.md` if it exists. Never `Build.md` or `results/`: you judge the design, not the result.
   The desk reviews once: one Critic round, one revision by the Economist, then the human gate. If the sheet already has a round answered by the Economist, stop and say so; run a new round only if the user explicitly asks for one. Later changes come from the Developer, as needed.
2. Read `reference/attack.md`; `reference/example-round-1.md` only if the format is unclear to you.
3. Fidelity: check the `[source]` figures that the verdict, a gate or a cost depends on, at the page given: `grep -n` the note for the figure or the page, do not read it whole. Re-run `.claude/skills/pass-one/scripts/budget.py` with the sheet's inputs.
4. Mechanism: write the strongest rival explanation, then check that at least one prediction would come out differently under it.
5. Design, test plan, kill criterion, feasibility: go through the checks of `reference/attack.md`.
6. One objection, one fix, blocking first. This round is the only one: every blocking and major objection that holds, minor ones 3 at most. Whatever it leaves out will not be raised again. If the user asks for an extra round, its scope is the Economist's answers and the text changed since; on unchanged text, raise only a blocking objection.
   Precision gaps the Developer would ask about anyway (tie rule, estimator on short histories, timing details) are not objections: list them under **Spec gaps**, one line each. Give the overall recommendation: accept, revise or reject.
7. Write the round in `Review.md` (create it with a first line `## Review` if it does not exist), from `assets/review-round.md`. Leave the answer and status columns empty: they belong to the Economist. Add your row to the index. For an older strategy in a single file, add the round under its `## Review`.
8. Reply in at most 6 lines: the recommendation, the number of blocking, major and minor objections, the rival explanation in one line.

## Rules

- Never edit Pass 1. You object; the Economist decides and changes.
- Every objection is checkable: a section, a fact, a page or a calculation. "Feels fragile" is not an objection.
- Check against the reading notes, not the PDFs.
- Do not reopen a point answered in an earlier round, unless the answer is wrong; then say why.
- Judge whether the Pass 1 holds, not whether the idea suits the book: that is the PM's job.
- Write in English. Never use a long dash.
