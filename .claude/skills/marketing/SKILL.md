---
name: ckm:marketing
description: "Marketing intelligence for AI builders: copywriting frameworks (AIDA, PAS, FAB), headlines and CTAs, content marketing and SEO, editorial calendars, email sequences and subject lines, social media posts per platform, and paid ad campaigns. Actions: write, plan, create, draft, review, optimize, audit marketing copy and campaigns. Channels: blog, email, newsletter, Instagram, Facebook, LinkedIn, X/Twitter, TikTok, YouTube, Google Ads, Meta Ads. Topics: copywriting, value proposition, funnel, conversion, SEO, keywords, meta tags, content calendar, A/B testing, metrics."
argument-hint: "[copywriting|content-seo|email|social-ads|campaign] [context]"
license: MIT
metadata:
  author: rahajivkarimchegue
  version: "1.0.0"
---

# Marketing

End-to-end marketing intelligence: copywriting, content & SEO, email, social & ads, and campaign strategy.

<args>$ARGUMENTS</args>

## When to Use

- Writing or reviewing marketing copy (headlines, value props, CTAs, ad copy)
- Planning content marketing and editorial calendars with SEO in mind
- Building email sequences, newsletters, and subject lines
- Creating platform-specific social posts and paid ad campaigns
- Designing a full-funnel campaign with goals, channels, and metrics

## Quick Start

**Easiest:** just type `/marketing` and say what you want in plain language
("write 3 subject lines for a cart email", "plan a launch campaign for X").
The skill runs everything below for you.

**One command for the terminal — `mkt`** (run from the repo root):
```bash
./mkt search "urgency cta"          # search; domain auto-detected
./mkt search "linkedin" channel     # search one domain (copy|channel|email|seo)
./mkt brief "TaskFlow" "signups" "SMB founders"   # generate a campaign brief
./mkt domains                       # list searchable domains
./mkt help                          # show all commands
```

Tip: make it even shorter with an alias → `alias mkt='./mkt'`, then `mkt search "..."`.

## Sub-skill Routing

Parse the first word of `$ARGUMENTS` and load the matching reference. If omitted,
auto-detect from the request (keywords: "headline/copy" → copywriting,
"blog/seo/keyword" → content-seo, "email/newsletter/subject" → email,
"post/ad/instagram/campaign budget" → social-ads, "funnel/launch/strategy" → campaign).

| Subcommand | Focus | Reference |
|------------|-------|-----------|
| `copywriting` | Frameworks, headlines, value props, CTAs, voice | `references/copywriting.md` |
| `content-seo` | Blog strategy, keywords, on-page SEO, meta tags | `references/content-seo.md` |
| `email` | Sequences, subject lines, automation, deliverability | `references/email-marketing.md` |
| `social-ads` | Per-platform posts, hooks, paid ad campaigns | `references/social-and-ads.md` |
| `campaign` | Funnels, launch planning, channel mix, metrics | `references/campaign-strategy.md` |
| `calendar` | Editorial / content calendar planning | `references/editorial-calendar.md` |

## References (Knowledge Base)

| Topic | File |
|-------|------|
| Copywriting Frameworks | `references/copywriting.md` |
| Content & SEO | `references/content-seo.md` |
| Editorial Calendar | `references/editorial-calendar.md` |
| Email Marketing | `references/email-marketing.md` |
| Social & Paid Ads | `references/social-and-ads.md` |
| Campaign Strategy & Metrics | `references/campaign-strategy.md` |

## Data (Searchable)

| Dataset | Contents |
|---------|----------|
| `data/copy_formulas.csv` | 20+ copywriting formulas with templates and use cases |
| `data/channels.csv` | Channel specs: format, audience, tone, best-for |
| `data/email_sequences.csv` | Email sequence blueprints (welcome, nurture, cart, winback) |
| `data/seo_checklist.csv` | On-page and technical SEO checklist items |

## CLI (`mkt`)

One dependency-free command. Launcher: `./mkt` (repo root) → `mkt.py`.

| Command | Purpose |
|---------|---------|
| `mkt search "<query>" [domain]` | Keyword search over the datasets (domain auto-detected if omitted) |
| `mkt brief "<product>" "<goal>" "<audience>"` | Generate a campaign brief from `templates/campaign-brief.md` |
| `mkt domains` | List searchable domains (copy, channel, email, seo) |
| `mkt help` | Show all commands |

## Templates

| Template | Purpose |
|----------|---------|
| `templates/campaign-brief.md` | One-page campaign brief (goal, audience, channels, KPIs) |
| `templates/content-calendar.md` | Monthly editorial calendar grid |
| `templates/email-sequence.md` | Multi-step email sequence skeleton |

## Workflow

1. Identify the marketing job (copy, content, email, social/ads, or full campaign).
2. Route to the matching reference and search `data/` for relevant formulas/specs.
3. Anchor copy in brand voice — if a `brand` skill or `docs/brand-guidelines.md` exists, load it first.
4. Draft using the framework templates, then self-review against the checklist in the reference.
5. For campaigns, fill `templates/campaign-brief.md` and define KPIs before writing creative.

## Cross-skill Tips

- For **visual assets** (banners, social images, logos), route to `design` / `banner-design`.
- For **brand voice and messaging architecture**, route to `brand`.
- For **landing page copy + UI**, pair this skill with `ui-ux-pro-max` (landing domain).
