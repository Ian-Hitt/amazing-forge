#!/usr/bin/env bash
# Lights, Camera, Action! — build a 6×9 print/distributable PDF from the Markdown source.
#
#   ./build/build-pdf.sh            -> build/Lights-Camera-Action.pdf
#
# Pipeline:  docs/*.md  --pandoc-->  Typst markup  --(book.typ template)-->  PDF
#
# The Markdown in docs/ stays the single source of truth. Re-run this any time
# the manuscript changes. The 7 HTML form-sheets in Part Four (moves cheatsheet,
# hero sheet, story-arc & challenge trackers, world-forge worksheet, cast/places
# sheets) plus the generated all-printables page are intentionally EXCLUDED —
# they are designed printables, best printed from the website. Everything else
# (Parts 1–3 + prose Part Four) is included.

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DOCS="$ROOT/docs"
BUILD="$ROOT/build"
CONTENT="$BUILD/content.typ"
ART="$BUILD/art"
mkdir -p "$ART"

# Resolve an art slot to an image file if one exists (any common extension).
# Prints the root-relative path (e.g. /build/art/G3.png) or nothing.
art_path() { # $1 = slot ID
  local ext
  for ext in png jpg jpeg svg webp; do
    if [[ -f "$ART/$1.$ext" ]]; then printf '/build/art/%s.%s' "$1" "$ext"; return; fi
  done
}

# Chapter-opener banner for a chapter slug (basename w/o .md). Prefer the dealt
# per-chapter strip in build/art/openers/<slug>.png; fall back to the shared O1
# motif if the per-chapter set hasn't been generated. Prints a #chapter-opener
# call (root-relative path) or nothing.
opener_typ() { # $1 = slug
  if [[ -f "$ART/openers/$1.png" ]]; then
    printf '#chapter-opener("/build/art/openers/%s.png")' "$1"; return
  fi
  local o; o="$(art_path O1)"
  [[ -n "$o" ]] && printf '#chapter-opener("%s")' "$o"
}

# Inline art markers. Authors drop <!--art:ID|caption|height--> in the prose to
# mark a spot/diagram slot (S1, S2, F1–F7, …). It's an HTML comment, so it's
# invisible on the website; here we convert it to a %%%ART%%% sentinel that
# survives Pandoc (which would otherwise drop HTML comments). A post-assembly
# pass (rewrite_art_markers below) turns each sentinel into #art-image (if a file
# named by ID exists in build/art/) or #art-placeholder. caption/height optional.
artmark() { sed -E 's/<!--[[:space:]]*art:([^>]*)-->/%%%ART:\1%%%/g'; }

# Output mode:  (default) full color for digital  |  "print" = B&W-priced interior
MODE_INPUT=()
OUT="$BUILD/Lights-Camera-Action.pdf"
if [[ "${1:-}" == "print" ]]; then
  MODE_INPUT=(--input mode=print)
  OUT="$BUILD/Lights-Camera-Action-print.pdf"
  echo "→ PRINT mode (ink-black / neutral gray, B&W-priced interior)"
fi

PANDOC="$(command -v pandoc || echo /opt/homebrew/bin/pandoc)"
TYPST="$(command -v typst || echo /opt/homebrew/bin/typst)"
PYBIN="$ROOT/.venv/bin/python"; [[ -x "$PYBIN" ]] || PYBIN="$(command -v python3)"

# Files per Part, in reading order (paths relative to docs/).
# Keep these arrays in sync with nav: in mkdocs.yml when chapters change.
FRONT=( foreword.md )
PART1=( part-one/00-introduction.md part-one/01-build-your-world.md \
        part-one/02-create-your-hero.md part-one/03-start-your-story-arc.md \
        part-one/04-the-roll.md part-one/05-playing-the-game.md \
        part-one/06-when-youre-stuck.md part-one/07-your-first-session.md )
PART2=( part-two/00-introduction.md part-two/07-the-roll.md \
        part-two/08-challenges.md part-two/09-readiness.md \
        part-two/10-story-arcs-and-the-antagonist-track.md part-two/11-ask-the-oracle.md \
        part-two/12-running-the-game.md part-two/13-growing-your-heroes.md )
PART3=( part-three/00-introduction.md part-three/14-the-world-forge.md \
        part-three/15-genres.md \
        part-three/genres/adventure.md part-three/genres/mystery.md \
        part-three/genres/horror.md part-three/genres/sci-fi.md \
        part-three/genres/caper.md part-three/genres/drama.md \
        part-three/genres/post-apocalypse.md \
        part-three/16-cool-characters.md part-three/17-making-locations.md \
        part-three/18-making-npcs.md )
