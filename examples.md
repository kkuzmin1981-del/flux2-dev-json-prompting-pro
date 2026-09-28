# Examples for FLUX.2 [dev]: six complete JSON prompts

These six examples are the exact output format of this skill: complete JSON in every block, every schema field (SKILL.md section III) filled in every example. Reuse their structure, field usage, and density.

These examples show what a professionally composed FLUX.2 [dev] JSON prompt looks like: how each field is filled in, what terminology is used, what density the text carries. They are an approximate guideline for composing your own prompt, not a template to copy — reuse the structure and the way fields are written, and build the actual content from the user's request.

## 1. Studio product with exact brand hex

What it demonstrates: the 60-30-10 palette in hex (dark dominant, brand-color subject, small saturated accent), a studio SQTSI build with a 2:1 ratio, center framing, 3:4.

```json
{
  "scene": "A cobalt blue ceramic mug standing on a small vermilion ceramic coaster, thin steam rising slowly from the hot coffee inside, in a clean modern studio setup with a dark warm gray seamless backdrop, the polished dark table holding soft reflections of the mug and the softboxes, and a quiet empty space around the product built for a commercial catalogue cover page",
  "subjects": [
    {
      "type": "Main Product",
      "description": "Minimalist hand-thrown ceramic coffee mug with a fine speckled matte glaze that holds the soft studio highlights in a thin even film, strictly in color #1F4FD8 cobalt blue, its round handle turned to the right, a thin ring of dark roasted coffee visible at the rim, small natural bubbles frozen in the glaze near the base, thin steam rising slowly from the hot coffee inside, positioned on a small vermilion ceramic coaster strictly in color #E0491F at the exact center of the polished table",
      "pose": "Stationary on the coaster, handle aligned toward the right edge of the frame",
      "position": "Center of the frame, resting on the polished table in front of the dark backdrop",
      "action": "Releasing a thin ribbon of steam that drifts upward and dissolves near the rim",
      "colors": ["#1F4FD8", "#E0491F"]
    }
  ],
  "style": "Ultra-realistic product photography",
  "color_palette": ["#26221F", "#1F4FD8", "#E0491F"],
  "lighting": "Large softbox key light at 45 degrees from the front-left with a second softbox as a quiet fill, soft diffused quality with a broad even falloff, neutral 5600K studio white, gently lifted shadows with a smooth gradient sliding into the backdrop, soft specular highlights tracing the curve of the handle and a faint rim along the left edge of the mug, a slow smooth falloff from the table surface into the dark backdrop, low 2:1 key-to-fill contrast",
  "mood": "Calm, premium, precisely controlled",
  "background": "A dark warm gray seamless backdrop strictly in color #26221F fading smoothly into soft shadow below, the polished table surface catching a soft mirrored reflection of both softboxes, a faint dark ellipse under the coaster, and a gentle brightness rising behind the mug to separate it from the wall",
  "composition": "Center framing",
  "camera": {
    "model": "Sony A7R IV",
    "angle": "high angle",
    "lens": "90mm macro lens",
    "f-number": "f/5.6",
    "ISO": 100,
    "distance": "medium shot",
    "focus": "Sharp focus on the speckled glaze and the rising steam, the rim of the mug crisp at the same plane",
    "depth_of_field": "medium depth of field, the steam and the speckled glaze crisp while the backdrop falls into a smooth soft blur"
  },
  "aspect_ratio": "3:4"
}
```

## 2. Golden hour portrait

What it demonstrates: the skin-tone line (warm natural skin against a hued environment, `color-light.md` §3), natural light with Kelvin and rim/bounce in the Interaction slot, 4:1 ratio, negative space, 2:3.

