#!/usr/bin/env python3
"""Marketing knowledge base search.

Lightweight keyword search over the marketing CSV datasets. No external
dependencies (mirrors the ui-ux-pro-max search ethos).

Usage:
    python3 search.py "<query>" [--domain copy|channel|email|seo] [-n N]

Domains:
    copy     copy_formulas.csv    persuasion frameworks + templates
    channel  channels.csv         platform/channel specs (organic + paid)
    email    email_sequences.csv  email sequence blueprints
    seo      seo_checklist.csv    on-page / technical / content SEO items

If --domain is omitted, all datasets are searched and the top matches across
domains are returned.
"""
import argparse
import csv
import os
import re
import sys

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")

DOMAINS = {
    "copy": "copy_formulas.csv",
    "channel": "channels.csv",
    "email": "email_sequences.csv",
    "seo": "seo_checklist.csv",
}


def tokenize(text):
    return re.findall(r"[a-z0-9]+", text.lower())


def load(domain):
    path = os.path.join(DATA_DIR, DOMAINS[domain])
    if not os.path.exists(path):
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def score(row, terms):
    """Score a row: exact term hits in any field, with a small boost for
    matches in the first (name/identifier) column."""
    fields = list(row.items())
    blob = " ".join(v or "" for _, v in fields).lower()
    blob_tokens = set(tokenize(blob))
    first_val = (fields[0][1] or "").lower() if fields else ""
    s = 0.0
    for t in terms:
        if t in blob_tokens:
            s += 1.0
        elif t in blob:  # partial / substring match
            s += 0.5
        if t in first_val:
            s += 1.0  # boost identifier matches
    return s


def search(query, domain=None, n=5):
    terms = tokenize(query)
    domains = [domain] if domain else list(DOMAINS.keys())
    results = []
    for d in domains:
        for row in load(d):
            s = score(row, terms)
            if s > 0:
                results.append((s, d, row))
    results.sort(key=lambda x: x[0], reverse=True)
    return results[:n]


def fmt(domain, row):
    # Show identifier + the most descriptive fields, skip empty values.
    items = [(k, v) for k, v in row.items() if v and v != "..."]
    head = items[0][1] if items else "(result)"
    lines = [f"[{domain}] {head}"]
    for k, v in items[1:]:
        lines.append(f"  - {k}: {v}")
    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser(description="Search the marketing knowledge base.")
    p.add_argument("query", help="search terms")
    p.add_argument("--domain", choices=list(DOMAINS.keys()), help="restrict to one dataset")
    p.add_argument("-n", type=int, default=5, help="max results (default 5)")
    args = p.parse_args()

    hits = search(args.query, args.domain, args.n)
    if not hits:
        print(f'No matches for "{args.query}"'
              + (f" in domain {args.domain}." if args.domain else "."))
        print("Domains: " + ", ".join(DOMAINS.keys()))
        return 0

    for _, domain, row in hits:
        print(fmt(domain, row))
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
