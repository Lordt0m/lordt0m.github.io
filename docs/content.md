# Public content and evidence register

This document owns approved public wording, destinations, and Claim state. Preserve meaning when adapting copy to fit a layout. Strengthen a Claim only after inspecting its Evidence.

## Identity and positioning

**Name — verified**

Ayotomiwa Ojo

**Role label — verified**

Full-stack Software Developer

**Portfolio address — verified**

`https://ayotomiwa.pages.dev/` is the owner-provided Cloudflare Pages production URL. The homepage, both case studies, stylesheet, screenshots, custom 404 response, and PDF CV were checked live against the reviewed repository before adopting it. Use this address for canonical metadata and the CV; keep GitHub repository URLs as source links.

**Primary statement — verified**

I build web applications from interface to database, with clear workflows and reliable systems underneath.

**Availability — verified**

Explore the live products, source code, and engineering decisions behind my work. Open to software development roles in delivery teams.

**Technology direction - owner stated, not shipped-project evidence**

React and TypeScript interfaces, Django REST APIs, PostgreSQL workflows, HTML and CSS. Rust, C++ and C remain future exploration interests, not shipped project evidence. Rust, C++, and C appear in About as future exploration, not as demonstrated skills.

**Portfolio presentation - verified against current project entries**

The homepage leads with ShelfSum, SpecShift and Nobelese. Three further projects remain available under More independent projects. Detailed engineering claims and limitations remain in project capabilities, case studies, and the evidence below. The featured and supporting labels describe presentation hierarchy, not employment or customer adoption.

**Hero actions**

- `View projects` — verified; link to `#projects`.
- `Backend CV (PDF)` - verified; link to `assets/documents/ayotomiwa-ojo-cv.pdf`. The current download is a Python/Django-specific CV and needs a separate full-stack revision before it can be labelled as a general CV.
- `Email me` — verified; link to `mailto:ayotomiwa529@gmail.com`.
- `GitHub` — verified; link to `https://github.com/Lordt0m`.

## Featured Project: ShelfSum

**Title — verified**

ShelfSum

**Descriptor — verified**

Explainable inventory and business activity for small shops.

**Project summary — verified**

ShelfSum is a server-rendered Django application for small-shop Owner and Staff Member teams to track Products, Stock on Hand, Purchases, Sales, Expenses, and operational estimates through records they can inspect and explain.

I designed it as an independent portfolio product around secure permissions, Business-scoped data, transactional stock operations, immutable movement history, deterministic fictional demonstration data, and reports that connect summaries to their underlying activity.

**Problem — verified**

Small retail teams need a dependable answer to two connected questions: what is currently on the shelf, and which recorded actions produced that position? A directly editable stock number cannot explain purchases, sales, corrections, reversals, or responsibility.

**Delivered behaviour — verified**

- Owner and Staff Member access with server-enforced permissions.
- Business-scoped lookups that prevent cross-Business record access.
- Products, Purchases, Sales, Expenses, Stock Adjustments, and Audit Events.
- Append-only Stock Movements with explicit reversal workflows.
- Explainable dashboard totals, filtered reports, and safe CSV exports.
- A public, read-only fictional Demo Business with deterministic August 2026 activity.

**Engineering evidence — verified**

- Python 3.13 and Django 5.2 LTS.
- PostgreSQL release verification and continuous integration on GitHub Actions.
- 288 automated tests passed with zero skips against PostgreSQL for the 16 October 2026 release, including all three concurrency tests. Verified CI: https://github.com/Lordt0m/shelfsum/actions/runs/38831631681 at production ref e4f4acd415c294a29e4dcf30ecf6fc56a16137b2.
- Public landing motion progressively enhances server-rendered content: a coordinated hero entrance and fictional Purchase/Sale sequence retain movement rows. Keyboard and reduced-motion replay settle immediately; the page remains useful without JavaScript.
- Deployed on Render with Neon PostgreSQL, WhiteNoise static handling, HTTPS-aware settings, and a health endpoint.
- Explicit domain services for transactional stock changes instead of hidden model signals.
- Public architecture decisions, invariant ownership, tickets, and release evidence in the repository.

