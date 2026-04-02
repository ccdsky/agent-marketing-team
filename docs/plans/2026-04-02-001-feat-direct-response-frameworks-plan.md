---
title: "feat: Integrate direct-response frameworks into marketing skills"
type: feat
status: active
date: 2026-04-02
origin: docs/specs/2026-04-02-direct-response-frameworks-design.md
---

# feat: Integrate direct-response frameworks into marketing skills

## Overview

Enrich 4 existing marketing skills with direct-response theory (Schwartz awareness mapping, Masterson lead types, mechanism building, Cialdini persuasion principles, Kahneman dual-process checks) and create 2 new skills (ad-angle multiplication and proof harvesting). Update 3 agent files and the CLAUDE.md routing table to wire everything together.

All changes are markdown edits — no code, no dependencies, no runtime changes.

## Problem Frame

The marketing team's skills have strong structural frameworks (Dunford positioning, Hormozi value equation, Laja messaging tests) but lack foundational direct-response theory that determines *how to talk to buyers based on where they are in their awareness journey*. The landing-page skill uses "cold/warm/hot" (a media-buying concept) instead of Schwartz's 5-stage awareness model. The positioning-angles skill names "mechanism-based" as an angle type but doesn't teach how to build one. There's no process for multiplying a chosen angle into creative variants, and no process for harvesting and organizing proof assets before writing. (See origin: `docs/specs/2026-04-02-direct-response-frameworks-design.md`)

## Requirements Trace

- R1. Landing page, email sequence, and blog post skills must diagnose buyer awareness stage and apply stage-appropriate messaging rules
- R2. Positioning angles skill must teach mechanism construction (Failure→Shift→Result) with 4 mechanism types and naming rules
- R3. New ad-angles skill must multiply an approved angle into 10-15 tagged creative variants across 6 dimensions
- R4. New proof-harvesting skill must systematically extract, score, and organize proof assets into a reusable library
- R5. Agent files (research-specialist, creative-specialist, campaign-lead) must reference new skills in their routing tables
- R6. CLAUDE.md must register new skills and keywords
- R7. All changes must follow existing file conventions (section ordering, cross-reference patterns, naming)

## Scope Boundaries

- NOT changing: market-research, keyword-research, lead-magnet-strategy, lead-magnet, expert-review, newsletter, social-post, repurpose skills
- NOT changing: TEAM.md, quality-gate.md, distribution-specialist.md
- NOT changing: sprint model, task coordination, or execution model
- NOT creating a standalone "persuasion layer" reference file — Cialdini/Kahneman concepts are embedded inline where used

## Context & Research

### Relevant Code and Patterns

**SKILL.md structure (all 12 files follow this):**
1. `# [Name] Skill` (H1)
2. `## Purpose` — with "Invoke when:" trigger
3. `## Methodology Sources` (strategy skills only)
4. `## Required Inputs` — bullet list of context file Read paths
5. `## Framework` — numbered Steps
6. `## Output Format` — save path + markdown template
7. `## Sprint 1 Checkpoint` (strategy skills only)
8. `## Quality Checklist` (content skills) or `## Quality Gate` (strategy skills)

**Cross-referencing:** Skills reference each other via `/skill-name` slash notation (e.g., "feeds directly into `/positioning-angles`"). Skills never reference agent files.

**Agent skill routing:**
- `creative-specialist.md` lines 72-81: maps asset type → `Read(file_path=".claude/skills/[name]/SKILL.md")`
- `research-specialist.md` lines 370-376: `## Research Skill Integration` section with bullet descriptions

**CLAUDE.md skill listing:** Two groups under `## Available Skills`:
- `**Content creation** (in .claude/skills/):` — bullet list `- /[name] — [description]`
- `**Marketing strategy** (in .claude/skills/):` — same format

**CLAUDE.md agent routing:** Each agent has `**Keywords:**` and `**Route when:**` entries under `### [Agent Name]`

### Institutional Learnings

No institutional learnings exist yet — `knowledge/learnings/` directories are scaffolded but empty. No prior campaigns have completed a retrospective.

## Key Technical Decisions

