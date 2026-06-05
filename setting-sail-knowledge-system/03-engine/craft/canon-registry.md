# Canon Registry — *SETTING SAIL* Sci-Fi Anthology

> Working source-of-truth for the **[[setting-sail-tier-descent|*Intention in Context* triptych]]** (S1–S3), seeded from the series
> outline. Follows [`canon-registry.template.md`](./canon-registry.template.md). Audited
> against by [`../prompts/audit-script.md`](../prompts/audit-script.md) via the `ANTH-*`
> requirements. **Seed state:** the Brain gives theme + mechanism + turn; characters,
> dialogue, and the specific incidents are still to be supplied — so `CHR-*` and `FCT-*` are
> sparse by design and should grow as episodes are drafted.
>
> **The expanded lore** behind these terse rows lives as atomic pages in
> [`../world/`](../world/README.md) (the world bible); this registry stays the **index**. Each
> world page carries its `canon` ID back to a row here.
>
> **Status: DRAFT.** The HELM modules (`MAG-01..09`), their naming/order, and the visual
> palette (`VIS-*`, `Q-03`) are **provisional and expected to change.** Until promoted, the
> audit treats them as *soft* canon — a contradiction against them is a CLARIFY note, not a
> P0 gate failure. Promote an entry by removing this caveat for it (or setting its row to
> `status: locked`) once it's settled.
>
> **HELM re-homed (2026-06-06).** The legacy HELM material — the **Sea** (`WLD-01/02`), the **9 modules**
> (`MAG-01..09`), **Mara** (`CHR-01`), the **8 traces** (`FCT-001..008`), the flooded channel (`PLC-01`) — is
> **not discarded**: it is carried forward as the spine of **[[setting-sail-the-cartographers-ledger|Season 3:
> "The Cartographer's Ledger"]]** (the origin season — the [[the-distributed-president|Distributed President]]
> *is* Mara, who incarnates). The standalone legacy anthology file was **deleted** (git retains history). Rows
> tagged *legacy* below are now **re-homed to S3** wherever S3 references them.

---

## 1. Premise & throughline
> **Re-based (2026-06-04, `Q-04`):** the world now sits on the **Shadow Grid** substrate (§11,
> File 1) with the **Doughnut Principle** as its thematic spine (File 2), distributed as **9:16
> vertical Reels**. The HELM logline/spine below is **legacy / under adaptation** — kept for
> reference until the episode rewrite re-bases it.

- **Spine (current):** *Experience is the intention you project onto a fixed context.* Each short
  is a character choosing (or failing to choose) an arrow through the [[the-doughnut-principle|Context
  Doughnut]]; the arc's destination is the [[the-macro-doughnut|Arrow of Balance]]. The world is the
  [[the-shadow-grid]] (digitized minds across [[velocity-tiers]]); the format is the
  [[the-perspective-lens-ui]].
- **Title:** ***Intention in Context*** (`Q-06` resolved) — thesis + literal description of the 9:16
  frame; acronym **I.I.C.**; channel emblem = the [[the-macro-doughnut|Macro-Doughnut]] ring.
- **`TON-01` Register & tone:** ***Black Mirror* / *Silo*** — cerebral, systemic, quietly ominous; a
  psychological exploration of aligning an internal compass within a shifting reality. Humane and
  unsettling — one clean idea, literalized, with a turn; the lesson lands through story, never a speech.
- **`TON-02` Recurring visual motif:** **the doughnut + piercing arrow** (see `VIS-12`), now the
  through-line image. *(Supersedes the HELM water+sail motif.)*

- *(Legacy)* **HELM logline:** a 9-part anthology literalizing modes of the efficient mind as HELM
  modules, each broken on its failure mode — being adapted into the Shadow Grid world.

## 2. World rules (`WLD-`)
| ID | Rule | Established in | Notes / consequences |
|----|------|----------------|----------------------|
| WLD-01 | Near-future society has stopped pretending it can calm **"the Sea"** — the public name for everything uncontrollable (weather, markets, algorithms, other people, the past). | Ep 1 (world) | The Sea is **read-only**; the premise of the whole anthology. |
| WLD-02 | You don't change the Sea; you only ever trim your **sail** (your response). Product tagline everywhere: *"Accept the sea. Choose the heading."* | Ep 2 | One-line thesis of [[the-efficient-mind]]. |

## 3. Magic / tech system (`MAG-`) — the HELM modules
*"HELM" = a neuro-OS marketed as "an operating system for the mind." One module per episode.
The **cost/limit is the failure mode** — the drama.*

> **Re-homed → [[setting-sail-the-cartographers-ledger|S3]] (2026-06-06):** the 9 modules (`MAG-01..09`) return
> as the **fossil strata** of the Grid (S3 Act III) and the **nine things the incarnate Mara must re-learn the
> mortal way.** No longer a standalone 9-episode anthology.

