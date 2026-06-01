# 📚 The Library — distilled wisdom from other books

A compounding shelf of **other people's books**, distilled to their main ideas and key
concepts, and cross-linked into the same knowledge graph as the *Setting Sail* codex. Read
one book here in 5 minutes; see how its ideas agree or clash with everything else you've read.

> This is **not** the full Setting Sail treatment. Each book gets **one high-signal
> distillation page** (`books/<slug>.md`) — thesis, ~8–15 key concepts, gold nuggets, and
> connections to the rest of the graph. Light, fast, recombinable.

## Layout
```
library/
├── books/<book-slug>.md   # one distillation page per book
├── maps/library-index.md  # all books + cross-book agreements / tensions / themes
└── _templates/book-distillation.md
```

## Conventions
- **One page per book.** Copy `_templates/book-distillation.md` → `books/<slug>.md`.
- **Slug** = kebab-case of the title (e.g. `deep-work`, `mans-search-for-meaning`).
- **Cross-linking (the whole point):** inside a concept, link straight to Setting Sail pages
  with `[[wikilinks]]` (e.g. "this is the book's version of [[becoming-the-observer]]").
  Link to another library book by its slug: `[[deep-work]]`.
- **Namespacing:** if you ever promote a book's concept to its *own* card, prefix the id with
  the book slug (`deep-work-attention-residue`) so it never collides with a codex page.
- **Provenance & copyright:** the **source file lives in `../../../input/` (git-ignored)** —
  it is *not* committed. These pages contain only **transformative distillation** (your notes,
  brief key-concept summaries, short attributed quotes), never the book's full text.

## Ingesting a new book (the distillation INGEST)
1. Drop the source file (`.pdf` / `.epub` / `.docx` / `.txt`) into `../../../input/`.
2. Extract the text (see `_schema/AGENTS.md §11` for the per-format commands).
3. Read it; fill `books/<slug>.md` from the template — thesis, key concepts (link to the codex
   where they rhyme), gold nuggets, and a **Connections** section (agreements & tensions).
4. Add a row to `maps/library-index.md` and note any new cross-book theme or contradiction.

## Start here
- [[library-index]] — every book on the shelf + the cross-book connection map.
