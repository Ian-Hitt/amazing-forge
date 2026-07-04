#!/usr/bin/env python3
"""Rewrite the SRD's HTML move-cards into sentinel markers Pandoc will carry
through untouched, so the SRD-PDF build can wrap them in a Typst #lca-move card.

The web SRD renders move cards via a raw-HTML <div class="lca-move"> block:

    <div class="lca-move" markdown>
    <p class="lca-move-name">The Roll <span class="lca-when">— any risky action</span></p>

    ...body markdown (lists, tables)...
    </div>

Pandoc's gfm→typst pass DROPS the wrapper and the name line, keeping only the
body. We convert each card to:

    %%%LCAMOVE|The Roll|any risky action%%%

    ...body markdown...

    %%%LCAEND%%%

The markers survive Pandoc as plain paragraphs; build-srd-pdf.sh then rewrites
them into `#lca-move(name: [...], when: [...])[ … ]` in the generated Typst.

Reads stdin, writes stdout.
"""
import re
import sys

CARD = re.compile(
    r'<div class="lca-move"[^>]*>\s*'
    r'<p class="lca-move-name">(?P<head>.*?)</p>'
    r'(?P<body>.*?)'
    r'</div>',
    re.DOTALL,
)
SPAN = re.compile(r'\s*<span class="lca-when">\s*[—-]*\s*(?P<when>.*?)</span>', re.DOTALL)


def convert(m: re.Match) -> str:
    head = m.group("head")
    when = ""
    sp = SPAN.search(head)
    if sp:
        when = sp.group("when").strip()
        head = head[: sp.start()]
    name = head.strip()
    body = m.group("body").strip()
    return f"%%%LCAMOVE|{name}|{when}%%%\n\n{body}\n\n%%%LCAEND%%%"


def main() -> None:
    text = sys.stdin.read()
    sys.stdout.write(CARD.sub(convert, text))


if __name__ == "__main__":
    main()
