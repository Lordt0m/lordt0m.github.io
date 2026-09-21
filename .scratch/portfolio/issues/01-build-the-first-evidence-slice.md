# 01: Build the first evidence slice

**Status:** completed

## Outcome

Deliver a coherent local page containing the approved hero, the complete ShelfSum Featured Project proof, the Credence Supporting Project proof, and verified contact actions, with the repository's structural verification interface in place.

## Read

- `AGENTS.md`
- `.scratch/portfolio/spec.md`
- `docs/content.md`: Identity and positioning; Featured Project: ShelfSum; Supporting Project: Credence; Contact actions
- `docs/architecture.md`: Public document, Presentation, Asset, and Verification modules
- `docs/adr/0001-use-a-static-progressively-enhanced-site.md`

## Acceptance

- [x] Create semantic `index.html` with a skip link, header navigation, hero, `main-content`, `projects`, one complete ShelfSum Project Proof Block, one complete Credence Project Proof Block, `contact`, and a minimal footer.
- [x] Use the approved wording and verified actions from `docs/content.md`; render GitHub and the confirmed recruiter email, but do not render withheld CV, LinkedIn, screenshots, About, Skills, or journal content.
- [x] Render the verified GitHub destination and `mailto:ayotomiwa529@gmail.com` in the Contact section; GitHub may also appear in the hero when the action hierarchy remains clear.
- [x] Create `assets/css/site.css` with named tokens, visible focus, bounded reading widths, and responsive behaviour from 320 CSS pixels upward.
- [x] Keep the page fully usable without JavaScript. Create no JavaScript file unless an accepted interaction proves necessary.
- [x] Create `scripts/verify_site.py` with the stable interface and checks defined in `docs/architecture.md` for the content that exists in this slice.
- [x] Add focused standard-library tests for the verifier's pass and material failure cases.
- [x] Provide accurate title, description, canonical-ready metadata, and social text; do not invent a deployed canonical URL or social image.
- [x] Run the verifier and its tests.
- [x] Serve the site locally and inspect 360, 768, 1024, and 1440 CSS-pixel widths, including keyboard navigation and visible focus.
- [x] Confirm local and external links, no page-level horizontal overflow, and no withheld content or placeholders.
- [x] Review the final diff against this ticket, commit one truthful slice, and append the completion record.

## Write boundary

This ticket may create only the first public slice, its stylesheet, verification module, verifier tests, and directly required documentation repairs. It must not add deployment configuration, speculative sections, claims beyond `docs/content.md`, a framework, a CMS, or visual assets.

## Completion record

- **Commit or reviewed ref:** Ticket 01 vertical slice on branch `main`
- **Public behaviour delivered:**
  - Semantic, accessible HTML structure in `index.html` with skip link, header navigation, hero section with Lagos positioning and availability statement, complete ShelfSum Featured Project Proof Block with problem, delivered behaviour, engineering evidence, trade-offs, and live demo / source code inspection actions, complete Credence Supporting Project Proof Block with source code inspection action, Contact section with verified email (`mailto:ayotomiwa529@gmail.com`) and GitHub links, and minimal footer.
  - Zero JavaScript runtime; pure CSS design system in `assets/css/site.css` with named tokens, editorial styling, bounded reading widths, responsive flex/grid layouts, and visible focus rings.
  - Withheld content strictly excluded: no CV download link or asset, no LinkedIn link, no placeholder images or screenshots, no About or Skills sections, and no private journal.
- **Automated checks and outcomes:**
  - `python scripts/verify_site.py`: PASS (0 errors).
  - `python -m unittest discover tests`: PASS (14 tests passed in 0.8s, 0 failures).
- **Inspected viewports and material findings:**
  - Inspected viewports: 320px, 360px, 768px, 1024px, 1440px via local HTTP server and headless Chrome.
  - Zero horizontal overflow across all widths (`scrollWidth <= innerWidth`).
  - Keyboard navigation verified: Skip link jumps to `#main-content`, moves from offscreen (`top: -9999px`) to visible (`top: 16px`) when focused.
  - High-contrast visible focus outline (`3px solid #0f766e` with 3px offset) on all interactive links.
  - Touch targets meet or exceed 44px height across all navigation and action controls.
  - Contrast ratios exceed WCAG requirements: text `#18181b` on `#fafafa` (>16:1, AAA), accent `#0f766e` on white (>5.3:1, AA).
- **Evidence and content changes:**
  - Preserved approved wording from `docs/content.md` for identity, availability, ShelfSum, Credence, and contact.
  - All external destinations validated against `APPROVED_EXTERNAL_URLS`.
- **Remaining risks and next ticket's first safe action:**
  - Remaining risks: CV PDF asset is not yet generated/verified; LinkedIn profile URL is pending owner confirmation; screenshots withheld pending ShelfSum ticket 13 completion.
  - Next safe action: In Ticket 02, verify CV PDF content and place at `assets/documents/ayotomiwa-ojo-cv.pdf` before rendering download action.
