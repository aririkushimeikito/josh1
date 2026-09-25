# -*- coding: utf-8 -*-
"""
Static site generator for the IsabelleJosephDNP.com design preview.

    python3 tools/build_site.py                 -> writes the site into the repo root (clean URLs; served by GitHub Pages / Netlify)
    python3 tools/build_site.py --flat OUTDIR   -> writes OUTDIR  (flat *.html, for hosted preview)

The generated pages are a high-fidelity preview of the Squarespace 7.1 build
described in SQUARESPACE-BUILD-GUIDE.md. Every section maps 1:1 to a native
Squarespace Fluid Engine section + native blocks. No JavaScript is used.
"""
import os, sys, html, re, shutil, datetime
sys.path.insert(0, os.path.dirname(__file__))
import content as C

FLAT = "--flat" in sys.argv
OUT = sys.argv[sys.argv.index("--flat") + 1] if FLAT else os.path.join(os.path.dirname(__file__), "..")
OUT = os.path.abspath(OUT)

# ------------------------------------------------------------------ helpers
PREFIX = ""  # relative path back to the site root for the page being rendered

def href(slug):
    """Internal link. slug '' = home. Links are relative so the site works at a domain root or a subpath."""
    if slug.startswith("http"):
        return slug
    slug, _, frag = slug.partition("#")
    frag = f"#{frag}" if frag else ""
    if FLAT:
        return ("index.html" if slug == "" else f"{slug}.html") + frag
    return (PREFIX if slug == "" else f"{PREFIX}{slug}/") + frag if (PREFIX or slug) else "./" + frag

IMAGES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "images")
REAL_EXTS = (".jpg", ".jpeg", ".png", ".webp")

def real_image(name):
    """Return the filename of a supplied photo for this placeholder name, if one exists."""
    if name in C.PHOTOS and os.path.isfile(os.path.join(IMAGES_DIR, C.PHOTOS[name][0])):
        return C.PHOTOS[name][0]
    for ext in REAL_EXTS:
        if os.path.isfile(os.path.join(IMAGES_DIR, name + ext)):
            return name + ext
    return None

def img(name):
    fn = real_image(name) or f"{name}.svg"
    return f"images/{fn}" if FLAT else f"{PREFIX}images/{fn}"

def esc(s):
    return html.escape(s, quote=True)

PH_RE = re.compile(r"\[([A-Z][A-Z0-9 /+\-—–,.'’]+)\]")
def rich(s):
    """Escape text and highlight [PLACEHOLDER] markers."""
    s = esc(s)
    return PH_RE.sub(r'<mark class="ph">[\1]</mark>', s)

def p(paras, cls=""):
    c = f' class="{cls}"' if cls else ""
    return "".join(f"<p{c}>{rich(x)}</p>" for x in paras)

def btn(label, slug, style="primary", external=None):
    url = href(slug)
    ext = external if external is not None else url.startswith("http")
    attrs = ' target="_blank" rel="noopener"' if ext else ""
    return f'<a class="btn btn--{style}" href="{url}"{attrs}>{esc(label)}</a>'

def book_btn(label="Book With Isabelle", style="primary"):
    return btn(label, C.BOOK_URL, style)

def shop_btn(label="Shop Skincare", style="secondary"):
    return btn(label, C.SHOP_URL, style)

def eyebrow(t):
    return f'<p class="eyebrow">{rich(t)}</p>' if t else ""

def figure(name, alt, cls="", focus=None):
    if name in C.PHOTOS:
        _, focus, alt = C.PHOTOS[name][0], focus or C.PHOTOS[name][1], C.PHOTOS[name][2]
    style = f' style="object-position:{focus}"' if focus else ""
    if real_image(name):
        return f'<figure class="ph-img ph-img--real {cls}"><img src="{img(name)}" alt="{esc(alt)}" loading="lazy"{style}></figure>'
    return (f'<figure class="ph-img {cls}"><img src="{img(name)}" alt="{esc(alt)}" loading="lazy" width="1200" height="1500">'
            f'<figcaption>[IMAGE TO BE PROVIDED] {esc(alt)}</figcaption></figure>')

# ------------------------------------------------------------------ sections
def section(inner, theme="cream", cls="", id_=None):
    i = f' id="{id_}"' if id_ else ""
    return f'<section class="sec sec--{theme} {cls}"{i}><div class="wrap">{inner}</div></section>'

def hero(eyebrow_t, h1, paras, ctas, image, alt, tagline=None, focus=None):
    tag = f'<p class="hero__tagline">{rich(tagline)}</p>' if tagline else ""
    # One sentence per line: break the headline after each period.
    parts = re.split(r"(?<=\.)\s+", h1.strip())
    if len(parts) > 1:
        h1_html = "<br>".join(f'<span class="h1-line">{rich(part)}</span>' for part in parts)
        h1_cls = ' class="h1--lines"'
    else:
        h1_html, h1_cls = rich(h1), ""
    return f'''
<section class="sec sec--cream hero">
  <div class="wrap hero__grid">
    <div class="hero__text">
      {eyebrow(eyebrow_t)}
      <h1{h1_cls}>{h1_html}</h1>
      {tag}
      <div class="hero__copy">{p(paras)}</div>
      <div class="cta-row">{"".join(ctas)}</div>
    </div>
    <div class="hero__media">{figure(image, alt, focus=focus).replace('loading="lazy"', 'loading="eager" fetchpriority="high"')}</div>
  </div>
</section>'''

def split(eyebrow_t, h2, paras, ctas, image, alt, reverse=False, theme="linen", sub=None, h_level=2):
    r = " split--reverse" if reverse else ""
    s = f'<p class="sub">{rich(sub)}</p>' if sub else ""
    c = f'<div class="cta-row">{"".join(ctas)}</div>' if ctas else ""
    return f'''
<section class="sec sec--{theme}">
  <div class="wrap split{r}">
    <div class="split__media">{figure(image, alt)}</div>
    <div class="split__text">
      {eyebrow(eyebrow_t)}
      <h{h_level}>{rich(h2)}</h{h_level}>
      {s}
      {p(paras)}
      {c}
    </div>
  </div>
</section>'''

def prose(eyebrow_t, h2, paras, ctas=None, theme="cream", sub=None, narrow=True, h_level=2):
    s = f'<p class="sub">{rich(sub)}</p>' if sub else ""
    c = f'<div class="cta-row">{"".join(ctas)}</div>' if ctas else ""
    n = " prose--narrow" if narrow else ""
    return section(f'''
    <div class="prose{n}">
      {eyebrow(eyebrow_t)}
      <h{h_level}>{rich(h2)}</h{h_level}>
      {s}
      {p(paras)}
      {c}
    </div>''', theme)

def feature_list(eyebrow_t, h2, intro, items, cta=None, theme="cream", sub=None, note=None, cols=2):
    rows = ""
    for i in items:
        t, d, c = i[0], i[1], (i[2] if len(i) > 2 else None)
        crow = f'<div class="cta-row">{c}</div>' if c else ""
        rows += f'<div class="feat"><h3>{rich(t)}</h3><p>{rich(d)}</p>{crow}</div>'
    s = f'<p class="sub">{rich(sub)}</p>' if sub else ""
    n = f'<p class="note">{rich(note)}</p>' if note else ""
    c = f'<div class="cta-row">{cta}</div>' if cta else ""
    return section(f'''
    <div class="sec-head">
      {eyebrow(eyebrow_t)}
      <h2>{rich(h2)}</h2>
      {s}
      {p(intro)}
    </div>
    <div class="feat-grid feat-grid--{cols}">{rows}</div>
    {n}{c}''', theme)

def steps(h2, items, cta=None, theme="linen", eyebrow_t="What to Expect"):
    rows = "".join(f'<li><div class="step__n">Step {i}</div><div><h3>{rich(t)}</h3><p>{rich(d)}</p></div></li>'
                   for i, (t, d) in enumerate(items, 1))
    c = f'<div class="cta-row">{cta}</div>' if cta else ""
    return section(f'''
    <div class="sec-head">{eyebrow(eyebrow_t)}<h2>{rich(h2)}</h2></div>
    <ol class="steps">{rows}</ol>{c}''', theme)

def checklist(h2, intro, bullets, outro, theme="cream", eyebrow_t=None, sub=None):
    li = "".join(f"<li>{rich(b)}</li>" for b in bullets)
    s = f'<p class="sub">{rich(sub)}</p>' if sub else ""
    return section(f'''
    <div class="check">
      <div class="check__text">{eyebrow(eyebrow_t)}<h2>{rich(h2)}</h2>{s}{p(intro)}</div>
      <ul class="check__list">{li}</ul>
      <div class="check__outro">{p(outro)}</div>
    </div>''', theme)

def faq(h2, items, theme="linen", eyebrow_t="FAQ", intro=None, h_level=2):
    d = "".join(f'<details class="acc"><summary><h{h_level+1}>{rich(q)}</h{h_level+1}></summary><div class="acc__body"><p>{rich(a)}</p></div></details>'
                for q, a in items)
    i = p(intro) if intro else ""
    return section(f'''
    <div class="faq">
      <div class="faq__head">{eyebrow(eyebrow_t)}<h{h_level}>{rich(h2)}</h{h_level}>{i}</div>
      <div class="faq__list">{d}</div>
    </div>''', theme)

def cta_band(h2, paras, ctas, theme="brown"):
    return section(f'''
    <div class="band">
      <h2>{rich(h2)}</h2>
      {p(paras)}
      <div class="cta-row">{"".join(ctas)}</div>
    </div>''', theme, "sec--band")

def results_gallery(items, h2="Real Results", intro=None, theme="linen", eyebrow_t="Before + After", cta=None):
    figs = "".join(f'<figure class="result"><img src="{img_file(f)}" alt="{esc(cap)}" loading="lazy"><figcaption>{esc(cap)}</figcaption></figure>' for f, cap in items)
    i = p(intro) if intro else ""
    c = f'<div class="cta-row">{cta}</div>' if cta else ""
    return section(f'''
    <div class="sec-head">{eyebrow(eyebrow_t)}<h2>{rich(h2)}</h2>{i}</div>
    <div class="results results--{min(len(items), 3)}">{figs}</div>
    <p class="note">{esc(C.RESULTS_NOTE)}</p>{c}''', theme)

def img_file(fn):
    return f"images/{fn}" if FLAT else f"{PREFIX}images/{fn}"

def related_pair(items, theme="cream"):
    cols = "".join(f'<div class="rel"><h2>{rich(t)}</h2>{p(ps)}<div class="cta-row">{btn(l, s, "text")}</div></div>'
                   for t, ps, (l, s) in items)
    return section(f'<div class="rel-grid">{cols}</div>', theme)

def service_groups(theme="cream", eyebrow_t="Explore Services", h2="Care Designed Around the Whole You", intro=None, ctas_per_group=True):
    groups = ""
    for gname, items in C.SERVICE_GROUPS:
        links = "".join(f'<li><a href="{href(s)}">{esc(n)}</a></li>' for n, s in items)
        anchor = {"Aesthetics": "aesthetics", "Wellness": "wellness", "Skin Health": "skin-health"}[gname]
        gcta = btn(f"Explore {gname}", f"services#{anchor}", "text") if ctas_per_group else ""
        groups += f'<div class="sg"><h3>{esc(gname)}</h3><ul class="sg__list">{links}</ul>{gcta}</div>'
    i = p(intro) if intro else ""
    return section(f'''
    <div class="sec-head">{eyebrow(eyebrow_t)}<h2>{rich(h2)}</h2>{i}</div>
    <div class="sg-grid">{groups}</div>''', theme)

