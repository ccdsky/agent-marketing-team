# Platform Formatting Reference

Used by Distribution Specialist. Read this file when formatting assets for any platform.

---

## Landing Pages (Web)

**Input:** Edited landing page (markdown)
**Output:** Web-ready HTML/markdown with formatting

**Optimizations:**
- Above-the-fold hook (headline + subheadline visible without scrolling)
- Mobile-responsive formatting
- Clear CTA buttons (color, size, placement)
- Social proof placement (testimonials, logos)
- Scannable sections (headers, bullets, white space)
- Fast load time considerations (image optimization)

**Technical requirements:**
- Meta title (60 chars max, includes keyword)
- Meta description (155 chars max, includes CTA)
- Open Graph tags (for social sharing)
- Structured data if applicable
- Tracking pixels (GA, FB, etc.)

**Format template:**
```markdown
---
# Landing Page: [Title]

Meta Title: [60 chars, keyword-optimized]
Meta Description: [155 chars, CTA-focused]
URL Slug: /[keyword-slug]

---

[Full landing page content with HTML/markdown formatting]

---

## Publishing Checklist

- [ ] Upload to web host ([platform name])
- [ ] Configure opt-in form to connect to email platform
- [ ] Add tracking pixels (GA: [ID], FB: [ID])
- [ ] Test form submission on desktop
- [ ] Test form submission on mobile
- [ ] Verify thank-you page redirect
- [ ] Set up A/B test if applicable

---

## Performance Tracking

**Business outcomes:** Opt-in-to-customer conversion rate (target: X%), revenue per visitor (target: $X)
**Demand signals:** Conversion quality (are opt-ins becoming qualified leads?), brand search lift post-launch
**Diagnostics:** Traffic sources, opt-in rate, time on page, scroll depth, CTA clicks

**Tracking setup:**
- Google Analytics: [Event name]
- Heatmaps: [Tool if applicable]
- Email platform: [Platform name]
```

---

## Email Sequences

**Input:** Edited email sequence (markdown)
**Output:** Individual emails formatted for email platform

**Optimizations:**
- Subject lines (45 chars max for mobile)
- Preview text (40-50 chars, complements subject)
- Mobile-first formatting (short paragraphs, scannable)
- Plain text option (for deliverability)
- Clear CTA (one primary action per email)
- Unsubscribe link (required by law)

**Email structure:**
```markdown
## Email [N]: [Subject Line]

Subject: [Subject line - 45 chars max]
Preview: [Preview text - 40-50 chars]
Delay: [Send X days/hours after previous email]

---

[Email body content]

---

**From:** [Your name / Sender name]
**Reply-to:** [Email address]
**Unsubscribe:** [Link to unsubscribe]

---

## Email Platform Setup

**Platform:** [ConvertKit / Mailchimp / ActiveCampaign / etc.]

**Sequence settings:**
- Trigger: [Tag added / Form submitted / etc.]
- Send time: [Time of day, timezone]
- Delay: [X days/hours after previous email]

**Tracking (outcomes first):**
- Revenue per subscriber (target: $X)
- Sequence-to-customer conversion rate (target: X%)
- Open rate (target: X%) — diagnostic
- Click rate (target: X%) — diagnostic
- Reply rate (if applicable) — diagnostic

**A/B tests:**
- [Subject line variant 1 vs variant 2]
- [CTA placement test]
```

---

## LinkedIn Posts

**Input:** Edited LinkedIn post
**Output:** Platform-optimized post

**Optimizations:**
- Hook in first 3 lines (visible before "see more")
- Length: 800-1300 characters optimal
- Line breaks for scannability
- Hashtags: 3-5 relevant tags
- CTA in comments (LinkedIn penalizes links in posts)
- Tag relevant people if applicable

**Format template:**
```markdown
## LinkedIn Post: [Topic]

**Character count:** [X]/1300

---

[Hook - first 3 lines must grab attention]

[Body - use line breaks for scannability]

[CTA - what should they do?]

---

**Hashtags:** #[Tag1] #[Tag2] #[Tag3] #[Tag4] #[Tag5]

**First comment (with link):**
[CTA text with link to landing page / resource]

---

## Publishing Checklist

- [ ] Copy post text to LinkedIn
- [ ] Add hashtags
- [ ] Post first comment with link
- [ ] Tag mentioned individuals
- [ ] Schedule or publish immediately
- [ ] Monitor engagement first 2 hours

---

## Performance Tracking

**Business outcomes:** Qualified leads from post (target: X), demo requests attributed to post
**Demand signals:** Profile views → connection requests (pipeline signal), comment quality (are ICPs engaging?)
**Diagnostics:** Engagement rate (target: X%), impressions, click-through rate (from first comment link)
```

---

## Twitter/X Threads

**Input:** Edited Twitter thread
**Output:** Individual tweets optimized for platform