- **Awareness diagnosis replaces traffic source (not supplements it):** The "cold/warm/hot" field in landing-page Step 1 is removed and replaced with the 5-stage Schwartz model. Rationale: the awareness model subsumes traffic temperature — cold traffic maps to Unaware/Problem Aware, warm to Solution Aware, hot to Product/Most Aware. Keeping both creates confusion about which to use.

- **Mechanism building is a new step (3.5), not a rewrite of Step 4:** Inserting between Step 3 and Step 4 preserves the existing angle generation logic. Step 4's mechanism-based angle type now references Step 3.5's output. Rationale: least disruptive to the existing flow that already works.

- **Ad-angles is a new skill, not part of positioning-angles:** Different job (creative multiplication vs. strategic scoring), different timing (Sprint 2 vs. Sprint 1), different owner (could be Research Specialist expanding into Sprint 2, or Creative Specialist). Rationale: keeps positioning-angles focused on its current purpose.

- **Proof-harvesting is a new skill, not part of market-research:** Market-research discovers market intelligence; proof-harvesting inventories your own evidence. Different sources, different output structure. Rationale: proof-harvesting output is a reusable library that persists across campaigns.

- **No standalone persuasion reference file:** Cialdini and Kahneman concepts are embedded inline in the skills where they apply (landing-page proof block, positioning-angles mechanism test, ad-angles dimensions). Rationale: agents follow SKILL.md instructions; they won't reliably consult a separate reference file unless a skill tells them to.

## Open Questions

### Resolved During Planning

- **Who owns ad-angles execution?** Research Specialist — it's a strategy output (tagged angles with awareness stages), not content creation. Added to research-specialist.md keywords.
- **Who owns proof-harvesting?** Research Specialist — it's an inventory and scoring exercise, not writing. Added to research-specialist.md keywords.
- **Should ad-angles be a Sprint 1 or Sprint 2 activity?** Sprint 2 — it requires an approved positioning angle from Sprint 1 checkpoint. But it runs at the start of Sprint 2, before content creation begins.
- **Should proof-harvesting have a Sprint 1 Checkpoint section?** No — it produces a proof library that feeds other skills, not a strategic decision that needs user approval. It's a supporting asset, not a checkpoint artifact.

### Deferred to Implementation

- **Exact wording of the awareness diagnosis in email-sequence:** The spec provides a lead-magnet-delivery example arc. The implementer should also add a brief note for nurture and launch sequence types, following the same pattern.
- **Whether blog-post needs its output template updated:** The current template doesn't have an awareness/lead-type field. Implementer should check if adding it improves the output without bloating it.

## Implementation Units

- [ ] **Unit 1: Enrich positioning-angles with mechanism building**

  **Goal:** Add Step 3.5 (Build the Mechanism) and Category Creation angle type to positioning-angles skill

  **Requirements:** R2, R7

  **Dependencies:** None — foundational, other units reference mechanism concepts

  **Files:**
  - Modify: `.claude/skills/positioning-angles/SKILL.md`

  **Approach:**
  - Insert `### Step 3.5: Build the Mechanism` section between existing Step 3 and Step 4
  - Content: Failure→Shift→Result structure, 4 mechanism types table, naming rules, Thiel "secret" test, Kahneman dual-process litmus test (as defined in spec Part 4, section 4a)
  - Add Category Creation angle type to existing Step 4 angle types list (spec section 4b)
  - Update `## Methodology Sources` line to add Thiel, Masterson/Forde, Kahneman (spec section 4c)
  - Renumber nothing — Step 3.5 sits between 3 and 4, existing steps keep their numbers
  - Add a carry-forward note at end of Step 3.5: "Output: one mechanism per unique attribute cluster from Step 3. Tag each with type. Carry forward into Step 4."

  **Patterns to follow:**
  - Existing Step structure in positioning-angles (bold headers, code blocks for templates, bullet lists for rules)
  - Methodology Sources format: `Author (Book Title) — concept.` on a single line, separated by periods

  **Test scenarios:**
  - Happy path: Reading the modified skill from top to bottom, the flow is Step 1 → 2 → 3 → 3.5 → 4 → 5 → 6 with no broken references
  - Edge case: Step 4's existing "Mechanism-based" angle type now says "reference Step 3.5 output" — verify this cross-reference is present
  - Integration: The Category Creation angle type references Step 3.5's Thiel test — verify the prerequisite language is present

  **Verification:**
  - Positioning-angles skill reads coherently as a complete document
  - Step 3.5 contains: Failure→Shift→Result structure, 4-type table, naming rules, Thiel test, Kahneman test
  - Existing Steps 1-6 are unchanged except for Step 4's mechanism-based reference update

