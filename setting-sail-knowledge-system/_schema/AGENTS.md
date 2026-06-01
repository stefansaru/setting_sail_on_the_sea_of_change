# AGENTS.md — The Governor

> This file tells any human **or** LLM how to read, maintain, and extend the
> Setting Sail Knowledge System. If you are an AI assistant working in this
> repository, **read this file first and follow it exactly.** It is the schema
> layer of a Karpathy-style LLM-maintained wiki: raw sources → curated codex →
> this governor.

---

## 0. What this repository is

A permanent, compounding wisdom repository reverse-engineered from the book
*Setting Sail on the Sea of Change*. It is four things at once:

1. **A personal philosophy wiki** — every idea in the book, atomized and linked.
2. **A human operating system** — principles and techniques you can run your life on.
3. **A legacy archive** — a structured inheritance (see `02-legacy/`).
4. **A content engine** — raw material for books, videos, podcasts, and future AI assistants (see `03-engine/`).

The goal is **not** to summarize the book. The goal is to expose the *worldview
architecture* hidden beneath the chapters and make it queryable, extendable, and
durable beyond the author's lifetime.

---

## 1. The three layers (never collapse them)

| Layer | Folder | Mutable? | Purpose |
|-------|--------|----------|---------|
| **Sources** | `00-sources/` | **NO — immutable** | Faithful extraction of the manuscript. The ground truth every claim cites back to. |
| **Codex** | `01-codex/` | Yes — curated | The wiki. Atomic, cross-linked, neutral-voice pages. |
| **Legacy / Engine** | `02-legacy/`, `03-engine/` | Yes | Derived products: the inheritance layer and the content-generation layer. |
| **Governor** | `_schema/` | Rarely | The rules (this file + templates + taxonomy). |

**Rule:** Never edit `00-sources/` to "fix" the book. If the book is wrong,
incomplete, or self-contradictory, that belongs in the codex as an
*opposing idea*, a *contradiction* (see `01-codex/maps/contradictions.md`), or a
*missing concept* (`01-codex/maps/gaps.md`) — never as a silent edit to the source.

---

## 2. Atomicity — one idea per file

Every page in `01-codex/` captures **exactly one** idea. If a page needs the word
"and" in its title, it is probably two pages. Atomic pages are what make the
system recombinable for content generation and retrievable by an LLM.

Page types and where they live:

| Type | Folder | What it is |
|------|--------|------------|
| `principle` | `principles/` | An irreducible truth / first principle the worldview rests on. |
| `concept` | `concepts/` | A named idea, model, or distinction. Tagged `tier: major` or `tier: supporting`. |
| `technique` | `techniques/` | A concrete, do-this-now practice with steps. |
| `metaphor` | `metaphors/` | A story, mascot, image, or analogy used as a memory hook. |
| `influence` | `influences/` | A thinker / source the worldview borrows from. |

Maps, indexes, and graphs live in `maps/` and are the **only** non-atomic files
in the codex.

---

## 3. Filenames & IDs

- Filename = `kebab-case-of-the-id.md`. Example: `camel-phase.md`.
- The `id` in frontmatter must equal the filename without `.md`.
- IDs are **permanent**. To rename, create a redirect note rather than breaking links.
- `[[wikilinks]]` reference the `id` (Obsidian-compatible). A link to a page that
  doesn't exist yet is allowed and *encouraged* — it marks a page worth writing.

---

## 4. Frontmatter (required on every codex page)

```yaml
---
id: camel-phase                 # == filename, permanent, kebab-case
title: The Camel Phase          # human title (Title Case ok; body prose is neutral)
type: concept                   # principle | concept | technique | metaphor | influence
tier: major                     # major | supporting  (concepts only; omit otherwise)
status: stable                  # seed | draft | stable
chapter: 3                      # primary chapter of origin (0 = front matter, multi = lowest)
sources: ["Ch.3 §3.1", "Ch.3 §3.4"]   # citation anchors into 00-sources/
tags: [nietzsche, values, development-arc]
related: [lion-phase, child-phase, thou-shalt-dragon]
created: 2026-06-01
updated: 2026-06-01
---
```

`status` ladder: **seed** (stub, title + a line) → **draft** (all sections present,
rough) → **stable** (reviewed, sourced, cross-linked).

---

## 5. Page body — the eight required fields

Every `principle` / `concept` page contains these sections, in this order.
`technique`, `metaphor`, and `influence` pages use the trimmed variants in
`_schema/templates/`.

