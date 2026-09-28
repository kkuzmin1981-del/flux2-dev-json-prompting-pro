# FLUX.2 [dev] Technical Handbook

This file contains the core methodologies and technical reference lists for building professional FLUX.2 [dev] prompts.

## Scope

The official documentation covers editing (image-to-image) use cases, but this skill builds **text-to-image** prompts only.

## §0. МЕТОДОЛОГИЯ 5-СЛОЙНОГО ОПИСАНИЯ (5-LAYER DESCRIPTION METHODOLOGY)

This is the primary tool for achieving photorealism. For every subject in the `description` field, the AI must avoid generic terms and instead construct a technically dense paragraph using these 5 layers:

1. **What (Объект):** Precise definition of the entity.
   - *Bad:* "A woman" $\rightarrow$ *Pro:* "A model with Nordic features and a sharp jawline"
2. **Material (Материал/Текстура):** Physical surface properties. This tells Flux 2 how to reflect light.
   - *Bad:* "In a dress" $\rightarrow$ *Pro:* "Wearing a gown of heavy matte silk with a subtle satin sheen"
3. **Color (Цвет + HEX):** Exact shade anchored to the object.
   - *Bad:* "Red" $\rightarrow$ *Pro:* "Deep burgundy (#800020) with cool undertones"
4. **State/Pose (Состояние/Поза):** Physicality, dynamics, or degree of wear/age.
   - *Bad:* "Standing" $\rightarrow$ *Pro:* "Captured in a slight turn of the head, shoulders relaxed and slightly raised"
5. **Position (Позиция):** Precise spatial location relative to the camera or other subjects.
   - *Bad:* "On the right" $\rightarrow$ *Pro:* "Positioned in the right third of the frame, creating negative space on the left"

**Assembled Example:**
*"A model with Nordic features, wearing a gown of heavy matte silk in deep burgundy (#800020), captured in a slight turn of the head, positioned in the right third of the frame."*

**Application rule:** layers 1–3 are mandatory for every subject; layer 4 — when there is an action/state; layer 5 — always (needed for positioning relative to other subjects).

## §0.1. МЕТОДОЛОГИЯ ОПИСАНИЯ СЦЕНЫ (SCENE DESCRIPTION METHODOLOGY)

The `scene` field is the foundation of the prompt. It must provide a high-density cinematic summary that sets the global context before the AI dives into subject details. 

**The Formula:**
`[Main Subject] → [Key Action] → [Dominant Style/Era] → [Environment & Atmosphere]`

1. **Main Subject:** Define the core entity with a professional descriptor.
   - *Bad:* "A girl" $\rightarrow$ *Pro:* "A high-fashion cyborg model"
2. **Key Action:** Describe the physical interaction or state.
   - *Bad:* "Standing" $\rightarrow$ *Pro:* "Leaning against a neon-lit rain-slicked wall"
3. **Dominant Style/Era:** Specify the aesthetic or cinematic period.
   - *Bad:* "Cyberpunk" $\rightarrow$ *Pro:* "Cinematic 80s retro-futurist style"
4. **Environment & Atmosphere:** Add atmospheric depth (weather, light, air).
   - *Bad:* "In the city" $\rightarrow$ *Pro:* "In a Tokyo alley with atmospheric haze and flickering holographic signs"

**Assembled Example:**
*"A high-fashion cyborg model leaning against a neon-lit rain-slicked wall in a cyberpunk Tokyo alley, captured in a cinematic 80s retro-futurist style, atmospheric haze and flickering holographic signs filling the background."*

## §10. Reference: cameras, lenses, angles, light, composition, color, film, styles

The sections below are the full technical reference pointed to by the schema's field notes (SKILL.md section III).

### 10.1 Cameras (for `camera.model`)

- `Sony A7IV` — `shot on Sony A7IV, clean sharp, high dynamic range`
- `Sony A7R IV` — `Shot using a Sony A7R IV with a 90mm f/2.8 macro lens, ISO 100, shutter 1/250, aperture f/2.8`
- `Hasselblad X2D` — `Shot on Hasselblad X2D, 80mm lens, f/2.8, natural lighting`
- `Canon 5D` — `Standard photographic style, versatile`
- `Canon 5D Mark IV` — `Canon 5D Mark IV, 24-70mm at 35mm, golden hour, shallow depth of field`
- `Fujifilm X-T5` — `Shot on Fujifilm X-T5, 35mm f/1.4`
- `IMAX camera` — `shot on IMAX camera`
- `Kodak camera` — `Realistic Kodak Camera Image`
- `early digital camera` — `early digital camera, slight noise, flash photography, candid, 2000s digicam style`

