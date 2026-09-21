# Portfolio system design

## System objective

Turn a recruiter's short visit into a reliable path from positioning to inspectable technical evidence, with the least possible implementation and maintenance surface.

The first release is one static page. Its architecture optimizes for owner comprehension, fast verification, durable public links, accessibility, and cheap future edits. The site itself must not become a fifth complex product competing with the projects it presents.

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

The initial implemented slice includes the verified ShelfSum Featured Project, Credence Supporting Project, and the available verified contact actions. It must remain a coherent page rather than display empty sections or placeholders for the CV, LinkedIn, journal, About copy, or screenshots.

## Module map

### Public document module

**Interface:** the semantic landmarks and stable fragment identifiers exposed by `index.html`.

Required identifiers when their content exists:

- `main-content`
- `projects`
- `skills`
- `about`
- `contact`

Its implementation owns public prose, heading order, link labels, accessible names, and the reading sequence. It does not own colors, breakpoints, or evidence decisions.

The Contact section exposes a simple list of verified Inspection Actions. It can accrete Email, GitHub, CV, and LinkedIn independently. An unavailable action is absent from the public document; the layout must not reserve an empty slot for it.

### Presentation module

**Interface:** named design tokens and responsive rules in `assets/css/site.css`.

Its implementation owns typography, spacing, color, focus appearance, layout, and local overflow. It must keep the page usable from 320 CSS pixels upward and must never require JavaScript.

### Enhancement module

**Interface:** accessible behaviours initialized from `assets/js/site.js`.

This module does not exist until a real interaction requires it. When created, it enhances existing HTML; it does not supply essential content, navigation, or project data.

### Asset module

**Interface:** stable repository-relative paths under `assets/`.

Use:

```text
assets/
  css/site.css
  documents/ayotomiwa-ojo-cv.pdf
  images/projects/<project-slug>/
  js/site.js
```

Create only directories containing real assets. Screenshots must show useful product states, use fictional data, include concise alternative text, and correspond to the linked live or repository evidence.

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