```json
{
  "scene": "A woman in a deep teal linen dress standing on a dry grass hill at golden hour, the wind lifting her warm brown hair, a thin red scarf knotted at her neck, small golden grass stems bending at the edge of the frame, in a warm cinematic portrait with open sky filling most of the frame and the last low sun sinking behind the horizon",
  "subjects": [
    {
      "type": "Main Character",
      "description": "A woman with warm natural skin tones and a gentle relaxed expression, a few loose strands of hair crossing her cheekbone, her lips slightly parted in a quiet breath, wearing a deep teal linen dress strictly in color #1D5C5A with a soft matte weave that shows the fine texture of the fabric, her warm brown hair strictly in color #6B3F23 lifting in the wind, a thin red scarf strictly in color #C1272D knotted loosely at her neck, positioned in the lower left of the frame with open sky to her right",
      "pose": "Standing, body angled toward the camera, shoulders relaxed, one hand resting on the scarf",
      "position": "Lower left of the frame, open sky filling the right side",
      "action": "Watching the wind lift her hair, her eyes half closed against the warm light",
      "colors": ["#1D5C5A", "#6B3F23", "#C1272D"]
    }
  ],
  "style": "Cinematic",
  "color_palette": ["#E9C46A", "#1D5C5A", "#6B3F23", "#C1272D"],
  "lighting": "The low golden hour sun from behind-right of the subject, soft warm quality through a light haze, warm 3200K light, the low sun grazing through the grass tips and lighting them from behind, soft shadows with a warm amber tone on the far cheek, a bright golden rim tracing the hair and the right shoulder, a warm bounce from the dry grass lifting the shadow side of the face, 4:1 key-to-fill contrast",
  "mood": "Warm, intimate, free",
  "background": "An open golden sky strictly in color #E9C46A melting into a hazy horizon, the dry grass of the hill in a muted warm tone falling into soft bokeh, a thin band of brighter haze lying along the horizon line, the hillside curving gently out of focus toward the right corner",
  "composition": "Negative space",
  "camera": {
    "model": "Fujifilm X-T5",
    "angle": "eye level",
    "lens": "85mm prime lens",
    "f-number": "f/1.8",
    "ISO": 200,
    "distance": "medium shot",
    "focus": "Sharp focus on the eyes, the rim of light on the hair crisp just behind them, the scarf's knot soft just below",
    "depth_of_field": "shallow depth of field, the sky and grass dissolving into soft warm bokeh, the horizon line a smooth warm band"
  },
  "aspect_ratio": "2:3"
}
```

## 3. Modern interior with a hero object

What it demonstrates: a scene with a hero object as the subject, wide angle with deep focus, the daylight rule (warm sun, cool-tinted shadows, `color-light.md` §8), leading lines, 4:3.

```json
{
  "scene": "A slate blue boucle sofa in a modern minimalist living room, afternoon sun raking across an oak floor, a tall window wall dressed with sheer curtains, in a clean bright interior with soft moving shadows and a quiet lived-in calm, the room holding a low afternoon hush",
  "subjects": [
    {
      "type": "Main Object",
      "description": "A three-seat sofa of slate blue boucle fabric strictly in color #556B7E with a subtle looped texture that catches the raking window light, a soft pile of natural light across the seat cushions, two matching cushions slightly angled on its seat, thin natural creases across the armrests, positioned in the center of the room facing the tall window",
      "pose": "Stationary, cushions arranged with a lived-in ease",
      "position": "Center of the room, facing the window",
      "action": "A long window shadow line moving slowly across its seat",
      "colors": ["#556B7E"]
    },
    {
      "type": "Accent Object",
      "description": "A small terracotta ceramic vase strictly in color #C96F4A with a smooth matte body and two dry grass stems, standing on a low oak sideboard strictly in color #B08968 with a fine visible grain, positioned to the right of the sofa",
      "pose": "Stationary on the sideboard",
      "position": "Right of the sofa, on the sideboard",
      "action": "Catching a small bright patch of window light",
      "colors": ["#C96F4A", "#B08968"]
    }
  ],
  "style": "Modern minimalist",
  "color_palette": ["#D8CFC4", "#B08968", "#556B7E", "#C96F4A", "#5B7553"],
  "lighting": "Afternoon sun through the tall window from the left, soft quality diffused by sheer curtains, neutral-warm 4300K light, long soft shadows across the floor with a cool blue tint gathering in the far corner, a faint shaft of light visible in the dust near the window, a gentle sheen along the ceramic vase and the oak sideboard, low 2:1 key-to-fill contrast",
  "mood": "Calm, airy, quiet",
  "background": "A warm greige plaster wall strictly in color #D8CFC4 with a soft even texture, a green fiddle leaf fig in the far left corner strictly in color #5B7553 with broad glossy leaves, the tall window frame drawing its lines toward the corner, an oak floor with wide planks running toward the window, and a thin shadow line running under the sideboard",
  "composition": "Leading lines",
  "camera": {
    "model": "Hasselblad X2D",
    "angle": "eye level",
    "lens": "24mm wide-angle lens",
    "f-number": "f/8",
    "ISO": 320,
    "distance": "wide shot",
    "focus": "Sharp focus on the sofa, the window and the far wall all crisp, the fig leaves a hair softer, and the vase's matte body solid at the same depth",
    "depth_of_field": "deep depth of field, the whole room sharp from the floor line to the window"
  },
  "aspect_ratio": "4:3"
}
```

