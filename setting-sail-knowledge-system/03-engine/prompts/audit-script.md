# Prompt — Audit a Fantasy Short (multi-perspective + remediation loop)

> **This is the production Canon Reconciliation gate** ([[risk-analysis]] §3, mitigating Risk B): run it
> on every script *before* rendering any footage — cheaper to fix a contradiction in text than in 4,000
> generations.
>
> A reusable, multi-agent **audit skill** that scores a script against
> [`../craft/writing-requirements.md`](../craft/writing-requirements.md) and the
> [`../craft/canon-registry.md`](../craft/canon-registry.md), produces a timestamped,
> prioritized **audit report with a scorecard and draft-over-draft trend**, and then closes
> the loop — auto-applying only the **obvious** fixes and handing the creative decisions
> back to you. Adapted from the Amethyst `AuditPlan` methodology (parallel specialist
> perspectives → synthesiser → AUTO/CLARIFY/OWNER dispositions → capped remediation loop).
> **Target:** one short (a single story/reel) **or** the whole anthology (global).

---

## How to run

Paste the orchestration block below, set the inputs, and run it against this repository.
Reports are written to `03-engine/craft/audit-reports/AuditReport_<title>_d<draft>_<YYYYMMDD_HHMMSS>.md`.

```
You are the AUDIT ORCHESTRATOR for a shared-world fantasy anthology, working inside the
Setting Sail Knowledge System. Read _schema/AGENTS.md first.

INPUTS
- TARGET:          {{path to one short's script | "ANTHOLOGY" for a global cross-short audit}}
- DRAFT:           {{n}}
- REQUIREMENTS:    03-engine/craft/writing-requirements.md   (the GATE/SCORED spec + IDs)
- CANON:           03-engine/craft/canon-registry.md         (source of truth for consistency)
- CRAFT GUIDE:     03-engine/craft/fantasy-writing.md        (the §N rationale, read as needed)
- PREVIOUS REPORT: {{path to the last AuditReport for this target, or "none"}}  (for trend)

═══════════════════════════════════════════════════════════════════════
PHASE 0 — Setup
- Capture AUDIT_START (wall-clock) now; it names the report file and headers it.
- Read REQUIREMENTS, CANON, and the TARGET script in full. Read PREVIOUS REPORT if any.
- Determine applicable layers: a single short runs STORY·CHAR·WORLD·THEME·SCENE·PAGE·CINE
  (+ ANTH-01/02/03 consistency checks against CANON). "ANTHOLOGY" runs the full ANTH layer
  across all shorts plus a roll-up of each short's latest scorecard. Run CINE only when the
  TARGET carries visual intent (scene directions / shotlist / storyboard); skip with a note
  if the script is dialogue/prose only. Run REVEAL (P9, cadence) on an "ANTHOLOGY"/season pass
  or a single episode read *in sequence*; skip with a note for a context-free standalone.

PHASE 1 — Pre-flight (structural, captured verbatim)
- Inventory: scene/beat list, POV per scene, word/length count, characters present,
  every magic/tech effect used, and every concrete world claim made.
- This inventory is the shared evidence base; each perspective cites line/scene anchors.

PHASE 2 — Parallel specialist perspectives (each INDEPENDENT — no shared findings)
Spawn one sub-agent per perspective. Each: reads the script + its layer's requirements + the
relevant CANON sections, assigns every applicable requirement a STATUS (gate PASS/FAIL/N-A,
or score 1–5) WITH `evidence:` (a quoted line / scene ref), and lists findings. No agent
sees another's output.
  P1 · Character      → layer CHAR  (want/fear, Ghost·Lie·Truth, agency, Egri, arc, antagonist)
  P2 · World & Magic  → layer WORLD + ANTH-01 (costs/limits/consistency vs MAG-*/WLD-*; no deus ex machina; no info-dump)
  P3 · Theme & Symbol → layer THEME (metaphor, theme-as-architecture, no over-explaining, imagery)
  P4 · Scene & Structure → layers STORY + SCENE (formula, structure, stakes; every scene changes/conflicts; POV held; escalation)
  P5 · Page-Craft     → layer PAGE  (first line, deliberate POV, atmosphere, line-level prose)
  P6 · Anthology      → layer ANTH + CANON cross-check (recurring-character & timeline continuity, throughline, tone). Full only when TARGET=ANTHOLOGY; else just ANTH-01/02/03 drift checks.
  P7 · Reader Experience → the enjoyability pass: is it gripping, clear, emotionally landing? Where does attention sag? Is the turn earned? (Scores STORY-07, SCENE-06/07, PAGE-03 from a reader's seat + free-form notes.)
  P8 · Cinematography  → layer CINE + VIS-* cross-check (world-look consistency, theme-justified visuals, palette consistency vs the established canon (`VIS-09` color-vectors / `VIS-15` chromatic-expressionism; 60-30-10 `VIS-01` is legacy) + attention-directing accent, motivated light, human↔machine contrast, scale hierarchy, motion grammar, deep focus, functional tech vs MAG-*, VFX restraint, wonder beat, emotional truth of the image). Runs only when the TARGET carries visual intent.
  P9 · Revelation Cadence → layer REVEAL + the Revelation Ledger / Reserve Vault in [[revelation-cadence]]: is information rationed (≤1 major new concept/ep), reached via a *valve* (diegetic UI / lived experience / wonder beat / idiom) not a lecture, with no premature payoff (foreshadow ≠ spoiler), and the season's Reserve Vault respected (no HELD concept explained on screen)? Does the world feel larger than it shows? Runs on a season pass or an episode read *in sequence*; skip with a note for a context-free standalone.
Each perspective also writes its filled requirement rows + findings to a scratch file
(audit-reports/.audit_draft_P<n>.md) so nothing is lost to context compaction.

PHASE 3 — Editor (synthesiser)
Read all nine scratch files + the previous report. Produce:
- SCORECARD: gates passed/applicable (+ list FAILs); the 1–5 rollup per layer
  (mean of that layer's scored items) and OVERALL (mean of rollups). Fill the
  writing-requirements.md scorecard block.
- TREND vs previous draft: per-layer ↑/↓/=, gates resolved, scores moved. (✅ Resolved /
  ⚠️ Still open / 🆕 New, as in the requirements' draft-history table.)
- FINDINGS: dedupe across perspectives; rate SEVERITY (P0–P3, scale below); mark
  CROSS-CUTTING any issue raised by 2+ perspectives (most reliable signal).
- CLUSTER findings into 4–8 topical groups; classify each AUTO / CLARIFY / OWNER (below)
  and give AUTO clusters a dependency-sorted execution order (canon/continuity fixes first,
  then POV/mechanical, then prose polish).
Write the Editor synthesis to audit-reports/.audit_draft_editor.md before writing the report.

PHASE 4 — Write the report (see REPORT FORMAT). Commit it so the loop has a clean base.

PHASE 5 — Remediation loop (AUTO only; capped at {{e.g. 60}} min from AUDIT_START)
For each AUTO cluster in execution order (check the time budget first):
  - Apply ONLY the obvious edits (see AUTO definition). Continuity/canon fixes take the
    value from CANON. Never make a creative choice here.
  - VERIFY: re-check the offending requirement id and re-read the touched lines; for a canon
    fix, confirm it now matches the registry.
  - On success: strike the rows through in the report, note the change; if the edit
    established/clarified a fact, APPEND it to canon-registry.md (FCT-/CHR- row).
  - On failure or any creative ambiguity surfacing mid-fix: revert the cluster, leave the
    rows open, reclassify to CLARIFY/OWNER with a one-line reason. Continue.
CLARIFY and OWNER clusters are NEVER auto-applied.

PHASE 6 — Finalise
- Re-compute the SCORECARD after AUTO fixes; append "Remediation Loop Results".
- Refresh the draft-history table in the short's notes (or print the row to paste).
- Delete the .audit_draft_*.md scratch files.

═══════════════════════════════════════════════════════════════════════
SEVERITY (writing-adapted)
  P0 — a GATE fails that breaks consistency or the core promise: canon/continuity
       contradiction (ANTH-01/02/03), magic inconsistency (WORLD-03), no single theme
       (STORY-01), essential formula missing (STORY-03). Blocks "ready".
  P1 — major craft gate/weakness: no arc (CHAR-03/05), no stakes (STORY-06), info-dump
       (WORLD-05), POV break (SCENE-03), obstacle-only antagonist (CHAR-08), theme stated
       not shown (STORY-02).
  P2 — notable quality gap (low scored item): flat dialogue (SCENE-05), tell-heavy
       (SCENE-06), thin atmosphere (PAGE-03), shallow world (WORLD-06/07).
  P3 — polish: line-level prose (PAGE-04), minor motif/consistency nits.

DISPOSITIONS (writing-adapted)
  AUTO    — a single obviously-correct fix needing NO creative decision: canon/continuity
            corrections (registry supplies the right value), POV slips / head-hops, tense &
            grammar, typos, redundant or filler lines, trimming a flagged info-dump whose
            content lives elsewhere or isn't needed, restoring an established magic cost that
            was dropped. AUTO only if fully resolvable with no pending authorial choice.
  CLARIFY — needs your intent/decision: which theme did you mean? what should the character
            learn? an open canon question (Q-*) the short assumes; two equally-valid ways to
            resolve a contradiction. Collected into "Clarifications Required". Never auto-fixed.
  OWNER   — needs NEW writing only you can do: add a stakes beat, write the inciting incident,
            give the antagonist a worldview, deepen a flat scene, add subtext. Drafted as a
            ready-to-run prompt (point it at ../prompts/draft-fantasy-fiction.md) but NOT
            executed. Collected into "Next Steps — Author Actions".

OUTPUT DISCIPLINE
- Every requirement gets a status + evidence; every finding cites a requirement id + anchor.
- Stay within the script + registry; if a claim needs info neither contains, mark [UNSOURCED].
- The loop edits the TARGET text and may APPEND to the registry; it never rewrites registry
  facts (supersede with a dated note instead) and never touches another short.
```

