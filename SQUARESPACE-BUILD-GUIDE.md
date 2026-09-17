# Isabelle Joseph, DNP, NP-BC — Squarespace 7.1 Build Guide

**Platform:** Squarespace 7.1 · Fluid Engine · 100% native blocks · no custom code
**Live preview of this design:** https://aririkushimeikito.github.io/josh1/ (static pages at this repo's root) — every section below exists in the preview so the Squarespace editor can match it 1:1.
**Sources used:** Brand Guide (colors + type), Website Sitemap + Team Guide, Homepage / About / Services Hub / Tox / Hyperhidrosis / Chemical Peels / GLP-1 / HRT / Hair Loss Content Blueprints, previous-site `sitemap.xml`.

Anything shown as `[IN BRACKETS]` is content that still needs to be supplied (see Section G). No medical facts, credentials, reviews, or locations were invented; all copy is transcribed from the blueprints.

---

## A. Website Architecture

### Primary navigation (Pages panel → Main Navigation)

```
HOME | ABOUT | SERVICES ▾ | SKINCARE | THE ISABELLE EDIT | BOOK
```

`BOOK` is styled as a button (Header → Elements → Button) linking to the Skin Clique booking URL. Squarespace's header button is the native "emphasized nav item" and needs no code.

### Page tree

| Nav label | Page type | URL slug | Notes |
|---|---|---|---|
| Home | Page (set as Homepage) | `/` | |
| About | Page | `/about` | "Meet Isabelle" |
| Services | **Folder** (with an index page inside, or link folder title to `/services`) | `/services` | Dropdown shows the 8 service pages below |
| ↳ Tox | Page | `/tox` | Aesthetics |
| ↳ Hyperhidrosis | Page | `/hyperhidrosis` | Aesthetics |
| ↳ Chemical Peels | Page | `/chemical-peels` | Aesthetics |
| ↳ GLP-1 Weight Management | Page | `/weight-loss` | Wellness |
| ↳ Hormone Replacement Therapy | Page | `/hormone-replacement-therapy` | Wellness |
| ↳ Hair Loss | Page | `/hair-loss` | Wellness |
| ↳ Skincare | (same page as top-level Skincare) | `/skincare` | Skin Health |
| ↳ Skincare Consultations | Page | `/skincare-consultations` | Skin Health |
| Skincare | Page | `/skincare` | Shop + product education |
| The Isabelle Edit | **Blog collection** | `/blog` | Categories: Skin, Wellness, Aesthetics, Education, Lifestyle |
| Book | Page | `/book` | Transition page → external Skin Clique booking |
| *(Not linked / footer)* FAQs | Page | `/faqs` | |
| *(Not linked)* 404 | Set under Design → 404 page | | |

**Squarespace folder note:** Squarespace 7.1 dropdown folders are a flat list. Group labels ("Aesthetics / Wellness / Skin Health") cannot be added natively inside a dropdown, so the dropdown lists the 8 pages with "All Services" first; the grouping is expressed on the `/services` hub page itself. The preview shows the grouped version as the ideal; use the flat version in Squarespace.

### Internal-linking architecture

- Home → Services → each Service → Book
- Home → About → Book
- Home → Skincare → Shop (external)
- Home → The Isabelle Edit → Services
- Every service page cross-links: Tox ↔ Chemical Peels ↔ Skincare; GLP-1 ↔ HRT ↔ Hair Loss; every page → FAQs, Book.

### Legacy URL redirects (Settings → Developer Tools → URL Mappings)

```
/about.html -> /about 301
/services-xeomin.html -> /tox 301
/services-chemical-peels.html -> /chemical-peels 301
/services-rx-skincare.html -> /skincare 301
/services-glp1-weight-management.html -> /weight-loss 301
/services-hair-loss.html -> /hair-loss 301
/faq.html -> /faqs 301
```

---

## B. Global Design System

### Colors (Design → Colors → Custom palette)

