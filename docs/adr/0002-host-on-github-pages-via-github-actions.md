# Host on GitHub Pages via GitHub Actions

The portfolio will be hosted as static files on GitHub Pages, deployed automatically on pushes to `main` via GitHub Actions.

## Context

The site is purely static HTML and CSS with zero server runtime or database requirements. We evaluated static hosting alternatives: GitHub Pages, Cloudflare Pages, and Render Static Sites.

## Decision

Use GitHub Pages via standard GitHub Actions deployment (`actions/deploy-pages`). The GitHub Actions workflow executes `python scripts/verify_site.py` and `python -m unittest discover tests` as release blockers prior to artifact upload.

## Consequences

- **Pros:** Zero hosting cost, automated TLS/HTTPS, native alignment with public repository and code review history, and no external token/credential configuration needed beyond standard repository permissions.
- **Trade-offs:** GitHub Pages does not support server-side redirects or header customization without external DNS/CDN layers (e.g. Cloudflare). Because the site is single-page with clean progressive enhancement, custom routing headers are unnecessary for this release. Custom domains remain fully supported via `CNAME`.