# ------------------------------------------------------------------ chrome
def header():
    # Dropdown groups mirror the primary-navigation design. Group labels
    # (AESTHETICS / WELLNESS / SKINCARE) and "Services" are non-linking — no page exists.
    dd_groups = [
        ("Aesthetics", [("Tox", "tox"), ("Hyperhidrosis", "hyperhidrosis"), ("Chemical Peels", "chemical-peels")]),
        ("Wellness", [("GLP-1 Weight Management", "weight-loss"), ("Hormone Replacement Therapy", "hormone-replacement-therapy"), ("Hair Loss", "hair-loss")]),
        ("Skincare", [("Skincare Consultation", "skincare-consultations"), ("Skincare", "skincare")]),
    ]
    svc = ""
    for gname, items in dd_groups:
        svc += f'<li class="dd__group" aria-hidden="true">{esc(gname)}</li>'
        svc += "".join(f'<li><a href="{href(s)}">{esc(n)}</a></li>' for n, s in items)
    return f'''
<header class="site-header">
  <div class="wrap site-header__row">
    <a class="brand" href="{href("")}"><span class="brand__name">Isabelle Joseph, <abbr title="Doctor of Nursing Practice">DNP</abbr></span><span class="brand__sub">Concierge Aesthetics • Wellness • Skincare</span></a>
    <input type="checkbox" id="nav-toggle" class="nav-toggle" aria-label="Open menu">
    <label for="nav-toggle" class="nav-burger" aria-hidden="true"><span></span><span></span><span></span></label>
    <nav class="nav" aria-label="Primary">
      <ul class="nav__list">
        <li><a href="{href("")}">Home</a></li>
        <li><a href="{href("about")}">About</a></li>
        <li class="dd">
          <span class="dd__toggle" role="button" tabindex="0" aria-haspopup="true">Services <span class="dd__caret" aria-hidden="true">▾</span></span>
          <ul class="dd__menu">{svc}</ul>
        </li>
        <li><a href="{href("faqs")}">FAQs</a></li>
        <li><a href="{href("blog")}">The Isabelle Edit</a></li>
        <li><a href="{esc(C.SHOP_URL)}" target="_blank" rel="noopener">Shop</a></li>
        <li><a href="{esc(C.BOOK_URL)}" target="_blank" rel="noopener">Book</a></li>
      </ul>
    </nav>
  </div>
</header>'''

def footer():
    svc_links = "".join(f'<li><a href="{href(s)}">{esc(C.SERVICES[s]["name"])}</a></li>' for s in C.SERVICE_ORDER)
    return f'''
<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot__brand">
        <p class="foot__name">Isabelle Joseph, DNP, NP-BC</p>
        <p class="foot__tag">Concierge Aesthetics • Wellness • Skincare</p>
        <p class="foot__area">Serving South Easton, Norwell, Randolph, Somerset, Stoughton, Westwood + surrounding communities.</p>
        <div class="cta-row">{book_btn()}</div>
      </div>
      <div class="foot__col"><h2>Explore</h2><ul>
        <li><a href="{href("about")}">Meet Isabelle</a></li>
        <li><a href="{href("services")}">Services</a></li>
        <li><a href="{href("skincare")}">Skincare</a></li>
        <li><a href="{href("blog")}">The Isabelle Edit</a></li>
        <li><a href="{href("faqs")}">FAQs</a></li>
      </ul></div>
      <div class="foot__col"><h2>Services</h2><ul>{svc_links}<li><a href="{href("skincare")}">Prescription Skincare</a></li><li><a href="{href("skincare-consultations")}">Skincare Consultations</a></li></ul></div>
      <div class="foot__col"><h2>Connect</h2><ul>
        <li><a href="{C.BOOK_URL}" target="_blank" rel="noopener">Book With Isabelle</a></li>
        <li><a href="{C.SHOP_URL}" target="_blank" rel="noopener">Shop Skincare</a></li>
        <li><a href="{C.CONTACT["instagram_url"]}" target="_blank" rel="noopener">Instagram {esc(C.CONTACT["instagram_handle"])}</a></li>
        <li><a href="#" aria-disabled="true">Facebook <mark class="ph">[LINK TO BE PROVIDED]</mark></a></li>
        <li><a href="mailto:{C.CONTACT["email"]}">{esc(C.CONTACT["email"])}</a></li>
        <li><a href="sms:{C.CONTACT["phone"].replace("-", "")}">{esc(C.CONTACT["phone"])}</a> <span class="foot__note">({esc(C.CONTACT["phone_note"])})</span></li>
      </ul></div>
    </div>
    <div class="foot__legal">
      <p>© {datetime.date.today().year} Isabelle Joseph, DNP, NP-BC. Booking, ecommerce, and clinical infrastructure provided by Skin Clique.</p>
      <p><a href="#">Privacy Policy</a> • <a href="#">Terms</a> • <mark class="ph">[HEALTHCARE / SITE DISCLAIMER TO BE PROVIDED]</mark></p>
      <p class="foot__disc">The information on this website is for general educational purposes and is not a substitute for individualized medical advice. Treatment appropriateness is determined during a consultation with a licensed provider.</p>
    </div>
  </div>
</footer>'''

