# Rebuild the portfolio as a recruiter first project showcase

Written against: `0322363b30253c9266b8a0d42133428861ab258c`

## Evidence chain

- Surface: `index.html`, `assets/css/site.css`, and the deployed homepage.
- Problem: the current page is accurate but dense. Long proof blocks, seven skill cards, repeated availability text, and text-first project sections make a recruiter's first scan slower than necessary.
- Design evidence: the owner selected `https://www.cyze.dev/` as the visual reference. Its useful qualities are a deep navy canvas, restrained blue accent, compact introduction, generous whitespace, quiet typography, and large image-led work previews.
- Owner: `index.html` owns homepage copy and order; `assets/css/site.css` owns presentation; new project case-study documents own deeper evidence.
- Scope and affected surfaces: homepage, ShelfSum case study, Credence case study, shared stylesheet, project images, `404.html`, verification scripts and tests.
- Uncertainty: exact image crops may need adjustment after responsive rendering. The reference is inspiration, not a pixel-for-pixel template.

## Design decision

Replace the existing light editorial proof-sheet presentation with a dark, image-led portfolio that keeps the repository's static, semantic, progressively enhanced architecture. Borrow the reference's calm visual rhythm and strong work imagery without copying its identity, content, layout details, or interactions.

The homepage becomes a fast recruiter overview. It introduces Ayotomiwa, shows ShelfSum and Credence immediately, lists only the most relevant skills, summarizes the self-taught background, and makes contact easy. Detailed architecture, tests, limitations, and trade-offs move to dedicated static case-study pages.

Do not add React, a component framework, a CMS, a build pipeline, an animation system, or a frontend dependency. JavaScript is unnecessary unless a small accessible enhancement is later proven essential.

## Reuse

- Reuse the semantic landmarks, skip link, visible focus treatment, shared stylesheet ownership, repository-relative asset paths, and `python scripts/verify_site.py` interface.
- Reuse ShelfSum screenshots from the owner-supplied local ShelfSum repository under `docs/screenshots/` after verifying them against the current repository and live deployment.
- Reuse Credence's fictional demonstration fixture and verified outputs from the owner-supplied local Credence repository under `fixtures/`.
- Exemplar: `https://www.cyze.dev/` for visual mood and information restraint only.

## Changes

1. `index.html`
   - Change: build a concise opening with the exact hierarchy below.
     - Name: `Ayotomiwa Ojo`
     - Role: `Python & Django Developer`
     - Primary line: `I build practical web applications and backend systems with Python and Django.`
     - Availability: `Self-taught developer based in Lagos, Nigeria. Open to junior developer and internship opportunities.`
     - Primary actions: `View projects`, `Download CV`, and `Email me`.
     - Secondary action: `GitHub`.
     - Navigation: `Projects`, `Skills`, `About`, `Contact`, and `GitHub`.
   - Preserve: truthful junior positioning, Lagos location, GitHub and email destinations, one `h1`, keyboard access, and full usability without JavaScript.
   - Verify: a recruiter can identify role, location, availability, projects, CV, and contact route without scrolling through repeated claims.

2. `index.html` project overview
   - Change: show exactly two image-led project entries, ShelfSum first and Credence second. Each entry must contain 80 to 120 words excluding labels, one useful real preview, exactly three concrete capabilities, a concise technology line, and immediately visible inspection actions.
   - ShelfSum actions: `Live demo`, `Source code`, `Case study`.
   - ShelfSum demo note: `The free demo may take a moment to start after inactivity.` Show the two published demo identities and passwords beside the demo link in an accessible disclosure or compact text block; screenshots remain available as the immediate alternative preview.
   - Credence actions: `Source code`, `Case study`. Do not invent a live demo.
   - Preserve: all claims must remain supported by the project repositories.
   - Verify: both projects are understandable at a glance and no architecture essay appears on the homepage.

3. `projects/shelfsum.html`
   - Change: create a static case study covering the user problem, intended users, what it does, three to five engineering decisions, testing evidence, deployment facts, limitations, and links to live demo and source.
   - Use plain headings such as `The problem`, `What it does`, `How it works`, `Key decisions`, `Testing`, and `Limitations`.
   - Preserve: distinguish a deployed demonstration from customer usage; do not claim production customers, measured coverage, business impact, or employment work.
   - Verify: every substantive claim traces to ShelfSum's README, code, tests, ADRs, or release evidence.

4. `projects/credence.html`
   - Change: create a static case study covering the cashbook problem, validation flow, deterministic outputs, exact decimal calculations, safe publication behaviour, tests, and limitations.
   - Include a clearly labelled fictional sample showing selected input rows and the verified result: 10 processed rows, 4 valid rows, 6 invalid rows, 7 errors, NGN 75,000.00 income, NGN 59,500.50 expenses, and NGN 15,499.50 net cash movement.
   - Preserve: state that Credence is a local command-line tool with no hosted application.
   - Verify: values match `fixtures/mixed_cashbook.csv` and `fixtures/expected_mixed_output/` exactly.

