# Public content and evidence register

This document owns approved public wording, destinations, and Claim state. Preserve meaning when adapting copy to fit a layout. Strengthen a Claim only after inspecting its Evidence.

## Identity and positioning

**Name — verified**

Ayotomiwa Ojo

**Role label — verified**

Python & Django Developer

**Primary statement — verified**

I build practical web applications and backend systems with Python and Django.

**Availability — verified**

Self-taught developer based in Lagos, Nigeria. Open to junior developer and internship opportunities.

**Hero actions**

- `View projects` — verified; link to `#projects`.
- `Download CV` — verified; link to `assets/documents/ayotomiwa-ojo-cv.pdf`.
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
- 271 local automated tests at the accepted release baseline, with the three PostgreSQL-only concurrency tests executed without skips in hosted PostgreSQL CI.
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

Verified screenshots copied from the ShelfSum repository's `docs/screenshots/` directory:
- `desktop-dashboard.png`: Owner dashboard metrics and activity summary
- `desktop-movements.png`: Immutable stock movement audit ledger
- `mobile-dashboard.png`: Responsive mobile dashboard view

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

**LinkedIn — intentionally visible as inert status text**

- Render only the inert text `LinkedIn — coming soon`.
- Do not render an anchor, `#` link, or disabled control.

**Location — verified**

Lagos, Nigeria. Do not publish a street address or more precise location.

## Skills — verified

Publish exactly five evidence-backed skill groups demonstrated by the portfolio projects:

- **Python:** Core Python 3.13, standard library, exact decimal arithmetic, CLI parsing, object-oriented domain services. Verified in Credence (zero runtime dependencies) and ShelfSum.
- **Django:** Django 5.2 LTS, server-rendered views, MTV architecture, custom authentication/permissions (Owner vs Staff Member), business-scoped queries, forms, CSRF protection. Verified in ShelfSum.
- **SQL & PostgreSQL:** Relational data modelling, PostgreSQL, Neon, transactions, integrity constraints, migrations, indexing, explainable reporting queries. Verified in ShelfSum.
- **HTML & CSS:** Semantic markup, responsive layouts, accessibility landmarks, visible focus states, zero-JS progressive enhancement. Verified in ShelfSum and Portfolio.
- **Git & GitHub:** Version control, focused commits, GitHub Actions CI, and release documentation. Verified across ShelfSum and Credence repositories.

## About — verified

**Prose — verified**

I am a self-taught developer focused on backend web development with Python, Django, and SQL. I hold a B.A. in English and Literary Studies from Federal University Oye-Ekiti. My background helps me communicate technical decisions clearly and document the systems I build.

I prioritize clean code, automated testing, and transactional integrity over speculative complexity, building practical software around clear operational rules.
