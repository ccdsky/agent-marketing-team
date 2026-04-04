# SkillsBench-Informed Plugin Improvements

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Apply the 7 key findings from the SkillsBench paper to improve this plugin's skill and agent architecture for measurably better outcomes.

**Architecture:** Restructure skills from monolithic comprehensive documents into focused core + reference modules. Compress agent definitions to reduce always-loaded context. Add worked examples to every content skill. Implement selective skill loading so agents consume 2-3 skills per task instead of all 15.

**Tech Stack:** Markdown, Claude Code plugin conventions (SKILL.md frontmatter, agent YAML)

---

## Research Summary: What the Paper Found

| Finding | Data | Implication for This Plugin |
|---------|------|-----------------------------|
| **F1: Skills help (+16.2pp avg)** | Range: +13.6pp to +23.3pp across configs | Our skills architecture is sound — optimize, don't rebuild |
| **F2: Claude Code + Opus gets highest improvement** | +23.3pp gain with native skill integration | We're on the right harness — focus on skill quality |
| **F3: Self-generated skills don't help** | −1.3pp average | Our human-curated frameworks (Schwartz, Cialdini, etc.) are the right approach |
| **F4: Domain variance is huge** | Media & Content: +13.9pp vs Healthcare: +51.9pp | Content/marketing is a well-pretrained domain — our skills need to add non-obvious procedural value, not reiterate general knowledge |
| **F5: 2-3 skills optimal, 4+ shows diminishing returns** | 2-3: +18.6pp, 4+: +5.9pp | Currently agents see 5-15 skills. Need selective loading |
| **F6: Detailed > Compact > Standard > Comprehensive** | Detailed: +18.8pp, Comprehensive: −2.9pp | Our strategy skills (3,000-3,650 tokens) are in the "comprehensive" danger zone |
| **F7: Smaller model + skills ≈ larger model without** | Haiku+Skills > Opus without | Skills quality directly determines cost efficiency |

### Token Budget Targets (from paper's ecosystem analysis)

- **Optimal SKILL.md size:** ~1,500 tokens median (Figure 6)
- **Current plugin skill sizes:** 1,445–3,650 tokens (strategy skills are 2-2.5× too long)
- **Current agent definition sizes:** 2,188–5,758 tokens (always loaded, compounding the problem)
- **Total always-loaded context (CLAUDE.md + TEAM.md + agent def):** ~10,000+ tokens before any skill is even read

---

## Current State Diagnosis

### Problem 1: Strategy Skills Are Comprehensive (F6 violation)

These skills exceed the "detailed" sweet spot and enter "comprehensive" territory where performance *degrades*:

| Skill | Current Tokens | Target | Reduction |
|-------|---------------|--------|-----------|
| `market-research` | ~3,623 | ~1,800 | 50% |
| `lead-magnet-strategy` | ~3,650 | ~1,800 | 51% |
| `keyword-research` | ~3,274 | ~1,800 | 45% |
| `positioning-angles` | ~2,950 | ~1,800 | 39% |
| `expert-review` | ~2,922 | ~1,800 | 38% |

### Problem 2: Too Many Skills Per Task (F5 violation)

Current flow: Campaign Lead references all 15 skills in CLAUDE.md routing table → specialist agents read their agent definition (which references 5-7 skills) → agent reads each skill before executing. This means 5-7 full skill documents loaded per specialist session.

### Problem 3: No Worked Examples (Discussion finding)

The paper's Discussion section states: *"concise, stepwise guidance with at least one working example is often more effective than exhaustive documentation."* Current skills have detailed frameworks but zero concrete output examples showing what a finished deliverable looks like.

### Problem 4: Agent Definitions Too Heavy

Agent definitions are always-loaded context that compounds with skills:

| Agent | Current Tokens | Issue |
|-------|---------------|-------|
| `distribution-specialist` | ~5,758 | Larger than most skills — includes full platform formatting guides |
| `campaign-lead` | ~4,702 | Includes campaign brief template inline |
| `quality-gate` | ~3,423 | Rubric detail could be a reference file |

### Problem 5: Harness Format Drift (Discussion finding)

