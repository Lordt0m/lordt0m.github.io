# Portfolio system design

## System objective

Turn a recruiter's short visit into a reliable path from positioning to inspectable technical evidence, with the least possible implementation and maintenance surface.

The portfolio is a small static site: one recruiter-focused overview, three project case studies, and an error page. Its architecture optimizes for owner comprehension, fast verification, durable public links, accessibility, and cheap future edits. The site itself must not become another complex product competing with the projects it presents.

## Reader flow

The page answers five questions in order:

1. Who is Ayotomiwa and what roles fit?
2. What has he built?
3. What engineering behaviour can be inspected?
4. What skills are demonstrated by that evidence?
5. How can a recruiter review the CV or make contact?

Use this section order:

1. Header navigation
2. Hero and availability
3. Featured Projects
4. Supporting Projects
5. Evidence-backed skills
6. About
7. CV and contact
8. Footer

The homepage includes the verified ShelfSum Featured Project, CrewCast Lagos and Credence Supporting Projects, five skill groups, two About paragraphs, the CV download, and verified contact actions. Detailed evidence belongs on the three case-study pages. LinkedIn remains visible only as inert status text until the owner supplies a verified URL.

## Module map

### Public document module

**Interface:** the semantic landmarks, stable fragment identifiers, and static case study routes.

Key documents:
- `index.html`: concise recruiter overview, hero, project proof blocks, 5 skills groups, About, CV download, and contact actions.
- `projects/shelfsum.html`: dedicated case study detailing problem, user roles, transactional stock architecture, immutable ledger, 271 tests, and Render/Neon deployment.
- `projects/credence.html`: dedicated case study detailing cashbook validation pipeline, 7-column CSV contract, deterministic artifacts, exact decimal math, and 35 tests.
- `projects/crewcast-lagos.html`: dedicated case study detailing forecast freshness, bounded provider traffic, scheduled updates, and the read-only demo boundary.
- `404.html`: standalone accessible error page with navigation and return routes.

Required identifiers when their content exists on `index.html`:
- `main-content`
- `projects`
- `skills`
- `about`
- `contact`

The Contact section exposes a simple list of verified inspection actions: direct Email, GitHub, and inert `LinkedIn — coming soon` status text.

### Presentation module

**Interface:** named dark design tokens and responsive rules in `assets/css/site.css`.

Its implementation owns typography, spacing, color, focus appearance, layout, rounded work frames, and local overflow. It must keep the page usable from 320 CSS pixels upward and must never require JavaScript.

### Enhancement module

**Interface:** accessible behaviours initialized from `assets/js/site.js`.

This module does not exist until a real interaction requires it. When created, it enhances existing HTML; it does not supply essential content, navigation, or project data.

### Asset module

**Interface:** stable repository-relative paths under `assets/`.

Structure:

```text
assets/
  css/site.css
  documents/ayotomiwa-ojo-cv.pdf
  images/favicon.svg
  images/projects/shelfsum/
```

Create only directories containing real assets. Screenshots must show useful product states, use fictional data, include concise alternative text, and correspond to the linked live or repository evidence. Credence's evidence preview is semantic HTML and CSS rather than an image asset.

### Verification module

**Interface:** `python scripts/verify_site.py` with a zero exit status for a structurally releasable site and a non-zero status with actionable messages otherwise.

The implementation concentrates deterministic checks in one place so builders and reviewers share the same seam. It must check:

- exactly one `main` landmark and one level-one heading;
- required identifiers for every rendered navigation link;
- valid repository-relative local links and assets;
- alternative text for informative images and empty alternative text for decorative images;
- absence of `TODO`, lorem ipsum, empty links, photograph placeholders, and machine-specific paths;
- the approved GitHub and project URLs from `docs/content.md`;
- presence of the availability message and at least one project inspection action.

Browser inspection remains the test surface for layout and interaction. The structural verifier must not pretend to prove responsive appearance.

### Hosting module

**Production interface:** Cloudflare Pages deploys the repository root from `main` through Git integration at `https://ayotomiwa.pages.dev/`. The verified assigned URL owns canonical and sharing metadata as well as the CV's portfolio link.

**Verification interface:** `.github/workflows/verify.yml` runs structural verification and unit tests on pushes and pull requests without publishing to GitHub Pages. The former GitHub Pages deployment workflow was retired only after the Cloudflare production site passed live page, asset, and CV checks.

## Source-of-truth map

| Information | Authority |
| --- | --- |
| Portfolio vocabulary | `CONTEXT.md` |
| Stable scope and acceptance | `.scratch/portfolio/spec.md` |
| Public copy, links, and claim state | `docs/content.md` |
| File ownership, seams, and verification | `docs/architecture.md` |
| Current work and completion evidence | active ticket |
| Implemented behaviour | repository files and executed checks |

When sources disagree, stop publication of the disputed Claim. Reconcile the owning source and implementation rather than copying the discrepancy into another document.

## Responsive contract

- **320-479:** single-column reading order; wrapping navigation; full-width primary actions when helpful.
- **480-767:** single-column content with increased spacing; no page-level horizontal overflow.
- **768-1023:** tablet layout may use two columns where content remains readable; navigation must wrap or collapse without hiding destinations.
- **1024 and above:** wider composition with bounded line lengths and no stretched text walls.

Wide screenshots and data tables may have local scrolling or responsive cropping. They must never expand the document viewport.

## Accessibility contract

- Provide a skip link to `main-content`.
- Use landmarks, logical heading order, descriptive link text, and visible keyboard focus.
- Respect reduced-motion preferences if motion is introduced.
- Do not encode meaning by color alone.
- Use images as evidence, not as containers for essential text.
- Keep touch targets and spacing usable at phone widths.

## Accretion rules

Add a new abstraction only when current implementation evidence shows repeated change or duplicated knowledge. Before adding a page generator, project schema, framework, component library, CMS, analytics provider, contact backend, or animation system, identify the repeated problem and record why the existing module interface cannot contain it.

New projects accrete through the existing Project Proof Block. New Claims enter `docs/content.md` as withheld or planned, become verified only after evidence is inspected, and reach the public document only after verification. This keeps expansion additive without weakening prior evidence.
