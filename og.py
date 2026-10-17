"""Draw SYNTAX's link-preview images: og/home.png and one og/<syntax>.png per syntax, 1200 x 630.
Run from this folder after adding or changing a syntax: python3 og.py   (build.py refuses a syntax without one)

Each image is a small page in the site's own look, the mark alone on the dark field and the name on the cream
sheet, rendered by headless Chrome. CHROME may name the browser; otherwise the usual places are tried.
"""
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

import build  # builds the site and gives the syntaxes, the marks and the version

HERE = Path(__file__).resolve().parent
OUT = HERE / "og"
OUT.mkdir(exist_ok=True)
CHROME = os.environ.get("CHROME") or next(
    (c for c in ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                 shutil.which("google-chrome") or "", shutil.which("chromium") or ""] if c and Path(c).exists()), None)
if not CHROME:
    raise SystemExit("No Chrome found: set CHROME to the browser's path")

FONTS = (HERE / "fonts").as_uri()
e = build.e


def card(mark, kicker, name, line):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face {{ font-family: "Mukta"; font-weight: 400; src: url({FONTS}/mukta-400.woff2); }}
@font-face {{ font-family: "Mukta"; font-weight: 600; src: url({FONTS}/mukta-600.woff2); }}
@font-face {{ font-family: "Mukta"; font-weight: 800; src: url({FONTS}/mukta-800.woff2); }}
html, body {{ margin: 0; width: 1200px; height: 630px; background: #0a1428; font-family: "Mukta", sans-serif; }}
.page {{ display: grid; grid-template-columns: 440px 1fr; height: 630px; }}
.field {{ display: flex; align-items: center; justify-content: center; }}
.field svg {{ height: 420px; width: auto; max-width: 340px; }}
.sheet {{ background: #f8f4ec; margin: 32px 32px 32px 0; border-radius: 6px; padding: 56px; display: flex;
  flex-direction: column; justify-content: center; color: #0a1428; }}
.kicker {{ font-weight: 600; font-size: 22px; letter-spacing: 0.08em; text-transform: uppercase; color: #1848c0; }}
.name {{ font-weight: 800; font-size: 96px; line-height: 1; margin-top: 16px; }}
.line {{ font-size: 32px; line-height: 1.3; margin-top: 24px; }}
.url {{ font-weight: 600; font-size: 22px; letter-spacing: 0.08em; margin-top: auto; }}
</style></head><body><div class="page"><div class="field">{mark}</div>
<div class="sheet"><span class="kicker">{e(kicker)}</span><span class="name">{e(name)}</span>
<span class="line">{e(line)}</span><span class="url">syntax.prayasabhinav.net</span></div></div></body></html>"""


cards = {"home": card(build.MARK, "Kinds of things, broken into parts", "SYNTAX",
                      f"{len(build.SYNTAXES)} syntaxes, each one kind of thing broken into element types and elements")}
for s in build.SYNTAXES:
    n_el = sum(len(t["elements"]) for t in s["element_types"])
    cards[s["slug"]] = card(build.family_mark(s), "a syntax", s["name"],
                            f"{len(s['element_types'])} element types and {n_el} elements")

with tempfile.TemporaryDirectory() as tmp:
    for slug, html in cards.items():
        src = Path(tmp) / f"{slug}.html"
        src.write_text(html)
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--window-size=1200,630",
                        "--virtual-time-budget=2000", f"--user-data-dir={tmp}/profile",
                        f"--screenshot={OUT / (slug + '.png')}", src.as_uri()],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("drew", OUT / f"{slug}.png")
