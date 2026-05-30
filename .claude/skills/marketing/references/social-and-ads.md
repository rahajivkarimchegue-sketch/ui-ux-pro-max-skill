# Social Media & Paid Ads

Per-platform organic posts, hooks, and paid ad campaign structure.

## Platform Cheat Sheet

> Specs/tone per channel: `python3 scripts/search.py "<platform>" --domain channel`

| Platform | Best content | Tone | Hook window | Notes |
|----------|--------------|------|-------------|-------|
| Instagram | Reels, carousels, photos | visual, aspirational | 1–2s | Carousels for saves; Reels for reach |
| TikTok | Short native video | raw, fast, trend-aware | <1s | Hook + payoff fast; ride sounds/trends |
| LinkedIn | Text posts, docs, articles | professional, insightful | first line | Hook before "...see more"; B2B |
| X / Twitter | Threads, hot takes, replies | concise, opinionated | first tweet | Thread = hook tweet + value + CTA |
| YouTube | Long video + Shorts | educational/entertaining | 15s | Title + thumbnail drive CTR |
| Facebook | Community, groups, video | conversational | first line | Older skew; groups still strong |
| Pinterest | Vertical pins, how-tos | inspirational | image | Evergreen search traffic |

## Organic Post Anatomy
```
Hook (stop the scroll — bold claim, question, or pattern interrupt)
Value (story, steps, insight — deliver on the hook)
Engagement prompt (question / "save this")
CTA (follow, link in bio, comment a keyword)
```
- One idea per post. Native-first (don't post a link and bail).
- Carousels/threads: each slide/tweet is a self-contained mini-hook.
- Post consistently; reply to comments in the first hour (algorithms reward early engagement).

## Hook Library
- "I [achieved result] in [timeframe]. Here's exactly how:"
- "Most people get [topic] wrong. Here's the truth:"
- "Stop doing [common thing]. Do this instead:"
- "[Number] [things] I wish I knew before [milestone]:"
- "Unpopular opinion: [contrarian take]."

## Paid Ads — Campaign Structure

### Hierarchy
```
Campaign  → objective + budget (awareness / traffic / leads / sales)
  Ad set  → audience + placement + bidding
    Ad    → creative + copy + CTA
```

### Funnel by objective
| Stage | Objective | Audience | Creative angle |
|-------|-----------|----------|----------------|
| TOFU | reach / awareness | broad / interest / lookalike | story, hook, problem |
| MOFU | traffic / engagement | retarget engagers, site visitors | proof, demo, comparison |
| BOFU | conversions / sales | cart/checkout abandoners, hot lists | offer, urgency, guarantee |

### Ad copy formula
```
Hook (call out audience or pain)        → first line / thumbnail
Body (PAS or FAB, 2–4 lines)            → value + proof
Offer + CTA (specific, low-friction)    → "Start free", "Shop the sale"
```
Match the ad's promise to the **landing page** headline (message match) or you burn budget.

### Creative testing
- Test **one variable at a time** (hook, image, audience, CTA).
- Run 3–5 creatives per ad set; let the algorithm find the winner before optimizing.
- Refresh creative when frequency climbs and CTR drops (ad fatigue).

## Paid Metrics
| Metric | Meaning | Watch when |
|--------|---------|-----------|
| CTR | clicks ÷ impressions | low → weak hook/creative |
| CPC / CPM | cost per click / 1k views | rising → fatigue or bad targeting |
| CVR | conversions ÷ clicks | low → landing page / offer mismatch |
| CPA / CAC | cost per acquisition | vs LTV — must stay profitable |
| ROAS | revenue ÷ ad spend | north-star for e-commerce |

## Self-Review Checklist
1. Does the **first second / first line** stop the scroll?
2. Is the content native to the platform (not a cross-post)?
3. One clear CTA, and does the destination match the promise?
4. For ads: right audience for the funnel stage, and is CPA < LTV?
5. Are you testing one variable, with enough budget to learn?
