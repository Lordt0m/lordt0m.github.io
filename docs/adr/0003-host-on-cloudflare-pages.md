# Host on Cloudflare Pages

**Status:** Accepted. Supersedes [ADR 0002](0002-host-on-github-pages-via-github-actions.md) after live production verification.

The portfolio production host is `https://ayotomiwa.pages.dev/`, deployed from `main` through Cloudflare Pages GitHub integration. The owner-provided address was adopted only after the homepage, case studies, assets, CV, and custom 404 response were verified live against the reviewed repository.

## Context

The initial release deployed to GitHub Pages at `https://lordt0m.github.io/`. The owner requested migrating hosting to Cloudflare Pages using its assigned `*.pages.dev` subdomain without requiring a purchased custom domain.

We evaluated Cloudflare Pages Git integration against remaining on GitHub Pages or moving to other static hosts.

## Decision

Use Cloudflare Pages for production hosting:
1. Connect the `Lordt0m/lordt0m.github.io` repository to Cloudflare Pages via GitHub integration.
2. Production branch is `main`, framework preset is `None`, the build command is `exit 0`, and the build output directory is `.` (the repository root). Leave the optional root-directory setting at its repository-root default.
3. GitHub Actions CI in `.github/workflows/verify.yml` remains a verification gate running `python scripts/verify_site.py` and unit tests on push and pull requests.
4. The GitHub Pages deployment job was retained until the assigned `*.pages.dev` site passed production checks, then removed. The former GitHub Pages site may remain reachable as a historical copy, but it is no longer the canonical destination or an active deployment pipeline.

## Consequences

- **Pros:** Global edge CDN performance, automatic SSL/TLS on assigned `*.pages.dev` domain, automatic branch previews for pull requests, and simple future custom domain addition if desired.
- **Trade-offs:** Git integration depends on owner-controlled Cloudflare/GitHub authorization. The `exit 0` build command leaves the static asset pipeline independent of node/npm build tools. GitHub Actions remains a separate verification pipeline, not a second publishing pipeline.
