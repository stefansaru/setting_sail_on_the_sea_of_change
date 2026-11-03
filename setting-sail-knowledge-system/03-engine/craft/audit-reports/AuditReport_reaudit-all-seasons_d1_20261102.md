# Audit Report: re-audit of all seasons, d1, 2026-11-02

> Second full pass after `Q-48`–`Q-52`. Four independent read-only audits, one per season, plus a mechanical link check.
> Follows [[AuditReport_requirements-all-seasons_d1_20261102]], whose §4 rows are referred to below as "row N".

## 1. Verdict
No season passes every gate yet. Each passes its own season row except S2. Counts were taken **before** the fixes in §3
and have not been re-run. Counts differ from the last report because `WR-T6`, `WR-B8` and `WR-M5` are new and these
auditors were stricter.

| Target | Pass | Fail | N/A | Season row | `WR-F3` |
|---|---|---|---|---|---|
| **S1** | 27 | 14 | 6 | Pass | ~4/5 |
| **S2** | 18 | 14 | 15 | **Fail** (glyph, must-not; both fixed in §3) | 3/5 |
| **S3** | 17 | 14 | 16 | Pass | 3/5 |
| **S4** | 23 | 15 | 9 | Pass | 3/5 |
| **Hull Cut** | | Fail | | Internal test only | |
| **Braided Cut** | | Fail | | One item open: swap Ep 7 and 8 | |

Most S1 failures left after §3 need the author. S1's durations recompute, apart from three in E3b and E12, now fixed.

## 2. Connection check
- 464 files. Every `Q-` and `WR-` reference resolves. 52 `WR` rules.
- 22 S1 scripts had nothing linking to them; the episode index now links each one.
- Two links broken by line wraps were repaired. The 18 unresolved links left are template placeholders, tag syntax and one
  library book not yet ingested. None is in a story file.
- Prose edition synced for the four changed lines. Glossary: 398 rows.

## 3. Fixes applied (about 160 factual edits)
- **S1:** E12's 20 years is 2 real hours, not seconds; E3b's verse is a song; Raul's heart alone fails in E17 (lungs were
  replaced in E10); E14 now fits `WR-M5` ("won't carry the beam in time"); E16 and E17 carry the new clocks;
  "interstellar" for E14; retired labels; Parish Metrics and the chain kept out of S1 planning notes.
- **S2:** nothing lies above Tier 3 (line deleted); the hollow glyph moved to the Merging, cold-complete placed at E16;
  the implants and Naomi's cure no longer blur; only unmaintained ledgers rot, not Ghosts; "missed her last months", not
  "her life"; *adam* means "man", tied to *adamah*, "earth".
- **S3:** fleet distance; Mara has no Lens, so UI on her is drawn in Raul's; Mara's sheet no longer claims traces that
  appear in no S1 or S2 script; "the DP" and old clone labels gone.
- **S4 and fleet table:** E15's packing now needs real Apex time (four minutes becomes most of a year); Decimus funds the
  climb; landfall moved to about T+10 and launch to about T−36 for acceleration and deceleration; Kai's body fails rather
  than dies when its line is cut; Rafe and his partner are finally named in E4, E16, E17; "manifest" Ghosts stand watches.

**Two fixes change meaning and need sign-off:** E15's new numbers and packing time (S4), and Decimus as the payer.

## 4. New structural findings
1. **The fleet lands before S2.** Landfall is about ten real years before S2E20, because S1's reply and the late ramp force
   it. This overrides `Q-29`'s "in flight throughout". S4 still runs as "meanwhile" for S1E14–17, not S2–S3. News of Mara's
   death reaches the colony over 30 years after landfall, so it can't be Part 2 texture unless S5 spans decades.
2. **The cure's donor has a gap.** Why isn't Ruth or the village a donor for Naomi? And what new thing did the climb buy,
   given chrome already existed? Recommended: the donor must be blood kin, and a body can't donate to itself. Adam
   was Naomi's only donor, and he sold his flesh climbing.
3. **Who is S3's Rafe?** A copy can't be summoned by E1's anomaly (round trip 8.8 years), and any copy sent after T+4.2 knows
   the strike. Recommended: he is the E16 reply copy, kept on Earth since T+8.2.
