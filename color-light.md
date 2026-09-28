# Color and light — designer ratios (reference)

Quantitative rules for `color_palette`, `style`, and `lighting`. The sources are two groups: Black Forest Labs documentation (the 5 light attributes, HEX prompting) and professional design/film practice — 500px (color wheel for photographers), PremiumBeat (color schemes in filmmaking), DFI Rentals (teal & orange colorimetry, skin tone line), HowToFilmSchool and Wandering DP (lighting ratios), Pixflow (color temperature).

Status: everything quantitative in this file — 60-30-10, key:fill ratios, Kelvin values, the direction and shadow/bounce rules (§7–8) — is **not from the official documentation**: it comes from professional design/film practice. FLUX understands it as plain English, and it is a necessary scene-building toolkit — use it deliberately in prompts. The official documentation does not confirm these specific constructions; do not cite them as official.

## 1. The 60-30-10 rule (color hierarchy)

Basic design and photography rule: 60% of the frame — dominant color, 30% — secondary, 10% — accent.

- **Dominant** — 60% of the frame. Fill it with: background, environment, large areas (sky, walls, ground). In FLUX JSON: the 1st hex in `color_palette`; usually muted/neutral.
- **Secondary** — 30% of the frame. Fill it with: the main subject, middle ground. In FLUX JSON: the 2nd hex in `color_palette`.
- **Accent** — 10% of the frame. Fill it with: a small high-saturation object (weapon, light, detail). In FLUX JSON: `strictly in color #HEX` in that subject's `description`.

Rules:
- Maximum **3 roles by area** (60-30-10 is the law). One role may hold multiple hex codes: the subject role carries dress + hair + accessory, the environment role carries wall + floor + sky, the accent role carries one or two small objects.
- **The `color_palette` length: floor three, hard cap seven.** Three is the minimum — one hex per 60-30-10 role; a gradient background adds its endpoint hexes, each extra subject can carry its own. It equals the number of distinct colors anchored in prose (SKILL.md rule 2): typically 3–5, up to 7 for complex brand or multi-subject scenes. If the scene needs more than 7 distinct colors, merge the minor shades into prose without separate hex or simplify the scene — do not exceed 7.
- The `color_palette` order is the hierarchy: dominant first, accent last; within a role, order by area share (largest first).
- The accent is always attached to a **small** object ("use #HEX somewhere" — never). The accent slot is never empty: if the scene has no natural small accent object, name a small one — a light source, a detail, a prop — and anchor its hex there.
- Dominant — muted neutral; all saturation lives in the accent.
- **Attention follows saturation and value.** The eye lands on the most saturated / brightest area — keep exactly one such area per frame and put the accent color there. A background element more saturated than the subject pulls attention off the subject.
- Two accents allowed if together they do not exceed ~10% visually (two or more full-strength accents make the frame muddy).

Ready phrasings:
- `a desaturated #HEX environment dominating the frame, with a small #HEX accent`
- `most of the frame in muted <X>, a vivid <Y> accent strictly in color #HEX`

## 2. Harmony schemes (color wheel)

Rule: **one harmony scheme per prompt** — like one framing technique.

- **Monochromatic** — construction: 1 hue + tints/shades. Effect: harmony, single mood: pink — coziness, cold blue — isolation.
- **Complementary** — construction: 2 opposite colors (blue-orange, red-green, yellow-purple). Effect: maximum contrast, the subject "pops" out of the frame.
- **Split-complementary** — construction: base + 2 neighbors of the opposite. Effect: contrast without harsh tension; **teal & orange is exactly this** (base — skin).
- **Analogous** — construction: 3 adjacent hues. Effect: calm, nature; no hue contrast between parts, separation by light.
- **Triadic** — construction: 3 equidistant, one dominant. Effect: vivid graphic.
- **Tetradic** — construction: 2 complementary pairs. Effect: rich, refined.
- **Discordant accent** — construction: muted palette + 1 "foreign" color. Effect: attention on an element.

Scheme to mood (quick pick):
- Warm dominant (amber/orange) — coziness, energy, closeness
- Cold dominant (blue/teal) — calm, distance, cold
- Neutral dominant (gray/beige) — elegance, minimalism; all emotion carried by the accent
- Saturated dominant — graphics/art; careful, it "shouts"

## 3. Skin tone line (why teal & orange works)

