# flux2-dev-json-prompting-pro

🌐 [English](readme.md) · [Русский](readme-rus.md) · [中文](readme-chn.md)

**FLUX.2 [dev] — Professional JSON Prompting System** — a universal agent skill for any AI agent.

The skill turns simple user requests ("a coffee mug on a table", "neon night street") into technically precise, professionally composed JSON prompts for the **FLUX.2 [dev]** text-to-image model (Black Forest Labs) — with real camera, lens, lighting and color-science terminology instead of vague adjectives. You'll be surprised how different plain text prompts are from professional JSON. Dive into professional FLUX 2.

## What the skill does

- **Full JSON schema** — JSON is the structured prompt format that FLUX 2 officially understands for professional use; the model reads JSON more precisely than running text. Every field mandatory, fixed field order, `aspect_ratio` last — offered to the user as a recommendation for the aspect-ratio choice.
- **Reference-driven vocabulary** — camera bodies, lenses, angles, shot sizes, focus, apertures, ISO, film stocks, style taxonomy, composition techniques, gradient phrasings and aspect ratios are chosen from built-in reference lists, not invented on the fly.
- **Color & light physics** — 60-30-10 palette hierarchy with HEX anchoring, Kelvin color temperature, key:fill ratios and the SQTSI lighting framework (Source → Quality → Temperature → Shadow → Interaction).
- **Recommend-then-confirm** — for every missing parameter the model proposes a professional value with a short reason; the prompt is finalized only after the user agrees or overrides specific values.

## File structure

```
flux2-dev-json-prompting-pro/
├── SKILL.md              # Protocol: workflow for LLM
├── handbook.md           # Technical reference lists: how LLM fills every field
├── color-light.md        # Color & light physics: palettes, Kelvin, ratios, SQTSI
├── examples.md           # Six complete JSON prompts — output format guideline for LLM
└── tools/
    └── check_prompt.py   # Mechanical validator (Python 3, standard library only)
```

## JSON prompt format

```json
{
  "scene": "",
  "subjects": [
    {
      "type": "",
      "description": "",
      "pose": "",
      "position": "",
      "action": "",
      "colors": []
    }
  ],
  "style": "",
  "color_palette": [],
  "lighting": "",
  "mood": "",
  "background": "",
  "composition": "",
  "camera": {
    "model": "",
    "angle": "",
    "lens": "",
    "f-number": "",
    "ISO": "",
    "distance": "",
    "focus": "",
    "depth_of_field": ""
  },
  "aspect_ratio": ""
}
```

## How to use

When invoking the skill, write a plain request describing what you want. You can also write it as short bullet points:

> "Come up with a prompt and details for it. 80s style, like in a TV series: a white cop and a Black detective are partners, Miami, standing by a car, night, city lights heavily blurred, diverse colors..."

The model will then deliberate silently and propose options for every parameter you did not specify — each with a short scene-based reason — and ask for your confirmation or corrections. If everything is fine, reply "Yes" (or point out specific changes). After that, just wait for completion — the final JSON prompt will be output.

## Recommendations

It is recommended to use an LLM with strong instruction-following that doesn't cut corners. For example: Qwen 3.8, GLM, ...

## Installation

Ask your agent to install this skill into its environment, pointing it at this link.

## Usage

Depends on your AI agent. For example, for Bionic by LM Studio: `@flux2-dev-json-prompting-pro`.

## Validator checks

The prompt structure and the fields used.