| Palette slot | Name | Hex | Used for |
|---|---|---|---|
| Accent | Terracotta | `#C17B5E` | Primary buttons, eyebrow labels, accordion "+", hover states |
| Dark | Deep Brown | `#2C2318` | Headings, body text, nav, dark CTA sections |
| Light 2 | Warm Linen | `#F0EAE2` | Alternating section backgrounds, footer |
| Secondary accent | Sage | `#8A9B80` | Bullet markers, category labels, one "consultation" CTA band (tinted `#DCE2D5`) |
| Light 1 | Cream | `#FAF7F3` | Page background, header |

**Section themes to create (Design → Colors → Section themes):**
1. **Lightest 1** = Cream background, Deep Brown text, Terracotta primary button.
2. **Lightest 2** = Warm Linen background, same text/buttons.
3. **Light** = Sage-tint `#DCE2D5` background (used once on Home).
4. **Darkest** = Deep Brown background, Cream text, Terracotta primary button, Cream-outline secondary button.

Never use Terracotta or Sage as full section backgrounds except the single sage band on Home.

### Typography (Design → Fonts → Custom)

| Role | Font | Size (desktop) | Notes |
|---|---|---|---|
| Heading 1 | DM Serif Display, 400 | 60–68px, line-height 1.05 | One per page |
| Heading 2 | DM Serif Display | 40–46px, lh 1.1 | Section titles |
| Heading 3 | DM Serif Display | 22–26px | Sub-items / steps |
| Heading 4 | DM Sans 500 | 17px | Accordion questions |
| Paragraph 1 (large) | DM Sans 400 | 18px | Hero copy |
| Paragraph 2 (body) | DM Sans 400 | 17px, lh 1.65, color Deep Brown | |
| Paragraph 3 (small) | DM Sans | 14–15px, muted | Notes, captions, disclaimers |
| Eyebrow / labels | DM Sans 600 | 12px, letter-spacing .16em, uppercase, Terracotta | Use Paragraph 3 + Terracotta color + uppercase |
| Buttons | DM Sans 600 | 13–14px, letter-spacing .09em, uppercase | |
| Site title | DM Serif Display | 23px | "Isabelle Joseph, DNP" |

Both fonts are in Squarespace's Google Fonts list. Mobile: H1 38–42px, H2 30px, body 17px.

### Spacing

- Section padding: **Large** (Squarespace section height "L" ≈ 100–120px desktop, 60px mobile).
- Content width: Fluid Engine default (max 1180px), gutters "Medium".
- Paragraph max width: keep text blocks ≤ 8 grid columns (≈ 68 characters).
- Hairline rules: use the native **Line block** in Deep Brown at 15% opacity, 1px, between list rows.

### Buttons (Design → Buttons)

| Style | Fill | Text | Border | Radius |
|---|---|---|---|---|
| Primary | Terracotta | White | none | 2px |
| Secondary | Transparent | Deep Brown | 1.5px Deep Brown | 2px |
| Tertiary ("text link") | none | Terracotta-deep `#A9674C` | 1.5px bottom underline | 0 |
| Padding | 16px 28px | | | |
| Hover | Primary → `#A9674C`; Secondary → filled Deep Brown | | | |

### Navigation (Design → Site Header)

- Layout: **Option 1** (site title left, nav right), height 82px, fixed/sticky, Cream background at 94% (use the native "solid" style with slight transparency), 1px bottom border.
- Site title: "Isabelle Joseph, DNP" (text logo) + optional tagline "Concierge Aesthetics • Wellness • Skincare" (add tagline in Site Title settings; hide on mobile).
- Nav items: Home · About · Services ▾ · Skincare · The Isabelle Edit · (FAQs in footer only).
- Header button: **Book** → Skin Clique booking URL, Primary style at full size (Terracotta fill, white uppercase text, 16px × 28px padding, 2px radius).
- Mobile menu (≤1100px, so tablets too): native overlay, DM Sans uppercase items, Cream background, Book button full width. Hide the site tagline on phones.

### Footer (Design → Footer, one Fluid Engine section, Warm Linen)

