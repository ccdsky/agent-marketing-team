---
name: buyer-panel
description: Convene a panel of persona sub-agents to deliver synthetic-audience buy signal on a marketing asset — per-persona yes/no, resonance points, consensus objections, and a prioritized revision list.
---

# Buyer Panel Skill

## When to Use

Convene a panel of 3-13 prospect persona sub-agents to react to a draft asset as buyers — not as craft critics. Each persona answers a standardized question set in character, producing a yes/no buy signal plus the specific resonance points and objections that drove it. The skill then synthesizes per-persona signals into consensus resonance, consensus objections, conflicting reactions, and a prioritized revision list.

Invoke for Sprint 2 drafts that are complete enough to react to, ad-variant scoring across persona segments, sales-page testing, or any standalone "test this against my audience" request. Returns per-persona buy signal + synthesis identifying consensus and divergence + prioritized revision list.

---

## `/buyer-panel` vs `/expert-review`

`/expert-review` is a craft-expert panel critiquing the asset; it asks "is this asset well-crafted?" `/buyer-panel` is a prospect panel reacting as the buyer; it asks "would I, the persona, buy this?" Experts produce craft fixes; prospects produce buy-decision blockers. Both at Sprint 2 is the rigorous play — they produce complementary parallel signal. Either alone is the time-boxed play.

---

## Do NOT invoke when

- **No personas defined in `context/personas/`** — stop cleanly and recommend the user run `/expert-review` in a separate task instead. Do NOT auto-load `/expert-review` from within this skill (preserves the max-2-SKILL.md-per-task rule).
- **Sprint 1 sketches** — content is too thin for buyer-reaction signal; route to `/expert-review` for craft-level critique if review is needed at all.
- **Single-line content** — headlines and one-liners alone are too narrow; bundle them into the parent asset before convening a panel.

---

## Required Inputs

**Standalone invocation:** Ask for the asset file path and target persona slugs (or recipe name) before proceeding. Then read the asset.

**Called by Creative Specialist (campaign mode):** Call `TaskGet(taskId="[drafting-task-ID from task description]")` to read `metadata["deliverable"]` (draft file path) and the brief's named personas. Then read the draft and the persona index.

Before starting, always read:
- Draft asset file path (e.g., `output/campaigns/[slug]/drafts/landing-page-draft.md`)
- Target persona slugs OR panel-composition recipe name (see `references/recipes.md`)
- Campaign brief if available: `output/campaigns/[slug]/campaign-brief.md`
- `context/personas/README.md` — Index of available persona dossiers
- The named persona dossiers at `context/personas/[slug].md` (one per panelist)

---

## Procedure

1. **Mode Check.** Mode Check auto-detects parallel sub-agent availability (`Task` in Claude Code, equivalent in other harnesses); spawns personas as parallel sub-agents when available. Headless callers can force sequential execution with `mode:sequential` regardless of platform availability. Sequential mode opens each persona with "I am embodying [persona name]..." and runs the same question set inline; the output format is identical either way. Use `embody` not `pretend` throughout sub-agent prompts — the wording materially affects in-character accuracy.

2. **Select panel composition.** Resolve in this priority order:
   - Explicit user instruction (named persona slugs in the request)
   - Primary/Secondary persona fields from the campaign brief
   - Recipe applied from `references/recipes.md` (e.g., `recipe:buying-committee`)
   - Fallback: all personas with `audience_role: prospect` in `context/personas/`

3. **Dispatch sub-agents.** Each sub-agent receives: the asset path, its assigned persona dossier *path* (not the dossier content inline — **pass paths, not content**), the standardized question set, and the structured output format. For the per-persona prompt template and question set, see `references/methodology.md`.

