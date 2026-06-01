# 03 — Engine (content generation)

The codex is structured precisely so it can be *recombined* into new artifacts. This
layer holds the machinery for turning atomic pages into books, videos, podcasts,
courses, and prompts for future AI assistants.

## What lives here

- `prompts/` — reusable LLM prompts that read the codex and emit drafts
  (e.g. "expand a concept into a 1,200-word essay", "turn a metaphor into a
  3-minute video script", "generate a podcast dialogue between two concepts").
- `formats/` — output templates per channel (book chapter, YouTube script,
  podcast outline, social post, course module).
- `series/` — outlines that sequence codex pages into a body of content
  (e.g. a "camel → lion → child" video trilogy; a 10-part newsletter on biases).
- `tools/` — optional helper scripts (lint, link audit, graph export).

## The core idea

Because every page is atomic, sourced, and linked, a generator can pull a coherent
set — *one principle + its supporting concepts + a metaphor + a technique* — and
have everything it needs to write, with citations back to the book.

## Worked example (seed)

See `series/camel-lion-child-trilogy.md` for how the [[three-metamorphoses]] arc
maps onto a three-part content series, each part anchored by a mascot
([[cammy-the-camel]]) and a master metaphor ([[you-are-the-sailor-not-the-wind]]).

*(This folder is scaffolded; prompts and formats are added as the codex grows.)*
