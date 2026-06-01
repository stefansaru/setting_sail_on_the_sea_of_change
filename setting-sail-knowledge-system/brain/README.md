# 🧠 The Brain — a scored, compounding model of how to think well

The **Brain** is the synthesis layer above everything else. While `01-codex/` atomizes
*Setting Sail* and `library/` distills other books one page each, the **Brain holds the
cross-source master concepts** — the recurring "ways of thinking" that show up again and
again — each **scored by how many books support it**, and expanded in detail.

> **Goal:** assemble, from *all* these books, a description of an **efficient way of thinking
> that improves quality of life.** The capstone is [[the-efficient-mind]].

## How it works

1. **Seed from Setting Sail.** The Brain starts from the most central concepts already in the
   codex (measured by inbound links) and expands them into cross-source master concepts.
2. **Every book updates the Brain.** When a book is ingested (see `_schema/AGENTS.md §12`),
   its sub-agent reports which Brain concepts it *supports* or *contradicts*, with evidence.
3. **Score = number of distinct sources that support a concept.** More books endorsing an
   idea → higher score → more central to the recommended way of thinking. *(Setting Sail = 1.)*
4. **Contradictions are surfaced to you.** When a book clashes with the Brain or another book,
   the orchestrator **pauses and asks you** how to resolve it (keep both as a polarity, prefer
   one, add a condition…). Resolved tensions become [[contradictions|polarity entries]].

## Scoring model
Each Brain concept's frontmatter lists `supported_by:` (source slugs) and `contested:`.
```
score        = len(supported_by)          # distinct sources (primary ranking)
mentions     = total references (optional, secondary)
contested    = true if sources disagree   → links to a contradiction entry
```
Run `_tools/recompute-brain-scores.py` to recompute every score from `supported_by:` and
regenerate the leaderboard in `maps/brain-index.md`. **Single source of truth = `supported_by`.**

## Layout
```
brain/
├── concepts/<concept>.md     # scored master concepts (the modes of thinking)
├── the-efficient-mind.md     # capstone: the assembled way of thinking (the goal)
├── maps/brain-index.md       # the scored leaderboard + coverage by source
└── _tools/recompute-brain-scores.py
```

## Page conventions
- `type: brain-concept`. Title = the mode of thinking (e.g. "Agency Over Circumstance").
- **Synthesis across sources:** a "How each source frames it" section that *grows per book*.
- Link down to the `01-codex/` pages (Setting Sail's instance) and to `library/books/<slug>` pages.
- A Brain concept is **higher-order** than a codex concept — it's the pattern *behind* many
  codex/book pages. Not every codex concept becomes a Brain concept; only the cross-cutting ones.

## Relationship to the rest
- `01-codex/` = Setting Sail, fully atomized (book #1's deep contribution + the seed).
- `library/books/` = every other book, one distillation page each.
- `brain/` = the **consensus core**: what they all teach about thinking well, scored and synthesized.

## Start here
- [[brain-index]] — the scored leaderboard of every mode of thinking.
- [[the-efficient-mind]] — the capstone synthesis (the goal).
