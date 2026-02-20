---
status: pending
priority: p2
issue_id: "060"
tags: [code-review, brand-guide, TEAM.md, context-reads]
---

# Brand-Guide "Optional" Label Creates Rhetorical Tension in TEAM.md

## Problem Statement

TEAM.md System Pre-Flight section (line 97) still says `` `context/brand-guide.md` is **optional**. If it doesn't exist, skip reads for it — do not fail. `` Immediately downstream, the new Pre-Task Protocol validation note clarifies: "Its 'optional' status means 'skip if missing,' not 'skip if it exists.'" An agent reading System Pre-Flight before the Pre-Task Protocol sees "optional" without the clarifying gloss and may correctly conclude it can skip the file even when present. This is the same failure mode as v1.3 (brand-guide never read).

## Findings

**TEAM.md line 97 (System Pre-Flight):**
```
`context/brand-guide.md` is **optional**. If it doesn't exist, skip reads for it — do not fail.
```

**TEAM.md lines 115-116 (Pre-Task Protocol, new addition from PR):**
```
If `context/brand-guide.md` exists, read it before any content work. Its "optional" status means "skip if missing," not "skip if it exists."
```

The clarification is correct but downstream. A reader encountering the "optional" label in System Pre-Flight has the wrong mental model before reaching the correction.

**File:** `.claude/agents/TEAM.md`, line 97
**Identified by:** architecture-strategist

## Proposed Solution

Replace the "optional" language in System Pre-Flight entirely:

**Current:**
```
`context/brand-guide.md` is **optional**. If it doesn't exist, skip reads for it — do not fail.
```

**Proposed:**
```
`context/brand-guide.md`: Read it if it exists. Skip only if the file is absent. Do not treat absence as a reason to skip a file that is present.
```

Then simplify or remove the downstream Pre-Task Protocol clarification note since the ambiguity is resolved at the source.

**Effort:** Trivial
**Risk:** None

## Acceptance Criteria

- [ ] "optional" label removed from brand-guide.md description in TEAM.md System Pre-Flight
- [ ] Replacement language makes conditional read/skip behavior unambiguous
- [ ] Downstream Pre-Task Protocol note updated or removed to avoid double-qualification

## Work Log

- 2026-02-19: Created from code review of PR #3. Identified by architecture-strategist.
