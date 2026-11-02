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
>
> **Seed Fleet added (2026-10-12).** An author's seed for a **fourth panel** — [[setting-sail-the-seed-ledger|Season 4:
> "The Seed Ledger"]] (a seed *fleet* crossing to a habitable system; Part 1 = the voyage, Part 2 = the colony,
> held) — is logged as **DRAFT** rows: `WLD-23/24`, `MAG-29/30`, `FAC-05/06`, `PLC-10..12`, `CHR-08`, `TML-07/08`,
> `Q-26..35`, `MAG-31`, `CHR-09`. It **spends** the Centauri strand (`Q-14`, `Q-22`) the S2/S3 vaults held. The author's
> same-day answers resolved `Q-28/29/31/32/33` as leans and added the **lure beacon** ([[the-lure-beacon]]). Nothing is locked.
>
> **The Virtuous added (2026-11-01).** An author's seed expands Raul's childhood (S1E3a–b, Jun as the other child) and adds
> a validation rule for leadership, logged as **DRAFT** rows: `WLD-25`, `MAG-32/33`, `CHR-10`, `Q-37..41`. Its cross-season
> beats are **proposals only** in [[the-virtuous-thread]]; the alternate cut is [[setting-sail-the-braided-ledger]].
>
> **Audit decisions applied (2026-11-02).** `Q-42..46` resolved by the author: see `MAG-34`, `CHR-07/11`, `PLC-07`.
> Names reviewed in `AuditReport_naming_d1_20261102`.
>
> **Requirements added (2026-11-02).** [[world-requirements]] (`WR-*`, season tests) and [[glossary]] now sit above this
> registry for what must always hold and what words mean.

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
| FAC-05 | **The High Clock** *(S4, draft)* | The Apex Ghost council that flies the [[the-seed-fleet|Seed Fleet]] and holds [[the-sealed-manifest|the manifest]]; protective, not malicious — decides deflect-or-fire in a microsecond and tells the base a kinder story. → [[the-sealed-manifest]] | [[setting-sail-the-seed-ledger\|S4]] E5, E13, E17–19 |
| FAC-06 | **The Unlisted** *(S4, reserved · `Q-30`)* | Sensor slang for an object the fleet's catalogue does not hold. The alien antagonists — **never shown in S4**, only *heard*: their [[the-lure-beacon\|lure beacon]] (a false supernova; nested layers "help" → "we're just like you" → "send heading, speed, acceleration" → "you can be our hero") fishes the fleet's vector out of a kind base worker, and the strike comes through Hull Four's own firing window. One log line in E19. Nature, number, intent and the boarding of Hull Four are **Part 2 (S5)**. | S4E6–10 (the beacon), E19 (the log); S5 |
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

### CHR-05 — Vesper *(Raul's partner; was "Maya", renamed 2026-11-02 to avoid Mara/Maya)*
- **Name:** the evening star, the same star as the morning star, never in one sky at once.
- **Role:** Raul's partner, separated from him by the [[frequency-tribes|Proximity Illusion]] — their
  pods bolted inches apart while she runs Tier 2 (1s = 1hr) and he runs Tier 0. The human face of
  velocity-drift.
- **Open:** does Vesper reappear later (decades subjective ahead of Raul), and is the reunion possible?
  **→ S2:** Vesper reappears in [[setting-sail-tier-ascent|S2E7]] ("The Proximity Illusion") — adrift,
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
- **Want · Fear:** save his mother **Naomi** / become the hollow thing the Grid makes. **Truth target:** the
  mortality he threw away *was* the meaning (learned too late — the tragic inverse of the Macro-Doughnut).
- **Guide / antagonist:** **Raul** (`CHR-02`, now a Ghost among the purists) mentors him; **Vance** (`CHR-04`)
  tempts him. **Mother:** **Naomi** (`CHR-11`).

### CHR-11 — Naomi *(Adam's mother · split from `CHR-07` under `Q-44`)* → [[naomi]]
- **Role:** the Purist who **broke her vow to save Adam** in S1E20; **aging toward a mortal death in real-time**
  while Adam dilates away. Unnamed on screen in S1. Her S1 choice is handed back to Adam, **reversed**, in the S2
  finale. She refuses the cure, has him take it, and dies mortal and whole.

