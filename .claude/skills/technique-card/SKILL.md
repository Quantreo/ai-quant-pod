---
name: technique-card
description: Turn techniques found in a reading note (or given by the user) into short technique cards in the vault library, one card per reusable technique, filed by brick, merged when a card already exists. Use after reading-source, or whenever the user asks to make, update or file a technique card, a "fiche technique", or to add a sizing, signal, exit, risk or diagnostic method to the library.
---

# Technique card

1. Collect the techniques: the Techniques table of the reading note, or the technique the user gives.
2. Triage each one as `reference/triage.md` says: card, diagnostic, or no card.
3. Show the triage table to the user and wait for their answer. If nobody is there, go on and list the triage in the reply.
4. For each card, search `vault/0 Library/Techniques/` for the same technique under any name: titles, `aliases` and "What it does".
5. Existing card: if it already lists this source, skip it. Otherwise add one bullet for the new source under each heading of "What the sources say" and under Sources, add a Variant line to "How it works" if the source changes the method, add its other names to `aliases`, add 1 to `sources`. New card: copy `assets/<brick>.md` to `vault/0 Library/Techniques/<Brick>/<Generic name>.md` and fill it.
6. In the reading note's Techniques table, link each carded technique to its card.
7. Reply: the triage table, the cards created and the cards updated.

## Rules

- Fill only from the reading note, or the PDF page it cites. Every fact gets its source and page.
- No outside knowledge, no advice on how to use the technique.
- Title: the name practitioners use ("Volatility targeting"), never a paper name. Other names go in `aliases`.
- Cite sources as first author and year ("Moskowitz 2012"), never as initials.
- Parameters and variants go inside the card, not in a new card.
- Length: "How it works" under 120 words; under 200 words per source in "What the sources say". Count them before you finish.
- Evidence: 3 or 4 results at most, the ones about this technique. The reading note holds the rest.
- More than one fact from a source under a heading: one sub-bullet per fact, under every heading.
- `tested_on`: asset classes from `vault/Toolbox/Tags.md` only (`[equities]`, `[multi-asset]`), never tickers or other words.
- Keep the template layout, a human reads these cards too: summary callout; "How it works" describes the family of the technique in general terms, one bullet per field, no page refs (a paper's own algorithm goes under that source's Parameters, as a variant, so the next paper on the same idea fits the same card); every source-specific fact goes under "What the sources say", one bullet per source in bold, one sub-bullet per result, with its page.
- Write in English. Never use a long dash.
