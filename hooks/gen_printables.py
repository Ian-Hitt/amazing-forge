"""Generate docs/part-four/all-printables.md from the individual printable sheets.

Each printable (Moves, Hero, Story Arc, Challenge, Worldbuilding, Cast, Places) is a
self-contained card with its own <style> block. Several share class names
(.af-sheet, .af-log, .af-hint, ...) with different values, so they can't simply be
concatenated onto one page. This hook reads each sheet, scopes its CSS under a unique
#pa-<slug> wrapper, and stitches them into one page with a "Print all sheets" button
and a page break between sheets — so a single Print/Save-as-PDF yields every sheet.

It runs in on_config (before MkDocs scans files), writing only when the content
changed so `mkdocs serve` doesn't loop. If anything goes wrong it falls back to a
simple page of links, so the site build never fails over this convenience page.
"""

import os
import re

# (slug, on-screen heading) in print order.
SHEETS = [
    ("moves-cheatsheet", "Moves Cheatsheet"),
    ("hero-sheet", "Hero Sheet"),
    ("story-arc-tracker-sheet", "Story Arc Tracker"),
    ("challenge-tracker-sheet", "Challenge Tracker"),
    ("world-forge-worksheet", "Worldbuilding Worksheet"),
    ("cast-sheet", "Cast Sheet"),
    ("places-sheet", "Places Sheet"),
]

OUT_REL = "part-four/all-printables.md"


def _strip_comments(css):
    return re.sub(r"/\*.*?\*/", "", css, flags=re.S)


def _parse(css):
    """Split CSS into top-level blocks: ('at', prelude, body) or ('rule', selectors, body)."""
    tokens, seg, i, n = [], "", 0, len(css)
    while i < n:
        c = css[i]
        if c == "{":
            prelude = seg.strip()
            depth, j = 1, i + 1
            while j < n and depth:
                if css[j] == "{":
                    depth += 1
                elif css[j] == "}":
                    depth -= 1
                j += 1
            body = css[i + 1 : j - 1]
            tokens.append(("at" if prelude.startswith("@") else "rule", prelude, body))
            seg, i = "", j
        else:
            seg += c
            i += 1
    return tokens


def _scope(css, prefix):
    """Prefix every selector with `prefix`; drop site-chrome (.md-*) rules (handled globally)."""
    out = []
    for kind, pre, body in _parse(_strip_comments(css)):
        if kind == "at":
            if pre.startswith("@media"):
                out.append("%s { %s }" % (pre, _scope(body, prefix)))
            else:
                out.append("%s { %s }" % (pre, body.strip()))
            continue
        sels = []
        for s in (s.strip() for s in pre.split(",")):
            if not s or ".md-" in s:
                continue
            sels.append("%s %s" % (prefix, s))
        if sels:
            out.append("%s { %s }" % (", ".join(sels), body.strip()))
    return "\n".join(out)


def _extract(src):
    """Return (style_css, card_html) from a sheet's markdown source."""
    m = re.search(r"<style>(.*?)</style>", src, re.S)
    style = m.group(1) if m else ""
    start = src.index('<div class="af-sheet"')
    end = src.rindex("</div>") + len("</div>")
    return style, src[start:end]


GLOBAL_CSS = """<style>
.pa-toolbar { position: sticky; top: 0; z-index: 5; display: flex; align-items: center; gap: 0.9rem;
  flex-wrap: wrap; padding: 0.6rem 0; margin: 0 0 0.5rem; }
.pa-print-btn { font: inherit; font-weight: 700; cursor: pointer; border: 2px solid #d35400;
  color: #fff; background: #d35400; border-radius: 6px; padding: 0.55rem 1.1rem; }
.pa-print-btn:hover { background: #b8490a; border-color: #b8490a; }
.pa-note { font-size: 0.85rem; opacity: 0.75; }
.pa-item { margin: 1.5rem 0; }
@media print {
  .md-header, .md-tabs, .md-sidebar, .md-footer, .md-content__button, .md-nav { display: none !important; }
  .md-main__inner, .md-content { margin: 0 !important; }
  .md-content__inner { margin: 0 !important; padding: 0 !important; }
  .md-content__inner > *:not(.pa-item) { display: none !important; }
  .pa-item { margin: 0 !important; }
  .pa-item + .pa-item { break-before: page; page-break-before: always; }
}
</style>"""


def _build_markdown():
    here = os.path.dirname(os.path.abspath(__file__))
    docs = os.path.normpath(os.path.join(here, "..", "docs"))
    parts = [
        "# Print All Sheets",
        "",
        "Every printable in one place. Click **Print all sheets** below (or use your "
        "browser's Print / Save as PDF) — the site menus are hidden automatically and "
        "each sheet starts on its own page, so one print job gives you the whole set. "
        "To print just one, use that sheet's own page instead.",
        "",
        '<div class="pa-toolbar" markdown="0">'
        '<button class="pa-print-btn" onclick="window.print()">&#128424; Print all sheets</button>'
        '<span class="pa-note">Tip: enable "Background graphics" in the print dialog so the '
        "boxes and borders show.</span></div>",
        "",
        GLOBAL_CSS,
        "",
    ]
    for slug, _title in SHEETS:
        with open(os.path.join(docs, "part-four", slug + ".md"), encoding="utf-8") as f:
            style, card = _extract(f.read())
        scoped = _scope(style, "#pa-" + slug)
        parts.append(
            '<section id="pa-%s" class="pa-item">\n<style>\n%s\n</style>\n%s\n</section>'
            % (slug, scoped, card)
        )
        parts.append("")
    return "\n".join(parts) + "\n"


def _fallback_markdown():
    links = "\n".join(
        "- [%s](%s/)" % (title, slug) for slug, title in SHEETS
    )
    return (
        "# Print All Sheets\n\n"
        "Open each sheet and use your browser's Print / Save as PDF:\n\n" + links + "\n"
    )


def on_config(config):
    here = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.normpath(os.path.join(here, "..", "docs", OUT_REL))
    try:
        content = _build_markdown()
    except Exception as exc:  # never break the build over this page
        print("WARNING: gen_printables fell back to a links page: %r" % exc)
        content = _fallback_markdown()
    # Write only when changed, so `mkdocs serve` doesn't rebuild in a loop.
    existing = None
    if os.path.exists(out_path):
        with open(out_path, encoding="utf-8") as f:
            existing = f.read()
    if existing != content:
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(content)
    return config