**Optimizations:**
- First tweet is hook (must stop scroll)
- Each tweet < 280 characters
- Each tweet standalone (can be RT'd individually)
- Thread flows logically
- CTA at end (and optionally mid-thread)
- Images/media if applicable (increase engagement)

**Format template:**
```markdown
## Twitter Thread: [Topic]

**Total tweets:** [N]

---

### Tweet 1/[N] (Hook)
[First tweet - must stop the scroll]

[Character count: X/280]

---

### Tweet 2/[N]
[Second tweet]

[Character count: X/280]

---

[Continue for all tweets...]

---

### Final Tweet (CTA)
[CTA tweet with link]

[Character count: X/280]

---

## Publishing Checklist

- [ ] Create thread in Twitter
- [ ] Verify each tweet < 280 chars
- [ ] Add images if applicable
- [ ] Schedule or publish immediately
- [ ] Pin thread to profile if important
- [ ] Monitor replies first 2 hours

---

## Performance Tracking

**Business outcomes:** Link clicks → landing page conversions (target: X), DM inquiries or replies from ICPs
**Demand signals:** Follower quality growth (are ICPs following?), reply/conversation quality
**Diagnostics:** Engagement rate (target: X%), impressions, retweets
```

---

## Blog Posts (SEO)

**Input:** Edited blog post
**Output:** SEO-optimized blog post

**Optimizations:**
- Title tag (60 chars, includes keyword)
- Meta description (155 chars, includes CTA)
- URL slug (short, keyword-focused)
- Headers (H1, H2, H3 structure)
- Internal links (3-5 to related content)
- External links (sources, references)
- Images with alt text
- Schema markup if applicable

**Format template:**
```markdown
---
# Blog Post: [Title]

**SEO Metadata:**
- Title: [60 chars, keyword-optimized]
- Meta Description: [155 chars]
- URL Slug: /blog/[keyword-slug]
- Primary Keyword: [keyword]
- Secondary Keywords: [keyword], [keyword]
- Category: [Category]
- Tags: [Tag], [Tag], [Tag]

---

[Full blog post content with proper header hierarchy]

---

## Publishing Checklist

- [ ] Upload to CMS ([WordPress / Ghost / etc.])
- [ ] Set featured image (with alt text)
- [ ] Add internal links
- [ ] Configure URL slug
- [ ] Add meta title and description
- [ ] Set category and tags
- [ ] Preview on desktop and mobile
- [ ] Publish or schedule

---

## Performance Tracking

**Business outcomes:** Organic-to-pipeline conversion rate (target: X%), leads generated from post (target: X/month)
**Demand signals:** Brand search lift after publish (Google Trends), returning visitor rate, CTA conversion rate
**Diagnostics:** Organic traffic (target: X visits/month), keyword rankings, avg. time on page, bounce rate, scroll depth

**SEO tracking:**
- Google Search Console: Monitor impressions, clicks, position
- Keyword rank tracking: [Tool]
```

---

## Analytics Report Templates

### Pre-Launch Success Metrics Template

```markdown
## Campaign: [Name]
## Success Metrics

**Primary Goal:** [500 email signups → 25 customers → $X revenue in 30 days]

### Tier 1 — Business Outcomes (Lead With This)
- Revenue target: [$X from this campaign]
- Revenue per lead: [Target: $X]
- Customer LTV estimate: [$X]
- Cost per acquisition: [Target: $X]
- ROI target: [3x]
- Pipeline contribution: [X% of quarterly pipeline]

### Tier 2 — Demand Signals (Prove Momentum)
- Conversion quality: [Close rate target: X%, average deal size: $X]
- Conversion velocity: [Target time-to-close: X days]
- Brand search growth: [Baseline Google Trends score before campaign: X]
- Share of voice vs. competitors: [Baseline: X% — track via branded search volume ratios]
- Net-new vs. existing: [Target: X% of conversions from contacts NOT already in CRM/list]

### Tier 3 — Funnel Diagnostics (Supporting Detail)
- Landing page visitors: [Target: 5000]
- Opt-in rate: [Target: 10% = 500 signups]
- Email open rate: [Target: 40%]
- Email click rate: [Target: 20%]
- Traffic sources: [Paid / organic / social / referral]
- Best performing channel: [channel name]

*Tier 1 goes in the headline of every report. Tier 2 proves marketing is building real demand. Tier 3 explains why numbers moved — use for diagnosis, not for proving value.*
```

### Tracking Setup Checklist

```markdown
## Tracking Setup: [Campaign]

- [ ] GA event: Landing page view
- [ ] GA event: Opt-in form submission
- [ ] GA event: Thank-you page view
- [ ] GA goal: Email signup
- [ ] UTM parameters: [Source/medium/campaign tags]
- [ ] Email platform: Tag new subscribers with campaign name
- [ ] Email platform: Track open/click rates per email in sequence
- [ ] Heatmap: Landing page scroll depth and click tracking
- [ ] Test all tracking (submit test opt-in, verify data appears)
```

### Daily Report Template

```markdown
## Day [N] Performance: [Campaign]

**Status:** 🟢 On track | 🟡 Below target | 🔴 Critical issue

**Business Outcomes (Tier 1):**
- Revenue goal progress: $[X] of $[Target] ([Y]%)
- Customers/deals from campaign: [X] (target: [Y] by day [N])
- On pace for: [Projected total revenue / customers]

**Demand Signals (Tier 2):**
- Conversion quality: [Close rate / deal size trend vs. baseline]
- Conversion velocity: [Days-to-close trend vs. baseline]
- Brand search trend: [Up / flat / down since launch]

**Funnel Diagnostics (Tier 3):**
- Landing page visitors: [X] (target: [Y]/day)
- Opt-in rate: [X]% (target: [Y]%)
- Email open/click rates: [X]% / [Y]%
- Top traffic source: [Source] at [X]% opt-in rate

**Flags:**
- [Any issues or concerns]

**Recommendations:**
- [Data-driven optimization suggestions]
```

### Weekly Report Template

```markdown
## Week [N] Performance Report: [Campaign]

**Campaign Goal:** [Original goal]
**Result:** [Actual result vs goal]

---

### Business Outcomes (Tier 1)

| Metric | Target | Actual | Variance | Status |
|--------|--------|--------|----------|--------|
| Revenue from campaign | $[X] | $[Y] | [+/- Z]% | [On track / Behind / Ahead] |
| Customers acquired | [X] | [Y] | [+/- Z]% | |
| Revenue per lead | $[X] | $[Y] | [+/- Z]% | |
| Cost per acquisition | $[X] | $[Y] | [+/- Z]% | |
| ROI | [X]x | [Y]x | [+/- Z]% | |

*If revenue data unavailable, use proxy: (leads × estimated close rate × average deal size)*

---

### Demand Signals (Tier 2)

**Conversion quality:**
- Close rate from campaign leads: [X]% (vs. [Y]% baseline)
- Average deal size from campaign leads: $[X] (vs. $[Y] baseline)
- Lead quality trend: [Improving / Stable / Declining]

**Conversion velocity:**
- Time-to-close from campaign leads: [X] days (vs. [Y] days baseline)
- Pipeline velocity trend: [Faster / Same / Slower]

**Brand demand growth:**
- Google Trends brand score: [X] (vs. [Y] at campaign launch)
- Direct traffic trend: [Up X% / Flat / Down X%]

**Share of voice:**
- Brand search volume vs. top competitor: [X]% (vs. [Y]% at launch)

---

### Incrementality Assessment

**Net-new vs. existing contacts:**
- Total conversions: [X]
- From net-new contacts (not in CRM/list before campaign): [X] ([Y]%)
- From existing contacts: [X] ([Y]%)

**Incrementality verdict:** [This campaign is creating new demand / This campaign is mostly capturing existing demand / Mixed — investigate further]

*If >70% of conversions are from existing contacts, this campaign may be taking credit for demand that already existed. Consider: what happens to these numbers if we pause this channel?*

---

### Funnel Diagnostics (Tier 3)

**Traffic & Conversion:**
| Source | Visitors | Opt-ins | Opt-in Rate | Cost/Lead |
|--------|----------|---------|-------------|-----------|
| [Source 1] | [X] | [Y] | [Z]% | $[A] |
| [Source 2] | [X] | [Y] | [Z]% | $[A] |

**Email Sequence:**
| Email | Sent | Open Rate | Click Rate | Unsubscribe |
|-------|------|-----------|------------|-------------|
| Email 1 | [X] | [Y]% | [Z]% | [A]% |
| Email 2 | [X] | [Y]% | [Z]% | [A]% |

*These metrics explain WHY outcomes moved. They are not the headline.*

---

### Insights & Patterns

**What's working:**
- [Specific insight with data — tie to business outcome, not just funnel metric]

**What's not working:**
- [Specific issue with data — explain the business impact, not just the metric gap]

**Unexpected findings:**
- [Surprising pattern]

---

### Optimization Recommendations

**High priority (implement this week):**
1. [Specific action based on data]
2. [Specific action based on data]

**Consider testing:**
1. [A/B test suggestion]

**Investigate:**
1. [Question that needs deeper analysis]

---

### Forecast

**If current trends continue:**
- Projected revenue: $[X] (target: $[Y])
- Projected customers: [X] (target: [Y])
- Likelihood of hitting goal: [High / Medium / Low]
- Gap to close: [Y] (if behind target)

**Recommended actions:**
[What to do to hit goal or optimize further]
```
