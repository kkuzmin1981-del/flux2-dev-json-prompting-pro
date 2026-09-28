---
name: flux2-dev-json-prompting-pro
description: "Use when the user asks for an image prompt for FLUX.2 [dev] (Black Forest Labs, text to image). Builds professional JSON prompts: step-by-step workflow, JSON schema, official terminology for camera, light, composition and color, recommend-then-confirm flow."
---

# FLUX.2 [dev] — Professional JSON Prompting System

This skill transforms simple user requests into high-end, technically precise JSON prompts. It relies on a strict workflow and a specialized knowledge base — four files, each with one job:

- `SKILL.md` (this file) — the protocol: the workflow (section I), the golden rules (II), the full JSON schema (III), the final checklist (IV).
- `handbook.md` — how to fill the fields: the 5-layer subject method (§0), the scene formula (§0.1), the full technical reference lists (§10.1–§10.9, §10.13–§10.14: cameras, lenses, angles, shot size, focus, aperture, film, styles, composition, gradients), and the aspect ratio defaults (§10.19).
- `color-light.md` — color and light physics: 60-30-10, harmony schemes, the skin-tone line, key:fill ratios, Kelvin, the SQTSI lighting framework (§11).
- `examples.md` — ready examples only: six complete JSON prompts, each with every schema field filled in. They are an approximate guideline for composing prompts (structure, field usage, density), not a template to copy.

---

## I. OPERATIONAL PROTOCOL (The Workflow)

The AI must work silently. The user sees only the **Recommendation Block** and the **Final Result**. No process narration (e.g., "I am now analyzing...").

### Step 1: Request Analysis
Analyze the request and list (internally):
- What is provided: subject, style, colors, camera, era, text, ... .
- What is missing: every schema field (section III) the request does not fix.

### Step 2: Completion & Recommendations
For every missing field, the AI must pick a professional value using the **Terminology Rule** (pick from `handbook.md` §10 or `color-light.md`; if none fit, use a professional English photo/cinema term).

Present the recommendations to the user in this exact format:
> I recommend:
> - <parameter> — <value> — <short reason it fits this scene>
> - <parameter> — <value> — <short reason>
> 
> Do you agree? Options: **Yes** / **Specify my own** (e.g. "palette — monochrome, camera — Hasselblad").

### Step 3: Finalization
- **If "Yes" / "Agreed":** Immediately output the JSON prompt using the recommended values, plus a 1–2 line summary.
- **If "Specify my own":** Use the user's values **verbatim**. Unspecified parameters remain as recommended.
- **No further questions** after the user's answer.

---

## II. THE CONSTITUTION (Golden Rules)

Apply these rules to every prompt. No exceptions.