# ------------------------------------------------------------------ CSS
CSS = r"""
:root{
  --terracotta:#C17B5E; --terracotta-deep:#A9674C;
  --brown:#2C2318; --ink:#2C2318; --ink-soft:#5C4F42; --ink-muted:#8A7B6C;
  --linen:#F0EAE2; --linen-deep:#E6DCCF;
  --sage:#8A9B80; --sage-soft:#DCE2D5; --sage-deep:#6F8066;
  --cream:#FAF7F3;
  --rule:rgba(44,35,24,.14);
  --serif:"DM Serif Display",Georgia,"Times New Roman",serif;
  --sans:"DM Sans",system-ui,-apple-system,"Segoe UI",Helvetica,Arial,sans-serif;
  --wrap:1240px; --gutter:clamp(16px,5vw,64px);
  --radius:2px;
}
*{box-sizing:border-box}
.quotes>*,.journal>*,.feat-grid>*,.concern-grid>*,.products>*,.sg-grid>*,.rel-grid>*,.split>*,.hero__grid>*,.check>*,.faq>*,.foot-grid>*{min-width:0}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}*{transition:none!important}}
body{margin:0;background:var(--cream);color:var(--ink);font-family:var(--sans);font-size:clamp(16px,.35vw + 15.5px,18px);line-height:1.65;font-weight:400}
img{max-width:100%;height:auto;display:block}
a{color:inherit}
a:focus-visible,button:focus-visible,summary:focus-visible,.nav-burger:focus-visible{outline:2px solid var(--terracotta);outline-offset:3px}
h1,h2,h3,h4{font-family:var(--serif);font-weight:400;line-height:1.1;margin:0 0 .5em;color:var(--brown);text-wrap:balance;letter-spacing:-.005em}
h1{font-size:clamp(2.35rem,5.2vw,4.3rem);line-height:1.04}
h2{font-size:clamp(1.85rem,3.4vw,2.85rem)}
h3{font-size:clamp(1.25rem,1.8vw,1.55rem);margin-bottom:.35em}
p{margin:0 0 1em;max-width:68ch}
p:last-child{margin-bottom:0}
abbr{text-decoration:none}
.wrap{max-width:var(--wrap);margin-inline:auto;padding-inline:var(--gutter)}
.eyebrow{font-family:var(--sans);font-size:.74rem;letter-spacing:.16em;text-transform:uppercase;color:var(--terracotta);font-weight:600;margin:0 0 1.1rem}
.sub{font-family:var(--serif);font-size:clamp(1.2rem,1.8vw,1.5rem);color:var(--ink-soft);margin:-.2rem 0 1.2rem;line-height:1.3}
.note{font-size:.9rem;color:var(--ink-muted);margin-top:1.5rem;max-width:72ch}
mark.ph{background:rgba(193,123,94,.14);color:var(--terracotta-deep);font-family:var(--sans);font-size:.78em;font-weight:600;letter-spacing:.04em;padding:.1em .4em;border-radius:var(--radius);white-space:normal;overflow-wrap:anywhere}

/* buttons — Squarespace Primary / Secondary / Tertiary equivalents */
.btn{display:inline-block;font-family:var(--sans);font-weight:600;font-size:.84rem;letter-spacing:.09em;text-transform:uppercase;text-decoration:none;padding:1rem 1.75rem;border-radius:var(--radius);border:1.5px solid transparent;transition:background .2s,color .2s,border-color .2s,transform .2s;line-height:1.15}
.btn--primary{background:var(--terracotta);color:#fff;border-color:var(--terracotta)}
.btn--primary:hover{background:var(--terracotta-deep);border-color:var(--terracotta-deep)}
.btn--secondary{background:transparent;color:var(--brown);border-color:var(--brown)}
.btn--secondary:hover{background:var(--brown);color:var(--cream)}
.btn--light{background:transparent;color:var(--cream);border-color:rgba(250,247,243,.6)}
.btn--light:hover{background:var(--cream);color:var(--brown)}
.btn--text{background:none;border:none;padding:.8rem 0;color:var(--terracotta-deep);border-radius:0;letter-spacing:.1em;position:relative;min-height:44px}
.btn--text::after{content:"";position:absolute;left:0;right:0;bottom:.7rem;height:1.5px;background:currentColor}
.btn--text:hover{color:var(--brown)}
.cta-row{display:flex;flex-wrap:wrap;gap:.6rem 1.25rem;align-items:center;margin-top:1.5rem}

/* header — native Squarespace header equivalent */
.site-header{position:sticky;top:env(safe-area-inset-top,0px);z-index:50;background:rgba(250,247,243,.94);backdrop-filter:blur(8px);border-bottom:1px solid var(--rule)}
.site-header__row{display:flex;align-items:center;justify-content:space-between;gap:1.5rem;min-height:82px;position:relative}
.brand{text-decoration:none;display:flex;flex-direction:column;line-height:1.1}
.brand__name{font-family:var(--serif);font-size:1.45rem;color:var(--brown)}
.brand__sub{font-size:.62rem;letter-spacing:.16em;text-transform:uppercase;color:var(--ink-muted);margin-top:.25rem;white-space:nowrap}
@media (max-width:560px){.brand__sub{display:none}.brand__name{font-size:1.3rem}}
.nav__list{list-style:none;margin:0;padding:0;display:flex;align-items:center;gap:clamp(1.1rem,2vw,1.85rem);flex-wrap:nowrap}
.nav__list>li>a:not(.btn),.nav__list>li>.dd__toggle{text-decoration:none;font-size:.8rem;font-weight:500;color:var(--brown);letter-spacing:.12em;text-transform:uppercase;padding:.5rem 0;display:inline-block}
.dd__toggle{cursor:pointer;user-select:none}
.nav__list>li>a:not(.btn):hover,.nav__list>li>.dd__toggle:hover{color:var(--terracotta-deep)}
.dd{position:relative}
.dd__caret{font-size:.7em;margin-left:.15em;color:var(--ink-muted)}
.dd__menu{list-style:none;margin:0;padding:.75rem 0;position:absolute;top:100%;left:-1rem;min-width:270px;background:var(--cream);border:1px solid var(--rule);box-shadow:0 18px 40px -20px rgba(44,35,24,.35);opacity:0;visibility:hidden;transform:translateY(6px);transition:opacity .18s,transform .18s,visibility .18s}
.dd:hover .dd__menu,.dd:focus-within .dd__menu,.dd__toggle:focus + .dd__menu{opacity:1;visibility:visible;transform:none}
.dd__menu a{display:block;padding:.5rem 1.25rem;text-decoration:none;font-size:.9rem;color:var(--brown)}
.dd__menu a:hover{background:var(--linen);color:var(--terracotta-deep)}
.dd__group{padding:.75rem 1.25rem .25rem;font-size:.66rem;letter-spacing:.16em;text-transform:uppercase;color:var(--sage-deep);font-weight:600}
.nav-toggle{position:absolute;opacity:0;width:1px;height:1px;pointer-events:none}
.nav-burger{display:none;width:44px;height:44px;flex-direction:column;justify-content:center;gap:6px;cursor:pointer;padding:8px;margin-right:-8px}
.nav-burger span{display:block;height:1.5px;background:var(--brown);transition:transform .2s,opacity .2s}
@media (max-width:1100px){
  .nav-burger{display:flex}
  .nav{position:absolute;left:0;right:0;top:100%;background:var(--cream);border-bottom:1px solid var(--rule);display:none;padding:1rem var(--gutter) 2rem;max-height:calc(100vh - 82px);overflow:auto}
  .nav-toggle:checked ~ .nav{display:block}
  .nav-toggle:checked ~ .nav-burger span:nth-child(1){transform:translateY(7.5px) rotate(45deg)}
  .nav-toggle:checked ~ .nav-burger span:nth-child(2){opacity:0}
  .nav-toggle:checked ~ .nav-burger span:nth-child(3){transform:translateY(-7.5px) rotate(-45deg)}
  .nav__list{flex-direction:column;align-items:stretch;gap:0}
  .nav__list>li>a:not(.btn),.nav__list>li>.dd__toggle{font-size:.95rem;padding:1rem 0;border-bottom:1px solid var(--rule);display:block}
  .dd__caret{display:none}
  .dd__menu{position:static;opacity:1;visibility:visible;transform:none;border:0;box-shadow:none;background:transparent;padding:0 0 .75rem;min-width:0;columns:2;column-gap:1rem}
  .dd__group{break-after:avoid;padding-left:0}
  .dd__menu a{padding:.35rem 0;break-inside:avoid}
}

/* sections — one Squarespace Fluid Engine section each */
.sec{padding-block:clamp(60px,8.5vw,120px)}
.sec--cream{background:var(--cream)}
.sec--linen{background:var(--linen)}
.sec--sage{background:var(--sage-soft)}
.sec--brown{background:var(--brown);color:var(--cream)}
.sec--brown h1,.sec--brown h2,.sec--brown h3{color:var(--cream)}
.sec--brown .eyebrow{color:var(--terracotta)}
.sec--terracotta{background:var(--terracotta);color:#fff}
.sec--terracotta h2{color:#fff}
.sec+.sec--cream:not(.hero){border-top:1px solid var(--rule)}
.sec-head{max-width:760px;margin-bottom:clamp(2rem,4vw,3.5rem)}
.prose--narrow{max-width:720px}

/* hero */
.hero{padding-block:clamp(40px,6vw,88px) clamp(60px,8vw,110px)}
.hero__grid{display:grid;grid-template-columns:7fr 5fr;gap:clamp(2rem,6vw,5.5rem);align-items:center}
.hero__text{container-type:inline-size}
.hero__text h1{margin-bottom:.6em}
.hero__text h1.h1--lines{font-size:clamp(1.8rem,9.8cqw,4.3rem)}
.h1-line{white-space:nowrap}
.hero__tagline{font-family:var(--serif);font-size:clamp(1.3rem,2vw,1.7rem);color:var(--terracotta-deep);margin:-.4rem 0 1.4rem;line-height:1.25}
.hero__copy p{font-size:1.06rem;color:var(--ink-soft);max-width:56ch}
.hero__media{margin-top:clamp(0px,4vw,56px)}
.hero--service .hero__grid{grid-template-columns:6fr 5fr;align-items:start}
@media (max-width:860px){.hero__grid,.hero--service .hero__grid{grid-template-columns:1fr}.hero__media{margin-top:0;order:-1}.hero__media .ph-img{aspect-ratio:4/3}.hero__text h1.h1--lines{font-size:clamp(1.8rem,7.4cqw,3.4rem)}}

/* placeholder imagery */
.ph-img{margin:0;position:relative;aspect-ratio:4/5;overflow:hidden;border-radius:var(--radius);background:var(--linen-deep)}
.ph-img img{width:100%;height:100%;object-fit:cover}
.ph-img figcaption{position:absolute;left:0;right:0;bottom:0;padding:.55rem .9rem;font-size:.68rem;letter-spacing:.1em;text-transform:uppercase;font-weight:600;color:var(--terracotta-deep);background:rgba(250,247,243,.88)}
.ph-img--real{background:var(--linen)}
.ph-img--wide{aspect-ratio:16/10}
.ph-img--square{aspect-ratio:1}
.ph-img--tall{aspect-ratio:3/4}

/* trust bar */
.trust{display:flex;flex-wrap:wrap;justify-content:space-between;gap:1rem 2rem;padding-block:1.6rem;border-top:1px solid var(--rule);border-bottom:1px solid var(--rule);list-style:none;margin:0}
.trust li{font-size:.76rem;letter-spacing:.16em;text-transform:uppercase;font-weight:600;color:var(--ink-soft);display:flex;align-items:center;gap:.7rem}
.trust li::before{content:"";width:8px;height:8px;border-radius:50%;background:var(--sage)}
@media (max-width:700px){.trust{flex-direction:column;align-items:flex-start;gap:.75rem}}

/* editorial split */
.split{display:grid;grid-template-columns:5fr 6fr;gap:clamp(2rem,6vw,6rem);align-items:center}
.split--reverse .split__media{order:2}
.split__text p{color:var(--ink-soft)}
.split__text h2{margin-bottom:.6em}
@media (max-width:860px){.split{grid-template-columns:1fr}.split--reverse .split__media{order:0}.split__media .ph-img{aspect-ratio:4/3}}

/* feature list — editorial rows, not cards */
.feat-grid{display:grid;gap:0 clamp(2rem,5vw,4.5rem);border-top:1px solid var(--rule)}
.feat-grid--2{grid-template-columns:repeat(2,1fr)}
.feat-grid--3{grid-template-columns:repeat(3,1fr)}
.feat{padding:1.75rem 0;border-bottom:1px solid var(--rule)}
.feat p{color:var(--ink-soft);font-size:.98rem}
.feat .cta-row{margin-top:.9rem}
@media (max-width:1024px){.feat-grid--3{grid-template-columns:repeat(2,1fr)}}
@media (max-width:640px){.feat-grid--2,.feat-grid--3{grid-template-columns:1fr}}

/* steps */
.steps{list-style:none;margin:0;padding:0;display:grid;gap:0;border-top:1px solid var(--rule);max-width:900px}
.steps li{display:grid;grid-template-columns:120px 1fr;gap:1.5rem;padding:1.75rem 0;border-bottom:1px solid var(--rule)}
.step__n{font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;font-weight:600;color:var(--terracotta);padding-top:.5rem}
.steps p{color:var(--ink-soft)}
@media (max-width:600px){.steps li{grid-template-columns:1fr;gap:.4rem}}

/* checklist */
.check{display:grid;grid-template-columns:1fr 1fr;gap:clamp(2rem,5vw,5rem);align-items:start}
.check__text p{color:var(--ink-soft)}
.check__list{margin:0;padding:0;list-style:none;border-top:1px solid var(--rule)}
.check__list li{padding:.75rem 0 .75rem 1.6rem;border-bottom:1px solid var(--rule);position:relative}
.check__list li::before{content:"";position:absolute;left:0;top:1.25rem;width:8px;height:8px;border-radius:50%;background:var(--sage)}
.check__outro{grid-column:1/-1;max-width:760px;color:var(--ink-soft);padding-top:.5rem}
@media (max-width:860px){.check{grid-template-columns:1fr}}

/* FAQ topic jump links — Button/Text blocks linking to section anchors */
.faq-topics{margin-top:2.5rem;border-top:1px solid var(--rule);padding-top:1.5rem}
.faq-topics ul{display:flex;flex-wrap:wrap;gap:.6rem;list-style:none;margin:0;padding:0}
.faq-topics a{display:inline-block;font-size:.74rem;letter-spacing:.12em;text-transform:uppercase;font-weight:600;padding:.7rem 1rem;border:1px solid var(--rule);border-radius:999px;color:var(--ink-soft);text-decoration:none;min-height:44px;line-height:1.4}
.faq-topics a:hover{border-color:var(--terracotta);color:var(--terracotta-deep)}
.faq{scroll-margin-top:100px}
[id^="faq-"]{scroll-margin-top:90px}

/* accordion — native Squarespace Accordion Block equivalent */
.faq{display:grid;grid-template-columns:4fr 7fr;gap:clamp(2rem,5vw,5rem);align-items:start}
.faq__head{position:sticky;top:110px}
.faq__head p{color:var(--ink-soft)}
.faq__list{border-top:1px solid var(--rule)}
.acc{border-bottom:1px solid var(--rule)}
.acc summary{list-style:none;cursor:pointer;padding:1.15rem 3rem 1.15rem 0;position:relative}
.acc summary::-webkit-details-marker{display:none}
.acc summary h3,.acc summary h4{font-family:var(--sans);font-weight:500;font-size:1.05rem;margin:0;color:var(--brown);line-height:1.4}
.acc summary::after{content:"+";position:absolute;right:.25rem;top:50%;transform:translateY(-50%);font-family:var(--serif);font-size:1.6rem;color:var(--terracotta);line-height:1;transition:transform .2s}
.acc[open] summary::after{content:"–"}
.acc__body{padding:0 3rem 1.4rem 0;color:var(--ink-soft)}
@media (max-width:860px){.faq{grid-template-columns:1fr}.faq__head{position:static}}

/* CTA band */
.sec--band .band{max-width:760px}
.sec--band p{opacity:.85}
.sec--brown .btn--secondary{color:var(--cream);border-color:rgba(250,247,243,.6)}
.sec--brown .btn--secondary:hover{background:var(--cream);color:var(--brown)}

/* related pair */
.rel-grid{display:grid;grid-template-columns:1fr 1fr;gap:clamp(2rem,5vw,5rem)}
.rel h2{font-size:clamp(1.5rem,2.4vw,2.1rem)}
.rel p{color:var(--ink-soft)}
@media (max-width:700px){.rel-grid{grid-template-columns:1fr}}

/* service groups — typographic, not cards */
.sg-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(2rem,4vw,4rem);border-top:1px solid var(--rule);padding-top:2.5rem}
.sg h3{font-family:var(--sans);font-size:.74rem;letter-spacing:.16em;text-transform:uppercase;font-weight:600;color:var(--sage-deep);margin-bottom:1rem}
.sg__list{list-style:none;margin:0 0 1.25rem;padding:0}
.sg__list a{font-family:var(--serif);font-size:clamp(1.35rem,2vw,1.8rem);text-decoration:none;line-height:1.25;display:inline-block;padding:.3rem 0;border-bottom:1px solid transparent}
.sg__list a:hover{color:var(--terracotta-deep);border-bottom-color:currentColor}
@media (max-width:640px){.sg-grid{grid-template-columns:1fr}}

/* concern discovery */
.concern-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:0 clamp(2rem,5vw,4.5rem);border-top:1px solid var(--rule)}
@media (max-width:640px){.concern-grid{grid-template-columns:1fr}}

/* before/after results — native Squarespace Gallery Block (grid) equivalent */
.results{columns:3;column-gap:clamp(1rem,2.5vw,2rem)}
.results--2{columns:2}
.result{margin:0 0 clamp(1rem,2.5vw,2rem);display:block;text-decoration:none;color:inherit;break-inside:avoid}
.result img{width:100%;height:auto;display:block;border-radius:var(--radius);background:var(--linen-deep)}
.results--4{columns:auto;display:grid;grid-template-columns:repeat(4,1fr);gap:clamp(1rem,2.5vw,2rem);align-items:start}
.results--4 .result{margin:0}
.results--4 img{aspect-ratio:3/4;object-fit:cover;object-position:50% 50%}
.result figcaption,.result__cap{display:block;margin-top:.6rem;font-size:.85rem;color:var(--ink-soft);line-height:1.4}
.result__cap strong{font-weight:600;color:var(--brown);margin-right:.35rem}
.result--link:hover img{opacity:.92}
.result--link:hover .result__cap strong{color:var(--terracotta-deep)}
@media (max-width:1024px){.results{columns:2}.results--4{grid-template-columns:repeat(2,1fr)}}
@media (max-width:560px){.results{columns:1}.results--4{grid-template-columns:1fr}.results--4 img{aspect-ratio:4/5}}

/* testimonials — text blocks in Fluid Engine */
.quotes{display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(1.5rem,3vw,3rem)}
.quote{border-top:2px solid var(--terracotta);padding-top:1.25rem}
.quote blockquote{margin:0;font-family:var(--serif);font-size:1.25rem;line-height:1.35;color:var(--brown)}
.quote cite{display:block;margin-top:1rem;font-style:normal;font-size:.8rem;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-muted)}
@media (max-width:1024px){.quotes{grid-template-columns:repeat(2,1fr)}}
@media (max-width:640px){.quotes{grid-template-columns:1fr}}

/* concierge trio */
.trio{display:grid;grid-template-columns:repeat(3,1fr);gap:2rem;margin-top:2rem;border-top:1px solid var(--rule);padding-top:2rem}
.trio h3{font-family:var(--sans);font-size:.78rem;letter-spacing:.16em;text-transform:uppercase;font-weight:600;color:var(--terracotta)}
.trio p{color:var(--ink-soft);font-size:.98rem}
@media (max-width:700px){.trio{grid-template-columns:1fr}}

/* blog listing — native Squarespace Blog collection equivalent */
.journal{display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(1.5rem,3vw,3rem)}
.post .ph-img{aspect-ratio:4/3;margin-bottom:1rem}
.post__cat{font-size:.7rem;letter-spacing:.16em;text-transform:uppercase;color:var(--sage-deep);font-weight:600}
.post h3{margin:.4rem 0 .5rem}
.post p{color:var(--ink-soft);font-size:.95rem}
.cats{display:flex;flex-wrap:wrap;gap:.6rem;list-style:none;margin:0 0 2.5rem;padding:0}
.cats li{font-size:.74rem;letter-spacing:.12em;text-transform:uppercase;padding:.45rem .9rem;border:1px solid var(--rule);border-radius:999px;color:var(--ink-soft)}
@media (max-width:1024px){.journal{grid-template-columns:repeat(2,1fr)}}
@media (max-width:640px){.journal{grid-template-columns:1fr}}

/* credentials */
.cred{display:grid;grid-template-columns:repeat(4,1fr);gap:1.5rem;border-top:1px solid var(--rule);border-bottom:1px solid var(--rule);padding-block:2rem;margin-top:2rem}
.cred div{font-family:var(--serif);font-size:1.15rem;line-height:1.3}
.cred span{display:block;font-family:var(--sans);font-size:.7rem;letter-spacing:.14em;text-transform:uppercase;color:var(--terracotta);margin-bottom:.4rem;font-weight:600}
@media (max-width:860px){.cred{grid-template-columns:1fr 1fr}}
@media (max-width:480px){.cred{grid-template-columns:1fr}}

/* products */
.products{display:grid;grid-template-columns:repeat(4,1fr);gap:1.5rem}
.product .ph-img{aspect-ratio:1;margin-bottom:.9rem}
.product .ph-img--real img{object-fit:cover}
.product h3{font-family:var(--sans);font-size:1rem;font-weight:600}
.product p{font-size:.92rem;color:var(--ink-soft)}
@media (max-width:1024px){.products{grid-template-columns:repeat(3,1fr)}}
@media (max-width:860px){.products{grid-template-columns:1fr 1fr}}

/* book page */
.book-steps{display:grid;grid-template-columns:repeat(3,1fr);gap:2rem;border-top:1px solid var(--rule);padding-top:2rem;margin-top:2rem}
.book-steps h3{font-size:1.3rem}
.book-steps p{color:var(--ink-soft);font-size:.98rem}
@media (max-width:760px){.book-steps{grid-template-columns:1fr}}

/* footer */
.site-footer{background:var(--linen);border-top:1px solid var(--rule);padding-block:clamp(48px,6vw,80px) 2rem;font-size:.95rem}
.foot-grid{display:grid;grid-template-columns:1.5fr 1fr 1fr 1fr;gap:2.5rem}
.foot__name{font-family:var(--serif);font-size:1.5rem;margin-bottom:.25rem}
.foot__tag{font-size:.7rem;letter-spacing:.16em;text-transform:uppercase;color:var(--ink-muted);font-weight:600}
.foot__area{color:var(--ink-soft);font-size:.9rem;max-width:34ch}
.foot__col h2{font-family:var(--sans);font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;font-weight:600;color:var(--sage-deep);margin-bottom:1rem}
.foot__col ul{list-style:none;margin:0;padding:0;display:grid;gap:.45rem}
.foot__col a{text-decoration:none;color:var(--brown);display:inline-block;padding:.2rem 0;overflow-wrap:anywhere}
.foot__col a:hover{color:var(--terracotta-deep)}
.foot__note{font-size:.8rem;color:var(--ink-muted)}
.foot__legal{margin-top:3rem;padding-top:1.5rem;border-top:1px solid var(--rule);font-size:.82rem;color:var(--ink-muted)}
.foot__legal p{max-width:none}
.foot__disc{max-width:80ch!important;margin-top:.75rem}
@media (max-width:860px){.foot-grid{grid-template-columns:1fr 1fr}}
@media (max-width:520px){.foot-grid{grid-template-columns:1fr}}

/* page intro (utility pages) */
.page-intro{max-width:760px}
.page-intro h1{margin-bottom:.5em}
.page-intro p{font-size:1.1rem;color:var(--ink-soft)}
"""

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@400;500;600&display=swap">'

