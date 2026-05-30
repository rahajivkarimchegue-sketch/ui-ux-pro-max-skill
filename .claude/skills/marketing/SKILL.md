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

**Search the marketing knowledge base (formulas, channels, sequences, SEO):**
```bash
python3 .claude/skills/marketing/scripts/search.py "urgency cta" --domain copy
python3 .claude/skills/marketing/scripts/search.py "welcome sequence" --domain email
python3 .claude/skills/marketing/scripts/search.py "linkedin b2b" --domain channel
python3 .claude/skills/marketing/scripts/search.py "on-page title tag" --domain seo
```

**Generate a campaign brief from a template:**
```bash
python3 .claude/skills/marketing/scripts/generate-brief.py --product "TaskFlow" --goal "signups" --audience "SMB founders"
```

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

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/search.py` | Keyword search over the marketing datasets (no dependencies) |
| `scripts/generate-brief.py` | Generate a campaign brief from `templates/campaign-brief.md` |

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
