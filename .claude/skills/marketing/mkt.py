#!/usr/bin/env python3
"""mkt — the single marketing CLI.

One memorable command with short subcommands. No external dependencies.

    mkt search "<query>" [domain]     search the knowledge base
    mkt brief  "<product>" "<goal>" "<audience>"   generate a campaign brief
    mkt domains                       list searchable domains
    mkt help                          show this help

Domains for search: copy, channel, email, seo (auto-detected if omitted).

Run it via the repo-root launcher:  ./mkt search "urgency cta"
or directly:                        python3 .claude/skills/marketing/mkt.py ...
"""
import csv
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(HERE, "data")
TEMPLATES_DIR = os.path.join(HERE, "templates")

DOMAINS = {
    "copy": "copy_formulas.csv",
    "channel": "channels.csv",
    "email": "email_sequences.csv",
    "seo": "seo_checklist.csv",
}


# ---------------------------------------------------------------- search ----
def tokenize(text):
    return re.findall(r"[a-z0-9]+", text.lower())


def load(domain):
    path = os.path.join(DATA_DIR, DOMAINS[domain])
    if not os.path.exists(path):
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def score(row, terms):
    fields = list(row.items())
    blob = " ".join(v or "" for _, v in fields).lower()
    blob_tokens = set(tokenize(blob))
    first_val = (fields[0][1] or "").lower() if fields else ""
    s = 0.0
    for t in terms:
        if t in blob_tokens:
            s += 1.0
        elif t in blob:
            s += 0.5
        if t in first_val:
            s += 1.0
    return s


def cmd_search(args):
    if not args:
        print('Usage: mkt search "<query>" [domain]')
        return 1
    query = args[0]
    domain = args[1] if len(args) > 1 else None
    if domain and domain not in DOMAINS:
        print(f"Unknown domain '{domain}'. Choose: {', '.join(DOMAINS)}")
        return 1

    n = 5
    terms = tokenize(query)
    domains = [domain] if domain else list(DOMAINS.keys())
    results = []
    for d in domains:
        for row in load(d):
            s = score(row, terms)
            if s > 0:
                results.append((s, d, row))
    results.sort(key=lambda x: x[0], reverse=True)
    results = results[:n]

    if not results:
        print(f'No matches for "{query}". Domains: {", ".join(DOMAINS)}')
        return 0
    for _, d, row in results:
        items = [(k, v) for k, v in row.items() if v and v != "..."]
        head = items[0][1] if items else "(result)"
        print(f"[{d}] {head}")
        for k, v in items[1:]:
            print(f"  - {k}: {v}")
        print()
    return 0


# ----------------------------------------------------------------- brief ----
def cmd_brief(args):
    if len(args) < 3:
        print('Usage: mkt brief "<product>" "<goal>" "<audience>"')
        return 1
    product, goal, audience = args[0], args[1], args[2]
    template = os.path.join(TEMPLATES_DIR, "campaign-brief.md")
    with open(template, encoding="utf-8") as f:
        text = f.read()
    mapping = {
        "CAMPAIGN_NAME": f"{product} — {goal}",
        "GOAL": goal,
        "AUDIENCE": audience,
        "KPI_PRIMARY": goal,
    }
    for key, val in mapping.items():
        text = text.replace("{{" + key + "}}", val)
    text = re.sub(r"\{\{([A-Z_]+)\}\}", lambda m: f"TODO: {m.group(1).lower()}", text)
    print(text)
    return 0


# ------------------------------------------------------------------ misc ----
def cmd_domains(_args):
    print("Searchable domains:")
    for d, f in DOMAINS.items():
        print(f"  {d:8s} → data/{f}")
    return 0


def cmd_help(_args):
    print(__doc__)
    return 0


COMMANDS = {
    "search": cmd_search,
    "brief": cmd_brief,
    "domains": cmd_domains,
    "help": cmd_help,
    "-h": cmd_help,
    "--help": cmd_help,
}


def main(argv):
    if not argv:
        return cmd_help([])
    cmd, rest = argv[0], argv[1:]
    handler = COMMANDS.get(cmd)
    if not handler:
        print(f"Unknown command '{cmd}'. Try: {', '.join(k for k in COMMANDS if not k.startswith('-'))}")
        return 1
    return handler(rest)


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except BrokenPipeError:
        # Output was piped into a command (e.g. `| head`) that closed early.
        try:
            sys.stdout.close()
        finally:
            sys.exit(0)
