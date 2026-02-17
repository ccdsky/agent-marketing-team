# Knowledge Directory

This directory is the **brain** of your marketing system. It stores research, learnings, and performance data that compounds over time.

## Directory Structure

```
knowledge/
├── research/              # Market research packages
│   └── [topic]-[date].md
│
├── learnings/             # Compounding patterns
│   └── campaigns/
│       ├── timing/        # When to send emails, publish, etc.
│       ├── asset-mix/     # Which asset combos work best
│       ├── coordination/  # Agent coordination patterns
│       ├── task-patterns/ # Task breakdown patterns
│       ├── quality-gates/ # Quality process insights
│       └── retrospectives/ # Campaign retrospectives
│
├── archive/               # Published campaigns (reference)
│   └── [campaign-slug]/
│
└── feedback/
    └── analytics/         # Performance data and reports
        └── [campaign]-[date].md
```

---

## Research Packages

**Location:** `knowledge/research/`

**Created by:** Research Specialist

**Purpose:** Market intelligence that informs campaign strategy

**Examples:**
- `dev-cli-market-landscape-2026-02.md` - Market players, positioning, trends
- `dev-cli-customer-language-2026-02.md` - Exact phrases customers use
- `competitor-analysis-cli-tools-2026-02.md` - How competitors market
- `keyword-research-developer-tools-2026-02.md` - SEO opportunities

**Format:** Structured markdown with findings, sources, and actionable insights

---

## Learnings (Knowledge Compounding)

**Location:** `knowledge/learnings/campaigns/`

**Purpose:** Extract patterns from campaigns to automatically improve future work

**How it works:**
1. Campaign completes
2. Retrospective identifies patterns (what worked, what didn't)
3. Patterns saved to appropriate category
4. Next campaign: Agents search learnings before planning
5. Patterns automatically applied to new campaigns

**System gets better with every campaign.**

### Timing Learnings

**Location:** `knowledge/learnings/campaigns/timing/`

**Examples:**
- `email-day3-optimal-for-features.md` - "Email 3 on Day 5 had 2x click rate vs Day 3"
- `linkedin-posting-time.md` - "Posts at 8am ET get 40% more engagement than 2pm"
- `blog-publish-tuesday.md` - "Tuesday blog posts get 25% more weekend traffic"

### Asset Mix Learnings

**Location:** `knowledge/learnings/campaigns/asset-mix/`

**Examples:**
- `lead-magnet-plus-blog.md` - "Lead magnet + blog outperformed lead magnet alone by 40%"
- `email-sequence-length.md` - "5-email sequences convert 15% better than 3-email"
- `social-traffic-sources.md` - "LinkedIn traffic converts 2x better than Twitter"

### Coordination Learnings

**Location:** `knowledge/learnings/campaigns/coordination/`

**Examples:**
- `parallel-research-limits.md` - "2 parallel research tasks work well, 3+ creates duplication"
- `draft-review-cycle.md` - "Expert review before editorial saves 1 revision cycle"
- `task-granularity.md` - "Tasks scoped to 1-3 hours work best for self-claiming"

### Task Pattern Learnings

**Location:** `knowledge/learnings/campaigns/task-patterns/`

**Examples:**
- `landing-page-task-split.md` - "Breaking landing page into structure + copy prevents bottlenecks"
- `email-sequence-dependencies.md` - "Email 1 should complete before drafting 2-5 (sets tone)"
- `research-to-draft-delay.md` - "Research completion → draft start gap of 4+ hours improves quality"

### Quality Gate Learnings

**Location:** `knowledge/learnings/campaigns/quality-gates/`

**Examples:**
- `lead-magnet-review-first.md` - "Reviewing lead magnet before landing page improves consistency"
- `voice-drift-patterns.md` - "Section 3 of landing pages tends toward corporate voice - watch for it"
- `cta-friction-check.md` - "Always check CTA for friction words: 'submit', 'sign up', etc."

### Retrospectives

**Location:** `knowledge/learnings/campaigns/retrospectives/`

**Purpose:** Comprehensive post-campaign analysis

**Created by:** Campaign Lead + Distribution Specialist after campaign completes

**Format:** Full retrospective using template (what worked, what didn't, metrics, learnings, ROI)

**Examples:**
- `dev-cli-launch-2026-02.md` - Full retrospective for developer CLI tool campaign
- `lead-gen-saas-2026-01.md` - Lead generation campaign retrospective

---

## Analytics

**Location:** `knowledge/feedback/analytics/`

**Created by:** Distribution Specialist

**Purpose:** Performance tracking and optimization recommendations

**Types:**
- Daily reports (Week 1 of campaign)
- Weekly reports (ongoing)
- Campaign retrospectives (post-campaign)

**Examples:**
- `dev-cli-launch-day3-2026-02-15.md` - Day 3 performance update
- `dev-cli-launch-week1-2026-02-20.md` - Week 1 comprehensive report
- `dev-cli-launch-final-2026-03-01.md` - Final campaign results

---

## Archive

**Location:** `knowledge/archive/`

**Purpose:** Reference library of published campaigns

**What to archive:**
- Final published versions of all assets
- Campaign brief
- Key research packages
- Performance results

**When to archive:** After campaign fully completes and retrospective is done

**Example structure:**
```
knowledge/archive/dev-cli-launch-2026-02/
├── campaign-brief.md
├── assets/
│   ├── lead-magnet-cli-patterns.pdf
│   ├── landing-page.html
│   └── email-sequence.md
├── research/
│   └── market-landscape.md
└── results/
    ├── week1-report.md
    └── final-retrospective.md
```

---

## How Agents Use Knowledge

### Before Campaign Planning
**Campaign Lead searches:**
```
Grep(
  pattern="lead generation",
  path="knowledge/learnings/campaigns/",
  glob="*.md"
)
```

**Finds:** Past learnings about lead gen campaigns automatically applied

### Before Writing Content
**Creative Specialist searches:**
```
Grep(
  pattern="landing page",
  path="knowledge/learnings/campaigns/",
  glob="*.md"
)
```

**Finds:** Voice patterns, CTA best practices, structure insights

### During Performance Monitoring
**Distribution Specialist searches:**
```
Grep(
  pattern="email open rate",
  path="knowledge/feedback/analytics/",
  glob="*.md"
)
```

**Finds:** Historical benchmarks to compare against

---

## Knowledge Compounding in Action

**Campaign 1:**
- Launch lead gen campaign
- Learn: "Email subject lines with numbers get 40% higher opens"
- Save: `knowledge/learnings/campaigns/timing/email-subject-numbers.md`

**Campaign 2:**
- Campaign Lead reads learnings before planning
- Finds: Email subject number pattern
- Instructs Creative Specialist: "Use numbers in subject lines"
- Creative Specialist applies pattern automatically
- Result: Better performance from day 1

**Campaign 3:**
- Now has 2 campaigns of learnings
- Even better performance
- New patterns identified
- Cycle continues...

**System compounds. Every campaign makes the next one better.**

---

## Privacy & Git

**Default:** `knowledge/research/` and `knowledge/feedback/` are .gitignored (may contain sensitive business info)

**Optional:** Commit `knowledge/learnings/` if you want to preserve patterns across machines/team members

**Recommended:** Keep research and analytics private, share learnings if working with team
