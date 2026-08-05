# Hermes Orchestration — Running This Team on a Hermes Agent Fleet

**Read this before creating any task.** This plugin was written for Claude Code, where the
Campaign Lead coordinates through `TaskCreate` / `TaskUpdate` and spawns specialists with the
`Agent` tool. On a Hermes agent fleet none of those tools exist. The work is the same; the
mechanism is different, and getting the mechanism wrong fails **silently** — tasks are created,
the board looks correct, and nothing runs.

This file is the translation. Where it conflicts with a tool name in `agents/campaign-lead.md`,
this file wins on the Hermes fleet.

---

## The mapping

| Plugin (Claude Code) | Hermes equivalent |
|---|---|
| `TaskCreate(subject=...)` | `hermes kanban create "<title>" --assignee <profile> --body "<spec>"` |
| `metadata={"role": "creative"}` | `--assignee creative` |
| `TaskUpdate(dependencies=[...])` | `hermes kanban link <parent-id> <child-id>` |
| `Agent(subagent_type="research-specialist")` | nothing — the dispatcher spawns the assignee itself |
| `TaskList` / `TaskGet` | `hermes kanban list` / `hermes kanban show <id>` |

Profile names on the fleet are `campaignlead`, `researcher`, `creative`, `qualitygate`,
`distribution`.

---

## Four rules that are not optional

### 1. Assign with `--assignee`, never `--profile`

`--profile` is Hermes' **global profile selector**. It is stripped from the command line before
the kanban subcommand ever parses arguments, so `--profile creative` does not assign anything —
it silently changes which profile's config is being read and creates an unassigned task.

There is no error. The command exits 0. The output reads:

```
Created t_d9ff85a3  (ready, assignee=-)
```

That `assignee=-` is the only signal. An unassigned task is skipped by the dispatcher forever —
it never runs, and nothing reports it. **Read the output of every create and confirm the assignee
is not `-`.**

### 2. Every task carries a `--body`

A bare title is not a task specification. The specialist receives only what you put in the body,
and its working directory is empty, so anything you omit it must go hunting for — or invent.

A body must state:

- **Brief** — absolute path to the campaign brief
- **Inputs** — absolute paths to the specific files this specialist should read
- **Output** — the absolute path its deliverable must be written to
- **Acceptance** — what "done" means for this task

Omitting the brief path is how a reviewer once loaded an unrelated campaign's brief, scored the
wrong asset against it, and passed it — with no error anywhere.

### 3. Set the workspace explicitly: `--workspace dir:<absolute path>`

The default workspace is `scratch`, and **a scratch workspace is deleted when the task
completes**. Any file the specialist wrote there that it did not explicitly declare as an artifact
is destroyed — not orphaned, destroyed. The task still goes green.

Point every specialist task at a real directory:

```
--workspace dir:/absolute/path/to/campaign
```

The path must be absolute; relative paths are rejected. Setting the board's `default_workdir`
is not sufficient on its own — it is inherited only by tasks already created with a `dir` or
`worktree` workspace, never by scratch tasks.

### 4. Write the campaign brief before you create specialist tasks

The brief is the shared context every downstream task points at. If it does not exist when the
tasks are created, the bodies reference a path that is not there and specialists improvise.
Write it first, then create tasks that cite it.

---

## Sequencing

`hermes kanban link <parent> <child>` makes the child wait for the parent. A task created with no
parent starts as `ready` and is dispatchable immediately; linking it to an unfinished parent
demotes it to `todo` until that parent is `done`.

**You do not run specialists.** The dispatcher polls the board and spawns the assigned profile
once a task's dependencies are satisfied. Do not @-mention the specialists to wake them and do not
try to invoke them directly — the plugin's `Agent(subagent_type=...)` step has no equivalent here,
and broadcasting to the whole team causes every profile to activate at once against a single
shared inference host.

Build the chain, then stop. The board runs itself.

---

## Worked example

A three-stage asset, correctly specified:

```bash
# 0. Brief first.
#    Written to /Users/hermes/marketing/output/campaigns/<slug>/campaign-brief.md

# 1. Research
hermes kanban create "Research: platform specs and audience style" \
  --assignee researcher \
  --workspace dir:/Users/hermes/marketing/output/campaigns/<slug> \
  --body "Brief: /Users/hermes/marketing/output/campaigns/<slug>/campaign-brief.md
Inputs: context/icp.md, context/voice-dna.md
Output: /Users/hermes/marketing/output/campaigns/<slug>/research/specs.md
Acceptance: platform specs verified against a primary source; audience style patterns named with examples."

# 2. Draft — depends on research
hermes kanban create "Draft: 20-second script" \
  --assignee creative \
  --workspace dir:/Users/hermes/marketing/output/campaigns/<slug> \
  --body "Brief: .../campaign-brief.md
Inputs: .../research/specs.md, context/voice-dna.md, context/brand-guide.md
Output: /Users/hermes/marketing/output/campaigns/<slug>/drafts/script-draft.md
Acceptance: matches the research brief's format constraints; owner voice; no filler."

hermes kanban link <research-id> <draft-id>

# 3. Review — depends on draft
#    ... same shape ...

hermes kanban list   # confirm: every row shows a real assignee, not "-"
```

---

## Simple Mode

For a **single-asset** request, `TEAM.md` specifies Simple Mode: the relevant specialist works
directly, sequentially, without a sprint. Do not open a five-task board for one asset. Read
`TEAM.md` for what qualifies and how the modes differ — `workflows/sprint-planning.md` covers the
multi-asset case only.

---

## Before you report a breakdown as complete

Run `hermes kanban list` and check every row:

- Assignee is a real profile, not `-`
- Body is present
- Workspace is a `dir:` path, not scratch
- Dependencies link the stages in the intended order

If any row fails, fix it with `hermes kanban assign <id> <profile>` or
`hermes kanban edit`, and re-check. A board that looks right in your summary but is wrong on
disk is the failure this file exists to prevent.