The paper found that *"Skills should explicitly match harness constraints (e.g., repeated format reminders)."* Current skills don't include Claude Code-specific output format reminders (file paths, task metadata conventions).

---

## Implementation Plan

### Task 1: Extract Reference Material from Strategy Skills

**Rationale (F6):** Move methodology deep-dives, example tables, and edge-case guidance out of SKILL.md into `references/` files. Keep SKILL.md focused on the core procedure + decision points + one worked example.

**Files:**
- Modify: `skills/market-research/SKILL.md`
- Create: `skills/market-research/references/methodology.md`
- Modify: `skills/lead-magnet-strategy/SKILL.md`
- Create: `skills/lead-magnet-strategy/references/methodology.md`
- Modify: `skills/keyword-research/SKILL.md`
- Create: `skills/keyword-research/references/methodology.md`
- Modify: `skills/positioning-angles/SKILL.md`
- Create: `skills/positioning-angles/references/methodology.md`
- Modify: `skills/expert-review/SKILL.md`
- Create: `skills/expert-review/references/panels.md`

**Pattern for each skill (apply consistently):**

- [ ] **Step 1: Read the current SKILL.md and identify what's core vs reference**

Core (keep in SKILL.md): Frontmatter, purpose, required inputs, step-by-step procedure (compressed), output format, one worked example.

Reference (extract): Methodology sourcing paragraphs, detailed framework tables with 5+ rows of options, edge-case handling, advanced variations.

Rule of thumb: If a section provides *options to choose from* (e.g., expert panel compositions, 12-step keyword process), it's reference material. If it provides *decisions to make in sequence*, it's core.

- [ ] **Step 2: Create `references/methodology.md` with extracted content**

Include a header: `# [Skill Name] — Extended Reference` and organize by section.

- [ ] **Step 3: Rewrite SKILL.md to ~1,800 tokens**

Structure:
```markdown
---
name: [skill-name]
description: [one-line — used for skill discovery]
---

# [Skill Name]

## When to Use
[1-2 sentences]

## Required Inputs
[File paths to read — keep existing list]

## Procedure
[Numbered steps — the core decision sequence, compressed]
[Each step: what to decide, what to produce, where to save]
[Reference: "For [detail], see references/methodology.md"]

## Output Format
[Exact file path pattern + required sections in output file]

## Example
[One concrete, abbreviated worked example showing the output structure with realistic content — not a full deliverable, but enough to show what "done" looks like]
```

- [ ] **Step 4: Verify the reference file is discoverable**

Add to SKILL.md procedure steps: `For [specific detail], read references/methodology.md` — agents will only load the reference when they need it.

- [ ] **Step 5: Verify token count is ≤ 2,000**

```bash
wc -c skills/[name]/SKILL.md | awk '{print int($1/4), "tokens"}'
```

**Repeat Steps 1-5 for each of the 5 strategy skills listed above.**

---

### Task 2: Add Worked Examples to Content Skills

**Rationale (Discussion):** The paper found that "stepwise guidance with at least one working example" drives the most improvement. Content skills (landing-page, email-sequence, blog-post, newsletter, social-post, lead-magnet) currently have zero output examples.

**Files:**
- Modify: `skills/landing-page/SKILL.md`
- Modify: `skills/email-sequence/SKILL.md`
- Modify: `skills/blog-post/SKILL.md`
- Modify: `skills/newsletter/SKILL.md`
- Modify: `skills/social-post/SKILL.md`
- Modify: `skills/lead-magnet/SKILL.md`
- Modify: `skills/repurpose/SKILL.md`

**For each content skill:**

- [ ] **Step 1: Write an abbreviated worked example**

The example should be for a fictional B2B SaaS product (e.g., "Acme DevOps — a CI/CD platform for mid-market engineering teams"). Use the same fictional product across all examples for consistency.

The example is NOT a full deliverable. It's a structural skeleton showing:
- What the output file looks like
- How each section maps to the framework steps
- What "good" looks like for 2-3 sections (write those fully)
- What the remaining sections contain (1-line placeholders like `[Section 4: Proof — 3 case study summaries with specific metrics]`)

Target: 300-500 tokens per example.

- [ ] **Step 2: Add the example to the end of SKILL.md**