def document(meta, body, is_index=False):
    title, desc, slug = meta["title"], meta["description"], meta["slug"]
    canonical = f"{C.SITE_URL}/" if slug == "" else f"{C.SITE_URL}/{slug}/"
    style = f"<style>{CSS}</style>" if FLAT else f'<link rel="stylesheet" href="{PREFIX}assets/styles.css">'
    head = f'''<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:type" content="website"><meta property="og:url" content="{canonical}">
{FONTS}
{style}'''
    inner = f'{head}\n{header()}\n<main id="main">{body}</main>\n{footer()}'
    if FLAT and is_index:
        # Hosted preview wraps index.html in its own <html>/<head>/<body> skeleton.
        return inner
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{head}
</head>
<body>
{header()}
<main id="main">{body}</main>
{footer()}
</body>
</html>'''

# ------------------------------------------------------------------ placeholder images
PLACEHOLDERS = {}
def placeholder_svg(name, label, w=1200, h=1500, tone="linen"):
    bg = {"linen": "#EFE7DC", "sage": "#DCE2D5", "terracotta": "#EAD3C6", "cream": "#F5EFE7"}[tone]
    acc = {"linen": "#C17B5E", "sage": "#6F8066", "terracotta": "#A9674C", "cream": "#8A9B80"}[tone]
    PLACEHOLDERS[name] = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{esc(label)}">
<rect width="{w}" height="{h}" fill="{bg}"/>
<circle cx="{w*0.68:.0f}" cy="{h*0.34:.0f}" r="{min(w,h)*0.26:.0f}" fill="{acc}" opacity=".16"/>
<rect x="{w*0.08:.0f}" y="{h*0.56:.0f}" width="{w*0.52:.0f}" height="{h*0.36:.0f}" fill="{acc}" opacity=".12"/>
<line x1="{w*0.08:.0f}" y1="{h*0.5:.0f}" x2="{w*0.92:.0f}" y2="{h*0.5:.0f}" stroke="{acc}" stroke-opacity=".35" stroke-width="2"/>
<text x="{w*0.08:.0f}" y="{h*0.47:.0f}" font-family="Georgia, 'Times New Roman', serif" font-size="{min(w,h)*0.085:.0f}" fill="#2C2318" opacity=".55">Image</text>
<text x="{w*0.08:.0f}" y="{h*0.5+min(w,h)*0.07:.0f}" font-family="Helvetica, Arial, sans-serif" font-size="{min(w,h)*0.032:.0f}" letter-spacing="3" fill="{acc}">TO BE PROVIDED</text>
<text x="{w*0.08:.0f}" y="{h*0.5+min(w,h)*0.12:.0f}" font-family="Helvetica, Arial, sans-serif" font-size="{min(w,h)*0.028:.0f}" fill="#5C4F42">{esc(label)}</text>
</svg>'''

