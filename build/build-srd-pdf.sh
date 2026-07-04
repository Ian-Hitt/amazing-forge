#!/usr/bin/env bash
# Lights, Camera, Action! — build the standalone System Reference Document PDF.
#
#   ./build/build-srd-pdf.sh            -> build/Lights-Camera-Action-SRD.pdf
#   ./build/build-srd-pdf.sh print      -> build/Lights-Camera-Action-SRD-print.pdf
#
# Pipeline:  docs/part-four/rules-reference.md
#              --srd-preprocess.py-->  markdown w/ move-card markers
#              --pandoc-->             Typst markup
#              --marker rewrite-->     #lca-move(...) card calls
#              --(srd.typ template)--> PDF
#
# The web SRD is the single source of truth; re-run this whenever it changes.
# Shares fonts, colors (lib.typ), and typography with the full-book build.

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$ROOT/docs/part-four/rules-reference.md"
BUILD="$ROOT/build"
CONTENT="$BUILD/content-srd.typ"

MODE_INPUT=()
OUT="$BUILD/Lights-Camera-Action-SRD.pdf"
if [[ "${1:-}" == "print" ]]; then
  MODE_INPUT=(--input mode=print)
  OUT="$BUILD/Lights-Camera-Action-SRD-print.pdf"
  echo "→ PRINT mode (ink-black / neutral gray, B&W-priced interior)"
fi

PANDOC="$(command -v pandoc || echo /opt/homebrew/bin/pandoc)"
TYPST="$(command -v typst || echo /opt/homebrew/bin/typst)"
PYTHON="$(command -v python3 || echo /usr/bin/python3)"

echo "→ assembling content-srd.typ"
printf '#import "lib.typ": *\n\n' > "$CONTENT"
"$PYTHON" "$BUILD/srd-preprocess.py" < "$SRC" \
  | "$PANDOC" -f gfm -t typst --wrap=preserve >> "$CONTENT"

# Rewrite the move-card markers into #lca-move(...) calls. The markers arrive as
# plain-text paragraphs from Pandoc: %%%LCAMOVE|name|when%%% … %%%LCAEND%%%.
echo "→ rewriting move-card markers into #lca-move cards"
"$PYTHON" - "$CONTENT" <<'PY'
import re, sys
path = sys.argv[1]
text = open(path, encoding="utf-8").read()
# name/when are already Pandoc-safe Typst content (e.g. Devil\'s, ---), so pass
# them as content [ ... ], not strings (which would choke on \' escapes).
text = re.sub(
    r'%%%LCAMOVE\|(.*?)\|(.*?)%%%',
    lambda m: f'#lca-move(name: [{m.group(1)}], when: [{m.group(2)}])[',
    text,
)
text = text.replace('%%%LCAEND%%%', ']')
# Intra-document cross-references (#link(<label>)[text]) point at MkDocs anchor
# slugs that don't line up with Pandoc's heading labels. In a standalone booklet
# we don't need them clickable — unwrap fully to the visible text (a bare [text]
# left inline would render literal brackets in Typst).
# External links (#link("http…")[text]) are left untouched.
text = re.sub(r'#link\(<[^>]*>\)\[([^\[\]]*)\]', r'\1', text)
open(path, "w", encoding="utf-8").write(text)
PY

# Print-friendly glyph substitutions (mirror build-pdf.sh).
echo "→ substituting print-friendly glyphs"
sed -i '' \
  -e 's/✅/#good[✓]/g' \
  -e 's/❌/#bad[✗]/g' \
  "$CONTENT"

# Widen tables to full measure (mirror build-pdf.sh): first col auto, rest 1fr.
echo "→ widening tables to full measure"
sed -i '' \
  -e 's/align(center)\[#table(/align(left)[#table(/g' \
  -e 's/columns: 2,/columns: (auto, 1fr),/g' \
  -e 's/columns: 3,/columns: (auto, 1fr, 1fr),/g' \
  -e 's/columns: 4,/columns: (auto, 1fr, 1fr, 1fr),/g' \
  -e 's/columns: 5,/columns: (auto, 1fr, 1fr, 1fr, 1fr),/g' \
  "$CONTENT"

echo "→ compiling PDF with Typst"
"$TYPST" compile --root "$ROOT" --font-path "$BUILD/fonts" --ignore-system-fonts \
  ${MODE_INPUT[@]+"${MODE_INPUT[@]}"} "$BUILD/srd.typ" "$OUT"

echo "✓ built $OUT"
