# 04: Relaunch recruiter portfolio and migrate hosting

**Status:** complete

## Outcome

Execute a comprehensive portfolio redesign inspired by Cyze's restrained dark presentation, build dedicated case study pages for ShelfSum and Credence, publish an aligned ATS-compliant CV PDF, extend verification, and migrate production hosting to Cloudflare Pages.

## Acceptance

- [x] Reconcile `docs/content.md`, `.scratch/portfolio/spec.md`, `docs/architecture.md`, and ADRs with the approved redesign plans.
- [x] Create ATS-friendly CV matching verified project evidence and personal background from the owner-supplied CV, render and inspect PDF at `assets/documents/ayotomiwa-ojo-cv.pdf`.
- [x] Copy verified screenshots from the local ShelfSum repository's `docs/screenshots/` directory to `assets/images/projects/shelfsum/`.
- [x] Create high-contrast, accessible semantic HTML demonstration preview for Credence matching `fixtures/expected_mixed_output/summary.json`.
- [x] Redesign `assets/css/site.css` with a dark navy palette, crisp typography, rounded preview cards, at least 44px touch targets, and zero horizontal overflow.
- [x] Rebuild `index.html` with concise recruiter-first hierarchy, exactly 2 project cards, 5 evidence-backed skill groups, 2-paragraph About section, active CV download, and inert `LinkedIn — coming soon` text.
- [x] Create static case-study pages at `projects/shelfsum.html` and `projects/credence.html` with deep architectural and testing evidence.
- [x] Update `404.html` with dark theme styling and navigation.
- [x] Extend `scripts/verify_site.py` and `tests/test_verify_site.py` to validate all HTML documents, CV asset, image paths/alt text, inert LinkedIn, and relative routes.
- [x] Inspect viewports at 320, 360, 768, 1024, and 1440 CSS pixels for zero horizontal overflow, visible focus, touch targets, and readable typography.
- [x] Commit and push truthful implementation slice to `main`.
- [x] Configure and verify Cloudflare Pages deployment, update canonical URLs, and retire GitHub Pages deployment job after Cloudflare production passes.

## Pre-authorization completion record

- **Reviewed ref:** `ce7d291` on `main`, based on `0322363`.
- **Public behaviour:** Dark recruiter-focused homepage, ShelfSum and Credence case studies, semantic Credence fixture preview, verified screenshots, active email/GitHub/CV actions, and inert LinkedIn status. The phone number appears only in the CV.
- **Automated checks:** `python scripts/verify_site.py` passes; `python -m unittest discover tests` passes 28 tests; `git diff --check` reports no whitespace errors.
- **Viewport review:** All four public pages inspected at 320, 360, 768, 1024, and 1440 CSS pixels. No page-level horizontal overflow, clipping, unreadable text, broken screenshots, small primary targets, hidden focus, or keyboard traps observed. Local routes and the PDF responded successfully; approved external GitHub links and the ShelfSum demo responded successfully.
- **Evidence:** ShelfSum is documented at 271 tests with exact public demo credentials. Credence's fictional fixture values and 35-test baseline match its local repository. CV personal and education details match the owner-supplied DOCX; the final PDF was text-checked, link-checked, rendered, and visually inspected.
- **Post-push deployment:** GitHub Pages workflow run `35951034139` completed successfully for `ce7d291`. The live homepage, both case studies, 404 page, PDF CV, and ShelfSum screenshot returned HTTP 200 with the expected content types. The live homepage contains 271 tests and exact demo usernames, with no stale count or LinkedIn link.
- **Remaining risk:** Cloudflare's assigned address does not exist until owner authorization and deployment. GitHub Pages remains active as the verified public site; do not publish an invented Cloudflare URL or retire GitHub Pages first.
- **Next safe action:** The owner authorizes Cloudflare Pages Git integration for `Lordt0m/lordt0m.github.io` and deploys `main`. Verify the assigned `*.pages.dev` URL and commit, then add canonical/social metadata and the portfolio URL to the CV, retire the GitHub Pages deployment job, accept ADR 0003, and close this ticket.

## Cloudflare cutover completion record

- **Reviewed and deployed ref:** `8ba7ff949f641a239b3875a7bcd36ea58e0fdaa7` on `main`, following the verified original Cloudflare deployment of `61146be`.
- **Production address:** `https://ayotomiwa.pages.dev/` is the canonical portfolio URL. The homepage, both case studies, custom 404 page, stylesheet, ShelfSum screenshot, and final CV were fetched over HTTPS after the cutover and matched the committed files exactly. An unknown route returned HTTP 404.
- **Public behaviour:** Homepage and case studies now expose exact canonical and Open Graph URLs. The one-page ATS-friendly CV includes the active Cloudflare portfolio link and omits the former GitHub Pages address. The GitHub Pages publishing workflow is retired; `.github/workflows/verify.yml` runs checks without publishing.
- **Automated checks:** `python scripts/verify_site.py` passed with zero errors; `python -m unittest discover tests` passed 30 tests; `git diff --check` passed. GitHub Actions run `35953942321` passed for `8ba7ff9`.
- **Viewport and interaction evidence:** Before cutover, all four public pages were inspected locally at 320, 360, 768, 1024, and 1440 CSS pixels for overflow, clipping, readable text, visible focus, keyboard navigation, and touch targets. The live HTML and CSS match that reviewed implementation, apart from added nonvisual metadata. Live local navigation, image, stylesheet, and CV paths returned successfully; the GitHub profile, both project source links, and ShelfSum demo were rechecked at HTTP 200. The email action remains a `mailto:` link, and LinkedIn remains inert text.
- **CV evidence:** The final PDF was regenerated after Cloudflare assigned the URL, checked for its one-page layout, correct text and six link annotations, rendered, visually inspected, then verified byte-for-byte against the live download.
- **Remaining limitations:** The former GitHub Pages address may remain accessible as a historical copy, but no GitHub Pages deployment job remains. No custom domain, LinkedIn URL, or production browser-viewport screenshots were added.
- **Next safe action:** Maintain the verification gate and update evidence-controlled content only when the linked projects or CV facts change.
