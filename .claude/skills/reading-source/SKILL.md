---
name: reading-source
description: Read one source and write a faithful reading note in the vault library: what the source says, with page references, and nothing else (no ideas, no opinions, no derivations). Research papers only for now. Use whenever the user asks to read, summarise, take notes on, "ficher", or add to the library a paper, a PDF, an SSRN or arXiv link, even if they do not say "reading note".
---

# Reading a source

1. Identify the source type. Research paper: read `reference/paper.md`. Any other type: stop and tell the user it is not supported yet.
2. Look for an existing note on the same source in `vault/0 Library/Notes/`. If one exists, stop and give its path.
3. Save the PDF as `vault/0 Library/Sources/<Year> - <Authors> - <Title>.pdf`.
4. Read the whole source as `reference/paper.md` says.
5. Copy `assets/paper-note-template.md` to `vault/0 Library/Notes/<Year> - <Authors> - <Title>.md` and fill it.
6. Run the checklist at the end of `reference/paper.md`. Fix what fails.
7. Reply to the user: note path, the five summary bullets, inconsistencies found.

## Rules

- Write only what the source says. Every fact gets a page, table or figure.
- No opinion, no idea, no derivation, no outside knowledge.
- No mechanism in the source: write "Not stated by the authors."
- Mark every value read from a chart with ≈.
- Write the note in English. Never use a long dash.