## 4. Neon night street (panoramic)

What it demonstrates: practical in-scene sources, the dual-temperature rule (warm sodium + cool neon, `color-light.md` §5), specular and rim on wet surfaces in the Interaction slot, 8:1 ratio, silhouette, 21:9 as a true panoramic frame (the only legitimate case for it).

```json
{
  "scene": "A lone pedestrian in a long charcoal coat crossing a rain-slicked city street at night, magenta and cyan neon signs glowing above a warm amber streetlamp, the glow of shop windows far down the block, in a Blade Runner 2049 style frame with atmospheric haze and wet reflections stretching across the asphalt, the far streetlights dissolving into round bokeh",
  "subjects": [
    {
      "type": "Main Character",
      "description": "A lone pedestrian in a long charcoal coat strictly in color #151A20, read as a dark silhouette with a hard edge against the glowing signs, the collar raised against the damp night air, the wool surface wet at the shoulders, captured mid-stride with the coat hem swinging, water beading on the fabric, positioned in the right third of the wet street under the neon signs",
      "pose": "Mid-stride, coat hem swinging, shoulders squared",
      "position": "Right third of the frame, under the neon signs",
      "action": "Walking across the rain-slicked street, one foot lifting from a shallow puddle, a faint splash hanging in the air",
      "colors": ["#151A20"]
    }
  ],
  "style": "Blade Runner 2049",
  "color_palette": ["#101418", "#151A20", "#FFB347", "#D81E5B", "#19B5C5"],
  "lighting": "Practical in-scene sources: a magenta neon sign and a cyan neon sign on the facades plus a warm sodium streetlamp from the left, mixed hard and soft quality with sharp specular pools from the neon, dual temperature with warm 2700K lamplight against cool 7500K neon, deep hard shadows with razor-sharp edges, the cyan sign washing the fog in a thin cold layer, bright specular reflections of both neons stretching across the wet asphalt, a cyan rim along the coat shoulder and the lamp glow hanging in the haze, 8:1 key-to-fill contrast",
  "mood": "Tense, lonely, cinematic",
  "background": "A near-black night sky and asphalt strictly in color #101418, the wet street mirroring the neon signs strictly in colors #D81E5B and #19B5C5 in long smeared streaks, the warm streetlamp strictly in color #FFB347 pooling on the left side, haze diffusing the far streetlights into soft round points of light, a row of dark shopfronts behind the pedestrian with their windows reflecting the neon",
  "composition": "Silhouette",
  "camera": {
    "model": "Sony A7IV",
    "angle": "low angle",
    "lens": "35mm prime lens",
    "f-number": "f/2.8",
    "ISO": 1600,
    "distance": "wide shot",
    "focus": "Sharp focus on the pedestrian and the neon signs, the puddle in front of the feet crisp, the sign lettering legible just behind the shoulder",
    "depth_of_field": "shallow depth of field, the far streetlights melting into round bokeh, the puddle surface glassy"
  },
  "aspect_ratio": "21:9"
}
```

## 5. Poster with rendered text

What it demonstrates: SKILL.md rule 3 in full — text in quotes, with position, font character, size, and anchored color hex — plus a second, smaller text line and an accent object, diagonal composition, 9:16.

