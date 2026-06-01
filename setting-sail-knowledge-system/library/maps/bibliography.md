# 📖 Bibliography — every source we've ingested

The master reference list. **One row per book**, recording exactly which single file we read
(and which we deliberately skipped), the language/format chosen, the depth tier, and a link to
its page. Every Brain concept's **## References** section points back here.

> **Selection rule (see `_schema/AGENTS.md §11`):** one book → **one file** read. Format
> priority **EPUB > PDF > RTF/DOCX > TXT**; language default **EN**, fallback **RO**. Audio,
> video, images, and duplicate editions are **skipped** (logged below for provenance).
> **Depth:** **T1** = fast, conclusions-first pass; **T2** = deep pass (only when the
> conclusions earned it); **Full** = complete atomization (only the home book).

## Books

| # | Title | Author | Yr | Lang | Fmt | Depth | Read this file | Skipped | Page |
|--:|-------|--------|----|----|-----|-------|----------------|---------|------|
| 0 | Setting Sail on the Sea of Change | (this author) | 2026 | EN | docx | **Full** | `input/20260217-…-revision-17.docx` | — | the whole `01-codex/` ([[worldview-spine]]) |
| 1 | _(first library book — add on ingest)_ | | | | | T1 | `input/…` | | |

## Skipped-file log (provenance)
*When a book folder has duplicates, note here what we ignored and why (so we never re-read it).*
- _(e.g. "Atomic Habits/ — read `…en.epub`; skipped `…ro.pdf` (duplicate language), `…audiobook.m4b` (audio), cover.jpg")_

## How to read this list
- The **count of rows** (minus #0) = how many sources support the Brain.
- A book's **Depth** tells you how much to trust its detail: T1 = thesis-level, T2 = deep.
- Sort mentally by how many Brain concepts a book feeds (see each concept's `supported_by`).

## Conventions
- Add the row in step 3 of the distillation INGEST (`AGENTS.md §11`), **before** touching the Brain.
- Keep `language` and `format` honest — they're the guarantee we read each book only once.
- Link the **Page** column to `library/books/<slug>` (or, for the home book, to the codex).
