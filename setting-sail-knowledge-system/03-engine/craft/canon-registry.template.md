# Canon Registry — TEMPLATE

> The **source of truth** for a shared-world anthology. Universal craft rules
> ([[writing-requirements]]) catch *"magic must have a cost"*; this registry catches
> **drift** — the established fact in short 2 that short 8 contradicts. Fill it as you write;
> every entry has a **stable ID** so the audit ([`../prompts/audit-script.md`](../prompts/audit-script.md))
> can cite it. Copy this file to `canon-registry.md` per anthology and keep it updated
> (requirement `PROC-01`, guide §33). **Append-only for facts:** never silently change an
> established fact — supersede it with a dated note so contradictions stay visible.

> **ID scheme:** `WLD-` world rules · `MAG-` magic/tech rules · `PLC-` places · `FAC-`
> factions/society · `CHR-` characters (bible) · `TML-` timeline · `FCT-` established-fact
> ledger · `TON-` tone/visual throughline · `VIS-` visual language (cinematography) · `Q-`
> open canon questions.

---

## 1. Premise & throughline
- **Logline (whole anthology):** …
- **Controlling question / spine:** …
- **`TON-01` Register & tone:** …
- **`TON-02` Recurring visual motif:** …

## 2. World rules (`WLD-`)
The fixed laws of the world (non-magic). One row per rule.

| ID | Rule | Established in | Notes / consequences |
|----|------|----------------|----------------------|
| WLD-01 | | | |

## 3. Magic / tech system (`MAG-`)
The audited heart of consistency. For each effect: what it does, its **cost**, its **limit**,
and who can use it.

| ID | Effect | Cost | Limit (can't do) | Who / access | Established in |
|----|--------|------|------------------|--------------|----------------|
| MAG-01 | | | | | |

## 4. Places (`PLC-`)
| ID | Place | What/where | Established in | Notes |
|----|-------|-----------|----------------|-------|
| PLC-01 | | | | |

## 5. Factions & society (`FAC-`)
| ID | Faction/institution | Interest / power | Established in |
|----|---------------------|------------------|----------------|
| FAC-01 | | | |

## 6. Character bible (`CHR-`) — especially recurring characters
One block per recurring/major character. Continuity (`ANTH-02`) is checked against these.

### CHR-01 — <Name>
- **Role / status:** …
- **Want · Fear:** …
- **Ghost · Lie · Truth:** …
- **Voice / speech signature:** …
- **Physical / identifying traits:** …
- **Relationships:** …
- **Knowledge state by short:** *(what they know/don't, per episode — guards reveals)* …
- **Appears in:** …

## 7. Timeline (`TML-`)
Chronology of in-world events and the publication/episode order, so cross-short time
references stay consistent (`ANTH-03`).

| ID | Event | When (in-world) | Short(s) | Notes |
|----|-------|-----------------|----------|-------|
| TML-01 | | | | |

## 8. Established-fact ledger (`FCT-`) — append-only
The catch-all for any concrete fact a later short must not contradict (a name, a number, a
color, a death, a rule-of-etiquette). Append; supersede with a dated note, never overwrite.

| ID | Fact | Established in | Status |
|----|------|----------------|--------|
| FCT-001 | | | active |

## 9. Visual language (`VIS-`) — cinematography canon
The look that must stay consistent across shorts. Audited by layer **CINE** (esp. `CINE-01`,
`CINE-06`, `CINE-13`) and `ANTH-06`. See [[scifi-cinematography]] for the rationale.

| ID | Element | Rule for this world | Status |
|----|---------|---------------------|--------|
| VIS-01 | **Palette (60-30-10)** | dominant __ / secondary __ / accent __ (accent = where the eye goes) | |
| VIS-02 | **Light sources** | what motivates light (panels, holograms, glow…) — "the world lights itself" | |
| VIS-03 | **Human↔machine contrast** | warm/soft/organic vs cool/sharp/geometric — how each reads | |
| VIS-04 | **Motion grammar** | what each camera behavior *means* here (stable / collapse / AI) | |
| VIS-05 | **Texture** | clean-sharp vs grain/decay, and why | |
| VIS-06 | **Wonder beats** | the planned awe moments (per short) | |
| VIS-07 | **Framing motif** | the recurring image carried through every frame (ties to `TON-02`) | |

## 10. Open canon questions (`Q-`)
Decisions not yet made — so the audit can flag a short that silently assumes an answer.

| ID | Question | Blocking? | Notes |
|----|----------|-----------|-------|
| Q-01 | | | |

---

## Maintenance
- When a short establishes a new fact, **add a row** (and note the short).
- When the audit finds a contradiction, the *registry wins* unless the author rules the
  registry was wrong — then supersede the entry with a dated note and fix the offending text.
- Keep `Q-` current: an answered question becomes a `WLD-`/`MAG-`/`FCT-` entry.
