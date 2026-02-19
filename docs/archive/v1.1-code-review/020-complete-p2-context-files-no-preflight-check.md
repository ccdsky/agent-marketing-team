---
status: pending
priority: p2
issue_id: "020"
tags: [code-review, context-files, voice-dna, icp, business-profile, graceful-degradation]
---

# Context Files Are Required But Have No Pre-Flight Check or Graceful Degradation

## Problem Statement

Every agent definition begins with a mandatory context-reading step:
```
Read(file_path="context/voice-dna.md")
Read(file_path="context/icp.md")
Read(file_path="context/business-profile.md")
```

These files currently contain placeholder/template content. No agent definition checks whether the files are populated, and no fallback behavior is specified if they contain stub content.

If `voice-dna.md` is a template, the Creative Specialist will produce generic content that sounds nothing like the owner — with no error signal. If `icp.md` contains boilerplate, all targeting will be wrong. This is a silent failure mode on every content task until setup is complete.

Additionally, `brand-guide.md` is listed as "optional" in CLAUDE.md but the `repurpose/SKILL.md` quality checklist references it as required. If the file doesn't exist, the Read call fails silently on the repurpose skill's final quality check.

## Proposed Solution

Add a "System Pre-Flight" section to `TEAM.md`:

```markdown
## System Pre-Flight

Before any agent begins work, verify these files are populated (not placeholder stubs):
- `context/voice-dna.md` — must contain actual writing samples and voice patterns
- `context/icp.md` — must contain real ICP definition
- `context/business-profile.md` — must contain actual offerings

**If any file contains placeholder text:** Stop. Escalate to user: "Context file [name] needs to be populated before I can work. Run /writer:setup or manually fill in the template."

`context/brand-guide.md` is optional. If it doesn't exist, skip reads for it — do not fail.
```

**Effort:** Small — 1 section added to TEAM.md, 1 note added to repurpose SKILL.md

## Acceptance Criteria

- [ ] TEAM.md defines pre-flight check for context files
- [ ] Agents know what to do if context files are stubs
- [ ] repurpose SKILL.md marks brand-guide.md as optional in its quality checklist

## Work Log

- 2026-02-18: Identified by architecture-strategist in second review pass
