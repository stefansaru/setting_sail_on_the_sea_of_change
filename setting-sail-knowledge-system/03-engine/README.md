# 03 — Engine (content generation)

The codex is structured precisely so it can be *recombined* into new artifacts. This
layer holds the machinery for turning atomic pages into books, videos, podcasts,
courses, and prompts for future AI assistants.

## What lives here

- `prompts/` — reusable LLM prompts that read the codex and emit drafts
  (e.g. "expand a concept into a 1,200-word essay", "turn a metaphor into a
  3-minute video script", "generate a podcast dialogue between two concepts").
- `series/` — outlines that sequence codex pages into a body of content
  (e.g. a "camel → lion → child" video trilogy; a 10-part newsletter on biases).
- `world/` — the **story-world bible**: atomic lore pages for a series' fictional universe
  (world concept, mechanics, technology, environment), each carrying its `canon-registry` ID.
  The registry is the index; these pages hold the depth.
- **Episode scripts** now live in **[`../04-scripts/episodes/`](../04-scripts/README.md)** (moved out of the
  engine, 2026-06-06): the verbatim `s1e##-slug.md` prose (+ descriptive standalone slugs) the audit runs
  against, plus the Episode Guide. Still paired with the outline in `series/` and the canon in `world/`.
- `craft/` — house references for *how* to write, shoot, and produce a given form, plus the
  audit apparatus: `fantasy-writing.md` (universal story craft), `scifi-writing.md` (the
  science-fiction genre overlay, with `avoiding-bad-scifi.md` anti-patterns),
  `scifi-cinematography.md` (visual craft, with deep-dives
  `negative-space.md`, `lighting.md`, `vertical-grammar.md` (9:16),
  `chromatic-expressionism.md` (the 5-master-artist scenic color/light system), and the
  `cinematography-techniques.md` master toolkit), `setting-design.md` (setting &
  production-design aesthetics), `film-production.md` (end-to-end production workflow), and the
  ops docs `ai-production-toolkit.md` (AI tool pipelines + cost), `market-research.md`
  (audience), `distribution-strategy.md` (the YouTube–TikTok Barbell + runtime pacing map), and
  `risk-analysis.md` (risk/mitigation matrix); `revelation-cadence.md` (the **information-rationing**
  guideline — the Revelation Ledger + Reserve Vault: how much world the *audience* gets per episode);
  `glossary.md` (every name and coined term: definition, first on-screen use, retired words — `WR-N1..N5`);
  `writing-requirements.md`
  (auditable GATE/SCORED requirements — story layers, the CINE layer + the REVEAL cadence layer); `canon-registry.md`
  (+ `.template.md` — the per-anthology source of truth for story *and* visual `VIS-*`
  consistency); and `audit-reports/` (timestamped scorecards).
- Helper scripts (lint, link audit, graph export) live in a `_tools/` folder next to
  what they operate on — today only [`../brain/_tools/recompute-brain-scores.py`](../brain/_tools/recompute-brain-scores.py).

## The core idea

Because every page is atomic, sourced, and linked, a generator can pull a coherent
set — *one principle + its supporting concepts + a metaphor + a technique* — and
have everything it needs to write, with citations back to the book.

## Worked example (seed)

See `series/camel-lion-child-trilogy.md` for how the [[three-metamorphoses]] arc
maps onto a three-part content series, each part anchored by a mascot
([[cammy-the-camel]]) and a master metaphor ([[you-are-the-sailor-not-the-wind]]).

*(This folder is scaffolded; prompts and formats are added as the codex grows.)*
