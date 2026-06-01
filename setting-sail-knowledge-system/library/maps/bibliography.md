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
| 1 | Think and Grow Rich (Gândește și devii bogat) | Napoleon Hill | 1937 | RO | pdf | **T2** | `input/Gandeste.si.devii.bogat-Napoleon Hill.pdf` | — | [[think-and-grow-rich]] |
| 2 | How to Stop Worrying and Start Living (Lasă grijile…) | Dale Carnegie | 1948 | RO | pdf·scan | T1 | `input/Lasa grijile incepe sa traiesti.ED.4.REV-Dale Carnegie.pdf` | image-only (no text layer) | [[how-to-stop-worrying]] |

## Skipped-file log (provenance)
*When a book folder has duplicates, note here what we ignored and why (so we never re-read it).*
- **#1 Hill** — single RO pdf; nothing to skip. Clean text via `pdftotext`.
- **#2 Carnegie** — single RO pdf, but a **334-page image scan with no text layer**; `pdftotext`
  returned nothing and no OCR tool is installed. Read **conclusions-first** by rendering the
  contents + key chapter pages to PNG (PyMuPDF) and vision-reading them. *If a clean EPUB/text
  edition appears later, prefer it and re-ingest at T2.*

## How to read this list
- The **count of rows** (minus #0) = how many sources support the Brain.
- A book's **Depth** tells you how much to trust its detail: T1 = thesis-level, T2 = deep.
- Sort mentally by how many Brain concepts a book feeds (see each concept's `supported_by`).

## Conventions
- Add the row in step 3 of the distillation INGEST (`AGENTS.md §11`), **before** touching the Brain.
- Keep `language` and `format` honest — they're the guarantee we read each book only once.
- Link the **Page** column to `library/books/<slug>` (or, for the home book, to the codex).