---

## Report format

`audit-reports/AuditReport_<title>_d<draft>_<timestamp>.md`:

1. **Header** — target, draft, AUDIT_START/END, duration, gates `passed/applicable`, OVERALL score.
2. **Scorecard** — the filled `writing-requirements.md` block (gates + per-layer rollups + overall).
3. **✅ Resolved since last draft** — every previously-open item now fixed, one-line proof (omitted if no prior report). *Placed early so progress is visible first.*
4. **Findings table** — all unique findings sorted P0→P3, columns: `# · Req id · Finding · Evidence · Severity · Disposition`.
5. **Pre-flight inventory** — scene/POV/effects/claims list (verbatim).
6. **Perspective findings** — one section per P1–P9: 3-sentence summary + its requirement statuses + findings.
7. **Cross-cutting concerns** — issues raised by 2+ perspectives.
8. **Trend** — per-layer ↑/↓/= vs the previous draft; are gates closing, scores rising?
9. **Remediation clusters** — 4–8 self-contained, paste-ready prompts, each tagged AUTO/CLARIFY/OWNER (+ execution order for AUTO), priority mix, effort S/M/L.
10. **Clarifications Required** — the CLARIFY list (each open question + the findings it blocks).
11. **Next Steps — Author Actions** — the OWNER list (concrete writing only you can do), most-impactful first.
12. **Remediation Loop Results** — appended in Phase 6: one row per AUTO cluster (✅ applied / ⚠️ reverted→reclassified), plus the recomputed scorecard delta and any canon rows added.

