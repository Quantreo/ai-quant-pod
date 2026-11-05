"""Download one open-access PDF into vault/0 Library/Sources with the desk's file name.

Usage:
  python fetch.py --url URL --year 2012 --authors "Tobias Moskowitz; Yao Hua Ooi; Lasse Pedersen" --title "Time series momentum"

Name: "<Year> - <Last names, up to 3, then et al> - <Title>.pdf". Checks the file is a real PDF. Never overwrites.
Run from the repository root.
"""
import argparse, re, ssl, sys, urllib.request
from pathlib import Path

DEST = Path("vault/0 Library/Sources")
UA = {"User-Agent": "Mozilla/5.0 (quant-desk-scout/0.1)"}


def _ssl_context():
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        return ssl.create_default_context()


CTX = _ssl_context()


def last_name(full):
    full = full.strip()
    if "," in full:
        return full.split(",")[0].strip()
    return full.split()[-1] if full else ""


def file_name(year, authors, title):
    names = [last_name(a) for a in re.split(r";|\band\b", authors) if a.strip()]
    who = " ".join(names[:3]) + (" et al" if len(names) > 3 else "")
    title = re.sub(r'[\\/:*?"<>|]', "", " ".join(title.split()))
    title = title.rstrip(".")
    if len(title) > 90:
        title = title[:90].rsplit(" ", 1)[0]
    return f"{year} - {who} - {title}.pdf"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", required=True)
    ap.add_argument("--year", required=True)
    ap.add_argument("--authors", required=True, help="full names separated by ';'")
    ap.add_argument("--title", required=True)
    a = ap.parse_args()
    path = DEST / file_name(a.year, a.authors, a.title)
    if path.exists():
        sys.exit(f"EXISTS {path}")
    try:
        with urllib.request.urlopen(urllib.request.Request(a.url, headers=UA), timeout=60, context=CTX) as r:
            data = r.read()
    except urllib.error.URLError as e:
        if isinstance(getattr(e, "reason", None), ssl.SSLCertVerificationError):
            sys.exit("SSL certificate error. Fix: python3 -m pip install certifi (or run 'Install Certificates.command' from your Python folder).")
        sys.exit(f"FAILED {a.url}: {e}")
    if not data.startswith(b"%PDF"):
        sys.exit(f"NOT A PDF {a.url} (probably a landing page or a paywall): download it by hand")
    DEST.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    print(f"SAVED {path} ({len(data) // 1024} KB)")


if __name__ == "__main__":
    main()