All human skin lies in a narrow orange hue arc (on a vectorscope — the "skin tone line"). The complement of skin is cyan/teal. The arc is the same for every skin tone — light to dark skin sits on the same orange line; vary the value (lightness), not the hue. Default for frames with people (a mood that dictates otherwise — warm golden hour, vintage film — overrides it):
- environment/background: the complement of skin (cool teal/blue),
- faces and warm objects (fire, candles, skin): warm,
- skin stays natural — not painted along with the environment ("the background goes teal, the face does not").

Ready phrasings:
- `cool desaturated teal environment, warm natural skin tones, warm amber highlights`
- `faces stay warm and natural against a cool blue world`

## 4. Light ratios (contrast)

**Key:fill** — ratio of key light to fill:

- `2:1` — soft, low contrast, open frame. Use for: product, commercial, daylight, a "clean" look.
- `4:1` — form and modeling + readable shadow detail. Use for: classic portrait, drama.
- `8:1+` — deep shadows, high contrast. Use for: noir, thriller, horror.

FLUX phrasings:
- `key-to-fill ratio of 4:1, soft fill lifting the shadows`
- `dramatic 8:1 key-to-fill contrast, deep shadow detail preserved`
- `low-contrast 2:1 lighting, soft open shadows`

**Subject:background** — separation by exposure:
- `subject lit two stops brighter than the background`
- `background falls into darkness, subject lifted by warm rim light`
- the subject 1–3 stops brighter than the background — this is what separates the subject from the scene and gives depth

Guideline: a low ratio gives a bright, safe, commercial look; a high ratio gives a cinematic, dramatic, threatening one.

## 5. Color temperature (Kelvin) — typical values from film practice

- `2000 K` — candles. In the frame: warmest, intimate, flicker.
- `2700 K` — warm tungsten, incandescent lamps. In the frame: cozy interior.
- `3200 K` — tungsten (warm standard). In the frame: studio warmth, hearth, fire.
- `4300 K` — mixed. In the frame: neutral-warm, "homey".
- `5600 K` — daylight (neutral standard). In the frame: neutral day.
- `7500 K` — overcast sky, blue hour. In the frame: cold, tense.
- `10000+ K` — deep blue, moonlight, shadows. In the frame: coldest, night, isolation.

Rules:
- **No more than 2 temperatures in the frame** — warm and cold; each with a visible source (fire below + sky above).
- Warm reads as closeness, nostalgia, comfort; cold reads as distance and clinical chill.
- Write temperature directly in `lighting`: `warm 2700K firelight from below, cool 7500K dusk light from above`.

## 7. Light direction — what each direction does

The direction options (front, side, back, overhead, below) name the position but not the effect. Effect mapping from professional practice, plain English:

- `front light` (from behind the camera) — flattens: even skin, minimal texture, minimal shadows. Use for: clean product, even ID-style light. FLUX phrasing: `soft even frontal light, minimal shadows`
- `45° key light` — the volume default: form and modeling without drama; the portrait/product classic (the official Rembrandt scheme is this direction). FLUX phrasing: `key light at 45 degrees`
- `side light (90°)` — sculpts: rakes across texture (brick, fabric, skin), splits the frame. Use for: drama, texture-forward scenes. FLUX phrasing: `strong side light raking across the texture`
- `backlight / rim light` — separates: a bright edge around the subject against the background; the strong version is a full silhouette. FLUX phrasing: `golden hour backlighting, rim light on the hair`
- `overhead / top light` — dramatizes: deep shadows under the brow, nose and chin; noon sun or an industrial lamp. FLUX phrasing: `harsh overhead light, deep shadows under the brow`
- `light from below` (fire, screens) — unnatural: campfire-warm or eerie. A deliberate choice, not a default. FLUX phrasing: `warm 2700K firelight from below`

Heuristic: from behind the camera — flattens; from the side — sculpts; from behind the subject — separates; from above — dramatizes.

## 8. Shadows and bounce light

- **A shadow is not black — it is ambient light.** The shadow area lost the key light but still receives the ambient/bounce light, so its color is the color of that light. Name the tint instead of leaving gray: `cool blue-tinted shadows` (daylight), `warm amber shadows` (firelight).
- **Daylight rule:** the sun is warm, the sky is the fill — shadows read cool: `warm sunlight, cool blue-tinted shadows`. One of the strongest realism cues in a photo prompt.
- **Dead black** is a noir/thriller tool (8:1+, §4). In a daylight frame pure black shadows read as a hole: lift them — `shadows lifted by bounce light, detail preserved`.
- **Bounce takes the color of the surface it reflects from:** sand, brick, skin → warm bounce; snow, water, glass → cool bounce. Name the surface: `warm bounce from the brick wall lifting the shadow side of the face`.
- Consistency: every shadow tint must match a named source (the sky, the fire, the wall) — the same rule as temperatures (§5): every tint has a source.

