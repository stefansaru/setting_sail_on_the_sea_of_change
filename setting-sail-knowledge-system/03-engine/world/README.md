# World Bible — the anthology's fictional universe

The **story-world layer**: atomic, cross-linked lore pages for the *SETTING SAIL* sci-fi world
([[setting-sail-tier-descent|the *Intention in Context* series]]) — the world concept, mechanics, technology, and environment,
written as *real*. This is distinct from its neighbours:

| Layer | What it is | Example |
|-------|-----------|---------|
| `craft/` | **how to** write/shoot/produce (generic know-how) | "magic must have a cost" |
| `craft/canon-registry.md` | the terse, auditable **consistency ledger / index** (ID'd rows) | `MAG-04 · Studio · cost: …` |
| **`world/` (here)** | the **lore itself** — the depth behind each registry row | a full page on the Studio module |

**The rule:** the registry stays the *index*; these pages hold the *depth*. Every page carries
its **canon ID** (e.g. `MAG-04`) in frontmatter so the registry indexes it and the audit can
cite it — no duplication. When you add a page for something **new**, also add/refresh its row in
[`../craft/canon-registry.md`](../craft/canon-registry.md).

---

## Structure (the four buckets)
One idea per file, in the bucket it belongs to:

- `concept/` — **world concept**: premise, cosmology, the big-picture logic (the Sea, the
  thesis, society's posture).
- `mechanics/` — **mechanics**: how things *work* — rules, systems, costs, limits, consequences
  (the auditable heart; maps to `WORLD-*`).
- `technology/` — **technology**: devices and interfaces (the HELM modules `MAG-*`).
- `environment/` — **environment**: places, ecology, atmosphere (`PLC-*`, the `VIS-*` look).

*(Recurring characters and factions normally live as `CHR-*`/`FAC-*` rows in the registry; give
one a full page here only if it needs real depth.)*

## Conventions
- Copy [`_template.md`](./_template.md). Fill the frontmatter, keep it atomic (one concept).
- `canon:` points to the registry ID this page expands (or `NEW → add a row`).
- `status: draft | locked` **mirrors the registry's soft/hard state** — `draft` means
  provisional (the audit treats contradictions as CLARIFY, not P0); promote to `locked` when
  settled.
- Link liberally with `[[id]]`. Put the *rules* (costs/limits/consequences) in their own section
  so `WORLD-01/02/03` are easy to verify; put the *look* notes against `VIS-*`.

## How it's audited
World pages are checked under the **WORLD** layer (rules, consistency, lived-in depth) and the
**ANTH** layer (cross-episode drift) of [[writing-requirements]], against
[`../craft/canon-registry.md`](../craft/canon-registry.md). Visual/setting notes feed **CINE** +
[[setting-design]].

---

## Index

> **The canonical world** (`Q-04` resolved 2026-06-04): the **Shadow Grid era** (File 1, substrate)
> with the **Doughnut Principle** thematic spine (File 2), distributed as **9:16 vertical Reels**.
> The HELM anthology is being **adapted into** this world. **Status: draft.** *(Provenance grouping
> below is by ingest file; it's all one world.)*

### concept/
- [[the-shadow-grid]] (`WLD-03`) — digitized consciousness on a distributed network; brain as antenna.
- [[the-cyborg-slip]] (`WLD-05`) — the real-time synthetic-replacement path to becoming digital.
- [[the-doughnut-principle]] (`WLD-06`) — **thematic spine**: intention in context; the Dual Arrows.
- [[the-macro-doughnut]] (`WLD-07`) — equilibrium / the Arrow of Balance (the maturity goal).
- [[the-shadow-entity]] (`WLD-08`) — tethered consciousness (body in stasis); Tether Sickness.
- [[the-ghost-entity]] (`WLD-09`) — purely digital, ledger-only soul; free but key-fragile.
- [[shells-with-ghosts-within]] (`WLD-10`) — leased physical hosts; the caste idiom & friction.
- [[the-ageless-default]] (`WLD-22`) — ageless avatars; substrate dysmorphia.
- [[the-sealed-manifest]] (`WLD-24`) — the High Clock's protective secrecy; the tissue-locked clause.
- [[the-ministry-of-hope]] (`FAC-03`) — the church-prison; accountability + a grey-line hospital.
- [[the-clock-brokers]] (`FAC-04`) — the overclocked criminal underclass; steal velocity credits to survive; Tether Sickness.
- [[the-medical-sanctuary]] (`MAG-17`) — Hope's experimental trials (99% cyborg / 1% ghost).
- [[the-distributed-president]] (`WLD-11`) — governance; law from real-time planetary status.
- [[the-post-labor-economy]] (`WLD-12`) — automation safety net: hospitality baseline OR Hope cloister.
- [[societal-values]] (`WLD-13`) — **the thematic skeleton**: the values matrix (today→future), System 1→2.
- [[the-memory-substrate]] (`WLD-14`) — **brain as lossy cache**: perfect recall in-grid, forgetting outside (closes S-01–05).
- [[standardized-vices]] (`WLD-15`) — vice licensed/standardized by substrate; accountability over taboo.
- [[intimate-commerce]] (`WLD-16`) — licensed sex work; biosecurity + client liability; cyborg/Ghost variants.
- [[frequency-tribes]] (`WLD-17`) — Dunbar-150 clock-based tribes; the Proximity Illusion; caste slang.
- [[parallel-pedagogy]] (`WLD-18`) — multi-threaded childhood; the Merging (graduation = ledger fusion); minor safeguards.
- [[recreation-culture]] (`WLD-19`) — fun as decompression for the sleepless: Turrell Raves, Historical Parsing, the Glacial Vacation.
- [[cultural-taboos]] (`WLD-20`) — the etiquette of disgust: the Glacial Stutter, Organic Leakage, Masked Intent.
- [[the-substrate-olympics]] (`WLD-21`) — Games split by substrate physics; the Tier-Reality Paradox (mind too fast for flesh).
- [[the-virtuous]] (`WLD-25`) — the creed every Grid child is raised in: break negative loops; no leadership without proof.

### mechanics/
- [[velocity-tiers]] (`WLD-04`) — the time-dilation hierarchy (Tier 0–3; Apex = 86,400×).
- [[inter-tier-travel]] (`MAG-10`) — the Data Buffer State (phase-matching tier clocks).
- [[the-1-percent-mutation]] (`MAG-13`) — DNA correction (99/1) + the Apex Escape Loop.
- [[progressive-digitalization]] (`MAG-15`) — the organic→synthetic body countdown (100→70→30→0%).
- [[the-absolution-protocol]] (`MAG-16`) — Hope's indefinite sentence; the Ledger of Absolution.
- [[intention-in-context-law]] (`MAG-18`) — fluid principle-based law; merit-keyed patches.
- [[disruptive-algorithms]] (`MAG-19`) — Bio-Fitness License + digital drugs as software exploits.
- [[compliance-validation-protocol]] (`MAG-20`) — real-time verification; the "Proven-in-Use" defense.
- [[intent-patch]] (`MAG-21`) — black-market spoof of the Intention Squares; games the CVP.
- [[tether-decay]] (`MAG-22`) — no dreaming in-grid; the TTD survival countdown; Sub-Velocity Sabbaticals.
- [[chromatic-tears]] (`MAG-23`) — malware as aesthetic corruption; flickers the Intention Squares, accelerates TTD.
- [[velocity-braking]] (`MAG-24`) — the spectacular takedown: Cognitive Shock Trap + Intercessor electromagnetic staffs.
- [[the-encrypted-block-paradox]] (`MAG-25`) — the sovereign-lock black box; an inmate the AI can neither read nor release.
- [[the-one-in-n-rule]] (`MAG-32`) — responsibility for N people requires passing a 1-in-N test; forks, ratings, ad-hoc succession.
- [[the-quickening]] (`MAG-34`) — capsules rush the body to keep up; the side-effects of rushing; the S1 real-time chronology.
- [[the-pattern-detector]] (`MAG-33`) — the Lens warning of a negative loop; the stress trigger; the alignment setting.
- [[the-stasis-economy]] (`WLD-23`) — watts vs chemistry; the fleet pyramid; the ramp.
- [[asymmetric-perspective]] (`MAG-27`) — shared coordinates, private renders.
- [[capsule-birth]] (`MAG-28`) — IVF → capsule; birth into the Tier-2 nursery.
- [[the-firing-protocol]] (`MAG-30`) — the open window.

### technology/
- [[the-personal-blockchain]] (`MAG-11`) — consciousness ledger; Full Disclosure; Chain-Check.
- [[the-cosmic-clone-paradox]] (`MAG-12`) — data-beaming; interstellar fork; Merge/Branch; tether risk.
- [[the-perspective-lens-ui]] (`MAG-14`) — the **9:16 UI grammar**: Context circles / Intention squares; custom lenses.
- [[flavor-scripts]] (`MAG-26`) — digital gastronomy: taste as a software packet; the room morphs color to the flavor.
- [[the-seed-fleet]] (`MAG-29`) — seven hulls; the two-clock T table.
- [[the-lure-beacon]] (`MAG-31`) — the false supernova.

### environment/
- [[the-shadow-grid-cooling]] (`PLC-03/04/05`) — frozen lunar servers, the Mirror Constellation, terrestrial vaults.
- [[data-graveyards]] (`PLC-09`) — frozen lunar-crater archival slums; bit-rot "Data Dementia" ghost-towns.