# ------------------------------------------------------------------ pages
def page_home():
    b = ""
    b += hero("Concierge Aesthetics + Wellness",
              C.PAGES["index"]["h1"],
              ["Isabelle Joseph, DNP, NP-BC provides personalized aesthetic, wellness, and skincare care designed around your goals—and your schedule. Experience expert care in the comfort and convenience of your home or preferred location."],
              [book_btn(), btn("Explore Services", "services", "secondary")],
              "home-hero", "Isabelle Joseph, DNP, NP-BC assessing a patient's face before an injectable treatment", focus="50% 35%")
    placeholder_svg("home-hero", "Hero portrait of Isabelle — warm, natural light", tone="linen")
    b += '<div class="wrap"><ul class="trust"><li>Doctorally Prepared</li><li>Personalized Care</li><li>Concierge Convenience</li></ul></div>'
    b += split("Meet Isabelle", "Clinical Expertise Meets Thoughtful, Personalized Care", [
        "Isabelle Joseph, DNP, NP-BC brings extensive clinical experience and a deeply personalized approach to aesthetics, wellness, and skin health.",
        "Her philosophy is simple: great care starts with listening. Rather than taking a one-size-fits-all approach, Isabelle works to understand your goals, concerns, and lifestyle before recommending options that make sense for you.",
        "Whether you're exploring aesthetic treatments, looking for support with your wellness goals, or trying to finally understand what your skin actually needs, you'll receive knowledgeable guidance in an environment designed to feel comfortable, approachable, and entirely focused on you.",
    ], [btn("Meet Isabelle", "about", "text")], "home-meet", "Isabelle Joseph in conversation with a patient", theme="cream")
    placeholder_svg("home-meet", "Editorial portrait — Isabelle, seated, relaxed", tone="sage")
    # concierge difference
    b += section(f'''
    <div class="split split--reverse">
      <div class="split__media">{figure("home-concierge", "Isabelle arriving for a home visit", "ph-img--tall")}</div>
      <div class="split__text">
        {eyebrow("Care That Comes to You")}
        <h2>Your Goals. Your Schedule. Your Space.</h2>
        {p(["Expert aesthetic and wellness care shouldn't have to mean rearranging your entire day.",
             "Through her concierge model, Isabelle brings personalized care directly to you—whether that's your home, office, or another convenient location.",
             "No crowded waiting room. No rushed experience. Just thoughtful, individualized care designed around you."])}
        <div class="trio">
          <div><h3>Convenient</h3><p>Care that works around your life.</p></div>
          <div><h3>Personal</h3><p>One-on-one attention focused on your goals.</p></div>
          <div><h3>Comfortable</h3><p>Receive care in a setting where you feel at ease.</p></div>
        </div>
        <div class="cta-row">{book_btn("Book a Visit")}</div>
      </div>
    </div>''', "linen")
    placeholder_svg("home-concierge", "Concierge visit — doorway, natural light, at-home setting", tone="terracotta")
    # real results
    figs = "".join(f'<a class="result result--link" href="{href(slug)}"><img src="{img_file(f)}" alt="{esc(area)} — before and after" loading="lazy"><span class="result__cap"><strong>{esc(area)}</strong> {esc(svc)}</span></a>' for f, area, svc, slug in C.RESULTS_HOME)
    b += section(f'''
    <div class="sec-head">{eyebrow("Real Results")}<h2>Thoughtful Treatment. Natural-Looking Results.</h2>
    {p(["A few of the concerns Isabelle treats, shown before and after. Explore each service to learn what to expect."])}</div>
    <div class="results results--4">{figs}</div>
    <p class="note">{esc(C.RESULTS_NOTE)}</p>''', "cream")
    # discovery
    concerns = [
        ("Fine Lines + Wrinkles", "Explore options designed to soften the appearance of dynamic lines while maintaining natural expression.", "Explore Tox", "tox"),
        ("Excessive Sweating", "Learn about treatment options for hyperhidrosis and how they may help reduce excessive sweating.", "Explore Hyperhidrosis", "hyperhidrosis"),
        ("Skin Tone + Texture", "Address concerns like dullness, uneven tone, texture, and signs of aging with personalized skin treatments.", "Explore Chemical Peels", "chemical-peels"),
        ("Weight + Metabolic Health", "Explore medically guided GLP-1 weight-management support personalized to your health and goals.", "Explore Weight Management", "weight-loss"),
        ("Hormonal Changes", "Learn more about personalized hormone replacement therapy and support for symptoms associated with hormonal changes.", "Explore HRT", "hormone-replacement-therapy"),
        ("Hair Thinning + Hair Loss", "Understand potential treatment options and take a more informed approach to hair health.", "Explore Hair Loss", "hair-loss"),
        ("Acne + Pigmentation + Aging Skin", "Get expert guidance on prescription and medical-grade skincare based on your individual concerns.", "Explore Skincare", "skincare"),
    ]
    rows = "".join(f'<div class="feat"><h3>{esc(t)}</h3><p>{esc(d)}</p><div class="cta-row">{btn(l, s, "text")}</div></div>' for t, d, l, s in concerns)
    b += section(f'''
    <div class="sec-head">{eyebrow("How Can I Help?")}<h2>Start With What You Want to Change</h2>
    {p(["You don't need to know which treatment or product you need. Start with what you're experiencing, and Isabelle can help you understand your options."])}</div>
    <div class="concern-grid">{rows}</div>''', "cream")
    b += service_groups(theme="linen")
    # skincare
    b += split("Better Skin Starts With Better Information", "Skincare Shouldn't Be Guesswork.", [
        "With endless products, ingredients, routines, and trends competing for your attention, figuring out what your skin actually needs can feel overwhelming.",
        "Isabelle takes a more personalized approach.",
        "From medical-grade skincare to prescription solutions, she can help you build a routine based on your skin, your concerns, and your goals—without filling your shelf with products you don't need.",
    ], [btn("Explore Skincare", "skincare", "secondary"), shop_btn("Shop With Isabelle", "text")], "home-skincare", "Curated medical-grade skincare products", theme="cream")
    placeholder_svg("home-skincare", "Skincare still life — products on linen, soft shadow", tone="cream")
    b += cta_band("Not Sure Where to Start? That's Okay.", [
        "You don't have to choose your treatment before you book. Start with a conversation. Isabelle can help you identify your concerns, talk through your goals, and understand the options available to you so you can make an informed decision about what feels right.",
    ], [book_btn("Start With a Consultation")], theme="sage")
    # testimonials (placeholder)
    q = "".join(f'<div class="quote"><blockquote>{rich("[APPROVED PATIENT TESTIMONIAL TO BE PROVIDED]")}</blockquote><cite>{rich("[NAME / INITIALS]")}</cite></div>' for _ in range(3))
    b += section(f'''
    <div class="sec-head">{eyebrow("Patient Experiences")}<h2>Care That Feels Different.</h2>
    <p class="note">Include 3–5 approved patient testimonials if available and appropriate for use. Confirm permission and any applicable Skin Clique requirements before publishing.</p></div>
    <div class="quotes">{q}</div>''', "cream")
    # edit
    posts = "".join(f'<article class="post">{figure("post-" + str(i), "Article cover image", "ph-img--wide")}<p class="post__cat">{esc(cat)}</p><h3>{esc(t)}</h3><p>{rich("[ARTICLE CONTENT TO BE PROVIDED]")}</p></article>'
                    for i, (t, cat) in enumerate(C.BLOG_LAUNCH, 1))
    for i in range(1, 4):
        placeholder_svg(f"post-{i}", f"Editorial cover — launch article {i}", 1200, 900, tone=["linen", "sage", "cream"][i-1])
    b += section(f'''
    <div class="sec-head">{eyebrow("The Isabelle Edit")}<h2>Expert Guidance for Aesthetics, Skin + Wellness</h2>
    {p(["Straightforward education to help you better understand your options, your skin, and your health."])}</div>
    <div class="journal">{posts}</div>
    <div class="cta-row">{btn("Explore The Isabelle Edit", "blog", "secondary")}</div>''', "linen")
    # service area
    b += section(f'''
    <div class="split">
      <div class="split__media">{figure("home-area", "South Easton, Massachusetts and surrounding communities", "ph-img--square")}</div>
      <div class="split__text">
        {eyebrow("Concierge Care in Your Community")}
        <h2>Aesthetic + Wellness Care That Comes to You</h2>
        {p(["Isabelle provides concierge aesthetic, wellness, and skincare services throughout South Easton and select surrounding Massachusetts communities, bringing personalized care directly to patients at home, at work, or another convenient location."])}
        <p class="note" style="margin-top:1rem"><strong>Communities served:</strong> South Easton • Norwell • Randolph • Somerset • Stoughton • Westwood</p>
        <div class="cta-row">{book_btn("Check Availability + Book")}</div>
      </div>
    </div>''', "cream")
    placeholder_svg("home-area", "Local landscape / neighborhood — South Easton, MA", 1200, 1200, tone="sage")
    b += cta_band("Ready for Care That Fits You?", ["Discover a more personal approach to aesthetics, wellness, and skin health with Isabelle Joseph, DNP, NP-BC."],
                  [book_btn(), btn("Explore Services", "services", "secondary")], theme="brown")
    return b

