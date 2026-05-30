# Email Marketing

Sequences, subject lines, newsletter structure, automation, and deliverability.

## Sequence Blueprints

> Search full blueprints: `python3 scripts/search.py "<type>" --domain email`

### Welcome (3–5 emails)
1. **Deliver + welcome** — confirm value, set expectations, quick win.
2. **Story / why** — founder or mission, build connection.
3. **Best resource** — your most useful content; build trust.
4. **Soft offer** — introduce the product as the natural next step.
5. **Direct CTA** — clear offer with a reason to act now.

### Nurture / Lead-magnet follow-up
Educate → demonstrate → overcome objection → case study → offer. Space 1–3 days apart.

### Abandoned cart (3 emails)
1. **Reminder** (~1h): "You left something behind."
2. **Objection handling** (~24h): shipping, returns, reviews.
3. **Incentive** (~48h): discount or urgency (use sparingly).

### Re-engagement / win-back
"We miss you" → best-of content → exclusive offer → "last email" permission check (helps list hygiene).

## Subject Line Patterns

| Type | Example |
|------|---------|
| Curiosity | "The mistake costing you signups" |
| Benefit | "Get 3 hours back this week" |
| Urgency | "Ends tonight: 20% off" |
| Personal | "Quick question, {{first_name}}" |
| Number/list | "5 templates inside" |
| How-to | "How to write a cold email that gets replies" |

Rules: 30–50 chars (mobile cuts ~40), front-load the value, write a complementary **preview text** (don't repeat the subject), avoid spam triggers (ALL CAPS, "FREE!!!", excessive emojis), one idea per subject. **A/B test** subject + preview on 10–20% of the list.

## Email Body Anatomy
```
Hook (1 line, matches subject promise)
Context / story (2–4 short lines)
Value or offer (the one thing)
Single CTA button (action verb, first person)
P.S. (restate offer or add urgency — often the most-read line)
```
- One goal and **one** primary CTA per email.
- Plain-text-feeling beats over-designed for relationship/nurture emails.
- Personalize beyond `{{first_name}}`: behavior, segment, lifecycle stage.

## Newsletter Structure (recurring)
1. Personal intro / hook
2. Main piece (one core idea, skimmable)
3. Curated links or quick tips
4. One CTA (reply, read, buy)
Consistency of cadence > frequency. Pick a schedule you can sustain.

## Deliverability Essentials
- Authenticate sending domain: **SPF, DKIM, DMARC**.
- Use a real reply-to; warm up new domains/IPs gradually.
- Keep lists clean: confirmed opt-in, remove hard bounces, sunset inactive subscribers.
- Maintain healthy text-to-image ratio; always include a working unsubscribe.
- Watch spam complaint rate (< 0.1%) and bounce rate (< 2%).

## Key Metrics (benchmarks vary by industry)
| Metric | Healthy range | Lever to improve |
|--------|---------------|------------------|
| Open rate | 25–40% | subject, preview, sender name, send time, list hygiene |
| Click rate (CTR) | 2–5% | offer relevance, single CTA, copy/design |
| Click-to-open | 10–15% | body copy and CTA clarity |
| Unsubscribe | < 0.5% | frequency, segmentation, expectation-setting |
| Conversion | goal-dependent | offer, landing page match |

## Self-Review Checklist
1. Does the subject promise something the body delivers?
2. Is there exactly **one** desired action?
3. Would it read fine as plain text on a phone?
4. Is it segmented/relevant to who receives it?
5. Compliant: physical address, unsubscribe, honest sender? (CAN-SPAM / GDPR)