FLUX phrasings:
- `warm sunlight, cool blue-tinted shadows, detail preserved in the shadows`
- `soft ambient fill lifting the shadows, detail preserved`
- `warm bounce from the sand lifting the shadow side of the face`

## 11. Lighting Physics: The SQTSI Framework

To achieve professional output, the AI must stop using vague terms ("dramatic light") and instead construct the `lighting` field using the **SQTSI physics framework**.

**The SQTSI Formula:** `[Source] → [Quality] → [Temperature] → [Shadow] → [Interaction]`

#### 1. S — Source (Where does the light come from?)
Avoid "artificial light"; specify the tool.
- **Natural:** `Direct midday sun`, `Golden hour sun`, `Overcast sky`, `Moonlight`, `Dappled sunlight through leaves`.
- **Artificial (Studio):** `Large Octabox`, `Beauty dish`, `Single bare strobe`, `Ring light`, `Softbox with grid`.
- **Practical (In-scene):** `Flickering neon tube`, `Warm desk lamp`, `Burning torch`, `LED strips`, `Computer screen glow`.

**Always name the position of the source:** `frontal`, `45° side key`, `90° side (split)`, `backlit`, `overhead`, `from below`. Each position has a specific effect — see `color-light.md §7`.

#### 2. Q — Quality (How "hard" is the light?)
Determined by the size of the source relative to the subject.
- **Soft (Large source):** `Soft diffused light`, `Wrap-around illumination`, `Low-contrast transitions`. (Used for beauty, soft mood).
- **Hard (Small source):** `Harsh direct light`, `Sharp-edged illumination`, `Specular highlights`. (Used for drama, texture, grit).

#### 3. T — Temperature (What is the color of the light?)
Refer to `§5` for Kelvin values.
- **Warm:** `2700K-3500K (Tungsten/Golden Hour)`, `warm amber glow`, `candlelight`.
- **Neutral:** `5000K-5500K (Daylight)`, `neutral white`, `clean studio white`.
- **Cool:** `6500K+ (Overcast/Blue Hour)`, `steely blue`, `clinical cold white`.

#### 4. S — Shadow (What happens where there is no light?)
Describe the depth and edge of the shadows.
- **Deep/Hard:** `High-contrast chiaroscuro`, `pitch-black shadows`, `razor-sharp shadow edges`.
- **Soft/Open:** `Gentle shadow gradients`, `open shadows with high fill`, `soft transition to darks`.

#### 5. I — Interaction (How does the light hit the subject?)
The "finish" of the lighting.
- **Rim/Edge:** `Sharp rim light separating subject from background`, `glowing contours`.
- **Bounce:** `Light bouncing off a white floor`, `indirect reflected fill`.
- **Volumetric:** `Light rays visible through haze (Tyndall effect)`, `atmospheric beams`.
- **Specular:** `Bright pin-point reflections on wet surfaces`, `sharp glints in the eyes`.

---

#### Technical Implementation: Converting "Styles" to Physics
When the user asks for a "style" of lighting, the AI must translate it into the SQTSI formula:

- **"Rembrandt Lighting"** $\rightarrow$ `Source: 45° key light (softbox) → Quality: soft → Temp: 4000K → Shadow: dramatic triangle on the cheek → Interaction: high-contrast separation`.
- **"Film Noir"** $\rightarrow$ `Source: Single hard practical source → Quality: harsh → Temp: neutral → Shadow: deep pitch-black, razor-sharp edges → Interaction: high-contrast chiaroscuro`.
- **"Cyberpunk Neon"** $\rightarrow$ `Source: Multiple neon tubes (magenta/cyan) → Quality: mixed soft/hard → Temp: dual-tone cool → Shadow: colorful fill → Interaction: strong specular reflections on rain-slicked surfaces`.
- **"High-Key Beauty"** $\rightarrow$ `Source: Large overhead softbox + white reflectors → Quality: ultra-soft → Temp: 5500K → Shadow: nearly nonexistent (open) → Interaction: wrap-around glow, flawless skin`.

**Cross-Reference:** Always check `color-light.md` for the **Key:Fill Ratio** (e.g., 4:1 for drama, 1:1 for flat) and include it at the end of the `lighting` field.
