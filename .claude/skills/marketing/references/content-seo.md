# Content Marketing & SEO

Blog strategy, keyword research, on-page SEO, and technical fundamentals.

## Content Strategy

### Topic Clusters (pillar + spokes)
- **Pillar page:** broad, high-volume term ("email marketing"), 2,000+ words, links to spokes.
- **Cluster posts:** specific long-tail terms ("email subject line length"), each links back to the pillar.
- Internal linking between cluster and pillar is what compounds rankings.

### Content Types by Funnel Stage
| Stage | Intent | Formats |
|-------|--------|---------|
| TOFU (awareness) | informational | how-to guides, listicles, glossary, explainers |
| MOFU (consideration) | comparison | "X vs Y", alternatives, case studies, templates |
| BOFU (decision) | transactional | pricing, demos, ROI calculators, product pages |

## Keyword Research

1. Seed terms → expand with "People also ask", autocomplete, competitor headers.
2. Classify by **search intent**: informational, commercial, transactional, navigational.
3. Prioritize by: relevance × (volume / difficulty) × business value.
4. Target **one primary keyword + 2–4 secondary** per page. Don't keyword-stuff.

### Intent → Page Type
- "how / what / why / guide" → blog/guide
- "best / top / vs / alternative / review" → comparison or listicle
- "buy / pricing / [brand] + [feature]" → product/landing page

## On-Page SEO Checklist

| Element | Rule |
|---------|------|
| Title tag | ≤ 60 chars, primary keyword near front, compelling |
| Meta description | ≤ 155 chars, benefit + keyword + CTA (not a ranking factor but drives CTR) |
| URL slug | short, lowercase, hyphenated, keyword-rich, no stop words |
| H1 | one per page, contains primary keyword |
| H2/H3 | descriptive, include secondary keywords + "People also ask" questions |
| First 100 words | state the answer; include primary keyword naturally |
| Image alt text | descriptive, keyword when relevant |
| Internal links | 2–5 to related pillar/cluster pages with descriptive anchors |
| Schema | Article/FAQ/Product/Breadcrumb structured data |

> Full list: `python3 scripts/search.py "<topic>" --domain seo`

## Meta Tag Templates

```html
<title>Primary Keyword: Benefit | Brand</title>
<meta name="description" content="Action verb + outcome in ≤155 chars. Includes primary keyword and a soft CTA.">
<meta property="og:title" content="Shareable, curiosity-driven version">
<meta property="og:description" content="One-line hook for social previews">
<meta property="og:image" content="https://.../share-1200x630.png">
```

## Title Tag Formulas
- "[Primary Keyword]: [Benefit/Number] [Year]"
- "[Number] [Adjective] [Keyword] to [Outcome]"
- "[Keyword] — A Complete Guide for [Audience]"

## Content Quality (E-E-A-T)
Experience, Expertise, Authoritativeness, Trust:
- Show first-hand experience (screenshots, original data, examples).
- Cite credible sources; add author bio with credentials.
- Keep content fresh — review and update timestamps.
- Answer the query fully and concisely above the fold.

## Technical Fundamentals
- Mobile-first, fast (Core Web Vitals: LCP < 2.5s, INP < 200ms, CLS < 0.1).
- Clean, crawlable URLs; XML sitemap; logical internal linking.
- One canonical URL per piece of content; fix duplicate/thin pages.
- HTTPS, no broken links, descriptive 404s.

## Distribution (don't just publish)
Repurpose each post into: email newsletter, 3–5 social posts, a thread, a short video script, and an answer on a relevant community/Q&A site.

## Self-Review Checklist
1. Does the page satisfy the searcher's intent better than page-1 competitors?
2. Title + meta optimized for **clicks**, not just keywords?
3. One clear next step (internal link or CTA)?
4. Original value (data, examples, opinion) vs rephrased competitors?
5. Skimmable: short paragraphs, descriptive subheads, lists, visuals?
