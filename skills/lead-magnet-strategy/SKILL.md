---
name: lead-magnet-strategy
description: Design high-converting lead magnet concepts scored by Hormozi Value Equation before any content creation begins.
---

# Lead Magnet Strategy Skill

## When to Use

Design a high-converting lead magnet concept based on the business's core offer, ICP pain points, and competitive landscape. Produces a scored concept brief before any content creation begins — preventing the common failure of building the wrong thing well. Invoke when Campaign Lead needs a lead magnet concept before assigning `/lead-magnet`, or user requests "design a lead magnet for [business/campaign]."

**Important:** This skill produces a *concept brief*, not a finished lead magnet. The `/lead-magnet` skill creates the actual content. Always run this first.

---

## Required Inputs

Before starting, always read:
- `context/business-profile.md` — Core offer, target deal, unique mechanism
- `context/icp.md` — Pain points, vocabulary, content preferences, current alternatives
- `context/voice-dna.md` — Owner's positioning and areas of expertise
- Research package: `knowledge/research/[relevant]-[date].md` (if available — especially market research and positioning angles)
- Campaign brief: `output/campaigns/[slug]/campaign-brief.md` (if this is for a specific campaign)

---

## Procedure

1. **Define the Bridge.** Map: Narrow Problem → Lead Magnet → Next Problem Revealed → Core Offer. Test: Is the narrow problem specific enough? Is the next problem revealed a natural consequence (not manufactured)? If the bridge feels forced, redesign before continuing.

2. **Select Lead Magnet Type.** Choose Problem Revealer, Sample/Trial, or One Step based on ICP awareness stage. Choose delivery mechanism (Software/Tool, Information, Service, Physical). B2B bias: prioritize Software/Tool and Service. For full selection table, see `references/methodology.md`.

3. **Score with Value Equation.** Value = (Dream Outcome × Perceived Likelihood) / (Time Delay × Effort). Rate each 1-10. Minimum threshold: ≥ 6.25. Below threshold → redesign. Time Delay and Effort are in the denominator — lower means faster/easier. For denominator guidance and scoring examples, see `references/methodology.md`.

4. **Apply Three Pillars Test.** Check Relevancy (urgent need, not just interesting), Perceived Value (worth giving contact info), True to Your Word (can we fully deliver?). Fail any pillar → redesign.

5. **Test Three Names.** Use the formula: [Specific outcome] + [Target audience marker] + [Timeframe or mechanism]. Evaluate: specific outcome? identifies ICP? includes specificity marker? would ICP pause their scroll? Select primary name; retain two as A/B options. For examples of strong and weak names, see `references/methodology.md`.

6. **Design Frictionless Delivery.** Name + email only. Instant delivery (60 seconds). PDF, video link, or tool URL. Mobile-friendly. No account creation.

7. **Map Nurture Goals.** Define: delivery mechanics, first-touch moment (value in 5 minutes), next problem revealed (the bridge the email sequence must complete), nurture goal (what subscriber should believe before conversion offer). Do NOT prescribe email count or arc structure — brief these goals to `/email-sequence` and let it determine structure. For campaign mode TaskCreate handoff template, see `references/methodology.md`.

8. **Map Distribution Channels.** Identify 3-5 channels: organic, paid, partnership, sales, referral. For each: format requirements, audience fit, cost, expected conversion range. For full channel table, see `references/methodology.md`.

9. **Quality Gate Test.** "Would someone pay for this?" If yes → present to Campaign Lead for Sprint 1 checkpoint. If no → back to Step 1.

---

## Output

Save to: `output/campaigns/[campaign-slug]/strategy/lead-magnet-concept-[date].md`
For standalone use: `output/drafts/lead-magnet-concept-[topic]-[date].md`

Required sections: The Bridge, Lead Magnet Type and Format, Value Equation Score, Three Pillars Test, Name Options, Delivery Design, Nurture Sequence Goals, Distribution Channels, Quality Gate Results, Brief for Creative Specialist.

For full markdown template, see `references/methodology.md`.

**Mark complete:**
```
TaskUpdate(taskId="[ID]", status="completed", metadata={
  "deliverable": "output/campaigns/[campaign-slug]/strategy/lead-magnet-concept-[YYYY-MM-DD].md",
  "assessment": "[1-line: voice X/10, clarity X/10, craft X/10]",
  "ready_for": "campaign-lead"
})
```

**Sprint 1 Checkpoint:** Do not proceed to content creation. Present concept for approval — human selects direction. Include: recommended concept + Value Equation score, alternatives considered + why they scored lower, one open question for the human.

---

## Example

**Scenario:** Lead magnet concept for Acme CI/CD — a CI/CD platform for mid-market engineering teams.

**The Bridge:**
- Narrow problem: Engineering managers can't quantify how much ops time their team spends maintaining CI pipelines
- Lead magnet: CI/CD Ops Cost Calculator — enter team size and incident frequency, get a dollar figure for hidden CI maintenance cost
- Next problem revealed: Once they see the number ($40K–$120K/year is typical), they need a way to eliminate it
- Core offer connection: Acme CI/CD eliminates maintenance burden entirely with managed pipelines

Bridge quality: Natural — the calculator reveals the problem; the product solves it.

**Value Equation Score:**

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Dream Outcome | 8 | Knowing the true cost of CI ops is a career-relevant number for an engineering manager |
| Perceived Likelihood | 7 | Calculator format with benchmarks makes it believable |
| Time Delay | 2 | 5 minutes to enter data and get result |
| Effort & Sacrifice | 2 | 4-5 form fields, no research required |

Value Score: (8 × 7) / (2 × 2) = **14.0** — PASS

**Primary Name:** "The CI/CD Ops Cost Calculator: See What Your Team Actually Spends Maintaining Pipelines"

---

## Quality Gate

Before marking complete:

- [ ] Bridge is natural and logical — solving narrow problem genuinely reveals the next problem (not manufactured)
- [ ] Value Equation score ≥ 6.25 — if below threshold, redesign before proceeding
- [ ] All three Exposure Ninja Pillars pass (Relevancy / Perceived Value / True to Your Word)
- [ ] Quality gate tests pass: "Would someone pay for this?" and "Would the ICP share it with a colleague?"
- [ ] Nurture goals section defines delivery mechanics and bridge — NOT a prescribed email arc
