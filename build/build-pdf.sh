#!/usr/bin/env bash
# Lights, Camera, Action! — build a 6×9 print/distributable PDF from the Markdown source.
#
#   ./build/build-pdf.sh            -> build/Lights-Camera-Action.pdf
#
# Pipeline:  docs/*.md  --pandoc-->  Typst markup  --(book.typ template)-->  PDF
#
# The Markdown in docs/ stays the single source of truth. Re-run this any time
# the manuscript changes. The 6 HTML form-sheets in Part Four (hero sheet,
# quest tracker, cast/places sheets, moves cheatsheet, world-forge worksheet)
# are intentionally EXCLUDED — they are designed printables, best printed from
# the website. Everything else (Parts 1–3 + prose Part Four) is included.

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DOCS="$ROOT/docs"
BUILD="$ROOT/build"
CONTENT="$BUILD/content.typ"

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

# Files per Part, in reading order (paths relative to docs/).
# Keep these arrays in sync with nav: in mkdocs.yml when chapters change.
FRONT=( foreword.md )
PART1=( part-one/00-introduction.md part-one/01-build-your-world.md \
        part-one/02-create-your-hero.md part-one/03-start-your-quest.md \
        part-one/04-the-roll.md part-one/05-playing-the-game.md \
        part-one/06-your-first-session.md )
PART2=( part-two/00-introduction.md part-two/07-the-roll.md \
        part-two/08-challenges.md part-two/09-readiness.md \
        part-two/10-quests-and-the-antagonist-track.md part-two/11-ask-the-oracle.md \
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
        part-four/teaching-the-game.md part-four/design-notes.md )

md2typ() { # $1 = docs-relative path -> append Typst markup to $CONTENT
  "$PANDOC" "$DOCS/$1" -f gfm -t typst --wrap=preserve >> "$CONTENT"
  printf '\n\n' >> "$CONTENT"
}

md2typ_intro() { # like md2typ, but drop the leading H1 so the part-intro doesn't
                 # duplicate the part-divider title that immediately precedes it
  sed '1{/^#\{1,2\} /d;}' "$DOCS/$1" | "$PANDOC" -f gfm -t typst --wrap=preserve >> "$CONTENT"
  printf '\n\n' >> "$CONTENT"
}

emit_part() { # $1 kicker, $2 title, rest = files (first file is the part intro)
  local kicker="$1" title="$2"; shift 2
  printf '#part-divider("%s", "%s")\n\n' "$kicker" "$title" >> "$CONTENT"
  local intro="$1"; shift
  md2typ_intro "$intro"
  for f in "$@"; do md2typ "$f"; done
}

echo "→ assembling content.typ"
printf '#import "lib.typ": *\n\n' > "$CONTENT"
for f in "${FRONT[@]}"; do md2typ "$f"; done
emit_part "Part One"   "Your First Game"          "${PART1[@]}"
emit_part "Part Two"   "Playing the Game, In Depth" "${PART2[@]}"
emit_part "Part Three" "Building Your World"       "${PART3[@]}"
emit_part "Part Four"  "Reference & Tools"         "${PART4[@]}"

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

echo "→ compiling PDF with Typst"
"$TYPST" compile --root "$ROOT" ${MODE_INPUT[@]+"${MODE_INPUT[@]}"} "$BUILD/book.typ" "$OUT"

echo "✓ built $OUT"
