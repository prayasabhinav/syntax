# SYNTAX

A kind of thing can be broken into the same parts every time. SYNTAX writes those parts down: the element types a kind of thing has, and the elements of each type. Once they are written, each thing of that kind can be described as a choice of elements, compared with others, and made by choosing differently.

Live at https://syntax.prayasabhinav.net.

## The words

- **syntax**: how one kind of thing breaks into element types and elements, named by the primary name of the kind of thing it breaks up, never by a tool or a brand.
- **element type**: one group of parts every thing of that kind has. It holds one element or several.
- **element**: one part.
- **entity**: one particular thing of that kind, described as its choice of elements.
- **instance**: a tool built on a syntax.

## Syntaxes

| Syntax | Read from | Instances |
|---|---|---|
| board game | `../boardgame-builder/palette.py`, `block_meta.py` | boardgameBuilder |

## Building and deploying

```bash
./make-tar.sh                                   # runs build.py, then packs the site
caprover deploy -n myplaceholder -a syntax -t syntax.tar
```

`build.py` reads each syntax from its instance, so the site and the instance never differ. It stops if a syntax is not named by a primary name, or if `VERSION` and the newest entry in `CHANGELOG.md` disagree.

## Files

| File | What it is |
|---|---|
| `build.py` | Reads the syntaxes, checks names and version, writes `site/` |
| `style.css` | The site's look |
| `site/` | Generated; never edited by hand |
| `Dockerfile`, `nginx.conf`, `captain-definition`, `make-tar.sh` | The deploy; nginx keeps no access log |
| `VERSION`, `CHANGELOG.md`, `ROADMAP.md` | The version, what changed, what comes next |

No analytics and no counters.
