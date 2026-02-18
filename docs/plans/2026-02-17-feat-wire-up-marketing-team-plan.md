---
title: "feat: Wire Up Agent Marketing Team v1.1"
type: feat
status: completed
date: 2026-02-17
brainstorm: docs/brainstorms/2026-02-17-system-wiring-brainstorm.md
---

# feat: Wire Up Agent Marketing Team v1.1

## Overview

The v1.0 blueprint is complete: 5 specialized agents, task-based coordination, sprint model, file ownership strategy. But the system cannot run a campaign yet. This plan closes the gap between the well-architected design and an operational marketing team.

**Critical correction from brainstorm:** The reviewer's concern about TaskTool semantics was wrong. `TaskCreate`, `TaskUpdate` (with `owner`, `addBlockedBy`, `metadata`), `TaskList`, and `TaskGet` all exist in Claude Code and match the agent specifications exactly. No changes needed to the coordination model.

**What changes:** Context files need real content, skills directory needs SKILL.md files, CLAUDE.md needs trimming, directories need scaffolding, and workflows/templates need to be created.

---

## Problem Statement

The system cannot execute any campaign because:

1. **Context files are templates** — `voice-dna.md`, `icp.md`, `business-profile.md` contain placeholder text (`YOUR_NAME`, `pain point 1`). Every agent reads these before working. Empty = useless output.
2. **Skills directory is empty** — Creative Specialist references `/landing-page`, `/email-sequence`, etc., but no SKILL.md files exist. Agents fall back to generic prompting.
3. **Directory tree doesn't exist** — When Research Specialist tries to `Write(file_path="knowledge/research/...")`, the directory doesn't exist. First campaign will fail on first write.
4. **CLAUDE.md is 625 lines** — Loaded into every conversation as system context. This length eats context window and causes model to deprioritize later sections.
5. **Workflow files are missing** — `sprint-planning.md` and `retrospective.md` are referenced but absent.
6. **Missing templates** — 3 of 4 campaign templates don't exist yet.

---

## Proposed Solution

Sequential MVP: address gaps in dependency order so each phase unblocks the next.

```
Phase 1: Context     → Agents have real voice/ICP/business data
Phase 2: Scaffolding → File writes won't fail
Phase 3: Skills      → Creative Specialist uses frameworks, not generic prompting
Phase 4: CLAUDE.md   → System prompt is concise and actionable
Phase 5: Workflows   → Sprint and retrospective processes documented
Phase 6: Test        → Validate basic pipeline before running full campaigns
```

---

## Technical Considerations

### SKILL.md Format

Skills in this Claude Code system are markdown files loaded on demand. Each SKILL.md should follow this pattern:

```markdown
# Skill Name

## Purpose
When to invoke this skill and what it produces.

## Required Inputs
- context/voice-dna.md
- context/icp.md
- [any research packages or campaign brief]

## Framework
Step-by-step process the Creative Specialist follows.

## Output Format
What the deliverable looks like, where to save it.

## Quality Checklist
- [ ] Voice match verified against voice-dna.md
- [ ] ICP relevance checked
- [ ] [skill-specific criteria]
```

### CLAUDE.md Trimming Strategy

Current CLAUDE.md (625 lines) contains three layers:
1. **Routing rules** — keep (agents need this in every context)
2. **Core principles** — keep (high-signal, short)
3. **Detailed campaign flows + multi-agent coordination walkthroughs** — move to `campaign-lead.md`

Campaign Lead already has detailed workflow docs (639 lines). The CLAUDE.md campaign flow examples duplicate what's in the agent file. Target: CLAUDE.md under 200 lines.

### Directory Scaffolding

Git won't track empty directories, so `.gitkeep` files or an init script must create the tree:

```
knowledge/
├── research/
├── learnings/campaigns/{timing,asset-mix,coordination,task-patterns,quality-gates,retrospectives}/
├── archive/
└── feedback/analytics/

output/campaigns/

.claude/skills/
.claude/workflows/
```

### Context File Population Approach

Use the `writer:setup` skill interactively — it's designed to capture voice, audience, and context through dialogue. This is better than having an agent guess at Christopher's voice from nothing.

