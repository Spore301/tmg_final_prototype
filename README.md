# Thermal Motion Group — Phase 2 Final Prototype

A high-fidelity, fully responsive HTML/CSS/JS prototype for the Thermal Motion Group (TMG) website. This is a static front-end prototype — no build tools, no frameworks, no dependencies beyond Google Fonts and Phosphor Icons loaded via CDN.

---

## What This Is

TMG is a US-based manufacturer and distributor of aftermarket industrial cooling systems — radiators, hydraulic oil coolers, gen-set coolers, mining rack coolers, and more. The site serves a dual audience:

- **B2B buyers** who need to spec and enquire about custom or high-volume cooling solutions
- **Direct purchasers** who want to buy stocked aftermarket radiators online (e-commerce flow)

This prototype covers the full user journey from discovery through to cart/quote submission, across desktop and mobile.

---

## Design Direction — "Industrial Architect"

The visual language is deliberately austere and structural. Think precision engineering drawings, not consumer retail.

**Core principles:**
- `border-radius: 0` everywhere — no rounded corners, ever
- Flat, architectural layouts with strong grid lines
- Typography does the heavy lifting — no decorative illustration
- Color is used sparingly and with intent (see token system below)
- White space is generous; density is reserved for data-heavy components

**Type system:**
| Role | Font | Notes |
|------|------|-------|
| Headings, labels, UI | Sofia Sans | Uppercase, tracked, weight 400 only |
| Body, editorial copy | Raleway | Weight 400 only — no bold |

**Color tokens:**
| Token | Value | Usage |
|-------|-------|-------|
| `--red` | `#C02B2D` | Primary CTA, accents, active states |
| `--red-h` | `#991B1B` | Red hover state |
| `--navy` | `#222F4B` | Primary text, secondary buttons, nav |
| `--pitch` | `#0F172A` | Headings, high-contrast text |
| `--surface` | `#F8FAFC` | Page background, input backgrounds |
| `--lines` | `#E2E8F0` | All borders and dividers |
| `--muted` | `#64748B` | Secondary text, labels, placeholders |
| `--deep` | `#334155` | Body copy |

**Division color system** — each product bucket has an assigned brand color used for pills, accents, and card borders:
| Division | Color |
|----------|-------|
| Aftermarket Radiators (TMG E-com) | `#222F4B` Navy |
| CJP Fabrication | `#1A5C7A` Teal |
| Power Transformers | `#C02B2D` Red |
| Battery Management | `#1B6B42` Green |
| Seals & Hydraulics | `#B0580F` Orange |
| Innovation & Prototyping | `#452080` Purple |

---

## Page Inventory

| File | Page | Purpose |
|------|------|---------|
| `index.html` | Homepage | Main entry point — hero switcher, product carousel, industry tiles, about, contact |
| `products.html` | Product Listing (PLP) | Full catalog with sidebar filters, sort, load more |
| `aftermarket-radiators.html` | Aftermarket Radiators | Sub-category / product family page for the core e-com bucket |
| `pdp.html` | Product Detail (PDP) | Single product — specs, imagery, pricing, quote CTA, tech docs |
| `cart.html` | Quote Cart | Review selected items before RFQ submission or checkout |
| `cart-drawer-snippet.html` | Cart Drawer (partial) | Off-canvas flyout cart — used as a snippet across pages |
| `auth.html` | Sign In / Sign Up | Authentication hub — login, registration, password recovery |
| `about.html` | About Us | Corporate profile — history, mission, manufacturing, values |
| `contact.html` | Contact Us | Enquiry form, office locations, support channels |
| `news.html` | News & Resources | Blog/press listing in grid format |
| `industries.html` | Industries Hub | Overview of all industrial sectors TMG serves |
| `data-centers.html` | Data Centers (Industry) | Example individual industry page — tailored solutions |
| `applications.html` | Applications | Real-world use cases across machinery and processes |
| `solutions.html` | Solutions | Custom engineering and manufacturing services |
| `search.html` | Search Results | Global site search results page |
| `404.html` | 404 Not Found | Error page |

---

## User Flow Architecture

There are four primary paths through the site:

```
SHOPPING FLOW
Homepage → Product List → Product Detail → Cart → Checkout → Confirmation

DISCOVERY FLOW (industry-first)
Homepage → Industries Hub → Industry Page → Application → Product Detail

BUCKET FLOW (division-first)
Homepage → Bucket Cards → Bucket Page → Product List (filtered)

CONTENT FLOW
Blog List → Blog Post  ·  About  ·  FAQ  ·  Contact
```

### E-commerce vs. Enquiry split

Only **Bucket 1 (Aftermarket Radiators / TMG E-com)** has full add-to-cart and buy-now functionality. All other product buckets (Power Transformers, Battery Management, etc.) route through an **Enquire Now** modal that pre-fills context from the referring page. This is a deliberate B2B design decision — high-value custom products don't suit a standard checkout flow.

