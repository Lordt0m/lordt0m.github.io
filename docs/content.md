# Public content and evidence register

This document owns approved public wording, destinations, and Claim state. Preserve meaning when adapting copy to fit a layout. Strengthen a Claim only after inspecting its Evidence.

## Identity and positioning

**Name — verified**

Ayotomiwa Ojo

**Role label — verified**

Python & Django Developer

**Primary statement — verified**

I build practical web applications and backend systems with Python, Django, and SQL. Focused on clean code, reliable systems, and solving real-world problems.

**Availability — verified**

Based in Lagos, Nigeria. Available for internship, graduate, associate, and junior Python or Django/backend opportunities, with onsite, hybrid, and Nigeria-remote roles prioritized.

**Hero actions**

- `View Projects` — verified; link to `#projects`.
- `GitHub` — verified; link to `https://github.com/Lordt0m`.
- `About` — verified; link to `#about`.
- `Download CV` — withheld until the final PDF exists at `assets/documents/ayotomiwa-ojo-cv.pdf` and has been inspected.
- `LinkedIn` — planned; do not render until a verified profile URL is recorded here.

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
- 268 local automated tests at the accepted release baseline, with the three PostgreSQL-only concurrency tests executed without skips in hosted PostgreSQL CI.
- Production deployment on Render with Neon PostgreSQL, WhiteNoise static handling, HTTPS-aware settings, and a health endpoint.
- Explicit domain services for transactional stock changes instead of hidden model signals.
- Public architecture decisions, invariant ownership, tickets, and release evidence in the repository.

**Trade-off — verified**

ShelfSum keeps a current Stock on Hand value for fast reads while recording every change in an immutable movement ledger. This makes the displayed balance efficient and independently explainable, at the cost of stricter transaction and reconciliation rules.

**Technology line — verified**

Python · Django · PostgreSQL · HTML · CSS · GitHub Actions · Render · Neon

**Inspection actions — verified**

- `Live Demo`: `https://shelfsum.onrender.com/`
- `Source Code`: `https://github.com/Lordt0m/shelfsum`
- `View Case Study`: initially link to the ShelfSum section itself only if an expanded in-page case study is visually distinct; otherwise omit this action rather than create a no-op link.

**Screenshot state — withheld**

Do not publish screenshots until ShelfSum Ticket 13 closes after restart-persistence and final responsive verification. When verified, prefer no more than three useful states: the Owner dashboard, a populated report, and an Audit Event or stock-history view.

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
- Credence has no hosted application. Do not render a `Live Demo` action.

## Featured Project: private books-and-TV journal

**State — planned**

Do not render as delivered work until a repository contains inspectable behaviour. When implemented, describe it as a private single-user journal with visitor or demo access; do not manufacture a product name, feature list, or completion claim here.

## Portfolio repository

**State — planned until the first implemented slice passes verification**

The portfolio itself may become a Supporting Project only after it demonstrates deliberate accessibility, responsive behaviour, evidence control, and deployment. Its existence alone is not an engineering Claim.

## Contact actions

**GitHub — verified**

- Label: `GitHub`
- Destination: `https://github.com/Lordt0m`

**Email — verified**

- Address: `ayotomiwa529@gmail.com`
- Render as a direct `mailto:ayotomiwa529@gmail.com` Inspection Action labelled `Email` or `Email me`.
- This is the owner-confirmed recruiter-facing address and is already published as package-author metadata in Credence.

**CV — withheld**

- Render `Download CV` only after the final PDF exists at `assets/documents/ayotomiwa-ojo-cv.pdf` and passes content and link inspection.

**LinkedIn — planned**

- The Contact interface supports a LinkedIn action.
- Do not render an empty icon, disabled action, `#` destination, or placeholder profile. Add the action when a verified public URL is recorded here.

**Location — verified**

Lagos, Nigeria. Do not publish a street address or more precise location.

## Skills — verified
 
Publish a skill only when at least one verified project demonstrates it.
 
- **Python:** Core Python 3.13, standard library, exact decimal arithmetic, CLI parsing, object-oriented domain services. Verified in Credence (zero runtime dependencies) and ShelfSum.
- **Django:** Django 5.2 LTS, server-rendered views, MTV architecture, custom authentication/permissions (Owner vs Staff Member), business-scoped queries, forms, CSRF protection. Verified in ShelfSum.
- **SQL & Databases:** Relational data modelling, PostgreSQL, Neon, transactions, integrity constraints, migrations, indexing, explainable reporting queries. Verified in ShelfSum.
- **HTML & CSS:** Semantic markup, responsive layouts, accessibility landmarks, visible focus states, zero-JS progressive enhancement. Verified in ShelfSum and Portfolio.
- **Git & GitHub:** Version control, disciplined vertical commits, GitHub Actions CI, pull requests, release documentation. Verified across ShelfSum and Credence repositories.
- **Testing:** Automated unit and integration testing, pytest, unittest, test isolation, deterministic fixtures, CI test matrices. Verified in ShelfSum (268 tests), Credence (35 tests), and Portfolio verification suite.
- **Deployment:** Production deployment, environment configuration, WhiteNoise static assets, health endpoints, hosted PostgreSQL, Render. Verified in ShelfSum on Render with Neon.

## About — verified

**Prose — verified**

I am a self-taught software developer based in Lagos, Nigeria, focused on backend web development with Python, Django, and SQL.

With a degree in English and Literary Studies, I combine technical discipline with clear communication—reading specifications closely, writing explainable architecture decisions, and building dependable systems.

I prioritize clean code, test coverage, and transactional integrity over speculative complexity, building practical software that solves real-world operational problems.

I am actively seeking internship, graduate, associate, and junior Python or Django/backend roles (onsite, hybrid, or Nigeria-remote).
