# Writing Requirements — Auditable Spec for Fantasy Shorts

> The verifiable, scoreable contract a script is audited against. Every requirement is
> derived from [`fantasy-writing.md`](./fantasy-writing.md) (cited as **§N**) and is either
> a **GATE** (binary MUST — pass/fail) or a **SCORED** criterion (1–5 SHOULD — the quality
> dial that should *rise* draft over draft). The companion runner is
> [`../prompts/audit-script.md`](../prompts/audit-script.md); consistency over time is
> enforced against [`canon-registry.md`](./canon-registry.md). Target unit: **one short**
> (a single story/reel) or the **whole anthology** (global, cross-short).

---

## How to use this

- **Gates are non-negotiable.** Every applicable GATE must be `PASS` for a draft to "pass
  the gate set." Any `FAIL` is a finding (severity P0–P1, see the runner).
- **Scores show improvement.** Each SCORED item is rated **1–5** against its rubric anchors,
  re-scored every draft, and **logged** (see *Scorecard* below) so you can watch a piece get
  stronger (e.g. CHAR rollup 2 → 4 across drafts). They are *quality*, not pass/fail.
- **Rollups.** A *layer score* = mean of that layer's scored items. *Overall* = mean of the
  layer rollups. Track both per draft; falling scores flag regressions.
- **Every finding cites an ID** (e.g. `WORLD-03`) and **evidence** (scene / line) so it is
  re-checkable. A requirement with no clear way to verify it does not belong here.

### Field conventions
Each requirement row carries: **ID** · **Type** (`G` gate, `S` scored 1–5) · the
**requirement + how to verify** · **§** the guide source. Scored rows include rubric anchors
(`1 / 3 / 5`). **Applies-to** is implied by the layer (per-short, per-character, per-scene,
or anthology-global) and noted where it differs.

### Status vocabulary (used in audit output)
`PASS` · `FAIL` · `N/A` (gates) — `1`–`5` · `N/A` (scored) — each with `evidence:` and, if
failing/low, a `finding:` id.

---

## Layer STORY — the piece as a whole *(per short, per draft)*

| ID | T | Requirement & how to verify | § |
|----|---|------------------------------|---|
| STORY-01 | G | **One controlling theme** is identifiable and nameable in a single phrase. *Verify:* state it; if you need "and", it's two themes — fail. | §4, §30 |
| STORY-02 | G | The theme is **dramatized, never stated** as a lesson in narration/dialogue. *Verify:* find any line that explains the moral → fail. | §16, §20 |
| STORY-03 | G | **Essential formula present:** wounded character · deep desire · consistent rules · theme-bearing conflict. *Verify:* name each of the four. | thesis, §5 |
| STORY-04 | G | A **central dramatic question** is posed early and answered (or pointedly refused) by the end. *Verify:* quote the question + the ending's response. | §6, §30 |
| STORY-05 | G | **Structure present:** opening disequilibrium → escalating complications → transformation. *Verify:* locate all three. | §18 |
| STORY-06 | G | **Stakes are explicit** — what is lost on failure is clear. *Verify:* state the cost of failure. | §5, §35 |
| STORY-07 | S | The **ending resolves the THEME**, not merely the plot. *1:* plot only / *3:* thematic gesture / *5:* plot and theme land as one. | §18, §30 |
| STORY-08 | S | **Form fits the cargo** (a short carries one idea/turn, not a crammed novel). *1:* novel stuffed into a short / *3:* fits / *5:* the form amplifies the idea. | §19 |

## Layer CHAR — each major character *(per character, per draft)*

