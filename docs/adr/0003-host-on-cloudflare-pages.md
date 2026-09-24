# Host on Cloudflare Pages

**Status:** Proposed. Supersedes [ADR 0002](0002-host-on-github-pages-via-github-actions.md) only after live production verification.

The portfolio production hosting is planned to migrate from GitHub Pages to Cloudflare Pages, deployed automatically from the `main` branch through Cloudflare's GitHub integration.

## Context

The initial release deployed to GitHub Pages at `https://lordt0m.github.io/`. The owner requested migrating hosting to Cloudflare Pages using its assigned `*.pages.dev` subdomain without requiring a purchased custom domain.

We evaluated Cloudflare Pages Git integration against remaining on GitHub Pages or moving to other static hosts.

## Decision

Migrate production hosting to Cloudflare Pages:
1. Connect the `Lordt0m/lordt0m.github.io` repository to Cloudflare Pages via GitHub integration.
2. Production branch is `main`, framework preset is `None`, the build command is `exit 0`, and the build output directory is `.` (the repository root). Leave the optional root-directory setting at its repository-root default.
3. GitHub Actions CI workflow is maintained as a pre-flight verification gate running `python scripts/verify_site.py` and unit tests on push and pull requests.
4. Keep the current GitHub Pages deployment active until the assigned `*.pages.dev` site is validated against the reviewed commit, then retire the GitHub Pages deployment steps and mark this ADR accepted.

## Consequences

- **Pros:** Global edge CDN performance, automatic SSL/TLS on assigned `*.pages.dev` domain, automatic branch previews for pull requests, and simple future custom domain addition if desired.
- **Trade-offs:** Deployment authorization requires owner-controlled OAuth/permissions setup in the Cloudflare dashboard. Zero build step keeps the static asset pipeline simple and independent of node/npm build tools.
