"""Build SYNTAX's site and its syntax files. Run from this folder: python3 build.py

Each syntax is read from the instance that holds it, never copied by hand: the board-game syntax comes from
boardgameBuilder's palette.py and block_meta.py. It is written to site/<name>.json (the syntax as data)
and site/<name>/index.html (the syntax as a page). The build stops if VERSION and the newest entry in
CHANGELOG.md disagree, or if a syntax is not named by a primary name.
"""
import html
import json
import re
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BGB = HERE.parent / "boardgame-builder"
sys.path.insert(0, str(BGB))

import palette  # noqa: E402
from block_meta import meta_for  # noqa: E402
from site_config import TOOL_URL, WIKI_URL  # noqa: E402

VERSION = (HERE / "VERSION").read_text().strip()
newest = re.search(r"^## (\S+)", (HERE / "CHANGELOG.md").read_text(), re.M).group(1)
if newest != VERSION:
    sys.exit(f"VERSION is {VERSION} but the newest CHANGELOG entry is {newest}")

# A syntax is named by the primary name of the kind of thing it breaks up, in plain lower case: never a tool or a brand
PRIMARY_NAME = re.compile(r"^[a-z]+( [a-z]+)*$")

games = json.loads((BGB / "games.json").read_text())
SYNTAXES = [{
    "name": "board game",
    "read_from": "boardgameBuilder",
    "slug": "board-game",
    "breaks_up": "a board game, or any game played at a table with things at hand",
    "element_types": [{
        "name": d["display"],
        "holds": "several" if d.get("multi") else "one",
        "description": d["description"],
        "elements": [{"name": b["display"], "description": meta_for(b["id"])["description"]} for b in d["blocks"]],
    } for d in palette.DIMENSIONS],
    "instances": [{"name": "boardgameBuilder", "url": TOOL_URL,
                   "what": "a tool for designing a board game from these elements, with a public wiki of what each combination tends to produce",
                   "wiki": WIKI_URL}],
    "described_entities": [{"name": g["title"].split(" — ")[0], "url": f"{TOOL_URL}/#games/{g['id']}"} for g in games],
}]

for s in SYNTAXES:
    if not PRIMARY_NAME.match(s["name"]):
        sys.exit(f"'{s['name']}' is not a primary name: name a syntax for the kind of thing it breaks up")

e = html.escape
STYLE = (HERE / "style.css").read_text()


MARK = (HERE / "brand" / "syntax-mark.svg").read_text()


def nav(current):
    links = [("/", "Home", "home"), ("/#syntaxes", "Syntaxes", "syntaxes")]
    mark = lambda key: ' aria-current="page"' if key == current else ""
    return "".join(f'<a href="{href}"{mark(key)}>{e(text)}</a>' for href, text, key in links)


def page(title, body, current):
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="SYNTAX breaks kinds of things into element types and elements, so that each thing of that kind can be described, compared and made from the same parts.">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/fonts/mukta-400.woff2" as="font" type="font/woff2" crossorigin>
<style>{STYLE}</style>
</head>
<body>
<div class="page">
<div class="field"><a href="/">{MARK}<span class="word">SYNTAX</span></a><span class="v">Version {VERSION}</span></div>
<div class="sheet">
<nav class="nav">{nav(current)}</nav>
<main>{body}</main>
<footer><p>SYNTAX is a project of <a href="https://prayasabhinav.net">Prayas Abhinav</a>. No analytics and no counters. Set in Mukta by Ek Type (<a href="/fonts/OFL.txt">SIL Open Font License</a>).</p></footer>
</div>
</div>
</body>
</html>
"""


for s in SYNTAXES:
    types = "".join(
        f"""<section class="type"><h3>{e(t['name'])} <span class="holds">holds {t['holds']}</span></h3>
<p class="aside">{e(t['description'])}</p>
<dl>{''.join(f'<dt>{e(x["name"])}</dt><dd>{e(x["description"])}</dd>' for x in t['elements'])}</dl></section>"""
        for t in s["element_types"])
    inst = "".join(f'<li><a href="{e(i["url"])}">{e(i["name"])}</a>: {e(i["what"])} (<a href="{e(i["wiki"])}">the wiki</a>)</li>' for i in s["instances"])
    ents = "".join(f'<li><a href="{e(x["url"])}">{e(x["name"])}</a></li>' for x in s["described_entities"])
    n_el = sum(len(t["elements"]) for t in s["element_types"])
    body = f"""<h1>The {e(s['name'])} syntax</h1>
<p class="lede">It breaks up {e(s['breaks_up'])} into {len(s['element_types'])} element types and {n_el} elements. A {e(s['name'])} described in it is one choice of elements from each type.</p>
<h2>Instances</h2><ul>{inst}</ul>
<h2>Element types and elements</h2>{types}
<h2>Described in it</h2><ul class="entities">{ents}</ul>
<p class="aside">The syntax as data: <a href="/{s['slug']}.json">{s['slug']}.json</a>. It is read from {e(s['read_from'])} each time this site is built, so the two never differ.</p>"""
    out = HERE / "site" / s["slug"]
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(page(f"The {s['name']} syntax · SYNTAX", body, "syntaxes"))
    (HERE / "site" / f"{s['slug']}.json").write_text(json.dumps(s, indent=1, ensure_ascii=False) + "\n")

rows = "".join(
    f'<li><a href="/{s["slug"]}/"><span class="name">{e(s["name"])}</span>'
    f'<span class="what">{len(s["element_types"])} element types · {sum(len(t["elements"]) for t in s["element_types"])} elements · '
    f'instance: {", ".join(e(i["name"]) for i in s["instances"])}</span></a></li>'
    for s in SYNTAXES)
index = f"""<h1>Kinds of things, broken into parts</h1>
<p class="lede">A kind of thing can be broken into the same parts every time. SYNTAX writes those parts down: the element types a kind of thing has, and the elements of each type. Once they are written, each thing of that kind can be described as a choice of elements, compared with others, and made by choosing differently.</p>
<h2>The words</h2>
<dl class="words">
<dt>syntax</dt><dd>how one kind of thing breaks into element types and elements. A syntax is named by the primary name of the kind of thing it breaks up, never by a tool or a brand.</dd>
<dt>element type</dt><dd>one group of parts every thing of that kind has. It holds one element or several.</dd>
<dt>element</dt><dd>one part.</dd>
<dt>entity</dt><dd>one particular thing of that kind, described as its choice of elements.</dd>
<dt>instance</dt><dd>a tool built on a syntax. Each syntax's page names its instances and the things described in it.</dd>
</dl>
<h2 id="syntaxes">Syntaxes</h2>
<ul class="syntaxes">{rows}</ul>
<p class="aside">Version {VERSION}. What changed, and what comes next, is kept with the project's source.</p>"""
(HERE / "site" / "index.html").write_text(page("SYNTAX", index, "home"))
(HERE / "site" / "favicon.svg").write_text(MARK)
shutil.copytree(HERE / "fonts", HERE / "site" / "fonts", dirs_exist_ok=True)
print(f"built SYNTAX {VERSION}: {len(SYNTAXES)} syntax(es)")
