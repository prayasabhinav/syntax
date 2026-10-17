# Changelog

What changed in SYNTAX, newest first. The version is in `VERSION` and shown on every page; `build.py` stops if `VERSION` and the newest entry here disagree. To add an entry: raise `VERSION` (the middle number for something people can use, the last for a fix), add a section at the top with the same number and the date, and build.

## 0.2.2 — 17 October 2026

- No syntax is named by the site's own frame. The navigation is Home and Syntaxes, so it stays the same however many syntaxes there are; the definitions on the home page no longer take their examples from the board game syntax; and a syntax's page takes its wording from that syntax's own name and source.

## 0.2.1 — 17 October 2026

- Every page has a navigation bar at the top of the sheet: Home, then each syntax by name, the current one marked. Before this the only ways home were the mark, which did not look like a link, and a small line of text.

## 0.2.0 — 17 October 2026

- A look and a mark. The mark is three element types, three cells each, with one element chosen from each type: two in cobalt, one in warm light. The site sets the mark alone on the dark ground and everything to read on a cream sheet beside it, stacked on a phone. Brand files are in `brand/`.
- One typeface, Mukta, served from the site itself, so a visit makes no request to anyone else.
- The index lists each syntax as a block; the board games described in a syntax are listed as blocks too.

## 0.1.0 — 17 October 2026

- SYNTAX begins: the words (syntax, element type, element, entity, instance), a site that lists the syntaxes, and the first syntax, **board game**, read from boardgameBuilder, its first instance.
- A syntax is named by the primary name of the kind of thing it breaks up; the build refuses any other name.