---

- [ ] **Unit 2: Enrich landing-page with awareness diagnosis**

  **Goal:** Replace traffic source with Schwartz awareness diagnosis, add Masterson lead types, enhance proof block and solution bridge

  **Requirements:** R1, R7

  **Dependencies:** None (can run in parallel with Unit 1)

  **Files:**
  - Modify: `.claude/skills/landing-page/SKILL.md`

  **Approach:**
  - **Step 1 changes:** Remove `Traffic source: cold traffic (SEO/ads) | warm (email) | hot (retargeting)` field. Replace with Buyer Awareness Stage diagnosis (5 stages + definitions), Matching Lead Type table (Masterson/Forde — 5 stages → lead types), and Messaging Rules by Stage (what to say / what not to say per stage). Content from spec Part 1, section 1a.
  - **Section 3 (Solution Bridge) changes:** After existing "Explain WHY it works" bullet, add Kahneman dual-process credibility check (System 1 intuitive + System 2 analytical tests). Content from spec Part 1, section 1b.
  - **Section 4 (Proof Block) changes:** After existing proof hierarchy, add Cialdini persuasion dimensions (Social Proof, Authority, Consistency) with arrangement guidance. Content from spec Part 1, section 1c.
  - **Output Format changes:** In the template metadata, replace `**Traffic source assumption:** [cold|warm|hot]` with `**Awareness stage:** [Unaware|Problem Aware|Solution Aware|Product Aware|Most Aware]` and `**Lead type used:** [Story|Secret|Problem-Agitation|Solution/Mechanism|Promise|Proof|Direct Offer]`. Content from spec Part 1, section 1d.

  **Patterns to follow:**
  - Existing Step 1 field format (bold label, options separated by pipes)
  - Existing Section sub-structure (bold headers, code blocks for templates)

  **Test scenarios:**
  - Happy path: Step 1 now contains awareness stage diagnosis with 5 stages, lead types, and messaging rules — no mention of "cold/warm/hot"
  - Happy path: Section 3 contains Kahneman check after existing mechanism guidance
  - Happy path: Section 4 contains Cialdini dimensions after existing proof hierarchy
  - Happy path: Output template metadata uses awareness stage and lead type fields
  - Edge case: Quality Checklist still references the updated concepts correctly (check if any checklist item mentioned "traffic source" — update if so)

  **Verification:**
  - Landing-page skill reads coherently with no orphaned references to old traffic source field
  - Awareness diagnosis provides clear, actionable guidance for each of the 5 stages
  - Output template matches the new field names

---

- [ ] **Unit 3: Enrich email-sequence with awareness arc**

  **Goal:** Add awareness-stage arc mapping to email sequence planning

  **Requirements:** R1, R7

  **Dependencies:** None (can run in parallel with Units 1-2)

  **Files:**
  - Modify: `.claude/skills/email-sequence/SKILL.md`

  **Approach:**
  - In Step 1, after the existing "Sequence arc" section (the `Email 1: [Emotional state at start] → deliver promise` block), add an `Awareness-Stage Arc:` subsection
  - Include: explanation of per-email awareness-stage transitions, lead-magnet-delivery example arc (5 emails mapping Problem Aware → Convert), rule about not skipping stages, note about Masterson lead types for subject lines
  - Content from spec Part 2, section 2a
  - Keep existing emotional arc — the awareness arc supplements it (emotional = how they feel, awareness = what they know)

  **Patterns to follow:**
  - Existing Step 1 format with bold headers and code block examples
  - Same indentation and list style as the existing sequence arc section

  **Test scenarios:**
  - Happy path: Step 1 contains both the emotional arc and the new awareness-stage arc, clearly distinguished
  - Happy path: Example shows awareness stage transitions per email with Masterson lead type references
  - Edge case: The "skip more than one stage" rule is present and clear

  **Verification:**
  - Email-sequence skill reads coherently with the new section integrated
  - Both arcs (emotional and awareness) are present and clearly serve different purposes

---

