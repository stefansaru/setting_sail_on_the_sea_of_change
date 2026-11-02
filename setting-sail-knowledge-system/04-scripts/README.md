# 04 — Scripts (workable outputs)

> The **production-ready, human-readable outputs** of the system, in one place — the cast, the readable
> season prose, and the briefs that turn scripts into media. This is the layer you *read from, cast from, and
> hand to tools*. It is distinct from **`03-engine/`**, which holds the *authoring/reference* material (the
> codex, world bible, craft guides, season blueprints).
>
> *(Renamed from the former `04-tools` on 2026-06-06, consolidated as the single "workable outputs" home.)*

## What lives here
- **`episodes/`** — the per-shot **shooting scripts** (`s1e##` + standalone reels) and the Episode Guide;
  the verbatim source the audit runs against (moved here from `03-engine/scripts/`, 2026-06-06).
- **`characters/`** — the **cast bible**: one page per character, expanding the terse `CHR-*` rows in
  [`../03-engine/craft/canon-registry.md`](../03-engine/craft/canon-registry.md) into full sheets (identity,
  arc per season, body-clock & glyph, want/fear/lie/truth, relationships, open questions).
- **`readable/`** — each season retold as **prose short stories** (the reading edition), production
  scaffolding stripped. Source of truth stays the shooting scripts in [`episodes/`](episodes/).
- **`production/`** — **tool briefs** that turn a script into media (e.g. the Manus keyframe-batch brief).

## The cast
| Character | Page | Canon | Role | Seasons |
|-----------|------|-------|------|---------|
| **Raul** | [[raul]] | `CHR-02` | Protagonist — "the Unsynced Mind" | S1 lead · S2 guide · S3 lead |
| **Mara, the Cartographer** | [[mara]] | `CHR-01` | The architect / Distributed President; incarnates | S1–S2 trace · S3 |
| **Adam** | [[adam]] | `CHR-06` | "The Grounded One" — the inverse pilgrim | S2 lead · S3 |
| **Naomi** | [[naomi]] | `CHR-11` | Adam's mother; breaks her vow, dies mortal | S1 · S2 |
| **Ruth** | [[ruth]] | `CHR-07` | The one who stays; the S3 surrogate (Book of Ruth) | S2 · S3 |
| **Vance** | [[vance]] | `CHR-04` | Antagonist — the optimization tempter | S2 · S3 |
| **Vesper** | [[vesper]] | `CHR-05` | Raul's partner; the Proximity Illusion | S1 · S2 · S3 |
| **The AI Guide** | [[the-ai-guide]] | `CHR-03` | The comforting guide (the Teddy Bear) | S1 · S2 echo |
| **Rafe** (the Centauri Clone) | [[the-centauri-clone]] | `CHR-02` Branch (`Q-14`) | Raul's branched other self; S3 rival-engineer | S1 · S3 |
| **Jun** | [[jun]] | supporting (`Q-08`) | Raul's friend; the gentle Cyborg Slip | S1E7 |
| **Nia** | [[nia]] | supporting (`Q-08`) | The Purist who becomes what she refused | S1E11–13 |
| **Kai** | [[kai]] | `CHR-08` (`Q-27`) | "The Sleeper" — the colonist trapped on Hull Four | S4 lead · S5 |
| **Teo** | [[teo]] | `CHR-09` (`Q-34`/`Q-35`) | "The Hero" — the worker who answers the lure | S4 · S5 |
| **Decimus** | [[decimus]] | `CHR-10` | The bay safeguard who jumps straight to 1 in 10 | S4 · S5 |

> **Minor / unwritten** (add a page as each is named, `Q-08`): the E1 parents, the Hope **Pastor**, the
> E19/E20 **Purist mother**. The terse index for all of the above is the `CHR-*` table in the
> [canon registry](../03-engine/craft/canon-registry.md).

## Readable editions
- [`readable/season-1-the-intention-ledger.md`](readable/season-1-the-intention-ledger.md) — **S1**, all 20
  episodes as prose. ✅
- **S2 "The Mortal Ledger"** and **S3 "The Cartographer's Ledger"** — to be drafted from their blueprints.
- **S4 "The Seed Ledger"** (draft seed, 2026-10-12) — blueprint only: [`../03-engine/series/setting-sail-the-seed-ledger.md`](../03-engine/series/setting-sail-the-seed-ledger.md).

## Conventions
- Character pages use the same frontmatter spirit as the world bible (`id`, `canon`, `status`, `related`),
  and link with `[[id]]`. The **canon registry remains the source of truth**; these pages are the expansion.
- Keep the readable prose faithful to the audited shooting scripts; when a script changes, update its prose.
