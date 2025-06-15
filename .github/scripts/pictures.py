#!/usr/bin/env python3
import re
import sys
from pathlib import Path

ROOT_DIR = Path("public")
WIDTHS   = [320, 640, 1024]

# Matches <img … src=… …> capturing:
#   1) all attrs up to the '>' (so we can re-emit them verbatim),
#   2) the URL, whether in double-quotes, single-quotes, or unquoted.
IMG_RE = re.compile(
    r'<img'                              # opening tag
    r'([^>]*?'                           #   any attrs (lazy)
        r'src='                            #   the src=
        r'(?:'                             #   begin non-capturing group for three cases
            r'"([^"]*)"'                    #     1. double-quoted URL  → group 2
        r'|'                               #     or
            r"\'([^\']*)\'"                 #     2. single-quoted URL → group 3
        r'|'                               #     or
            r'([^ \t\r\n>]+)'               #     3. unquoted URL      → group 4
        r')'                               #   end non-capturing
    r'[^>]*?)'                           #   any trailing attrs
    r'>',                                # close tag
    re.IGNORECASE
)

# Split out <footer>…</footer> (with any attributes, multiline-safe)
FOOTER_RE = re.compile(r'(<footer[^>]*>.*?</footer>)', re.IGNORECASE | re.DOTALL)

def wrap_img(m):
    attrs = m.group(1)
    src = m.group(2) or m.group(3) or m.group(4) # pick whichever group matched the URL
    base = re.sub(r'\.[^./]+$', "", src) # strip file-extension
    out = ["<picture>"]
    for w in WIDTHS:
        webp = f"{base}-{w}.webp"
        out.append(
            f'<source srcset="{webp}" '
            f'type="image/webp" '
            f'media="(max-width: {w}px)">'
        )

        avif = f"{base}-{w}.avif"
        out.append(
            f'<source srcset="{avif}" '
            f'type="image/avif" '
            f'media="(max-width: {w}px)">'
        )

    out.append(f"<img{attrs}>") # re-emit the original <img…> (attrs already include src=… etc)
    out.append("</picture>")
    return "".join(out)

def process_file(path: Path):
    html = path.read_text(encoding="utf-8")
    parts = FOOTER_RE.split(html)
    for i in range(0, len(parts), 2):
        parts[i] = IMG_RE.sub(wrap_img, parts[i])

    new_html = "".join(parts)
    path.write_text(new_html, encoding="utf-8")
    print(f"Processed {path}")

def main():
    for f in ROOT_DIR.rglob("*.html"):
        process_file(f)

if __name__ == "__main__":
    main()