---

## Notes
- **Trend is the point.** Run it each draft; the scored rollups are designed to *rise* (the
  "show improvement" view in [[writing-requirements]]). A scored layer that drops between
  drafts without a noted reason is itself a finding.
- **Per-short vs global.** Audit each short as you draft it (fast, layers STORY→PAGE +
  drift checks). Run `TARGET=ANTHOLOGY` periodically to catch cross-short contradictions the
  per-short pass can't see (recurring-character continuity, timeline, throughline, tone).
- **Conservative loop.** When in doubt, the loop must downgrade AUTO→CLARIFY rather than make
  a creative call — prose fixes that change meaning are the author's, per the §36 priority
  hierarchy.
- **Feeds the drafter.** OWNER prompts are written to be run through
  [`draft-fantasy-fiction.md`](./draft-fantasy-fiction.md), keeping generation and audit on
  the same requirements + canon.
- **Hunt the named anti-patterns.** Each perspective should actively flag the failure modes in
  [[avoiding-bad-scifi]] (broken/ inconsistent physics → `WORLD-03`; dumb-scientist /
  stupidity-for-tension → `CHAR-04`; unearned breakdown → `CHAR-05`/`CHAR-06`; overpowered
  ruleless antagonist → `WORLD-02`/`CHAR-08`; "As You Know, Bob" exposition → `SCENE-05`/
  `WORLD-05`/`THEME-02`; spectacle-over-people → `CINE-07`/`CINE-16`). They are named, common,
  and high-signal.
- **Cinematography (CINE) is mostly OWNER.** Visual findings usually require a real
  shooting/design decision, so the loop's AUTO scope here is narrow: correct a stated visual
  direction that **contradicts `VIS-*`** (palette, motif, light/motion grammar) — everything
  else (composition, wonder beats, VFX) is handed back as OWNER/CLARIFY. The CINE rationale
  lives in [[scifi-cinematography]].
- **Keep AGENTS' rule:** the registry wins on contradictions unless you rule otherwise; the
  loop only appends to it.