# Part Four: prose only — the 6 HTML form-sheets are excluded by design.
PART4=( part-four/00-introduction.md part-four/the-story-engine.md \
        part-four/three-act-structure.md part-four/beat-sheet.md \
        part-four/teaching-the-game.md part-four/glossary.md \
        part-four/design-notes.md )

md2typ() { # $1 = docs-relative path -> append Typst markup to $CONTENT
  case "$1" in
    part-three/genres/*.md)                     # genre files carry a plate (G1–G7)
      local base slot cap
      base="$(basename "$1" .md)"
      case "$base" in
        adventure)       slot=G1; cap="Adventure genre plate";;
        mystery)         slot=G2; cap="Mystery genre plate";;
        horror)          slot=G3; cap="Horror genre plate";;
        sci-fi)          slot=G4; cap="Sci-Fi genre plate";;
        caper)           slot=G5; cap="Caper genre plate";;
        drama)           slot=G6; cap="Drama genre plate";;
        post-apocalypse) slot=G7; cap="Post-Apocalypse genre plate";;
      esac
      md2typ_genre "$1" "$slot" "$cap"
      ;;
    *)
      local tmp op; tmp="$(mktemp)"
      artmark < "$DOCS/$1" | "$PANDOC" -f gfm -t typst --wrap=preserve > "$tmp"
      op="$(opener_typ "$(basename "$1" .md)")"
      if [[ -n "$op" ]]; then
        awk -v op="$op" '{print} /^= / && !d {print ""; print op; print ""; d=1}' "$tmp" >> "$CONTENT"
      else
        cat "$tmp" >> "$CONTENT"
      fi
      printf '\n\n' >> "$CONTENT"
      rm -f "$tmp"
      ;;
  esac
}

md2typ_genre() { # $1 file, $2 slot ID, $3 caption — opener strip then plate, after the H1
  local tmp art img op; tmp="$(mktemp)"
  artmark < "$DOCS/$1" | "$PANDOC" -f gfm -t typst --wrap=preserve > "$tmp"
  img="$(art_path "$2")"
  if [[ -n "$img" ]]; then art="#art-image(\"$img\", width: 100%, height: 4.6in)"
  else art="#art-placeholder(\"$2\", \"$3\", height: 4.6in)"; fi
  op="$(opener_typ "$(basename "$1" .md)")"
  awk -v op="$op" -v art="$art" '{print} /^= / && !done {print ""; if (op != "") {print op; print ""} print art; print ""; done=1}' "$tmp" >> "$CONTENT"
  printf '\n\n' >> "$CONTENT"
  rm -f "$tmp"
}

md2typ_intro() { # like md2typ, but drop the leading H1 so the part-intro doesn't
                 # duplicate the part-divider title that immediately precedes it
  sed '1{/^#\{1,2\} /d;}' "$DOCS/$1" | artmark | "$PANDOC" -f gfm -t typst --wrap=preserve >> "$CONTENT"
  printf '\n\n' >> "$CONTENT"
}

emit_part() { # $1 kicker, $2 title, $3 divider slot, rest = files (first = intro)
  local kicker="$1" title="$2" slot="$3"; shift 3
  local img; img="$(art_path "$slot")"
  if [[ -n "$img" ]]; then
    printf '#part-divider("%s", "%s", slot: "%s", art: image("%s", width: 86%%, height: 4.0in, fit: "contain"))\n\n' \
      "$kicker" "$title" "$slot" "$img" >> "$CONTENT"
  else
    printf '#part-divider("%s", "%s", slot: "%s")\n\n' "$kicker" "$title" "$slot" >> "$CONTENT"
  fi
  local intro="$1"; shift
  md2typ_intro "$intro"
  for f in "$@"; do md2typ "$f"; done
}

# Deal the chapter-opener strips: one banner per opener-bearing chapter (every
# file except the part intros, whose H1 is dropped), in reading order. Skipped
# gracefully if the vignette pool (build/art/V*.png) hasn't been generated — the
# opener then falls back to the shared O1 motif.
if compgen -G "$ART/V*.png" > /dev/null; then
  echo "→ dealing chapter-opener strips"
  OPENER_SLUGS=()
  for f in "${FRONT[@]}" "${PART1[@]:1}" "${PART2[@]:1}" "${PART3[@]:1}" "${PART4[@]:1}"; do
    OPENER_SLUGS+=("$(basename "$f" .md)")
  done
  ( IFS=,; "$PYBIN" "$BUILD/deal-openers.py" --slugs "${OPENER_SLUGS[*]}" )
fi

echo "→ assembling content.typ"
printf '#import "lib.typ": *\n\n' > "$CONTENT"
for f in "${FRONT[@]}"; do md2typ "$f"; done
emit_part "Part One"   "Your First Game"           D1 "${PART1[@]}"
emit_part "Part Two"   "Playing the Game, In Depth" D2 "${PART2[@]}"
emit_part "Part Three" "Building Your World"        D3 "${PART3[@]}"
emit_part "Part Four"  "Reference & Tools"          D4 "${PART4[@]}"

# Map web emoji to print-friendly colored markers. Source keeps the emoji (they
# render in color on the website); the PDF gets typographic equivalents instead.
echo "→ substituting print-friendly glyphs"
sed -i '' \
  -e 's/✅/#good[✓]/g' \
  -e 's/❌/#bad[✗]/g' \
  -e 's/🎲 */#text(fill: accent, weight: "bold")[Roll: ]/g' \
  "$CONTENT"

# Tables: Pandoc centers them and sizes columns to content. Left-align and remap
# columns to fill the text width (first col auto for the key, rest share the rest
# as 1fr so long cells wrap instead of overflowing).
echo "→ widening tables to full measure"
sed -i '' \
  -e 's/align(center)\[#table(/align(left)[#table(/g' \
  -e 's/columns: 2,/columns: (auto, 1fr),/g' \
  -e 's/columns: 3,/columns: (auto, 1fr, 1fr),/g' \
  -e 's/columns: 4,/columns: (auto, 1fr, 1fr, 1fr),/g' \
  "$CONTENT"

# Inline art-marker sentinels -> #art-image / #art-placeholder. Each %%%ART:ID|
# caption|height%%% becomes an image if build/art/ID.<ext> exists, else a labeled
# placeholder box. caption defaults to the ID; height defaults to 2.4in.
echo "→ placing inline art slots"
ROOT="$ROOT" CONTENT="$CONTENT" python3 - <<'PY'
import os, re
root, content = os.environ["ROOT"], os.environ["CONTENT"]
exts = ("png", "jpg", "jpeg", "svg", "webp")
def art_path(slot):
    for e in exts:
        p = f"/build/art/{slot}.{e}"
        if os.path.isfile(root + p):
            return p
    return None
def repl(m):
    parts = [p.strip() for p in m.group(1).split("|")]
    slot = parts[0]
    caption = parts[1] if len(parts) > 1 and parts[1] else slot
    height = parts[2] if len(parts) > 2 and parts[2] else "2.4in"
    p = art_path(slot)
    if p:
        # height caps the box (fit: contain): spots stay small & centered; wide
        # diagrams whose natural height is under the cap still fill the measure.
        return f'#art-image("{p}", width: 100%, height: {height})'
    cap = caption.replace("\\", "\\\\").replace('"', '\\"')
    return f'#art-placeholder("{slot}", "{cap}", height: {height})'
text = open(content, encoding="utf-8").read()
text, n = re.subn(r"%%%ART:(.*?)%%%", repl, text)
open(content, "w", encoding="utf-8").write(text)
print(f"  {n} inline art slot(s)")
PY

# Whole-book art slot passed as an input: the frontispiece (C2). (The chapter
# opener is now injected per-chapter after each H1; see opener_typ / md2typ.)
# When the file is absent the template draws a placeholder.
FP_IMG="$(art_path C2)"; [[ -n "$FP_IMG" ]] && MODE_INPUT+=(--input "frontispiece=$FP_IMG")

echo "→ compiling PDF with Typst"
# Hermetic fonts: embed ONLY the OFL/commercially-licensed fonts vendored in
# build/fonts/ (Montserrat, Source Serif 4, DejaVu Sans + their LICENSE-*.txt).
# --ignore-system-fonts guarantees no unlicensed macOS system font (e.g. Avenir
# Next, Iowan Old Style, Apple Color Emoji) can sneak into the embedded PDF.
"$TYPST" compile --root "$ROOT" --font-path "$BUILD/fonts" --ignore-system-fonts \
  ${MODE_INPUT[@]+"${MODE_INPUT[@]}"} "$BUILD/book.typ" "$OUT"

echo "✓ built $OUT"
