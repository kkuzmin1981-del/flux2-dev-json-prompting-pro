#!/usr/bin/env python3
"""Mechanical validator for FLUX.2 [dev] JSON prompts.

Checks the deterministic part of the SKILL.md final checklist (section IV,
the "Zero-Error" list). The judgment items (prose quality, one framing
technique, series consistency) stay manual -- this script covers what a
machine can check:

  - valid JSON (tolerates ```json fences and surrounding prose)
  - English-only values (rule 7)
  - negative phrasings: no / not / without / never / contractions (rule 1)
  - vague phrases: "professional photo", "good lighting" (rule 5)
  - every hex anchored in prose (subject description or scene/background)
    and repeated in the scene palette (rule 2)
  - required schema fields present (SKILL.md section III)
  - camera.lens: the single required lens field (SKILL.md section III);
    a leftover "lens-mm" is flagged as deprecated
  - aspect_ratio present (required field, SKILL.md section III); 21:9 flagged
    for a panoramic-intent check

Usage:
    python check_prompt.py prompt.json
    cat prompt.json | python check_prompt.py

Exit codes: 0 = clean (warnings possible), 1 = errors found, 2 = input error.
"""

import json
import re
import sys

REQUIRED_FIELDS = [
    "scene", "subjects", "style", "color_palette", "lighting",
    "mood", "background", "composition", "camera",
]

NEGATIVE_RE = re.compile(
    r"\b(no|not|without|never|nothing|nobody|cannot|"
    r"don't|doesn't|isn't|won't|can't)\b", re.I)

VAGUE_PHRASES = ["professional photo", "professional photograph", "good lighting"]

HEX_RE = re.compile(r"#[0-9a-fA-F]{8}\b|#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b")
WORD_RE = re.compile(r"\S+")
FENCE_RE = re.compile(r"```json\s*(.*?)```", re.S)
SUBJ_DESC_RE = re.compile(r"^\$\.subjects\[\d+\]\.description$")
SUBJ_PAL_RE = re.compile(r"^\$\.subjects\[\d+\]\.(color_palette|colors)")


def extract_json(raw):
    """Parse the input; tolerate markdown fences and surrounding prose."""
    raw = raw.strip()
    candidates = [raw]
    m = FENCE_RE.search(raw)
    if m:
        candidates.append(m.group(1))
    start, end = raw.find("{"), raw.rfind("}")
    if start != -1 and end > start:
        candidates.append(raw[start:end + 1])
    for candidate in candidates:
        try:
            return json.loads(candidate), None
        except ValueError:
            continue
    return None, "not valid JSON (no parseable object found)"


def strings_of(obj, path="$"):
    """Yield (path, text) for every string value in the JSON tree."""
    if isinstance(obj, str):
        yield path, obj
    elif isinstance(obj, dict):
        for k, v in obj.items():
            yield from strings_of(v, "%s.%s" % (path, k))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from strings_of(v, "%s[%d]" % (path, i))


def ascii_safe(text):
    """Keep console output ASCII-safe on any Windows codepage."""
    return text.encode("ascii", "replace").decode("ascii")


