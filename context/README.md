# Context Directory

This directory contains your persistent context that informs all marketing work.

## Required Files (Create Before Running Campaigns)

### `voice-dna.md` ⚠️ REQUIRED
Your unique voice profile analyzed from writing samples.

**What to include:**
- Sentence rhythm and patterns
- Word choice and vocabulary
- Tone (formal/casual, personal/corporate)
- Personality traits that come through
- What you'd never say (anti-patterns)
- 3-5 writing samples for reference

**Create with:** `/setup` skill or manual analysis

### `icp.md` ⚠️ REQUIRED
Your ideal customer profile - who you're targeting.

**What to include:**
- Demographics (role, company size, industry)
- Pain points they experience
- Goals they're trying to achieve
- Language they use (exact phrases)
- Where they hang out (channels, platforms)
- Objections they typically have

**Create with:** `/setup` skill or interview-based questionnaire

### `business-profile.md` ⚠️ REQUIRED
What you offer and how you position it.

**What to include:**
- Products/services description
- Unique value proposition
- How you're different from competitors
- Pricing model and packages
- Customer results and testimonials
- Your story (why you do this)

**Create with:** `/setup` skill or manual documentation

## Optional Files

### `brand-guide.md`
Visual and stylistic brand standards.

**What to include:**
- Brand colors, fonts, visual style
- Logo usage guidelines
- Image/photo style preferences
- Platform-specific formatting rules
- Dos and don'ts

**Create when:** You have established visual brand standards

---

## Example File Structure

```
context/
├── voice-dna.md          ⚠️  REQUIRED - How you sound
├── icp.md                ⚠️  REQUIRED - Who you target
├── business-profile.md   ⚠️  REQUIRED - What you offer
└── brand-guide.md        (Optional - Visual standards)
```

---

## Important Notes

**Privacy:** These files are .gitignored by default (may contain sensitive business information). Only commit if you're comfortable sharing.

**Agents always read these:** Before any campaign or content work, agents read voice-dna, ICP, and business-profile to ensure alignment.

**Keep updated:** As your business evolves, update these files. Agents will automatically use the latest version.

**Voice DNA is critical:** The quality of voice matching directly depends on the quality of your voice-dna.md file. Invest time in analyzing multiple writing samples.
