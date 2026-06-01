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
- Source file (git-ignored): input/{{FILENAME}}
- Extracted text: {{TMP_TXT_PATH}}   (already extracted for you; if missing, extract per §11)

DO
1. Read the extracted text. Identify the book's thesis, ~8–15 key concepts, key techniques,
   and the best ~5 quotable lines.
2. WRITE the distillation page library/books/{{SLUG}}.md from
   library/_templates/book-distillation.md. In "Key concepts," link each idea to the codex
   page it rhymes with using [[wikilinks]] (consult brain-index.md and the codex). In
   "Connections," state agreements and tensions with Setting Sail / other books.
3. Do NOT edit anything under brain/ or any maps/ file. Only create your one book page.
4. Return ONLY the Contribution Report below as your final message (this is what the
   orchestrator consumes — keep it strict).

CONTRIBUTION REPORT (return exactly this structure)
---
book: {{SLUG}}
one_line_thesis: <one sentence>
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
1. For each `supports[].concept`: add `{{SLUG}}` to that concept's `supported_by:` (and add a
   bullet under "How each source frames it" with the evidence).
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
