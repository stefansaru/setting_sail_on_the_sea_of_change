# Manus Brief — Generate the S01E01 Keyframe Image Batch

> **You are an autonomous production agent.** Your job: generate a **consistent batch of
> still keyframe images** for one 2.5-minute vertical short film, Episode 1 ("The Meadow
> Consensus"). These stills will later be animated into video, so they must look like frames
> from **one single film** — same two actors, same location, same light, same grade.
>
> You have **no prior context** about this project. Everything you need is in this file. Do
> not invent characters, props, locations, text, or UI. Follow the prompts **verbatim**.

---

## 0. The one rule that matters: CONSISTENCY

Image models are **stateless** — each generation is independent, so by default every image
will drift (different faces, different clothes, different light). You must defeat this:

1. **Generate a small REFERENCE PACK first** (Step 1) — the two actors and the location.
2. **Lock those reference images**, then **feed them as reference/consistency inputs into
   every keyframe generation** in Step 2.
3. **Never paraphrase** the descriptions. Copy the actor and setting wording **exactly** the
   same way in every prompt.
4. **Use one image model, one version, one fixed seed** for the entire batch. Do not switch
   models or change the seed mid-batch.

**Tooling:** Use an image generator that supports **reference-image conditioning for
character + scene consistency** — e.g. **Runway Gen-4 References** (preferred), or an
equivalent (Midjourney character-reference, Flux/Nano-Banana with reference images). Whatever
you use, the locked reference images **must** be attached to every keyframe generation.

---

## 1. Global look (applies to EVERY image)

- **Style:** cinematic, **photoreal, live-action film grade** (NOT illustration, NOT
  cartoon, NOT watercolor, NOT 3D-render look). Shot on **35mm anamorphic**.
- **Aspect ratio:** **9:16 vertical.** Resolution **at least 1080×1920**, prefer 2160×3840.
- **Palette:** warm **golden-yellow, glazed, luminous** — a "feel-good" utopian grade.
- **Light:** flawless, impossibly clean **golden-hour sunlight**. Serene beauty with a
  **faint uncanny, too-perfect stillness** (calm, quietly unsettling — like a beautiful
  simulation). Tender, peaceful mood.
- **Setting (the only location in this episode):** an **endless pristine sunlit meadow** —
  tall dewy green grass, a **distant ring of ancient broadleaf trees**, soft clearing sky.
- **Always avoid (negative):** any text, captions, subtitles, UI overlays, HUD, logos,
  watermarks; modern/branded clothing; jewelry; visible makeup; extra people; buildings,
  roads, vehicles, technology; harsh midday light; gloomy or desaturated grading.

### The two actors (THE PARENTS) — keep identical in every image
- **WOMAN:** early 30s, **warm light-brown wavy shoulder-length hair**, **hazel eyes**, soft
  natural features, **simple undyed cream linen wrap dress**, **barefoot**, no jewelry, no
  makeup, gentle expression.
- **MAN:** early 30s, **short dark-brown hair**, **light stubble**, calm warm face, **open
  natural-linen shirt and loose linen trousers**, **barefoot**, no jewelry, gentle expression.

---

## 2. STEP 1 — Generate and LOCK the reference pack (3 images)

Generate these three first. For the actor sheet, generate a few candidates, **pick the one
with the clearest, most natural faces**, and treat it as locked. Save with the exact
filenames given.

**`s01e01_ref_parents.png`** — actor reference sheet
```
Photoreal character reference sheet, live-action film grade, neutral soft studio lighting,
plain light-grey background. TWO people standing side by side, full body, plus inset face
close-ups of each.
WOMAN: early 30s, warm light-brown wavy shoulder-length hair, hazel eyes, soft natural
features, simple undyed cream linen wrap dress, barefoot, no jewelry, no makeup.
MAN: early 30s, short dark-brown hair, light stubble, calm warm face, open natural-linen
shirt and loose linen trousers, barefoot, no jewelry.
Warm healthy skin, relaxed natural expressions. Consistent, locked faces for film continuity.
No text, no logos.
```

**`s01e01_ref_meadow.png`** — location plate (no people)
```
Photoreal cinematic location plate, 35mm anamorphic, 9:16 vertical, NO people. An endless
pristine sunlit meadow: tall dewy green grass, a distant ring of ancient broadleaf trees, a
soft clearing sky. Flawless impossibly-clean golden-hour light, warm golden-yellow glazed
luminous palette, serene with a faint uncanny too-perfect stillness. No text, no UI, no logos.
```

**`s01e01_ref_palette.png`** — color/light target (optional 3rd reference)
```
A single photoreal beauty frame of the same golden meadow at golden hour, exemplifying the
exact target grade: warm golden-yellow, glazed, luminous, soft, dreamlike but photoreal.
Use only as a color/light reference. 9:16 vertical. No text, no logos.
```

**After this step:** load `s01e01_ref_parents.png` + `s01e01_ref_meadow.png` (and
`s01e01_ref_palette.png` if your tool allows a 3rd) as reference images, and **attach them to
every generation in Step 2.**

---

## 3. STEP 2 — Generate the 12 keyframes

Each prompt below is **complete and ready to use as written**. For every one: attach the
locked reference images, keep the **same model, version, and fixed seed**, output **9:16
vertical**, and save with the exact filename. Generate them **in one continuous session**.

> Shorthand used below — `[LOOK]` = paste this every time:
> *"Cinematic photoreal, live-action film grade, 35mm anamorphic, 9:16 vertical; endless
> pristine sunlit meadow with tall dewy grass, a distant ring of ancient trees and soft
> clearing sky; warm golden-yellow glazed luminous palette; flawless impossibly-clean
> golden-hour light, serene with a faint uncanny too-perfect stillness; no text, no UI, no
> logos."*

**`s01e01_K01_establishing.png`** — extreme-wide aerial establishing, high angle
```
[LOOK] Extreme wide aerial establishing shot, high angle looking down and across the endless
meadow. Two tiny barefoot figures — the WOMAN (warm light-brown wavy hair, cream linen wrap
dress) and the MAN (short dark hair, light stubble, linen shirt and trousers) — walk together
far below, dwarfed by the vast luminous grassland and the distant tree-ring. A god's-eye sense
of a contained, watched paradise. Full golden sunrise raking across the grass.
```

**`s01e01_K02_wide.png`** — symmetrical wide full shot, eye level
```
[LOOK] Symmetrical wide full shot, eye level. The couple — WOMAN (warm light-brown wavy hair,
cream linen wrap dress) and MAN (short dark hair, stubble, linen shirt and trousers), both
barefoot — walk toward camera through tall dewy grass, framed low in the bottom third with vast
open headroom of sky and ancient trees. Serene, breathing room, security.
```

**`s01e01_K03_lowangle.png`** — low-angle medium-full, front tracking
```
[LOOK] Low-angle medium-full shot from the front of the couple walking — WOMAN (warm
light-brown wavy hair, cream linen wrap dress) and MAN (short dark hair, stubble, linen shirt
and trousers), barefoot. Hero grass blades in soft foreground bokeh, sun flaring behind them,
gentle heroic scale, shallow depth of field.
```

**`s01e01_K04_twoshot_stop.png`** — medium two-shot, eye level (they stop)
```
[LOOK] Medium two-shot, eye level. The couple have stopped walking and the WOMAN (warm
light-brown wavy hair, cream linen wrap dress) turns to face the MAN (short dark hair, stubble,
linen shirt). Bodies close, a held, quiet, mid-conversation stillness, soft breeze through the
grass.
```

**`s01e01_K05_ots.png`** — over-the-shoulder onto her face
```
[LOOK] Over-the-shoulder shot, past the MAN's shoulder (soft, out of focus in the foreground)
onto the WOMAN's face — warm light-brown wavy hair, hazel eyes searching his, calm and full of
quiet wonder. Long lens, shallow focus, blurred golden meadow behind.
```

**`s01e01_K06_mcu_her.png`** — intimate medium close-up, her
```
[LOOK] Intimate medium close-up of the WOMAN — warm light-brown wavy hair, hazel eyes, soft
natural features, cream linen wrap dress — calm but full of quiet wonder, looking slightly off
camera. Blurred golden greenery behind, warm long-lens shallow focus.
```

**`s01e01_K07_cu_him.png`** — close-up, him
```
[LOOK] Close-up of the MAN's face — short dark-brown hair, light stubble, calm warm
expression — gentle and reassuring as he speaks. Warm catchlight in his eyes, soft golden rim
light, shallow focus, blurred meadow behind.
```

**`s01e01_K08_insert_bird.png`** — insert detail, the bird
```
[LOOK] Insert detail shot: a small wild songbird lands on a tall grass stalk and tilts its
head. Extreme shallow focus, dew droplets on the grass catching golden light. The couple are
soft and far out of focus in the background. Quiet, lifelike, intimate.
```

**`s01e01_K09_intimate_lean.png`** — intimate medium, rear three-quarter
```
[LOOK] Intimate medium shot, rear three-quarter angle. The WOMAN (warm light-brown wavy hair,
cream linen wrap dress) rests her head on the MAN's shoulder; he (short dark hair, linen shirt)
wraps his arms around her. Both face out over the sunlit meadow, backs partly to camera.
Tender, secure, warm.
```

**`s01e01_K10_ecu_hands.png`** — extreme close-up insert, hands
```
[LOOK] Extreme close-up insert of the couple's fingers weaving together, hands clasping. Warm
natural skin, soft golden backlight, very shallow focus, blurred golden meadow beyond. The
single human constant.
```

**`s01e01_K11_final_start.png`** — final shot, START frame (wide rear)
```
[LOOK] Wide full shot from behind: the couple — WOMAN (cream linen wrap dress, warm light-brown
hair) and MAN (linen shirt, short dark hair), barefoot, holding hands — walk away from camera
into shimmering backlit leaves and golden haze, sun flaring through the distant trees. A
peaceful departure.
```

**`s01e01_K11L_final_last.png`** — final shot, LAST frame (the held image)
```
[LOOK] Same wide rear composition as the previous shot: the couple now small and distant,
almost dissolving into an overwhelming bloom of perfect golden light that swallows the frame.
Beautiful and faintly unsettling — the seam of a too-perfect simulation implied in the glow.
Still holding hands, walking away.
```

---

## 4. Deliverables & filenames

Produce exactly these files, **9:16 vertical**, PNG, at least 1080×1920:

```
s01e01_ref_parents.png      s01e01_K04_twoshot_stop.png   s01e01_K09_intimate_lean.png
s01e01_ref_meadow.png       s01e01_K05_ots.png            s01e01_K10_ecu_hands.png
s01e01_ref_palette.png      s01e01_K06_mcu_her.png        s01e01_K11_final_start.png
s01e01_K01_establishing.png s01e01_K07_cu_him.png         s01e01_K11L_final_last.png
s01e01_K02_wide.png         s01e01_K08_insert_bird.png
s01e01_K03_lowangle.png
```

Plus one **`s01e01_contactsheet.png`** — all 12 keyframes (K01–K11L) tiled in a single grid,
in order, so consistency can be checked at a glance.

---

## 5. Quality-control checklist (self-review before you finish)

- [ ] The WOMAN looks like the **same person** in K02–K11L (same hair, eyes, dress).
- [ ] The MAN looks like the **same person** in K02–K11L (same hair, stubble, clothing).
- [ ] Both are **barefoot**, in **undyed linen**, with **no jewelry/makeup/modern items**.
- [ ] The meadow, tree-ring, and **golden glazed light** match across all frames.
- [ ] Every image is **photoreal** (not illustrated) and **9:16 vertical**.
- [ ] **No** text, UI, logos, watermarks, buildings, vehicles, or extra people anywhere.
- [ ] Faces are clean and natural (no distortion, no extra fingers in K10 hands insert).
- [ ] Re-generate any single outlier rather than re-rolling the whole set.
```
