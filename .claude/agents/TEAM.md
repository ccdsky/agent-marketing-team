# Marketing Team — Agent Operating Manual

This file defines shared protocols, file ownership, and coordination standards for all agents. Read it before any work.

Sprint model and task naming conventions: `.claude/workflows/sprint-planning.md`
Campaign retrospectives: `.claude/workflows/retrospective.md`

---

## File Ownership Strategy (Avoid Conflicts)

Each agent **creates NEW files** in their phase directory. No shared editing.

| Phase | Owner | Creates Files In | Read-Only For |
|-------|-------|------------------|---------------|
| Strategy | Campaign Lead | `output/campaigns/[name]/campaign-brief.md` | All agents |
| Retrospective | Campaign Lead | `knowledge/learnings/`, `knowledge/archive/` | All agents |
| Research | Research Specialist | `knowledge/research/` | All agents |
| Drafting | Creative Specialist | `output/campaigns/[name]/drafts/` | Editor |
| Editing | Quality Gate | `output/campaigns/[name]/edited/` | Publisher |
| Publishing | Distribution Specialist | `output/campaigns/[name]/ready/` | Analyst |
| Analysis | Distribution Specialist | `knowledge/feedback/analytics/` | Campaign Lead |

**Campaign directory structure:**
```
output/campaigns/dev-cli-launch-2026-02/
├── campaign-brief.md       (Campaign Lead maintains)
├── research/               (Research Specialist)
├── drafts/                 (Creative Specialist)
├── edited/                 (Quality Gate)
├── ready/                  (Distribution Specialist)
└── analytics/              (Distribution Specialist)
```

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

**If any file contains placeholder text:** Stop. Escalate to the user: "Context file [name] needs to be populated before work can begin. Fill in the template at `context/[name].md` — each file has inline instructions describing what to put there."

`context/brand-guide.md` — read if it exists, skip if missing. Absence of the file is not a failure; skipping a file that exists is.

---

## Pre-Task Protocol

Before claiming any task, read:
- `context/voice-dna.md`
- `context/icp.md`
- `context/business-profile.md`
- Campaign brief: `output/campaigns/[slug]/campaign-brief.md` (if in a campaign)
- Relevant research: `knowledge/research/[topic]-[date].md` (if available)
- Past learnings: `knowledge/learnings/campaigns/` (Grep for relevant patterns — skip if directory doesn't exist yet; it's created after the first campaign completes)

If context files may be unpopulated, run System Pre-Flight first.

**Validation step (Campaign Lead and specialists):** Before claiming your first task in a session, confirm you have loaded each required file. If a file hasn't been read in this session, read it now. Do not proceed on cached assumptions — context may have changed since the last campaign.

**Brand guide note:** If `context/brand-guide.md` exists, read it before any content work. It contains banned phrases that can disqualify otherwise excellent content. Its "optional" status means "skip if missing," not "skip if it exists."

---

## Execution Model

**Simple Mode (single asset):** The activated specialist operates directly within the conversation. No subagents. Sequential execution. Use for single-asset tasks like "Write a LinkedIn post."

**Campaign Mode (multi-asset sprint):** Campaign Lead uses the `Task` tool to spawn specialists as subagents. Each subagent accesses the shared project file system. "Parallel" execution only applies here.

**Spawning a specialist in Campaign Mode:**
```
Task(
  subagent_type="general-purpose",
  prompt="You are the [role] for the [campaign-name] campaign. Read .claude/agents/[role].md, then claim and execute all available tasks matching your role from TaskList() in a loop until no unclaimed unblocked tasks for your role remain. Complete each task fully before claiming the next. When done, report which tasks you completed.",
  description="[Role] — [campaign-slug]"
)
```

---

## Agent Protocol (Self-Claiming)

All agents follow this protocol:

**1. Check for tasks:**
```
TaskList()
```
Look for: Status `pending`, owner empty, `blockedBy` empty.

**Filter by role keywords before claiming:**

| Role | Claim tasks containing these keywords |
|------|--------------------------------------|
| Research Specialist | research, competitor analysis, customer language, positioning angles, keyword research |
| Creative Specialist | draft, write, revise, create, blog post, email sequence, landing page, lead magnet, newsletter, social post |
| Quality Gate | edit, review, quality check, approve |
| Distribution Specialist | format, publish, distribution, analytics, performance |

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

Use this format when escalating to Campaign Lead or directly to the user:

```markdown
## Escalation: [Issue]

**From:** [Agent name]
**Campaign:** [Name] (if applicable)

**Situation:**
[What's happening]

**Options:**
1. [Option A]: [Pros/cons]
2. [Option B]: [Pros/cons]

**My Recommendation:**
[Which option and why]

**Decision Needed:**
[What needs to be decided before work can continue]
```

---

*This team compounds. Every campaign makes the next one better.*
