# Changelog

What changed in SYNTAX, newest first. The version is in `VERSION` and shown on every page; `build.py` stops if `VERSION` and the newest entry here disagree. To add an entry: raise `VERSION` (the middle number for something people can use, the last for a fix), add a section at the top with the same number and the date, and build.

## 0.6.2 — 17 October 2026

- The README is the documentation: what SYNTAX is, the words, the rules every syntax keeps, the syntax file field by field with an example, how the family mark is drawn, every address the site serves, how to add a syntax, and how to build and deploy. Its table of syntaxes is written by the build, from the same list the site is.
- Badges at the top of the README, drawn by the build in SYNTAX's colours so the version and the number of syntaxes cannot fall behind: version, syntaxes, licence, site, names, left out, AI, build, analytics. None counts stars, downloads or visitors.
- The life syntax's page shows its note, which says an animal holds every part of it in full. The build had been reading past it.

## 0.6.1 — 17 October 2026

- Link previews: every page carries Open Graph and Twitter tags, with an image in the site's look, the mark on the dark field and the name on the cream sheet. The home page and the list of syntaxes use SYNTAX's own; each syntax's page uses one with its family mark. `og.py` draws them into `og/`, and the build refuses a syntax that has none.

## 0.6.0 — 17 October 2026

- The fifth syntax, **framework**: a framework, broken into stance, pool, rooms, access and count, each read from the Museum of Vestigial Desire's own texts. It is read from the Museum's `framework-syntax.json`, and the Museum is its instance. What it leaves out says what its texts do not settle: voice, a pool other than a uniform one, and whether rooms belong to every framework.

## 0.5.1 — 17 October 2026

- The personhood syntax says in so many words that things are excluded and animals are partially excluded: an animal holds intent, and is excluded from language, judgement and residue.

## 0.5.0 — 17 October 2026

- The fourth syntax, **life**: an animal's life, broken into place, food, action, body and signal, each either the animal's own or taken by use. An animal holds every part of it. It is read from Split-Domain Cognition's `life-syntax.json`, and its instance is the animal-rights variant.
- Personhood is partial for an animal: in the personhood syntax an animal holds intent and no other part.
- Every syntax's page has a *Left out* section: what the syntax does not describe, or who cannot hold a part of it, said in words and read from the syntax's own source, so an exclusion is never only an absence from a list. The build refuses a syntax that does not state it.
- A holder that is not a person, a model or code, is marked as a *thing*: it holds a part only as a tool a person set up, and has no personhood. *Left out* and *thing* join the words on the home page.

## 0.4.0 — 17 October 2026

- The third syntax, **personhood**: a piece of work in which language work and judgement work are both in play, broken into intent, language, judgement and residue, each held by one of the person, other people, a model under negotiation, or code. It is read from Split-Domain Cognition's `personhood-syntax.json`. Its instances are Split-Domain Cognition, and Koher as its child.

## 0.3.1 — 17 October 2026

- The record syntax's instance links to Zariia's simulator, now live, as well as to zariia.org.

## 0.3.0 — 17 October 2026

- The second syntax, **record**: a record with two channels in one file, broken into open channel, sealed channel and class. It is read from Zariia's `website/record-syntax.json`, so the two never differ. Zariia is its instance.
- SYNTAX is licensed CC BY 4.0: the full text is in `LICENSE`, and every page's footer says so.
- Every page's footer links the source on GitHub, and the home page links the changelog and the roadmap there.
- Every syntax has a mark in the SYNTAX family, made by the build from the syntax itself: one row per element type, three cells a row, one lit in each row at a place set by the syntax's name, and the last row's lit cell warm. A syntax's page shows its mark and name in the dark column, the list of syntaxes shows each one's mark, and each is served as `/<syntax>/mark.svg`.
- A syntax's page opens with two sentences instead of one, so a description containing a colon no longer runs into the counts.

## 0.2.3 — 17 October 2026

- Syntaxes in the navigation opens its own page, /syntaxes/, listing every syntax. Before this it jumped to a section of the home page and looked as though it went nowhere.

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