- [ ] **Unit 4: Enrich blog-post with awareness-matched intros**

  **Goal:** Map funnel stage to awareness level and lead type for intro strategy

  **Requirements:** R1, R7

  **Dependencies:** None (can run in parallel)

  **Files:**
  - Modify: `.claude/skills/blog-post/SKILL.md`

  **Approach:**
  - In Step 1, after the existing `Funnel stage: Awareness | Consideration | Decision` field, add an `Awareness-Stage Mapping:` subsection
  - Maps each funnel stage to Schwartz awareness level and Masterson lead type, with one-sentence intro strategy guidance per stage
  - Content from spec Part 3, section 3a
  - This is the smallest change — ~15 lines added

  **Patterns to follow:**
  - Existing Step 1 field format in blog-post skill

  **Test scenarios:**
  - Happy path: Funnel stage → awareness level → lead type mapping is present and clear
  - Happy path: Each mapped level has intro strategy guidance

  **Verification:**
  - Blog-post Step 1 contains the mapping without disrupting existing fields
  - Smallest of all changes, reads naturally in context

---

- [ ] **Unit 5: Create proof-harvesting skill**

  **Goal:** Create new skill for systematic proof extraction, scoring, and organization

  **Requirements:** R4, R7

  **Dependencies:** None (can run in parallel, but implementing after Unit 2 ensures familiarity with the Cialdini patterns being used)

  **Files:**
  - Create: `.claude/skills/proof-harvesting/SKILL.md`

  **Approach:**
  - Follow SKILL.md structural convention exactly: H1, Purpose (with "Invoke when:"), Methodology Sources (Cialdini), Required Inputs, Framework (4 Steps), Output Format, Quality Gate
  - Step 1: Inventory Available Proof — source categories table, capture fields
  - Step 2: Score Each Proof Asset — Specificity/Credibility/Relevance scoring (1-5 each, threshold 9+), Cialdini persuasion tags
  - Step 3: Identify Proof Gaps — matrix mapping proof inventory against content needs
  - Step 4: Organize Proof Library — by strength tier, by Cialdini dimension, by content need
  - Output path: `knowledge/research/proof-library-[company]-[date].md`
  - Full content from spec Part 6
  - This is a **strategy** skill → use `## Quality Gate` (not Quality Checklist), include `## Methodology Sources`
  - Cross-reference: note that output feeds `/landing-page` Section 4, `/email-sequence` proof emails, `/ad-angles` proof dimension

  **Patterns to follow:**
  - `positioning-angles/SKILL.md` — closest structural analogue (strategy skill with scoring rubric and output template)
  - Required Inputs format from existing skills
  - Quality Gate checkbox format from strategy skills

  **Test scenarios:**
  - Happy path: File exists at `.claude/skills/proof-harvesting/SKILL.md` with all 8 required sections
  - Happy path: Scoring rubric has clear 1-5 scales with examples at each level
  - Happy path: Gap analysis matrix maps to specific content skill sections
  - Edge case: Cross-references to downstream skills use `/skill-name` notation
  - Integration: Cialdini tags in this skill match the Cialdini dimensions referenced in landing-page Section 4 (Unit 2)

  **Verification:**
  - Skill follows the exact section ordering convention
  - Scoring is specific enough that two different agents would score the same proof asset similarly
  - Output template is structured for downstream consumption by Creative Specialist

---

