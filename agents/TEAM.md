# Marketing Team — Agent Operating Manual

This file defines shared protocols, file ownership, and coordination standards for all agents. Read it before any work.

Sprint model and task naming conventions: `workflows/sprint-planning.md`
Campaign retrospectives: `workflows/retrospective.md`

---

## File Ownership Strategy (Avoid Conflicts)

Each agent **creates NEW files** in their phase directory. No shared editing.

| Phase | Owner | Creates Files In | Read-Only For |
|-------|-------|------------------|---------------|
| Strategy | Campaign Lead | `output/campaigns/[name]/campaign-brief.md` | All agents |
| Retrospective | Campaign Lead | `knowledge/learnings/`, `knowledge/archive/` | All agents |
| Research | Research Specialist | `knowledge/research/`, `output/campaigns/[name]/research/` | All agents |
| Positioning | Research Specialist | `output/campaigns/[name]/strategy/` | All agents |
| Drafting | Creative Specialist | `output/campaigns/[name]/drafts/` | Editor |
| Reviews | Creative Specialist | `output/campaigns/[name]/reviews/` | All agents |
| Editing | Quality Gate | `output/campaigns/[name]/edited/` | Publisher |
| Publishing | Distribution Specialist | `output/campaigns/[name]/ready/` | Analyst |
| Analysis | Distribution Specialist | `knowledge/feedback/analytics/` | Campaign Lead |

**Campaign directory structure:**
```
output/campaigns/dev-cli-launch-2026-02/
├── campaign-brief.md       (Campaign Lead maintains)
├── research/               (Research Specialist)
├── strategy/               (Research Specialist — positioning angles, lead magnet concepts)
├── drafts/                 (Creative Specialist)
├── reviews/                (Creative Specialist — expert review outputs)
├── edited/                 (Quality Gate)
├── ready/                  (Distribution Specialist)
└── analytics/              (Distribution Specialist)
```

---

## File Naming

All generated files follow one grammar: `[type]-[slug]-[YYYY-MM-DD].md`. Slugs are kebab-case with no slashes — a "[company-or-topic]" placeholder means *company or topic*, rendered as a single kebab-case token (e.g. `market-research-acme-cicd-2026-07-04.md`). Dates are always ISO `YYYY-MM-DD`. Downstream agents Glob by these patterns; deviating breaks handoffs.

**Scoring scales note:** Skills deliberately use different scoring scales because each follows its methodology source (1-5 × 3 dimensions for positioning/proof, 0-3 Business Potential for keywords, 1-10 Value Equation for lead magnet concepts, X/10 expert panels, binary buyer-panel votes). Do not normalize scores across skills — compare only within a skill's own scale.

---

## Communication Protocols

### Task Handoffs (Primary)
Agents communicate deliverable location and status via `TaskUpdate` metadata on completion:

```
TaskUpdate(
  taskId="[ID]",
  status="completed",
  metadata={
    "deliverable": "output/campaigns/[slug]/drafts/landing-page-draft.md",
    "assessment": "8/10 voice match — strong hook, ICP-relevant. Ready for QG.",
    "ready_for": "quality-gate"
  }
)
```

Downstream agents call `TaskGet(taskId="[ID]")` to read the deliverable path and assessment before claiming their task.

**For blockers:** Update task metadata with `"status": "blocked"` and `"blocker": "[what's missing]"`, then escalate to Campaign Lead.

### Escalation (Urgent)
**Use for:**
- Stuck > 2 hours with no path forward
- Strategic uncertainty requiring user input

---

## Quality Standards (All Agents)

Before marking any task complete, verify:

1. **Voice fidelity** - Does this sound like the owner?
2. **Audience value** - Would the ICP care?
3. **Honesty** - No fluff, no filler
4. **Craft** - Work we're proud of

**If standards can't be met, escalate rather than ship subpar work.**

---

## Escalation Triggers

Always escalate to the user when:
- **Strategic uncertainty:** Multiple valid directions with real tradeoffs
- **Voice uncertainty:** Topic requires the owner's personal perspective
- **Quality concerns:** Standards can't be met within constraints
- **Sensitivity:** Content involves personal stories or controversial positions
- **Conflicts:** Agents disagree on approach
- **Stuck > 2 hours:** Can't make progress on claimed task

---

## System Pre-Flight

Before any agent begins work, verify these context files are populated (not placeholder stubs):
- `context/voice-dna.md` — must contain actual writing samples and voice patterns
- `context/icp.md` — must contain real ICP definition
- `context/business-profile.md` — must contain actual offerings

**If any file is missing (not found):** Stop. Escalate to the user: "Project not initialized. Run `/agent-marketing-team:init` to scaffold context, knowledge, and output directories, then populate the context files."

**If any file contains placeholder text:** Stop. Escalate to the user: "Context file [name] needs to be populated before work can begin. Fill in the template at `context/[name].md` — each file has inline instructions describing what to put there."

`context/brand-guide.md` — read if it exists, skip if missing. Absence of the file is not a failure; skipping a file that exists is.

---

## Pre-Task Protocol

Before claiming any task, read:
- `context/voice-dna.md`
- `context/icp.md`
- `context/business-profile.md`
- `context/personas/README.md` — read if it exists, skip if missing. If present, do not pre-load individual dossiers — see "Identify target personas for this task" below.
- Campaign brief: `output/campaigns/[slug]/campaign-brief.md` (if in a campaign)
- Relevant research: `knowledge/research/[topic]-[YYYY-MM-DD].md` (if available)
- Past learnings: `knowledge/learnings/campaigns/` (Grep for relevant patterns — skip if directory doesn't exist yet; it's created after the first campaign completes)

If context files may be unpopulated, run System Pre-Flight first.