**Trade-off — verified**

ShelfSum keeps a current Stock on Hand value for fast reads while recording every change in an immutable movement ledger. This makes the displayed balance efficient and independently explainable, at the cost of stricter transaction and reconciliation rules.

**Technology line — verified**

Python · Django · PostgreSQL · HTML · CSS · GitHub Actions · Render · Neon

**Inspection actions — verified**

- `Live Demo`: `https://shelfsum.onrender.com/`
- `Source Code`: `https://github.com/Lordt0m/shelfsum`
- `Case Study`: `projects/shelfsum.html`

**Demo guidance — verified**

- The free demo may take a moment to start after inactivity.
- Fictional demonstration credentials: Owner (`demo-owner@shelfsum.test` / `ShelfSumDemoOwner2026!`) and Staff Member (`demo-staff@shelfsum.test` / `ShelfSumDemoStaff2026!`).

**Screenshot state — verified**

Captured and visually inspected from the live 16 October release (production ref e4f4acd415c294a29e4dcf30ecf6fc56a16137b2), using only the fictional read-only Demo Business:
- `desktop-landing-20261016.jpg`: public hero and clearly labelled fictional product preview.
- `desktop-dashboard-20261016.jpg`: current Owner dashboard and stock priorities.
- `desktop-movements-20261016.jpg`: August 2026 movement report with original and reversal records.
- `mobile-dashboard-20261016.jpg`: current dashboard at a 390-by-844 CSS-pixel viewport.

Desktop captures used a 1440-by-1000 CSS-pixel viewport; stored images are 1425 by 990 pixels. The phone image is 390 by 844 pixels. Static images do not reproduce animation; the case study links to the live page to inspect motion. Ticket 08 records the review and portfolio verification.

## Supporting Project: Credence

**Title — verified**

Credence

**Descriptor — verified**

Deterministic cashbook validation and financial summaries from one Python command.

**Project summary — verified**

Credence is a Python command-line application that turns small-business cashbook CSV files into an explainable validation report, a clean transaction file, and a reconciled financial summary in Nigerian Naira.

It processes files locally without accounts, databases, cloud APIs, spreadsheet software, or runtime dependencies. Invalid rows remain traceable through stable error codes and physical source-line numbers, while financial totals include only validated transactions.

**Delivered behaviour — verified**

- Strict seven-column CSV contract with flexible column order.
- Accumulated row-level errors rather than first-error-only reporting.
- Case-insensitive whole-file duplicate transaction rejection.
- Exact decimal arithmetic for income, expenses, and net cash movement.
- Three deterministic artifacts: clean transactions, validation errors, and a JSON summary.
- Explicit exit codes separating clean validation, row issues, and operational failure.
- Staged output generation, collision refusal, and best-effort rollback for handled publication failures.

**Engineering evidence — verified**

- Python 3.13 standard-library runtime with zero runtime package dependencies.
- 35 automated unit, integration, and demonstration tests at the accepted release baseline.
- Public GitHub Actions CI passing on Ubuntu and Windows with Python 3.13.
- Both `credence` console-script and `python -m credence` entry points verified against fictional demonstration data.
- Public input contracts, architectural decisions, known limitations, and release evidence in the repository.

**Trade-off — verified**

Credence stages every report before publication and refuses to overwrite existing target files. It provides best-effort rollback for handled filesystem failures, while explicitly avoiding the false claim that separate files can be atomically committed across sudden power loss, operating-system crashes, or forced termination.

**Technology line — verified**

Python · Standard Library · pytest · GitHub Actions · CSV · JSON

**Inspection actions — verified**

- `Source Code`: `https://github.com/Lordt0m/credence`
- `Case Study`: `projects/credence.html`
- Credence has no hosted application. Do not render a `Live Demo` action.

**Demonstration output preview — verified**

