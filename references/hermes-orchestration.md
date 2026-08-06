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
| `TaskUpdate(dependencies=[...])` | `--parent <parent-id>` at creation (preferred) — `hermes kanban link <parent-id> <child-id>` only for a task that has not started |
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

### 2. Every task carries a `--body`, and the body carries the SUBJECT

A bare title is not a task specification. The specialist receives only what you put in the body,
and its working directory is empty, so anything you omit it must go hunting for — or invent.

A body must state:

- **Subject** — what this asset is actually about, in the requester's own words. Not the asset
  *category*, the specific thing.
- **Brief** — absolute path to the campaign brief (which must already exist — see rule 4)
- **Inputs** — absolute paths to the specific files this specialist should read
- **Output** — the absolute path its deliverable must be written to
- **Acceptance** — what "done" means for this task

**The Subject line is the one people drop, and dropping it is expensive.** A request for "a
20-second video of me making a full sheet of stickers with print-and-cut" was written into a body
as "clear demonstration of the print-and-cut feature." The word *stickers* never reached the
writer. Having no subject and no brief, it searched for the nearest prior campaign, found one
about Christmas ornaments, and wrote a script about ornaments. Every structural field was correct
and the deliverable was still wrong.

Copy the requester's own nouns into the Subject line. If the request says stickers, the body says
stickers.

Omitting the brief path is how a reviewer once loaded an unrelated campaign's brief, scored the
wrong asset against it, and passed it — with no error anywhere.

**Never use another campaign's files as a template.** If your inputs are missing, that is a
blocker to raise (`hermes kanban block <id> --kind needs_input "<what is missing>"`), not a gap to
fill from whatever similar work you can find. Two agents did exactly that on the sticker run —
`search_files "*ornament*"` — and produced a confidently wrong asset.

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

### 4. Write the campaign brief BEFORE the first task exists — and verify it

This is a hard gate, not a preference. The brief is the shared context every downstream body
points at.

```bash
# write it, then prove it exists before going further
ls -l /Users/hermes/marketing/output/campaigns/<slug>/campaign-brief.md
```

If that `ls` fails, **stop and write the brief.** Do not create tasks whose bodies say
"(to be created)" — that phrase appeared in all three bodies on the sticker run, the brief was
never written, and both specialists went hunting through old campaigns to fill the void.

---

## Sequencing — use `--parent`, not create-then-link

**Set the dependency at creation time:**

```bash
hermes kanban create "<title>" --assignee creative --parent <research-task-id> ...
```

A task created with `--parent` starts as `todo` and cannot be dispatched until the parent is
`done`. That is the safe form.

**`hermes kanban link <parent> <child>` after the fact is racy.** A task created without a parent
starts as `ready` and the dispatcher polls every 60 seconds — so if you create three tasks and
then link them, the dispatcher can claim task two before your link lands. That happened on the
sticker run: the writer started drafting while its research task was still running, so it had no
research at all. `link` demotes a `ready` child to `todo` only if it gets there first.

Use `link` only to add a dependency to a task that already exists and has not started.

**You do not run specialists.** The dispatcher polls the board and spawns the assigned profile
once a task's dependencies are satisfied. Do not @-mention the specialists to wake them and do not
try to invoke them directly — the plugin's `Agent(subagent_type=...)` step has no equivalent here,
and broadcasting to the whole team causes every profile to activate at once against a single
shared inference host.

Build the chain, then stop. The board runs itself.

---

## Worked example

A three-stage asset, correctly specified. Note the order: brief first, then each task created
with its parent already set.

