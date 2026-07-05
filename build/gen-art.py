#!/usr/bin/env python3
"""Generate grayscale-sketch placeholder art for *Lights, Camera, Action!*

Reads build/art-prompts.json and calls the Google Gemini image model once per
slot, writing build/art/<ID>.png. build-pdf.sh then places each file into its
wired slot (dividers, genre plates, frontispiece, opener motif, inline spots).
Diagrams (F1-F7) and icons (I1) are NOT handled here — those are hand-built as
SVG. Grayscale-only by design: the print interior stays on the cheap black-ink
tier, and the sketch look reads as intentional in pure gray.

Setup:
    pip install google-genai
    export GEMINI_API_KEY=...            # from https://aistudio.google.com/apikey
                                          # (a consumer Gemini Pro sub does NOT include this)

Use:
    ./build/gen-art.py --dry-run          # print composed prompts, no API calls, no key needed
    ./build/gen-art.py                     # generate every slot that has no image yet
    ./build/gen-art.py --only G1,G3 --force
    ./build/gen-art.py --ref build/art/G1.png --only G2,G3,G4   # anchor style to an approved image
    ./build/gen-art.py --list             # list slots and whether art exists

The --ref flag is the consistency trick: generate ONE piece you like, then pass
it as a style reference so the rest of the set matches its linework.
"""
from __future__ import annotations
import argparse, base64, json, os, sys, warnings
from pathlib import Path

warnings.filterwarnings("ignore")  # hush google-auth Py3.9-EOL / LibreSSL notices

ROOT = Path(__file__).resolve().parent.parent
ART = ROOT / "build" / "art"
MANIFEST = ROOT / "build" / "art-prompts.json"

# The model. A Gemini 3.x image line is emerging and is cheaper/better; swap this
# one string when you move to it (e.g. "gemini-3-flash-image").
MODEL = "gemini-2.5-flash-image"
EXTS = ("png", "jpg", "jpeg", "svg", "webp")


def existing(slot: str) -> Path | None:
    for e in EXTS:
        p = ART / f"{slot}.{e}"
        if p.is_file():
            return p
    return None


def compose(manifest: dict, slot: str, spec: dict) -> str:
    prefix, neg = manifest["style_prefix"], manifest["negative"]
    return (
        f"{prefix}\n\nSubject: {spec['subject']}\n\n"
        f"Composition: {spec['aspect']} aspect ratio.\n"
        f"Avoid: {neg}."
    )


def load_manifest() -> dict:
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def load_dotenv() -> None:
    """Pull KEY=value lines from a gitignored build/.env into the environment,
    so the API key lives in one local file (works across shells) and is never
    committed. Real env vars still win."""
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
    ap = argparse.ArgumentParser(description="Generate placeholder art via Gemini.")
    ap.add_argument("--only", help="comma-separated slot IDs (default: all)")
    ap.add_argument("--force", action="store_true", help="regenerate even if art exists")
    ap.add_argument("--dry-run", action="store_true", help="print prompts, no API calls")
    ap.add_argument("--list", action="store_true", help="list slots and status, then exit")
    ap.add_argument("--ref", help="path to a reference image to anchor the sketch style")
    args = ap.parse_args()

    manifest = load_manifest()
    slots: dict = manifest["slots"]
    if args.only:
        want = [s.strip() for s in args.only.split(",")]
        unknown = [s for s in want if s not in slots]
        if unknown:
            print(f"unknown slot(s): {', '.join(unknown)}", file=sys.stderr)
            return 2
        slots = {k: slots[k] for k in want}

    if args.list:
        for slot in slots:
            got = existing(slot)
            print(f"  {slot:5} {'✓ ' + got.name if got else '· (placeholder)'}")
        return 0

    ART.mkdir(parents=True, exist_ok=True)
    targets = [s for s in slots if args.force or not existing(s)]
    skipped = [s for s in slots if s not in targets]
    if skipped:
        print(f"skipping {len(skipped)} slot(s) that already have art: {', '.join(skipped)}")
    if not targets:
        print("nothing to generate.")
        return 0

    if args.dry_run:
        for slot in targets:
            print(f"\n===== {slot}  ({slots[slot]['aspect']}) =====")
            print(compose(manifest, slot, slots[slot]))
        print(f"\n[dry-run] {len(targets)} slot(s) would be generated.")
        return 0

    # ---- real generation: lazy-import the SDK so --dry-run/--list need no deps ----
    try:
        from google import genai
        from google.genai import types
    except ImportError:
        print("google-genai not installed. Run: pip install google-genai", file=sys.stderr)
        return 1

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("no API key. Put GEMINI_API_KEY=... in build/.env or export it "
              "(key from https://aistudio.google.com/apikey)", file=sys.stderr)
        return 1
    client = genai.Client(api_key=api_key)

    ref_part = None
    if args.ref:
        ref_bytes = Path(args.ref).read_bytes()
        mime = "image/png" if args.ref.lower().endswith(".png") else "image/jpeg"
        ref_part = types.Part.from_bytes(data=ref_bytes, mime_type=mime)
        print(f"style reference: {args.ref}")

    ok = 0
    for slot in targets:
        spec = slots[slot]
        prompt = compose(manifest, slot, spec)
        if ref_part is not None:
            prompt = "Match the exact art style, linework, and shading of the reference image.\n\n" + prompt
        contents = [ref_part, prompt] if ref_part is not None else [prompt]
        try:
            resp = client.models.generate_content(
                model=MODEL,
                contents=contents,
                config=types.GenerateContentConfig(
                    response_modalities=["IMAGE"],
                    # aspect_ratio lives on ImageConfig in current SDKs; if your
                    # installed version rejects it, the prompt also states the ratio.
                    image_config=types.ImageConfig(aspect_ratio=spec["aspect"]),
                ),
            )
            data = None
            for part in resp.candidates[0].content.parts:
                inline = getattr(part, "inline_data", None)
                if inline and inline.data:
                    data = inline.data
                    break
            if not data:
                print(f"  {slot}: no image in response (skipped)", file=sys.stderr)
                continue
            if isinstance(data, str):  # some SDK paths return base64 text
                data = base64.b64decode(data)
            out = ART / f"{slot}.png"
            out.write_bytes(data)
            print(f"  {slot}: wrote {out.relative_to(ROOT)}")
            ok += 1
        except Exception as e:  # keep going; one bad slot shouldn't kill the batch
            print(f"  {slot}: ERROR {e}", file=sys.stderr)

    print(f"\ndone: {ok}/{len(targets)} generated. Rebuild: ./build/build-pdf.sh")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
