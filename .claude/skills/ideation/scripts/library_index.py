"""Compact index of the desk library, for the Ideator. Standard library only.

Usage (from the repository root):
  python .claude/skills/ideation/scripts/library_index.py
  python .claude/skills/ideation/scripts/library_index.py --family carry
  python .claude/skills/ideation/scripts/library_index.py --asset fx --section notes,cards

Prints, as short markdown:
  notes       tags and the five summary bullets of each reading note
  cards       title, brick, one-line summary, tested_on and sources of each technique card
  journal     title, status and family of each Idea Journal entry
  strategies  each strategy sheet and its status (folder)
--family and --horizon filter notes only (cards are bricks, reusable in any family). --asset filters notes and cards; --brick filters cards. Journal and strategies are always listed in full,
so that the Ideator never proposes an idea already there.
"""
import argparse, re
from pathlib import Path

VAULT = Path("vault")
NOTES = VAULT / "0 Library" / "Notes"
CARDS = VAULT / "0 Library" / "Techniques"
JOURNAL = VAULT / "1 Ideas" / "Idea Journal.md"
STRATS = VAULT / "2 Strategies"


def frontmatter(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    fm = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip().strip('"')
    return fm


def as_list(value):
    return [x.strip() for x in value.strip("[]").split(",") if x.strip()]


def notes(args):
    out = ["## Reading notes", ""]
    for p in sorted(NOTES.glob("*.md")):
        t = p.read_text()
        fm = frontmatter(t)
        tags = as_list(fm.get("tags", ""))
        if args.family and args.family not in tags: continue
        if args.asset and args.asset not in tags: continue
        if args.horizon and args.horizon not in tags: continue
        s = re.search(r"## Summary\n(.*?)\n(?:Page numbers|## )", t, re.S)
        bullets = [l for l in (s.group(1).splitlines() if s else []) if l.startswith("- ")]
        out.append(f"### [[{p.stem}]]")
        out.append(f"tags: {', '.join(tags)} | tier {fm.get('tier', '?')} | read {fm.get('read', '?')}")
        out += bullets or ["- (no summary)"]
        out.append("")
    return out


def cards(args):
    out = ["## Technique cards", ""]
    for p in sorted(CARDS.glob("*/*.md")):
        t = p.read_text()
        fm = frontmatter(t)
        brick = fm.get("brick") or ("diagnostic/" + fm.get("kind", "?"))
        tested = as_list(fm.get("tested_on", ""))
        if args.brick and args.brick not in brick: continue
        if args.asset and tested and args.asset not in tested and "multi-asset" not in tested: continue
        summary = re.search(r"> \[!summary\]\n> (.*)", t)
        sources = sorted(set(re.findall(r"^- \*\*([^*]+ \d{4})\*\*", t, re.M)))
        out.append(f"- [[{p.stem}]] ({brick}; tested on {', '.join(tested) or '-'}; {', '.join(sources) or '-'}): "
                   f"{summary.group(1).strip() if summary else ''}")
    return out + [""]


def journal(args):
    out = ["## Idea Journal", ""]
    if not JOURNAL.exists():
        return out + ["(no journal)", ""]
    blocks = re.split(r"^### ", JOURNAL.read_text(), flags=re.M)[1:]
    for b in blocks:
        lines = [l for l in b.splitlines() if l.strip()]
        title = lines[0]
        meta = next((l for l in lines[1:] if "`" in l and "**" in l), "")
        fam = re.search(r"`([^`]+)`", meta)
        status = re.search(r"\*\*([^*]+)\*\*", meta)
        reason = meta.split("**")[-1].strip(" :·") if status else ""
        out.append(f"- {title} | {fam.group(1) if fam else '?'} | {status.group(1) if status else '?'}"
                   + (f" | {reason}" if reason and not reason.startswith("revisit") else ""))
    return out + [""]


def strategies(args):
    out = ["## Strategy sheets", ""]
    for p in sorted(STRATS.glob("*/*/*.md")):                     # one folder per strategy: <status>/<Name>/<Name>.md
        if p.stem != p.parent.name: continue
        out.append(f"- [[{p.stem}]] | {p.parent.parent.name.lower()} | family {frontmatter(p.read_text()).get('family', '?')}")
    return out + [""]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--family"); ap.add_argument("--asset"); ap.add_argument("--horizon"); ap.add_argument("--brick")
    ap.add_argument("--section", default="notes,cards,journal,strategies")
    a = ap.parse_args()
    parts = {"notes": notes, "cards": cards, "journal": journal, "strategies": strategies}
    for s in a.section.split(","):
        print("\n".join(parts[s.strip()](a)))


if __name__ == "__main__":
    main()