Alternative: Manually populate the template files following the section headers already in each file.

---

## Implementation Phases

### Phase 1: Context Population (Critical Path — Blocks Everything)

**Goal:** Real voice, ICP, and business data so agents produce useful output.

**Files to populate:**
- `context/voice-dna.md` — Voice analysis from writing samples (sentence patterns, vocabulary, tone, what you'd never say, 3-5 samples)
- `context/icp.md` — Ideal customer profile (demographics, pain points, goals, exact language, channels, objections)
- `context/business-profile.md` — What you offer, differentiators, pricing, results, story

**Method:** Run `writer:setup` skill which captures voice/audience/context through structured dialogue.

**Acceptance criteria:**
- [ ] `voice-dna.md` contains actual writing samples (not placeholders)
- [ ] `icp.md` contains named persona with real pain points in the ICP's own language
- [ ] `business-profile.md` contains actual products/services and value proposition
- [ ] Status line in each file updated from "TEMPLATE" to reflect completion

---

### Phase 2: Directory Scaffolding

**Goal:** Prevent write failures when agents try to create research packages or campaign outputs.

**Files to create:**

```
knowledge/research/.gitkeep
knowledge/learnings/campaigns/timing/.gitkeep
knowledge/learnings/campaigns/asset-mix/.gitkeep
knowledge/learnings/campaigns/coordination/.gitkeep
knowledge/learnings/campaigns/task-patterns/.gitkeep
knowledge/learnings/campaigns/quality-gates/.gitkeep
knowledge/learnings/campaigns/retrospectives/.gitkeep
knowledge/archive/.gitkeep
knowledge/feedback/analytics/.gitkeep
output/campaigns/.gitkeep
.claude/skills/.gitkeep
.claude/workflows/.gitkeep
.claude/agents/handoffs/.gitkeep
.claude/agents/feedback/.gitkeep
```

**Implementation:**
```bash
# Create all directories with .gitkeep files
mkdir -p knowledge/research knowledge/learnings/campaigns/{timing,asset-mix,coordination,task-patterns,quality-gates,retrospectives} knowledge/archive knowledge/feedback/analytics output/campaigns .claude/skills .claude/workflows .claude/agents/handoffs .claude/agents/feedback

# Touch .gitkeep in each empty dir
find knowledge output/.claude -type d -empty -exec touch {}/.gitkeep \;
```

**Acceptance criteria:**
- [x] All referenced directories exist on disk
- [x] `knowledge/research/` is writable
- [x] `output/campaigns/` is writable
- [x] `.claude/skills/` exists

---

### Phase 3: Content Skills (7 SKILL.md Files)

**Goal:** Creative Specialist uses proven frameworks instead of generic prompting.

**Files to create (in `.claude/skills/`):**

#### `landing-page/SKILL.md`
Direct-response landing page framework. Sections: above-fold hook, problem agitation, solution reveal, proof block, offer stack, CTA. Required inputs: ICP, research package, campaign brief. Output: `drafts/landing-page-draft.md`.

#### `email-sequence/SKILL.md`
Automated email campaign framework. Covers: drip, nurture, onboarding sequences. 5-part structure: story, problem, solution, proof, action. Output: numbered email files in `drafts/email-sequence/`.

#### `blog-post/SKILL.md`
SEO-optimized article framework. Keyword integration, header structure, internal linking strategy, meta description. Output: `drafts/blog-[topic]-draft.md`.

#### `newsletter/SKILL.md`
Email newsletter framework. Personal story hook, insight or lesson, specific example, CTA. Output: `drafts/newsletter-[date]-draft.md`.

#### `social-post/SKILL.md`
Platform-optimized posts for LinkedIn, Twitter/X, Substack Notes. Hook patterns, engagement mechanics, hashtag strategy by platform. Output: `drafts/social-[platform]-[topic]-draft.md`.

#### `lead-magnet/SKILL.md`
High-value opt-in content creation. Checklist, guide, template, mini-course formats. Value-density test, title formula (specific + outcome + timeframe). Output: `drafts/lead-magnet-[title]-draft.md`.

#### `repurpose/SKILL.md`
Multi-platform adaptation of existing content. Content audit, platform fit analysis, reformatting rules by platform. Output: `drafts/repurposed/[platform]-[original-title]-draft.md`.

**Acceptance criteria:**
- [x] All 7 SKILL.md files exist in `.claude/skills/[name]/SKILL.md`
- [x] Each file has: Purpose, Required Inputs, Framework, Output Format, Quality Checklist
- [x] Creative Specialist can invoke each skill without needing to improvise the framework
- [x] Voice-matching checklist included in each skill

---

### Phase 4: CLAUDE.md Trimming

**Goal:** System prompt under 200 lines. Fast loading, high signal-to-noise.

**What to keep in CLAUDE.md:**
- Team table (5 agents + roles) — 8 lines
- Routing rules with trigger keywords — ~80 lines
- Core principles (task-based, sprint model, funnel thinking) — ~30 lines
- Available skills list — ~20 lines
- Quick start commands — ~20 lines

**What to move to `campaign-lead.md`:**
- Full multi-agent campaign flow walkthroughs (Sprint 1/2/3 detailed breakdowns) — already largely present in campaign-lead.md
- Detailed routing examples with code blocks

**Files to modify:**
- `CLAUDE.md` — Trim from 625 → ~180 lines
- `.claude/agents/campaign-lead.md` — Add "Campaign Flows Reference" section with the moved content

**Acceptance criteria:**
- [x] `CLAUDE.md` is ≤ 200 lines
- [x] All routing rules preserved (none removed, just campaign flow examples moved)
- [x] Campaign Lead agent file contains moved campaign flow content
- [x] Core principles remain intact in CLAUDE.md

---

### Phase 5: Workflows and Missing Templates

**Goal:** Complete the documented directory structure.

**Files to create:**

#### `.claude/workflows/sprint-planning.md`
Sprint planning workflow: how Campaign Lead breaks campaigns into Sprint 1/2/3 tasks, dependency graph rules, task granularity guidelines (30min–3hr per task), how to present sprint checkpoints to user.

#### `.claude/workflows/retrospective.md`
Campaign retrospective workflow: 5 retrospective questions, learnings extraction format, how to save patterns to `knowledge/learnings/campaigns/`, what categories to use.

#### `.claude/templates/lead-gen-campaign.md`
Lead generation campaign template: audience + problem statement, 3-5 asset plan (lead magnet + landing page + email sequence), success metrics, timeline. Fills in `campaign-brief.md` for lead gen campaigns.

#### `.claude/templates/product-launch.md`
Product launch campaign template: launch announcement structure, pre-launch warming sequence, launch day assets, post-launch follow-up.

#### `.claude/templates/content-sprint.md`
Content sprint template: 30-day content calendar structure, blog post schedule, social post plan, newsletter cadence.

**Acceptance criteria:**
- [x] `sprint-planning.md` exists with step-by-step sprint workflow
- [x] `retrospective.md` exists with retrospective questions and learnings format
- [x] All 3 campaign templates exist and follow `campaign-brief-template.md` format
- [x] Templates are referenced from CLAUDE.md Available Skills section

---

### Phase 6: Smoke Test

**Goal:** Validate basic pipeline works before attempting a full campaign.

**Test request:** "Write a LinkedIn post about why marketing teams need to think in funnels, not pieces."

**Expected execution path:**
1. Creative Specialist self-claims task
2. Reads `context/voice-dna.md`, `context/icp.md`
3. Searches `knowledge/learnings/` for relevant patterns (empty — OK)
4. Invokes `.claude/skills/social-post/SKILL.md`
5. Creates `output/campaigns/smoke-test-2026-02/drafts/social-linkedin-funnels-draft.md`
6. Self-assesses against voice checklist
7. Returns draft to user

**Red flags to watch for:**
- Voice doesn't match Christopher's style → improve `voice-dna.md`
- Agent asks many questions → context files need more detail
- Directory write fails → Phase 2 scaffolding missed a directory
- Agent ignores skill framework → check skill invocation pattern in creative-specialist.md

**Optional second test (after smoke test passes):** "Write a 3-email welcome sequence for [product]" — validates email sequence skill and directory structure.

**Acceptance criteria:**
- [ ] LinkedIn post is generated without errors
- [ ] Output file created in correct location
- [ ] Voice matches Christopher's actual writing style
- [ ] Agent did not invent its own framework (used social-post skill)

---

## Dependencies

```
Phase 1 (Context)
    ↓ (agents need real data to produce useful output)
Phase 2 (Scaffolding)  ← can run in parallel with Phase 1
    ↓ (directories must exist before skills can write)
Phase 3 (Skills)
    ↓ (agents must be able to invoke skills)
Phase 4 (CLAUDE.md)    ← can run in parallel with Phase 3
    ↓
Phase 5 (Workflows)    ← can run in parallel with Phase 3
    ↓ (all wiring complete)
Phase 6 (Smoke Test)
```

**Parallelizable:**
- Phase 2 + Phase 1 (scaffolding doesn't need context data)
- Phase 3 + Phase 4 + Phase 5 (all can run after Phase 2)

---

## Success Metrics

| Metric | Target | How to Measure |
|--------|--------|----------------|
| LinkedIn post passes voice check | >8/10 voice fidelity | Compare to actual Christopher writing |
| Agent asks questions | < 2 per task | Count clarifying questions during smoke test |
| Directory write errors | 0 | Run smoke test without file errors |
| CLAUDE.md length | ≤ 200 lines | `wc -l CLAUDE.md` |
| Skills invoked correctly | 7/7 | Each skill referenced in task output |

---

## Dependencies & Risks

### Critical Risk: Context Quality
**Risk:** If `voice-dna.md` is populated with generic descriptions instead of actual writing samples and patterns, all content will sound like AI, not Christopher.

**Mitigation:** Use `writer:setup` skill which extracts voice through structured analysis of real writing samples. Provide 3-5 actual pieces of writing for analysis. Better to spend 30 minutes here than redo 7 skills.

### Risk: Skill Framework Fidelity
**Risk:** If SKILL.md files are too high-level, Creative Specialist will improvise and bypass the framework.

**Mitigation:** Each skill should include concrete templates, specific decision trees, and explicit output format. Vague skills = vague output.

### Risk: CLAUDE.md Trimming Breaks Routing
**Risk:** Removing lines from CLAUDE.md might accidentally remove routing keywords that agents depend on.

**Mitigation:** Test routing after trimming by asking for a simple content piece and a campaign request — verify correct agent activation.

---

## Files Changed

### New Files
```
.claude/skills/landing-page/SKILL.md
.claude/skills/email-sequence/SKILL.md
.claude/skills/blog-post/SKILL.md
.claude/skills/newsletter/SKILL.md
.claude/skills/social-post/SKILL.md
.claude/skills/lead-magnet/SKILL.md
.claude/skills/repurpose/SKILL.md
.claude/workflows/sprint-planning.md
.claude/workflows/retrospective.md
.claude/templates/lead-gen-campaign.md
.claude/templates/product-launch.md
.claude/templates/content-sprint.md
knowledge/research/.gitkeep
knowledge/learnings/campaigns/[6 subdirs]/.gitkeep
knowledge/archive/.gitkeep
knowledge/feedback/analytics/.gitkeep
output/campaigns/.gitkeep
.claude/agents/handoffs/.gitkeep
.claude/agents/feedback/.gitkeep
```

### Modified Files
```
CLAUDE.md                    → Trim from 625 to ~180 lines
.claude/agents/campaign-lead.md → Add campaign flow reference section
context/voice-dna.md         → Populate with real data
context/icp.md               → Populate with real data
context/business-profile.md  → Populate with real data
```

---

## References

- Brainstorm: `docs/brainstorms/2026-02-17-system-wiring-brainstorm.md`
- Agent definitions: `.claude/agents/[agent-name].md`
- Team philosophy: `.claude/agents/TEAM.md`
- Campaign brief template: `.claude/templates/campaign-brief-template.md`
- Implementation summary: `IMPLEMENTATION-SUMMARY.md`
