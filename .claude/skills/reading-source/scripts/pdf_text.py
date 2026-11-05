"""
A paper as text, page by page, for the Reader: text costs a few times fewer tokens than page images.

    poetry run python .claude/skills/reading-source/scripts/pdf_text.py "<pdf>"              # text + list of chart pages
    poetry run python .claude/skills/reading-source/scripts/pdf_text.py "<pdf>" --png 7,12   # those pages as images

Writes results/_pdf/<stem>.txt with a line "=== PDF page N ===" before each page, and prints the page count and
the pages that hold a figure (an embedded image, or a "Figure"/"Fig." caption), the only ones worth looking at as
images. --png renders pages to results/_pdf/<stem> p<N>.png (130 dpi), to open with the Read tool.
Needs pymupdf (in pyproject); no poppler.
"""
import argparse, re
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / "results" / "_pdf"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("--png", help="comma-separated PDF page numbers to render as images")
    a = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(a.pdf)
    stem = Path(a.pdf).stem[:80]
    if a.png:
        for n in [int(x) for x in a.png.split(",")]:
            p = OUT / f"{stem} p{n}.png"
            doc[n - 1].get_pixmap(dpi=130).save(p)
            print(p)
        return
    parts, figs = [], []
    for i, page in enumerate(doc, start=1):
        t = page.get_text()
        parts.append(f"=== PDF page {i} ===\n{t.strip()}\n")
        if page.get_images() or re.search(r"^\s*(Figure|Fig\.)\s*\d", t, re.M):
            figs.append(i)
    txt = OUT / f"{stem}.txt"
    txt.write_text("\n".join(parts))
    n_chars = sum(len(x) for x in parts)
    print(f"{txt}\n{len(doc)} pages, {n_chars:,} characters (about {n_chars // 4:,} tokens)\npages with a figure: {figs or 'none'}")


if __name__ == "__main__":
    main()
