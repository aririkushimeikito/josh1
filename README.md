# Isabelle Joseph, DNP — Website

Squarespace 7.1 / Fluid Engine design build for **IsabelleJosephDNP.com**, plus a
static high-fidelity preview of that design.

| What | Where |
|---|---|
| **Live site (GitHub Pages)** | https://aririkushimeikito.github.io/josh1/ |
| Squarespace build guide (architecture, design system, page specs, build map, responsive strategy, SEO map, content requirements) | [`SQUARESPACE-BUILD-GUIDE.md`](SQUARESPACE-BUILD-GUIDE.md) |
| Static site (served by GitHub Pages from the repo root; also deployable to Netlify) | `index.html`, `about/`, `tox/`, … `images/`, `assets/` |
| Site generator + all page copy | [`tools/build_site.py`](tools/build_site.py), [`tools/content.py`](tools/content.py) |
| Netlify config + 301 redirects from the old site URLs | [`netlify.toml`](netlify.toml) |

## Preview site

The site is plain HTML + one CSS file + SVG placeholder images, generated into the repo root. No JavaScript, no frameworks.
Every section is a 1:1 stand-in for a native Squarespace Fluid Engine section so the
design can be rebuilt inside Squarespace exactly as previewed.

```bash
python3 tools/build_site.py          # regenerates the site pages from tools/content.py
python3 -m http.server
```

## Replacing placeholder images

Every placeholder is an SVG in `images/` whose caption says what photo belongs
there. Drop a JPG, PNG, or WebP with the **same name** into `images/` (for example
`images/home-hero.jpg`) and run `python3 tools/build_site.py`. The build picks up the
photo automatically, removes the placeholder caption, and deletes the unused SVG.

## External systems

- Booking: Skin Clique — `https://book.skinclique.com/webstoreNew/services/97d1c710-b934-4863-a258-42d8dce92b9c`
- Shop: Skin Clique — `https://shop.skinclique.com/?provider=97d1c710-b934-4863-a258-42d8dce92b9c`

The site never recreates booking or checkout; both are external CTAs.