Verified fixture output from `fixtures/expected_mixed_output/summary.json` implemented directly as accessible, responsive semantic HTML and CSS without raster or SVG image files:
- Processed rows: 10
- Valid rows: 4
- Invalid rows: 6
- Total errors: 7
- Total income: NGN 75,000.00
- Total expenses: NGN 59,500.50
- Net cash movement: NGN 15,499.50

## Supporting Project: CrewCast Lagos

**Title and descriptor — verified**

CrewCast Lagos — weather-aware job planning for outdoor dispatchers in Lagos.

**Project summary — verified**

CrewCast is a Django planning aid that compares scheduled outdoor jobs with retrieved Open-Meteo forecasts. Public access is read-only with example sites and jobs; forecast retrievals are real. It shows when a forecast was last obtained, explains threshold-based recommendations, and suppresses favourable recommendations when the data becomes stale. Public wording uses the product name and “Open CrewCast” without demo/prototype framing.

The 16 October 2026 release adds a weather-bulletin interface, explicit job windows and retrieval provenance, responsive operational records, and progressive TypeScript date navigation that preserves the board position. All evaluation and authorization remain in Django. Core content, links and forms work without JavaScript.

**Engineering evidence — verified**

- A pure evaluator combines job windows, hourly forecast metrics, and versioned weather policies.
- PostgreSQL stores forecast snapshots, sync attempts, budget reservations, and recommendations; web page loads do not call the provider.
- A Lagos-calendar daily call budget, retry policy, and provider circuit breaker bound external requests.
- GitHub Actions runs the forecast refresh on a schedule; automatic `schedule` run [36246262643](https://github.com/Lordt0m/crewcast-lagos/actions/runs/36246262643) succeeded on 26 September 2026. The public Operations page showed that run's per-site attempts against the shared Neon database.
- Operations exposes actual retrieval attempts, retry outcomes and provider circuit state. The failure replay has been retired; old app bookmarks redirect to the planning board.
- CrewCast CI passed after the portfolio-readiness fixes at [36247508159](https://github.com/Lordt0m/crewcast-lagos/actions/runs/36247508159), and the final public error-copy fix passed at [36248342118](https://github.com/Lordt0m/crewcast-lagos/actions/runs/36248342118).
- The interface release [e7bcb50](https://github.com/Lordt0m/crewcast-lagos/commit/e7bcb5076d0c6d131952efbd397d7b449922d667) passed [CI 38928513370](https://github.com/Lordt0m/crewcast-lagos/actions/runs/38928513370): 94 application tests with PostgreSQL/Redis and six frontend tests for comparison highlights, request cancellation and recovery.
- The 19 October cleanup [563aaa2](https://github.com/Lordt0m/crewcast-lagos/commit/563aaa24a283d497a6fe5d825c7baba0d2985cf5) is live on Render. [CI 39207360080](https://github.com/Lordt0m/crewcast-lagos/actions/runs/39207360080) passed 102 application tests with PostgreSQL/Redis and six frontend tests, including nine legacy bookmark cases.
- Product wording release [3b73284](https://github.com/Lordt0m/crewcast-lagos/commit/3b73284961936fa0d5e3b1c2c1fe68cb3b081498) removes the public mode banner and demo/prototype framing while retaining read-only enforcement, example labels and forecast provenance. [CI 39209381596](https://github.com/Lordt0m/crewcast-lagos/actions/runs/39209381596) passed 102 PostgreSQL/Redis application tests and six frontend tests.
- Browser checks covered desktop/phone layouts, keyboard, reduced motion, JavaScript-disabled public date navigation, browser Back and offline retry. Slower CPU/network emulation was checked; physical lowest-end devices and production Core Web Vitals were not measured.
- The example comparison uses optional, interruptible highlights; keyboard and reduced-motion activation settle immediately. Its concise public label is “Example comparison.”

**Interface evidence — verified 19 October 2026**

- Actual published entry and Operations captures: `assets/images/projects/crewcast/desktop-entry-product-20261019.jpg` and `desktop-operations-product-20261019.jpg`. The retired replay screenshot is removed from public pages.
- The entry explains a work-window comparison. Operations shows stored retrieval records with their individual ages. Do not imply customer jobs or a fully fresh fleet.

**Trade-off and limitations — verified**

Public access is read-only. The site contains example jobs and provides planning signals, not occupational-safety clearance. GitHub's scheduled jobs can be delayed or skipped, and provider requests can fail. CrewCast therefore surfaces data age and failure states rather than implying forecasts are always fresh. No always-on production worker or hosted Redis is claimed.

**Technology line — verified**

Python · Django · PostgreSQL · TypeScript · CSS · Neon · GitHub Actions · Render · Open-Meteo

**Inspection actions — verified**

- `Open CrewCast`: `https://crewcast-lagos.onrender.com/`
- `Operations`: `https://crewcast-lagos.onrender.com/operations/`
- `Release CI`: `https://github.com/Lordt0m/crewcast-lagos/actions/runs/39207360080`
- `Source code`: `https://github.com/Lordt0m/crewcast-lagos`
- `Case study`: `projects/crewcast-lagos.html`

## Supporting Project: CiteGrid

**Title and descriptor — verified**

CiteGrid — reproducible citations for development data.

**Project summary — verified**

CiteGrid is a Django evidence ledger for comparing electricity access across Nigeria, Ghana, and Kenya. It records complete, immutable snapshots, shows revisions between them, and keeps a public example briefing pinned to the exact snapshot it cites.

**Engineering evidence — verified**

- Complete imports cover all nine country and indicator series in one publication transaction; partial imports do not publish a snapshot.
- A content hash identifies normalized observation records; a revision ledger records changed, new, and withdrawn values between adjacent published snapshots.
- The public example briefing and its CSV/source export remain tied to a specific snapshot.
- The offline suite found 121 tests: 120 passed and one PostgreSQL-only concurrency test skipped on SQLite.
- The PythonAnywhere demo and public GitHub source were inspected on 1 October 2026.

**Demo boundary — verified**

The hosted site contains simulated fixture data. It labels the example as simulated and must not be described as a live World Bank data feed. The World Bank is attributed as the indicator provider and underlying source; values in this demo are illustrative. The free PythonAnywhere site requires a monthly renewal in the owner's Web tab.

**Technology line — verified**

Python · Django · SQLite demo · HTML · CSS · PythonAnywhere

**Inspection actions — verified**

- `Live demo`: `https://lordtom.pythonanywhere.com/`
- `Example briefing`: `https://lordtom.pythonanywhere.com/comparisons/example/`
- `Source code`: `https://github.com/Lordt0m/citegrid`
- `Case study`: `projects/citegrid.html`

## Contact actions

**GitHub — verified**

- Label: `GitHub`
- Destination: `https://github.com/Lordt0m`

**Email — verified**

- Address: `ayotomiwa529@gmail.com`
- Destination: `mailto:ayotomiwa529@gmail.com`

**CV — verified**

- Asset: `assets/documents/ayotomiwa-ojo-cv.pdf`
- Rendered as direct download action on homepage hero.
- Include the verified production portfolio URL `https://ayotomiwa.pages.dev/`; do not include the former GitHub Pages address.

**LinkedIn — intentionally visible as inert status text**

- Render only the inert text `LinkedIn — coming soon`.
- Do not render an anchor, `#` link, or disabled control.

**Location — verified**

Lagos, Nigeria. Do not publish a street address or more precise location.

## Skills - verified

Publish five groups: Python; Django & REST APIs; SQL & PostgreSQL; React, TypeScript & Web; Git & Delivery. Python, data processing and database rules are supported by ShelfSum and Credence; Django REST and access-control work by Nobelese; React and TypeScript by SpecShift. Automated verification and delivery documentation are inspectable in the linked repositories.

## About - verified

I am a self-taught software developer in Lagos. I build usable interfaces, backend workflows, and the data models that connect them. My independent projects combine React and TypeScript interfaces with Django APIs and PostgreSQL workflows. I hold a B.A. in English and Literary Studies from Federal University Oye-Ekiti, a background that helps me explain and document technical decisions clearly.

I am also exploring systems programming with Rust, C++, and C as a direction for future projects. Across stacks, I care about useful products, explicit rules, and testable behaviour.

## KDN-focused selection | verified 13 November 2026

This is a general portfolio update supporting a specific application. No KDN employment, relationship or delivery is implied. No KDN problem claims are published on the portfolio.

### SpecShift - verified independent project

- React 19 and TypeScript interface with a Django REST Framework comparison service; README and web/package.json inspected on 13 November 2026.
- The public studio loaded with an explicitly recorded, synthetic comparison. This review did not execute a fresh API comparison or rerun its project tests.
- Supports a bounded OpenAPI 3.0.0-3.0.3 subset. Unsupported constructs create coverage gaps; graph reachability is not proof of client runtime failure.
- Public source: https://github.com/Lordt0m/specshift ; studio: https://specshift.pages.dev/ ; portfolio case study: projects/specshift.html.
- Homepage preview is a labelled illustrative rendering of the documented synthetic order API example, not a screenshot, benchmark or customer result.

### Nobelese - verified independent project

- Ojo & Associates appointment API is a fictional demonstration, not a law-firm client engagement.
- Django REST API with token-authenticated staff roles, public slot retrieval, pending request review and guarded confirmation/decline/cancellation workflows.
- booking/services.py and booking/permissions.py inspected on 13 November 2026. Confirmation uses an atomic transaction, locked records and database constraints.
- Public source: https://github.com/Lordt0m/nobelese ; portfolio case study: projects/nobelese.html.
- No public deployment endpoint was verified; publish source and case-study actions, not a live-demo button.

### Homepage and skill copy

- Hero: I build web applications from interface to database, with clear workflows and reliable systems underneath.
- Support: React and TypeScript interfaces, Django APIs, and PostgreSQL workflows. Built around clear user journeys, controlled access, and records people can inspect.
- Five groups remain: Python; Django & REST APIs; SQL & PostgreSQL; React, TypeScript & Web; Git & Delivery.
- About describes independent web/backend projects and an English and Literary Studies background. Future systems-language exploration is labelled as future work.
- The current PDF is a backend-specific CV. No general or tailored full-stack CV has been substituted or claimed.


## Orderlane independent concept | verified 13 November 2026

- Public Django application: https://orderlane-demo.onrender.com/ ; source: https://github.com/Lordt0m/lordt0m.github.io/tree/main/demos/orderlane ; case study: projects/orderlane.html.
- Independently inspired by FufuPlanet's advertised customer/vendor order features. No KDN affiliation, client engagement or missing-feature claim.
- Customer ordering and a vendor desk with server-owned menu prices, relational records, scoped restaurant queries, request-key uniqueness, legal status transitions, conditional revision updates and transactional audit events.
- All 23 API tests passed locally and during the hosted build. Live requests verified order creation, identical replay returning the same order, cross-restaurant 404 and the full lifecycle. No high-load or PostgreSQL concurrency test claim.
- Browser-session workspaces with an explicit demo role switcher, not production authentication. Temporary SQLite filesystem storage can reset. No payments, delivery or native mobile build.
- Preview on homepage is a labelled workflow overview, not a screenshot. Local customer screen and ordering were exercised; hosted/mobile visual QA remains unverified due to browser connection failure.


## Orderlane customer-first redesign | 14 November 2026

User selected customer ordering and free-only hosting, then dropped PythonAnywhere and requested retaining Render unless a clearly better free fit was established. Host and demo URL remain unchanged. No cold-start or latency improvement is claimed.

Current interface: local licensed dish photos, self-hosted Manrope, search/dietary filters, separate editable kitchen baskets, session draft recovery, confirmation, customer order history, secondary kitchen operations and Build details. Fictional starter orders are excluded from customer history. Uncertain requests retain their keys across reload.

Verification: 24 Django API tests and13 DOM integration checks against actual local Django API passed. Independent source-review findings on license links and history handling were fixed and rechecked. Browser connection was unavailable; no screenshot, mobile layout or visual-conformance claim. Photo licenses are attached per asset and in the interface.