| ID | T | Requirement & how to verify | § |
|----|---|------------------------------|---|
| CHAR-01 | G | Has a concrete external **WANT** in this piece. *Verify:* state the goal. | §5, §7 |
| CHAR-02 | G | Has a **FEAR / obstacle** that opposes the want. *Verify:* name it. | §7, §10 |
| CHAR-03 | G | Has a named **Ghost, Lie, and Truth**. *Verify:* the past wound; the false belief; the truth reached or refused. | §8 |
| CHAR-04 | G | Is **active** — drives ≥1 plot turn by choice, not only reaction. *Verify:* point to a decision that changes the story. | §7 |
| CHAR-05 | S | **Arc dramatized** (the Lie is tested across the piece); arc type stated (positive/flat/negative). *1:* no arc / *3:* stated not tested / *5:* tested at every beat. | §8 |
| CHAR-06 | S | **Egri dimensions coherent** — physiology, sociology, psychology consistent and motivating. *1:* a name only / *3:* sketched / *5:* the three explain the behavior. | §7 |
| CHAR-07 | S | **Relatable** — motive is understandable regardless of likability. *1:* opaque / *3:* legible / *5:* we feel the want from the inside. | §7 |
| CHAR-08 | G | *(Antagonist)* Embodies a **credible alternative worldview** ("what if the protagonist is wrong?"), not just an obstacle. *Verify:* state the antagonist's argument. | §9 |

## Layer WORLD — world & magic *(per short; cross-checked against the canon registry)*