def page_about():
    A = C.PAGES["about"]
    b = hero("Meet Isabelle", A["h1"], [
        "For Isabelle Joseph, DNP, NP-BC, great care is about more than choosing a treatment. It starts with listening, understanding what matters to you, and creating a plan that fits your goals, your lifestyle, and your comfort level.",
        "With more than 15 years of clinical experience, Isabelle brings advanced medical knowledge together with a warm, personalized approach to aesthetics, wellness, and skin health.",
        "Her goal isn't to change who you are. It's to help you feel informed, supported, and confident in the choices you make for yourself.",
    ], [book_btn()], "about-hero", "Portrait of Isabelle Joseph, DNP, NP-BC", tagline="Expert Care Starts With Truly Knowing Your Patient")
    placeholder_svg("about-hero", "Full-length editorial portrait — Isabelle", tone="linen")
    b += prose(None, "Experience You Can Trust. Care That Feels Personal.", [
        "Isabelle's clinical background and doctoral education have shaped the way she approaches every patient interaction: thoughtfully, individually, and with an emphasis on education. She believes patients deserve to understand their options—not simply be told what they need.",
        "Whether you're considering Tox for the first time, navigating changes in your skin or hair, exploring support for weight or hormonal changes, or simply trying to build a better skincare routine, Isabelle takes the time to understand the bigger picture.",
        "Together, you'll talk about your concerns, your goals, and the options available to you so you can make informed decisions about your care.",
    ], theme="linen")
    b += split("A Thoughtful Approach to Aesthetics", "You Should Still Look Like You.", [
        "Aesthetic care doesn't have to be about dramatic change. Isabelle's approach centers on thoughtful recommendations and results designed to help you feel refreshed and confident while still feeling like yourself.",
        "Every patient is different. Your facial anatomy, skin, goals, lifestyle, and preferences all matter when determining whether a treatment is appropriate for you.",
        "That's why Isabelle begins with the individual—not the procedure.",
    ], [btn("Explore Aesthetic Services", "services#aesthetics", "text")], "about-aesthetics", "Natural skin detail — editorial close-up", theme="cream")
    placeholder_svg("about-aesthetics", "Natural skin / expression — editorial detail", tone="terracotta")
    b += split("Looking Beyond the Surface", "Wellness That Connects the Pieces", [
        "Isabelle's interest in wellness extends beyond aesthetics. She believes feeling your best can involve many interconnected pieces—from skin health and hormonal changes to weight, hair health, movement, nutrition, and overall well-being.",
        "That perspective has shaped a more comprehensive approach to care and allows Isabelle to support patients through services spanning aesthetics, wellness, and skin health.",
        "It's not about chasing perfection. It's about having knowledgeable support as you decide what feeling your best looks like for you.",
    ], [btn("Explore Wellness Services", "services#wellness", "text")], "about-wellness", "Wellness lifestyle — movement, morning light", reverse=True, theme="linen")
    placeholder_svg("about-wellness", "Wellness lifestyle — walking, outdoors, calm", tone="sage")
    b += split(None, "Skincare Without the Guesswork", [
        "Isabelle has a particular passion for medical-grade skincare and helping patients understand what their skin actually needs. With countless products, ingredients, routines, and trends available, skincare can quickly become overwhelming. Isabelle helps simplify it.",
        "Through personalized skincare consultations, medical-grade products, and prescription skincare options when appropriate, she helps patients create realistic routines based on their individual skin concerns and goals.",
        "The goal isn't more products. It's the right products.",
    ], [btn("Explore Skincare", "skincare", "text")], "about-skincare", "Skincare products on a vanity", theme="cream")
    placeholder_svg("about-skincare", "Skincare still life — edited routine, three products", tone="cream")
    b += section(f'''
    <div class="split split--reverse">
      <div class="split__media">{figure("about-concierge", "Isabelle providing care in a patient's home", "ph-img--tall")}</div>
      <div class="split__text">
        {eyebrow("Care That Comes to You")}
        <h2>A More Convenient, Personal Way to Receive Care</h2>
        {p(["Isabelle provides care through a concierge model, meeting patients where they're comfortable. Appointments may take place in your home, office, or another convenient location, allowing you to receive personalized care without the traditional waiting-room experience.",
             "For Isabelle, concierge care isn't simply about convenience. It's an opportunity to create a more relaxed, personal experience where there's room for questions, conversation, education, and individualized attention.",
             C.CONCIERGE_AREA_P])}
        <div class="cta-row">{book_btn()}</div>
      </div>
    </div>''', "linen")
    placeholder_svg("about-concierge", "Home visit — living room, warm light", tone="terracotta")
    b += section(f'''
    <div class="prose">
      {eyebrow("Education + Clinical Experience")}
      <h2>Knowledge Matters When You're Choosing a Provider</h2>
      {p(["Isabelle brings more than 15 years of clinical experience to her work and has pursued advanced education through the University of Pennsylvania and Regis College."])}
    </div>
    <div class="cred">
      <div><span>Credential</span>Doctor of Nursing Practice</div>
      <div><span>Certification</span>Board-Certified Nurse Practitioner</div>
      <div><span>Experience</span>15+ Years of Clinical Experience</div>
      <div><span>Education</span>University of Pennsylvania + Regis College</div>
    </div>
    <div class="prose" style="margin-top:2rem">
      {p(["Her clinical experience, continued education, and commitment to evidence-informed care allow her to approach aesthetics and wellness from a medical perspective while keeping each patient's individual goals at the center of the conversation."])}
    </div>''', "cream")
    b += split("Beyond the Credentials", "Meet the Person Behind the Provider", [
        "Isabelle believes wellness should fit into real life—and she tries to live that philosophy herself. She has led a fitness accountability group for women and understands firsthand the value of encouragement, consistency, and having a community supporting your goals.",
        "Outside of her professional life, Isabelle loves exploring new destinations, enjoying great food, decorating her home, spending time at the beach, and making memories with the people she loves.",
        "Those experiences are part of what makes her approach to patient care so personal. She understands that everyone sitting across from her has a life beyond an appointment—and that the best care should complement that life rather than take it over.",
    ], None, "about-personal", "Isabelle at the beach — candid, personal", theme="linen")
    placeholder_svg("about-personal", "Candid lifestyle — beach, travel, or at home", tone="sage")
    b += service_groups(theme="cream", eyebrow_t="How Isabelle Can Help", h2="Aesthetics. Wellness. Skin Health.")
    b += cta_band("Your Care Should Feel Like Your Care.", [
        "You don't need to arrive knowing exactly which treatment, product, or service you need. You just need a place to start.",
        "Isabelle will listen to what's concerning you, help you understand the options available, and work with you to determine an approach that makes sense for your individual goals. Ready to meet Isabelle?",
    ], [book_btn()], theme="brown")
    return b

def page_services():
    S = C.PAGES["services"]
    b = hero("Services", S["h1"], [
        "Your goals are personal. Your care should be, too.",
        "Isabelle Joseph, DNP, NP-BC provides concierge aesthetic, wellness, and skincare services designed around your individual concerns, goals, and lifestyle.",
        "Whether you want to soften the appearance of fine lines, better understand changes happening in your body, improve your skin, address hair thinning, or simply aren't sure where to begin, Isabelle can help you understand your options and determine an approach that makes sense for you. And because care is concierge, Isabelle comes to you.",
    ], [book_btn()], "services-hero", "Isabelle preparing for a concierge appointment", tagline="Personalized Care That Starts With You")
    placeholder_svg("services-hero", "Editorial — Isabelle with treatment kit, at-home setting", tone="linen")
    b += prose("How Can Isabelle Help?", "Start With What You're Experiencing", [
        "You don't have to know the name of the treatment you need before reaching out. Start with your concern.",
        "Isabelle will help you understand the options available, answer your questions, and determine whether a treatment or service is appropriate for your individual needs. Explore Isabelle's services below.",
    ], theme="linen")
    # Aesthetics
    b += feature_list("Aesthetics", "Thoughtful Treatments. Natural-Looking Results.", [
        "Aesthetic care shouldn't be about changing the way you look. Isabelle takes a personalized approach to aesthetics, considering your individual anatomy, concerns, goals, and preferences before recommending treatment.",
        "The goal is thoughtful care designed to help you feel refreshed, confident, and still completely like yourself.",
    ], [
        ("Tox", "Soften the appearance of expression lines while maintaining natural movement. Tox treatments use neuromodulators to temporarily relax targeted muscles responsible for dynamic lines and wrinkles. Treatment may be considered for concerns such as forehead lines, frown lines, and crow's feet. Isabelle takes a conservative, personalized approach based on your anatomy and aesthetic goals.", btn("Explore Tox", "tox", "text")),
        ("Hyperhidrosis", "When excessive sweating interferes with everyday life, treatment options are available. Hyperhidrosis causes excessive sweating beyond what the body typically needs for temperature regulation. Neuromodulator treatment may help temporarily reduce excessive sweating by targeting the chemical signals responsible for activating sweat glands in treated areas.", btn("Explore Hyperhidrosis", "hyperhidrosis", "text")),
        ("Chemical Peels", "Refresh dull, uneven, or changing skin. Chemical peels use carefully selected solutions to exfoliate the skin and encourage renewal. Depending on your skin and the treatment selected, peels may help improve concerns such as uneven tone, texture, dullness, pigmentation, and visible signs of aging.", btn("Explore Chemical Peels", "chemical-peels", "text")),
    ], theme="cream", cols=3)
    b = b.replace('<section class="sec sec--cream ">', '<section class="sec sec--cream " id="aesthetics">', 1) if 'id="aesthetics"' not in b else b
    # Wellness
    w = feature_list("Wellness", "Support for the Changes You Can Feel", [
        "Your health and wellness needs can change over time. Isabelle provides personalized wellness services designed to help patients better understand those changes, explore appropriate treatment options, and make informed decisions about their care.",
    ], [
        ("GLP-1 Weight Management", "A medically guided approach to weight management. Weight is complex, and successful weight management isn't simply about willpower. For appropriate patients, GLP-1 medications may be one tool used as part of a medically guided approach. Isabelle can help you understand the program, discuss your health and goals, and determine whether GLP-1 weight-management support may be appropriate for you.", btn("Explore GLP-1 Weight Management", "weight-loss", "text")),
        ("Hormone Replacement Therapy", "Understand your symptoms. Explore your options. Hormonal changes can affect many aspects of how you feel. Hormone replacement therapy may be an option for certain patients experiencing symptoms associated with hormonal changes. Isabelle provides personalized guidance to help you better understand your symptoms, available options, and whether HRT may be appropriate for your individual health needs.", btn("Explore Hormone Replacement Therapy", "hormone-replacement-therapy", "text")),
        ("Hair Loss", "Hair changes deserve more than a one-size-fits-all solution. Hair thinning and hair loss can occur for many reasons, and understanding what's contributing to the change is an important part of determining an appropriate path forward. Isabelle can help you explore available hair-loss treatment options and develop an approach based on your individual concerns and goals.", btn("Explore Hair Loss", "hair-loss", "text")),
    ], theme="linen", cols=3)
    b += w.replace('<section class="sec sec--linen ">', '<section class="sec sec--linen " id="wellness">', 1)
    sk = feature_list("Skin Health", "Better Skin Starts With Understanding Your Skin", [
        "Skincare doesn't need to be complicated. Isabelle helps patients move beyond trends and trial-and-error by taking a more personalized approach to skin health.",
        "Together, you can identify your concerns, simplify your routine, and explore skincare options based on what your skin actually needs.",
    ], [
        ("Prescription Skincare", "Target specific skin concerns with personalized prescription options. For some skin concerns, prescription skincare may provide options beyond traditional over-the-counter products. Depending on your individual needs, Isabelle can help determine whether prescription skincare is appropriate and provide guidance on incorporating it into your routine.", btn("Explore Prescription Skincare", "skincare", "text")),
        ("Personalized Skincare Consultations", "Stop guessing which products belong in your routine. A personalized skincare consultation gives you an opportunity to discuss your skin, current routine, concerns, and goals with Isabelle. From acne and pigmentation to texture, dryness, and visible signs of aging, Isabelle can help you build a realistic skincare routine using products selected with your individual skin in mind.", btn("Explore Skincare Consultations", "skincare-consultations", "text")),
        ("Medical-Grade Skincare", "Great skincare isn't about having more products. It's about having the right ones. Isabelle can help patients understand medical-grade skincare, active ingredients, and how different products may fit into an effective routine. Explore Isabelle's skincare recommendations and shop products through her Skin Clique storefront.", shop_btn("Shop With Isabelle", "text")),
    ], theme="cream", cols=3)
    b += sk.replace('<section class="sec sec--cream ">', '<section class="sec sec--cream " id="skin-health">', 1)
    b += section(f'''
    <div class="split">
      <div class="split__media">{figure("services-concierge", "Concierge appointment in a patient's home", "ph-img--tall")}</div>
      <div class="split__text">
        {eyebrow("The Concierge Difference")}
        <h2>Care Designed to Fit Into Your Life</h2>
        {p(["Finding time for yourself shouldn't require rearranging your entire schedule. Through her concierge model, Isabelle brings personalized aesthetic, wellness, and skincare care directly to you.",
             "Appointments can take place in your home, office, or another convenient location, creating an experience that's private, comfortable, and centered around you.",
             C.CONCIERGE_AREA_P])}
        <div class="cta-row">{book_btn()}</div>
      </div>
    </div>''', "linen")
    placeholder_svg("services-concierge", "Concierge appointment — home setting, editorial", tone="terracotta")
    b += related_pair([
        ("You Don't Have to Figure It Out Alone.", [
            "It's completely normal to know what you'd like to improve without knowing which treatment or service might help. That's where Isabelle comes in.",
            "Start with a conversation about what you're experiencing and what you'd like to accomplish. Isabelle can help you understand your options, answer your questions, and determine an appropriate next step. No pressure. No one-size-fits-all plan. Just personalized guidance to help you make an informed decision.",
        ], ("Start With Isabelle", C.BOOK_URL)),
        ("Explore. Learn. Decide What's Right for You.", [
            "Aesthetics, wellness, and skincare can come with a lot of information—and sometimes even more opinions.",
            "The Isabelle Edit makes it easier to understand the topics that matter to you with straightforward education about treatments, skin health, products, wellness, and more.",
        ], ("Visit The Isabelle Edit", "blog")),
    ], theme="cream")
    b += cta_band("Ready to Get Started?", ["Experience a more personal approach to aesthetics, wellness, and skin health with Isabelle Joseph, DNP, NP-BC."], [book_btn()], theme="brown")
    return b

