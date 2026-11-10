"""
Where a strategy lives in the vault: one folder per strategy, inside the folder of its status.

    vault/2 Strategies/<Pipeline | Passed | Killed>/<Name>/<Name>.md

The folder holds the strategy and everything made for it. <Name>.md is the index (frontmatter: status, version;
one row per seat); each seat writes its own section file: Pass 1.md, Review.md, Changelog.md, Data check.md,
Build.md, Pass 2.md, Red team.md, Test.md. Older strategies may hold everything in <Name>.md. Changing status is
moving the folder.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STRATEGIES = ROOT / "vault" / "2 Strategies"


def sheet_path(name):
    """The sheet of a strategy, whatever its status. Raises if there is none or more than one."""
    found = list(STRATEGIES.glob(f"*/{name}/{name}.md"))
    if len(found) != 1:
        raise FileNotFoundError(f"{len(found)} sheets named {name!r} under {STRATEGIES}")
    return found[0]


def strategy_folder(name):
    return sheet_path(name).parent


SECTIONS = ["Pass 1", "Review", "Changelog", "Data check", "Build", "Pass 2", "Red team", "Test"]


def sheet_text(name):
    """The whole strategy as one text: the index followed by its section files, in pipeline order."""
    index = sheet_path(name)
    parts = [index.read_text()]
    for sec in SECTIONS:
        f = index.parent / f"{sec}.md"
        if f.exists():
            parts.append(f.read_text())
    return "\n\n".join(parts)