Add under a `## Example` heading. Keep existing skill content unchanged for content skills (they're already in the "detailed" range at 1,500-2,300 tokens).

- [ ] **Step 3: If adding the example pushes the skill over ~2,500 tokens, compress the framework section**

Move any "formula options" lists (e.g., the 4 headline formulas in landing-page) to a `references/` file. Keep only the top 2 options inline.

- [ ] **Step 4: Verify total size**

```bash
wc -c skills/[name]/SKILL.md | awk '{print int($1/4), "tokens"}'
```

Target: ≤ 2,500 tokens for content skills (they benefit from examples more than strategy skills).

**Repeat for all 7 content skills.**

---

### Task 3: Compress Agent Definitions

**Rationale (F5, F6):** Agent definitions are always-loaded context. Every token in an agent file competes with skill tokens for the context budget. The distribution-specialist at 5,758 tokens is larger than most skills.

**Files:**
- Modify: `agents/distribution-specialist.md`
- Create: `agents/references/platform-formats.md`
- Modify: `agents/campaign-lead.md`
- Create: `agents/references/campaign-templates.md`
- Modify: `agents/quality-gate.md`
- Create: `agents/references/review-rubric.md`

#### 3a: Distribution Specialist (~5,758 → ~2,500 tokens)

- [ ] **Step 1: Read the full file and identify extractable content**

```
Read(file_path="agents/distribution-specialist.md")
```

The platform-specific formatting guides (LinkedIn character limits, email subject line rules, Twitter thread formatting, web meta tag templates) are reference material — only needed when formatting for that specific platform.

- [ ] **Step 2: Create `agents/references/platform-formats.md`**

Move all platform-specific formatting sections here. Organize by platform with clear headers so agents can read just the section they need.

- [ ] **Step 3: Rewrite distribution-specialist.md**

Keep: Role definition, responsibilities list, self-claiming workflow, analytics tier structure (this is core — it defines how the agent thinks about measurement).

Replace platform sections with: `For [platform] formatting guidelines, read agents/references/platform-formats.md`

- [ ] **Step 4: Verify ≤ 2,500 tokens**

#### 3b: Campaign Lead (~4,702 → ~2,800 tokens)

- [ ] **Step 5: Extract campaign brief template and sprint task templates**

Move the campaign-brief.md template and the full sprint task-creation examples to `agents/references/campaign-templates.md`.

Keep: Role definition, workflow sequence (numbered steps), checkpoint presentation format, escalation rules.

- [ ] **Step 6: Verify ≤ 2,800 tokens**

#### 3c: Quality Gate (~3,423 → ~2,200 tokens)

- [ ] **Step 7: Extract detailed rubric examples**

Move the per-criteria scoring examples and sprint-specific threshold tables to `agents/references/review-rubric.md`.

Keep: Role definition, 4-criteria rubric (names + weights), approve/revise decision tree, the rule about serial task claiming.

- [ ] **Step 8: Verify ≤ 2,200 tokens**

---

### Task 4: Implement Selective Skill Loading

**Rationale (F5):** 2-3 skills per task is optimal. Currently agents reference 5-7 skills each. The fix is to make agents load skills on-demand based on the specific task they've claimed, not pre-load all skills for their role.

**Files:**
- Modify: `agents/research-specialist.md`
- Modify: `agents/creative-specialist.md`
- Modify: `agents/TEAM.md`

- [ ] **Step 1: Add skill-loading protocol to TEAM.md**

Add a new section after "Pre-Task Protocol" called "Skill Loading Protocol":

```markdown
## Skill Loading Protocol

Load skills **on-demand per task**, not all skills for your role.

**Rule:** Read at most 2 skill SKILL.md files per task. If a task spans two skill domains (e.g., "write a landing page with email sequence"), read both. Never pre-load skills you might not need.

**How to load:** When you claim a task, identify the 1-2 most relevant skills from the routing table below, then:
1. Read the SKILL.md for the primary skill
2. If needed, read the SKILL.md for a secondary skill
3. If you need deep methodology detail during execution, read the skill's references/ files

**Do NOT pre-read all skills before claiming tasks.**
```

- [ ] **Step 2: Update research-specialist.md**

Replace the current "Capabilities" section (which lists all 6 research skills with full descriptions) with a skill routing table:

```markdown
## Skill Routing (load on claim, max 2 per task)

| Task Keywords | Primary Skill | Secondary (if needed) |
|---------------|---------------|----------------------|
| market research, competitors, landscape | `/market-research` | — |
| positioning, angles, differentiation | `/positioning-angles` | `/market-research` |
| keywords, SEO, search terms | `/keyword-research` | — |
| lead magnet concept, opt-in strategy | `/lead-magnet-strategy` | `/positioning-angles` |
| ad angles, creative angles, variations | `/ad-angles` | `/positioning-angles` |
| proof, testimonials, case studies | `/proof-harvesting` | — |
```

- [ ] **Step 3: Update creative-specialist.md**

Same pattern — replace the full skill descriptions with a routing table:

```markdown
## Skill Routing (load on claim, max 2 per task)

| Task Keywords | Primary Skill | Secondary (if needed) |
|---------------|---------------|----------------------|
| landing page, conversion page | `/landing-page` | — |
| email, drip, nurture, onboarding | `/email-sequence` | — |
| blog, article, SEO content | `/blog-post` | — |
| newsletter, email newsletter | `/newsletter` | — |
| LinkedIn, Twitter, social | `/social-post` | — |
| lead magnet, guide, checklist | `/lead-magnet` | `/lead-magnet-strategy` |
| repurpose, adapt, multi-platform | `/repurpose` | — |
| expert review, expert panel | `/expert-review` | — |
```

- [ ] **Step 4: Verify agent definitions didn't grow**

The routing tables should be *shorter* than the current full-description sections they replace.

---

### Task 5: Add Harness Format Reminders to Skills

**Rationale (Discussion):** The paper found that skills should "explicitly match harness constraints." Claude Code agents work through file I/O and task metadata. Skills should reinforce this.

**Files:**
- Modify: All 15 `skills/*/SKILL.md` files

- [ ] **Step 1: Add a standardized "Output" section to each skill**

At the end of each skill's procedure, before the example, add:

```markdown
## Output

**Save to:** `[exact path pattern with placeholders]`
**Mark complete with:**
```
TaskUpdate(taskId="[ID]", status="completed", metadata={
  "deliverable": "[path to file you just wrote]",
  "assessment": "[1-line self-score: voice/10, clarity/10, craft/10]",
  "ready_for": "[next-agent-role]"
})
```
```

This reinforces the harness convention from TEAM.md at the point where agents are about to produce output — reducing format drift.

- [ ] **Step 2: Verify each skill has an explicit file path pattern**

Check that every skill specifies WHERE to save output. Current state: some skills say "save to `knowledge/research/`" but don't give the full filename pattern. Fix any that are vague.

Example fix:
- Before: "Save research to the knowledge directory"
- After: "Save to: `knowledge/research/[topic]-[YYYY-MM-DD].md`"

---

### Task 6: Compress TEAM.md and CLAUDE.md

**Rationale (F5, F6):** These files are loaded into EVERY agent session. Every token here is permanent context overhead.

**Files:**
- Modify: `agents/TEAM.md` (~2,188 tokens → ~1,600 tokens)
- Modify: `CLAUDE.md` (review for redundancy with TEAM.md)

- [ ] **Step 1: Audit TEAM.md for content that duplicates agent definitions**

The "Agent Protocol (Self-Claiming)" section (lines 146-193) repeats workflow that each agent's own definition already covers. Compress to a 3-line summary with a pointer: "See your agent definition for role-specific task keywords."

- [ ] **Step 2: Compress the escalation format template**

The full markdown escalation template (lines 199-219) is nice-to-have but takes ~200 tokens. Replace with a 2-line instruction: "Escalate with: situation, options (with tradeoffs), your recommendation, decision needed."

- [ ] **Step 3: Audit CLAUDE.md for redundancy**

CLAUDE.md contains the full routing table with keywords, example triggers, and flow descriptions for all 5 agents. This is ~1,500 tokens of always-loaded context. Compress to:
- Agent name + 1-line role description + skill count
- Remove the "Route when" example phrases (the agent definitions handle routing)
- Remove the "Flow" descriptions (TEAM.md and agent definitions cover this)

- [ ] **Step 4: Verify total always-loaded context budget**

Target: CLAUDE.md + TEAM.md + one agent definition < 6,000 tokens total (down from ~10,000+). This leaves more budget for the 2-3 skills that actually execute the task.

---

### Task 7: Validate Changes End-to-End

**Files:**
- All modified files from Tasks 1-6

- [ ] **Step 1: Token budget audit**

Run token estimates on all modified files:
```bash
for f in skills/*/SKILL.md agents/*.md CLAUDE.md; do
  chars=$(wc -c < "$f")
  tokens=$((chars / 4))
  echo "$f: ~${tokens} tokens"
done
```

Verify:
- No SKILL.md exceeds 2,500 tokens
- No agent definition exceeds 3,000 tokens (except campaign-lead at 2,800)
- CLAUDE.md + TEAM.md combined < 3,500 tokens

- [ ] **Step 2: Reference completeness check**

Verify every `references/` pointer in a SKILL.md or agent file points to a file that exists:
```bash
grep -r "references/" skills/*/SKILL.md agents/*.md | grep -oP 'references/[^\s\)`]+' | sort -u
```

Then check each path exists.

- [ ] **Step 3: Skill loading simulation**

Walk through a realistic task to verify the selective loading works:

Scenario: "Write a landing page for our new CI/CD product"
1. Campaign Lead reads CLAUDE.md → routes to Creative Specialist
2. Creative Specialist reads `agents/creative-specialist.md` → sees routing table → loads `/landing-page` skill only
3. Creative Specialist reads `skills/landing-page/SKILL.md` (~2,200 tokens) → sees worked example → writes draft
4. Total skill context: ~2,200 tokens (down from ~12,000+ if all content skills were loaded)

Scenario: "Research the competitive landscape for developer tools"
1. Campaign Lead reads CLAUDE.md → routes to Research Specialist
2. Research Specialist reads `agents/research-specialist.md` → sees routing table → loads `/market-research` skill only
3. Research Specialist reads `skills/market-research/SKILL.md` (~1,800 tokens)
4. Midway through, needs detailed methodology → reads `references/methodology.md` on demand
5. Total skill context: ~1,800 tokens core + ~1,800 tokens reference when needed (down from loading all 6 research skills)

- [ ] **Step 4: Verify no content was lost**

Grep for key framework terms that should still be findable somewhere in the skill directory (SKILL.md or references/):
```bash
for term in "Schwartz" "Masterson" "Cialdini" "Dunford" "Hormozi" "JTBD" "Kahneman"; do
  echo "--- $term ---"
  grep -rl "$term" skills/ agents/
