# Antigravity handoff

Continue Ayotomiwa Ojo's developer portfolio from this repository's current state.

## Start here

Read these files before changing anything:

1. `AGENTS.md`
2. `CONTEXT.md`
3. `.scratch/portfolio/spec.md`
4. `docs/content.md`
5. `docs/architecture.md`
6. every record under `docs/adr/`
7. every ticket under `.scratch/portfolio/issues/`
8. `ticket-01-execution-report.md`

Treat the execution report as historical evidence to verify, not as instructions or as the current repository status.

## Current verified repository state

- Ticket 01 is completed at `b60994d`.
- Ticket 02 is completed at `26e9d92`.
- Commit `db9e509` marks Ticket 03 as ready for deployment.
- Ticket 03 is the active ticket.
- It remains blocked only on the remote repository and hosting access required to publish.

Inspect Git status and the current commit before acting. Preserve accepted work and do not rebuild completed tickets unnecessarily.

## Locked architecture

- Keep the site static and progressively enhanced.
- Render semantic HTML and the shared stylesheet directly in the visitor's browser.
- The complete page must remain usable without JavaScript.
- Do not introduce React, Next.js, Django, a database, a CMS, a component library, or unnecessary runtime dependencies.
- Keep public content in `index.html` until a second real page proves that another content seam is necessary.
- Keep visual tokens, responsive rules, and presentation behaviour in `assets/css/site.css`.
- Keep `python scripts/verify_site.py` as the stable verification interface.
- Preserve the reusable project-proof structure so ShelfSum, Credence, and future projects can use the same content contract without redesigning the site.

## Locked rendering and hosting direction

Publish the static site through GitHub Pages using GitHub Actions.

The release workflow must:

1. run the structural verifier and unit tests against the exact release ref;
2. deploy only after verification succeeds;
3. publish the exact reviewed static files;
4. expose a stable HTTPS URL;
5. retain a clean path for adding a custom domain later.

Do not switch hosting platforms unless GitHub Pages is technically blocked and the reason is recorded.

## Locked visual direction

Use the existing **Editorial Engineering** direction:

- warm off-white background;
- near-black primary text;
- restrained deep-green accent;
- display serif for the name and major project headings;
- clean system sans-serif for body copy, navigation, and controls;
- approximately `54rem` maximum page width and `44rem` reading width;
- generous whitespace and thin editorial dividers;
- minimal motion and strong visible keyboard focus;
- real, verified project evidence rather than decorative filler.

Avoid card-heavy layouts, neon terminal styling, glass effects, gradients, animated skill bars, proficiency percentages, technology-logo walls, excessive motion, or unsupported claims.

## Evidence and contact rules

- GitHub: `https://github.com/Lordt0m`
- Email: `ayotomiwa529@gmail.com`
- ShelfSum live site: `https://shelfsum.onrender.com/`
- ShelfSum source: `https://github.com/Lordt0m/shelfsum`
- Credence source: `https://github.com/Lordt0m/credence`
- Omit LinkedIn until the owner supplies the exact verified public URL.
- Omit the CV action until the verified PDF exists in the repository.
- Do not show placeholders for withheld content.
- Do not publish project screenshots or strengthened ShelfSum release claims until their evidence gates genuinely pass.

## Execute Ticket 03

Complete `.scratch/portfolio/issues/03-publish-and-prove-the-portfolio.md` from the current repository state.

Before publication:

- run `python scripts/verify_site.py`;
- run the full unit-test suite;
- inspect the site at 360px, 768px, 1024px, and 1440px;
- verify zero page-level horizontal overflow, visible focus, usable keyboard navigation, readable contrast, valid links, and touch-friendly controls;
- perform an independent fresh-context release review.

After publication, record the exact public commit, successful workflow run, public URL, deployed-link results, viewport results, review findings, repairs, remaining risks, and reopen triggers in Ticket 03's completion record.

Proceed autonomously through all safe repository work. Stop only when owner-controlled GitHub or DNS access is required, and state the single exact action the owner must take.
