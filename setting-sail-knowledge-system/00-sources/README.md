# 00 — Sources (immutable)

Faithful extraction of the manuscript. **Do not edit these files to "fix" the
book.** This layer is the ground truth every codex claim cites back to.

- `chapters/` — one Markdown file per chapter, with stable section anchors
  (`§N.M`) and preserved poems, quotes, and captions.
- `source-map.md` — the index of chapters → sections, and the canonical
  **citation format**: `Ch.N §N.M "section title"`.

Original manuscript: `../../input/20260217-setting-sail-on-the-sea-of-change-revision-17.docx`
(revision 17). The `input/` folder is **git-ignored** (large binary source files live there,
preserved by a `.gitkeep`), so the manuscript itself is not version-controlled — only this
faithful text extraction is. Extraction is text-only; embedded images/figures remain in the .docx.

If the book is wrong, incomplete, or self-contradictory, that does **not** get
fixed here — it is recorded in the codex as an *opposing idea*, a logged entry in
`01-codex/maps/contradictions.md`, or a gap in `01-codex/maps/gaps.md`.