---

## Key Components & Patterns

### Announcement Bar
Red full-bleed strip at the very top. Used for stock alerts, event notices, or promotions. Centered on desktop, left-aligned on mobile.

### Sticky Navigation
White bar with logo, nav links (desktop), hamburger (mobile), search icon, account icon, and cart icon with badge count. Stays fixed on scroll. Includes dropdown menus for Solutions and Resources.

### Hero — Industry Switcher
Full-bleed dark hero with an industry strip at the bottom. Six industry tabs auto-advance every 5 seconds (disabled on mobile). Clicking a tab swaps the background image, headline, and subheading with a fade transition. Progress bar per tab shows time remaining.

### Product Cards
Consistent card anatomy across all listing pages:
1. Division color pill (top-left badge)
2. Availability badge (top-right — IN STOCK / ENQUIRE / REQUEST QUOTE)
3. Product image (1:1, `mix-blend-mode: multiply` on white bg)
4. Product name
5. Industry tag pills
6. 3 spec bullet points
7. Price or "Request a Quote"
8. CTA buttons — `[ADD TO CART]` + `[BUY NOW]` for e-com, `[ENQUIRE]` + `[VIEW DETAILS]` for non-e-com

### Sidebar Filters (Products page)
Sticky sidebar on desktop with collapsible filter groups: Product Type, Industry, Availability, Price Range. On mobile, filters live in a slide-in drawer triggered by a "FILTERS" button. Active filters render as dismissible pills in the sort bar.

### Enquiry Modal
Triggered by any non-e-com product CTA or the global "Enquire Now" buttons. Pre-fills product name and context. Fields: Name, Email, Company, Message. Closes on overlay click or X button.

### Trust Ticker
Infinite CSS marquee of OEM partner names (Caterpillar, Cummins, John Deere, etc.). Opacity 0.25 at rest, full opacity on hover.

### Stats Bar
4-column grid of key numbers — years in manufacturing, industries served, lead time, product count. Full-bleed navy background.

---

## Responsive Behavior

| Breakpoint | Behavior |
|------------|----------|
| `≥ 1280px` | 4-column product grid, full sidebar, all nav links visible |
| `1024–1279px` | 3-column product grid |
| `768–1023px` | 2-column product grid, sidebar visible, hamburger nav |
| `< 768px` | 1-column grid, filter drawer, hamburger nav, hero auto-rotate off |

Mobile-specific adjustments:
- `ph-count` (product count in page header) visible only on mobile — the sort bar handles this on desktop
- Social icons in utility bar hidden on mobile
- Cart drawer full-width on mobile
- CTA rows stack vertically

---

## Assets

```
assets/
  logo/
    TMG Logo.svg          — dark version (nav, light backgrounds)
    TMG Logo_White.svg    — white version (footer, dark backgrounds)
  hero-images/
    agriculture.png
    crypto_data_centers.png
    Hydraulics.png
    oil_and_gas.png
    power_generation.png
    trucking.png
  products/
    cad_*.png             — CAD-style product renders (white bg, multiply blend)
    *_[timestamp].png     — photographic product shots
```

---

## JavaScript Approach

All JS is vanilla, inline per-page. No bundler, no framework. Key behaviors:

- **Hero switcher** — tab click + auto-advance timer with progress bar animation
- **Mobile menu** — hamburger toggle with CSS transition
- **Product grid** — JS-rendered from a `products[]` data array; supports filter, sort, and load-more
- **Sidebar filters** — checkbox state management with pill rendering and clear-all
- **Custom select dropdowns** — replaces native `<select>` for consistent cross-browser styling
- **Enquiry modal** — open/close with overlay, pre-fill from product context
- **Cart** — localStorage-backed cart count badge, drawer open/close
- **Testimonial rotator** — stacked list with prev/active/next CSS states, auto-advances

---

## What's Intentionally Placeholder

- Phone number: `(+1) 555-000-0000`
- Email: `info@thermalmotion.com`
- Location: `[City, State]`
- Stats: `[X] Years`, `[X]+ Products` — awaiting real data
- Customer testimonials — placeholder copy, real quotes needed before launch
- OEM partner names in the trust ticker — require written approval before going live
- Product pricing — "From $X" figures are illustrative

---

## Running the Prototype

No build step required. Open any `.html` file directly in a browser, or serve the folder with any static file server:

```bash
# Python
python -m http.server 8080

# Node (npx)
npx serve .
```

All asset paths are relative, so the site works from any directory as long as the folder structure is intact.

---

## File Utilities

| File | Purpose |
|------|---------|
| `build.py` | Python script for any build/copy tasks during development |
| `cleanup.py` | Utility script for cleaning up temp or duplicate files |
| `screens_knowledge_base.md` | Inventory of all screens with titles and purposes |

---

*Thermal Motion Group — Keeping Industry Moving*
