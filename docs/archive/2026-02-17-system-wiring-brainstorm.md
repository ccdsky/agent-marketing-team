---
date: 2026-02-17
topic: system-wiring
---

# Agent Marketing Team: System Wiring

## What We're Building

Closing the gap between the well-designed v1.0 blueprint and an operational system. The architecture (sprint model, task-based coordination, file ownership, knowledge compounding) is sound. The wiring is missing: context files are empty templates, skills directory doesn't exist, CLAUDE.md is too long, and directory scaffolding is absent.

## One Important Correction

The reviewer's concern about TaskTool semantics was **incorrect**. Claude Code's `TaskCreate`, `TaskUpdate` (with `owner`, `addBlockedBy`, `metadata`), `TaskList`, and `TaskGet` exist and match exactly what the agent definitions describe. The coordination model does **not** need to be simplified or replaced. This is a non-issue.

## Why This Approach (Sequential MVP)

Address the gaps in priority order. Minimum viable working system first, then polish. Don't over-engineer — get to a first campaign run as fast as possible so the retrospective system can start compounding real learnings.

## Key Decisions

- **Context files**: Use `writer:setup` skill to populate voice-dna, ICP, and business-profile interactively — this is the most important step and requires Christopher's input
- **Skills**: Create `.claude/skills/` directory with the 7 content creation skills as SKILL.md files (landing-page, email-sequence, blog-post, newsletter, social-post, lead-magnet, repurpose) — these should follow the compound-engineering skill format
- **CLAUDE.md**: Trim the detailed campaign flow examples and multi-agent coordination walkthroughs — move them into Campaign Lead's agent definition. Keep routing rules and core principles. Target: under 200 lines
- **Directory scaffolding**: Create `knowledge/` subdirectories and `output/campaigns/` so first campaign write operations don't fail
- **Workflows**: Create `sprint-planning.md` and `retrospective.md` in `.claude/workflows/` — these complete the documented structure
- **Missing templates**: Create `lead-gen-campaign.md`, `product-launch.md`, `content-sprint.md` in `.claude/templates/`
- **Test**: Run "Write a LinkedIn post about [topic]" as the smoke test before attempting a full campaign

## Work Items (Priority Order)

1. **Populate context files** — Nothing works without voice-dna, ICP, business-profile (use writer:setup)
2. **Create directory scaffolding** — knowledge/ tree + output/campaigns/ so writes don't fail
3. **Create content skills** — 7 SKILL.md files in .claude/skills/
4. **Trim CLAUDE.md** — Move detailed examples to campaign-lead.md; keep CLAUDE.md under 200 lines
5. **Create workflow files** — sprint-planning.md + retrospective.md
6. **Create missing templates** — lead-gen-campaign.md, product-launch.md, content-sprint.md
7. **Smoke test** — Single LinkedIn post to validate basic creative pipeline

## Resolved Questions

- TaskTool semantics: Confirmed real tools exist, no gap to fix
- Skills: Create new SKILL.md files (no other project to copy from confirmed)
- Context population: Use writer:setup skill interactively

## Next Steps

→ `/workflows:plan` to design implementation details
