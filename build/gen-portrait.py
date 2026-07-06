#!/usr/bin/env python3
"""Redraw a PHOTO of a person as a book-style pen-and-ink sketch portrait.

Unlike gen-art.py's --ref (which treats a reference image as the STYLE to copy),
here the reference photo is the SUBJECT: we hand Gemini the photo and ask it to
redraw that person's likeness in the book's house sketch style (the shared
style_prefix from art-prompts.json), on a plain white ground. Used for the
author portrait in the foreword.

Setup: same as gen-art.py (GEMINI_API_KEY in build/.env).

Use:
    ./build/gen-portrait.py --in ~/Downloads/ian.jpg --out build/art/A1.png
    ./build/gen-portrait.py --in photo.jpg --out build/art/A1.png \\
        --subject "friendly head-and-shoulders author portrait, slight smile"
"""
from __future__ import annotations
import argparse, base64, json, os, sys, warnings
from pathlib import Path

warnings.filterwarnings("ignore")

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "build" / "art-prompts.json"
MODEL = "gemini-2.5-flash-image"


def load_dotenv() -> None:
    envf = ROOT / "build" / ".env"
    if not envf.is_file():
        return
    for line in envf.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="src", required=True, help="source photo (jpg/png)")
    ap.add_argument("--out", required=True, help="output PNG path")
    ap.add_argument("--subject", default="friendly head-and-shoulders author portrait, natural expression",
                    help="framing hint")
    ap.add_argument("--aspect", default="3:4")
    args = ap.parse_args()

    style = json.loads(MANIFEST.read_text(encoding="utf-8"))["style_prefix"]
    prompt = (
        "Redraw the PERSON in the attached reference photograph as a portrait, "
        "faithfully preserving their likeness: face shape, hairstyle, facial hair, "
        "and expression. Replace the photo's background entirely with a plain white "
        f"ground. {args.subject}. Single subject, centered.\n\n{style}\n\n"
        f"Composition: {args.aspect} aspect ratio."
    )

    try:
        from google import genai
        from google.genai import types
    except ImportError:
        print("google-genai not installed. Run: pip install google-genai", file=sys.stderr)
        return 1

    load_dotenv()
    key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not key:
        print("no API key (build/.env GEMINI_API_KEY=...)", file=sys.stderr)
        return 1
    client = genai.Client(api_key=key)

    src = Path(args.src).expanduser()
    mime = "image/png" if src.suffix.lower() == ".png" else "image/jpeg"
    photo = types.Part.from_bytes(data=src.read_bytes(), mime_type=mime)

    resp = client.models.generate_content(
        model=MODEL,
        contents=[photo, prompt],
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE"],
            image_config=types.ImageConfig(aspect_ratio=args.aspect),
        ),
    )
    data = None
    for part in resp.candidates[0].content.parts:
        inline = getattr(part, "inline_data", None)
        if inline and inline.data:
            data = inline.data
            break
    if not data:
        print("no image in response", file=sys.stderr)
        return 1
    if isinstance(data, str):
        data = base64.b64decode(data)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(data)
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
