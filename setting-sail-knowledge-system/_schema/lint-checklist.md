# Lint Checklist

Run this after any INGEST pass, or periodically, to keep the codex healthy.
A future helper script (in a `_tools/` folder, like `brain/_tools/`) can automate the mechanical checks.

## Structural
- [ ] Every codex page's frontmatter `id` equals its filename (minus `.md`).
- [ ] Every page has a `type` matching its folder.
- [ ] Every page has at least one `sources:` anchor that resolves in `00-sources/source-map.md`.
- [ ] Every required section is present for the page's type (see templates).
- [ ] No page title contains "and" hiding two atomic ideas.

## Link health
- [ ] No broken `[[wikilinks]]` **except** intentional `seed` targets.
- [ ] Relationships are reciprocal: if A links B as related, B links A.
- [ ] No orphan pages (every page is reachable from a Map-of-Content or the graph).

## Content integrity
- [ ] Every `principle`/`concept` page has a non-empty **Opposing ideas & tensions** section.
- [ ] Contradictions between book claims are logged in `maps/contradictions.md`, not smoothed away.
- [ ] Identified gaps / missing concepts are logged in `maps/gaps.md`.
- [ ] Direct quotes preserve the book's original styling; prose is neutral sentence case.
- [ ] `00-sources/` is unchanged (the source layer is immutable).

## Map freshness
- [ ] New pages are added to `maps/knowledge-graph.md`.
- [ ] New pages carry a `stratum/*` and (if relevant) `arc/*` tag.
- [ ] New recurring themes are reflected in `maps/themes.md`.
