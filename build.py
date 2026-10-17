"""Build SYNTAX's site and its syntax files. Run from this folder: python3 build.py

Each syntax is read from the instance that holds it, never copied by hand: the board-game syntax comes from
boardgameBuilder's palette.py and block_meta.py. It is written to site/<name>.json (the syntax as data)
and site/<name>/index.html (the syntax as a page). The build stops if VERSION and the newest entry in
CHANGELOG.md disagree, or if a syntax is not named by a primary name.
"""
import html
import json
import re
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
    "slug": "board-game",
    "breaks_up": "a board game, or any game played at a table with things at hand",
    "element_types": [{
        "name": d["display"],
        "holds": "several" if d.get("multi") else "one",
        "description": d["description"],
        "elements": [{"name": b["display"], "description": meta_for(b["id"])["description"]} for b in d["blocks"]],
    } for d in palette.DIMENSIONS],
    "instances": [{"name": "boardgameBuilder", "url": TOOL_URL,
                   "what": f"a tool for designing a board game from these elements, with a public wiki of what each combination tends to produce ({WIKI_URL})"}],
    "described_entities": [{"name": g["title"].split(" — ")[0], "url": f"{TOOL_URL}/#games/{g['id']}"} for g in games],
}]

for s in SYNTAXES:
    if not PRIMARY_NAME.match(s["name"]):
        sys.exit(f"'{s['name']}' is not a primary name: name a syntax for the kind of thing it breaks up")

e = html.escape
STYLE = (HERE / "style.css").read_text()


def page(title, body):
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="SYNTAX breaks kinds of things into element types and elements, so that each thing of that kind can be described, compared and made from the same parts.">
<style>{STYLE}</style>
</head>
<body>
<header><a class="name" href="/">SYNTAX</a><span class="v">v{VERSION}</span></header>
<main>{body}</main>
<footer><p>SYNTAX is a project of <a href="https://prayasabhinav.net">Prayas Abhinav</a>. No analytics and no counters.</p></footer>
</body>
</html>
"""


for s in SYNTAXES:
    types = "".join(
        f"""<section class="type"><h3>{e(t['name'])} <span class="holds">holds {t['holds']}</span></h3>
<p class="aside">{e(t['description'])}</p>
<dl>{''.join(f'<dt>{e(x["name"])}</dt><dd>{e(x["description"])}</dd>' for x in t['elements'])}</dl></section>"""
        for t in s["element_types"])
    inst = "".join(f'<li><a href="{e(i["url"])}">{e(i["name"])}</a>: {e(i["what"])}</li>' for i in s["instances"])
    ents = ", ".join(f'<a href="{e(x["url"])}">{e(x["name"])}</a>' for x in s["described_entities"])
    n_el = sum(len(t["elements"]) for t in s["element_types"])
    body = f"""<p class="crumb"><a href="/">Syntaxes</a></p>
<h1>The {e(s['name'])} syntax</h1>
<p class="lede">It breaks up {e(s['breaks_up'])} into {len(s['element_types'])} element types and {n_el} elements. A board game described in it is one choice of elements from each type.</p>
<h2>Instances</h2><ul>{inst}</ul>
<h2>Element types and elements</h2>{types}
<h2>Board games described in it</h2><p>{ents}</p>
<p class="aside">The syntax as data: <a href="/{s['slug']}.json">{s['slug']}.json</a>. It is read from boardgameBuilder each time this site is built, so the two never differ.</p>"""
    out = HERE / "site" / s["slug"]
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(page(f"The {s['name']} syntax · SYNTAX", body))
    (HERE / "site" / f"{s['slug']}.json").write_text(json.dumps(s, indent=1, ensure_ascii=False) + "\n")

rows = "".join(
    f'<li><a href="/{s["slug"]}/">{e(s["name"])}</a>: {len(s["element_types"])} element types, '
    f'{sum(len(t["elements"]) for t in s["element_types"])} elements; instance {", ".join(e(i["name"]) for i in s["instances"])}</li>'
    for s in SYNTAXES)
index = f"""<h1>SYNTAX</h1>
<p class="lede">A kind of thing can be broken into the same parts every time. SYNTAX writes those parts down: the element types a kind of thing has, and the elements of each type. Once they are written, each thing of that kind can be described as a choice of elements, compared with others, and made by choosing differently.</p>
<h2>The words</h2>
<dl class="words">
<dt>syntax</dt><dd>how one kind of thing breaks into element types and elements. A syntax is named by the primary name of the kind of thing: <em>board game</em>.</dd>
<dt>element type</dt><dd>one group of parts every thing of that kind has, such as <em>victory condition</em>. It holds one element or several.</dd>
<dt>element</dt><dd>one part, such as <em>race to finish</em>.</dd>
<dt>entity</dt><dd>one particular thing of that kind, described as its choice of elements: Pig is a board game of <em>push your luck</em>, <em>race to finish</em> and <em>take turns</em>, among others.</dd>
<dt>instance</dt><dd>a tool built on a syntax. boardgameBuilder is an instance of the board game syntax.</dd>
</dl>
<h2>Syntaxes</h2>
<ul>{rows}</ul>
<p class="aside">Version {VERSION}. What changed, and what comes next, is kept with the project's source.</p>"""
(HERE / "site" / "index.html").write_text(page("SYNTAX", index))
print(f"built SYNTAX {VERSION}: {len(SYNTAXES)} syntax(es)")
