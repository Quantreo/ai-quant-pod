---
type: reference
updated: 2026-10-26
---

# Kill Policy

> **What this is** : the one rule every seat follows to kill a strategy. The Economist writes kill criteria with it, the Critic reviews them with it, the Analyst and the Red team apply it.
> **Why** : the desk killed about forty ideas in two days, most of them on controls with 14 to 47% power whose t came out positive but under 2. "Not shown" was read as "no edge". See `3 Research Log/Desk reports/2026-10-25 Gate power diagnostic.md`.

## The principle

**Innocent until proven guilty.** A strategy is killed on evidence against it, never on the absence of evidence for it. A strategy with no evidence against goes to the test; the human reads its sheet and decides with his own judgement of the economics. The sealed test, the luck line and the money rule stay: they are what protects the book.

## What kills (evidence against)

1. **Level fails**:
   - train gate: net Sharpe at or below the luck line plus cost (measured turnover), or a t under the bar of the train's length (1 under 5 years, 2 otherwise);
   - validation: net mean negative with t at or below -1, or train plus validation pooled net Sharpe under the luck line;
   - test: the "contradicts" zone (test mean below minus half the earlier mean, test t under -1.5).
2. **A control contradicts**: the strategy does worse than its control (alpha t at or below -1), or the effect has the opposite sign of the mechanism with t at or below -1. A simpler twin that does better (difference t at or above 1) is not a kill: the twin replaces the base, one try.
3. **The construction is wrong**: a look-ahead or leak found (Red team), the sign flips without the best week, day or name, costs above half the gross P&L, a one-day delay that removes the P&L because of a leak.

At most three kill criteria per sheet, each one of these kinds.

## What does not kill (absence of evidence)

- A control or a prediction with a positive sign and a t under 2: a **label**, written at the top of Pass 2 and of the tear sheet. "Premium, alpha over <control> not shown (t 1.7)". "Mechanism not shown (P2 t 0.9)".
- A low-power criterion of any kind, a failed read-only prediction, a missing diagnostic.
- An ambiguous rule: say so, do not kill on it, write the question for the user.

Criteria written before this policy that kill on absence of evidence (a control's t under 2 with the right sign) are read as labels.

## Money

- The test decides paper or not. Money needs the net t-stat of train, validation and test together at 2 or more; otherwise paper only, whatever the zone.
- The PM decides whether the book needs it.
