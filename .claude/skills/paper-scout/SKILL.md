---
name: paper-scout
description: Find trading-strategy papers on arXiv and OpenAlex, triage them from title and abstract, and download the open-access PDFs the user picks into the vault library. Use whenever the user asks to find, search, look for, discover or import new papers or research on a strategy family, a market or a technique.
---

# Paper scout

1. Pick the queries: the user's topic, else `reference/queries.md`.
2. For each query, run `python3 .claude/skills/paper-scout/scripts/search.py "<query>"` from the repository root. It skips papers already in Sources or in the scout log.
3. Triage every candidate with `reference/criteria.md`: keep, maybe or reject, with a one-line reason. When the abstract is unclear, open the PDF and read the introduction.
4. Show the user the keep and maybe papers, best first, 10 at most: title, year, one-line reason. Wait for their picks. If nobody is there, take the keep papers only, 5 at most.
5. Download each pick with `scripts/fetch.py` (`--url`, `--year`, `--authors` as full names separated by ";", `--title`).
6. A pick with no PDF, or "NOT A PDF": list it with its landing link for a manual download.
7. Append every candidate you triaged to `vault/0 Library/Inbox/Scout log.md`: `- <date> | <id> | <verdict> | <title> | <reason>`.
8. Reply: files saved, papers to download by hand, number rejected.

## Rules

- Only arXiv and OpenAlex. Never Google Scholar; never scrape SSRN.
- Do not read papers in depth or write notes: that is the Reader's job.
- Write only in `vault/0 Library/Sources/` and in the scout log.
- Never use a long dash.
