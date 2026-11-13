# Orderlane

An independent, small food-ordering concept by Ayotomiwa Ojo, inspired by FufuPlanet's advertised customer and vendor workflows. Not affiliated with KDN or FufuPlanet. No real orders, accounts, payments or delivery. Intended audience: engineering reviewers following a portfolio or application link.

Visitors place a fictional order, switch to the restaurant desk, and advance it through valid stages. An engineering panel runs actual API checks for idempotency, restaurant isolation and stale updates. Every browser session gets an isolated workspace. Demo role selection is not production authentication. SQLite records on free ephemeral hosting can disappear on restart.

Scope: same-origin Django JSON API, relational records, server-owned prices, transactional order creation, request replay protection, conditional status updates, audit events, responsive accessible vanilla JavaScript interface. No external assets, heavy framework, payment integration or background infrastructure.