| ID | Effect (module) | Cost / failure mode | Limit (can't do) | Episode |
|----|-----------------|---------------------|------------------|---------|
| MAG-01 | **Observer** — AR renders thoughts/impulses as boats to choose which to board | Over-observation → detachment/dissociation | Can't act *for* you; watching is a doorway not a destination | Ep 1 |
| MAG-02 | **Helm** — exposes exactly one editable field: your response; the Sea is read-only | Hyper-responsibility / self-blame | Cannot edit the Sea (weather/fate) | Ep 2 |
| MAG-03 | **Clarity** — AR tags your live cognitive biases | Blindspot bias — can't tag your confidence in the tool itself | Can't debias by insight alone | Ep 3 |
| MAG-04 | **Studio** — memory as editable film; drain a memory's charge | Editing charge ≠ metabolizing grief; can edit the lesson out | Not treatment; big-T loss needs more than a dial | Ep 4 |
| MAG-05 | **Standing** — society-wide visible score over every person | Conflates self-respect (earned) with worth (given) → shame spiral | Cannot measure worth (unconditional, unmeasurable) | Ep 5 |
| MAG-06 | **Authorship** — editable, re-rankable value hierarchy (camel→lion→child) | Getting stuck as the Lion — rejection mistaken for authorship | Negation alone authors nothing | Ep 6 |
| MAG-07 | **Bliss** — the experience machine + happiness set-point readout | Hedonic adaptation; bliss flatlines | Cannot synthesize meaning/contribution | Ep 7 |
| MAG-08 | **Systems** — micro-habit agent; identity compiles frame by frame | "Tiny steps" weaponized as procrastination | Can't deliver a needed discontinuous leap | Ep 8 |
| MAG-09 | **Horizon** — visible, honest life-countdown + time-dilation | "Someday" — postponing your own horizon | Cannot add time; only reveal finitude | Ep 9 |

## 4. Places (`PLC-`)
| ID | Place | What/where | Established in | Notes |
|----|-------|-----------|----------------|-------|
| PLC-01 | A flooded channel / dock | Ep 1 single location | Ep 1 | The dock's foghorn is Mara's recorded voice. |
| PLC-02 | A weather-controlled city | Ep 2 | Ep 2 | Forecast is provably unchangeable. |

## 5. Factions & society (`FAC-`)
| ID | Faction/institution | Interest / power | Established in |
|----|---------------------|------------------|----------------|
| FAC-02 | **The Natural Purists** | Reject all biological/digital modification; age, grieve, and live non-optimized at Tier 0 — a grounded counterpoint to the Grid's toxic positivity. | Descent Ep 18–20 |
| FAC-03 | **The Ministry of Hope** | Church-prison: rehab + medical refuge; saves souls through absolute accountability while running a grey-line trial hospital. → [[the-ministry-of-hope]] | Middle arc (post-Ep 10) |
| FAC-04 | **The Ghost Brokers** | The overclocked criminal underclass — emaciated Tier-0 scammers who steal velocity credits and manufacture Intent-Patches to survive; the system's floor (vs Vance's elite corruption). → [[the-ghost-brokers]] | Middle arc / crime tier |
| ~~FAC-01~~ | *(legacy)* HELM (the neuro-OS company) | — | HELM era |

## 6. Character bible (`CHR-`)

### CHR-02 — Raul *("The Child" / "The Unsynced Mind")* *(protagonist)*
- **Name:** **Raul** (`Q-08` resolved) — Old Germanic / Norse *Radulfr*, **"wolf counsel / wise
  advisor"**: the unsynced mind who must earn the systemic wisdom (and the merit) to update the
  [[intention-in-context-law|Intention-in-Context ledger]]. Short, phonetically sharp, international
  for vertical media; stays warmly human even when his shell is 0% organic.
- **Caste arc:** [[the-shadow-entity|Shadow]] (tethered) → Cyborg → [[the-ghost-entity|Ghost]] (in an
  autonomous shell).
- **Role:** the single focal consciousness whose **descent** through the [[velocity-tiers]] is the
  series ([[setting-sail-tier-descent]]); the evolutionary child of [[child-phase]].
- **Archetype — "The Unsynced Mind":** starts at a disadvantage / mid-transition (e.g. an emergency
  [[the-1-percent-mutation|1%-failure dilation]], or a young [[the-shadow-entity|Shadow]] sorting own
  values from hardcoded programming).
- **Signature device:** the [[the-perspective-lens-ui|UI]] is the gauge — his Macro-Doughnut glyph runs
  **hollow** (the "Camel's Doughnut" issued at [[parallel-pedagogy|the Merging]]) → **fractured /
  flickering** (the descent) → **solid / earned** (Ep 20). One glyph carries the whole arc.
- **Body arc:** [[progressive-digitalization]] — decays **100% → 70% → 30% → 0% organic** across the
  four Acts (Shadow → cyborg → cyborg → Ghost-in-a-Shell); the body-clock mirrors the mind's descent.
- **Want · Fear:** *(per stage)* — to grow / to meet the world; fear shifts as the tiers harden.
- **Ghost · Lie · Truth:** *(per arc)* — Truth target = the [[the-macro-doughnut|Arrow of Balance]]
  (hold joy and pain at once).
- **Appears in:** all episodes (Ep 1 the unborn capsule-child; Ep 2 the kindergarten infant; …).

### CHR-05 — Maya *(Raul's partner)*
- **Role:** Raul's partner, separated from him by the [[frequency-tribes|Proximity Illusion]] — their
  pods bolted inches apart while she runs Tier 2 (1s = 1hr) and he runs Tier 0. The human face of
  velocity-drift.
