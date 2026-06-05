# Anti-Patterns — How to Avoid Bad Science Fiction

> The failure-mode companion to [[scifi-writing]]: where that guide says what *to* do, this
> one names what to *avoid*. The worst sci-fi isn't lazy B-movie schlock — it's the film with
> **high production values that takes itself seriously, intends to be profound, and then
> insults the intelligence of anyone who passed high-school science.** Each trap below is
> tagged with the **requirement it violates** ([[writing-requirements]]) so the audit
> ([`../prompts/audit-script.md`](../prompts/audit-script.md)) can flag it by name. **▶ notes**
> apply it to [[setting-sail-tier-descent]].

> The root cause is almost always the same inversion: **the tech became the point and the
> people became the set.** Good sci-fi keeps the human condition in the foreground and lets the
> science be the stage ([[fantasy-writing]] §1, §36; [[scifi-cinematography]] §16).

---

## 0. First, calibrate — what to *forgive*
Not every implausibility is a crime. Don't apply this brand of criticism to:
- **The Golden Age exemption** — 1950s–early-'70s genre films worked with limited effects and
  a genuine lack of knowledge about space, physics, and computing. Judge them by their era.
- **Genre mismatch** — don't hold "space-adjacent" films to hard-SF standards. *Star Wars* is
  an adventure/western with knights and magic; *Passengers* is a castaway romance. They're
  built for entertainment, not scientific critique.
- **Remakes / rip-offs** — these usually fail because they're *embarrassing*, not because the
  sci-fi premise is broken.
> ▶ The anthology is **soft SF** ([[scifi-writing]] §1), so it claims the genre exemption from
> hard-physics nitpicks — but **internal consistency is never exempt** ("scientific accuracy
> optional; internal consistency mandatory"). HELM can be impossible; it cannot be *incoherent*.

## 1. Scientific-integrity traps · *violate `WORLD-03`, [[scifi-writing]] §4*
If you *claim* to be grounded, breaking physical law turns serious drama into accidental comedy.
- **"Asymmetrical" travel dynamics** — inventing nonsensical distances/times to suit pacing
  (3 weeks to Mars but 10 weeks to Neptune). **Fix:** map your universe's travel mechanics and
  hold a consistent scale of time and distance (record it in `WLD-*`/`TML-*`).
- **Insulting physical/biological law** — fake forces for cheap drama: reviving from *zero*
  oxygen, a snapped tether acting like a rocket booster on two idle bodies, centripetal force
  that flings a thing *at* you the instant a tether snaps. **Fix:** let the *real* danger of the
  environment drive tension; consult someone who knows the science.

## 2. Characterization & logic traps · *violate `CHAR-04`, `CHAR-05`, `CHAR-06`*
- **"Dumb scientist" syndrome** — trained specialists ignoring basic quarantine/safety just to
  manufacture a scare. **Fix:** no *stupidity for the sake of tension*. A genuinely terrifying
  threat should defeat characters who make **smart, logical choices** — that's scarier, and it
  protects `CHAR-04` (agency) and `CHAR-08` (a real antagonist).
- **Psychological incongruity** — establishing a trait then contradicting it unearned (the
  hardened loner who *loves* solitude but loses his mind on a routine 10-week transit).
  **Fix:** breakdowns must be *earned* by the established person (`CHAR-05` arc, `CHAR-06` Egri
  coherence).
- **Complete tactical nonsense** — illogical actions staged only to make an action beat (a
  trained crew opening fire *inside a cockpit full of unprotected control panels*). **Fix:**
  action must fit the environment; people who conquered the Solar System shouldn't behave like
  action-movie caricatures.

## 3. World-building & dialogue traps
- **The "Jason Voorhees" alien** · *violates `WORLD-02` (limits), `CHAR-08`; Sanderson Law 2.*
  An antagonist that breaks every biological rule to be unstoppable — grows faster than yeast,
  acid-immune, eyeless-but-sees, survives vacuum and plasma, *and* pilots a ship through
  re-entry hours after escaping — isn't a realistic alien, it's a slasher villain in space.
  **Infinite capability kills stakes.** **Fix:** give every life-form/tech clear strengths
  *and* vulnerabilities — limitations are more interesting than powers ([[scifi-writing]] §4).
- **"As You Know, Bob" hand-holding** · *violates `SCENE-05`, `WORLD-05`, `THEME-02`.*
  Characters explaining to each other what they'd both already know, purely to inform the
  audience — stilted, over-explained tech lectures. **Fix:** trust the audience; let the
  world's terminology be natural idiom. (The *Matrix* "Coppertop" reveal works because you
  piece it together *later* — discovery beats a lecture, [[fantasy-writing]] §14/§20.)

---

## Summary checklist — what good sci-fi must do
1. A premise reasonably related to a science concept (even if taken loosely). → `STORY-03`
2. A strong, **focused** sci-fi theme across environment, plot, and dialogue. → `STORY-01`, `THEME-03`
3. **Structural coherency** with the science we already know (or with its own stated rules). → `WORLD-03`
4. **People over spectacle** — the human condition above CGI-heavy, physics-defying noise. → `CINE-07`/`CINE-16`, `STORY-03`

## Anti-pattern → requirement map (for the audit)
| Anti-pattern | Flag under |
|--------------|------------|
| Asymmetrical travel / broken physics | `WORLD-03` (+ `WLD-*`/`TML-*` canon) |
| Dumb-scientist / stupidity-for-tension | `CHAR-04` |
| Unearned psychological break | `CHAR-05`, `CHAR-06` |
| Tactical nonsense | `CHAR-04`, `WORLD-03` |
| Overpowered, ruleless antagonist | `WORLD-02`, `CHAR-08` |
| "As You Know, Bob" exposition | `SCENE-05`, `WORLD-05`, `THEME-02` |
| Spectacle over people | `CINE-07`/`CINE-16`, `STORY-03` |

> ▶ The anthology is structurally *immune* to the worst of these by design: each short is built
> to **break its gadget on a real failure mode** — the opposite of the "Jason Voorhees"
> infinite-capability trap. Watch instead for the soft-SF risks: HELM rules drifting between
> episodes (`WORLD-03`/`ANTH-01`), a protagonist's collapse arriving *unearned* (`CHAR-05`), and
> the temptation to *explain* the module instead of letting the story collapse it (`THEME-02`).

## Sources & credits
- Synthesis of a "bad sci-fi" critique/manifesto (the Golden-Age & genre-mismatch exemptions,
  the physics/biology pitfalls, dumb-scientist & tactical-nonsense tropes, the overpowered-alien
  and "As You Know, Bob" traps) with the standard craft canon.
- Cross-references the *internal-consistency-over-accuracy* doctrine ([[scifi-writing]] §1/§4),
  Sanderson's Second Law (limitations > powers, [[fantasy-writing]] §12), and the
  show-don't-lecture rule ([[fantasy-writing]] §14/§20).
