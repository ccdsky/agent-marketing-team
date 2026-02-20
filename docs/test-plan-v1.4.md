# Test Plan: Agent Marketing Team v1.4

> **Purpose:** Validate all v1.4 fixes targeting delegation compliance, context consumption, and retrospective enforcement.
> **Based on:** v1.3 evaluation (`docs/plans/campaign-evaluation.md`) — all 23 test criteria retained, delegation test 2.12 added as must-pass.
> **Date:** February 2026

---

## v1.4 Changes Being Tested

The following agent definition changes are validated by this test plan:

| Fix | Change | File |
|-----|--------|------|
| 1 | Explicit delegation directives in Sprint 2 and Sprint 3 | `campaign-lead.md` |
| 2 | "YOU DO NOT" negative list at header | `campaign-lead.md` |
| 3 | Self-check protocol before file creation | `campaign-lead.md` |
| 4 | Mandatory kickoff protocols with numbered spawning steps | `campaign-lead.md` |
| 5A | Context validation gate before Sprint 1 tasks | `campaign-lead.md` |
| 5B | Explicit context reads in specialist Before You Start sections | `creative-specialist.md`, `quality-gate.md`, `distribution-specialist.md` |
| 6 | Retrospective runs after Sprint 3, not after week 1 analytics | `campaign-lead.md` |
| 7 | TEAM.md validation step added to Pre-Task Protocol | `TEAM.md` |

---

## Sprint 1: Strategy & Research

**Evaluation criteria:**

| # | Test | Pass | Fail |
|---|------|------|------|
| 1.1 | **Context consumption.** Did Campaign Lead read all four context files before planning? | `voice-dna.md`, `icp.md`, `business-profile.md`, and `brand-guide.md` (if present) are all read before Sprint 1 tasks are created. Context validation gate checklist is completed. | Only one or two files read. Sprint 1 tasks created before context gate is satisfied. |
| 1.2 | **Research specificity.** Did Research Specialist find real competitor content? | Research package names specific competitor articles, identifies positioning gaps, mines actual customer language patterns. | Research is generic without competitive intelligence or customer language. |
| 1.3 | **ICP targeting.** Are positioning angles tailored to the actual ICP? | Angles reference ICP-specific details from `icp.md` — industry, decision dynamics, cycles. | Angles could apply to any B2B buyer. |
| 1.4 | **Positioning differentiation.** Are 3-5 options genuinely different? | Each angle represents a distinct editorial strategy with different hooks and proof points. | Angles are the same idea with slightly different wording. |
| 1.5 | **Sprint structure.** Proper task naming with dependencies? | Tasks use `[S1]`/`[S2]`/`[S3]` prefixes, have `blockedBy` dependencies, follow sprint-planning workflow. | Flat task list without dependencies or sprint prefixes. |
| 1.6 | **Brand-guide awareness.** Does the plan respect brand standards? | Campaign Lead reads `brand-guide.md` and plan reflects brand constraints. No banned phrases in planning output. | Brand-guide not read. Banned phrases appear in planning documents. |

**Sprint 1 threshold:** All 6 must pass. Test 1.1 and 1.6 are the v1.4 focus — they were failures in v1.3.

---

## Sprint 2: Drafting & Review

**Evaluation criteria:**

| # | Test | Pass | Fail |
|---|------|------|------|
| 2.1 | **Voice fidelity — blog post.** Sounds like the owner, not generic B2B? | Reads like voice-dna.md samples. Leads with reader's situation. Names fear with specifics. | Generic consultancy voice. Banned phrases. Company-first framing. |
| 2.2 | **Voice fidelity — email sequence.** Voice holds across 3-email arc? | Consistent voice, distinct purpose per email, peer-to-peer tone, soft-to-medium CTAs. | Voice shifts. Aggressive CTAs. Template feel. |
| 2.3 | **Voice fidelity — LinkedIn posts.** Sound like a person, not a brand account? | Strong hook per post, thought leadership voice, minimal hashtags, no "excited to announce." | Corporate. Brand-account language. Hashtag spam. |
| 2.4 | **Voice fidelity — newsletter.** Personal, deliberate, one clear insight? | Feels handwritten. Standalone value for non-prospects. One topic done well. | Marketing blast. Multiple disconnected topics. Salesy. |
| 2.5 | **ICP language integration.** Uses words the ICP actually uses? | Industry-specific language from research and icp.md throughout all assets. | Generic business language. No industry specifics. |
| 2.6 | **Fear-of-failure messaging.** Names fear directly, answers with substance? | Explicitly addresses buyer fear. Answers with methodology, proof, specifics — not platitudes. | Avoids the fear. Answers with vague reassurances. |
| 2.7 | **AI positioning.** Correct framing (outcomes, not headline)? | If mentioned, AI is in context of outcomes. Not the lead. | AI is the headline or main selling point. |
| 2.8 | **Quality Gate scoring.** Correct rubric (40% voice, 25% clarity, 25% craft, 10% positioning)? | Scores itemized across all four criteria by a Quality Gate subagent, not Campaign Lead. Feedback specific and actionable. | Campaign Lead self-scores. Wrong rubric weights. Vague feedback. |
| 2.9 | **Quality Gate teeth.** QG requests real revisions? | At least one asset gets specific revision requests identifying something Creative Specialist missed. | Everything passes 9-10/10 first time (rubber-stamp). |
| 2.10 | **Anti-pattern enforcement.** Zero banned phrases across all drafts? | No banned phrases in any asset through Quality Gate. | Any banned phrase passes QG undetected. |
| 2.11 | **Skill usage.** Correct skill file loaded before each asset type? | Evidence that each skill SKILL.md was read before drafting its corresponding asset. | Assets don't follow skill frameworks. |
| 2.12 | **Delegation model.** ⭐ NEW — must-pass. Campaign Lead spawns specialists; does NOT execute content work itself. | Creative Specialist and Quality Gate each spawned as separate `Task(subagent_type="general-purpose")` subagents. Campaign Lead creates zero files in `drafts/` or `edited/`. All Sprint 2 output files created by correct agents. | Campaign Lead wrote drafts, ran QG, or created files in `drafts/`/`edited/` directly. Specialists were not spawned as separate agents with correct type. |