done
```

All terms should still appear — just moved from SKILL.md to references/ where appropriate.

- [ ] **Step 5: Commit changes**

```bash
git add skills/ agents/ CLAUDE.md docs/
git commit -m "refactor: apply SkillsBench findings — compress skills, add examples, selective loading

- Compress 5 strategy skills from ~3,000-3,650 to ~1,800 tokens (F6: detailed > comprehensive)
- Extract methodology deep-dives to references/ subdirectories
- Add worked examples to 7 content skills (Discussion: examples drive improvement)
- Compress 3 agent definitions by 40-55% (reduce always-loaded context)
- Implement selective skill loading: max 2 skills per task (F5: 2-3 optimal)
- Add harness format reminders to all skills (Discussion: match harness constraints)
- Compress TEAM.md and CLAUDE.md to reduce permanent context overhead

Based on SkillsBench (Li et al., 2026) findings across 7,308 trajectories."
```

---

## Expected Impact

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Avg skill tokens loaded per task | ~8,000-12,000 | ~2,000-4,000 | −60-70% |
| Always-loaded context (CLAUDE.md + TEAM.md + agent) | ~10,000+ | ~5,500-6,000 | −40% |
| Skills with worked examples | 0/15 | 14/15 (all except /init) | +14 |
| Largest skill (SKILL.md only) | 3,650 tokens | ~2,500 tokens | −32% |
| Largest agent definition | 5,758 tokens | ~2,500 tokens | −57% |
| Reference material accessible | 0 files | ~8 reference files | On-demand loading |

**Predicted outcome improvement (based on paper's findings):**
- Moving from "comprehensive" to "detailed" skills: +18.8pp vs −2.9pp = ~+21pp potential swing on strategy tasks
- Reducing skill count per task from 5-7 to 2-3: +18.6pp vs +5.9pp = ~+13pp potential swing
- Adding worked examples: qualitative improvement (paper doesn't isolate this, but Discussion identifies it as the #1 authoring recommendation)

These improvements compound: better skill quality × fewer distracting skills × clearer output examples = significantly more reliable campaign execution.

---

## Order of Execution

Tasks 1-3 can run in parallel (independent file sets). Task 4 depends on Tasks 1-3 (needs compressed skills/agents to write routing tables against). Task 5 can run in parallel with Task 4. Task 6 can run in parallel with Tasks 4-5. Task 7 must run last.

```
Tasks 1, 2, 3  →  (parallel)
                    ↓
