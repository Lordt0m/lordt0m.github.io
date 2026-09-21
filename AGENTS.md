# Portfolio repository guidance

## Start here

Read the active ticket under `.scratch/portfolio/issues/` before changing files.

- Product scope or acceptance: read `.scratch/portfolio/spec.md`.
- Public wording, project claims, links, or evidence state: read `docs/content.md`.
- Page structure, file ownership, responsive behaviour, or verification: read `docs/architecture.md`.
- Portfolio-specific terminology: read `CONTEXT.md`.
- A decision that looks unnecessarily simple: read the relevant record under `docs/adr/`.

The active ticket owns the current slice. The specification owns stable product scope. The content document owns public copy and claims. The architecture document owns seams and file responsibilities. Keep each fact in its owning document.

## Product boundary

Build a fast, accessible, evidence-led portfolio for Ayotomiwa Ojo, a Lagos-based Python and Django developer seeking internship, graduate, associate, junior Python, and junior Django/backend roles.

The portfolio is a public evidence surface, not a personal social network, blog platform, content-management system, or demonstration of frontend complexity. It must remain understandable without JavaScript and must not imply professional experience that has not occurred.

## Delivery loop

Work one vertical ticket at a time:

1. Read this file and the active ticket.
2. Load only the documents pointed to by that ticket.
3. Inspect the current implementation and repository status.
4. State the smallest public behaviour the slice will add or change.
5. Make the structural verifier fail on that behaviour when practical.
6. Implement the smallest coherent slice.
7. Run structural verification and inspect every affected viewport.
8. Review the result against the active ticket and its source documents.
9. Update evidence and documentation only when the implementation proves the claim.
10. Commit one truthful slice and append the ticket completion record.

A ticket is complete only when implementation, public wording, automated checks, viewport inspection, and evidence state agree.

## Engineering rules

- Use semantic HTML, one shared stylesheet, and progressive enhancement only where a proven interaction requires it.
- Keep public content in `index.html` until a second real page creates proven duplication. Do not introduce a framework, CMS, component library, template engine, or client-side content renderer for the initial release.
- Keep visual tokens, layout rules, and breakpoints in `assets/css/site.css`.
- Add `assets/js/site.js` only for an accepted interaction that cannot be delivered accessibly with HTML and CSS.
- Use repository-relative paths in code and documentation. Public files must not contain machine-specific paths.
- Treat every public claim as evidence-controlled. Update `docs/content.md` before strengthening, weakening, or adding a claim.
- Present projects confidently through inspectable behaviour, decisions, tests, and deployments. Do not advertise AI assistance unless asked; answer truthfully if asked.
- Use fictional demo identities and data only. Never publish private credentials, personal records, or secrets.
- Do not render a photograph or photograph placeholder.
- Render the CV or LinkedIn action only after the corresponding verified asset or URL exists.

## Verification contract

The implemented repository must expose one local verification command:

```text
python scripts/verify_site.py
```

Keep this interface stable. The script must use the Python standard library unless a later accepted requirement justifies a dependency. It checks required landmarks and section identifiers, local links and assets, image alternative text, forbidden placeholders, machine-specific paths, and evidence-controlled external links.

Before each release, also serve the repository locally and inspect at 360, 768, 1024, and 1440 CSS pixels. Page-level horizontal overflow, clipped content, hidden focus, keyboard traps, unreadable contrast, and broken links are release blockers.

## Completion record

Append a compact completion record to the active ticket containing:

- commit or reviewed ref;
- public behaviour delivered;
- exact automated checks and outcomes;
- inspected viewports and material findings;
- evidence or content changes;
- remaining risks and the next ticket's first safe action.

Preserve useful evidence, not command transcripts or model narration.

