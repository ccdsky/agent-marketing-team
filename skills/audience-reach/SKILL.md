---
name: audience-reach
description: Research where and how to reach specific personas — discover named, current outlets per persona, score them on reach-fit, and roll up into a campaign-level Channel Reach Map.
---

# Audience Reach Skill

## When to Use

Discover which specific outlets and mediums reach a given persona or buying committee — before planning paid, earned, event, or outbound motions. Invoke when the Research Specialist receives an audience-reach / channel-discovery / media-planning request, or when the Campaign Lead needs a reach plan before activating a multi-channel campaign.

**Distinct from `/market-research`:** that skill maps audience behavior at the *category* level as a byproduct of competitive intel. This skill is *persona-level and outlet-specific* — it names real, current outlets and is the dedicated tool for the reach question. Run `/market-research` for the landscape; run `/audience-reach` for the reach plan.

---

## Required Inputs

Before starting, always read:
- `context/personas/README.md` → then the **1–3 target persona dossiers** (the launch pad — they already hold behavior signal)
- `context/icp.md` — buying-committee dynamics and the intermediary-influence map
- `context/business-profile.md` — category, offerings, geography (bounds which outlets are plausible)
- `context/brand-guide.md` — if present (platform tones); skip silently if absent

**If `context/personas/` doesn't exist or is empty:** do not invent personas. Fall back to `context/icp.md` as a single aggregate pseudo-persona, state that explicitly in the output header, and mark all persona-fit scores [I] (inferred). Recommend creating persona dossiers for a higher-confidence rerun.

Define scope before starting: which personas to reach (1–3, per Pre-Task Protocol — infer from task/brief, or ask)? Tied to a campaign? Any market-timing events (trade show, fiscal cycle, buying season)?

**Budget is NOT an input** — cost-to-access appears as a per-outlet output band, because real prices vary by outlet and are knowable only once the outlet is identified.

---

## Procedure

**Phase 1: GROUND**
1. Run Pre-Task Protocol. Identify the 1–3 target personas. Read their dossiers. Establish category, geography, and buying-committee context from `business-profile.md` + `icp.md`.

**Phase 2: MINE**
2. For each persona, extract the media/behavior signal *already in the dossier*: publications read, communities, events attended, influencers followed, search habits, platform presence, trust sources. Record what's present and what's missing.

**Phase 3: RESEARCH** (Web)
3. For each persona, research outward to name **specific, current outlets — not categories** — across five medium types: Earned/Organic, Paid, Events, Influence/Intermediary, Outbound. For the per-type checklist, see `references/methodology.md`. Each outlet carries: why it fits this persona, evidence/source, and a reachability note.

**Phase 4: SCORE & ENRICH**
4. Score each outlet 1–5 on Persona fit, Reachability, Intent/signal quality, Cost-to-access efficiency, Effort/feasibility. Tag each score **[E]** evidence-based (dossier signal or cited source) or **[I]** inferred — no bare scores. Attach a cost band ($/$$/$$$) and an intent read (Awareness / Consideration / Decision). Rank per persona. For the scoring guide, see `references/methodology.md`.

**Phase 5: ROLL UP**
5. Across the buying committee: separate shared outlets (multi-persona efficiency) from persona-unique outlets (precision reach); build a coverage matrix; and flag timing/sequencing dependencies tied to editorial calendar + market timing. Hand these to the Campaign Lead — flag, do not orchestrate.

**Phase 6: SYNTHESIZE**
6. Compile the Channel Reach Map (see Output).

---

## Output

Save to: `knowledge/research/audience-reach-[persona-or-campaign]-[YYYY-MM-DD].md`

Required sections:
- **Header** — date, target personas, campaign (if any), researcher
- **Executive Summary** — top reach recommendations
- **Per-Persona Channel Reach Map** — one table per persona: `outlet | medium type | persona-fit (1-5) | reachability (1-5) | intent | cost band | effort (1-5) | source`
- **Campaign Roll-Up** — shared vs. persona-unique outlets, coverage matrix (personas × outlets), flagged timing/sequencing dependencies
- **Prioritized Recommendations** — which outlets to pursue first, per persona and combined
- **Freshness & Confidence Flags** — snapshot date, per-outlet confidence, honest gaps

For the full markdown template, see `references/methodology.md`.

**Mark complete:**
```
TaskUpdate(taskId="[ID]", status="completed", metadata={
  "deliverable": "knowledge/research/audience-reach-[...]-[YYYY-MM-DD].md",
  "key_findings": "1. [Finding] 2. [Finding] 3. [Finding]",
  "recommended_outlets": "[top outlets per persona]",
  "ready_for": "campaign-lead"
})
```

---

## Example

**Scenario:** Reach plan for **Acme CI/CD**, targeting two buying-committee members: a **VP of Engineering** (economic buyer) and a **Director of Platform Engineering** (technical champion).

**Phase 2 excerpt — MINE (Director of Platform):**
Dossier shows they live in `r/devops`, follow two named SRE creators on LinkedIn, and cite the "Ship It!" podcast in discussions. No publication-reading signal recorded — gap to research.

**Phase 3 excerpt — RESEARCH (named outlets):**
- Earned: `r/devops` (active), "DevOps Weekly" newsletter, "Ship It!" podcast — Source: dossier + current subreddit activity
- Events: KubeCon + CloudNativeCon NA — Source: speaker/attendee profile match
- Paid: LinkedIn ad targeting `job title = Platform Engineering` + `skill = Kubernetes` — Source: platform targeting catalog

**Phase 4 excerpt — SCORE:**

| Outlet | Medium | Persona-fit | Reachability | Intent | Cost | Effort |
|--------|--------|-------------|--------------|--------|------|--------|
| r/devops | Earned/Organic | 5 [E] | 3 [E] (no overt selling) | Consideration | $ | 2 (credibility build) |
| KubeCon | Events | 4 [E] | 4 [I] | Consideration | $$$ | 2 |
| DevOps Weekly placement | Paid | 4 [E] | 5 [E] | Awareness | $$ | 5 |
| Gartner DevOps analyst | Influence/Intermediary | 4 [I] | 3 [I] | Consideration | $$$ | 2 |
| LinkedIn outreach to Platform leads | Outbound | 3 [I] | 4 [E] | Decision | $ | 3 |

**Phase 5 excerpt — ROLL UP:**
Coverage matrix:

| Outlet | VP Engineering | Director of Platform |
|--------|----------------|----------------------|
| KubeCon | ✓ | ✓ |
| r/devops |  | ✓ |
| Gartner DevOps analyst | ✓ |  |

Shared outlet: KubeCon reaches both the VP (keynote/exec track) and the Director (technical sessions) — efficiency play. Timing flag for Campaign Lead: *paid awareness in DevOps Weekly should lead the trial-nurture email motion by ~2 weeks and ramp ahead of KubeCon (early Nov), the market-timing anchor.*

---

## Quality Gate

Before marking complete:

- [ ] Outlets are **named and specific** — not categories ("`r/devops`," not "Reddit")
- [ ] Each outlet has a source/evidence
- [ ] Cost is **banded ($/$$/$$$), never invented** as a precise figure
- [ ] Intent quality (Awareness/Consideration/Decision) assigned to each outlet
- [ ] Roll-up flags timing/sequencing dependencies for the Campaign Lead
- [ ] Deliverable is dated as a snapshot (outlet maps are time-sensitive)
- [ ] Gaps flagged honestly — no LOW-confidence guesses presented as conclusions
