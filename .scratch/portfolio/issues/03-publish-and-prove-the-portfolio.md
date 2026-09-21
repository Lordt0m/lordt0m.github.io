# 03: Publish and prove the portfolio

**Status:** ready for deployment (blocked on remote repository/hosting credentials)

## Outcome

Publish the exact reviewed portfolio ref and record sufficient evidence for recruiters and future maintainers to trust the release.

## Acceptance

- [x] Choose the simplest static hosting route that provides HTTPS and a stable public URL (GitHub Pages via GitHub Actions; locked in `ANTIGRAVITY-HANDOFF.md`).
- [x] Record the hosting decision only if it creates a durable, non-obvious trade-off (Recorded in `docs/adr/0002-host-on-github-pages-via-github-actions.md`).
- [x] Run the structural verifier against the release ref (`python scripts/verify_site.py` passed with 0 errors; 17 automated tests passed).
- [ ] Verify every public link and downloadable asset on the deployed site (Blocked on owner push to GitHub and GitHub Pages activation).
- [ ] Inspect keyboard behaviour and 360, 768, 1024, and 1440 CSS-pixel layouts on the live deployment (Locally verified; live inspection pending deployment).
- [x] Verify page title, description, sharing metadata, favicon, error behaviour, and absence of machine-specific paths or secrets (`assets/images/favicon.svg`, `404.html`, metadata verified).
- [ ] Record the public ref, deployment URL, exact checks, material limitations, and next safe action (Pending live deployment URL).
- [ ] Mark the portfolio repository as a Supporting Project only if its final evidence justifies that Claim (Planned until deployed and proven).

## Pre-flight verification record

- **Ref:** Ticket 03 pre-flight deployment slice on branch `main`.
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
- **Single required owner action to deploy:**
  - Add remote `origin` to this repository and push `main` to GitHub:
    `git remote add origin https://github.com/Lordt0m/<repo-name>.git`
    `git push -u origin main`
  - In GitHub repository Settings &rarr; Pages, set **Build and deployment** source to **GitHub Actions**.

