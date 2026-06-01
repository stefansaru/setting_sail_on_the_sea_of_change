# Prompt — Per-Book Ingestion Sub-Agent

> Spawn **one sub-agent per book** to parallelize ingestion at scale (hundreds of books).
> Each sub-agent works on an **isolated file** (`library/books/<slug>.md`) so there are no
> write conflicts, and returns a structured **Contribution Report** that the *orchestrator*
> (main agent) merges into the shared `brain/`. The sub-agent **must not** edit `brain/` or
> any shared map — only its own book page. This keeps Brain updates serial and lets the
> orchestrator centralize the one thing that needs a human: **contradictions**.

---

## Sub-agent task (fill the slots, then spawn)

```
You are ingesting ONE book into the Setting Sail knowledge system.
First read _schema/AGENTS.md (esp. §11 Library and §12 Brain) and brain/maps/brain-index.md
so you know the existing Brain concepts.

BOOK
- Title: {{TITLE}}   Author: {{AUTHOR}}   Slug: {{SLUG}}
- Source folder/files (git-ignored): input/{{PATH}}

DO
0. **Select ONE source file** (never read duplicates). Ignore images/audio/video. Choose one
   format (EPUB > PDF > RTF/DOCX > TXT) and one language (EN; else RO). If chapter-split,
   concatenate that format's files in order. Note what you skipped. Extract text to C:/tmp/{{SLUG}}.txt.
1. **Read conclusions first (Tier 1 — fast):** table of contents, the conclusion/summary/
   epilogue/"key takeaways" (usually the last ~10–15%), the introduction (thesis), and any
   chapter-end summaries. From this capture: thesis, ~8–15 key concepts, ~5 best quotes.
   **Escalation gate:** only read more deeply (Tier 2) if the conclusions are *novel vs. the
   Brain, sharply contradictory, or unusually dense with actionable ideas.* Otherwise stop.
2. WRITE the distillation page library/books/{{SLUG}}.md from
   library/_templates/book-distillation.md — fill `language`, `format`, `files_skipped`,
   `depth`. In "Key concepts," link each idea to the codex page it rhymes with via [[wikilinks]]
   (consult brain-index.md). In "Connections," state agreements and tensions.
3. Do NOT edit anything under brain/, bibliography.md, or any maps/ file. Only create your one
   book page. (The orchestrator registers the book and updates the Brain.)
4. Return ONLY the Contribution Report below as your final message (strict format).

CONTRIBUTION REPORT (return exactly this structure)
---
book: {{SLUG}}
registry: { title, author, year, language, format, source_file, files_skipped, depth }  # for bibliography.md
one_line_thesis: <one sentence>
depth_used: T1 | T2
escalated_because: <reason, or "n/a — Tier 1 sufficed">
supports:              # existing Brain concepts this book endorses (+ evidence)
  - concept: <brain-concept-id>
    evidence: "<short quote or paraphrase + page/loc>"
  - ...
contradicts:           # where this book DISAGREES with the Brain or another book
  - concept: <brain-concept-id or 'book:other-slug'>
    claim: "<what THIS book argues>"
    against: "<what the Brain/other book argues>"
    evidence: "<short quote + page/loc>"
new_concepts:          # candidate Brain concepts not yet covered (may be empty)
  - id: <kebab-id>
    why: "<why it deserves a Brain page; is it cross-book?>"
notes: "<anything the orchestrator should know>"
---
```

---

## Orchestrator merge (main agent, after each sub-agent returns)
Run **serially** across returned reports (no concurrency on shared files):
0. **Register the book** in `library/maps/bibliography.md` from `report.registry`
   (title, author, year, language, format, file read, files skipped, depth). One row per book.
1. For each `supports[].concept`: add `{{SLUG}}` to that concept's `supported_by:`, add a
   bullet under "How each source frames it" with the evidence, **and add the book to that
   concept's `## References` section** (link to its `library/books/<slug>` page + [[bibliography]]).
2. For each `new_concepts[]`: if genuinely cross-cutting, create a `brain/concepts/<id>.md`
   (or a `seed` row) with `supported_by: [{{SLUG}}]`.
3. **For each `contradicts[]`: STOP and ASK the author** (AskUserQuestion) how to resolve —
   options: (a) keep both as a polarity (log in `01-codex/maps/contradictions.md`), (b) prefer
   one source, (c) add a condition/missing dimension (see [[polarity-thinking]]). Set
   `contested: true` on the affected Brain concept and link the polarity.
4. Run `brain/_tools/recompute-brain-scores.py --write` to refresh scores + the leaderboard.
5. Periodically regenerate `brain/the-efficient-mind.md` from the top of the leaderboard.

## Batching guidance
- Spawn in **batches** (e.g. 5–10 sub-agents at a time), not hundreds at once — keeps cost
  and review manageable, and lets you act on contradictions as they surface.
- Sub-agents are the *expensive* path; use them because the per-book work is large and
  parallel. For a handful of short books, the main agent can ingest directly without spawning.
- Group related books in a batch so cross-book agreements/tensions surface together.