4 columns desktop / 2 tablet / 1 mobile:
1. Brand: "Isabelle Joseph, DNP, NP-BC", tagline, service-area line, Book button.
2. Explore: Meet Isabelle · Services · Skincare · The Isabelle Edit · FAQs.
3. Services: Tox · Hyperhidrosis · Chemical Peels · GLP-1 Weight Management · HRT · Hair Loss · Prescription Skincare · Skincare Consultations.
4. Connect: Book With Isabelle · Shop Skincare · Instagram @isabellejosephDNP · Facebook `[LINK]` · isabellejoseph@skinclique.com · 617-634-5416 (text only).
Legal row: © year · Privacy Policy · Terms · `[HEALTHCARE DISCLAIMER]` · educational disclaimer.

### Imagery

- All photography: supplied portraits and lifestyle shots. Warm, natural light, natural skin, editorial crops (4:5 portrait, 3:4 tall, 1:1, 16:10 wide).
- Placeholders in the preview are named by intended shot (e.g. `home-hero.svg` = "Hero portrait of Isabelle — warm, natural light"). Replace 1:1.
- Image blocks: use **Image Block → Inline**, focal point set, no rounded corners (2px max), no shadows.
- Alt text: descriptive, human ("Isabelle Joseph, DNP, NP-BC in consultation with a patient").

### Reusable section patterns (save each as a Squarespace **Saved Section**)

| Pattern | Blocks | Reused on |
|---|---|---|
| **Editorial Hero** | Text (eyebrow) + H1 + P1 + 2 Buttons · Image (4:5) | Every page |
| **Editorial Split** | Image (5 cols) + Text (6 cols) + Button; mirrored variant | Home, About, Services, all Service pages, Skincare, Book |
| **Feature List** (rows with hairlines) | Text H3 + P + tertiary Button per row; Line blocks | Home concerns, Services hub, "What it addresses", Options |
| **Service Groups** (typographic) | 3 Text columns with H3 label + serif link list | Home, About |
| **Steps** | Text "Step n" label + H3 + P per row | Every service page, Consultations |
| **Checklist** | Text + bulleted Text block | "Is it right for me?", "Before your appointment" |
| **FAQ** | Text (sticky title) + **Accordion Block** | Every service page, FAQs page |
| **Related Pair** | 2 Text columns with H2 + P + tertiary button | Service pages, Blog, Consultations |
| **CTA Band** (Darkest theme) | Text H2 + P + Primary + Secondary Buttons | Every page (final section) |
| **Booking CTA** (Sage theme) | Text + Primary Button | Home |

---

## C. Page-by-Page Specification

Each section lists: background theme · blocks · desktop arrangement (24-col Fluid Engine grid) · mobile arrangement · CTA. Copy is final blueprint copy; see `tools/content.py` for the full text of every section.

### 1. Home `/`
Purpose: strongest brand expression; primary conversion = Book.

| # | Section | Theme | Blocks | Desktop | Mobile | CTA |
|---|---|---|---|---|---|---|
| 1 | Hero — "Expert Care. Personalized to You. Delivered Where You Are." | Cream | Text (eyebrow "Concierge Aesthetics + Wellness", H1, P1), 2 Buttons, Image | Text cols 1–13, Image cols 15–24 offset down 2 rows | Image first (4:3), then text, buttons full width | Book With Isabelle · Explore Services |
| 2 | Trust bar | Cream | 3 small Text blocks with sage dot bullet, Line above/below | 3 across | Stacked | — |
| 3 | Meet Isabelle | Cream | Image (cols 1–10) + Text (12–24) | Split | Stacked | Meet Isabelle → /about (tertiary) |
| 4 | The Concierge Difference | Linen | Text + 3-column "Convenient / Personal / Comfortable" Text blocks + Image right | Text 1–12, Image 14–24 | Image → text → trio stacked | Book a Visit |
| 5 | How Can I Help? (7 concerns) | Cream | Feature List, 2 columns | 2 cols | 1 col | Explore Tox … Explore Skincare (tertiary) |
| 6 | Explore Services | Linen | Service Groups, 3 columns | 3 cols | 1 col | Explore Aesthetics / Wellness / Skin Health |
| 7 | Skincare | Cream | Image + Text | Split | Stacked | Explore Skincare (secondary) · Shop With Isabelle (tertiary, external) |
| 8 | Consultation CTA | Sage tint | Text + Button | Left-aligned 14 cols | Full | Start With a Consultation |
| 9 | Testimonials `[TO BE PROVIDED]` | Cream | 3 Text blocks (Quote style) | 3 cols | 1 col | — |
| 10 | The Isabelle Edit | Linen | **Summary Block (Blog, Grid, 3 items)** | 3 cols | 1 col | Explore The Isabelle Edit |
| 11 | Service Area | Cream | Image (1:1) + Text | Split | Stacked | Check Availability + Book |
| 12 | Final Conversion | Darkest | CTA Band | 14 cols | Full | Book With Isabelle · Explore Services |