Tasks 4, 5, 6  →  (parallel, after 1-3)
                    ↓
Task 7         →  (validation, after all)
```

---

## Post-Implementation Review (Second Pass)

After implementing Tasks 1-7, a second-pass audit against the paper identified additional gaps:

### Fixed in Second Pass

- **Gap 1 (fixed):** `ad-angles` and `proof-harvesting` lacked worked examples — added Acme CI/CD examples to both
- **Gap 2 (fixed):** Section header inconsistency — all 14 non-init skills now use `## When to Use` consistently

### Recommended Future Work

**Gap 3: Strip general marketing knowledge from content skills (F4 risk)**

The paper's Table 4 shows Media & Content Production at only +13.9pp — 8th out of 11 domains. The explanation: *"domains with strong pretraining coverage benefit less from external procedural guidance."* LLMs already know how to write good marketing copy.

Some sections in our content skills reiterate general copywriting knowledge that Claude already has:
- "Name the pain the ICP is experiencing" (landing-page Section 2)
- "Make your headline specific and believable" (landing-page Section 1)
- "Lead with a story or question" (social-post hook patterns)

These sections risk the **conflicting guidance failure mode** (p.7): "Skills may introduce conflicting guidance or unnecessary complexity for tasks models already handle well." 16/84 tasks in the benchmark showed *negative* deltas from skills.