1. **One-line definition** — a `>` callout at the very top.
2. **## Definition** — what it is, in neutral prose.
3. **## Why it matters** — the stakes; why it earns a place in a life OS.
4. **## Supporting ideas** — what reinforces it (links + brief reasoning).
5. **## Opposing ideas & tensions** — honest counterpoints, limits, where it breaks. *Never skip this.*
6. **## Practical examples** — concrete, from the book and beyond.
7. **## Common mistakes** — how people get it wrong.
8. **## Related concepts** — `[[wikilinks]]`, each with one phrase on the relationship.
9. **## Source locations** — citation anchors (`Ch.N §N.M "title"`).
10. **## Gold nuggets** *(optional)* — verbatim quotable lines, attributed.

---

## 6. Voice

The codex is written in a **neutral, encyclopedic** voice — clean for humans, LLMs,
and content reuse. (The author's personal/first-person address lives only in
`02-legacy/`.) The book itself is written in all-lowercase; **direct quotations
preserve that styling**, but codex prose uses standard sentence case.

---

## 7. Citation format

Every factual claim traces to the source layer using the anchor format:

```
Ch.N §N.M "section title"
```

These anchors are stable headings in `00-sources/chapters/`. The book's `.docx`
has no reliable page numbers, so **section anchors are the canonical citation
unit.** See `00-sources/source-map.md`.

---

## 8. The three operations

This system runs on the same three operations as the Karpathy wiki pattern.

### INGEST — process a source into the codex
1. Read the chapter in `00-sources/chapters/`.
2. List every candidate: principle, concept (major/supporting), technique,
   metaphor, influence, recurring theme, contradiction, gap, gold nugget.
3. For each, check for an existing page (search `id` and titles) before creating
   a new one — **extend, don't duplicate**.
4. Create/extend atomic pages using the templates. Fill all required sections.
5. Add `[[wikilinks]]` both ways where a relationship exists.
6. Update `maps/` (knowledge graph, the relevant Map-of-Content, themes,
   contradictions, gaps) and log new gold nuggets.
7. Set `status` honestly. Leave `seed` stubs for anything you couldn't finish.

### QUERY — answer a question from the codex
1. Search the codex first; synthesize from atomic pages.
2. Cite the pages used and, through them, the source anchors.
3. If the answer reveals a *new* durable insight, file it back as a page or a
   note (the wiki should get richer with every good question).

### LINT — health-check the codex
Run the checklist in `_schema/lint-checklist.md`. In short: no orphan pages, no
broken `[[wikilinks]]` (except intentional seeds), every page has all required
sections and a source anchor, frontmatter `id` matches filename, contradictions
and gaps logged.

---

## 9. Discovering architecture (not mirroring chapters)

Do **not** organize the codex by chapter. Chapters are the book's delivery order,
not its logic. The reverse-engineered architecture is a four-stratum developmental
spine (Inheritance → Liberation → Authorship → Meaning) carried by Nietzsche's
camel → lion → child. See `01-codex/maps/worldview-spine.md`. New pages attach to
that architecture, with `chapter:` retained only as a provenance breadcrumb.

---

## 9.5 Editorial stance — preserve + critique

The codex is a faithful archive, not a rewrite. Standing policy (set by the author):

- **Preserve** every claim the book makes, faithfully, in the relevant page.
- **Critique in place** — when content is dated, gendered, factually shaky, or
  ethically narrow (e.g. the Ch.3 pickup-influenced relationship framing), record the
  concern in the page's **Opposing ideas & tensions** and, if structural, in
  `maps/gaps.md`. Do **not** silently soften or delete the original.
- **Neutral archivist voice** in the codex; personal reinterpretation belongs in
  `02-legacy/`. Do not moralize in the page body — state the limitation and move on.
- This keeps the system honest and trustworthy as a source, while leaving a clear
  trail for the legacy layer to restate ideas more durably if the author wishes.

## 10. When in doubt

- Prefer **more, smaller** pages over fewer large ones.
- Prefer **linking** over repeating.
- Prefer **logging a gap or contradiction** over smoothing it away.
- Preserve the author's metaphors and mascots — they are the system's memory hooks
  and its richest content-generation fuel.

---

## 11. The Library — distilling *other* books

`library/` holds **distillations of other authors' books**, cross-linked into the same
graph. This is a *lighter* operation than the full INGEST: **one page per book**, not
hundreds. See `library/README.md`.