4. **Collect and synthesize.** Confirm response count: full panel responded = full confidence; 60% to <100% responded = normalize weights and label "REDUCED CONFIDENCE — [N]/[total] personas responded"; <60% responded = do not synthesize, flag incomplete. Identify:
   - **Consensus yes** — personas align on what works (safe — don't change)
   - **Consensus no** — personas align on what blocks the buy (highest priority)
   - **Split reactions** — asset works for some personas not others (surface explicitly; do not average away)

5. **Build prioritized revision list.** Three tiers:
   - **Must Fix** — consensus objections + hot-button violations flagged by any persona
   - **Should Fix** — single-persona high-impact issues (e.g., one persona's category-defining red flag)
   - **Nice to Have** — subjective preferences, single-persona low-impact

   Each item: specific change + section reference + which personas flagged it + expected impact.

---

## Output

**Campaign mode:** Save to `output/campaigns/[campaign-slug]/reviews/buyer-panel-[asset-type]-[YYYY-MM-DD].md`

**Standalone:** Save to `output/buyer-panel-[asset-name]-[YYYY-MM-DD].md`

Required sections in order: Aggregate Buy Signal table (persona → yes/no + 1-line reason), Consensus Resonance, Consensus Objections, Must Fix, Should Fix, Nice to Have, Conflicting Persona Reactions, Revision Checklist.

For the full markdown template, see `references/methodology.md`.

**Mark complete:**

```
TaskUpdate(taskId="[ID]", status="completed", metadata={
  "deliverable": "output/campaigns/[campaign-slug]/reviews/buyer-panel-[asset-type]-[YYYY-MM-DD].md",
  "persona_signals": "[yes-count]/[total]",
  "consensus_objections": "[1-line summary of top blockers]",
  "ready_for": "creative-specialist"
})
```

---

## Example

**Scenario:** Buyer-panel review of a sales-page draft for an operations-systemization service. Convened via the `buying-committee` recipe — Morgan (Founder/CEO, prospect), Priya (Head of Ops, internal-stakeholder), Dan (CFO, internal-stakeholder).

**Draft snippet:**

> *"Transform your operations and unlock the next phase of growth. Our proven framework helps mid-market founders break through plateaus and build the systematic foundation they need to scale. Book a strategy call to see how we can partner with you on your transformation journey."*

**Aggregate Buy Signal:**

| Persona | Signal | Reason |
|---------|--------|--------|
| Morgan (Founder/CEO) | NO | "Transformation," "partner," and "journey" all read as agency-speak. No specifics. |
| Priya (Head of Ops) | NO | I'd be the one running this internally — page doesn't say what month one looks like for me. |
| Dan (CFO) | NO | Hidden pricing + "book a call" CTA. Can't budget against this. |

**Consensus Objections:**
- Generic transformation language without a specific outcome named (all three)
- Hidden pricing / call-gated next step (Morgan, Dan)
- No "month one" operational picture for the person doing the work (Priya, Morgan)

**Must Fix:**
1. Rewrite hero to name the specific outcome (e.g., "Get out of the bottleneck on $25K+ decisions in 90 days") — flagged by all three. Impact: passes the 200-word skim test for Morgan; gives Dan something concrete to budget.
2. Add a visible pricing range and a low-commitment first step before the call CTA — flagged by Morgan and Dan. Impact: removes the bounce trigger.
3. Add a "What month one looks like" section showing the operator's time commitment — flagged by Priya. Impact: addresses the internal-stakeholder's veto.

**Should Fix:** Add one named peer reference with a specific outcome (Morgan: "one named peer outperforms ten anonymous logos").

**Nice to Have:** Replace "partner" and "journey" throughout.

---

## Quality Gate

Before marking complete:

- [ ] Correct personas convened — matches brief, recipe, or explicit user instruction (not a guess)
- [ ] Each persona sub-agent prompt includes the dossier *path*, not inlined content
- [ ] Consensus signals distinguished from single-persona signals in the synthesis
- [ ] Conflicting reactions surfaced explicitly (not averaged away)
- [ ] Revision list prioritized into three tiers (Must Fix / Should Fix / Nice to Have), not a flat list
- [ ] Each revision item names the personas who flagged it and the expected impact