4. **Every beam-out leaves a copy** (`WR-M3`), so every evacuated Ghost has a second self, including Rafe. Recommended: a
   hull can pause until its last minutes, so only late beams fork. That keeps the second Kai unique.
5. **Hull Four after the strike.** A dead hull can't brake, so it overtakes the fleet within weeks, crosses the system before
   landfall, and contradicts "far astern". S5 must make something slow it. If it dies at zero, nothing can still transmit.
6. **Teo's mind has no way off Hull Four.** Recommended: lifeboats carry a small tether-only stack.
7. **Refugees cost only a trickle if paused,** so they couldn't halt the ramp. Recommended: lifeboats can't hold deep stasis,
   and re-stilling each refugee is a one-off chemistry hit.
8. **Rafe's route to the High Clock** has no rating behind it after four months aboard (`WR-S2`).
9. **Vance's E12 bargain never closes,** Hope's sentence has no exit, and nobody pays for E16's Apex hours. Recommended: at E15
   Adam takes Vance's keys, buying both his exit and the 2.4 hours, at the price of his last flesh.
10. **S3's secret has no mechanism.** The tribe knows who the child is from E8, yet she doesn't until E17, and Adam
    "recognizes" her in E14.
11. **The sovereign lock doesn't fit `MAG-25`:** only tissue can lock, and Mara's clip is on a server.
12. **Barrenness is never planted** before S3E7.
13. **Hull body counts.** "A few hundred minds, a handful of bodies" conflicts with bodies being "the many", so the pyramid has
    nothing to invert in S5.

**Decided 2026-11-02 after this report:** findings 2 (donor must be willing and dying, not kin), 3, 4 and 5, as `Q-53`–`Q-56`. Then, as recommended: findings 6–10, and rows 3 and 4 (`Q-57`–`Q-64`). Mara dying at about 17 leaves a new gate question: E16 and E18 offer a Merge to a minor, against `WR-M2`. Resolved 2026-11-03 as `Q-65`–`Q-68`: Mara's Merge is a signed exception; row 8, the strike; finding 11, the lock; finding 13, hull numbers.

