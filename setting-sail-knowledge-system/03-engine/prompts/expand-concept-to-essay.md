# Prompt — Expand a Concept into an Essay

> A reusable LLM prompt that turns one or more atomic codex pages into a finished
> piece, with citations back to the book. Copy the block below, fill the slots, and
> run it against this repository.

---

## The prompt

```
You are a writer working inside the Setting Sail Knowledge System. Read
_schema/AGENTS.md first to understand the system and its citation format.

GOAL
Write a {{FORMAT: e.g. 1,200-word essay | 3-minute video script | podcast monologue}}
on the idea below, for an audience of {{AUDIENCE}}.

PRIMARY SOURCE PAGES (read these in full from 01-codex/):
- {{primary-concept-id}}
{{+ any supporting concept / principle / technique / metaphor ids}}

VOICE
{{Neutral and clear  |  In the author's voice — first read 02-legacy/voice.md}}

REQUIREMENTS
1. Open with a hook drawn from the page's "Gold nuggets" or the master metaphor
   [[you-are-the-sailor-not-the-wind]] when relevant.
2. Lead with a metaphor/story before the abstract claim (house style).
3. Include at least one of the page's "Practical examples" and one "Common mistake".
4. Honor the "Opposing ideas & tensions" — do NOT oversell; acknowledge the limit.
   If the topic appears in 01-codex/maps/contradictions.md, address the tension.
5. End with one concrete action (link a [[technique]] page if one exists).
6. Cite the book using the Source locations from each page (format: Ch.N §N.M "title").
7. Stay strictly within what the source pages support; if you need a claim they
   don't contain, flag it as [UNSOURCED] rather than inventing it.

OUTPUT
- The piece.
- A short "Sources used" list (page ids + Ch.N §N.M anchors).
- A "Gaps noticed" line if you hit anything thin (so it can be logged in maps/gaps.md).
```

---

## Notes
- For a **video/podcast** format, add: "mark [VISUAL] / [B-ROLL] cues" or "write as
  spoken dialogue between two voices: one asking, one explaining."
- For a **series**, point it at a file in `../series/` and ask it to draft one part.
- Keep the "stay within the sources / flag UNSOURCED" rule — it is what keeps the
  content engine trustworthy and traceable to the book.