def main(argv):
    if len(argv) > 1:
        try:
            with open(argv[1], encoding="utf-8", errors="replace") as f:
                raw = f.read()
        except OSError as exc:
            print("input error: %s" % exc)
            return 2
    else:
        if hasattr(sys.stdin, "reconfigure"):
            sys.stdin.reconfigure(encoding="utf-8", errors="replace")
        raw = sys.stdin.read()

    data, err = extract_json(raw)
    errors, warnings, oks = [], [], []

    if err:
        errors.append(err)
    else:
        # Required schema fields (SKILL.md section III)
        missing = [f for f in REQUIRED_FIELDS if f not in data]
        if missing:
            errors.append("missing required fields: %s" % ", ".join(missing))
        else:
            oks.append("schema: all %d required fields present" % len(REQUIRED_FIELDS))

        all_strings = list(strings_of(data))

        # English only (rule 7)
        foreign = []
        for path, text in all_strings:
            bad_words = [w for w in WORD_RE.findall(text)
                         if any(ch.isalpha() and ord(ch) > 127 for ch in w)]
            if bad_words:
                foreign.append((path, bad_words[0]))
        if foreign:
            for path, word in foreign[:5]:
                errors.append('non-English text in %s: "%s" (rule 7)' % (path, ascii_safe(word)))
        else:
            oks.append("english only")

        # Negative phrasings (rule 1)
        neg_count = 0
        for path, text in all_strings:
            for m in NEGATIVE_RE.finditer(text):
                context = text[max(0, m.start() - 30):m.end() + 30].replace("\n", " ")
                errors.append('negative phrasing in %s: "...%s..." (rule 1)'
                              % (path, ascii_safe(context)))
                neg_count += 1
                if neg_count >= 5:
                    break
            if neg_count >= 5:
                break
        if neg_count == 0:
            oks.append("no negative phrasings")

        # Vague phrases (rule 5)
        vague_found = False
        for path, text in all_strings:
            low = text.lower()
            for phrase in VAGUE_PHRASES:
                if phrase in low:
                    errors.append('vague phrase in %s: "%s" (rule 5)' % (path, phrase))
                    vague_found = True
        if not vague_found:
            oks.append("no vague phrases")

        # Hex attachment (rule 2)
        scene_palette = data.get("color_palette") or []
        scene_prose = [t for p, t in all_strings if p in ("$.scene", "$.background")]
        subj_desc, subj_pal = [], []
        for p, t in all_strings:
            if SUBJ_DESC_RE.match(p):
                subj_desc.append(t)
            elif SUBJ_PAL_RE.match(p):
                subj_pal.append(t)

        def contains(code, items):
            return any(code.lower() in it.lower() for it in items)

        seen_hex = set()
        for _, text in all_strings:
            for code in HEX_RE.findall(text):
                if code in seen_hex:
                    continue
                seen_hex.add(code)
                in_subject = contains(code, subj_desc) or contains(code, subj_pal)
                in_scene = contains(code, scene_prose)
                if not in_subject and not in_scene:
                    errors.append("hex %s is not anchored in any prose (rule 2)" % code)
                elif not contains(code, scene_palette):
                    errors.append("hex %s is not repeated in the scene color_palette (rule 2)" % code)
        if seen_hex:
            oks.append("hex check: %d code(s) scanned" % len(seen_hex))
            # 7-hex hard cap (SKILL.md section III). The scene palette is the
            # canonical list of the prompt's distinct colors (anchored prose
            # hex must be repeated there), so its length is the right measure.
            distinct_palette = [h.lower() for h in scene_palette if isinstance(h, str)]
            if len(set(distinct_palette)) > 7:
                warnings.append("color_palette: %d distinct hex codes - hard cap is 7 (SKILL.md section III); "
                                "merge minor shades into prose without separate hex or simplify the scene" % len(set(distinct_palette)))
        else:
            oks.append("hex check: no hex codes in the prompt")

        # Subjects (five layers, handbook.md section 0)
        subs = data.get("subjects")
        if isinstance(subs, list) and subs:
            for i, s in enumerate(subs):
                if not isinstance(s, dict):
                    continue
                if not s.get("description"):
                    errors.append("subjects[%d]: missing description" % i)
                elif not s.get("position"):
                    warnings.append('subjects[%d]: no "position" (five layers, handbook.md section 0)' % i)
        elif "subjects" in data:
            errors.append('"subjects" must be a non-empty list')

        # Camera lens (SKILL.md section III): one required `lens` field
        cam = data.get("camera", {})
        if isinstance(cam, dict):
            if not cam.get("angle"):
                warnings.append('camera: no "angle"')
            if not (cam.get("depth_of_field") or cam.get("focus")):
                warnings.append('camera: neither "depth_of_field" nor "focus"')
            if not cam.get("lens"):
                errors.append('camera: missing "lens" (single required field, SKILL.md section III)')
            if cam.get("lens-mm"):
                warnings.append('camera: "lens-mm" is deprecated - merge the focal length into "lens" (e.g. "85mm prime lens")')

        # Aspect ratio (SKILL.md section III convention)
        ALLOWED_RATIOS = ("1:1", "2:3", "3:2", "3:4", "4:3", "9:16", "16:9", "21:9")
        if data.get("aspect_ratio"):
            ratio = str(data["aspect_ratio"]).strip()
            if ratio in ALLOWED_RATIOS:
                oks.append("aspect_ratio: %s" % ratio)
                if ratio == "21:9":
                    warnings.append('aspect_ratio 21:9 - uncommon; confirm the compositional intent is panoramic '
                                    '(a cinematic or epic style alone is not a reason)')
            else:
                errors.append('aspect_ratio %r not in the allowed list %s (SKILL.md section III)' % (ratio, ", ".join(ALLOWED_RATIOS)))
        else:
            errors.append('aspect_ratio missing (required field, SKILL.md section III)')

    print("FLUX.2 JSON prompt check")
    for e in errors:
        print("[ERROR] %s" % e)
    for w in warnings:
        print("[WARN]  %s" % w)
    for o in oks:
        print("[OK]    %s" % o)
    print("result: %d error(s), %d warning(s)" % (len(errors), len(warnings)))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
