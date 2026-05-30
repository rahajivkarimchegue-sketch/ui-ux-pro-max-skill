#!/usr/bin/env python3
"""Generate a campaign brief from templates/campaign-brief.md.

Fills the {{PLACEHOLDER}} tokens from CLI flags and prints the result (or
writes it to --out). Unfilled tokens are left as TODO markers so you can see
what still needs deciding.

Usage:
    python3 generate-brief.py --product "TaskFlow" --goal "trial signups" \
        --audience "SMB founders" --channels "Meta Ads, Email, LinkedIn" \
        --target "500 signups in 30 days" --out brief.md
"""
import argparse
import os
import sys

TEMPLATE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "templates", "campaign-brief.md"
)


def main():
    p = argparse.ArgumentParser(description="Generate a campaign brief.")
    p.add_argument("--product", required=True, help="product / brand name")
    p.add_argument("--goal", required=True, help="primary goal (e.g. signups, sales)")
    p.add_argument("--audience", required=True, help="target audience / ICP")
    p.add_argument("--target", default="", help="measurable target metric")
    p.add_argument("--deadline", default="", help="campaign deadline")
    p.add_argument("--offer", default="", help="the offer")
    p.add_argument("--value-prop", default="", help="one-line value proposition")
    p.add_argument("--channels", default="", help="comma-separated channels (2-3)")
    p.add_argument("--budget", default="", help="total budget")
    p.add_argument("--out", default="", help="write to file instead of stdout")
    args = p.parse_args()

    if not os.path.exists(TEMPLATE):
        print(f"Template not found: {TEMPLATE}", file=sys.stderr)
        return 1

    with open(TEMPLATE, encoding="utf-8") as f:
        text = f.read()

    channels = [c.strip() for c in args.channels.split(",") if c.strip()]
    mapping = {
        "CAMPAIGN_NAME": f"{args.product} — {args.goal}",
        "GOAL": args.goal,
        "TARGET": args.target,
        "DEADLINE": args.deadline,
        "AUDIENCE": args.audience,
        "OFFER": args.offer,
        "VALUE_PROP": args.value_prop,
        "BUDGET": args.budget,
        "KPI_PRIMARY": args.goal,
        "CHANNEL_1": channels[0] if len(channels) > 0 else "",
        "CHANNEL_2": channels[1] if len(channels) > 1 else "",
        "CHANNEL_3": channels[2] if len(channels) > 2 else "",
    }

    for key, val in mapping.items():
        text = text.replace("{{" + key + "}}", val if val else f"TODO: {key.lower()}")

    # Any remaining tokens → TODO markers.
    import re
    text = re.sub(r"\{\{([A-Z_]+)\}\}", lambda m: f"TODO: {m.group(1).lower()}", text)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Brief written to {args.out}")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