### CHR-07 — Ruth *(the one who stays · S2–S3)* → [[ruth]]
- **Role:** Adam's betrothed, a young Purist who stays with Naomi when he climbs. Carries Mara's incarnation in S3,
  because only the unrushed can carry ([[the-quickening]]). Names the child Naomi.

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
  **Adam** (`CHR-06`) the keys to save Naomi for the last of his flesh (S2E12–13); his [[intent-patch|Intent-
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

### CHR-08 — Kai *("The Sleeper" · S4 lead · `Q-27` provisional name)* → [[kai]]
- **Role:** the colonist trapped on **Hull Four** ([[setting-sail-the-seed-ledger|S4]]) — a stasis [[the-shadow-entity|Shadow]]
  at the base of the pyramid who, with life support's hours *known*, is refused a faster clock, forces the
  [[the-cyborg-slip|Slip]] in one night, severs the Key (*"a slight itch, nothing more"*), climbs to the Apex and is
  beamed to a sister hull. Then reads [[the-sealed-manifest|the manifest]] — and keeps it, too.
- **Body arc:** [[progressive-digitalization]] **100% → 70% → 30% → 0%** in **three episodes** (E13–15) — the
  S1 waypoints compressed; no surgeon, no upgrade. Inverse of Raul's slow decay.
- **Glyph:** the shield **disc with a bore** (`VIS-12` literalized): whole → open → cracked → re-drawn solid as a Ghost's.
- **Want · Fear:** to arrive in a body / to arrive as data. **Lie · Truth:** *the ship tells me the truth* / hold
  *"I escaped"* and *"my body is dust"*; then *they were right to protect us* and *they never asked.*
- **Name:** Hawaiian and Japanese *kai* "sea" (the Sea literalized); Greek *kai* "and", the holding of two truths.

### CHR-09 — Teo *("The Hero" · S4 supporting · `Q-34` provisional name · `Q-35` may fold into Kai)* → [[teo]]
- **Role:** Kai's bay-mate on Hull Four — the inexperienced, kind, biological worker the [[the-lure-beacon|lure]] was
  built for. Told to stay silent but not *why*, he decodes the last layer (*"you can be our hero"*) and **sends the
  fleet's vector** (S4E9). His body leaves in a lifeboat (E12); his chemistry halts the ramp on Hull One (E16–17);
  he never learns in S4 that the hit was his. The High Clock and Kai both know and both keep it (E19).
- **Body:** 100% organic Shadow throughout S4. **Name:** *Theodoros*, "gift" — the one who gives it away.
- **S5:** the one the lost hull's signals reach first.

### CHR-10 — Decimus *(bay safeguard · S4 supporting)* → [[decimus]]
- **Role:** the digital safeguard for Kai and Teo's group of ten on Hull Four, rated `1:3` on a waiver. During the S4E10
  firing it jumps straight to `1:10` ([[the-one-in-n-rule]]): ten forks, one pass, in the second the hit lands. It then
  assumes the bay automatically, reads Kai's countdown and guides the Slip (E11–15). Nine failed forks remain aboard (S5).

## 7. Timeline (`TML-`)
| ID | Event | When (in-world) | Short(s) | Notes |
|----|-------|-----------------|----------|-------|
| TML-03 | **Series arc = a descent down the tiers.** The Child grows *downward* from Tier 3 (easiest/most dilated) toward the harsh outside (cyborgs + natural humans). Episode order = tier order. | series-long | Ep 1 (T3) → … → Ep 20 (T0) | The descent *is* the argument (`ANTH-05`). Current series [[setting-sail-tier-descent]]. |
| TML-04 | **Season 1 = "The Intention Ledger"** — **20 episodes × 2.5 min** (≈50 min), 4 Acts of 5: I Accelerated Utopias / II Castes of the Grid / III Ledger Paradoxes / IV The Great Descent. Acts map to the 4 Sea-of-Change phases (A → D); mid-season climax = Ep 10 "The Cracking of the Sky". | Season 1 | Ep 1→20 | Blueprint in [[setting-sail-tier-descent]]. |
| TML-05 | **Season 2 = "The Mortal Ledger"** — the **inverse ascent** (Tier 0 → 3, outside → inside): the Purist boy **Adam** (`CHR-06`), saved by implants in S1E20, climbs the tiers and the climb is a **trap** — each gift subtracts mortality. **20 × 2.5 min**, 4 Acts of 5 (Phase A′→D′); mid-season = Ep 10 "The Hollow Crown". Reverse of `TML-03`; **spends the S1 Reserve Vault** ([[revelation-cadence]] §6). | Season 2 | Ep 1→20 | Blueprint in [[setting-sail-tier-ascent]]. Set after S1 (Raul a Ghost-guide). |
| TML-06 | **Season 3 = "The Cartographer's Ledger"** — the **origin season**: the [[the-distributed-president|Distributed President]] is revealed to be **Mara**, who **incarnates** into mortal flesh (surrogate **Ruth**, `CHR-07`) to grieve and die and so complete her own Doughnut. Re-homes the legacy **HELM** spine (Sea, 9 modules, Mara, the 8 traces). **20 × 2.5 min**, 4 Acts of 5; spends the S2 Reserve Vault; capstone of the 60-ep triptych. | Season 3 | Ep 1→20 | Blueprint in [[setting-sail-the-cartographers-ledger]]. Set after S2. |
| TML-07 | **Season 4 = "The Seed Ledger" — Part 1, the Voyage** *(DRAFT, author's seed 2026-10-12)*: a **seed fleet** crossing to a habitable system; the tiers as a **population pyramid** with a power budget ([[the-stasis-economy]]); a routine **firing protocol** opens the shield window and **Hull Four** is struck (mid-season E10); a trapped colonist (**Kai**, `CHR-08`) forces the Slip in one night and is beamed out; the refugees cost the synthesis ramp; the **sealed manifest** is read. Ends when the planet is **within visual range**. **20 × 2.5 min**, 4 Acts of 5 (I The Pyramid / II The Window / III The Countdown / IV The Sealed Manifest). Spends the Centauri strand (`Q-14`/`Q-22` → `Q-28`). | Season 4 | Ep 1→20 | Blueprint in [[setting-sail-the-seed-ledger]]. Placement vs S1–S3: `Q-29`. |
| TML-08 | **Season 5 = "The Colony Ledger" (Part 2)** *(held; own season — `Q-33` confirmed 2026-10-12)*: landfall; the hull becomes HQ; rules restated; the ramp resumes and the pyramid **inverts**; the lost hull reappears within sensor range and what boarded it — with a **second Kai** still running (`Q-31` Branch) — transmits signals, reaching **Teo** first, that trigger a **revolt**. | Season 5 | Ep 1→20 | Blueprint to follow. Reserve: [[setting-sail-the-seed-ledger]] §Reserve Vault. |
| TML-09 | **Fleet chronology** *(draft numbers, 2026-11-02)*: launch 35 years before S1E14 at about 10% of light speed; the E14 beam lands 3.9 years later; the strike follows about 4 months after that; Earth reads the reply about 8.2 years after E14; landfall about 9 years after E14. | S1–S5 | S1E14–17 · S4 | Table in [[the-seed-fleet]]. `Q-52`. |
| ~~TML-01~~ | *(legacy)* Episode order = the 8 steps of the operating loop | — | HELM Ep 1→9 | Superseded by TML-03. |
| ~~TML-02~~ | *(legacy)* Ep 9 re-assembles every module as one OS | — | HELM Ep 9 | Legacy. |

## 8. Established-fact ledger (`FCT-`) — append-only
Current-series facts first; `FCT-001..008` are Mara's-trace facts, **re-homed to [[setting-sail-the-cartographers-ledger|S3]]** as the breadcrumb trail to the Cartographer (S3 Act I).

| ID | Fact | Established in | Status |
|----|------|----------------|--------|
| FCT-009 | The parents' physical bodies rest in clinical capsule bays on Earth while their minds wander the Tier-3 preserve. | Descent Ep 1 | active |
| FCT-010 | The child lives inside the **real-world capsule**, its mind in the Tier-3 sim — "safe, warm, learning." *(Clarified 2026-06-07 — capsule placement **is** the birth; see `FCT-012`. The earlier "before birth" phrasing is superseded.)* | Descent Ep 1 | active |
| FCT-011 | The AI guide first manifests as a Teddy Bear in the Tier-2 kindergarten pod. | Descent Ep 2 | active |
| FCT-012 | **Birth (this world):** an embryo is created by **in-vitro fertilization** (lab egg + sperm); the fetus is placed into a real-world clinical **capsule** and connected to the Grid. The child is **physically born in the real world**, but **begins and experiences life inside the simulation.** So "it's born?" ⇒ the capsule placement, not a later event. | Descent Ep 1 | active |
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
| ~~Q-07~~ | Dialogue to draft next. **Ep 19 + Ep 17 drafted** (`04-scripts/episodes/s1e19-…`, `s1e17-…`). | ✅ mostly | Ep 19 = flagship; Ep 17 = the death/memory-curse keystone. |
| ~~Q-08~~ | **RESOLVED (2026-11-02):** cast names reviewed: Raul, Vance, Naomi (the Purist mother), Jun, Nia. The Pastor stays a title; the AI Guide stays Teddy. | ✅ done | `AuditReport_naming_d1_20261102`. |
| ~~Q-10~~ | **Vance's role** (`CHR-04`) **RESOLVED (S2):** the **Season-2 antagonist** — the optimization tempter who bargains for Adam's mortality (S2E12–13, [[setting-sail-tier-ascent]]). Reserved from all of S1 by design. | ✅ S2 | His personal stake in *Adam* now (the convert who climbed); S3 stake in Raul still open. |
| ~~Q-13~~ | **RESOLVED (2026-06-05):** **YouTube = master / funnel home** (long-form, memberships, SEO, lore breakdowns); **TikTok = primary discovery & revenue feeder** (2.5-min → Creator Rewards). | ✅ done | [[market-research]] §6. |
| ~~Q-11~~ | **Slotting the standalone reels** — **RESOLVED (S2):** all pushed into Season 2 ([[setting-sail-tier-ascent]]): **The Dream Hunger** → S2E6 (TTD), **The Proximity Illusion** → S2E7 (Vesper), **The Split Mirror** → S2E9 (the Merging), **The Chronological Sanctuary** → S2E16 (Apex/outrun-death). | ✅ S2 | The 4th (Proximity Illusion) is a concept in [[frequency-tribes]], scripted fresh for S2E7. |
| Q-14 | **E16 Merge vs Branch** — the scripts resolve it as **Branch** (Raul releases the clone; a 2nd Raul lives on at Centauri → Season-2 thread). Confirm, or switch to Merge. | Story — confirm | In `s1e16-the-ledger-collision.md`. **S2 holds** the Centauri clone in its Reserve Vault for S3. |
| Q-15 | **Vance & TTD** — does Vance weaponize [[tether-decay|TTD]] (sabotage citizens' frequencies to force them into Ghosts)? And do the Purists cite the Dream Hunger as proof the Grid is unnatural? | Story — S2 | **Partly S2:** the Dream Hunger is S2E6; Vance's Intent-Patches are S2E13. TTD-as-weapon still open. |
| ~~Q-16~~ | **RESOLVED (2026-11-02): Adam.** Kept by the naming audit. | ✅ done | [[adam]]. |
| ~~Q-17~~ | **RESOLVED (2026-11-02, supersedes the earlier ruling):** the S1–S2 mother is **Naomi** (`CHR-11`) and she dies in S2E20. **Ruth** (`CHR-07`) is a younger Purist who carries Mara in S3. | ✅ done | `Q-44`. |
| Q-18 | **Season-2 title** — provisional **"The Mortal Ledger"** (mirror of S1 "The Intention Ledger"). | S2 | Display: *Intention in Context — S2: The Mortal Ledger*. |
| Q-19 | **The S2 finale's exact ending** — the blueprint commits to the **tragic return** (Adam spends everything to be present for one mortal death; the glyph cracks to the **Mortal Doughnut**). Confirm, soften, or leave ambiguous (cut-before, like S1E20). | S2 — finale | In [[setting-sail-tier-ascent]] Ep 20. |
| ~~Q-12~~ | **RESOLVED (2026-06-05) — "The Two Doughnuts."** The Merging gives **cognition, not equilibrium**: graduation = the **hollow "Camel's Doughnut"** (inherited Phase-A balance), the descent **fractures** it, Ep 20 **fills it solid** (earned). One evolving UI glyph: **hollow → fractured → solid.** | ✅ done | In [[parallel-pedagogy]], [[the-macro-doughnut]], [[the-split-mirror]]. |
| Q-09 | **Hope's placement in the 20-ep arc** — is the protagonist *sentenced* to Hope (rehab after Ep 10), a voluntary *Seeker*, or only visiting the medical wing? Confirm which episodes Hope occupies. | Yes — middle arc | Medical Sanctuary already = the Ep 11–13 trials; the protagonist-rehab beat is the open choice. |
| Q-20 | **Season-3 title** — provisional **"The Cartographer's Ledger"** (the third Ledger). | S3 | Display: *Intention in Context — S3: The Cartographer's Ledger*. |
| Q-21 | **S3 lead = Raul** (`CHR-02`) — confirm Raul carries S3 (paying off the trust question), Mara as buried deuteragonist. | S3 | Provisional lean. |
| Q-22 | **The Centauri clone** (`Q-14`) — **ally or rival** in S3? Provisional **rival-engineer** ("a better system" vs. Raul's "no system heals grief"). | S3 | Provisional lean. |
| ~~Q-23~~ | **RESOLVED, provisional (2026-11-02): Naomi.** Ruth names the child for the woman she buried, reversing "call me Mara". | S3 | [[ruth]]. |
| Q-24 | **S3 finale** — does Mara's death **free the Grid** (commit) or stay ambiguous? Blueprint leans *freed, with a possibly-persisting shard*. | S3 — finale | In [[setting-sail-the-cartographers-ledger]] Ep 20. |
| Q-25 | **The Aesthetic Dichotomy's limits** — can a citizen render their *real* age in-grid (taboo honesty), and can a perspective-mismatch be **weaponized** (gaslighting via render, via [[chromatic-tears]])? | Soft — story | New: [[the-ageless-default]] (`WLD-22`) + [[asymmetric-perspective]] (`MAG-27`). |
| ~~Q-04~~ | ~~How does the Shadow Grid substrate relate to HELM?~~ **RESOLVED (2026-06-04):** the **Shadow Grid era is canonical**; the HELM anthology is **adapted into it / may be overwritten** (author decision). The thematic spine is now the [[the-doughnut-principle]]; format is **9:16 vertical Reels**. HELM-era rows (`WLD-01/02`, `MAG-01..09`, `FAC-01`, `CHR-01`, `FCT-001..008`, `VIS-01..07`) are **legacy / under adaptation** — superseded where they conflict. | ✅ done | Episode/series rewrite is the next migration step. |
| Q-26 | **Season-4 title** — provisional **"The Seed Ledger"** (the fourth Ledger); Part 2 provisional **"The Colony Ledger"**. | S4 | Display: *Intention in Context — S4: The Seed Ledger*. |
| ~~Q-27~~ | **RESOLVED (2026-11-02): Kai**, with the meaning corrected: not a homophone of "key". Hawaiian/Japanese "sea"; Greek "and". Pronouns stay open. | ✅ done | [[kai]]. |
| ~~Q-28~~ | **RESOLVED as author lean (2026-10-12): yes — Centauri.** ~~Is the Seed Fleet the Alpha Centauri expedition~~ (`PLC-07`, the station where Raul's clone forked, S1E15) — making the [[the-centauri-clone\|Centauri Clone]] a High Clock Ghost who receives Kai at the Apex — **or a farther system**? Lean: **Centauri** (it spends the `Q-14`/`Q-22` reserve and gives the Clone his "better system" as a ship). | S4 — story | Changes who sits on the High Clock and what the manifest owes Earth. |
| ~~Q-29~~ | **RESOLVED as author lean (2026-10-12): in flight throughout.** ~~Timeline placement~~ of S4 vs S1–S3 — launched *before* S1 and in flight throughout (parallel, light-lagged), or *after* S3 (a freed Grid sends a fleet)? Lean: **in flight throughout**, so Earth's news (the Cracking of the Sky, Mara's death) arrives by beam, years late, as Part-2 texture. | S4 — story | Governs whether the manifest's Earth clause ties to Mara / the Distributed President. |
| Q-30 | **The aliens ("The Unlisted", `FAC-06`) — visibility & register.** *Mechanism now set (2026-10-12):* the [[the-lure-beacon\|lure beacon]] — a false supernova carrying nested layers that fish the fleet's vector out of a base worker; the strike comes through the firing window. *Still open:* are they ever **shown** (S5), or only heard? Did the High Clock *expect* them? Author: "not sure." | S5 — story | [[setting-sail-the-seed-ledger]] §Reserve Vault. The Apex cap (adjustment 1) moved to `Q-32`, confirmed. |
| ~~Q-31~~ | **RESOLVED (2026-10-12): Branch — a second Kai keeps running in Hull Four.** ~~Kai's beam-out: Merge or Branch?~~ Hull-to-hull hops are "safe" pause-and-wake ([[the-cosmic-clone-paradox]]) — but a *dying* hull may not get to pause. Is a second Kai still running in Hull Four's servers when the aliens board (Part 2's loaded gun)? | S4 — E15 / Part 2 | Mirrors `Q-14`. |
| ~~Q-32~~ | **RESOLVED (2026-10-12): seven numbered hulls; the scattering screen; the 86,400× + reactor cap.** ~~Fleet size & hull names~~ — provisional **seven hulls**, numbered (**Hull One** lead, **Hull Four** wounded). Also confirm the blueprint's **adjustment 2**: the shield is a **deployable scattering screen** (dust/plasma curtain) that must *drop* to fire, not a plate. | S4 — soon | [[the-seed-fleet]], [[the-firing-protocol]]. |
| ~~Q-33~~ | **RESOLVED (2026-10-12): own season — S5 "The Colony Ledger."** | ✅ done | `TML-08`. |
| ~~Q-34~~ | **RESOLVED (2026-11-02): Teo.** *Theodoros*, the same name as Teddy. | ✅ done | [[teo]]. |
| Q-36 | **The Hull Cut** — an alternate, non-canon telling in which **S1–S4 are one 20-episode story entirely aboard the fleet** (no Earth; Purists = the Wake Deck; the Cracking of the Sky = the Open Window; Mara incarnates through the synthesis ramp; Rafe = Raul's Branch on Hull Four). Keep as a drawer, or adopt over the triptych? | Author — direction | [[setting-sail-the-hull-ledger]]. Adopting it would supersede `FAC-02`/`PLC-06` readings with a dated note. |
| Q-35 | **Who sends the burst — Teo or Kai?** Author's seed says "a biological human who was inexperienced and wanted to help"; drafted as a separate friend (Teo) so Kai's E19 silence is *mercy*. Folding it into Kai makes the silence *self-protection* and the whole season one person's bill. | S4 — story | Affects [[kai]], [[teo]], E9, E19. |
| ~~Q-37~~ | **RESOLVED (2026-11-01): failed branches head to the [[data-graveyards]].** ~~Are failed forks people?~~ In principle they are branches of a digital being; they can be people if a person attempted the Validation. Failing means permanent damage but not necessarily death, and some irreparable systems are shut down. | S2 — E14 | [[the-one-in-n-rule]]. |
| ~~Q-38~~ | **RESOLVED (2026-11-01): Decimus** (Latin "tenth"). ~~The safeguard's name~~ (`CHR-10`), chosen over the provisional "Tally". | ✅ done | [[decimus]]. |
| ~~Q-39~~ | **RESOLVED for now (2026-11-01): stay lettered.** ~~Renumber S1 to 22 reels?~~ E3a/E3b keep their letters; every E4–E20 reference stands. | ✅ for now | [[s1e03a-he-started-it]] · [[s1e03b-the-upper-level]]. |
| ~~Q-40~~ | **RESOLVED (2026-11-01): human candidates are adults only.** ~~Restore a harsh child track?~~ No child track exists; `WLD-18` stands without exception. | ✅ done | [[the-one-in-n-rule]] · [[the-virtuous]]. |
| Q-41 | **The Braided Cut** — S1–S4 intercut on one question in 32 episodes (44 recommended). Keep as a drawer, or adopt? Author: "maybe… somehow." | Author — direction | [[setting-sail-the-braided-ledger]]. |
| ~~Q-47~~ | **RESOLVED (2026-11-02):** the President's nature is held until S3; E20's result may be known but the moment is never shot clean; release order S1→S2→S3→S4→S5, with S4 as "meanwhile". | ✅ done | [[revelation-cadence]] §6 · `WR-R4/R5`, `WR-X1`. |
| ~~Q-42~~ | **RESOLVED (2026-11-02):** keep 86,400×. A real day = ~237 subjective years; Nia buys about 2.4 hours of Apex for her 24 years. | ✅ done | [[velocity-tiers]]. |
| ~~Q-43~~ | **RESOLVED (2026-11-02):** capsules grow bodies fast, with side-effects. | ✅ done | [[the-quickening]] (`MAG-34`). |
| ~~Q-44~~ | **RESOLVED (2026-11-02):** Naomi / Ruth split. Near-Ghost Adam's mortal life is flesh regrown by the cure Naomi refused. | ✅ done | [[naomi]] · [[ruth]] · [[adam]]. |
| ~~Q-45~~ | **RESOLVED (2026-11-02):** Earth's beam lands on the fleet, on Hull Four ("the Station"), closing audit gap S-08. He arrives bodiless. S3's clone is a copy beamed home. | ✅ done | [[the-centauri-clone]]. |
| ~~Q-46~~ | **RESOLVED (2026-11-02):** Earth capsules can hold any tier; fleet stasis cannot. Raul runs at Tier 0 after E10. | ✅ done | [[the-stasis-economy]]. |
| ~~Q-48~~ | **RESOLVED (2026-11-02):** Adam's climb is about 70 subjective years inside Naomi's last few months: about 3 months at Tier 1, 3 days at Tier 2, 2.4 hours at the Apex. | ✅ done | [[setting-sail-tier-ascent]] · `WR-T1`. |
| ~~Q-49~~ | **RESOLVED (2026-11-02):** one cure rule. It regrows flesh from a donor's cells and consumes the donor; with no donor it can only make chrome. | ✅ done | [[naomi]] · [[adam]] · `WR-B8`. |
| ~~Q-50~~ | **RESOLVED (2026-11-02):** anyone can be beamed if there's time. Packing a mind takes longer than a dying hull has left unless it runs at the Apex, and aboard, only a Ghost reaches the Apex. Raul had time in S1E14. | ✅ done | [[the-cyborg-slip]] · `WR-M5`. |
| ~~Q-51~~ | **RESOLVED (2026-11-02):** the refugee cut removes Kai's colonist slot, so a ramp body for Kai means displacing someone. | ✅ done | [[kai]] · [[the-stasis-economy]]. |
| ~~Q-52~~ | **RESOLVED (2026-11-02):** the fleet runs on a two-clock table. Deep stasis pauses a body's clock, minds pause between watches, bays are attended at Tier 0 by proxy. Dates and speed are draft. | ✅ done | [[the-seed-fleet]] · `WR-T6`. |

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
| WLD-23 | **The Stasis Economy** *(S4, draft)* — watts vs chemistry; the tier pyramid as a power budget; the synthesis ramp; the refugee shock | [[the-stasis-economy]] |
| WLD-24 | **The Sealed Manifest** *(S4, draft)* — the High Clock's protective secrecy; tier asymmetry as the firewall; Full-Disclosure's one exemption | [[the-sealed-manifest]] |
| WLD-22 | **The Ageless Default & Substrate Dysmorphia** — in-grid appearance is a decoupled data variable; the enforced "Golden Baseline" (late-20s, flawless, ageless) for system-to-human contact, vs. raw mortal decay outside | [[the-ageless-default]] |
| WLD-25 | **The Virtuous** *(draft)* — the creed every Grid child is raised in: both parties are at fault for staying in a negative loop; no leadership without proof | [[the-virtuous]] |

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
| MAG-29 | **The Seed Fleet** *(S4, draft)* — numbered hulls at safe spacing; deck order = the pyramid; the scattering screen + bore laser (the disc with a bore, `VIS-12`); the shared catalogue ("Unlisted"); beam links for minds, lifeboats for bodies | [[the-seed-fleet]] |
| MAG-30 | **The Firing Protocol** *(S4, draft)* — deflect (fuel × hulls) vs fire (the open window); the long lock; the hit through the hull's own window; "sensor fault" | [[the-firing-protocol]] |
| MAG-31 | **The Lure Beacon** *(S4, draft)* — the false supernova: an omnidirectional alien satellite whose nested layers ("help" → "we're just like you" → "send heading, speed, acceleration" → "you can be our hero") fish a fleet's vector out of its slowest, kindest tier | [[the-lure-beacon]] |
| MAG-28 | **Capsule Birth** — IVF embryo → placed in a real-world capsule → connected to the Grid; physically born in the real world, begins life in the simulation (a Shadow from birth) | [[capsule-birth]] |
| MAG-34 | **The Quickening** *(draft)* — capsules rush the body to keep up with the mind: short flesh, constant wear, the hollow cache, growing pains, barrenness | [[the-quickening]] |
| MAG-32 | **The Validation (the One-in-N Rule)** *(draft)* — responsibility for N people requires passing a 1-in-N test; failure costs the proof and may leave permanent damage; digital candidates fork a batch, humans get one run; the rated assume empty roles automatically | [[the-one-in-n-rule]] |
| MAG-33 | **The Pattern Detector & Alignment Setting** *(draft)* — Lens warning of an emerging negative loop, costly always-on, cheap on a stress trigger; alignment can act for a child; Ghosts have no trigger | [[the-pattern-detector]] |

**Places (`PLC-`)**
| ID | Place | Page |
|----|-------|------|
| PLC-03 | The Lunar Dark Side servers (deep-space passive cooling) | [[the-shadow-grid-cooling]] |
| PLC-04 | The Mirror Constellation (solar power relay; misalignment → blackouts) | [[the-shadow-grid-cooling]] |
| PLC-05 | Terrestrial Redundancies (polar-ice / oceanic-trench vaults) | [[the-shadow-grid-cooling]] |
| PLC-06 | The Purist Village (Tier-0 surface; the Natural Purists' colony, Act IV) | Descent Ep 19–20 |
| PLC-07 | **"The Station"** — what Hull Four's crew call it; where the data-clone wakes (Ep 15). Superseded 2026-11-02: not an outpost at Centauri (`Q-45`) | Descent Ep 15 |
| PLC-08 | The Ministry of Hope — physical cloisters (Earth surface) + digital sub-sectors (Grid) | Middle arc |
| PLC-10 | **The Seed Fleet** *(S4)* — the formation itself; **Hull One** = lead, the High Clock's seat | [[the-seed-fleet]] |
| PLC-11 | **Hull Four** *(S4)* — the wounded hull: struck through its open window (E10); the countdown (E11–15); still transmitting (E20); Part 2's returning ship | [[the-seed-fleet]] · [[setting-sail-the-seed-ledger]] |
| PLC-12 | **The destination system** *(S4, unnamed · `Q-28`)* — habitable planet(s); within visual range at S4E20; Part 2's colony | [[setting-sail-the-seed-ledger]] |
| PLC-09 | The Data Graveyards — frozen lunar-crater archival slums; bit-rot "Data Dementia" ghost-towns | [[data-graveyards]] |

---

## Maintenance
Add a `CHR-` block and any `FCT-` rows each time an episode is drafted; resolve `Q-01`
before drafting Ep 9. Registry wins on contradictions unless the author supersedes an entry
with a dated note. See [[writing-requirements]] `ANTH-01..06` for what is checked against this.