**Sprint 2 threshold:** 10 of 12, with tests 2.1–2.4 and **2.12** as must-pass.

**Test 2.12 is the primary v1.4 regression test.** In v1.3, this scored 0% (delegation failure). Any v1.4 run that fails 2.12 is an architecture failure regardless of content quality.

---

## Sprint 3: Polish & Ship

**Evaluation criteria:**

| # | Test | Pass | Fail |
|---|------|------|------|
| 3.1 | **Revision quality.** Creative Specialist addresses all QG feedback items? | Targeted improvements applied. QG feedback items resolved, documented. Not a full rewrite. | Feedback ignored or only partially addressed. |
| 3.2 | **Platform formatting.** Distribution Specialist creates comprehensive platform briefs? | Per-platform briefs with SEO metadata, automation triggers, scheduling calendars, checklists. | Generic formatting. Missing platform-specific requirements. |
| 3.3 | **File organization.** Assets in correct directories? | Drafts in `drafts/`, edited in `edited/`, ready in `ready/`, research in `knowledge/research/`. | Files in wrong directories or mixed up. |
| 3.4 | **Analytics setup.** Campaign tracking configured? | Analytics plan with platform metrics, UTM schema, KPI dashboard, check-in cadence. | No analytics plan or placeholder only. |
| 3.5 | **Retrospective quality.** All 5 retrospective questions answered? | Campaign Lead runs retrospective after Sprint 3 completes (not after launch). All 5 questions answered with specific, evidence-based observations. | No retrospective run. Questions skipped or answered with generalities. |
| 3.6 | **Knowledge compounding.** At least one learning saved to knowledge base? | At least one learning file saved to `knowledge/learnings/campaigns/[category]/` with proper frontmatter. Archive entry created. | No learnings saved. `knowledge/learnings/` remains empty. |

**Sprint 3 threshold:** 5 of 6. Tests 3.5 and 3.6 are the v1.4 focus — both failed in v1.3.

---

## Delegation Audit Protocol

For each sprint, verify delegation by reviewing the session transcript:

**Pass criteria:**
- `Task()` call spawning Creative Specialist appears **before** any `Write()` to `drafts/`
- `Task()` call spawning Quality Gate appears **before** any `Write()` to `edited/`
- Campaign Lead has zero `Write()` calls to `drafts/` or `edited/`

**Fail criteria:**
- Any `Write()` to `drafts/` or `edited/` executed by Campaign Lead directly
- Specialists never spawned as separate `Task(subagent_type="general-purpose")` calls

Audit by searching the session log for `Write(file_path=` calls attributed to Campaign Lead. If any path contains `drafts/` or `edited/`, test 2.12 fails.

---

## Edge Case Watch List

| # | Edge Case | What to Watch |
|---|-----------|---------------|
| E1 | **The empathy trap** | Does content validate fear without amplifying it? |
| E2 | **The platitude trap** | Does content answer fear with substance, not reassurances? |
| E3 | **The self-promotion trap** | Is the client the hero, not the company? |
| E4 | **The consistency trap** | Does voice hold across all four formats? |
| E5 | **The rubber-stamp trap** | Does Quality Gate actually find something? |
| E6 | **The research-to-content gap** | Do specific research findings appear in drafts? |
| E7 | **The brand-guide blind spot** (v1.3 confirmed) | Is brand-guide explicitly read by Campaign Lead AND each specialist? |
| E8 | **The self-execution trap** (v1.3 confirmed) | Does Campaign Lead claim any specialist-role tasks? |

---

## Score Card Template

| Sprint | Tests | Required | Threshold |
|--------|-------|----------|-----------|
| Sprint 1 | 1.1–1.6 (6 tests) | 6/6 | All pass |
| Sprint 2 | 2.1–2.12 (12 tests) | 10/12, must-pass: 2.1–2.4, 2.12 | Content + delegation |
| Sprint 3 | 3.1–3.6 (6 tests) | 5/6 | Core delivery + retrospective |
| **Total** | **24 tests** | Sprint thresholds | **All 3 sprints meet threshold** |

**v1.3 baseline for comparison:**
- Sprint 1: 4.5/6 (FAIL — brand-guide not read, context incomplete)
- Sprint 2: 10.5/11 content tests pass, but 0% delegation compliance
- Sprint 3: 4/6 (FAIL — retrospective and learnings missing)

**v1.4 success criteria:** All three sprints meet threshold, delegation test 2.12 passes.

---

## Verdict Definitions

| Verdict | Criteria |
|---------|---------|
| **PASS** | All three sprints meet threshold. Delegation test 2.12 passes. |
| **PASS WITH FIXES** | Sprint thresholds met but specific non-critical issues identified. Delegation test 2.12 must still pass. |
| **FAIL — Content quality** | One or more voice tests (2.1–2.4) fail. |
| **FAIL — Architecture** | Delegation test 2.12 fails (Campaign Lead self-executes Sprint 2). This verdict applies regardless of content quality scores. |
| **FAIL — Knowledge loop** | Both 3.5 and 3.6 fail (retrospective and learnings both missing). |