- [ ] **Unit 6: Create ad-angles skill**

  **Goal:** Create new skill for multiplying an approved positioning angle into creative variants

  **Requirements:** R3, R7

  **Dependencies:** Unit 1 (references Step 3.5 mechanism output from positioning-angles)

  **Files:**
  - Create: `.claude/skills/ad-angles/SKILL.md`

  **Approach:**
  - Follow SKILL.md structural convention: H1, Purpose (with "Invoke when:"), Methodology Sources, Required Inputs, Framework (4 Steps), Output Format, Quality Gate
  - Methodology Sources: Cialdini (Influence), Dixon/Adamson (Challenger Sale), Schwartz awareness model
  - Required Inputs: approved positioning angle, mechanism from Step 3.5, icp.md, voice-dna.md, proof library (if available)
  - Step 1: Load the Core Angle
  - Step 2: Multiply Across 6 Dimensions (Pain, Desire, Proof, Identity, Contrarian, Urgency) with source attribution and Cialdini/Challenger framework tags
  - Step 3: Tag Each Angle — table format with dimension, hook, awareness stage, best channel, proof needed
  - Step 4: Quality Filter — removal criteria
  - Output path: `output/campaigns/[slug]/strategy/ad-angles-[date].md`
  - Full content from spec Part 5
  - This is a **strategy** skill → `## Quality Gate`, `## Methodology Sources`
  - No Sprint 1 Checkpoint section — this runs in Sprint 2

  **Patterns to follow:**
  - `positioning-angles/SKILL.md` — closest structural analogue
  - Output Format table structure from positioning-angles
  - Quality Gate checkbox format

  **Test scenarios:**
  - Happy path: File exists at `.claude/skills/ad-angles/SKILL.md` with all required sections
  - Happy path: All 6 dimensions defined with example hooks and source attribution
  - Happy path: Tagging table includes awareness stage and channel columns
  - Happy path: Quality filter criteria are specific and actionable
  - Edge case: Urgency dimension explicitly requires genuine scarcity (no manufactured deadlines)
  - Integration: References to Step 3.5 mechanism and `/positioning-angles` output use correct notation

  **Verification:**
  - Skill follows section ordering convention
  - 6 dimensions are distinct and well-defined with worked examples
  - Output format is structured for Creative Specialist consumption

---

- [ ] **Unit 7: Update agent files**

  **Goal:** Wire new skills into research-specialist, creative-specialist, and campaign-lead agent definitions

  **Requirements:** R5, R7

  **Dependencies:** Units 5-6 (references the new skill file paths)

  **Files:**
  - Modify: `.claude/agents/research-specialist.md`
  - Modify: `.claude/agents/creative-specialist.md`
  - Modify: `.claude/agents/campaign-lead.md`

  **Approach:**

  **research-specialist.md:**
  - In `## Research Skill Integration` section (line ~370), add two new bullet entries:
    - `- **Ad-angle multiplication:** Read .claude/skills/ad-angles/SKILL.md — Multiplies approved positioning into 10-15 creative variants across 6 dimensions (Pain, Desire, Proof, Identity, Contrarian, Urgency). Run after Sprint 1 checkpoint when angle is approved.`
    - `- **Proof harvesting:** Read .claude/skills/proof-harvesting/SKILL.md — Systematic proof extraction and scoring with Cialdini persuasion tags. Run during Sprint 1 alongside market research. Output feeds all content skills.`
  - In `## Self-Claiming Workflow` task keywords (line ~40), add: `ad angles, angle multiplication, proof harvesting, proof inventory, proof audit`

  **creative-specialist.md:**
  - In Step 5 skill routing table (lines 72-81), add: `- Ad angles → Read(file_path=".claude/skills/ad-angles/SKILL.md")`
  - In Step 4 context loading section, add: `Read(file_path="knowledge/research/proof-library-[company]-[date].md")  # if available`

  **campaign-lead.md:**
  - In Sprint 1 task breakdown section, add a note that proof harvesting can be included as an [S1] task alongside market research: "Consider adding an [S1] proof harvesting task if the business has existing customer results, testimonials, or case studies to inventory."

  **Patterns to follow:**
  - research-specialist.md Research Skill Integration bullet format: `**Name:** Read path — description with framework names`
  - creative-specialist.md skill routing: `- Asset type → Read(file_path="...")`
  - campaign-lead.md Sprint 1 uses TaskCreate example format

  **Test scenarios:**
  - Happy path: research-specialist.md lists all 5 strategy skills (market-research, keyword-research, positioning-angles, ad-angles, proof-harvesting)
  - Happy path: creative-specialist.md can route to ad-angles skill
  - Happy path: creative-specialist.md loads proof library in context step
  - Happy path: campaign-lead.md mentions proof harvesting as an optional Sprint 1 task
  - Edge case: Task keyword lists don't duplicate existing keywords

  **Verification:**
  - Each agent file reads coherently with new entries
  - Skill file paths are correct (`.claude/skills/ad-angles/SKILL.md`, `.claude/skills/proof-harvesting/SKILL.md`)

---