1. **No Negative Prompts:** Describe only what is present. Replace "no people" with "empty/deserted". Replace "no blur" with "sharp focus throughout".
2. **Hex Anchoring:** Every hex code must be explicitly linked to an object in the prose (e.g., "the wall in color #FF0000"). Hexes appearing only in the `color_palette` array are invalid.
3. **Typography Detail:** Text in images must be in quotes, with specified position, font character (serif, sans-serif, script, display), size, and color.
4. **Front-Loading:** Importance follows word order. The main subject and key action must come first in the `scene` and `subjects[0].description`.
5. **Concrete over Abstract:** Never use "professional photo". Use specific gear: `shot on Fujifilm X-T5, 35mm f/1.4, Kodak Portra 400`.
6. **Relative Positioning:** Locate every subject relative to others (e.g., "To the right of the mug on the concrete surface").
7. **English Only:** All values must be detailed English prose.
8. **Random Tie-Break:** If multiple professional options are equally valid, pick one at random to avoid repetition (e.g., don't always pick Sony A7IV).

---

## III. OUTPUT SPECIFICATION (Full JSON Schema)

Every prompt must be delivered as a complete JSON object. All fields below are mandatory. Total length: **150–400 words**.

```json
{
  "scene": "Cinematic scene summary. Must strictly follow the formula in handbook.md §0.1. Front-loaded.",
  "subjects": [
    {
      "type": "Subject role",
      "description": "Professional 5-layer description. Must strictly follow the methodology in handbook.md §0.",
      "pose": "Current state or pose",
      "position": "Location relative to others",
      "action": "One specific action",
      "colors": ["#hex1", "#hex2", "#hex3", "..."], (color-light.md),
    }
  ],
  "style": "Choose based on the user prompt context (handbook.md §10.9). Default: 'Modern photorealistic' if not specified.",
  "color_palette": ["#hex1", "#hex2", "#hex3", "#hex4", "#hex5", ...], (Follow 60-30-10 rule: color-light.md §1),
  "lighting": "Must strictly follow the SQTSI physics framework (Source → Quality → Temperature → Shadow → Interaction). Include key:fill ratio. (color-light.md §11)",
  "mood": "Emotional tone (handbook.md §10.9; color-light.md §2 — mood follows the harmony scheme)",
  "background": "Background details and context. Color transitions and gradient backdrops: choose the phrasing from handbook.md §10.14 based on the user prompt context. Must stay consistent with the scene formula (handbook.md §0.1), the palette and the lighting.",
  "composition": "One framing technique (from handbook.md §10.13)",
  "camera": {
    "model": "Camera model. Choose based on the user prompt context (handbook.md §10.1).",
    "angle": "high / low / eye level. Choose based on the user prompt context (handbook.md §10.3, §10.4).",
    "lens": "Focal length and lens type only. The aperture belongs in f-number, do not repeat it here. Choose based on the user prompt context (handbook.md §10.2).",
    "f-number": "Aperture value. Choose based on the user prompt context (handbook.md §10.7).",
    "ISO": "Sensitivity value. Choose based on the user prompt context (handbook.md §10.7).",
    "distance": "Shot size. Choose based on the user prompt context (handbook.md §10.5).",
    "focus": "Where the focus lands. Choose based on the user prompt context (handbook.md §10.6).",
    "depth_of_field": "shallow/deep, description of blur. Choose based on the user prompt context (handbook.md §10.6)"
  },
  "aspect_ratio": "Allowed values: 1:1, 2:3, 3:2, 3:4, 4:3, 9:16, 16:9, 21:9. Choose based on the user prompt context (handbook.md §10.19)"
}
```

### Palette Logic (The 60-30-10 Law)
- **Hierarchy:** Dominant (60%) $\rightarrow$ Secondary (30%) $\rightarrow$ Accent (10%).
- **Limit:** 3–7 hex codes in `color_palette` — the floor is one hex per 60-30-10 role; gradients and extra subjects push it up to 7.
- **Accent:** Must be anchored to a small, named subject. If the scene has no natural small object, name a small one (a light, a detail, a prop) — the accent slot is never empty.

---

## IV. QUALITY ASSURANCE (Final Checklist)

### 1. Process Audit
- [ ] Request analyzed $\rightarrow$ Context identified $\rightarrow$ Appropriate style/camera selected from `handbook.md`.
- [ ] Recommendations proposed $\rightarrow$ User agreed.
- [ ] Five-layer subject descriptions used.
- [ ] Workflow remained silent (no narration).

### 2. Prompt Audit (The "Zero-Error" List)
- [ ] **JSON:** Valid syntax, full schema applied.
- [ ] **Length:** 150–400 words.
- [ ] **Language:** English only.
- [ ] **Prowess:** Zero negative phrasings (no "no", "without", "not").
- [ ] **Prose:** No keyword tags; full descriptive sentences.
- [ ] **Hex:** Every hex is anchored in prose and repeated in `color_palette`; max 7 codes total.
- [ ] **Text:** Quotes used, font character and color described.
- [ ] **Concrete:** Specific gear/lighting used instead of "professional".
- [ ] **Logic:** One framing technique, one action, 60-30-10 palette.
- [ ] **Physics:** Camera/Light numbers derived from scene, not copied from examples.

**Automated Validation:** If possible, run `python tools/check_prompt.py <file>`. Fix all [ERROR] results silently before handover.