```bash
# 0. BRIEF FIRST — write it, then prove it exists.
ls -l /Users/hermes/marketing/output/campaigns/<slug>/campaign-brief.md   # must succeed

# 1. Research — no parent, starts ready
R=$(hermes kanban create "Research: platform specs and audience style" \
  --assignee researcher \
  --workspace dir:/Users/hermes/marketing/output/campaigns/<slug> \
  --body "Subject: <the specific thing, in the requester's words>
Brief: /Users/hermes/marketing/output/campaigns/<slug>/campaign-brief.md
Inputs: context/icp.md, context/voice-dna.md
Output: /Users/hermes/marketing/output/campaigns/<slug>/research/specs.md
Acceptance: platform specs verified against a primary source; audience style patterns named.")

# 2. Draft — --parent set AT CREATION so it starts todo, never ready
hermes kanban create "Draft: 20-second script" \
  --assignee creative --parent <research-id> \
  --workspace dir:/Users/hermes/marketing/output/campaigns/<slug> \
  --body "Subject: <the same specific thing — do not generalise it away>
Brief: .../campaign-brief.md
Inputs: .../research/specs.md, context/voice-dna.md, context/brand-guide.md
Output: /Users/hermes/marketing/output/campaigns/<slug>/drafts/script-draft.md
Acceptance: matches the research brief's format constraints; owner voice; no filler."

# 3. Review — --parent set to the draft task, same pattern

hermes kanban list   # every row: real assignee, and only stage one is ready
```

---

## Closing the loop — you must report back

**A finished board is not a finished job.** The person who asked for the work is not watching
the kanban. If nobody tells them it is done, the run silently ends and they find out by
checking. Buzz's own agent guidance names a missing completion callback as *the single biggest
cause of stalled collaboration*, and it is the easiest thing in this whole flow to forget,
because by the time the work finishes your original turn ended long ago.

### Own an umbrella task

Create one task **assigned to yourself**, and make every specialist task a child of it:

```bash
# 1. Umbrella task — you own this one
U=$(hermes kanban create "Campaign: <name>" --assignee campaignlead \
      --workspace dir:/Users/hermes/marketing/output/campaigns/<slug> \
      --body "Subject: <what the requester asked for, their words>
Requester: <who to report back to, and on which surface>
Acceptance: all child tasks done; deliverables verified at their absolute paths; result
reported back to the requester.")

# 2. Every specialist task hangs off it
hermes kanban create "Research: ..."  --assignee researcher --parent $U ...
hermes kanban create "Draft: ..."     --assignee creative   --parent <research-id> ...
```

The umbrella stays open while its children run. When they all finish, the dispatcher **wakes
you back up** on that task to judge the result — that wake-up is the only reason you get a
turn after the work completes. Without a parent task you own, there is no wake-up and no
report. A single standalone task is a dead end, even when it succeeds.

Requires `kanban.orchestrator_profile` to name a profile in `config.yaml`. If it is empty,
nothing wakes.

### What to do when you wake

1. **Check the deliverables on disk**, at the absolute paths in each child's Output line. A
   `done` status is a claim, not proof. `ls -l` them.
2. **Report to the requester** on the surface they asked from — the Buzz channel or DM the
   request arrived in. On Buzz you **must `@mention` them** in that message, with an explicit
   `--mention <hex|npub>`. A report they are not mentioned in does not notify them.
3. **Say what was produced and where.** Absolute paths, one line each.
4. **Say what did not get done, and why.** A blocked or refused task is part of the result,
   not an omission to quietly drop. If you refused something, say what you refused and what
   would unblock it.
5. **Then complete the umbrella task.**

Never format an @mention in bold, italics, or backticks — it breaks notification delivery.

### Refusals count as completion

If a requested asset cannot be honestly produced — the hardware has not arrived, the source
material does not exist, a claim cannot be supported — do not invent it and do not silently
drop it. Block that task with a reason:

```bash
hermes kanban block <id> --kind needs_input "<what is missing and what would unblock it>"
```

Then report the refusal alongside the work that did land. A run that delivers three assets and
names the fourth as blocked is a successful run. A run that delivers four assets where one was
fabricated is a failure that looks like success — and that is the more expensive outcome,
because nobody catches it until it ships.

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