def page_service(key):
    s = C.SERVICES[key]
    b = hero(s["group"], s["h1"], s["intro"], [book_btn(s["hero_cta"]), btn("All Services", "services", "secondary")],
             s["hero_image"][0], s["hero_image"][1], tagline=s["tagline"])
    b = b.replace('class="sec sec--cream hero"', 'class="sec sec--cream hero hero--service"')
    placeholder_svg(s["hero_image"][0], s["hero_image"][1], tone="linen")
    b += prose("Overview", s["overview_h2"], s["overview"], theme="linen", sub=s.get("overview_sub"))
    for h, sub, paras in s.get("extra_before_addresses", []):
        b += prose(None, h, paras, theme="cream", sub=sub)
    b += feature_list("Who It May Be For", s["addresses_h2"], [s["addresses_intro"]] if s.get("addresses_intro") else [], s["addresses"],
                      cta=book_btn(s["addresses_cta"]), theme="cream", sub=s.get("addresses_sub"), note=s.get("addresses_note"),
                      cols=2 if len(s["addresses"]) != 3 else 3)
    if key in C.RESULTS:
        b += results_gallery(C.RESULTS[key], intro=[f"A look at the areas Isabelle treats with {s['name'].lower() if key != 'tox' else 'Tox'}."], theme="linen",
                             cta=book_btn(s["addresses_cta"]))
    for h, sub, paras in s.get("extra_after_addresses", []):
        b += prose(None, h, paras, theme="cream" if key in C.RESULTS else "linen", sub=sub)
    if s.get("options"):
        b += feature_list("Options", s["options_h2"], [s["options_intro"]], s["options"], theme="linen", sub=s["options_sub"], note=s["options_note"], cols=2)
    b += split(s["approach_eyebrow"], s["approach_h2"], s["approach"], None, s["approach_image"][0], s["approach_image"][1], reverse=True, theme="cream")
    placeholder_svg(s["approach_image"][0], s["approach_image"][1], tone="sage")
    b += steps(s["steps_h2"], s["steps"], cta=book_btn(s.get("steps_cta", s["hero_cta"])), theme="linen")
    for h, sub, paras in s.get("extra_after_steps", []):
        b += prose(None, h, paras, theme="cream", sub=sub)
    b += section(f'''
    <div class="split">
      <div class="split__media">{figure(s["slug"] + "-concierge", "Concierge care in a comfortable setting", "ph-img--tall")}</div>
      <div class="split__text">
        {eyebrow(s["concierge_eyebrow"])}
        <h2>{rich(s["concierge_h2"])}</h2>
        {p(s["concierge"])}
        <div class="cta-row">{book_btn()}</div>
      </div>
    </div>''', "sage")
    placeholder_svg(s["slug"] + "-concierge", "Concierge setting — home, office, or preferred location", tone="terracotta")
    b += checklist(s["candidates_h2"], s["candidates_intro"], s["candidates"], s["candidates_outro"], theme="cream", eyebrow_t="Is It Right for Me?")
    before = ""
    if s.get("before_list"):
        li = "".join(f"<li>{rich(x)}</li>" for x in s["before_list"])
        before = f'<div class="check"><div class="check__text"><h2>{rich(s["before_h2"])}</h2>{p([s["before_intro"]])}</div><ul class="check__list">{li}</ul><div class="check__outro">{p(s["before"])}</div></div>'
    else:
        before = f'<div class="prose prose--narrow"><h2>{rich(s["before_h2"])}</h2>{p(s["before"])}</div>'
    after = f'<div class="prose prose--narrow" style="margin-top:3.5rem"><h2>{rich(s["after_h2"])}</h2>{p(s["after"])}</div>' if s.get("after") else ""
    b += section(f'{eyebrow("What to Know")}{before}{after}', "linen")
    b += faq(s["faq_h2"], s["faq"], theme="cream", eyebrow_t="Frequently Asked Questions",
             intro=["Have a question you don't see here? Bring it to your consultation, or browse the full FAQ page."])
    b += related_pair(s["related"], theme="linen")
    b += prose(None, s["notsure_h2"], s["notsure"], [book_btn()], theme="cream")
    b += cta_band(s["final_h2"], s["final"], [book_btn(s["final_cta"]), btn("All Services", "services", "secondary")], theme="brown")
    return b

def page_skincare():
    b = hero("Skin Health", C.PAGES["skincare"]["h1"], [
        "With endless products, ingredients, routines, and trends competing for your attention, figuring out what your skin actually needs can feel overwhelming. Isabelle takes a more personalized approach.",
        "From medical-grade skincare to prescription solutions, she can help you build a routine based on your skin, your concerns, and your goals—without filling your shelf with products you don't need.",
    ], [shop_btn("Shop Skincare", "primary"), btn("Book a Skincare Consultation", C.BOOK_URL, "secondary")],
        "skincare-hero", "Curated skincare products", tagline="Better Skin Starts With Better Information")
    placeholder_svg("skincare-hero", "Skincare hero — products, hands, natural skin", tone="cream")
    b += feature_list("Skin Health", "Three Ways Isabelle Supports Your Skin", [
        "Skincare doesn't need to be complicated. Isabelle helps patients move beyond trends and trial-and-error by taking a more personalized approach to skin health.",
    ], [
        ("Prescription Skincare", "For some skin concerns, prescription skincare may provide options beyond traditional over-the-counter products. Depending on your individual needs, Isabelle can help determine whether prescription skincare is appropriate and provide guidance on incorporating it into your routine.", book_btn("Ask About Prescription Skincare", "text")),
        ("Personalized Skincare Consultations", "A personalized skincare consultation gives you an opportunity to discuss your skin, current routine, concerns, and goals with Isabelle. From acne and pigmentation to texture, dryness, and visible signs of aging, she can help you build a realistic routine using products selected with your individual skin in mind.", btn("Explore Skincare Consultations", "skincare-consultations", "text")),
        ("Medical-Grade Skincare", "Great skincare isn't about having more products. It's about having the right ones. Isabelle can help you understand medical-grade skincare, active ingredients, and how different products may fit into an effective routine. Explore her recommendations and shop products through her Skin Clique storefront.", shop_btn("Shop With Isabelle", "text")),
    ], theme="linen", cols=3)
    prods = ""
    for i, (name, desc) in enumerate(C.PRODUCT_TILES, 1):
        placeholder_svg(f"product-{i}", f"Product image {i}", 1000, 1000, tone=["cream", "linen", "sage", "cream"][i-1])
        prods += f'<div class="product">{figure(f"product-{i}", "Product image")}<h3>{rich(name)}</h3><p>{rich(desc)}</p></div>'
    b += section(f'''
    <div class="sec-head">{eyebrow("Shop My Skincare")}<h2>Selected Products + Categories</h2>
    {p(["Products Isabelle recommends are available through her Skin Clique storefront. [SELECTED PRODUCTS / CATEGORIES TO BE PROVIDED BY ISABELLE]"])}</div>
    <div class="products">{prods}</div>
    <div class="cta-row">{shop_btn("Shop Skincare", "primary")}</div>
    <p class="note">Purchases are completed securely on Skin Clique. This website does not process orders.</p>''', "cream")
    b += results_gallery(C.RESULTS["skincare"], h2="Real Skin. Real Results.", intro=["Prescription and medical-grade skincare results from Isabelle's patients."], theme="linen", cta=book_btn("Book a Skincare Consultation"))
    b += split("Skincare Philosophy", "The Goal Isn't More Products. It's the Right Products.", [
        "Isabelle has a particular passion for medical-grade skincare and helping patients understand what their skin actually needs.",
        "Through personalized skincare consultations, medical-grade products, and prescription skincare options when appropriate, she helps patients create realistic routines based on their individual skin concerns and goals.",
        "Your everyday routine also plays an important role in protecting your skin and supporting your goals between professional treatments such as chemical peels. Isabelle can help you determine which cleansers, antioxidants, moisturizers, retinoids, pigment-focused products, and sun protection may make sense for your individual skin.",
    ], [btn("Explore Chemical Peels", "chemical-peels", "text")], "skincare-philosophy", "Isabelle reviewing a skincare routine with a patient", theme="cream", reverse=True)
    placeholder_svg("skincare-philosophy", "Isabelle reviewing products with a patient", tone="sage")
    b += section(f'''
    <div class="sec-head">{eyebrow("Education")}<h2>Skincare Reading From The Isabelle Edit</h2></div>
    <div class="journal"><article class="post">{figure("post-2", "Article cover image", "ph-img--wide")}<p class="post__cat">Skin</p><h3>Medical-Grade Skincare: Is It Really Different?</h3><p>{rich("[ARTICLE CONTENT TO BE PROVIDED]")}</p></article></div>
    <div class="cta-row">{btn("Explore The Isabelle Edit", "blog", "text")}</div>''', "cream")
    b += cta_band("Ready to Simplify Your Skincare?", ["Start with a consultation, or shop Isabelle's curated recommendations on Skin Clique."],
                  [book_btn("Book a Skincare Consultation"), btn("Shop Skincare", C.SHOP_URL, "secondary")], theme="brown")
    return b

def page_skincare_consultations():
    b = hero("Skin Health", C.PAGES["skincare-consultations"]["h1"], [
        "A personalized skincare consultation gives you an opportunity to discuss your skin, current routine, concerns, and goals with Isabelle.",
        "From acne and pigmentation to texture, dryness, and visible signs of aging, Isabelle can help you build a realistic skincare routine using products selected with your individual skin in mind.",
    ], [book_btn("Book a Skincare Consultation"), btn("Explore Skincare", "skincare", "secondary")],
        "consult-hero", "Skincare consultation", tagline="Stop Guessing Which Products Belong in Your Routine.")
    placeholder_svg("consult-hero", "Consultation — Isabelle and patient, skincare on table", tone="linen")
    b += feature_list("Who It May Be For", "Concerns a Consultation Can Address", [
        "You don't need to arrive knowing which product, ingredient, or treatment you need. Start with your skin.",
    ], [
        ("Acne + Congestion", "Clogged pores, breakouts, and lingering post-acne marks. Isabelle can help determine whether prescription skincare, changes to your home routine, a chemical peel, or another approach may be appropriate."),
        ("Pigmentation + Uneven Tone", "Dark spots, post-inflammatory marks, and uneven tone. Because pigmentation can have different causes, an individualized assessment matters."),
        ("Texture, Dryness + Dullness", "Rough texture, dryness, and skin that simply isn't responding to your current routine."),
        ("Visible Signs of Aging", "Fine lines, loss of radiance, and changes in skin quality that a thoughtfully edited routine may help support."),
    ], theme="linen", cols=2)
    b += steps("What to Expect", [
        ("Talk Through Your Skin", "You'll discuss your skin, current routine, previous products and treatments, concerns, and goals with Isabelle."),
        ("Simplify + Select", "Isabelle helps you identify what your skin actually needs and which medical-grade or prescription options may fit, without filling your shelf with products you don't need."),
        ("Build Your Routine", "You'll leave with a realistic routine, and can shop recommended products through Isabelle's Skin Clique storefront. [ADDITIONAL CONSULTATION DETAILS TO BE PROVIDED]"),
    ], cta=book_btn("Book a Skincare Consultation"), theme="cream")
    b += related_pair([
        ("Professional Treatments + Your Routine", ["What you do between treatments matters. If a chemical peel is part of your plan, Isabelle can help you prepare your skin and protect your results with the right at-home routine."], ("Explore Chemical Peels", "chemical-peels")),
        ("Shop Isabelle's Recommendations", ["Medical-grade products Isabelle recommends are available through her Skin Clique storefront."], ("Shop Skincare", C.SHOP_URL)),
    ], theme="linen")
    b += cta_band("Ready to Get Started?", ["Book a personalized skincare consultation with Isabelle Joseph, DNP, NP-BC."], [book_btn("Book a Skincare Consultation")], theme="brown")
    return b

