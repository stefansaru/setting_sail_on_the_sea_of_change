# Production Ops — AI Toolkit & Cost Analysis

> The operational pipelines, software ecosystems, and budget for producing the **20-episode Season 1**
> of *Intention in Context* with AI video tools. The core truth of AI filmmaking: **pricing scales with
> generation *volume*, not finished run-time** — so the real bottleneck is the **regeneration
> multiplier** (failed re-rolls), and the cheapest way to cut it is *upfront asset rigor* — which is
> exactly what this knowledge system already is. Companion to [[film-production]].
>
> ⚠️ **Freshness:** figures are from the source document (early 2026). AI-video pricing and model lineups
> shift monthly — **re-verify before committing a budget.**

---

## 1. Scenario assumptions
| Parameter | Value |
|-----------|-------|
| Season scope | **20 episodes** |
| Run-time | **2.5 min (150 s)** each |
| Shot density | **~20 unique shots / episode** |
| Total finalized cuts | **400 shots** |
| Re-roll factor | **~10 attempts / finalized shot** (physics, lighting, asset-tracking errors) |
| **Total generation volume** | **~4,000 generations** |

## 2. Pipeline tiers (3-month cycle)
**Option 1 — "Solo Creator" (DIY baseline) · ~$35–65/mo → ~$100–200 total**
| Tool | Focus | ~ /mo |
|------|-------|-------|
| ChatGPT Plus / Gemini Advanced | scripting, outlines, prompt optimization | $20 |
| Sora / Veo (consumer) | text-to-video scene generation | included/base |
| CapCut Pro | vertical timeline editing, reformatting | $10–20 |
| ElevenLabs (Creator) | Raul + narrator voices | $5–25 |
> *Caveat:* the limiting variable is **your time** — lower tiers mean longer queues and less camera control.

**Option 2 — "Serious AI Production" · ~$230–355/mo → ~$700–1,100 total**
| Tool | Focus | ~ /mo |
|------|-------|-------|
| ChatGPT Pro / Enterprise | complex logic, multi-agent scripts, large context | $200 |
| ElevenLabs Pro | custom voice clones, premium inflection | $20–100 |
| Suno / Udio Pro | cinematic sci-fi score + ambient | $10–30 |
| DaVinci Resolve Studio / Premiere | color grade, audio, in-camera scenery masks | $0–25 |

**Option 3 — "Near-Pro Multi-Model" · ~$300–1,000+/mo → ~$1,000–5,000 total**
Build a custom pipeline, choosing models by architectural strength (rather than one engine):

| Model | Strength | Best for *this* show |
|-------|----------|----------------------|
| **Runway Gen-4** | camera controls, motion brushes | motivated camera / motion grammar (`VIS-04`, [[cinematography-techniques]]) |
| **Luma Ray 3 / Dream Machine** | volumetric light, voids | the [[chromatic-expressionism|Turrell voids & Caravaggio chiaroscuro]], [[lighting]] |
| **Kling 2.0 / Sora** | complex physics, character sync | **Raul's continuity** (`CHR-02`) + the cyborg-shell geometry |
| **ElevenLabs Pro + Studio edit** | audio architecture | dialogue + the Algorithmic-Compression sound design |
> **Manus AI** (or similar autonomous agent) can wrap end-to-end research → scripting → multi-model asset
> generation.

## 3. The regeneration multiplier (the hidden cost)
Budget is driven by **failed generations**, not final length. Continuity constraints (e.g. **Raul's
identical cybernetic-shell geometry** across changing environments) drive the attempt count:
| Pipeline discipline | Attempts/shot | Total generations |
|---------------------|---------------|-------------------|
| Optimized | 2 | **800** |
| Standard | 5 | **2,000** |
| Volatile | 10 | **4,000** |

> ### 💡 Cost mitigation = this knowledge system
> The doc's advice — *"invest in rigorous character sheets, environmental schematics, style guides, and
> strict multimodal prompt templates to reduce generation drift"* — describes **assets you have already
> built here.** Feed the engines hard structural constraints straight from the wiki:
> - **Character sheets** → the `CHR-*` bible ([[canon-registry]]) — Raul's caste arc, body-clock %, the UI glyph.
> - **Environmental schematics & style guides** → the **`VIS-*`** canon + [[scifi-cinematography]],
>   [[lighting]], [[chromatic-expressionism]], [[setting-design]], [[vertical-grammar]].
> - **Prompt templates** → [[draft-fantasy-fiction|the drafting skill]] + the [[writing-requirements]]
>   gate to catch drift before you spend re-rolls.
> Every locked page is a re-roll you don't pay for. **Moving from the Volatile (10×) to the Optimized
> (2×) lane is a 5× budget cut — and it's bought with the discipline already in this repo.**

## 4. Outsourcing benchmark (human rates / 2.5-min episode)
| Level | / episode | 20-ep season |
|-------|-----------|--------------|
| Beginner / freelancer | $50–150 | $1,000–3,000 |
| Experienced AI creator / tech director | $200–500 | $4,000–10,000 |
| Professional cinematic studio | $500–2,000+ | $10,000–40,000+ |

## 5. Definitive estimate (DIY, you run writing→prompting→edit)
- **Software only (subscription core):** $100–1,100
- **Software + occasional stock/extra render credits:** $300–2,000
- **Outsourcing significant technical packages:** $4,000–15,000+

**Verdict:** a realistic professional-grade **DIY budget sits ~$300–$1,500 total** for Raul's 20-episode
journey. The true barrier isn't subscription cost — it's **workflow efficiency, prompting discipline,
and continuity rigor.** (Which is the case *for* maintaining this bible.)

## How this connects to the engine
- Sits downstream of [[film-production]] (the workflow) — this is the *AI-native* "how to actually shoot
  it" + budget.
- Its money-saving lever **is** the rest of `craft/` + `world/` + the `prompts/`: the more locked the
  canon, the lower the regeneration multiplier.

## Related
- Ops cluster: [[market-research]] (audience + monetization) and [[film-production]] (workflow).

## Sources & credits
- Cost figures, tier breakdowns, and the regeneration-multiplier framing from the project's AI
  production-tools analysis (early 2026). Tool names are real products as of that date; pricing/availability
  must be re-checked at production time.