**Orientation by scene:**
- product / still-life, macro detail — Sony A7R IV or Hasselblad X2D
- portrait / people, natural skin tones — Fujifilm X-T5
- documentary / reportage, candid — Sony A7IV or Canon 5D Mark IV
- landscape / architecture, large-format quality — Hasselblad X2D or Fujifilm X-T5
- classic photo look, versatile — Canon 5D
- monumental epic scale — IMAX camera
- analog Kodak look, retro flash — Kodak camera
- 2000s digicam, flash, candid noise — early digital camera

### 10.2 Lenses (for `camera.lens`)

- `24mm / wide-angle lens` — wide shot
- `35mm` — documentary style
- `50mm` — neutral "eye" level
- `80mm` — medium format (Hasselblad X2D)
- `85mm` — portrait; `shallow depth of field, 85mm lens`
- `90mm f/2.8 macro` — macro shooting
- `135mm+` — tele compression
- `24-70mm (at 35mm)` — versatile zoom
- `35mm spherical lens` — fashion, spherical distortion
- `macro lens` — `shot with macro lens for sharp detail`
- `anamorphic lens` — widescreen, oval bokeh

### 10.3 Camera angles — vertical (for `camera.angle`)

- `eye level` — neutral, "as the eye sees".
- `high angle / bird's eye view` — patterns and spatial relationships.
- `low angle / worm's eye view` — subject is powerful and dominant.
- `Dutch angle (camera tilt)` — tension, psychological discomfort.
- `aerial (aerial shot)` — wide view from above.
- `ground level` — camera at ground level looking across the scene.
- `flat lay / top-down` — flat composition from above (product).

### 10.4 Camera angles — horizontal (for `camera.angle`)

**A. Subject orientation:**
- `front-facing / full face view` — sincerity, direct gaze.
- `three-quarter view` — portrait classic, depth and volume.
- `two-thirds view` — more dynamic than three-quarter.
- `profile shot` — 90°, contemplation, emotional distance.
- `back view / seen from behind` — immersion, mystery.

**B. Camera position:**
- `over-the-shoulder shot` — dialogue, depth.
- `reverse shot` — opposite perspective, same scene axis.
- `two shot` — relationship between two subjects.
- `three shot` — group dynamics.
- `POV` — "the subject's eyes", immersion.
- `Object POV` — unusual vantage point (e.g. "from inside the fridge").
- `Mirror POV` — visible in a mirror reflection.
- `tableau` — static, perfectly symmetrical, "staged" frame.

### 10.5 Shot size / distance (for `camera.distance`)

- `close up (close-up)` — detail, emotion.
- `medium shot (medium)` — default for people.
- `wide shot (wide)` — environment, context.
- `macro / extreme close-up` — extreme detail.

### 10.6 Focus and depth of field (for `camera.focus` / `camera.depth_of_field`)

- `shallow depth of field` — blurred background (f/1.4–f/2.8).
- `deep depth of field` — everything sharp (f/8–f/16).
- `Sharp focus on <object>` — focal point.
- `sharp focus throughout` — everything in focus.
- `razor-sharp subject + soft background` — high separation.
- `softly blurred <X>` — soft background elements.
- `people in the background fading` — depth perception.
- `oval bokeh` — cinematic (anamorphic lens).

### 10.7 Aperture, ISO, shutter speed (for `camera.f-number`, `camera.ISO`)

- `f/1.4–f/2.8` — shallow depth of field.
- `f/2.0` — mid aperture (common in noir).
- `f/5.6` — medium depth (fashion benchmark).
- `f/8–f/16` — deep focus.
- `ISO 100` — clean frame.
- `ISO 1600–3200` — grain, film look.
- `1/125` — dappled light.
- `1/250` — macro benchmark.

### 10.8 Film Stocks (for `style` - the aesthetic look)

- `Kodak Portra 400` — `Shot on Kodak Portra 400, natural grain, organic colors`
- `Kodak Ektachrome 64 (expired, cross-processed)` — `expired Kodak Ektachrome 64 slide film cross-processed, extreme color shifts, cyan-magenta split`
- `35mm Kodak film` — `a wide, sweeping 35mm Kodak film aerial photograph, underexposed and richly grainy`
- `35mm film` — basic film aesthetic, shallow DoF.
- `polaroid` — vintage spontaneous look.
- `sepia tone` — sepia, old photo archive.

### 10.9 Style Taxonomy (for `style`)

The AI must choose a style based on the user's prompt context using these categories. Do not mix technical gear (cameras/lenses) into the `style` field; those belong in `camera`.

#### 1. Modern Digital (Clean, Commercial, High-End)
- `Modern Digital` — clean, sharp, high dynamic range, commercial quality.
- `Modern photorealistic` — clean, natural, documentary-level realism. This is the default when the user names no style (SKILL.md section III).
- `Ultra-realistic product photography` — high-end commercial look.
- `Modern minimalist` — clean lines, neutral tones, high precision.

