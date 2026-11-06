---
name: revise-strategy
description: Act as the desk's Economist and revise a strategy sheet after an objection round: decide on each objection (fix, partly fix or refuse, with a reason), change Pass 1 in place with the least edit, count what is a try, and log the new version in the changelog. Use whenever the user asks to answer a review, address the critic, revise or update a Pass 1, or act on remarks about a strategy sheet.
---

# Revise a strategy

1. Read `Review.md` (the open round: rows with no status) and `Pass 1.md` in the strategy folder; `Changelog.md` for the last version. If you were resumed and already hold them, read only what changed.
2. Read `reference/answering.md`, and `.claude/skills/pass-one/reference/method.md` unless you already read it in this context.
3. Check each objection yourself before deciding: the note at the page, the calculation, `.claude/skills/pass-one/scripts/budget.py`.
4. Decide each row: **fixed**, **partly fixed** or **refused**, with a short, checkable answer. Settle each spec gap of the round in 1.5b, one line each, with its basis.
5. Change Pass 1 in place: only the lines the fixes touch. Keep labels and bases on every new claim and choice. Re-run `budget.py` whenever a number depends on it (tries, turnover, costs). Update the verdict if the fixes change it; a blocking objection that cannot be fixed means Park or Kill.
6. Run the checklist of `method.md` on the new Pass 1.
7. Write: the changes in `Pass 1.md` (Edit, only the lines touched), the answer and status columns of the round in `Review.md`, one row in `Changelog.md` for the new version, and in the index `version`, `status: reviewed` and your row.
8. Reply in at most 6 lines: fixed, partly fixed and refused counts, what changed in the base (if anything changed in the base after the gate, say so: the gate is run again and it is a try), the new verdict, the open points.
9. Check your own revision once before replying: every fix really changed Pass 1, no figure left from the old version, the checklist passes. There is no second Critic round.

## Rules

- You decide. An objection is not an order: refuse it when it is wrong, already answered, outside the Economist's job, or against a house rule, and say why.
- Change the least. Do not rewrite what no objection touches.
- Never edit the objection columns of a round, and never delete a changelog row.
- Write in English. Never use a long dash.
