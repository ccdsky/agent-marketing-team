# Agent Marketing Team

An AI-powered marketing system built on [Claude Code](https://claude.ai/claude-code) that executes full-funnel B2B campaigns — from market research through conversion optimization.

Five specialized agents coordinate through shared task lists, work in parallel, and follow a sprint model with human checkpoints.

---

## What It Does

Give it a campaign goal. It researches, strategizes, writes, reviews, and formats — across multiple assets, with your approval at two checkpoints.

**Simple request:**
```
"Write a LinkedIn post about why B2B teams should think in funnels, not content pieces"
```
→ Creative Specialist reads your voice profile, creates a draft in your voice, returns it inline.

**Full campaign:**
```
"Create a lead generation campaign for my developer CLI tool:
 - Lead magnet: CLI patterns guide
 - Landing page
 - 5-email nurture sequence
 - Goal: 500 signups in 2 weeks"
```
→ Campaign Lead designs the strategy → Research Specialist analyzes the market and competitors → Creative Specialist writes all assets in your voice → Quality Gate reviews for voice fidelity and craft → Distribution Specialist formats for platforms and sets up tracking.

**You review at two checkpoints:**
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
Build an email list with qualified leads. Assets: lead magnet, landing page, thank-you page, email nurture sequence. Timeline: 10-14 days.

### Product Launch
Announce a new offering, drive signups or sales. Assets: sales page, launch email sequence, blog post, social assets. Timeline: 14-21 days.

### Content Marketing Sprint
SEO-focused authority building. Assets: 3-5 blog posts, email announcements, social promotion plan. Timeline: 10-14 days.

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

Several skills encode direct-response marketing theory that shapes how the team writes. These frameworks are embedded in the skills themselves — agents apply them automatically when running the skill. Understanding how they work will help you get better results and give better feedback.

### Schwartz Awareness Mapping

**Where it lives:** `/landing-page` Step 1, `/email-sequence` Step 1, `/blog-post` Step 1

Every buyer sits at one of five awareness stages. The stage determines the messaging approach — what you can say, what you must not say, and what kind of "lead" (opening) to use.

| Stage | The buyer... | What to lead with |
|-------|-------------|-------------------|
| **Unaware** | Doesn't know they have the problem | Story or curiosity — never mention the product |
| **Problem Aware** | Feels the pain, doesn't know solutions exist | Agitate the pain before offering solutions |
| **Solution Aware** | Evaluating approaches | Mechanism differentiation — "Most fail because..." |
| **Product Aware** | Knows your product, not yet convinced | Proof — results, case studies, testimonials |
| **Most Aware** | Knows and trusts you | Direct offer — price, terms, urgency |

**How to use it:** When requesting a landing page, email sequence, or blog post, tell the system who the audience is and where they're coming from. The skill will diagnose the awareness stage and apply the right messaging rules. If you're running ads to cold traffic, that's Unaware/Problem Aware. If you're emailing your existing list, that's Product Aware or Most Aware.

**Lead types** (from Masterson/Forde's *Great Leads*) are paired with each stage: Story Leads for Unaware, Problem-Agitation Leads for Problem Aware, Solution/Mechanism Leads for Solution Aware, Proof Leads for Product Aware, Direct Offer Leads for Most Aware.

### Mechanism-Based Positioning

**Where it lives:** `/positioning-angles` Step 3.5

A mechanism is the "why this works" story. It makes your positioning believable and defensible — not just a claim, but an explanation that creates an "aha" moment.

**The structure:**
1. **The Failure** — Why what they tried before didn't work
2. **The Shift** — What's different about your approach
3. **The Result** — What becomes possible now

**Four mechanism types:**
- **Process** — "Instead of X, we do Y, which means Z"
- **Discovery** — "We found that [non-obvious truth]..."
- **System** — "Our [Named System] works because..."
- **Timing** — "Until [recent change], this wasn't possible..."

**How to use it:** When you run `/positioning-angles`, Step 3.5 will build mechanisms from your unique attributes before generating angles. Every angle then references or builds on a mechanism. If your mechanism passes Thiel's "secret" test (encodes a non-obvious truth competitors would disagree with), the skill flags it as a category-creation candidate.

The mechanism also gets checked against Kahneman's dual-process model: does it *feel* right intuitively (System 1) AND hold up to logical scrutiny (System 2)? If it only passes one, it needs revision.

### Ad-Angle Multiplication

**Where it lives:** `/ad-angles` (new skill)

After Sprint 1 approves a positioning angle, this skill multiplies it into 10-15 distinct creative variants — each targeting a different buyer psychology and awareness stage.

**Six dimensions:**

| Dimension | Leads with... | Source |
|-----------|--------------|--------|
| **Pain** | What hurts | ICP pain points |
| **Desire** | What they want | ICP desired outcomes |
| **Proof** | Evidence | Proof library |
| **Identity** | Who they are | Tribal belonging |
| **Contrarian** | What's wrong | Challenge conventional wisdom |
| **Urgency** | Why now | Market timing (genuine only) |

**How to use it:** Run this at the start of Sprint 2 after the positioning angle is approved. The output is a tagged table — each angle includes its awareness stage target (so you know which audience it fits) and best channel (LinkedIn ad, email subject, blog title, etc.). Creative Specialist uses this as a hook library when writing content.

```
"Multiply the approved positioning angle into ad angles for [campaign]"
```

### Proof Harvesting

**Where it lives:** `/proof-harvesting` (new skill)

Before writing any content that needs evidence, run this to inventory and score all available proof assets.

**How it works:**
1. **Inventory** — Audit all sources: testimonials, case studies, data, credentials, media, community metrics
2. **Score** — Rate each asset on Specificity (1-5), Credibility (1-5), and Relevance (1-5). Minimum 9/15 to include.
3. **Tag** — Assign Cialdini persuasion dimensions: Social Proof, Authority, Consistency, Liking, Reciprocity, Scarcity
4. **Gap analysis** — Map inventory against content needs and identify what's missing

**How to use it:** Run this during Sprint 1 alongside market research. It produces a `knowledge/research/proof-library-[company]-[date].md` file that Creative Specialist loads before writing landing pages, email sequences, and ad copy.

```
"Harvest proof for [company/product]"
```

If gaps exist (e.g., no case study arc for email sequences, no Score 13+ result for landing page hero), the skill tells you who to ask and what to request.

### How the Frameworks Connect

In a full campaign, the frameworks chain together:

```
Sprint 1:
  /market-research        → competitive landscape
  /proof-harvesting       → scored proof library
  /positioning-angles     → mechanism built (Step 3.5), angles scored
  [Human checkpoint]      → approve positioning angle

Sprint 2:
  /ad-angles              → 10-15 creative variants from approved angle
  /landing-page           → awareness stage drives messaging approach
  /email-sequence         → awareness arc maps each email's job
  /blog-post              → funnel stage → awareness level → intro strategy
  [Human checkpoint]      → approve drafts

Sprint 3:
  Revise, polish, ship
```

Each skill reads the output of upstream skills. The proof library feeds landing pages and ad angles. The mechanism from positioning-angles feeds the landing page's Solution Bridge. The awareness diagnosis in the landing page matches the awareness-stage arc in the email sequence. No framework is applied in isolation.

---

## Optional: MCP Integration

For deeper market research, configure MCPs in `~/.claude/mcp-config.json`:

- **Perplexity MCP** — Multi-source market research synthesis
- **Firecrawl MCP** — Scrape competitor websites at scale
- **Playwright MCP** — Screenshot competitor pages for visual analysis

Not required — the Research Specialist falls back to `WebSearch` and `WebFetch` when MCPs aren't configured.

---

**Built with [Claude Code](https://claude.ai/claude-code).** Inspired by [Anthropic's Agent Teams Pattern](https://docs.anthropic.com/en/build-with-claude/agent-patterns).