| ID | T | Requirement & how to verify | § |
|----|---|------------------------------|---|
| WORLD-01 | G | Every named magic/tech effect has a stated or **established cost**. *Verify:* list effects; each maps to a cost. | §13, §24 |
| WORLD-02 | G | Magic/tech has explicit **limits** (what it *can't* do). *Verify:* name a limit. | §12, §13 |
| WORLD-03 | G | Rules are **consistent** within the piece **and** with `canon-registry.md`. *Verify:* cross-check each rule use vs `MAG-*`. | §13 |
| WORLD-04 | G | Reader-facing **problem-solving magic is understood before it resolves conflict** (no deus ex machina). *Verify:* the rule that fixes the climax was set up earlier. | §12 |
| WORLD-05 | G | **No info-dump** — world is revealed via action/sensory detail/conflict, not lore blocks. *Verify:* flag any expository block that halts the story. | §14 |
| WORLD-06 | S | Society/economy/institutions **reflect the magic systemically** (warfare, trade, law, religion, medicine). *1:* costume world / *3:* some ripple / *5:* institutions built *by* the magic. | §24, §25 |
| WORLD-07 | S | **Depth over scale** — shown detail is lived-in, not encyclopedic breadth. *1:* atlas dump / *3:* adequate / *5:* one place feels fully real. | §11 |
| WORLD-08 | S | **Geography/culture logic** supports the conflict. *1:* arbitrary / *3:* plausible / *5:* terrain & culture drive the plot. | §11, §25 |

## Layer THEME — theme & symbol *(per short; some anthology-global)*

| ID | T | Requirement & how to verify | § |
|----|---|------------------------------|---|
| THEME-01 | G | The central **monster/antagonist/conflict carries a clear metaphoric meaning**. *Verify:* state what it represents. | §9 |
| THEME-02 | G | **No over-explaining** of symbols/rules; gaps are left for the reader. *Verify:* flag any passage that decodes its own symbolism. | §20 |
| THEME-03 | S | Theme is **architecture** — it touches plot, world, magic, imagery, arc, and ending (one system). *1:* decoration / *3:* present in plot only / *5:* every layer points at it. | §30 |
| THEME-04 | S | **Central images are deliberate** and rhyme with the theme. *1:* random / *3:* some motif / *5:* a controlling image recurs and means something. | §28 |

## Layer SCENE — recurring checks *(applied to every scene/beat)*

| ID | T | Requirement & how to verify | § |
|----|---|------------------------------|---|
| SCENE-01 | G | The scene **changes something** (info / relationship / power / stakes / understanding / character). *Verify:* name the change; none → cut or rewrite. | §29 |
| SCENE-02 | G | The scene contains **conflict** — someone wants, meets resistance. *Verify:* state the want and the resistance. | §5, §14 |
| SCENE-03 | G | **POV is held** — only what the POV character can know is narrated (no head-hop). *Verify:* flag any line outside the POV. | §31 |
| SCENE-04 | G | **Action has consequence**, not spectacle. *Verify:* each action beat changes the situation. | §5, §29 |
| SCENE-05 | S | **Dialogue creates tension** (want / power / secret under it), not info-transfer. *1:* exposition / *3:* characterized / *5:* subtext-driven. | §10 |
| SCENE-06 | S | **Show/tell balance** — emotional beats shown, connective tissue summarized. *1:* told throughout / *3:* mixed / *5:* deliberate, rhythmic. | §16, §17 |
| SCENE-07 | S | *(middle scenes)* **Pressure escalates** vs the prior scene. *1:* flat/wandering / *3:* maintained / *5:* each beat raises cost. | §29 |

## Layer PAGE — page-level craft *(per short)*

| ID | T | Requirement & how to verify | § |
|----|---|------------------------------|---|
| PAGE-01 | G | The **first line/page creates curiosity, tension, or intrigue** and opens in want/trouble (not weather/backstory). *Verify:* read the opening cold. | §32 |
| PAGE-02 | S | **POV chosen deliberately** (whose eyes / how close) and suited to the story. *1:* accidental / *3:* consistent / *5:* POV *is* the story's lens. | §31 |
| PAGE-03 | S | **Atmosphere via selection, rhythm, silence** — not over-description. *1:* flat or overstuffed / *3:* present / *5:* evocative restraint. | §17 |
| PAGE-04 | S | **Prose clean at the line** — no filler, thoughtless cliché, or redundancy. *1:* noisy / *3:* serviceable / *5:* every line earns its place. | §21, §26 |

## Layer CINE — sci-fi cinematography *(per short's visual plan / shotlist / scene directions; some anthology-global)*

Derived from [[scifi-cinematography]] (cited **cine §N**). Audits the **visual intent** —
shot choices, palette, light, motion, framing, wonder — as specified in the script's scene
descriptions or a shotlist/storyboard. `CINE-01` and `CINE-06` are also checked anthology-wide
against the `VIS-*` block of [[canon-registry]]. **Composition is judged in the series' 9:16
vertical grammar** (UI-safe zones, vertical lead-room, top↔bottom stacking) — see [[vertical-grammar]].

| ID | T | Requirement & how to verify | cine § |
|----|---|------------------------------|--------|
| CINE-01 | G | The world's **defined look** (tech level, conditions, human↔tech relationship) is established before spectacle and is **internally consistent** with `VIS-*`. *Verify:* visual choices conform to the registry; none bend for convenience. | §1 |
| CINE-02 | G | Each major visual choice (**composition / color / light / motion**) is justified by the short's **central question/theme**. *Verify:* name the question; map ≥1 visual choice to it. | §2 |
| CINE-03 | G | Every scene carries **human emotional truth OR worldbuilding info** (ideally both). *Verify:* per scene, name which it delivers. | §3 |
| CINE-04 | G | Every prop/interface is **functional** (why here / what problem / who uses / limits) and agrees with `MAG-*`; no "cool-only" tech. *Verify:* pick the key device; answer the four. | §12 |
| CINE-05 | G | At least one earned **wonder beat** — the audience pauses to *look* (not action/dialogue). *Verify:* locate it; confirm it's set up. | §15 |
| CINE-06 | G | Color follows the anthology's **established palette canon** — the `VIS-09` emotional color-vectors and `VIS-15` chromatic-expressionism templates (the HELM-era 60-30-10 of `VIS-01` is **legacy**, superseded per `Q-04`) — and is intentional, **directing attention** to the focal point. *Verify:* name the scene's register (feel-bad / feel-good / equilibrium, or its `VIS-15` master-palette) and the attention anchor; ad-hoc color matching no `VIS-*` row → fail. | §6 |
| CINE-07 | G | Signature images carry **emotional truth**, not just spectacle. *Verify:* name the feeling each key image delivers; a spectacle-only image is a fail. | §16 |
| CINE-08 | S | **Scale hierarchy** used intentionally (shot sizes ordered world↔character, no random jumps). *1:* arbitrary / *3:* mostly motivated / *5:* scale moves are an argument. | §4 |
| CINE-09 | S | **Composition grammar** deliberate — symmetry/centered = order/control, asymmetry = chaos/decay; **negative space** (lead/looking room, balance, smallness-in-the-void) used with intent, not by default ([[negative-space]]). *1:* accidental / *3:* consistent / *5:* framing & empty space state the meaning. | §5 |
| CINE-10 | S | **Light is motivated** — appears to come from the world (panels, holograms, glow), not obvious movie lights; contrast/negative-fill/underlight used with intent ([[lighting]]). *1:* stagey / *3:* mostly diegetic / *5:* "the room lights itself". | §7 |
| CINE-11 | S | **Human↔machine visual contrast** (warm/soft/organic vs cool/sharp/geometric) used where thematically apt. *1:* none / *3:* present / *5:* the contrast carries the theme. | §8 |
| CINE-12 | S | **Atmosphere/volume** (haze, particles + backlight for volumetric beams, [[lighting]] §4) gives light, depth, scale where useful. *1:* flat / *3:* some / *5:* light made visible and meaningful. | §9 |
| CINE-13 | S | **Camera motion expresses the world's state** (stable=dolly/crane; collapse=handheld; AI=mathematically smooth) per `VIS-04`, and is **motivated** — never moves for style alone ([[cinematography-techniques]]). *1:* unmotivated / *3:* consistent / *5:* motion is characterization. | §10 |
| CINE-14 | S | **Deep focus / layered frames** invite discovery ("more world beyond"). *1:* flat staging / *3:* some depth / *5:* the frame rewards inspection. | §11 |
| CINE-15 | S | **VFX restraint** — few convincing effects over many mediocre; spectacle stays affordable/believable. *1:* CGI overload / *3:* controlled / *5:* one effect does the work of fifty. | §13 |
| CINE-16 | S | **Texture is deliberate** (clean/sharp vs grain/decay) and matches the subgenre, not a default filter. *1:* reflexive grain / *3:* intentional / *5:* texture is a thesis. | §14 |

## Layer ANTH — anthology consistency *(global; cross-short, run against the canon registry)*

| ID | T | Requirement & how to verify | § |
|----|---|------------------------------|---|
| ANTH-01 | G | **World facts match the canon registry** across all shorts (no contradictions). *Verify:* every world claim ↔ `WLD-*`/`MAG-*`/`PLC-*`. | §13 |
| ANTH-02 | G | **Recurring characters are continuous** (traits, voice, status, knowledge) vs the character bible. *Verify:* each appearance ↔ `CHR-*`. | §13, registry |
| ANTH-03 | G | **Timeline/chronology consistent** across shorts vs the canon timeline. *Verify:* order events ↔ `TML-*`. | registry |
| ANTH-04 | G | Each short is **self-contained** (delivers one idea cold) **yet contributes to the arc**. *Verify:* can a newcomer follow it? does it advance the throughline? | series |
| ANTH-05 | S | The **throughline compounds** — ordering is meaningful; later shorts build on earlier. *1:* unrelated set / *3:* loose links / *5:* the order is the argument. | series |
| ANTH-06 | S | **Tone & visual throughline consistent** across shorts (register, recurring motif). *1:* drifting / *3:* mostly steady / *5:* a signature runs through all. | series |

## Layer REVEAL — revelation cadence *(per episode in sequence; some season-global)*

Derived from [[revelation-cadence]] (cited **rc §N**). Audits **information rationing** — the rate and
route of disclosure across the arc, the layer the per-scene `WORLD-05`/`THEME-02` gates can't see. Runs as
perspective **P9** in [[audit-script]] on a season pass (`TARGET=ANTHOLOGY`) or a single episode read *in
sequence*; skip with a note for a context-free standalone.

| ID | T | Requirement & how to verify | rc § |
|----|---|------------------------------|------|
| REVEAL-01 | G | **Per-episode reveal budget:** introduces **≤1 major** new world-concept (+ ≤2 minor); mid/late eps spend more on payoff than setup. *Verify:* list newly-revealed concepts; >1 major (and not *the* reveal episode) → finding. | §4 |
| REVEAL-02 | G | **No premature payoff / spoiler:** a later episode's turn isn't resolved early; a plant raises a question the audience *can't yet answer*. *Verify:* each plant pays off *later*, not in-scene; no scene lets the viewer complete a future turn. | §5 |
| REVEAL-03 | G | **Reveal via a valve, never a lecture:** every world-fact reaches the audience through diegetic UI / lived experience / a wonder beat / idiom (extends `WORLD-05`/`THEME-02` across the arc). *Verify:* name the valve per reveal; an expository gloss → fail. | §3 |
| REVEAL-04 | G | **Reserve Vault respected:** no script reveals or explains a concept the season marks **HELD**. *Verify:* cross-check each new concept against the [[revelation-cadence]] §6 vault. | §1, §6 |
| REVEAL-05 | S | **Drip balance across the season** — the Ledger reads as a steady column, no act front-loaded or starved. *1:* lumped/dumped / *3:* uneven / *5:* steady, compounding drip with payoffs where guns were planted. | §7 |
| REVEAL-06 | S | **Mystery economy** — enough withheld that the world feels larger than it shows; permanent mysteries protected. *1:* over-explained / *3:* some reserve / *5:* the unseen mass is *felt* (the "larger machine"). | §1, §6 |

## Layer PROCESS — author hygiene *(tracked, not script-audited)*

Not scored against the text; checked at the project level. `PROC-01` a **story bible /
[`canon-registry.md`](./canon-registry.md) is maintained** and updated as facts are
established (§33). `PROC-02` drafts advance under the **one-mission-per-pass** discipline and
the rule that **finished beats perfect** (§21, §35). The §36 **priority hierarchy** is the
tiebreaker when requirements conflict: characters > worldbuilding, conflict > lore, next
draft > perfect plan.

---

## Scorecard (per short, per draft)

Copy this block into the audit report / the short's working notes and fill it each draft.

```
SHORT: <title>            DRAFT: <n>            DATE: <YYYY-MM-DD>
GATES:  <passed>/<applicable>   (list any FAIL ids)
SCORES (1–5 rollups):
  STORY __  CHAR __  WORLD __  THEME __  SCENE __  PAGE __  CINE __  ANTH __  REVEAL __
  OVERALL __
TOP FINDINGS: <P0/P1 ids>          CANON UPDATES: <new FCT-/CHR- ids>
```

### Draft history (trend — this is the "show improvement" view)

| Draft | Date | Gates | STORY | CHAR | WORLD | THEME | SCENE | PAGE | CINE | ANTH | REVEAL | Overall | Note |
|-------|------|-------|-------|------|-------|-------|-------|------|------|------|--------|---------|------|
| 1 | | /n | | | | | | | | | | | first pass |
| 2 | | /n | | | | | | | | | | | |
| 3 | | /n | | | | | | | | | | | |

A healthy trend: **gates trend to full**, scored rollups **rise**, and no layer regresses
between drafts without a noted reason.

---

## Related
- Craft source for every requirement: [[fantasy-writing]] (story §N) and
  [[scifi-cinematography]] (visual **cine §N**, layer CINE).
- Consistency source of truth: [[canon-registry]] (filled per anthology).
- The runner that produces the scorecard + findings: [`../prompts/audit-script.md`](../prompts/audit-script.md).
- The work being audited: [[setting-sail-tier-descent]].