```json
{
  "scene": "A cream coffee shop poster mounted on a weathered brick wall, the large red words 'SLOW MORNINGS' centered on its face, under soft overcast daylight with a warm glow spilling from the cafe window to the right and a vintage mustard bike leaning in the lower right corner",
  "subjects": [
    {
      "type": "Main Object",
      "description": "A matte cream paper poster strictly in color #F2E9DC with a fine paper grain, mounted flat on the brick wall, a soft even shadow lying along its right edge, its upper half carrying the large bold condensed sans-serif words 'SLOW MORNINGS' strictly in color #C0392B spanning two thirds of the poster width, and a smaller tracked-out serif line 'COFFEE - OPEN DAILY 7:00' strictly in color #3A2A1E centered below it, positioned in the center of the wall above the door frame",
      "pose": "Stationary, mounted flat on the wall",
      "position": "Center of the brick wall, above the door frame",
      "action": "Holding the soft overcast light on its matte face",
      "colors": ["#F2E9DC", "#C0392B", "#3A2A1E"]
    },
    {
      "type": "Accent Object",
      "description": "A vintage city bike with a matte mustard frame strictly in color #F4B41A, thin tires, a small leather saddle and a low handlebar, leaning against the brick wall in the lower right of the frame below the poster",
      "pose": "Leaning against the wall",
      "position": "Lower right of the frame, below and right of the poster",
      "action": "Casting a soft shadow on the sidewalk",
      "colors": ["#F4B41A"]
    }
  ],
  "style": "Modern Digital",
  "color_palette": ["#8A5A44", "#F2E9DC", "#C0392B", "#3A2A1E", "#F4B41A"],
  "lighting": "Overcast sky light from the front-left, soft even quality, neutral 5600K daylight, gentle low-contrast shadows with a cool neutral tint under the door frame, a soft sheen where the light rakes across the paper grain and the brick texture, plus a warm spill from the cafe window on the right edge, 2:1 key-to-fill contrast",
  "mood": "Cozy, inviting, calm",
  "background": "A weathered brick wall strictly in color #8A5A44 with visible mortar lines and small chips in the surface, the wall receding toward the right edge in perspective, the wooden cafe door frame on the left and a warm lit window in the upper right with a faint curtain visible behind the glass, the sidewalk in muted gray below",
  "composition": "Diagonal composition",
  "camera": {
    "model": "Canon 5D Mark IV",
    "angle": "eye level",
    "lens": "50mm prime lens",
    "f-number": "f/4",
    "ISO": 400,
    "distance": "medium shot",
    "focus": "Sharp focus on the poster face and its lettering",
    "depth_of_field": "shallow depth of field, the brick wall at the frame edges softening"
  },
  "aspect_ratio": "9:16"
}
```

## 6. Two people and a dog

What it demonstrates: a `subjects[]` array of three subjects, relative positioning (SKILL.md rule 6) in every description, two distinct actions per scene, a shared palette with per-subject hex, triangular composition, 3:2, and the style default `Modern photorealistic`.

```json
{
  "scene": "A young couple strolling through a sunlit city park, a golden retriever walking between them, the air still and warm, in a warm candid documentary frame with tall green trees, a gravel path and a wooden bench resting in the shade",
  "subjects": [
    {
      "type": "Main Character",
      "description": "A young man with short dark hair in a slate navy field jacket strictly in color #2F4858 and dark trousers, captured mid-step on the gravel path, a paper coffee cup held in one hand, positioned to the left of the woman with the dog between them",
      "pose": "Mid-step, one hand holding a paper coffee cup",
      "position": "Left of the frame center, on the gravel path",
      "action": "Handing a treat to the dog between them",
      "colors": ["#2F4858"]
    },
    {
      "type": "Main Character",
      "description": "A young woman with shoulder-length auburn hair in a rust linen midi dress strictly in color #B85C38, the dress hem swaying with her step, a small burgundy leather bag strictly in color #7A2E3B on her shoulder, captured mid-step with a relaxed smile, positioned to the right of the man with the dog between them",
      "pose": "Mid-step, shoulders relaxed",
      "position": "Right of the frame center, on the gravel path",
      "action": "Looking down at the dog",
      "colors": ["#B85C38", "#7A2E3B"]
    },
    {
      "type": "Companion Animal",
      "description": "A golden retriever with a dense coat strictly in color #C98F4E catching bright spots of sun, the fur at the ruff standing out in the light, its tail in motion, walking between the couple on the gravel path",
      "pose": "Walking, tail in motion",
      "position": "Between the couple, slightly ahead of the woman",
      "action": "Sniffing the man's outstretched hand",
      "colors": ["#C98F4E"]
    }
  ],
  "style": "Modern photorealistic",
  "color_palette": ["#4F6B4A", "#2F4858", "#B85C38", "#7A2E3B", "#C98F4E"],
  "lighting": "High midday sun through the tree canopy from above, soft dappled quality, neutral 5500K daylight, dappled leaf shadows with soft edges crossing the path and the figures, warm bounce from the gravel lifting the shadowed faces, a faint sun shaft hanging in the air above the path, 2:1 key-to-fill contrast",
  "mood": "Warm, easy, joyful",
  "background": "Tall green park trees strictly in color #4F6B4A with sunlit leaves glowing at the top, a gravel path in muted beige leading into the distance, a wooden bench under the trees on the left, grass softening at the edges of the path, the park's fence a soft line in the distance",
  "composition": "Triangular composition",
  "camera": {
    "model": "Canon 5D",
    "angle": "eye level",
    "lens": "35mm prime lens",
    "f-number": "f/2.8",
    "ISO": 200,
    "distance": "wide shot",
    "focus": "Sharp focus on the couple, the dog a hair softer",
    "depth_of_field": "shallow depth of field, the trees behind the couple softening into green bokeh"
  },
  "aspect_ratio": "3:2"
}
```