#### 2. Vintage & Retro (Era-based Aesthetics)
- `2000s Digicam` — early digital camera look, slight noise, candid flash photography.
- `80s Vintage` — film grain, warm color cast, soft focus, 80s photo aesthetic.
- `70s Retro` — bold colors, groovy typography, retro-saturated.
- `Early 1900s Analog` — faded, stiff poses, old family portrait look, archival.
- `Analog Film` — organic colors, natural grain.

#### 3. Cinematic & Atmospheric (Film & Mood)
- `Cinematic` — high production value, composed, painterly (e.g., "in the style of Roger Deakins").
- `Film Noir` — dramatic chiaroscuro, high contrast, moody, teal/orange grading.
- `Blade Runner 2049` — neon-drenched, teal and orange color grading, sci-fi atmosphere.
- `VHS Aesthetic` — retro VHS look, scan lines, magnetic distortion.
- `Epic Scale` — monumental, sweeping, IMAX-style cinematic vistas.

#### 4. Artistic & Stylized (Non-Photographic)
- `Artistic` — oil painting, watercolor, pencil sketch, Art Nouveau, Bauhaus.
- `Digital Art` — concept art, matte painting, octane render, 3D surrealism.
- `Illustration` — flat design, vector, comic book, anime style.

#### 5. Commercial & Editorial (High Fashion & Brand)
- `Fashion Editorial` — high-fashion, stylized poses, Vogue-style lighting and composition.
- `Beauty Photography` — soft skin, macro detail, high-key lighting.
- `Brand Identity` — strict adherence to brand colors and minimalist studio environment.

### 10.13 Composition (for `composition`)

One framing technique per prompt. Choose based on the user prompt context.

- `Leading lines`
- `Foreground layers / occlusion`
- `Symmetrical`
- `Negative space`
- `Center framing`
- `Rule of thirds`
- `Frame within frame`
- `Silhouette`
- `Diagonal composition`
- `Pattern and repetition`
- `Triangular composition`

### 10.14 Gradients (for `background`)

A gradient is a smooth color transition. FLUX renders it reliably only when the endpoints are named as hex codes attached to a specific zone or object (SKILL.md rule 2); every gradient hex is repeated in `color_palette`. Two to three colors per gradient keep it clean; more turns it muddy. The phrasings below follow the BFL prompting guide's gradient examples.

- `Linear` — straight-line transition; state the direction (top to bottom, left to right, diagonal). Phrasing: `a gradient starting with color #HEX and finishing with color #HEX, transitioning top to bottom`
- `Radial` — from a center point outward to the edges; circular or elliptical. Phrasing: `a radial gradient from #HEX at the center fading outward to #HEX at the edges`
- `Multi-stop (3+ colors)` — several color zones blending smoothly; use for sky, sunset, atmospheric depth. Phrasing: `three distinct horizontal color zones blending smoothly: the upper portion #HEX, the middle #HEX, the lowest section near the horizon #HEX`
- `Studio backdrop` — seamless paper sweep across the frame. Phrasing: `transitioning left-to-right from #HEX through #HEX into #HEX`
- `Minimal dark` — the short commercial variant for product frames. Phrasing: `dark gradient background`

### 10.19 Aspect ratios (for `aspect_ratio`)

Allowed values: 1:1, 2:3, 3:2, 3:4, 4:3, 9:16, 16:9, 21:9.

Selection defaults: when the user does not name a ratio, match it to the subject's orientation and the carrier the image will live in. The map below covers all eight allowed values with their typical cases:

- `1:1` — square carrier: avatar, icon, social post, sticker sheet, one centered product. Example: a set of stickers on a gray background (examples.md §7).
- `2:3` — tall portrait: full-body person, fashion editorial, poster, one standing product. Example: a model standing on stone steps before a chapel (examples.md §8).
- `3:2` — the photo default: general photography, landscape with a subject, any scene when nothing else fits.
- `3:4` — portrait photo: one centered subject with room above and below, the standard product frame. Example: the mug series — all three states (examples.md §1).
- `4:3` — classic landscape: e-commerce listing, desktop frame, a product group arranged left to right, interior landscape.
- `9:16` — mobile vertical: stories, reels, phone wallpaper, vertical infographic. Example: the vertical coffee infographic (examples.md §6).
- `16:9` — widescreen: cinematic still, banner, film frame, wide interior with a horizon.
- `21:9` — ultrawide panoramic: epic landscape, car on a horizon, a true panoramic composition only — a cinematic or epic style alone is not a reason (the validator flags 21:9).