5. `assets/images/projects/shelfsum/`
   - Change: copy no more than three current screenshots. Prefer the dashboard, products or movements view, and one mobile state. Crop only when it improves composition without hiding material UI.
   - Preserve: fictional data and visual accuracy.
   - Verify: descriptive alternative text identifies the useful state shown rather than repeating the project name.

6. `index.html` and `projects/credence.html`
   - Change: create a compact, accessible output preview from the actual fictional fixture and verified generated artifacts using semantic HTML and CSS for the tabular or terminal-like content.
   - Preserve: label it `Fictional sample data` and keep the values exact.
   - Verify: the preview remains readable on a 360px viewport and never requires horizontal page scrolling.

7. `index.html` skills
   - Change: replace seven verbose cards with five concise evidence-linked groups: `Python`, `Django`, `SQL & PostgreSQL`, `HTML & CSS`, and `Git & GitHub`.
   - Mention testing, CI, deployment, CSV, JSON, pytest, Render, Neon, and GitHub Actions only inside the relevant project evidence where they are demonstrated. Do not present every library as a separate skill.
   - Preserve: skills remain evidence-backed.
   - Verify: the entire skills section is scannable in seconds and contains no proficiency meters, logos, percentages, or generic tool wall.

8. `index.html` About and Contact
   - Change: use two short About paragraphs. State that Ayotomiwa is self-taught, focused on backend development, and holds a B.A. in English and Literary Studies from Federal University Oye-Ekiti. Connect the degree to clear technical communication and documentation without overstating expertise.
   - Change: keep email and GitHub active. Display `LinkedIn — coming soon` as inert text, not an anchor, disabled control, empty icon, or `#` link.
   - Preserve: do not place the phone number on the homepage. It may remain in the downloadable CV.
   - Verify: availability appears once, contact actions work, and LinkedIn cannot be mistaken for a broken link.

9. `assets/css/site.css`
   - Change: introduce a coherent dark visual system inspired by the reference: deep navy background, slightly lighter project surfaces, soft cool-blue accent, high-contrast warm-white text, restrained muted text, generous vertical spacing, rounded image frames, and a maximum reading width that keeps lines comfortable.
   - Use a clean system sans-serif throughout unless one restrained display face is already available without a network dependency. Avoid copying Cyze's exact colors or proportions.
   - Add subtle hover and focus transitions only. Respect `prefers-reduced-motion`.
   - Preserve: touch targets at least 44px, strong visible focus, semantic reading order, and no page-level overflow.
   - Verify: project imagery dominates the work section on desktop while content stacks naturally on mobile.

10. `404.html`
    - Change: apply the new tokens and navigation style.
    - Preserve: standalone accessibility, skip link, and a clear route back to the homepage.
    - Verify: no stale light-theme styling remains.

11. `scripts/verify_site.py` and `tests/`
    - Change: extend local-link and asset checks to every public HTML document; require CV, project pages, image alternative text, exact navigation targets, and evidence-controlled external links.
    - Preserve: standard-library-only implementation and stable command interface.
    - Verify: a missing case study, image, alternative text, CV, or broken relative link causes an actionable failure.

## Scope

- Inherit: homepage, project case studies, 404 page, and all shared navigation and design tokens.
- Verify: document metadata, social copy, favicon contrast, screenshots, demo guidance, case-study links, and every local or external destination.
- Exclude: changes to ShelfSum authentication or backend behaviour, changes to Credence behaviour, a blog, CMS, analytics, contact form storage, theme switcher, social feed, testimonials, skill ratings, or speculative projects.

## Validation

- Product: a recruiter can understand Ayotomiwa's positioning, inspect ShelfSum and Credence, download the CV, and send email without guessing where to click.
- Interface: inspect homepage, both case studies, and 404 page at 360, 768, 1024, and 1440 CSS pixels. Check keyboard-only navigation, visible focus, readable text, image loading, reduced motion, and zero horizontal overflow.
- System: confirm that one stylesheet owns shared presentation and that project detail lives in case-study pages rather than duplicated homepage essays.
- Repository: `python scripts/verify_site.py` and `python -m unittest discover tests` must pass.

## Stop conditions

- Stop if a proposed public statement cannot be verified from the supplied CV or a project repository.
- Stop if a screenshot contains private or non-fictional data.
- Stop rather than inventing a LinkedIn URL, employment history, customer usage, project date, metric, or personal contribution.

## Design documentation

- After acceptance and validation: update `.scratch/portfolio/spec.md`, `docs/content.md`, `docs/architecture.md`, and the visual-direction ADR so they describe the accepted dark, image-led system and the two case-study pages.