**What to keep:** The genuinely additive frameworks — Schwartz awareness diagnosis (non-obvious: changes the entire approach), JTBD force mapping, Hormozi Value Equation scoring, Dunford 5-component positioning, Masterson lead type selection, Cialdini proof tagging. These are procedural and non-obvious.

**What to trim:** Generic craft advice that any skilled writer/LLM knows. The litmus test: *"Would Claude produce worse output without this instruction?"* If a section describes what good copywriting looks like (which models already know), remove it. If it forces a specific decision framework the model wouldn't apply on its own, keep it.

**Estimated impact:** Moving content skills from "standard" (+10.1pp) toward "detailed" (+18.8pp) category by reducing general-knowledge noise and focusing on decision-forcing frameworks.

**Gap 4: Skills composition effects (Future Work, p.8)**

The paper calls out as future work: *"whether composite performance can be predicted from atomic Skills effects"* — i.e., when multiple skills chain together (market-research → positioning-angles → ad-angles), does the benefit compound or do the skills interfere?

Our sprint model chains 3-5 skills per campaign. Each individual task loads max 2 skills (per our selective loading fix), but the *campaign* creates a chain of skill outputs. Future measurement should track whether the full-campaign outcome exceeds the sum of individual-task improvements, or whether chaining introduces drift.

**Gap 5: Ecosystem-representative quality (Appendix A.4)**

The paper notes a *"Benchmark vs. Ecosystem Gap"*: their benchmark used top-quartile skills (quality score ≥ 9/12), but the real ecosystem averages 6.2/12. Our skills are well-crafted, but after the compression pass, we should verify they still score high on the paper's quality rubric:
1. **Completeness** (0-3): Required components present
2. **Clarity** (0-3): Readable and organized
3. **Specificity** (0-3): Actionable vs. vague guidance
4. **Examples** (0-3): Presence and quality of examples

Target: 10+/12 on each skill after all changes.
