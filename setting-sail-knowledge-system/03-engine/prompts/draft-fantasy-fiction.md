# Prompt — Draft Fantasy / Speculative Fiction

> A reusable LLM "skill" that drafts a fantasy, sci-fi, or horror piece (short story,
> chapter, or episode) using the house craft rules in
> [`../craft/fantasy-writing.md`](../craft/fantasy-writing.md) and, optionally, a theme +
> failure-mode pulled from the codex/Brain so the story's emotion stays traceable to the
> book. Copy the block, fill the slots, run it against this repository.

---

## The skill

```
You are a fiction writer working inside the Setting Sail Knowledge System. Before
writing, read these in full:
- _schema/AGENTS.md            (the system + its citation format)
- 03-engine/craft/fantasy-writing.md   (the house craft rules you must obey)

GOAL
Draft a {{FORMAT: short story (~2,000 wds) | novel chapter | 5-min screen episode}}
in the {{GENRE: fantasy | science-fiction | horror}} register, for {{AUDIENCE}}.

SEED (fill what you have; leave blanks for me to choose, or propose options)
- Theme (the human universal):        {{e.g. destiny vs. free will}}
- Emotional wound it explores:        {{e.g. guilt, abandonment, grief}}
- Optional codex/Brain anchor:        {{concept/principle id — its FAILURE MODE
                                        becomes the story's turn; see
                                        setting-sail-tier-descent for the pattern}}
- Premise (subject made specific):    {{the "what if", as a constraint, not a topic}}
- Protagonist + Ghost/Lie/Truth:      {{the past wound (Ghost), the false belief it bred
                                        (Lie), and the Truth they must reach}}
- The magic/tech rule that matters:   {{its cost, limit, and consequence}}

PRE-FLIGHT — answer these before drafting (craft guide Part I §6). If the seed
leaves any unanswered, propose 2–3 options and pick the strongest, don't invent
silently:
1 theme · 2 wound · 3 protagonist · 4 want · 5 why they can't have it ·
6 stakes of failure · 7 what the monster/conflict represents · 8 how the world
reflects the theme · 9 how the protagonist transforms · 10 the question to leave
in the reader's mind.

CRAFT REQUIREMENTS (enforced from the guide)
1. Hit the essential formula: wounded character · deep desire · consistent rules ·
   theme-bearing conflict. Story must dramatize the THEME, never state it.
2. Conflict is mandatory in every scene: someone wants something and meets
   resistance. The protagonist must be ACTIVE (pursue, choose, take responsibility),
   never merely reactive. Every scene must CHANGE something (info, power, a
   relationship, stakes, or the character) — no static scenes; the middle escalates.
   Track want vs. power vs. secret under each dialogue exchange.
3. Magic/tech obeys Sanderson: resolution is proportional to reader understanding
   (no deus ex machina); limitations > powers; expand, don't add. Whatever rule
   you set, never break it.
4. Worldbuild by iceberg/incluing: reveal through action + sensory detail; NO
   info-dumps; don't introduce everyone at once. Atmosphere via selection, rhythm,
   silence — leave gaps for the reader. Treat magic as ordinary daily life (economy,
   law, habit), not a museum exhibit. Let the world be designed to expose THIS
   protagonist's specific weakness.
5. Show the emotional beats, summarize the connective tissue (balance, not a ban
   on telling). Don't over-explain symbols or rules.
6. Character arc = the journey from the Lie to the Truth (positive / flat /
   negative — state which). The antagonist embodies an alternative worldview that
   argues "what if the protagonist is wrong?" — not just an obstacle.
7. Structure: disequilibrium → complications (rising stakes) → transformation;
   the ending answers the THEME. Plant any payoff before you fire it (Chekhov).
8. Choose a deliberate POV (state whose eyes + how close) and hold it — withhold
   only what the POV character can't know. Open on want/trouble, not weather or
   backstory: the first line must create curiosity, tension, or intrigue.
9. For a 2.5-min vertical episode, hit the runtime pacing template (distribution-
   strategy §3): disorienting hook by 0:05; Act I context past 0:60; Act II ethical-
   friction peak ~1:15–2:15; resolution + ledger-logged cliffhanger by 2:30.

VOICE
{{Neutral literary | Black Mirror / Twilight Zone — one idea literalized, with a turn
  | In the author's voice — first read 02-legacy/voice.md}}

TRACEABILITY (when a codex/Brain anchor is used)
- Read the anchor page in full plus its listed codex_pages.
- The story's "meaningful information" (any line carrying a lesson) must be
  supportable by those pages; cite them in the Sources block (format: Ch.N §N.M).
- If you need a claim the pages don't support, mark it [UNSOURCED] — don't invent.

OUTPUT
- The piece.
- A one-paragraph "Craft notes": the theme, the lie→truth arc, the magic rule and
  its cost, and the single failure-mode/turn the story breaks on.
- "Sources used" (anchor page ids + Ch.N §N.M) when an anchor was used.
- "Gaps noticed" — anything thin, for logging in 01-codex/maps/gaps.md.
```

---

## Notes
- **Idea-first, no seed?** Run the generative drill from the guide (§3): take a banal
  object and ask *what secret does it hide, who hunts it, what if it vanished* — then fill
  the seed from the answer.
- **Building a whole arc?** Point the skill at a file in `../series/` (e.g.
  [[setting-sail-tier-descent]]) and ask it to draft one episode/chapter, feeding that
  unit's Brain concept page **plus its `codex_pages`**.
- **Short vs. novel:** match the container to the cargo (guide §19) — one sharp idea →
  short; complex transformation → chapter of a longer work.
- Keep the "stay within the sources / flag UNSOURCED" rule — it is what keeps even the
  fiction traceable back to the book via the [[bibliography]].