- [ ] **Unit 8: Update CLAUDE.md routing table**

  **Goal:** Register new skills and keywords in the root routing file

  **Requirements:** R6, R7

  **Dependencies:** Units 5-7 (skills must exist, agents must reference them)

  **Files:**
  - Modify: `CLAUDE.md`

  **Approach:**

  **Add to `## Available Skills` section:**
  - Under `**Marketing strategy** (in .claude/skills/):`:
    - `- /ad-angles — Ad-angle multiplication across 6 dimensions`
    - `- /proof-harvesting — Proof asset extraction and scoring`

  **Add to Research Specialist keywords:**
  - Add `proof harvesting, proof audit, ad angles, angle multiplication` to the `**Keywords:**` line

  **Add to Research Specialist Route when:**
  - Add examples: `"Harvest proof for...", "Multiply angles for...", "Generate ad angles for..."`

  **Patterns to follow:**
  - Existing skill listing format: `- /[name] — [3-8 word description]`
  - Existing keyword format: comma-separated in `**Keywords:**` line
  - Existing Route when format: quoted example phrases

  **Test scenarios:**
  - Happy path: Both new skills appear in the Available Skills list under Marketing strategy
  - Happy path: Research Specialist keywords include proof harvesting and ad angles terms
  - Happy path: Route when examples cover the new skill trigger phrases
  - Edge case: New keywords don't conflict with Creative Specialist routing (verify "ad angles" doesn't match Creative Specialist's "create" keyword — it shouldn't, since "angles" routes to Research)

  **Verification:**
  - CLAUDE.md accurately reflects all 14 skills (12 existing + 2 new)
  - Routing table correctly sends proof/angle requests to Research Specialist

## System-Wide Impact

- **Interaction graph:** Skills reference each other via `/skill-name` notation. New cross-references: proof-harvesting → `/landing-page`, `/email-sequence`, `/ad-angles`. Ad-angles → `/positioning-angles` Step 3.5. These are read-time references (agents read skill files), not runtime callbacks.
- **Error propagation:** Not applicable — no code execution, no runtime errors. If a skill file has a formatting error, the agent reading it may misinterpret instructions, but this is caught by verification (reading each file top-to-bottom).
- **State lifecycle risks:** None — these are static instruction files. No caching, no partial writes.
- **API surface parity:** The two new skills must follow the exact same structural convention as the existing 12. This is verified per-unit.
- **Unchanged invariants:** TEAM.md protocols, sprint model, task coordination, quality-gate scoring rubric, distribution-specialist workflow — all unchanged. The new skills integrate into the existing sprint timeline (proof-harvesting in Sprint 1, ad-angles at Sprint 2 start) without altering the sprint structure itself.

## Risks & Dependencies

| Risk | Mitigation |
|------|------------|
| Enriched skills become too long and agents lose focus on key steps | Keep additions concise — awareness diagnosis is ~30 lines, mechanism building is ~50 lines. Review each modified skill for total length after editing |
| New concepts conflict with existing framework references | Spec explicitly preserves all existing frameworks (Dunford, Hormozi, Laja). New concepts supplement, not replace |
| Agents may not consistently apply awareness diagnosis without enforcement | The diagnosis is embedded in Step 1 (mandatory first step) with explicit messaging rules per stage. This is the strongest enforcement position available in a markdown instruction system |
| Campaign Lead may not create proof-harvesting tasks in Sprint 1 | Added as a suggestion in campaign-lead.md, not mandatory. First campaign using the enriched skills will validate whether it should become mandatory |

## Sources & References

- **Origin document:** [docs/specs/2026-04-02-direct-response-frameworks-design.md](docs/specs/2026-04-02-direct-response-frameworks-design.md)
- **Source repo:** realkimbarrett/advertising-skills (Schwartz mapper, mechanism builder, ad-angle multiplier, sequential workflow model)
- **Book frameworks:** Cialdini (Influence), Masterson/Forde (Great Leads), Thiel (Zero to One), Kahneman (Thinking Fast and Slow), Dixon/Adamson (Challenger Sale)
- **Existing skills:** `.claude/skills/positioning-angles/SKILL.md`, `.claude/skills/landing-page/SKILL.md`, `.claude/skills/email-sequence/SKILL.md`, `.claude/skills/blog-post/SKILL.md`
- **Agent files:** `.claude/agents/research-specialist.md`, `.claude/agents/creative-specialist.md`, `.claude/agents/campaign-lead.md`
