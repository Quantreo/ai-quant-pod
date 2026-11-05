"""Search arXiv (q-fin) and OpenAlex for papers. Standard library only.

Usage:
  python search.py "time series momentum" [--source arxiv|openalex|all] [--max 25] [--since 2010]

Prints one JSON object per candidate (source, id, title, authors, year, abstract, pdf_url, landing_url).
Skips papers already in vault/0 Library/Sources or already listed in vault/0 Library/Inbox/Scout log.md.
Run from the repository root.
"""
import argparse, json, re, ssl, sys, time, urllib.parse, urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

SOURCES_DIR = Path("vault/0 Library/Sources")
LOG_FILE = Path("vault/0 Library/Inbox/Scout log.md")
UA = {"User-Agent": "quant-desk-scout/0.1 (research; contact via repository owner)"}


def _ssl_context():
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        return ssl.create_default_context()


CTX = _ssl_context()


def get(url):
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=30, context=CTX) as r:
            return r.read()
    except urllib.error.URLError as e:
        if isinstance(getattr(e, "reason", None), ssl.SSLCertVerificationError):
            sys.exit("SSL certificate error. Fix: python3 -m pip install certifi (or run 'Install Certificates.command' from your Python folder).")
        raise


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def known():
    titles, ids = set(), set()
    if SOURCES_DIR.exists():
        for p in SOURCES_DIR.glob("*.pdf"):
            parts = p.stem.split(" - ", 2)
            titles.add(norm(parts[-1]))
    if LOG_FILE.exists():
        ids |= set(re.findall(r"(arxiv:\S+?|openalex:W\d+)(?=\s|\|)", LOG_FILE.read_text()))
    return titles, ids


def arxiv(query, n, since):
    cats = "(cat:q-fin.TR OR cat:q-fin.PM OR cat:q-fin.ST OR cat:q-fin.GN)"
    q = f'{cats} AND all:"{query}"'
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(
        {"search_query": q, "start": 0, "max_results": n, "sortBy": "relevance"})
    return parse_arxiv(get(url), since)


def parse_arxiv(xml_bytes, since):
    ns = {"a": "http://www.w3.org/2005/Atom"}
    out = []
    for e in ET.fromstring(xml_bytes).findall("a:entry", ns):
        aid = e.findtext("a:id", "", ns).rsplit("/abs/", 1)[-1]
        aid = re.sub(r"v\d+$", "", aid)
        year = int(e.findtext("a:published", "0000", ns)[:4])
        if year < since:
            continue
        pdf = next((l.get("href") for l in e.findall("a:link", ns) if l.get("title") == "pdf"), f"https://arxiv.org/pdf/{aid}")
        out.append({"source": "arxiv", "id": f"arxiv:{aid}",
                    "title": " ".join(e.findtext("a:title", "", ns).split()),
                    "authors": [a.findtext("a:name", "", ns) for a in e.findall("a:author", ns)],
                    "year": year, "abstract": " ".join(e.findtext("a:summary", "", ns).split()),
                    "pdf_url": pdf, "landing_url": f"https://arxiv.org/abs/{aid}"})
    return out


def openalex(query, n, since):
    url = "https://api.openalex.org/works?" + urllib.parse.urlencode({
        "search": query, "per-page": n,
        "filter": f"open_access.is_oa:true,from_publication_date:{since}-01-01"})
    return parse_openalex(json.loads(get(url)))


def parse_openalex(data):
    out = []
    for w in data.get("results", []):
        inv = w.get("abstract_inverted_index") or {}
        words = sorted((i, k) for k, idx in inv.items() for i in idx)
        loc = w.get("best_oa_location") or {}
        out.append({"source": "openalex", "id": "openalex:" + w["id"].rsplit("/", 1)[-1],
                    "title": w.get("display_name") or "",
                    "authors": [a["author"]["display_name"] for a in w.get("authorships", [])],
                    "year": w.get("publication_year"), "abstract": " ".join(k for _, k in words),
                    "pdf_url": loc.get("pdf_url"),
                    "landing_url": loc.get("landing_page_url") or w.get("doi") or w["id"],
                    "doi": w.get("doi")})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query")
    ap.add_argument("--source", default="all", choices=["arxiv", "openalex", "all"])
    ap.add_argument("--max", type=int, default=25)
    ap.add_argument("--since", type=int, default=2005)
    a = ap.parse_args()
    titles, ids = known()
    found = []
    if a.source in ("arxiv", "all"):
        found += arxiv(a.query, a.max, a.since)
        time.sleep(3)  # arXiv asks for 3 seconds between calls
    if a.source in ("openalex", "all"):
        found += openalex(a.query, a.max, a.since)
    seen = set()
    for c in found:
        key = norm(c["title"])
        if c["id"] in ids or key in titles or key in seen:
            continue
        seen.add(key)
        c["abstract"] = c["abstract"][:1500]
        print(json.dumps(c, ensure_ascii=False))


if __name__ == "__main__":
    main()