def page_faqs():
    import json
    groups = [("general", "General + Booking", "General", C.FAQ_GENERAL, ["Everything you need to know before your first visit."])]
    for key in C.SERVICE_ORDER:
        sv = C.SERVICES[key]
        items = list(sv["faq"]) + C.FAQ_EXTRA.get(key, [])
        label = "Tox (Xeomin, Dysport, Botox)" if key == "tox" else sv["name"]
        groups.append((key, label, sv["group"], items, [f"Learn more on the {sv['name']} page."]))
    groups.append(("skincare", "Prescription + Medical-Grade Skincare", "Skin Health", C.FAQ_SKINCARE, ["Learn more on the Skincare page."]))
    groups.append(("practice", "About the Practice", "Practice", C.FAQ_PRACTICE, ["Learn more about Isabelle on the About page."]))

    chips = "".join(f'<li><a href="#faq-{k}">{esc(lbl.split(" (")[0])}</a></li>' for k, lbl, *_ in groups)
    b = section(f'''<div class="page-intro">{eyebrow("FAQ")}<h1>{esc(C.PAGES["faqs"]["h1"])}</h1>
    {p(["Answers to the questions Isabelle hears most about concierge care, aesthetic treatments, wellness programs, and skincare. Jump to a topic or browse them all."])}
    <div class="cta-row">{book_btn()}</div></div>
    <nav class="faq-topics" aria-label="FAQ topics"><ul>{chips}</ul></nav>''', "cream")

    themes = ["linen", "cream"]
    page_links = {"tox": "tox", "hyperhidrosis": "hyperhidrosis", "chemical-peels": "chemical-peels", "weight-loss": "weight-loss",
                  "hormone-replacement-therapy": "hormone-replacement-therapy", "hair-loss": "hair-loss", "skincare": "skincare", "practice": "about"}
    for i, (k, lbl, eb, items, intro) in enumerate(groups):
        html_ = faq(lbl, items, theme=themes[i % 2], eyebrow_t=eb, intro=intro)
        html_ = html_.replace('<section class="sec sec--' + themes[i % 2] + ' ">', f'<section class="sec sec--{themes[i % 2]} " id="faq-{k}">', 1)
        if k in page_links:
            name = {"skincare": "Skincare", "practice": "About"}.get(k, C.SERVICES[k]["name"] if k in C.SERVICES else k)
            html_ = html_.replace(f"on the {esc(name)} page", f'on the <a href="{href(page_links[k])}">{esc(name)} page</a>')
            html_ = html_.replace("Learn more about Isabelle on the About page.", f'Learn more about Isabelle on the <a href="{href("about")}">About page</a>.')
        b += html_

    # FAQPage structured data (native Squarespace: Settings -> Advanced -> Code Injection, or the page's header injection)
    entities = [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for _, _, _, items, _ in groups for q, a in items]
    ld = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": entities}, ensure_ascii=False)
    b += f'<script type="application/ld+json">{ld}</script>'
    b += cta_band("Still Have Questions?", ["Book a consultation and Isabelle will cover everything specific to your goals.",
                  f"Prefer to text? Reach Isabelle at {C.CONTACT['phone']} ({C.CONTACT['phone_note'].lower()})."],
                  [book_btn("Book a Consultation")], theme="brown")
    return b

def page_blog():
    cats = "".join(f"<li>{esc(c)}</li>" for c in C.BLOG_CATEGORIES)
    posts = "".join(f'<article class="post">{figure("post-" + str(i), "Article cover image", "ph-img--wide")}<p class="post__cat">{esc(cat)}</p><h2 style="font-size:1.5rem">{esc(t)}</h2><p>{rich("[ARTICLE CONTENT TO BE PROVIDED]")}</p><p class="note" style="margin-top:.5rem">Coming soon</p></article>'
                    for i, (t, cat) in enumerate(C.BLOG_LAUNCH, 1))
    b = section(f'''<div class="page-intro">{eyebrow("The Journal")}<h1>{esc(C.PAGES["blog"]["h1"])}</h1>
    {p(["Expert guidance for aesthetics, skin + wellness. Straightforward education to help you better understand your options, your skin, and your health."])}</div>''', "cream")
    b += section(f'''<ul class="cats" aria-label="Categories">{cats}</ul><div class="journal">{posts}</div>
    <p class="note">Recommended launch articles from the content blueprint. Articles are published through the native Squarespace Blog collection.</p>''', "linen")
    b += related_pair([
        ("Explore Services", ["Ready to move from reading to a conversation? Explore Isabelle's aesthetic, wellness, and skin health services."], ("Explore Services", "services")),
        ("Book With Isabelle", ["You don't have to choose a treatment before you book. Start with a consultation."], ("Book With Isabelle", C.BOOK_URL)),
    ], theme="cream")
    return b

def page_book():
    b = section(f'''<div class="page-intro">{eyebrow("Book With Isabelle")}<h1>{esc(C.PAGES["book"]["h1"])}</h1>
    {p(["Appointments with Isabelle are scheduled securely through Skin Clique. You don't need to know exactly which treatment you need—start with a consultation, and Isabelle will help you understand your options.",
         "Concierge appointments take place in your home, office, or another convenient location in South Easton and select surrounding Massachusetts communities. Wellness programs may support a broader area."])}
    <div class="cta-row">{book_btn("Book With Isabelle")}<span class="note" style="margin:0">Opens Skin Clique in a new tab</span></div></div>
    <div class="book-steps">
      <div><h3>1. Choose a service or consultation</h3><p>Select a treatment, a wellness intake, or a general consultation if you're not sure where to start.</p></div>
      <div><h3>2. Complete your intake</h3><p>Skin Clique's secure intake gives Isabelle the health information she needs before your visit.</p></div>
      <div><h3>3. Isabelle comes to you</h3><p>Receive personalized, one-on-one care in a setting where you feel at ease.</p></div>
    </div>''', "cream")
    b += section(f'''
    <div class="split">
      <div class="split__media">{figure("book-hero", "Isabelle arriving for an appointment", "ph-img--tall")}</div>
      <div class="split__text">
        {eyebrow("Questions Before Booking?")}
        <h2>We're Happy to Help.</h2>
        {p(["Browse the FAQs, or reach out directly."])}
        <p>Text: <a href="sms:{C.CONTACT["phone"].replace("-", "")}">{esc(C.CONTACT["phone"])}</a> ({esc(C.CONTACT["phone_note"].lower())})<br>Email: <a href="mailto:{C.CONTACT["email"]}">{esc(C.CONTACT["email"])}</a><br>Instagram: <a href="{C.CONTACT["instagram_url"]}" target="_blank" rel="noopener">{esc(C.CONTACT["instagram_handle"])}</a></p>
        <div class="cta-row">{btn("Read the FAQs", "faqs", "secondary")}{btn("Shop Skincare", C.SHOP_URL, "text")}</div>
      </div>
    </div>''', "linen")
    placeholder_svg("book-hero", "Isabelle — welcoming, at the door", tone="terracotta")
    b += cta_band("Ready for Care That Fits You?", ["Book concierge aesthetic, wellness, and skincare care with Isabelle Joseph, DNP, NP-BC."], [book_btn("Book With Isabelle")], theme="brown")
    return b

def page_404():
    return section(f'''<div class="page-intro"><h1>Page Not Found</h1>{p(["The page you're looking for has moved or doesn't exist."])}
    <div class="cta-row">{btn("Go Home", "", "secondary")}{book_btn()}</div></div>''', "cream")

# ------------------------------------------------------------------ build
def write(path, s):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(s)

def out_path(slug):
    if FLAT:
        return os.path.join(OUT, "index.html" if slug == "" else f"{slug}.html")
    return os.path.join(OUT, "index.html" if slug == "" else os.path.join(slug, "index.html"))

GENERATED = ["index.html", "404.html", "robots.txt", "sitemap.xml", ".nojekyll", os.path.join("assets", "styles.css"), "images"]

def clean():
    """Remove previously generated output only (never the whole repo root)."""
    if FLAT:
        if os.path.isdir(OUT):
            shutil.rmtree(OUT)
        os.makedirs(OUT)
        return
    for name in GENERATED + list(C.PAGES[k]["slug"] for k in C.PAGES if C.PAGES[k]["slug"]) + C.SERVICE_ORDER:
        path = os.path.join(OUT, name)
        if name == "images":
            if os.path.isdir(path):
                for f in os.listdir(path):
                    if f.endswith(".svg"):
                        os.remove(os.path.join(path, f))
            continue
        if os.path.isdir(path):
            shutil.rmtree(path)
        elif os.path.isfile(path):
            os.remove(path)

def main():
    clean()
    builders = {
        "": (C.PAGES["index"], page_home),
        "about": (C.PAGES["about"], page_about),
        "services": (C.PAGES["services"], page_services),
        "skincare": (C.PAGES["skincare"], page_skincare),
        "skincare-consultations": (C.PAGES["skincare-consultations"], page_skincare_consultations),
        "faqs": (C.PAGES["faqs"], page_faqs),
        "blog": (C.PAGES["blog"], page_blog),
        "book": (C.PAGES["book"], page_book),
    }
    for k in C.SERVICE_ORDER:
        builders[k] = (C.SERVICES[k], lambda k=k: page_service(k))
    global PREFIX
    for slug, (meta, fn) in builders.items():
        PREFIX = "" if (FLAT or slug == "") else "../"
        write(out_path(slug), document(meta, fn(), is_index=(slug == "")))
    PREFIX = ""
    write(os.path.join(OUT, "404.html"), document(dict(title="Page Not Found | Isabelle Joseph, DNP", description="Page not found.", slug="404"), page_404()))
    if not FLAT:
        write(os.path.join(OUT, ".nojekyll"), "")
    if not FLAT:
        write(os.path.join(OUT, "assets", "styles.css"), CSS)
        write(os.path.join(OUT, "robots.txt"), f"User-agent: *\nAllow: /\nSitemap: {C.SITE_URL}/sitemap.xml\n")
        urls = [""] + [s for s in builders if s]
        today = datetime.date.today().isoformat()
        sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
            f'  <url><loc>{C.SITE_URL}/{(s + "/") if s else ""}</loc><lastmod>{today}</lastmod><priority>{"1.0" if s == "" else ("0.9" if s in C.SERVICES else "0.8")}</priority></url>\n' for s in urls) + "</urlset>\n"
        write(os.path.join(OUT, "sitemap.xml"), sm)
    for name, svg in PLACEHOLDERS.items():
        if not real_image(name):
            write(os.path.join(OUT, "images", f"{name}.svg"), svg)
    print(f"Built {len(builders)+1} pages and {len(PLACEHOLDERS)} placeholder images -> {OUT}")

if __name__ == "__main__":
    main()