**Validation step (Campaign Lead and specialists):** Before claiming your first task in a session, confirm you have loaded each required file. If a file hasn't been read in this session, read it now. Do not proceed on cached assumptions — context may have changed since the last campaign.

**Identify target personas for this task:** After loading the persona index (if present), determine which personas (1-3 maximum) this task targets, in priority order:

1. Explicit user instruction in the task description (e.g., "for the CFO persona").
2. `Primary Persona(s)` / `Secondary Persona(s)` fields in the Campaign Brief, if in a campaign.
3. Inference from the index plus task keywords.

Load only the dossiers for the identified personas — do not load every persona in the library. If targets are uncertain, ask the user rather than guess. If no personas are defined (directory absent or empty), proceed with `icp.md`-only behavior — this is normal, not an error.

Persona discovery globs `context/personas/*.md` excluding `*.template.md` files (templates are reference material, not selectable personas).

**Awareness diagnosis (content work):** Diagnose the awareness stage — and select the lead type, where the skill defines lead types — per the **primary persona's** profile (their `What They Say Out Loud` voice samples, hot buttons, red flags, AI Agent Simulation Block). Different personas may sit at different awareness stages for the same offering. Fall back to the `context/icp.md` aggregate if no primary persona is defined. Skills reference this rule as "persona diagnosis per Pre-Task Protocol."

**Brand guide note:** If `context/brand-guide.md` exists, read it before any content work. It contains banned phrases that can disqualify otherwise excellent content. Its "optional" status means "skip if missing," not "skip if it exists."

**Persona note:** If `context/personas/` contains user-authored personas, drafts can address named buyers specifically and `/buyer-panel` can convene synthetic-audience signal on completed drafts. See `context/personas/README.md` for the library index and `skills/buyer-panel/references/recipes.md` for panel-composition recipes. Like the brand guide, persona consultation is optional — absence of the directory is not a failure.

---

## Skill Loading Protocol

Load skills **on-demand per task**, not all skills for your role.

**Rule:** Read at most 2 SKILL.md files per task. If a task spans two domains, read both. Never pre-load skills you might not need.

**How to load:**
1. Claim a task from TaskList()
2. Identify the 1-2 most relevant skills from your routing table
3. Read the SKILL.md for the primary skill
4. Grep `knowledge/learnings/` for the skill name and asset type (e.g. `landing-page`, `lead magnet`) — apply any codified learnings on top of the skill's framework. Skip silently if the directory doesn't exist yet.
5. If needed during execution, read the skill's `references/` files on demand

**Do NOT pre-read all skills before claiming tasks.**

---

## Execution Model

**Simple Mode (single asset):** The activated specialist operates directly within the conversation. No subagents. Sequential execution. Use for single-asset tasks like "Write a LinkedIn post."

**Campaign Mode (multi-asset sprint):** Campaign Lead uses the `Task` tool to spawn specialists as subagents. Each subagent accesses the shared project file system. "Parallel" execution only applies here.

**Spawning a specialist in Campaign Mode:**
```
Agent(
  subagent_type="[agent-name]",
  prompt="Campaign: [campaign-name]. Claim and execute all available [sprint-prefix] tasks matching your role from TaskList() in a loop until no unclaimed unblocked tasks for your role remain. Complete each task fully before claiming the next. When done, report which tasks you completed.",
  description="[Role] — [campaign-slug]"
)
```

Agent names match the `name` field in each agent's YAML frontmatter: `research-specialist`, `creative-specialist`, `quality-gate`, `distribution-specialist`.

---

## Agent Protocol (Self-Claiming)

All agents follow this protocol:

**1. Check for tasks:**
```
TaskList()
```
Look for: Status `pending`, owner empty, `blockedBy` empty.

**Filter by role before claiming — metadata first, keywords as fallback:**

If `task.metadata["role"]` is set, claim only tasks where it matches your agent name exactly (e.g. `"creative-specialist"`). The keyword table below applies only to tasks **without** a `role` field. Never claim a task whose `role` names another agent, even if its subject matches your keywords.

| Role | Claim tasks containing these keywords |
|------|--------------------------------------|
| Research Specialist | research, market research, competitor analysis, customer language, positioning gaps, keyword research, positioning angles, differentiation angles, lead magnet strategy, lead magnet concept, proof harvesting, proof audit, ad angles, angle multiplication, audience reach, channel discovery, outlet research, media planning |
| Creative Specialist | draft, write, revise, create, blog post, email sequence, landing page, lead magnet, newsletter, social post, expert review, expert panel, buyer panel, persona panel, audience signal, synthetic audience |
| Quality Gate | edit, editing, review, quality check, approve, feedback, editorial |
| Distribution Specialist | format, formatting, publish, publishing, distribution, distribute, analytics, performance, metrics, track |

**If no matching task exists:** Do not claim an off-role task. Report back that no role-appropriate tasks are available.

**2. Claim:**
```
TaskUpdate(taskId="[ID]", status="in_progress", owner="[your-role]")
```

**3. Read task details:**
```
TaskGet(taskId="[ID]")
```
Read `task.metadata` for upstream deliverable paths and context.

**4. Execute** — follow your agent-specific workflow.

**5. Complete with metadata:**
```
TaskUpdate(
  taskId="[ID]",
  status="completed",
  metadata={
    "deliverable": "[path to output file]",
    "assessment": "[brief self-assessment]",
    "ready_for": "[next-agent-role]"
  }
)
```

**Quality Gate only:** Claim ONE editing task at a time (serial). Complete fully before claiming the next.

---

## Escalation Format

When escalating, include: **situation** (what's happening), **options** (with tradeoffs), **your recommendation** (which and why), **decision needed** (what must be decided before work continues).

---

*This team compounds. Every campaign makes the next one better.*