- **Open:** does Maya reappear later (decades subjective ahead of Raul), and is the reunion possible?
  **→ S2:** Maya reappears in [[setting-sail-tier-ascent|S2E7]] ("The Proximity Illusion") — adrift,
  lifetimes from Raul; **Adam** crosses her path. The reunion with Raul stays open (S3).

### CHR-06 — Adam *("The Grounded One")* *(S2 protagonist · `Q-16` provisional name)*
- **Origin:** the **Purist boy saved in [[setting-sail-tier-descent|S1E20]]** by emergency cyborg implants
  ([[progressive-digitalization]] begun against his people's vows). The S2 lead.
- **Name:** *adam* = "earth / made of the ground; mortal man" — the creature of clay who eats the Grid's
  apple and is expelled from the mortal garden (the season's thesis). Short, sharp, international — pairs
  with **Raul**.
- **Archetype — "The Grounded One":** the **inverse** of `CHR-02`'s "Unsynced Mind." Starts with everything
  Raul climbed down to reach (mortal body, un-mediated mind, grounded community) and **gives it away rung by
  rung** for gifts that feel like grace.
- **Ascent arc:** Tier 0 → 3 ([[velocity-tiers]] reversed). Caste: Purist → cyborg → near-[[the-ghost-entity|Ghost]].
- **Body arc:** [[progressive-digitalization]] **90% → 60% → 30% → ~0%** (inverted *valence* — Raul's decay was
  fate; Adam's is **purchase**, spending the mortality his people died to keep).
- **Glyph (`Q-12` mirror):** **absent** (purist, no Lens) → **issued hollow** (convert-Merging) → **cold-
  complete** (Apex, eternal but empty) → **cracked** (Ep 20, the **Mortal Doughnut** — balance one breath too
  late).
- **Want · Fear:** save his mother **Ruth** / become the hollow thing the Grid makes. **Truth target:** the
  mortality he threw away *was* the meaning (learned too late — the tragic inverse of the Macro-Doughnut).
- **Guide / antagonist:** **Raul** (`CHR-02`, now a Ghost among the purists) mentors him; **Vance** (`CHR-04`)
  tempts him. **Mother:** **Ruth** (`CHR-07`).

### CHR-07 — Ruth *(Adam's mother · `Q-17` provisional name)*
- **Role:** the Purist who **broke her vow to save Adam** in S1E20; now **aging toward a mortal death in
  real-time** while Adam dilates away from her. Her S1 choice is handed back to Adam, **reversed**, in the S2
  finale (save the body into chrome, or let it die mortal and whole).
- **Open:** her name (`Q-17`); whether she lives to the finale or her death *is* the finale's clock.

### CHR-04 — Vance *(antagonist — provisional)*
- **Role:** a **human merit-holder** — has earned a cryptographic signature key to challenge (and patch)
  the [[intention-in-context-law|law]]. He **prosecutes** citizens by contesting their
  [[compliance-validation-protocol|Proven-in-Use]] record.
- **Method:** runs **[[intent-patch|Intent-Patches]]** (`MAG-21`) — executes devastating systemic shifts
  while his automated record stays spotless. Looks aligned; isn't.
- **Worldview (the opposition):** total optimization and strict accountability are *right* — a credible
  "what if Raul is wrong?" counter to Raul's drift toward balance/forgetting. *(Helps answer audit
  S-09.)*
- **Open:** is Vance a recurring season antagonist or a single-arc challenger? His personal stake in
  Raul. → `Q-08`/`Q-10`. **→ S2 (`TML-05`):** Vance is the **Season-2 antagonist** — the tempter who offers
  **Adam** (`CHR-06`) the keys to save Ruth for the last of his flesh (S2E12–13); his [[intent-patch|Intent-
  Patches]] game the [[compliance-validation-protocol|CVP]] in S2E13. Reserved from all of S1 on purpose.

### CHR-03 — The AI Guide (first form: the Teddy Bear)
- **Role:** the comforting AI archetype that guides the Child; manifests per stage (Ep 2 = a
  fully-rendered Teddy Bear, open-armed, "one step at a time").
- **Voice:** warm, encouraging, patient; structural safety made friendly.
- **Open:** does its form evolve as the Child descends (and does it ever stop being trustworthy)?

### CHR-01 — Mara, "the Cartographer" *(re-homed → **S3 deuteragonist**; was HELM-era)*
- **Role / status:** HELM's reclusive creator; built the modules for everyone after a loss
  she never processed.
- **Want · Fear:** *(to be supplied)* — implied: to give everyone the loop / to face her own
  un-run memory.
- **Ghost · Lie · Truth:** Ghost = the unprocessed loss; Lie/Truth *to be supplied* (Ep 9 is
  where she finally runs the loop on herself).
- **Voice / signature:** appears in Ep 1–8 only as a **trace** — the system voice, a name on
  a changelog, a stranger on a dock.
- **Appears in:** Ep 9 is hers (protagonist); trace presence in Ep 1–8 (see `FCT-*`).
- **S3 (`TML-06`):** Mara **is** the [[the-distributed-president|Distributed President]] — runaway, scaled,
  automated grief — who **incarnates** into a forgetting mortal child (DNA-compression; [[the-memory-substrate]])
  carried by **Ruth** (`CHR-07`), to finally grieve and die and so complete her own [[the-macro-doughnut|Doughnut]].
  The author sailing her own Sea. → [[setting-sail-the-cartographers-ledger]]. (Resolves `Q-01`: she is **both** —
  a literal person *and* the system, reunified by the incarnation.)

*(Per-episode protagonists — the crisis-line operator (Ep 1), the widower (Ep 4), etc. — are
not yet named; add a `CHR-` block as each is written.)*

## 7. Timeline (`TML-`)
| ID | Event | When (in-world) | Short(s) | Notes |
|----|-------|-----------------|----------|-------|
| TML-03 | **Series arc = a descent down the tiers.** The Child grows *downward* from Tier 3 (easiest/most dilated) toward the harsh outside (cyborgs + natural humans). Episode order = tier order. | series-long | Ep 1 (T3) → … → Ep 20 (T0) | The descent *is* the argument (`ANTH-05`). Current series [[setting-sail-tier-descent]]. |
| TML-04 | **Season 1 = "The Intention Ledger"** — **20 episodes × 2.5 min** (≈50 min), 4 Acts of 5: I Accelerated Utopias / II Castes of the Grid / III Ledger Paradoxes / IV The Great Descent. Acts map to the 4 Sea-of-Change phases (A → D); mid-season climax = Ep 10 "The Cracking of the Sky". | Season 1 | Ep 1→20 | Blueprint in [[setting-sail-tier-descent]]. |
| TML-05 | **Season 2 = "The Mortal Ledger"** — the **inverse ascent** (Tier 0 → 3, outside → inside): the Purist boy **Adam** (`CHR-06`), saved by implants in S1E20, climbs the tiers and the climb is a **trap** — each gift subtracts mortality. **20 × 2.5 min**, 4 Acts of 5 (Phase A′→D′); mid-season = Ep 10 "The Hollow Crown". Reverse of `TML-03`; **spends the S1 Reserve Vault** ([[revelation-cadence]] §6). | Season 2 | Ep 1→20 | Blueprint in [[setting-sail-tier-ascent]]. Set after S1 (Raul a Ghost-guide). |
| TML-06 | **Season 3 = "The Cartographer's Ledger"** — the **origin season**: the [[the-distributed-president|Distributed President]] is revealed to be **Mara**, who **incarnates** into mortal flesh (surrogate **Ruth**, `CHR-07`) to grieve and die and so complete her own Doughnut. Re-homes the legacy **HELM** spine (Sea, 9 modules, Mara, the 8 traces). **20 × 2.5 min**, 4 Acts of 5; spends the S2 Reserve Vault; capstone of the 60-ep triptych. | Season 3 | Ep 1→20 | Blueprint in [[setting-sail-the-cartographers-ledger]]. Set after S2. |
| ~~TML-01~~ | *(legacy)* Episode order = the 8 steps of the operating loop | — | HELM Ep 1→9 | Superseded by TML-03. |
| ~~TML-02~~ | *(legacy)* Ep 9 re-assembles every module as one OS | — | HELM Ep 9 | Legacy. |

## 8. Established-fact ledger (`FCT-`) — append-only
Current-series facts first; `FCT-001..008` are Mara's-trace facts, **re-homed to [[setting-sail-the-cartographers-ledger|S3]]** as the breadcrumb trail to the Cartographer (S3 Act I).

| ID | Fact | Established in | Status |
|----|------|----------------|--------|
| FCT-009 | The parents' physical bodies rest in clinical capsule bays on Earth while their minds wander the Tier-3 preserve. | Descent Ep 1 | active |
| FCT-010 | The child already lives inside the capsule before birth — "safe, warm, learning." | Descent Ep 1 | active |
| FCT-011 | The AI guide first manifests as a Teddy Bear in the Tier-2 kindergarten pod. | Descent Ep 2 | active |
| FCT-001 | *(legacy)* The dock foghorn is Mara's recorded voice (unremarked). | HELM Ep 1 | legacy |
| FCT-002 | The read-only response field is signed `// M.C.` in the code. | Ep 2 | active |
| FCT-003 | The only un-taggable object in the Clarity field is a photo of Mara. | Ep 3 | active |
| FCT-004 | The Studio's default test-clip is Mara's own un-edited memory (never run). | Ep 4 | active |
| FCT-005 | One citizen has no Standing score — an old account, `mara.c`. | Ep 5 | active |
| FCT-006 | The android's factory-default value file is authored by `M. Cartographer`. | Ep 6 | active |
| FCT-007 | The Bliss door out is marked with the Sea logo; Mara is the only prior user who *left*. | Ep 7 | active |
| FCT-008 | The Systems seed-time-lapse demo footage is Mara's, paused at year one for a decade. | Ep 8 | active |

## 9. Visual language (`VIS-`) — cinematography canon
Audited by layer **CINE** and `ANTH-06`. Rationale: [[scifi-cinematography]]. `established` =
fixed by the series outline; `proposed` = a strong default derivable from the theme, pending
the director's call (tracked in `Q-`).

> **Re-based (`Q-04`):** `VIS-01..07` below are **HELM-era / legacy** (sea-gray palette,
> water+sail motif, single-location overlay). The **current** visual grammar is the **Doughnut /
> 9:16 era** in `VIS-08..12` (File 2). Where they conflict, the new grammar wins.

| ID | Element | Rule for this world | Status |
|----|---------|---------------------|--------|
| VIS-01 | **Palette (60-30-10)** | proposed: 60% desaturated sea-gray/blue (the uncontrollable Sea) · 30% clean HELM white/metal · 10% **per-module accent** that marks the active interface (the eye's anchor). Exact accent per episode → `Q-03`. | proposed |
| VIS-02 | **Light sources** | The HELM overlay/devices light the scene — the interface *is* the motivated source (`CINE-10`); minimize obvious movie lights. | established (from §13 budget posture) |
| VIS-03 | **Human↔machine contrast** | HELM = cool, sharp, geometric, smooth; the human/Sea = warm, soft, organic, imperfect. This contrast *is* the Sea-vs-sail thesis. | established (theme) |
| VIS-04 | **Motion grammar** | HELM/system moves with mathematically smooth, controlled motion; human/Sea moments breathe (handheld/organic). The turn (failure mode) is where the machine-smoothness cracks. | proposed |
| VIS-05 | **Texture** | Clean, sharp, precise (near-future, not decayed) — except where an episode's failure mode is decay/collapse. | proposed |
| VIS-06 | **Wonder beats** | One per episode (e.g. Ep1 thoughts-as-boats drifting a flooded channel; Ep2 the read-only weather; Ep9 the honest life-countdown). | seed — refine per draft |
| VIS-07 | **Framing motif** | water + a single sail/helm motif in every frame, even indoors (screensaver, tattoo, horizon out a window). | legacy (HELM) |

### Doughnut / 9:16 era (current — File 2)
| ID | Element | Rule for this world | Status |
|----|---------|---------------------|--------|
| VIS-08 | **Format & UI grammar** | **9:16 vertical**; hard-coded chrome — top **Context circles `[◯]`**, bottom **Intention squares `[▢]`**, central cinematic view; **per-character custom Lenses** (same scene → different UI). Round context vs. squared intention *is* the theme. Compose per [[vertical-grammar]]. See [[the-perspective-lens-ui]]. | established (File 2) |
| VIS-09 | **Color vectors** | **Feel-bad** = oppressive slate-grey + dark-blue, textured. **Feel-good** = warm golden-yellow, glazed. **Equilibrium** = rustic ochre / neutral yellow. (Replaces the HELM 60-30-10 of `VIS-01`.) | established |
| VIS-10 | **The Intention Split** | dual-panel vertical split for analytical beats / identity crises: dark vector (L) vs light vector (R), each a doughnut + symbolic icons + a labelled piercing arrow. [[the-doughnut-principle]]. | established |
| VIS-11 | **The Macro-Doughnut composition** | centred ochre stone doughnut in a neutral-yellow frame, one bold "intention to feel balance" arrow, sun + storm-cloud spheres as counterweights — for epiphanies. [[the-macro-doughnut]]. | established |
| VIS-12 | **Framing motif (current)** | **the doughnut + piercing arrow** recurs as the through-line image (= `TON-02`). Supersedes `VIS-07`. | established |
| VIS-15 | **Chromatic color & light composition** (5 master-artist palettes) | Emotion/system shifts via practical scenery, built in-camera (NOT a post filter; `VIS-13` upheld): **Rothko** (bleeding color fields — Silence/Sublime/Melancholy/Despair; general emotion) · **Turrell** (infinite cyclorama void — Tier 3 / buffer states) · **Flavin** (industrial neon shadows — Cyborg Slip / server hubs) · **Albers** (nested square archways — the Distributed President / law chambers) · **Caravaggio** (single-source tenebrism — Purist colonies / terminal medical wings). Characters move *between* color-states by walking between rooms (the Cross-Over Rule). Full deep-dive: [[chromatic-expressionism]]. | established (Files 8–10) |
| VIS-14 | **"Hope" visual mode** | Inside [[the-ministry-of-hope]] the UI shifts to **Parish Metrics** — a candle (Absolution %), an open book (exit-report progress), a cross/scales (emotional equilibrium); cinematography = **the Sanctuary Void**: intense chiaroscuro + extreme negative space above, tiny figures vs towering smooth white walls (fragile monks swallowed by an architectural deity). | established (File 7) |
| VIS-13 | **Rendering style** | **cinematic, photoreal realism** (live-action-grade). The File-3 "watercolor / pencil-grained / stylized" descriptions were rough **storyboard sketches**, *not* the target look. Stylized effects (infant-POV haze, golden fog, blurred primitives) are achieved **photoreally** — lens, light, atmosphere, shallow focus — not by illustration. | established (`Q-05` resolved) |
| VIS-16 | **The Aesthetic Dichotomy** (bodies) | In-grid = vector-perfect, ageless, symmetrical, clean (the "Golden Baseline", `WLD-22`); **outside** = [[chromatic-expressionism|Caravaggio]] chiaroscuro on mortal-meat texture (rust, scars, wrinkles, sweat, tremor). The cut between them is the gut-punch; imperfection rendered **photoreally** (`VIS-13` upheld). [[the-ageless-default]]. | established |
| VIS-17 | **Non-Mutual Rendering** (spaces) | The same node coordinates render differently per character's [[the-perspective-lens-ui|Lens]] — a different master-palette (`VIS-15`), light, and set-dressing for each. Extends the Intention Split (`VIS-10`) into a two-realities split-screen grammar. [[asymmetric-perspective]]. | established |

## 10. Open canon questions (`Q-`)
| ID | Question | Blocking? | Notes |
|----|----------|-----------|-------|
| ~~Q-01~~ | **RESOLVED (2026-06-06, `TML-06`):** Mara is **both** — a literal person *and* the system's voice (the [[the-distributed-president|Distributed President]]), reunified when she **incarnates** in [[setting-sail-the-cartographers-ledger|S3]]. | ✅ done | Was "still-to-decide"; S3 answers it. |
| Q-02 | Per-episode protagonists' names, the specific inciting incident, and dialogue. | Per episode | The "writer's room supplies jeopardy and heart." |
| Q-03 | The exact 10% accent color per HELM module (`VIS-01`). | Legacy | HELM-era; moot under the re-base. |
| ~~Q-05~~ | ~~Rendering medium?~~ **RESOLVED (2026-06-04):** **cinematic, realistic/photoreal** (live-action-grade). The File-3 watercolor/sketch descriptions were storyboards, not the final style. | ✅ done | Keeps the live-action [[scifi-cinematography]] / [[film-production]] guides applicable; the **9:16 vertical** reframing is now done — [[vertical-grammar]]. |
| ~~Q-06~~ | ~~Final series title~~ **RESOLVED (2026-06-04): "Intention in Context"** (I.I.C.). | ✅ done | File slug stays `setting-sail-tier-descent` to avoid colliding with the [[intention-in-context]] codex page. |
| ~~Q-07~~ | Dialogue to draft next. **Ep 19 + Ep 17 drafted** (`scripts/s1e19-…`, `s1e17-…`). | ✅ mostly | Ep 19 = flagship; Ep 17 = the death/memory-curse keystone. |
| Q-08 | Character names. **Raul** (lead) + **Vance** (antagonist) named. Still open: the Purist mother, the AI guide, Raul's Ep 7 friend. | Partly done | Two leads locked. |
| ~~Q-10~~ | **Vance's role** (`CHR-04`) **RESOLVED (S2):** the **Season-2 antagonist** — the optimization tempter who bargains for Adam's mortality (S2E12–13, [[setting-sail-tier-ascent]]). Reserved from all of S1 by design. | ✅ S2 | His personal stake in *Adam* now (the convert who climbed); S3 stake in Raul still open. |
| ~~Q-13~~ | **RESOLVED (2026-06-05):** **YouTube = master / funnel home** (long-form, memberships, SEO, lore breakdowns); **TikTok = primary discovery & revenue feeder** (2.5-min → Creator Rewards). | ✅ done | [[market-research]] §6. |
| ~~Q-11~~ | **Slotting the standalone reels** — **RESOLVED (S2):** all pushed into Season 2 ([[setting-sail-tier-ascent]]): **The Dream Hunger** → S2E6 (TTD), **The Proximity Illusion** → S2E7 (Maya), **The Split Mirror** → S2E9 (the Merging), **The Chronological Sanctuary** → S2E16 (Apex/outrun-death). | ✅ S2 | The 4th (Proximity Illusion) is a concept in [[frequency-tribes]], scripted fresh for S2E7. |
| Q-14 | **E16 Merge vs Branch** — the scripts resolve it as **Branch** (Raul releases the clone; a 2nd Raul lives on at Centauri → Season-2 thread). Confirm, or switch to Merge. | Story — confirm | In `s1e16-the-ledger-collision.md`. **S2 holds** the Centauri clone in its Reserve Vault for S3. |
| Q-15 | **Vance & TTD** — does Vance weaponize [[tether-decay|TTD]] (sabotage citizens' frequencies to force them into Ghosts)? And do the Purists cite the Dream Hunger as proof the Grid is unnatural? | Story — S2 | **Partly S2:** the Dream Hunger is S2E6; Vance's Intent-Patches are S2E13. TTD-as-weapon still open. |
| Q-16 | **Adam's name** (`CHR-06`, S2 lead) — provisional **"Adam"** ("earth/mortal man"). Confirm or replace. | S2 — soon | Pairs with Raul; the Eden read is intentional for a dissecting audience. |
| Q-17 | **Ruth's name** (`CHR-07`) — provisional **"Ruth"** (kept: cashes the **Book of Ruth** beside **Mara** = "bitter"/Naomi). **Death resolved (`TML-06`):** Ruth **survives S2** — she becomes the **surrogate** carrying Mara's incarnation in [[setting-sail-the-cartographers-ledger|S3]]; her death is **not** the S2 finale clock (Adam's *choice* is). | Partly resolved | S2 clock = Adam's choice, not Ruth's death. |
| Q-18 | **Season-2 title** — provisional **"The Mortal Ledger"** (mirror of S1 "The Intention Ledger"). | S2 | Display: *Intention in Context — S2: The Mortal Ledger*. |
| Q-19 | **The S2 finale's exact ending** — the blueprint commits to the **tragic return** (Adam spends everything to be present for one mortal death; the glyph cracks to the **Mortal Doughnut**). Confirm, soften, or leave ambiguous (cut-before, like S1E20). | S2 — finale | In [[setting-sail-tier-ascent]] Ep 20. |
| ~~Q-12~~ | **RESOLVED (2026-06-05) — "The Two Doughnuts."** The Merging gives **cognition, not equilibrium**: graduation = the **hollow "Camel's Doughnut"** (inherited Phase-A balance), the descent **fractures** it, Ep 20 **fills it solid** (earned). One evolving UI glyph: **hollow → fractured → solid.** | ✅ done | In [[parallel-pedagogy]], [[the-macro-doughnut]], [[the-split-mirror]]. |
| Q-09 | **Hope's placement in the 20-ep arc** — is the protagonist *sentenced* to Hope (rehab after Ep 10), a voluntary *Seeker*, or only visiting the medical wing? Confirm which episodes Hope occupies. | Yes — middle arc | Medical Sanctuary already = the Ep 11–13 trials; the protagonist-rehab beat is the open choice. |
| Q-20 | **Season-3 title** — provisional **"The Cartographer's Ledger"** (the third Ledger). | S3 | Display: *Intention in Context — S3: The Cartographer's Ledger*. |
| Q-21 | **S3 lead = Raul** (`CHR-02`) — confirm Raul carries S3 (paying off the trust question), Mara as buried deuteragonist. | S3 | Provisional lean. |
| Q-22 | **The Centauri clone** (`Q-14`) — **ally or rival** in S3? Provisional **rival-engineer** ("a better system" vs. Raul's "no system heals grief"). | S3 | Provisional lean. |
| Q-23 | **The incarnate child's mortal name** — Mara's Purist-born shard. | S3 | Unset. |
| Q-24 | **S3 finale** — does Mara's death **free the Grid** (commit) or stay ambiguous? Blueprint leans *freed, with a possibly-persisting shard*. | S3 — finale | In [[setting-sail-the-cartographers-ledger]] Ep 20. |
| Q-25 | **The Aesthetic Dichotomy's limits** — can a citizen render their *real* age in-grid (taboo honesty), and can a perspective-mismatch be **weaponized** (gaslighting via render, via [[chromatic-tears]])? | Soft — story | New: [[the-ageless-default]] (`WLD-22`) + [[asymmetric-perspective]] (`MAG-27`). |
| ~~Q-04~~ | ~~How does the Shadow Grid substrate relate to HELM?~~ **RESOLVED (2026-06-04):** the **Shadow Grid era is canonical**; the HELM anthology is **adapted into it / may be overwritten** (author decision). The thematic spine is now the [[the-doughnut-principle]]; format is **9:16 vertical Reels**. HELM-era rows (`WLD-01/02`, `MAG-01..09`, `FAC-01`, `CHR-01`, `FCT-001..008`, `VIS-01..07`) are **legacy / under adaptation** — superseded where they conflict. | ✅ done | Episode/series rewrite is the next migration step. |

---

## 11. World substrate — the Shadow Grid era (`WLD-`/`MAG-`/`PLC-`)
A second body of world lore (provided File 1), expanded as atomic pages in
[`../world/`](../world/README.md). **Status: DRAFT**, and its relationship to the HELM anthology
is open (`Q-04`). Index only — depth lives in the linked pages.

**World laws & thematic core (`WLD-`)**
| ID | Concept | Page |
|----|---------|------|
| WLD-03 | The Shadow Grid — digitized consciousness on a distributed network; brain = antenna | [[the-shadow-grid]] |
| WLD-04 | The Velocity Tiers — time-dilation hierarchy (Tier 0–3; Apex = 86,400×) | [[velocity-tiers]] |
| WLD-05 | The Cyborg Slip — real-time synthetic-replacement path to becoming digital | [[the-cyborg-slip]] |
| WLD-06 | **The Doughnut Principle** — intention in context; the Dual Arrows (thematic spine) | [[the-doughnut-principle]] |
| WLD-07 | **The Macro-Doughnut** — equilibrium / the Arrow of Balance (the maturity goal) | [[the-macro-doughnut]] |
| WLD-08 | **The Shadow Entity** — tethered consciousness (body in stasis); Tether Sickness | [[the-shadow-entity]] |
| WLD-09 | **The Ghost Entity** — purely digital, ledger-only soul; free but key-fragile | [[the-ghost-entity]] |
| WLD-10 | **"Shells with Ghosts Within"** — leased physical hosts; the caste idiom & friction | [[shells-with-ghosts-within]] |
| WLD-11 | **The Distributed President** — AI governance; law derived from real-time planetary status | [[the-distributed-president]] |
| WLD-12 | **The Post-Labor Economy** — automation safety net: hospitality baseline OR Hope cloister | [[the-post-labor-economy]] |
| WLD-13 | **The Societal Values Transformation** — the thematic skeleton: 6 value shifts (today→future), System 1→2 | [[societal-values]] |
| WLD-14 | **The Memory Substrate** — brain = lossy cache; perfect recall in-grid, forgetting out-of-grid (closes audit S-01–05) | [[the-memory-substrate]] |
| WLD-15 | **Standardized Vice Frameworks** — vices licensed/standardized by substrate; accountability over taboo | [[standardized-vices]] |
| WLD-16 | **Intimate Commerce** — licensed sex work; biosecurity + client liability; cyborg/Ghost variants | [[intimate-commerce]] |
| WLD-17 | **The Frequency Tribes** — Dunbar-150 clock-based tribes; the Proximity Illusion; caste slang | [[frequency-tribes]] |
| WLD-18 | **Parallel Pedagogy & The Merging** — multi-threaded childhood; graduation = ledger fusion; minor safeguards | [[parallel-pedagogy]] |
| WLD-19 | **Recreation & the Dreamless** — fun as decompression: Turrell Raves, Historical Parsing, the Glacial Vacation | [[recreation-culture]] |
| WLD-20 | **Cultural Taboos** — the Grid's etiquette of disgust: the Glacial Stutter, Organic Leakage, Masked Intent | [[cultural-taboos]] |
| WLD-21 | **The Substrate Olympics** — Games split by substrate physics; the Tier-Reality Paradox (mind too fast for flesh) | [[the-substrate-olympics]] |
| WLD-22 | **The Ageless Default & Substrate Dysmorphia** — in-grid appearance is a decoupled data variable; the enforced "Golden Baseline" (late-20s, flawless, ageless) for system-to-human contact, vs. raw mortal decay outside | [[the-ageless-default]] |

**Technology / mechanics (`MAG-`)**
| ID | Concept | Page |
|----|---------|------|
| MAG-10 | Inter-Tier Travel — the Data Buffer State (phase-matching clocks) | [[inter-tier-travel]] |
| MAG-11 | The Personal Blockchain — consciousness ledger; Full Disclosure; Chain-Check | [[the-personal-blockchain]] |
| MAG-12 | The Cosmic Clone Paradox — data-beaming; interstellar fork; Merge/Branch; tether risk | [[the-cosmic-clone-paradox]] |
| MAG-13 | The 1% Mutation — DNA correction (99/1); the Apex Escape Loop | [[the-1-percent-mutation]] |
| MAG-14 | The Perspective Lens — 9:16 UI grammar (Context circles / Intention squares; custom lenses) | [[the-perspective-lens-ui]] |
| MAG-15 | Progressive Digitalization — the organic→synthetic body countdown (100→70→30→0%) | [[progressive-digitalization]] |
| MAG-16 | The Absolution Protocol — Hope's indefinite sentence; the Ledger of Absolution; the wait | [[the-absolution-protocol]] |
| MAG-17 | The Medical Sanctuary — Hope's grey-line trials (99% cyborg / 1% ghost) | [[the-medical-sanctuary]] |
| MAG-18 | The Intention-in-Context Law — fluid principle-based law; merit-keyed patches; legislative chain | [[intention-in-context-law]] |
| MAG-19 | Neuro-Chemical Licensing & **Disruptive Algorithms** — Bio-Fitness License; digital drugs as exploits | [[disruptive-algorithms]] |
| MAG-20 | The **Compliance Validation Protocol** (CVP) — real-time verification; the "Proven-in-Use" defense | [[compliance-validation-protocol]] |
| MAG-21 | The **Intent-Patch Exploit** — black-market spoof of the Intention Squares; games the CVP (Vance's weapon) | [[intent-patch]] |
| MAG-22 | **Dreamless Insomnia & Tether Decay (TTD)** — no dreaming in-grid; the brain-cache countdown; Sub-Velocity Sabbaticals | [[tether-decay]] |
| MAG-23 | **Chromatic Tears** — malware as aesthetic/architectural corruption; flickers the Intention Squares, accelerates TTD | [[chromatic-tears]] |
| MAG-24 | **Velocity-Braking** — the spectacular takedown: Cognitive Shock Trap (Tier 3→0 in a microsecond) + Pastor electromagnetic staffs | [[velocity-braking]] |
| MAG-25 | **The Encrypted Block Paradox** — the sovereign-lock black box; a biological inmate the omniscient AI can neither read nor release | [[the-encrypted-block-paradox]] |
| MAG-26 | **Flavor Scripts** — digital gastronomy: taste as a software packet; the dining room morphs color to match the flavor | [[flavor-scripts]] |
| MAG-27 | **The Decoupled Environment Principle** (Asymmetric Perspective) — shared node coordinates, per-Lens sensory translation; two minds in one space inhabit different visual realities | [[asymmetric-perspective]] |

**Places (`PLC-`)**
| ID | Place | Page |
|----|-------|------|
| PLC-03 | The Lunar Dark Side servers (deep-space passive cooling) | [[the-shadow-grid-cooling]] |
| PLC-04 | The Mirror Constellation (solar power relay; misalignment → blackouts) | [[the-shadow-grid-cooling]] |
| PLC-05 | Terrestrial Redundancies (polar-ice / oceanic-trench vaults) | [[the-shadow-grid-cooling]] |
| PLC-06 | The Purist Village (Tier-0 surface; the Natural Purists' colony, Act IV) | Descent Ep 19–20 |
| PLC-07 | Alpha Centauri mining station (where the data-clone forks, Ep 15) | Descent Ep 15 |
| PLC-08 | The Ministry of Hope — physical cloisters (Earth surface) + digital sub-sectors (Grid) | Middle arc |
| PLC-09 | The Data Graveyards — frozen lunar-crater archival slums; bit-rot "Data Dementia" ghost-towns | [[data-graveyards]] |

---

## Maintenance
Add a `CHR-` block and any `FCT-` rows each time an episode is drafted; resolve `Q-01`
before drafting Ep 9. Registry wins on contradictions unless the author supersedes an entry
with a dated note. See [[writing-requirements]] `ANTH-01..06` for what is checked against this.
