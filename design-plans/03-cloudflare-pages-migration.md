# Move portfolio hosting to Cloudflare Pages

Written against: `0322363b30253c9266b8a0d42133428861ab258c`

## Evidence chain

- Surface: `.github/workflows/deploy.yml`, GitHub Pages ADR, canonical and sharing metadata, live deployment, and release ticket.
- Problem: the owner no longer wants GitHub Pages and does not own a domain.
- Design evidence: Cloudflare Pages supports GitHub integration, automatic deployments, preview URLs, and an assigned `*.pages.dev` production URL for projects without a custom domain.
- Owner: hosting configuration and ADR own deployment; HTML metadata owns the canonical URL only after successful deployment.
- Scope and affected surfaces: CI workflow, hosting documentation, deployment evidence, canonical metadata, sitemap/robots files if present, and live-link verification.
- Uncertainty: the final `*.pages.dev` project name is chosen during the owner-controlled Cloudflare connection.

## Design decision

Keep GitHub as the source repository and migrate production hosting to Cloudflare Pages through its GitHub integration. Use the generated `*.pages.dev` address; do not require or purchase a custom domain. Preserve repository verification in GitHub Actions, but remove GitHub Pages deployment after Cloudflare production is proven.

## Reuse

- Existing static files and zero-build architecture.
- Existing `python scripts/verify_site.py` and unit-test suite as CI gates.
- Existing GitHub repository as the source of deployments.
- Official references: Cloudflare Pages Git integration and static HTML deployment documentation.

## Changes

1. `.github/workflows/deploy.yml`
   - Change: replace GitHub Pages publication with a verification-only CI workflow, or rename it to `verify.yml` if that improves truthfulness.
   - Preserve: run the structural verifier and unit tests for pushes and pull requests.
   - Verify: no `pages` permissions, Pages artifact upload, or GitHub Pages deployment job remains after migration acceptance.

2. Cloudflare Pages project
   - Change: connect `Lordt0m/lordt0m.github.io` to Cloudflare Pages using the GitHub integration, production branch `main`, no framework preset, repository root as the static output, and no application build step beyond settings supported by the current Cloudflare interface.
   - Preserve: automatic production deploys from `main` and preview deployments for non-production branches or pull requests.
   - Verify: the deployment reports the expected commit and every required file is available from the assigned `*.pages.dev` URL.

3. `docs/adr/0002-host-on-github-pages-via-github-actions.md`
   - Change: supersede it with a new ADR explaining the Cloudflare Pages decision, the generated subdomain, Git integration, preview deployments, and the reason GitHub Pages was retired.
   - Preserve: history; do not rewrite the old decision as though it never existed.
   - Verify: only the new ADR describes the active host.

4. Metadata and public URLs
   - Change: after successful deployment, replace `https://lordt0m.github.io/` in canonical, Open Graph, sitemap, docs, and release evidence with the exact Cloudflare Pages production URL.
   - Preserve: repository links continue to point to GitHub.
   - Verify: no stale production URL remains in public files or active documentation, except historical records clearly labelled as superseded.

5. Release evidence
   - Change: create a new migration/relaunch ticket recording the deployed commit, exact Pages URL, Cloudflare deployment result, CI result, viewport checks, link checks, CV download, screenshots, case studies, and remaining limitations.
   - Preserve: earlier ticket records as historical evidence.
   - Verify: production checks run against the exact Cloudflare URL.

## Scope

- Inherit: all static pages and assets.
- Verify: homepage, two case studies, 404 behaviour, CV download, images, email, GitHub, demo, source links, metadata, and HTTPS.
- Exclude: purchasing a domain, moving the Git repository, Workers Functions, server-side code, analytics, forms, databases, or Cloudflare Access.

## Validation

- Product: the new Cloudflare Pages URL is the primary portfolio address and loads the exact reviewed commit over HTTPS.
- Interface: inspect 360, 768, 1024, and 1440 CSS pixels on production with keyboard navigation, visible focus, image loading, and zero horizontal overflow.
- System: GitHub Actions verifies; Cloudflare Pages deploys. No second deployment pipeline remains active.
- Repository: `python scripts/verify_site.py` and `python -m unittest discover tests` pass before and after metadata updates.

## Stop conditions

- Stop at the single owner-controlled action if Cloudflare account creation or GitHub authorization is required. Report the exact dashboard choices rather than requesting unrelated access.
- Do not disable the existing GitHub Pages site until the Cloudflare production deployment passes all checks.
- Do not invent a final `*.pages.dev` URL before Cloudflare assigns it.

## Design documentation

- After acceptance and validation: add the Cloudflare Pages ADR, update `docs/architecture.md`, update the release ticket, and mark the GitHub Pages ADR as superseded.

## Delivery evidence

- The owner-provided production address is `https://ayotomiwa.pages.dev/`; it was live before the cutover and matched the reviewed `61146be` site.
- Cutover commit `8ba7ff9` added canonical/social URLs, the portfolio URL to the verified CV, and verification-only GitHub Actions; it retired the GitHub Pages deployment workflow. GitHub Actions run `35953942321` passed.
- After the push, the live homepage, both case studies, 404 page, stylesheet, ShelfSum screenshot, and CV exactly matched the committed files over HTTPS. An unknown route returned HTTP 404. Ticket 04 records the complete verification and remaining limitations.