### Copyright (important)
- Source files live in the repo-root **`input/` folder, which is git-ignored** — never
  commit a copyrighted book or its full-text extraction.
- Library pages contain only **transformative distillation**: brief key-concept summaries,
  your own notes, and *short* attributed quotes. No wholesale text.

### Extracting text by format (tools verified present on this machine)
- **PDF:** `pdftotext "input/book.pdf" "C:/tmp/book.txt"` (poppler, already installed). For
  scanned/visual PDFs, use the Read tool with `pages` ranges instead.
- **EPUB:** it's a zip of XHTML. Extract with Python (stdlib `zipfile` + `lxml`, both present):
  read the OPF spine order, strip tags from each XHTML doc, concatenate. (Same pattern as the
  `.docx` extraction script used for Setting Sail.)
- **DOCX:** the `zipfile` + `word/document.xml` regex method (see how Setting Sail was extracted).
- **TXT / MD:** read directly.
- **MOBI / AZW:** convert to EPUB/PDF first (Calibre `ebook-convert`); not installed here.

### The distillation INGEST (per book)
1. Drop the source in `input/`; extract text to `C:/tmp/` (don't commit the extraction).
2. Read it. Copy `library/_templates/book-distillation.md` → `library/books/<slug>.md`.
3. Fill: thesis · ~8–15 key concepts (each linked to the codex page it rhymes/clashes
   with) · techniques · gold nuggets · **Connections** (agreements & tensions).
4. Update `library/maps/library-index.md` (add the row; note cross-book agreements/tensions).
5. Log any *sharp* disagreement in `01-codex/maps/contradictions.md` as a cross-book polarity.
6. **Namespacing:** if a book's concept becomes its own card, prefix the id with the book
   slug (`deep-work-attention-residue`) so it never collides with a codex page.

The payoff: every new book makes the *whole* graph richer — you see where authors converge,
where they contradict, and where each fills a gap the others leave.

---

## 12. The Brain — the scored, compounding synthesis

`brain/` is the top layer: **cross-source master concepts** (the recurring "ways of thinking"),
each **scored by how many books support it**, building toward one description of an efficient
way of thinking that improves life ([[the-efficient-mind]]). See `brain/README.md`.

### Scoring (the rule)
- Each `brain/concepts/<id>.md` has `supported_by:` (list of source slugs) and `contested:`.
- **`score = number of distinct sources in `supported_by``** — the single source of truth.
- `brain/_tools/recompute-brain-scores.py --write` recomputes every `score:` and regenerates
  the leaderboard in `brain/maps/brain-index.md`. Never hand-edit scores; edit `supported_by`.
- More sources endorsing a concept → higher score → more central to the recommended way of thinking.

### What belongs in the Brain (vs. the codex)
- The Brain is **higher-order and selective**: only the cross-cutting modes of thinking that
  recur across books. Not every codex/book concept is promoted.
- A Brain concept *synthesizes* and links **down** to the codex pages (Setting Sail's instance)
  and `library/books/<slug>` pages that support it. Don't duplicate their detail — point to it.
- Seed the Brain from the most-referenced codex concepts; expand as books arrive.

### Updating the Brain (per book) — and the contradiction rule
Driven by the per-book sub-agent's Contribution Report (`03-engine/prompts/ingest-book-subagent.md`):
1. **supports** → append the book slug to the matched concept's `supported_by:` + add an
   "How each source frames it" bullet with evidence.
2. **new_concepts** → create a new Brain page (or `seed` row) if genuinely cross-cutting.
3. **contradicts → ASK THE AUTHOR.** This is a hard rule: when a book clashes with the Brain
   or another book, **pause and ask** (AskUserQuestion) how to resolve — keep both as a
   [[polarity-thinking|polarity]] (log in `01-codex/maps/contradictions.md`), prefer one
   source, or add a missing dimension. Mark the concept `contested: true`. Never silently pick a side.
4. Run the score script; periodically regenerate [[the-efficient-mind]] from the leaderboard top.

### Scale: one sub-agent per book
For large libraries, spawn **one sub-agent per book** (batches of ~5–10). Each writes only its
own `library/books/<slug>.md` (no write conflicts) and returns a Contribution Report; the
**orchestrator** serially merges reports into `brain/` and handles contradictions with the
author. For a few short books, ingest directly without spawning.
