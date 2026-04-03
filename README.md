# Agent Marketing Team

An AI-powered marketing system built on [Claude Code](https://claude.ai/claude-code) that executes full-funnel B2B campaigns — from market research through conversion optimization.

Five specialized agents coordinate through shared task lists, work in parallel, and follow a sprint model with human checkpoints.

---

## What It Does

Give it anything from a one-line request to a multi-asset campaign. It researches, strategizes, writes, reviews, and formats — with your approval at two checkpoints.

### Quick Tasks (Single Asset, No Campaign)

These run inline — one specialist, no sprint overhead.

**Draft a post:**
```
"Write a LinkedIn post about why most B2B landing pages fail
 at the first sentence"
```
→ Creative Specialist diagnoses the audience awareness stage (Problem Aware — they feel the pain but haven't found the fix), uses a Problem-Agitation Lead, writes in your voice.

**Research a market:**
```
"Research the stormwater compliance software market — who are the
 players, how do they position, and where are the gaps?"
```
→ Research Specialist runs the `/market-research` framework: maps three tiers of competitors, mines customer language from review sites, scores competitor messaging on Clarity/Relevance/Value/Differentiation, and flags positioning gaps where no one is competing.

**Find your positioning:**
```
"Run positioning angles for Gray Matter Logic against the
 ERP consulting market"
```
→ Research Specialist maps the real competitive alternatives (including "do nothing" and "hire an internal team"), extracts unique attributes, builds mechanisms using the Failure→Shift→Result structure, generates 5-8 angles scored by defensibility/resonance/provability, and tests the top 3 against Laja's 4-layer filter.

**Harvest your proof:**
```
"Harvest proof for 2NDNATURE — we have case studies on the website,
 a few G2 reviews, and some customer emails with results"
```
→ Research Specialist inventories every proof asset, scores each on Specificity + Credibility + Relevance (min 9/15 to include), tags with Cialdini persuasion dimensions (Social Proof, Authority, Consistency), and maps gaps against what your landing page, emails, and ads will need.

**Get a content strategy:**
```
"What keywords should we target for our municipal stormwater
 compliance product? We want to build organic traffic."
```
→ Research Specialist runs the `/keyword-research` framework: starts from ICP problems (not keyword tools), scores by Business Potential (0-3), splits into Money Phrases vs. Content Keywords, and produces an editorial calendar.

### Multi-Asset Campaigns (Full Sprint Model)

These activate Campaign Lead, who coordinates specialists across three sprints.

**Lead generation campaign:**
```
"Create a lead generation campaign for our ERP migration assessment tool:
 - Lead magnet: 'ERP Migration Readiness Scorecard'
 - Landing page targeting CFOs frustrated with their current system
 - 5-email nurture sequence bridging from scorecard to sales call
 - Goal: 200 qualified leads in 30 days"
```

Sprint 1 produces: market research, proof library, positioning angles with named mechanisms, lead magnet concept brief scored by Hormozi's Value Equation. You approve the direction.

Sprint 2 produces: the scorecard content, a landing page (awareness-diagnosed — CFOs from LinkedIn ads are Solution Aware, so it leads with mechanism differentiation, not problem agitation), a 5-email sequence with awareness-stage transitions per email (Solution Aware → Product Aware → Most Aware → Convert), ad angles multiplied across 6 dimensions for LinkedIn and email. You approve the drafts.

Sprint 3: polish, editorial review, platform formatting, publish.

**Product launch:**
```
"Launch our new AI-powered compliance monitoring feature:
 - Sales page for existing customers (they know us)
 - Announcement email sequence (3 emails)
 - Blog post for SEO
 - LinkedIn campaign (5 posts over 2 weeks)
 - Target: 50 demo requests from existing customers,
   100 new leads from organic"
```

The system handles two audiences simultaneously: existing customers are Most Aware (direct offer lead, proof-heavy), while organic traffic is Unaware/Problem Aware (story leads, pain agitation). Each asset gets the right messaging for its audience — the sales page and announcement emails lead with the offer and proof, while the blog post and LinkedIn campaign lead with the problem and mechanism.

**Content sprint:**
```
"Create a 4-week content marketing sprint on stormwater compliance:
 - 4 blog posts targeting different keywords
 - 1 newsletter per week repurposing blog content
 - LinkedIn posts promoting each piece
 - Goal: rank for 'stormwater compliance software' within 90 days"
```

Each blog post gets its funnel stage mapped to an awareness level: the top-of-funnel post opens with a Story Lead ("Last winter, a city in Oregon got a $2M fine..."), the mid-funnel post uses a Mechanism Lead ("Most compliance tools fail because they monitor after the fact..."), the bottom-funnel post uses a Proof Lead ("Here's how City of Portland reduced violations by 67%...").

### Standalone Skill Requests

You can invoke any skill directly without a campaign.

```
"Write a landing page for our free compliance audit — targeting
 municipal public works directors who've been manually tracking
 stormwater permits in spreadsheets"
```
→ Diagnoses awareness stage (Problem Aware — they know spreadsheets aren't working but haven't looked for software). Uses Problem-Agitation Lead above the fold. Names the mechanism in Section 3. Pulls proof from the proof library if available. Scores itself honestly before handing to Quality Gate.

```
"Create a 5-email onboarding sequence for new trial signups of
 our compliance platform"
```
→ Maps the awareness arc: Email 1 moves them from Product Aware to Most Aware (deliver the activation value), Email 2 deepens with a non-obvious insight, Email 3 introduces the full platform with a case study, Email 4 handles the top objection, Email 5 converts with a clear upgrade CTA.

```
"Design a lead magnet concept for attracting IT directors
 who are evaluating ERP systems"
```
→ Runs `/lead-magnet-strategy`: defines the Bridge (narrow problem → lead magnet → next problem revealed → core offer), selects the type (Problem Revealer — they need to discover how bad their current system is), scores with Hormozi's Value Equation, tests three names, maps distribution channels, and produces a concept brief for approval before any content gets written.

```
"Expert review our landing page draft"
```
→ Spawns 3-5 specialist reviewers (conversion optimizer, copywriter, ICP advocate, design strategist) who evaluate in parallel, score independently, then synthesize into a prioritized revision list.

```
"Repurpose our latest blog post for LinkedIn, Twitter thread,
 and newsletter"
```
→ Adapts the core content for each platform's native format, length, and conventions — not just truncation, but restructuring for how people consume on each platform.

**You review at two checkpoints (campaigns only):**
1. **After Sprint 1** — approve strategic direction and positioning angles
2. **After Sprint 2** — approve drafts and provide feedback

Sprint 3 executes the approved direction without a checkpoint.

---

## The Team

| Agent | Role | What They Do |
|-------|------|-------------|
| **Campaign Lead** | Coordinator | Designs strategy, creates task breakdowns, manages sprint checkpoints. Does NOT write content. |
| **Research Specialist** | Market Intelligence | Competitor analysis, customer language mining, keyword research, positioning gap identification. |
| **Creative Specialist** | Content Creator | Writes all assets (landing pages, emails, blogs, lead magnets, social posts) in your voice using skill frameworks. |
| **Quality Gate** | Editorial Review | Evaluates drafts: voice fidelity (40%), clarity (25%), craft (25%), positioning (10%). Approves or requests revisions. |
| **Distribution Specialist** | Publishing & Analytics | Formats for platforms, publishes, tracks performance, recommends optimizations. |

Agent definitions live in `.claude/agents/`. Team-wide protocols (task coordination, sprint model, escalation) are in `.claude/agents/TEAM.md`.

---

## How It's Organized

```
agent-marketing-team/
├── .claude/
│   ├── agents/                 # Agent definitions and team protocols
│   │   ├── TEAM.md             # Shared philosophy, coordination model, sprint framework
│   │   ├── campaign-lead.md    # Campaign orchestration workflow
│   │   ├── research-specialist.md
│   │   ├── creative-specialist.md
│   │   ├── quality-gate.md
│   │   └── distribution-specialist.md
│   │
│   ├── skills/                 # Frameworks agents load on demand
│   │   ├── landing-page/       # Direct-response landing pages
│   │   ├── email-sequence/     # Drip, nurture, onboarding sequences
│   │   ├── blog-post/          # SEO-optimized articles
│   │   ├── newsletter/         # Email newsletters
│   │   ├── social-post/        # LinkedIn, Twitter/X, Substack Notes
│   │   ├── lead-magnet/        # High-value opt-in content
│   │   ├── repurpose/          # Multi-platform adaptation
│   │   ├── positioning-angles/ # B2B differentiation frameworks
│   │   ├── keyword-research/   # Audience-intent keyword research
│   │   ├── market-research/    # Competitive intelligence
│   │   ├── expert-review/      # Multi-agent specialized analysis
│   │   ├── lead-magnet-strategy/ # Lead magnet concept design
│   │   ├── ad-angles/          # Ad-angle multiplication (6 dimensions)
│   │   └── proof-harvesting/   # Proof asset extraction and scoring
│   │
│   ├── templates/              # Campaign structure templates
│   │   ├── campaign-brief-template.md
│   │   ├── lead-gen-campaign.md
│   │   ├── product-launch.md
│   │   └── content-sprint.md
│   │
│   └── workflows/              # Multi-step processes
│       ├── sprint-planning.md
│       └── retrospective.md
│
├── context/                    # Your persistent context (populate before first campaign)
│   ├── voice-dna.md            # Your writing voice profile
│   ├── icp.md                  # Ideal customer profile
│   ├── business-profile.md     # Products, positioning, value proposition
│   └── brand-guide.md          # Optional platform-specific tone guidance
│
├── knowledge/                  # Compounding knowledge base
│   ├── research/               # Market research packages (populated during campaigns)
│   ├── learnings/campaigns/    # Patterns extracted from retrospectives
│   ├── archive/                # Published campaign records
│   └── feedback/analytics/     # Performance data
│
├── output/                     # Generated campaigns
│   └── campaigns/
│       └── [slug]-[YYYY-MM]/   # Each campaign gets its own directory
│           ├── campaign-brief.md
│           ├── research/
│           ├── strategy/       # Positioning angles, lead magnet concepts
│           ├── drafts/         # Creative Specialist writes here
│           ├── reviews/        # Expert review outputs
│           ├── edited/         # Quality Gate writes here
│           ├── ready/          # Distribution Specialist writes here
│           └── analytics/
│
├── CLAUDE.md                   # Routing rules (loaded into every conversation)
└── README.md                   # This file
```

**Why this structure:** Each agent writes to a separate directory. Drafts → Edited → Ready creates an audit trail with no file conflicts. Research compounds in `knowledge/` so future campaigns benefit from past work.

---

## Getting Started

### 1. Populate Context Files

**Required before running any campaign.** The system reads these before every task.

| File | What to put in it | How to create it |
|------|-------------------|------------------|
| `context/voice-dna.md` | Your writing voice — sentence patterns, word choice, tone, what you'd never say | Run `/writer:setup` or analyze 3-5 writing samples manually |
| `context/icp.md` | Ideal customer profile — pain points, goals, language, where they hang out | Run `/writer:setup` or document from customer conversations |
| `context/business-profile.md` | Products, pricing, positioning, customer results | Manual documentation |

**The system will stop and ask you to populate these if it finds placeholder content.**

### 2. Run a Simple Test

Start with a single asset to validate voice matching:

```
"Write a LinkedIn post about [topic you know well]"
```

Check: Does it sound like you? Does it reference your ICP? Is the craft quality high?

### 3. Run a Full Campaign

Once voice matching works, test the full sprint model:

```
"Create a lead generation campaign for [your product]:
 - Lead magnet: [topic] starter guide
 - Landing page
 - 3-email delivery sequence
 - Goal: 50 signups in 1 week"
```

This exercises the complete pipeline: research → strategy checkpoint → drafts → editorial review → platform formatting.

---

## Available Skills

### Content Creation
| Skill | What It Produces |
|-------|-----------------|
| `/landing-page` | Direct-response landing pages with hero, problem, solution, proof, offer, CTA |
| `/email-sequence` | Drip, nurture, onboarding, launch, or re-engagement sequences |
| `/blog-post` | SEO-optimized articles with meta tags, FAQ schema, keyword integration |
| `/newsletter` | Email newsletters in 4 formats (Personal Letter, Insight Post, Story+Lesson, Curated) |
| `/social-post` | LinkedIn (150-300 words), Twitter (threads), Substack Notes |
| `/lead-magnet` | High-value opt-in content (PDFs, checklists, templates, guides) |
| `/repurpose` | Adapt one piece for multiple platforms with native formatting |

### Marketing Strategy
| Skill | What It Produces |
|-------|-----------------|
| `/positioning-angles` | 5-8 scored differentiation angles based on competitive analysis |
| `/keyword-research` | Prioritized keyword map scored by business potential, not just volume |
| `/market-research` | Structured competitive intelligence with desk research + primary research flags |
| `/expert-review` | Multi-agent review from 3-5 specialist perspectives |
| `/lead-magnet-strategy` | Scored lead magnet concepts before any content creation begins |
| `/ad-angles` | 10-15 creative variants of an approved angle across Pain, Desire, Proof, Identity, Contrarian, Urgency |
| `/proof-harvesting` | Scored proof library (testimonials, case studies, data) with Cialdini persuasion tags and gap analysis |

Skills are markdown framework files in `.claude/skills/[name]/SKILL.md`. Agents read them on demand — they define the canonical process for each content type.

---

## Campaign Types

### Lead Generation
Build an email list with qualified leads. The system designs a lead magnet concept (scored by Hormozi's Value Equation before any content gets written), writes a landing page with awareness-appropriate messaging, creates the lead magnet content, builds a nurture sequence that walks subscribers through awareness stages toward a conversion CTA, and multiplies the core angle into ad variants.

**Assets:** lead magnet concept brief, lead magnet content, landing page, email nurture sequence, ad-angle library, social promotion posts.

### Product Launch
Announce a new offering and drive signups or sales. The system handles dual audiences — existing customers (Most Aware, proof-heavy, direct offer) and new prospects (Unaware/Problem Aware, story-led, mechanism-heavy). Each asset gets the right messaging for its audience.

**Assets:** sales/landing page, launch email sequence, announcement blog post, social campaign, ad-angle library.

### Content Marketing Sprint
SEO-focused authority building. Each piece targets a different keyword and funnel stage, with the awareness framework ensuring top-of-funnel articles open differently than bottom-of-funnel articles. Blog content gets repurposed into newsletters and social posts natively.

**Assets:** 3-5 keyword-targeted blog posts, email announcements, LinkedIn/Twitter promotion plan.

### Rebranding / Repositioning
When you're shifting positioning (like OSI → Gray Matter Logic), the system researches the new competitive landscape, builds mechanisms for the new positioning, generates scored angles, then produces all the content assets targeting the new audience — while maintaining voice consistency with the brand you're building.

Templates for each type are in `.claude/templates/`.

---

## How Coordination Works

### Task-Based (Not Sequential Handoffs)

Agents coordinate through Claude Code's TaskTool — shared task lists with dependencies, metadata-based handoffs, and parallel execution.

```
Campaign Lead creates tasks with dependencies
  → Specialists claim unblocked tasks from TaskList()
  → Each specialist completes and sets metadata (deliverable path, assessment, next agent)
  → Downstream agents read metadata via TaskGet() to find their inputs
```

Multiple researchers and writers can work simultaneously. Quality Gate works serially (one asset at a time) to maintain voice consistency.

### Sprint Model

| Sprint | Goal | You Review | Duration |
|--------|------|-----------|----------|
| **1: Plan & Sketch** | Research, positioning angles, campaign structure | ✅ Approve direction | 2-7 days |
| **2: Refine & Deepen** | Full drafts, expert reviews, deeper research | ✅ Approve creative | 3-10 days |
| **3: Execute & Ship** | Polish, editorial review, format, publish, track | Auto (approved direction) | 2-5 days |

### File Ownership

Each phase creates new files in separate directories — no shared editing, no merge conflicts:

| Phase | Agent | Directory |
|-------|-------|-----------|
| Research | Research Specialist | `research/` |
| Drafts | Creative Specialist | `drafts/` |
| Edited | Quality Gate | `edited/` |
| Ready | Distribution Specialist | `ready/` |

---

## Knowledge Compounding

After every campaign, the system runs a retrospective that extracts patterns into `knowledge/learnings/`. Future campaigns read these automatically. Categories: timing, asset-mix, coordination, task-patterns, quality-gates.

Research packages persist in `knowledge/research/` — competitor analysis from one campaign informs positioning for the next.

**The system gets better with every campaign.**

---

## Direct-Response Frameworks

The skills encode direct-response marketing theory that agents apply automatically. You don't need to memorize these — but understanding them helps you give better input and sharper feedback.

### Schwartz Awareness Mapping

**Used in:** `/landing-page`, `/email-sequence`, `/blog-post`

Every buyer sits at one of five awareness stages. The stage determines everything — what kind of opening to write, what to say, and what to avoid.

| Stage | What to lead with | What fails |
|-------|-------------------|-----------|
| **Unaware** | Story, curiosity, pattern interrupt | Mentioning your product, explaining solutions |
| **Problem Aware** | Pain agitation, "you're not alone" | Jumping to the solution too fast |
| **Solution Aware** | Mechanism — "Most fail because..." | Generic features, undifferentiated claims |
| **Product Aware** | Proof — results, case studies | More education (they already get it) |
| **Most Aware** | Direct offer — price, terms, urgency | Long warmups, storytelling (just make it easy) |

Each stage pairs with a **Masterson Lead Type** (from *Great Leads*): Story → Problem-Agitation → Mechanism → Proof → Direct Offer. The skill selects automatically based on who the audience is and where they're coming from.

**Tip:** When requesting content, mention the traffic source — "this is for cold LinkedIn ads" (Unaware), "this goes to our email list" (Product/Most Aware), "this targets people searching for alternatives" (Solution Aware). That one detail shapes the entire piece.

### Mechanism-Based Positioning

**Used in:** `/positioning-angles` Step 3.5

The mechanism is the "why this works" story — not a feature list, but an explanation that creates an "aha" moment. Structure: **Failure** (why the old way doesn't work) → **Shift** (what's different about your approach) → **Result** (what becomes possible).

Four types: **Process** (new method), **Discovery** (hidden insight), **System** (proprietary framework), **Timing** (market shift enables it).

The mechanism gets two checks:
- **Thiel's "secret" test** — Does it encode a truth competitors would disagree with? If yes, it's a category-creation candidate.
- **Kahneman's dual-process test** — Does it feel intuitively right AND hold up to logic? If only one, revise.

### Ad-Angle Multiplication

**Used in:** `/ad-angles`

Takes one approved positioning angle and expands it into 10-15 creative variants across six psychology dimensions: **Pain** (what hurts), **Desire** (what they want), **Proof** (evidence), **Identity** (tribal belonging), **Contrarian** (challenge consensus), **Urgency** (why now — genuine only).

Each variant gets tagged with its target awareness stage and best channel (LinkedIn ad, email subject, blog title, etc.). Creative Specialist uses this as a hook library when writing Sprint 2 content.

### Proof Harvesting

**Used in:** `/proof-harvesting`

Inventories every available proof asset (testimonials, case studies, data, credentials, media), scores each on Specificity + Credibility + Relevance (min 9/15 to include), tags with Cialdini persuasion dimensions (Social Proof, Authority, Consistency, Liking, Reciprocity, Scarcity), and maps gaps against what each content asset will need.

Run during Sprint 1. The output is a reusable proof library that Creative Specialist loads before writing anything that needs evidence.

### How They Chain Together

```
Sprint 1:
  /market-research        → competitive landscape, customer language
  /proof-harvesting       → scored proof library with gap analysis
  /positioning-angles     → mechanisms built, angles scored, Laja-tested
  [You approve]           → select positioning angle

Sprint 2:
  /ad-angles              → 10-15 creative variants from approved angle
  /landing-page           → awareness stage drives messaging and lead type
  /email-sequence         → awareness arc maps each email's transition
  /blog-post              → funnel stage → awareness level → intro strategy
  [You approve]           → approve drafts, give revision notes

Sprint 3:
  Revise → editorial review → format → publish
```

Each skill reads the output of upstream skills. The proof library feeds landing pages and ad angles. The mechanism feeds the Solution Bridge. The awareness diagnosis in the landing page matches the arc in the email sequence. Nothing is applied in isolation.

---

## Optional: MCP Integration

For deeper market research, configure MCPs in `~/.claude/mcp-config.json`:

- **Perplexity MCP** — Multi-source market research synthesis
- **Firecrawl MCP** — Scrape competitor websites at scale
- **Playwright MCP** — Screenshot competitor pages for visual analysis

Not required — the Research Specialist falls back to `WebSearch` and `WebFetch` when MCPs aren't configured.

---

**Built with [Claude Code](https://claude.ai/claude-code).** Inspired by [Anthropic's Agent Teams Pattern](https://docs.anthropic.com/en/build-with-claude/agent-patterns).