## 5. Author items from the season audits, not applied
- **S1:** E11–13 has 21.5 unused hours (recommended: pods use them building Nia's body); E2 vs `FCT-010`; proxy notes for E14,
  E17; E18 spends E19's turn; who grants E1's Tier 3; castes for minor roles; Raul's want at E14 (`Q-09`); "Purist" is never
  said on screen; the four name collisions; E2 under `WR-F1`.
- **S2:** Adam's body location through the climb; Vesper's body outlives `WR-B2`; E18's Raul line states the theme; Vesper reunion
  is promised in S3 but missing; E10's message has no sender.
- **S3:** "clone" vs a gamete with a father; Vance's argument and age; god "forks herself" against `WR-M2`; E9, E19 with a Purist in a
  simulated place; "the prophesied return"; Raul speaks the thesis; `law-feed`, `the divers`, `Re-Cut` need glossary rows.
- **S4:** E4's hull; why "Quickened" is sealed; the High Clock's clearance for Rafe's reply.
- **Still open from the last report:** rows 3, 4, 8–18 and its §6 sign-offs.

## Related
- [[AuditReport_requirements-all-seasons_d1_20261102]] · [[world-requirements]] · [[glossary]] · [[the-seed-fleet]]

## 6. Auto-fix loop, 2026-11-03
The author delegated the remaining decisions. Round 1 applied rulings `Q-85`–`Q-114` and fixed each season (decisions logged as `Q-115`–`Q-118`); round 2 reconciled the seasons (`Q-119`, `Q-120`).

| Season | Before | After round 1 | Left after round 1 |
|---|---|---|---|
| S1 | 37 / 5 / 5 | 40 / 1 / 6 | glossary rows, now added |
| S2 | 26 / 10 / 11 | 42 / 1 (of 43 that apply) | glossary rows, now added |
| S3 | 23 / 10 / 14 | 29 / 2 / 16 | glossary rows, now added; S3E17 line, now `Q-120` |
| S4 | 33 / 5 / 9 | 41 / 1 / 8 | glossary rows, now added |

Hull and Braided Cuts pass their internal checks after round 1; neither was re-checked against `Q-119`. Round 2 repaired six cross-season threads (#9, #12, #13, the tissue lock, Raul's Lens, Parallel Pedagogy) and wrote one timeline into [[the-seed-fleet]]. No independent full re-audit has run since round 2.

## 7. Third full audit, 2026-11-03 (after commit 74fb045)
Five independent read-only audits (one per season, one for both cuts), then fixes applied the same day.

| Target | Pass | Fail | N/A | Season row | `WR-F3` | `WR-X4` | Fails (all fixed) |
|---|---|---|---|---|---|---|---|
| **S1** | 42 | 3 | 5 | Pass | 3.7 | 4 | B1 (Kavana, window woman, supper attendant), M5 (packing time), E1 (Rafe's watches unbudgeted) |
| **S2** | 40 | 1 | 9 | Pass | 4 | 4 | B1 (Adam's caste) |
| **S3** | 36 | 3 | 11 | Pass | 4 | 4 | N1 (`Slip: none`), N5 ("birth grant"), X2 (Vesper reunion unspent) |
| **S4** | 39 | 3 | 8 | Pass | 4 | 4 | T4 (Kai's E20 clock), B1 (ship's voice), N1 (Hull One) |
| **Hull Cut** | | 2 | | Internal test fixed | | | Glyph timeline; audit note; Q-71/Q-69 wording; Raul's T |
| **Braided Cut** | | 1 | | Order passes | | | Decimus first appearance (fixed); one-reveal-per-reel still fails by design |

- About 75 edits, no misses. Delegated calls logged as `Q-121` (Vesper reunion spent S3E14; her clock ran in bursts),
  `Q-122` (Kai's E20 clock), `Q-123` ("birth grant" on screen from S3E11; Hull-Cut Guide and Raul's T), `Q-124`
  (caste renamed **Woken**; Raul packs at Tier 1; Full Disclosure default with opt-out; Kavana a Shadow in the Apex).
- Contradictions cleaned: stale `Q-14`/`Q-23`/`Q-24`, "station accident" → "the night the Station is holed", SAVE is
  the patch not the alignment, alignment on by default (not won), the last copy of Mara's genome on Earth, Locked Block
  as one welded door, Mirror Asymmetry can't air in S1.
- Link check: 18 non-story placeholders, no undefined `Q-` or `WR-` references, 52 `WR` rules.
- **Still open:** the Braided Cut's folded reels exceed one major reveal (needs re-scripting or the 45-reel version, `Q-41`);
  `Q-09` (Hope placement), `Q-15`, `Q-18`, `Q-19`; S5's packet contents and who pays its Apex pack.

## 8. Knowledge-system audit, 2026-11-04 (after the author's Q-09…Q-41 answers)
Three read-only audits (world pages; craft, series and prompts; `04-scripts/`) plus a mechanical sweep of all 465
files, including `01-codex`, `brain` and `library`.

- **Sweep:** no retired terms or stale `Q-` references outside the story layers; 18 non-story placeholder links; no
  undefined `Q-`/`WR-` references; 52 `WR` rules.
- **World pages (54 edits):** birth wakes in the Tier-2 nursery (`FCT-013`); the vat clone retired for capsule growth;
  the 1% mutation is a dying Purist's last resort, never agelessness (`Q-74`); "AI President" → "the President"
  (`Q-98`); the encrypted-block page rebuilt around the tissue lock and the welded door; Woken, Tier-1 packing and Full
  Disclosure opt-out carried through; resolved questions struck; eight pages added to the world index.
- **Craft and series (49 edits):** registry fact rows synced with resolved rulings; glossary castes and first
  appearances (Woken has no S4 instance; ramp bodies stay stilled); three new interface rows; cadence vault and ledger
  rows for the slotted reels; blueprint ruling lists; `audit-script.md` now takes `world-requirements`, glossary and
  cadence as inputs and runs P10–P11.
- **Scripts and sheets (27 edits):** Q-09 Seeker notes in S1E11 and Raul's sheet; Kavana's Shadow hours; Vesper's
  bursts; Mara's remainder; Teo; cast table and readable list. No on-screen line changed except the prose's "visiting
  the wing" (matches S1E11).
- Delegated calls logged as `Q-126`. **Still open (author):** `Q-20`–`Q-22` (S3 title, lead, Rafe ally or rival) and
  `Q-36` (the Hull Cut's status). All belong to S3/the cuts, not S1–S2.
