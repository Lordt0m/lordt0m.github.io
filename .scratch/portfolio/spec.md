# Portfolio specification

## Outcome

Create a precise, technically confident public portfolio that helps recruiters evaluate Ayotomiwa Ojo for Python and Django opportunities without overstating experience or making them search for evidence.

## Primary readers

- Recruiters and hiring managers for Nigerian onsite, hybrid, and remote roles.
- Engineers reviewing candidates for Python/Django internships, graduate or associate developer positions, junior Python roles, and junior Django/backend roles.
- International remote reviewers as a secondary audience.

## Product principles

1. **Evidence before decoration:** project behaviour and inspection links carry the argument.
2. **Specific before comprehensive:** publish a small set of defensible claims rather than an exhaustive skill list.
3. **Readable before clever:** semantic content, bounded line lengths, and predictable navigation outrank effects.
4. **Static before abstract:** add machinery only after repeated work proves it is needed.
5. **Truth before polish:** withhold incomplete assets and unverified claims rather than display placeholders.

## Required content

- Approved identity, role label, Lagos positioning, and concise junior-developer available-for-work message.
- Featured ShelfSum project overview with live demo link, source link, dedicated case study link, demo guidance, and verified screenshots.
- Supporting Credence project overview with source link, dedicated case study link, and verified demonstration output preview.
- Supporting CrewCast Lagos project overview with live demo, source, and dedicated case study links; distinguish synthetic jobs from live forecast retrievals.
- Dedicated case-study pages for ShelfSum (`projects/shelfsum.html`), CrewCast Lagos (`projects/crewcast-lagos.html`), and Credence (`projects/credence.html`).
- Downloadable CV PDF (`assets/documents/ayotomiwa-ojo-cv.pdf`) inspected and linked directly from the hero section.
- GitHub link (`https://github.com/Lordt0m`).
- Exactly five evidence-backed skills groups (`Python`, `Django`, `SQL & PostgreSQL`, `HTML & CSS`, `Git & GitHub`).
- Two-paragraph About section highlighting self-taught background and B.A. in English and Literary Studies from Federal University Oye-Ekiti.
- Contact routes: direct email action (`mailto:ayotomiwa529@gmail.com`), GitHub link, and inert `LinkedIn — coming soon` status text.

## Required behaviour

- Every navigation destination exists and works with JavaScript disabled.
- External destinations are clearly labelled and valid at release time.
- The page works with keyboard-only navigation and exposes visible focus.
- Layout remains readable without page-level horizontal overflow from 320 CSS pixels upward.
- Useful content is visible in a sensible order on phone, tablet, and desktop widths.
- The site exposes no secrets, real demo records, machine-specific paths, placeholder links, or unfinished sections.
- Search and social metadata identify Ayotomiwa and the portfolio accurately without exaggerated claims.

## Visual direction

Restrained dark presentation inspired by Cyze: deep navy background, slightly elevated project surfaces, soft cool blue accents, high-contrast text, rounded work preview frames, generous vertical whitespace, and clean system sans-serif typography. Project evidence is image-led on the homepage and expanded in dedicated case-study pages. No photograph or photograph placeholder is required.

## Explicit exclusions

- Blog, newsletter, comments, accounts, admin interface, CMS, database, server application, contact-message storage, analytics dashboard, theme switcher, animation system, skill meters, testimonials, certificates gallery, and AI-dependent behaviour.
- Claims of professional experience, client work, employment duration, or production scale that evidence does not support.
- Public discussion of AI assistance unless specifically requested.

## Release acceptance

The redesign release is accepted only when:

1. every rendered Claim is `verified` in `docs/content.md`;
2. `python scripts/verify_site.py` passes across all public HTML documents and assets;
3. keyboard navigation and visible focus pass manual review;
4. 320, 360, 768, 1024, and 1440 CSS-pixel inspections show no page-level overflow, clipping, or broken content;
5. all public links, case study pages, and downloadable CV work from the deployed site;
6. the repository contains no machine-specific paths, secrets, empty placeholders, or unrelated generated files;
7. the active release ticket records the public ref, deployment URL, checks, viewports, remaining limitations, and next safe action.