### 2. About `/about`
Purpose: trust, credentials, personal connection. H1 "Meet Isabelle Joseph, DNP, NP-BC".

Sections: Hero (portrait, tagline "Expert Care Starts With Truly Knowing Your Patient", Book) → Experience + Personal Care (Linen prose) → Aesthetic Philosophy (Split, CTA Explore Aesthetic Services) → Wellness Philosophy (Split mirrored, Linen) → Skincare (Split) → Concierge Care (Split mirrored, Linen, includes service-area paragraph) → Education + Clinical Experience (prose + 4-column credential row: DNP · Board-Certified NP · 15+ yrs · UPenn + Regis) → Beyond the Credentials (Split, Linen) → How Isabelle Can Help (Service Groups) → Final CTA (Darkest).

### 3. Services hub `/services`
H1 "Concierge Aesthetics, Wellness + Skincare". Hero → "Start With What You're Experiencing" (Linen prose) → **Aesthetics** feature list, 3 cols, anchor `#aesthetics` → **Wellness** (Linen) `#wellness` → **Skin Health** `#skin-health` → Concierge Difference (Split, Linen) → Related Pair ("You Don't Have to Figure It Out Alone" / "Explore. Learn. Decide.") → Final CTA. Anchor links: set each section's anchor in section settings.

### 4. Service Page Template (Tox, Hyperhidrosis, Chemical Peels, GLP-1, HRT, Hair Loss)
Identical order on all six; delete a row if a blueprint has no content for it.

| # | Section | Theme | Blocks |
|---|---|---|---|
| 1 | Hero: eyebrow = category, H1, serif tagline, intro, Book CTA + "All Services" | Cream | Text, 2 Buttons, Image |
| 2 | Overview ("What Is …?") | Linen | Text |
| 2b | Educational prose sections (e.g. "Perimenopause vs. Menopause") | Cream | Text |
| 3 | Who it may be for / What it addresses | Cream | Feature List + Book button |
| 3b | Options (GLP-1, HRT only) | Linen | Feature List + note |
| 4 | Isabelle's Approach | Cream | Split mirrored (Image + Text) |
| 5 | What to Expect (steps) | Linen | Steps + Button |
| 5b | Extra prose ("Will my skin peel?", "Side effects", "Hair growth takes time") | Cream | Text |
| 6 | Concierge / Provider section | Sage tint | Split |
| 7 | Is it right for me? | Cream | Checklist |
| 8 | Before / After appointment | Linen | Checklist or prose |
| 9 | FAQ | Cream | **Accordion Block** |
| 10 | Related pair (cross-links) | Linen | 2 Text columns |
| 11 | Not sure? | Cream | Prose + Book |
| 12 | Final CTA | Darkest | CTA Band |

### 5. Skincare `/skincare`
H1 "Skincare Shouldn't Be Guesswork." Hero (Shop Skincare primary, Book consultation secondary) → Three ways (Prescription / Consultations / Medical-Grade, Linen) → Selected Products `[PRODUCTS TO BE PROVIDED]` (4 Image+Text columns + Shop button + "Purchases complete on Skin Clique" note) → Philosophy split (Linen) → one Isabelle Edit article (Summary Block filtered to "Skin") → Final CTA.

### 6. Skincare Consultations `/skincare-consultations`
Hero → Concerns (feature list, Linen) → What to Expect (3 steps, last step marked `[DETAILS TO BE PROVIDED]`) → Related pair → Final CTA.

