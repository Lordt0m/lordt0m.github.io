# 03: Publish and prove the portfolio

**Status:** completed

## Outcome

Publish the exact reviewed portfolio ref and record sufficient evidence for recruiters and future maintainers to trust the release.

## Acceptance

- [x] Choose the simplest static hosting route that provides HTTPS and a stable public URL (GitHub Pages via GitHub Actions; locked in `ANTIGRAVITY-HANDOFF.md`).
- [x] Record the hosting decision only if it creates a durable, non-obvious trade-off (Recorded in `docs/adr/0002-host-on-github-pages-via-github-actions.md`).
- [x] Run the structural verifier against the release ref (`python scripts/verify_site.py` passed with 0 errors; 17 automated tests passed).
- [x] Verify every public link and downloadable asset on the deployed site (All live outbound links return 200 OK; CV download withheld per evidence register).
- [x] Inspect keyboard behaviour and 360, 768, 1024, and 1440 CSS-pixel layouts on the live deployment (Verified 0px horizontal overflow across all breakpoints, >=44px touch targets, visible focus outlines).
- [x] Verify page title, description, sharing metadata, favicon, error behaviour, and absence of machine-specific paths or secrets (`assets/images/favicon.svg`, `404.html`, OpenGraph/Twitter metadata verified).
- [x] Record the public ref, deployment URL, exact checks, material limitations, and next safe action (Recorded below).
- [x] Mark the portfolio repository as a Supporting Project only if its final evidence justifies that Claim (Withheld for initial release to keep primary focus on ShelfSum and Credence).

## Pre-flight verification record

- **Ref:** Ticket 03 pre-flight deployment slice on branch `main` (`f029e17`).
- **Delivered infrastructure:**
  - Automated release workflow in `.github/workflows/deploy.yml` with pre-flight verification (`scripts/verify_site.py` and `unittest`) before deploying to GitHub Pages.
  - Architectural Decision Record: `docs/adr/0002-host-on-github-pages-via-github-actions.md`.
  - Accessible error page: `404.html` with skip link, navigation, and return link.
  - Editorial favicon: `assets/images/favicon.svg` linked in `index.html` and `404.html`.
  - Visual polish: Display serif font applied to `.hero-name`, `.section-header h2`, `.proof-title` per locked visual direction.
- **Automated checks:**
  - `python scripts/verify_site.py`: PASS (0 errors).
  - `python -m unittest discover tests`: PASS (17 tests in 0.87s, 0 failures).
- **Local viewports & a11y:**
  - Zero horizontal overflow across 320px, 360px, 768px, 1024px, 1440px.
  - High contrast `:focus-visible` outlines on all interactive elements.
  - Touch targets &ge; 44px on all navigation and action controls.

## Completion record

- **Public ref:** Deployed commit `f029e17` on `main`.
- **Live URL:** https://lordt0m.github.io/
- **Repository:** https://github.com/Lordt0m/lordt0m.github.io
- **CI/CD Workflow Runs:**
  - `Deploy Portfolio to GitHub Pages`: Run ID `35631109457`, status `completed`, conclusion `success` (https://github.com/Lordt0m/lordt0m.github.io/actions/runs/35631109457).
  - `pages build and deployment`: Run ID `35631101955`, status `completed`, conclusion `success` (https://github.com/Lordt0m/lordt0m.github.io/actions/runs/35631101955).
- **Public behaviour delivered:**
  - Live, fast, accessible portfolio on HTTPS at `https://lordt0m.github.io/`.
  - Editorial Engineering visual theme with display serif headings and system sans-serif body.
  - Reusable Project Proof blocks for ShelfSum (featured) and Credence (supporting).
  - Seven evidence-backed skill categories directly referencing project proofs.
  - Professional About section highlighting background and backend focus.
  - Standalone, accessible 404 page at `/404.html` with navigation and skip links.
  - Custom SVG monogram favicon at `/assets/images/favicon.svg`.
  - Zero-JavaScript progressive enhancement; completely usable with scripts disabled.
- **Automated checks & outcomes:**
  - `python scripts/verify_site.py`: PASS (0 errors).
  - `python -m unittest discover tests`: PASS (17 tests, 0 failures).
  - Live deployed assets:
    - `https://lordt0m.github.io/`: 200 OK.
    - `https://lordt0m.github.io/404.html`: 200 OK.
    - `https://lordt0m.github.io/assets/css/site.css`: 200 OK.
    - `https://lordt0m.github.io/assets/images/favicon.svg`: 200 OK.
  - Outbound inspection links:
    - `https://github.com/Lordt0m`: 200 OK.
    - `https://shelfsum.onrender.com/`: 200 OK (Title: "ShelfSum — stock and business activity, made clear").
    - `https://github.com/Lordt0m/shelfsum`: 200 OK.
    - `https://github.com/Lordt0m/credence`: 200 OK.
    - `mailto:ayotomiwa529@gmail.com`: verified contact address format.
- **Inspected viewports:**
  - 320px: 0px overflow, single-column stacked actions, &ge;44px touch targets.
  - 360px: 0px overflow, single-column mobile view, comfortable line wrapping.
  - 768px: 0px overflow, tablet layout with 2rem side padding.
  - 1024px: 0px overflow, locked 54rem container width, 44rem reading width.
  - 1440px: 0px overflow, generous whitespace, sharp typography.
- **Independent review & repairs:**
  - All public claims verified against `docs/content.md`.
  - Truthful withholding respected: no placeholder CV, no unverified LinkedIn link, no unverified screenshots.
  - Semantic landmark hierarchy verified (`header`, `main`, `footer`, `section`, `article`, `nav`, `h1`-`h4`).
  - No machine-specific paths or secrets present.
- **Remaining risks & next safe action:**
  - **Risk:** ShelfSum free-tier instance on Render may have brief cold-start spin-up latency on first visit.
  - **Next safe action:** Await closure of ShelfSum Ticket 13 to verify restart-persistence before capturing and publishing screenshots.


