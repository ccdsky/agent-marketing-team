# Agent Marketing Team

**An AI-powered marketing system that executes full-funnel campaigns from market research through conversion optimization.**

This isn't a content team—it's a marketing team. We think in funnels, research first, and iterate until right.

---

## Table of Contents

- [What This Is](#what-this-is)
- [Quick Start](#quick-start)
- [The Team](#the-team)
- [How It Works](#how-it-works)
- [Campaign Types](#campaign-types)
- [Setup](#setup)
- [Product Requirements Document](#product-requirements-document)

---

## What This Is

A **multi-agent marketing system** powered by Claude Code that executes campaigns autonomously:

**From this:**
```
"I need to generate 500 leads for my new product"
```

**To this:**
```
✅ Market research complete (competitor analysis, customer language, positioning gaps)
✅ 3-5 positioning angles generated
✅ Lead magnet created (10-page PDF guide)
✅ Landing page written and optimized
✅ 5-email nurture sequence deployed
✅ Campaign launched
✅ Performance tracking active
📊 Weekly reports: 487 signups and counting...
```

**In 10-14 days, with 2 approval checkpoints.**

---

## Quick Start

### For Simple Content

**Request:**
```
"Write a LinkedIn post about agent marketing systems"
```

**What happens:**
- Creative Specialist reads your voice DNA, ICP, and past learnings
- Creates post in your voice
- Quality Gate reviews (optional for simple posts)
- Returns polished post ready to publish

**Time:** 15-30 minutes

### For Full Campaigns

**Request:**
```
"Create a lead generation campaign for my developer CLI tool:
 - Lead magnet: CLI patterns guide
 - Landing page
 - 5-email sequence
 - Goal: 500 signups in 2 weeks"
```

**What happens:**

**Sprint 1 (3-5 days): Plan & Sketch**
- Research market landscape, competitors, customer language
- Generate 3-5 positioning angle options
- Design campaign structure
- **Checkpoint:** You approve strategic direction

**Sprint 2 (5-7 days): Refine & Deepen**
- Draft lead magnet, landing page, emails
- Run expert reviews (3-5 specialized agents analyze)
- Incorporate your feedback
- **Checkpoint:** You approve drafts and voice

**Sprint 3 (3-4 days): Execute & Ship**
- Polish assets to shipping quality
- Format for platforms
- Publish campaign
- Set up performance tracking

**Total time:** 11-16 days with 2 approval checkpoints

---

## The Team

### Campaign Lead (Coordinator)
**Role:** Design strategy, break campaigns into tasks, monitor progress, present checkpoints
**Does NOT:** Write content, conduct research, edit

**You'll interact with Campaign Lead for:**
- Campaign kickoff and design
- Sprint checkpoint approvals
- Progress updates
- Strategic decisions

### Research Specialist (Market Intelligence)
**Role:** Market research, competitor analysis, customer language mining, keyword research
**Delivers:** Research packages with actionable insights

**Example outputs:**
- Market landscape: Players, positioning, pricing models
- Customer language: Exact phrases customers use to describe pain points
- Positioning gaps: Differentiation opportunities competitors aren't exploiting

### Creative Specialist (Content Creator)
**Role:** Write all marketing assets in your voice using research insights
**Invokes:** Content skills (landing pages, emails, blogs, lead magnets, social posts)

**Example outputs:**
- Landing pages (direct-response, conversion-optimized)
- Email sequences (automated campaigns: nurture, onboarding, drip)
- Lead magnets (PDFs, checklists, templates, guides)
- Blog posts (SEO-optimized)
- Social posts (LinkedIn, Twitter, Substack Notes)

### Quality Gate (Editorial Review)
**Role:** Ensure voice match, quality standards, and craft before publishing
**Decides:** Approve for publishing or request revisions

**Evaluates against:**
- Voice fidelity (40%): Does this sound like you?
- Clarity & structure (25%): Scannable and logical?
- Craft quality (25%): Every sentence earning its place?
- Positioning alignment (10%): Reflects approved positioning angle?

### Distribution Specialist (Publishing & Analytics)
**Role:** Format for platforms, publish campaigns, track performance
**Delivers:** Ready-to-publish assets + performance reports

**Handles:**
- Platform optimization (LinkedIn, Twitter, email, web)
- Publishing coordination (correct sequence, timing)
- Analytics setup (GA, email platform, tracking pixels)
- Performance monitoring (daily in week 1, weekly ongoing)
- Optimization recommendations (data-driven improvements)

---

## How It Works

### Task-Based Coordination

Agents coordinate through **shared task lists** (not sequential handoffs).

**Traditional handoff model:**
```
Strategist → creates handoff.md → Researcher reads → hands to Writer → hands to Editor
```

**Task-based model (this system):**
```
Campaign Lead → creates task list with dependencies
Agents self-claim tasks when unblocked
Agents communicate via task comments
Everyone sees progress in real-time
```

**Benefits:**
- **Parallel work:** Multiple researchers, multiple writers work simultaneously
- **Clear dependencies:** Task can't start until X completes (explicit blocking)
- **Transparent progress:** Anyone can see task status
- **No file conflicts:** Agents own their phase outputs

### Sprint Model (Iterative Validation)

Campaigns execute in **3 sprints with checkpoints**, not one-shot linear execution.

**Why sprints?**
- Validate strategy before burning tokens on assets (Sprint 1 checkpoint)
- Get feedback on drafts before final production (Sprint 2 checkpoint)
- Avoid wrong direction → wrong execution → wasted work

| Sprint | Goal | You Review | Duration |
|--------|------|------------|----------|
| **Sprint 1: Plan & Sketch** | Validate campaign direction | ✅ Approve positioning & structure | 2-7 days |
| **Sprint 2: Refine & Deepen** | Create first drafts | ✅ Approve creative & voice | 3-10 days |
| **Sprint 3: Execute & Ship** | Polish & publish | (Auto - approved direction) | 2-5 days |

### File Ownership (Prevents Conflicts)

Each agent **creates NEW files** in their phase directory. No shared editing.

```
output/campaigns/dev-cli-launch-2026-02/
├── campaign-brief.md          (Campaign Lead maintains)
├── research/                  (Research Specialist creates)
├── drafts/                    (Creative Specialist creates)
├── edited/                    (Quality Gate creates)
├── ready/                     (Distribution Specialist creates)
└── analytics/                 (Distribution Specialist creates)
```

**Audit trail:** Draft → Edited → Ready (clear progression, no overwrites)

---

## Campaign Types

### 1. Lead Generation Campaign

**Goal:** Build email list with qualified leads

**Assets:**
- Lead magnet (PDF, checklist, template, guide)
- Landing page (opt-in focused)
- Thank you page (deliver lead magnet)
- 5-email nurture sequence
- (Optional) Blog post to drive traffic

**Timeline:** 10-14 days
**Token budget:** ~60-80K tokens

**Success metrics:**
- Email signups (primary goal)
- Opt-in rate (target: 8-12%)
- Email engagement (opens, clicks)
- Lead-to-customer conversion

### 2. Product Launch Campaign

**Goal:** Announce new offering, drive signups/sales

**Assets:**
- Sales page (conversion-optimized)
- Launch email sequence (3-5 emails to existing list)
- Supporting blog post (SEO, long-tail traffic)
- Social media assets (LinkedIn, Twitter)
- (Optional) Demo video script

**Timeline:** 14-21 days
**Token budget:** ~80-120K tokens

**Success metrics:**
- Signups or sales (primary goal)
- Conversion rate
- Revenue generated
- Traffic sources

### 3. Content Marketing Sprint

**Goal:** SEO-focused, long-tail traffic and authority building

**Assets:**
- 3-5 SEO-optimized blog posts
- Email to announce each post (to existing subscribers)
- Social promotion plan
- (Optional) Lead magnet to capture readers

**Timeline:** 10-14 days
**Token budget:** ~60-100K tokens

**Success metrics:**
- Organic traffic
- Keyword rankings
- Time on page
- Conversions (CTA clicks)

### 4. Re-engagement Campaign

**Goal:** Win back inactive leads/customers

**Assets:**
- Re-engagement email sequence (3-5 emails)
- Special offer or incentive
- Survey (if needed to understand why inactive)
- Sunset sequence (clean list of non-engagers)

**Timeline:** 7-10 days
**Token budget:** ~40-60K tokens

**Success metrics:**
- Re-engagement rate
- Conversion rate
- List cleaning (remove dead leads)

---

## Setup

### 1. Clone or Initialize Repository

```bash
git clone [repo-url] agent-marketing-team
cd agent-marketing-team
# OR
mkdir agent-marketing-team && cd agent-marketing-team && git init
```

### 2. Create Core Context Files

**Required before running any campaigns:**

#### `context/voice-dna.md`
Your unique voice profile. Analyze 3-5 writing samples to capture:
- Sentence rhythm and patterns
- Word choice and vocabulary
- Tone (formal/casual, personal/corporate)
- Personality traits
- What you'd never say

**Create with:** `/setup` skill or manually analyze samples

#### `context/icp.md`
Your ideal customer profile. Define:
- Who they are (demographics, role, company size)
- Pain points they experience
- Goals they're trying to achieve
- Language they use
- Where they hang out (channels, platforms)

**Create with:** `/setup` skill or interview-based questionnaire

#### `context/business-profile.md`
What you offer. Document:
- Products/services
- Unique value proposition
- Positioning (how you're different)
- Pricing model
- Customer results/testimonials

**Create with:** `/setup` skill or manual documentation

### 3. Set Up MCPs (For Advanced Research)

**Required for market intelligence:**
- **Perplexity MCP** - Deep market research, comprehensive answers
- **Firecrawl MCP** - Scrape competitor websites at scale
- **Playwright MCP** - Screenshot competitor pages, visual analysis

**Optional but valuable:**
- **Exa MCP** - Semantic search for similar content/companies
- **Brave Search MCP** - Real-time search results
- **Memory MCP** - Persist research findings across sessions

**Configure in Claude Code settings:**
```
~/.claude/mcp-config.json
```

### 4. First Campaign (Test Case)

**Recommended first campaign:**
```
"Create a simple lead magnet campaign:
 - Lead magnet: [Your expertise area] Starter Guide (PDF)
 - Landing page
 - 3-email delivery sequence
 - Goal: 50 signups in 1 week (low-stakes test)"
```

**This validates:**
- Task coordination works
- Sprint checkpoints function
- File ownership prevents conflicts
- Quality gates catch issues
- Voice matching is accurate

**Start small, then scale to complex campaigns.**

---

## Directory Structure

```
agent-marketing-team/
├── .claude/
│   ├── agents/                      # Team definitions
│   │   ├── TEAM.md                  # Philosophy & protocols
│   │   ├── campaign-lead.md
│   │   ├── research-specialist.md
│   │   ├── creative-specialist.md
│   │   ├── quality-gate.md
│   │   └── distribution-specialist.md
│   ├── skills/                      # Marketing frameworks
│   │   ├── positioning-angles/
│   │   ├── keyword-research/
│   │   ├── market-research/
│   │   ├── expert-review/
│   │   ├── lead-magnet-strategy/
│   │   ├── landing-page/
│   │   ├── email-sequence/
│   │   ├── blog-post/
│   │   └── [more content skills...]
│   ├── templates/                   # Campaign structures
│   └── workflows/                   # Multi-step processes
│
├── context/                         # Your persistent context
│   ├── voice-dna.md                 ⚠️  REQUIRED
│   ├── icp.md                       ⚠️  REQUIRED
│   ├── business-profile.md          ⚠️  REQUIRED
│   └── brand-guide.md (optional)
│
├── knowledge/                       # Knowledge base
│   ├── research/                    # Market research packages
│   ├── learnings/                   # Compounding patterns
│   │   └── campaigns/
│   │       ├── timing/
│   │       ├── asset-mix/
│   │       ├── coordination/
│   │       ├── task-patterns/
│   │       ├── quality-gates/
│   │       └── retrospectives/
│   └── feedback/
│       └── analytics/               # Performance data
│
├── output/                          # Generated campaigns
│   └── campaigns/
│       └── [campaign-slug]-[YYYY-MM]/
│           ├── campaign-brief.md
│           ├── research/
│           ├── drafts/
│           ├── edited/
│           ├── ready/
│           └── analytics/
│
├── CLAUDE.md                        # Routing & instructions
└── README.md                        # This file
```

---

## Product Requirements Document

### Document Type

**This is a PRD (Product Requirements Document), not an implementation plan.**

**What this defines:**
- **WHAT:** A coordinated agent marketing team system using Claude Code
- **WHY:** To execute full-funnel marketing campaigns autonomously
- **WHO:** The agents, their roles, and how they coordinate
- **WHEN:** Sprint-based execution with iterative checkpoints

**What this does NOT define:**
- **HOW:** Step-by-step implementation instructions (implementation determines exact details)
- **WHERE:** Specific line numbers, exact code (those are implementation details)

### Context

**Why this transformation:** Traditional writing teams use sequential handoffs where agents pass work linearly. This works well for single content pieces but cannot handle complex marketing campaigns requiring:
- Parallel research across multiple topic areas
- Coordinated multi-asset creation (lead magnets, landing pages, blogs, email sequences)
- Top-of-funnel campaigns with lead generation and nurturing
- Performance validation and analytics

**The solution:** Adopt Anthropic's agent teams pattern where agents coordinate through **shared task lists** (not handoffs), communicate **directly with each other**, and work **in parallel** when beneficial. A **Campaign Lead** orchestrates but doesn't implement, while specialist agents self-claim tasks from a shared list.

### The Realization: Writing Team → Marketing Team

After reviewing the Vibe Marketing Playbook, this isn't actually a writing team—it's a **marketing team**. The distinction matters:

**Writing team thinks:** "What content should we create?"
**Marketing team thinks:** "What business outcome do we need, and what assets get us there?"

### The Three-Layer Stack (Vibe Marketing)

```
┌─────────────────────────────────────────────────────────────┐
│                    LAYER 3: PROCESS                         │
│         Research → Foundation → Structure → Assets          │
│         ✅ This system (agent coordination via tasks)       │
├─────────────────────────────────────────────────────────────┤
│                  LAYER 2: METHODOLOGY                       │
│     Skills = marketing frameworks loaded on demand          │
│     ✅ This system (13+ content creation skills)            │
├─────────────────────────────────────────────────────────────┤
│                    LAYER 1: RESEARCH                        │
│        MCPs = real-time market intelligence                 │
│        ⚠️  Requires MCP setup (Perplexity, Firecrawl, etc.) │
└─────────────────────────────────────────────────────────────┘
```

### Key Differences from Writing System

| Aspect | Writing System | Marketing System |
|--------|----------------|------------------|
| **Focus** | Content pieces | Business outcomes |
| **Coordination** | Sequential handoffs | Task-based parallel work |
| **Research** | Content research (support claims) | Marketing research (inform strategy) |
| **Metrics** | Content performance | Funnel metrics (leads, conversions, ROI) |
| **Workflow** | Linear (write → edit → publish) | Sprint-based (plan → draft → polish) |
| **Validation** | Editor approval | Sprint checkpoints with user |

### Core Principles

#### 1. Task-Based Coordination (Not Handoffs)

Agents coordinate through **shared task lists** managed by Claude Code's TaskTool.

**Benefits:**
- Parallel work (multiple researchers, multiple writers)
- Clear dependencies (task can't start until X completes)
- Transparent progress (anyone can see task status)
- No file conflicts (agents own their phase outputs)

#### 2. Sprint Model (Iterative Validation)

Campaigns execute in **3 sprints with checkpoints**, not one-shot linear execution.

**Sprint 1: Plan & Sketch** (Strategy Validation)
- Research synthesis
- Positioning angle options
- Campaign structure sketch
- **Checkpoint:** User approves direction

**Sprint 2: Refine & Deepen** (Creative Iteration)
- First drafts (expect rejection/revision)
- Expert reviews
- Deeper research if needed
- **Checkpoint:** User approves creative and voice

**Sprint 3: Execute & Ship** (Final Production)
- Polish approved assets
- Platform formatting
- Publishing
- (No checkpoint - executing approved direction)

#### 3. The Vibe Marketing Insight: Options + Taste = Winners

> "AI generates options. Your taste picks winners. That's your advantage."

**How this works:**
1. **Agents generate variants** (positioning angles, headline options, email sequences)
2. **User picks winners** (using taste + business judgment)
3. **Agents optimize winners** (iterate on selected direction)

**Agents provide OPTIONS. User provides TASTE.**

#### 4. File Ownership Strategy (Avoid Conflicts)

Each agent **creates NEW files** in their phase directory. No shared editing.

| Phase | Owner | Creates Files In | Read-Only For |
|-------|-------|------------------|---------------|
| Research | Research Specialist | `knowledge/research/` | Writer, Strategist |
| Drafting | Creative Specialist | `output/campaigns/[name]/drafts/` | Editor |
| Editing | Quality Gate | `output/campaigns/[name]/edited/` | Publisher |
| Publishing | Distribution Specialist | `output/campaigns/[name]/ready/` | Analyst |
| Analysis | Distribution Specialist | `knowledge/feedback/analytics/` | Campaign Lead |

### Marketing Mindset Shifts

**We think in funnels, not pieces:**
- Top of funnel: Lead generation (lead magnets, landing pages, blogs)
- Middle of funnel: Nurture (email sequences, case studies, demos)
- Bottom of funnel: Conversion (sales pages, pricing, testimonials)

**We measure outcomes, not outputs:**
- Not "we published 5 pieces"
- Instead "we generated 500 qualified leads"

**We research first, create second:**
- Market landscape before positioning
- Customer language before copywriting
- Competitor analysis before differentiation

**We iterate until right:**
- Sprint 1: Strategy options
- Sprint 2: First drafts (expect rejection)
- Sprint 3: Polish and ship

### Success Criteria

✅ Campaign Lead can autonomously break down complex campaigns into task lists
✅ Specialist agents self-claim tasks without manual assignment
✅ Multiple researchers work in parallel on different topics
✅ Writers create multiple assets simultaneously after research completes
✅ No file conflicts occur (clear ownership per phase)
✅ Quality gates prevent unapproved content from publishing
✅ Distribution Specialist validates campaign performance against stated goals
✅ All content skills work unchanged within new system
✅ Knowledge compounding continues (learnings automatically applied)
✅ User can request full campaigns and receive coordinated execution

### Evolution: From v1.0 to v2.0

**v1.0 (Current):** Task-based coordination with sprint checkpoints
**v2.0 (Future):** Add Vibe Marketing research layer

**To add in v2.0:**
- MCPs for market intelligence (Perplexity, Firecrawl, Playwright)
- 5 new marketing skills (positioning-angles, keyword-research, market-research, expert-review, lead-magnet-strategy)
- Marketing strategist mindset (research-first, conversion-focused)
- Full-funnel campaign types (not just content campaigns)

**What's preserved:**
- Agent coordination via task lists ✅
- 13 content creation skills ✅
- Knowledge compounding ✅
- Context files (voice-dna, ICP, business) ✅

---

## Rollback Plan

If agent teams don't work as expected:

**Fallback 1:** Keep Campaign Lead but use Task tool to spawn agents (current Multi-Agent mode)
- Coordination through Campaign Lead remains
- Agents spawned explicitly rather than self-claiming

**Fallback 2:** Return to sequential handoffs for complex work
- Revert agent definitions to handoff protocols
- Keep task lists for tracking only (not coordination)

**Preserved in all cases:**
- All content creation skills
- Context files (voice-dna, ICP, business-profile)
- Knowledge compounding system
- Learnings database

---

## Contributing

This system is designed to compound. After each campaign:

1. **Run retrospective** - What worked, what didn't, what to optimize
2. **Extract learnings** - Codify patterns in `knowledge/learnings/campaigns/`
3. **Update agent definitions** - If process improvements emerge
4. **Share insights** - Help others learn from your campaigns

**The system gets better with every campaign.**

---

## License

[Specify license - MIT, proprietary, etc.]

---

## Acknowledgments

**Inspired by:**
- [Anthropic's Agent Teams Pattern](https://docs.anthropic.com/en/build-with-claude/agent-patterns)
- [Vibe Marketing Playbook](https://vibemarketing.com) - Marketing research frameworks
- A prior writing system (predecessor to this marketing system)

**Built with:**
- [Claude Code](https://claude.ai/claude-code) - AI agent coordination
- Claude 4.5/4.6 models - Content creation and analysis

---

*This is a marketing team. We compound knowledge, iterate relentlessly, and measure outcomes.*