### 7. FAQs `/faqs`
Page intro + Book → topic jump row (Button blocks styled as pills, each linking to a section anchor; no JavaScript) → one Accordion Block per group, alternating Cream/Linen, each with a link back to its page: General + Booking 4 · Tox 10 · Hyperhidrosis 12 · Chemical Peels 12 · GLP-1 15 · HRT 11 · Hair Loss 16 · Prescription + Medical-Grade Skincare 3 · About the Practice 2 (85 total; blueprint FAQs plus the previous site's faq.html content) → "Still Have Questions?" CTA with the text-only number. Add the FAQPage JSON-LD to the page's header code injection for rich results.

### 8. The Isabelle Edit `/blog`
Native **Blog Page**, layout "Grid", 3 columns, image 4:3, show category + title + excerpt. Create categories: Skin, Wellness, Aesthetics, Education, Lifestyle. Draft the 3 launch posts as **drafts** (titles from blueprint) until content arrives. Below the list: Related Pair (Explore Services / Book).

### 9. Book `/book`
Page intro (H1 "Book With Isabelle", what to expect, Book button with "Opens Skin Clique in a new tab") → 3 mini-steps (Choose · Intake · Isabelle comes to you) → "Questions Before Booking?" split with FAQ button and `[CONTACT DETAILS]` (add a native **Form Block** here if a contact form is wanted) → Final CTA.

### 10. 404
H1 "Page Not Found" + Go Home / Book.

---

## D. Squarespace Build Map

| Page | Section | Squarespace element | Purpose |
|---|---|---|---|
| Global | Header | Site Header (Option 1) + Folder nav + Header Button | Navigation / booking |
| Global | Footer | Fluid Engine section, 4 Text blocks + Button | Wayfinding, legal |
| Home | Hero | Fluid Engine + Text + Image + 2 Buttons | Primary conversion |
| Home | Trust bar | 3 Text + 2 Line blocks | Credibility |
| Home | Meet Isabelle | Image + Text + Button | About |
| Home | Concierge Difference | Image + Text + 3 Text + Button | Positioning |
| Home | Concerns | 7 × (Text + Button) + Line blocks | Discovery |
| Home | Services | 3 × Text (linked list) + Buttons | Service discovery |
| Home | Skincare | Image + Text + 2 Buttons | Shop path |
| Home | Consultation CTA | Text + Button (Light theme) | Conversion |
| Home | Testimonials | 3 Text (Quote) | Trust |
| Home | Isabelle Edit | Summary Block (Blog) | Editorial |
| Home | Service area | Image + Text + Button | Local SEO |
| Home | Final CTA | Text + 2 Buttons (Darkest) | Conversion |
| About | Bio sections | Image + Text (+ Button) × 7 | Trust |
| About | Credentials | 4 Text columns + Lines | Credibility |
| Services | Category lists | Text + Buttons + Lines, anchored sections | Navigation |
| Service page | Overview / prose | Text | Education |
| Service page | Addresses / options | Text + Button rows | Education |
| Service page | Steps | Text rows | Expectation setting |
| Service page | FAQ | **Accordion Block** | Education / SEO |
| Service page | CTA | Text + Buttons | External booking |
| Skincare | Products | 4 × Image + Text, Button | Product education |
| Blog | Articles | **Native Blog collection** | Editorial |
| FAQs | Groups | Accordion Blocks | Education |
| Book | Booking CTA | Text + Button (+ optional Form Block) | External booking |

Fluid Engine settings: desktop grid 24 columns; enable "Fill Screen" off; section height L; use **block animations** only on hero images ("Fade") and CTA bands ("Fade") — nowhere else.

---

## E. Responsive Strategy

**Desktop (≥1180px):** asymmetric 7/5 and 5/6 splits, hero image offset 2 grid rows down for editorial tension, sticky FAQ title, 3-column lists.

**Tablet (641–1100px):** hamburger navigation; 3-column lists step down to 2 columns (feature lists, journal, testimonials); splits stack image-first below 860px; H1 44–56px.

**Mobile (≤ 640px) — arrange separately in Fluid Engine's mobile editor:**
- Every split: image first (crop 4:3), then eyebrow/heading/copy/buttons; buttons full-width, 48px tall.
- Hero H1 38–42px; body 17px; section padding 60px.
- Lists and steps single column; "Step n" label sits above the heading.
- Accordion full-width; sticky FAQ title becomes static.
- Trust bar becomes a vertical list.
- Footer 1 column; Book button full width.
- No horizontal scroll (verified in preview at 400px on every page).

---

## F. SEO Map

| Page | URL | H1 | SEO title | Meta description | Primary topic | Key internal links |
|---|---|---|---|---|---|---|
| Home | `/` | Expert Care. Personalized to You. Delivered Where You Are. | Concierge Aesthetics & Wellness \| Isabelle Joseph, DNP | Discover personalized concierge aesthetics, wellness and skincare with Isabelle Joseph, DNP, NP-BC, serving South Easton and surrounding MA communities. | Concierge aesthetics + wellness, South Easton MA | About, Services, all service pages, Skincare, Blog, Book |
| About | `/about` | Meet Isabelle Joseph, DNP, NP-BC | Meet Isabelle Joseph, DNP, NP-BC \| South Easton, MA | Meet Isabelle Joseph, DNP, NP-BC, a concierge aesthetics and wellness provider bringing personalized care to patients in South Easton, MA and surrounding communities. | Provider bio | Aesthetics, Wellness, Skincare, Tox, HRT, GLP-1, Consultations, Book |
| Services | `/services` | Concierge Aesthetics, Wellness + Skincare | Concierge Aesthetics & Wellness Services \| Isabelle Joseph | Explore concierge aesthetics, wellness and skincare services with Isabelle Joseph, DNP, NP-BC, serving South Easton and surrounding Massachusetts communities. | Services hub | Each service, Skincare, Blog, Book |
| Tox | `/tox` | Tox Treatments With Isabelle Joseph, DNP, NP-BC | Tox Treatments in South Easton, MA \| Isabelle Joseph, DNP | Explore personalized concierge Tox treatments with Isabelle Joseph, DNP, NP-BC, serving South Easton and select surrounding Massachusetts communities. | Tox / neuromodulators (local) | About, Services, Chemical Peels, Skincare, Consultations, Blog, Book |
| Hyperhidrosis | `/hyperhidrosis` | Hyperhidrosis Treatment With Isabelle Joseph, DNP, NP-BC | Hyperhidrosis Treatment in South Easton, MA \| Isabelle Joseph | Explore concierge treatment for excessive sweating of the underarms, palms and feet with Isabelle Joseph, DNP, NP-BC in South Easton, MA. | Excessive sweating (local) | Services, About, Tox, FAQs, Blog, Book |
| Chemical Peels | `/chemical-peels` | Chemical Peels With Isabelle Joseph, DNP, NP-BC | Chemical Peels in South Easton, MA \| Isabelle Joseph, DNP | Explore personalized concierge chemical peels with Isabelle Joseph, DNP, NP-BC for concerns including dullness, texture, pigmentation and congested skin. | Chemical peels (local) | Services, About, Skincare, Consultations, Tox, Blog, Book |
| GLP-1 | `/weight-loss` | GLP-1 Weight Management With Isabelle Joseph, DNP, NP-BC | GLP-1 Weight Management \| Isabelle Joseph, DNP | Explore medically supervised GLP-1 weight management with Isabelle Joseph, DNP, NP-BC, including personalized treatment and ongoing provider support. | GLP-1 / semaglutide / tirzepatide (not localized) | Services, About, HRT, Hair Loss, FAQs, Blog, Book |
| HRT | `/hormone-replacement-therapy` | Hormone Replacement Therapy With Isabelle Joseph, DNP, NP-BC | Hormone Replacement Therapy (HRT) \| Isabelle Joseph, DNP | Explore personalized hormone replacement therapy for perimenopause and menopause with Isabelle Joseph, DNP, NP-BC, including lab-guided care and ongoing support. | Perimenopause / menopause HRT (not localized) | GLP-1, Hair Loss, Services, About, FAQs, Blog, Book |
| Hair Loss | `/hair-loss` | Hair Loss Treatment With Isabelle Joseph, DNP, NP-BC | Hair Loss Treatment \| Isabelle Joseph, DNP | Explore personalized hair loss treatment with Isabelle Joseph, DNP, NP-BC, including medically guided topical and oral options for thinning hair and hair loss. | Thinning hair / minoxidil (not localized) | HRT, GLP-1, Services, About, Skincare, FAQs, Blog, Book |
| Skincare | `/skincare` | Skincare Shouldn't Be Guesswork. | Medical-Grade & Prescription Skincare \| Isabelle Joseph, DNP | Skincare shouldn't be guesswork. Explore medical-grade and prescription skincare guidance with Isabelle Joseph, DNP, NP-BC, and shop her curated Skin Clique storefront. | Medical-grade / prescription skincare | Consultations, Chemical Peels, Blog, Shop, Book |
| Consultations | `/skincare-consultations` | Personalized Skincare Consultations With Isabelle Joseph, DNP, NP-BC | Personalized Skincare Consultations \| Isabelle Joseph, DNP | Stop guessing which products belong in your routine. Book a personalized skincare consultation with Isabelle Joseph, DNP, NP-BC. | Skincare consultation | Skincare, Chemical Peels, Shop, Book |
| FAQs | `/faqs` | Frequently Asked Questions | Frequently Asked Questions \| Isabelle Joseph, DNP | Answers to common questions about Tox, hyperhidrosis treatment, chemical peels, GLP-1 weight management, hormone replacement therapy and hair loss care with Isabelle Joseph, DNP, NP-BC. | FAQ | Every service, Book |
| Blog | `/blog` | The Isabelle Edit | The Isabelle Edit \| Aesthetics, Skin + Wellness Education | The Isabelle Edit: straightforward education from Isabelle Joseph, DNP, NP-BC to help you better understand your options, your skin, and your health. | Editorial | Services, Book |
| Book | `/book` | Book With Isabelle | Book With Isabelle \| Isabelle Joseph, DNP, NP-BC | Book concierge aesthetic, wellness and skincare care with Isabelle Joseph, DNP, NP-BC. Appointments are scheduled securely through Skin Clique. | Booking | FAQs, Shop, Skin Clique |

Squarespace: enter SEO title/description per page under Page Settings → SEO. Set site-wide SEO title format to `%p | Isabelle Joseph, DNP`. Enable SSL, submit `/sitemap.xml` (auto-generated by Squarespace) to Search Console. Pricing is never hard-coded (per blueprint pricing notes).

---

## G. Content Requirements (still to be supplied)

**Images (42 placeholders, named in `images/`):**
- Home: hero portrait; seated editorial portrait; concierge doorway/at-home shot; skincare still life; local landscape (South Easton); 3 article covers.
- About: full-length portrait; natural-skin detail; wellness lifestyle; skincare routine; home-visit shot; candid personal (beach/travel).
- Services hub: hero with treatment kit; concierge appointment.
- Each service page (×6): hero image, "approach" image, concierge image.
- Skincare: hero; philosophy shot; 4 product images. Consultations: hero. Book: welcoming portrait.
- Logo / wordmark file if one exists (currently a text site title).

**Copy / information:**
- 3–5 approved patient testimonials (with permission + Skin Clique approval).
- Selected skincare products / categories and short education copy for the Skincare page.
- Skincare Consultations: any additional detail on format, duration, or what's included.
- Payment / cancellation policy FAQ answers, if wanted (booking logistics are now covered).
- Facebook URL (email, text number, and Instagram are in place from the previous site).
- Privacy Policy, Terms, and healthcare/site disclaimer text.
- The 3 launch articles for The Isabelle Edit (titles supplied; bodies not).
- Confirmation of whether `/skincare-consultations` should stay a separate page or merge into `/skincare`.
- Any hours / availability information to show on the Book page.

**Not invented, per instructions:** no additional credentials, awards, patient numbers, outcomes, or pricing were added. Service-area text uses only the six communities named in the blueprints.
