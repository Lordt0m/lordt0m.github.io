# Orderlane

A compact, working customer-to-vendor ordering concept by Ayotomiwa Ojo. Independently inspired by FufuPlanet's publicly advertised vendor/order features. No affiliation with KDN, and no claim that these features are missing from its products.

## Review in two minutes

1. Choose a kitchen, search or filter the menu, and add meals to the basket.
2. Place a fictional collection order and inspect its confirmation in Orders.
3. Open Kitchen from the confirmation or navigation, then accept and progress the order.
4. Return to Orders and refresh. Open API lab from the navigation to run actual API checks.

The customer-first interface uses locally hosted AI-generated food illustrations, a self-hosted Outfit font and a licensed unDraw cooking illustration. Separate baskets survive kitchen switches and session refreshes. An uncertain submission keeps its request key for a safe retry. Starter orders are labelled and shown in the kitchen view; they are excluded from customer history. The active files are `templates/counter.html`, `static/counter.css`, and `static/storefront.js`.

## Run locally

Python 3.12 or newer. From this directory:

```powershell
python -m venv .venv
.venv/Scripts/python -m pip install -r requirements.txt
.venv/Scripts/python manage.py migrate
.venv/Scripts/python manage.py test
.venv/Scripts/python manage.py runserver --insecure
```

On Linux use `.venv/bin/python`. `--insecure` serves local development assets with DEBUG disabled; production uses WhiteNoise and collectstatic. Visit the URL printed by Django.

## Frontend integration verification

With the local Django server running, install the development-only dependency using `npm install`, then run `npm run test:ui`. The 15 checks use jsdom against the real local Django API, including an interrupted response after the server accepts an order. They cover filtering, empty-state recovery, focus, separate kitchen baskets, reload recovery, confirmation, vendor updates, tracking, safe replay, generated-image disclosure, all twelve image endpoints, regional-description search and a complete six-dish basket. The expanded menu also passes 28 Django tests. Earlier browser captures cover the preceding five-meal layout at 1440, 1280, 390 and 320 CSS pixels; fresh viewport review of the twelve-meal update remains pending because browser screenshot approval review hit a usage limit. These checks do not establish a complete accessibility audit. Set `ORDERLANE_TEST_URL` to test another explicit deployment.

## Assets

The twelve active menu images are AI-generated food illustrations created with OpenAI's built-in image generation on 14 November 2026. They are disclosed in About & credits and `static/assets/credits.json`; they are not photographs of real restaurant orders. The shared brief is in `static/assets/menu-image-brief.json`: matching cream bowls, pale limestone, natural daylight and recognisable dish ingredients. The 960 x 720 JPEGs total 2,122,816 bytes. Earlier licensed photos are retained as unused source assets; their attribution remains in `static/assets/legacy-photo-credits.json`. The unDraw Cooking illustration and its permitted recolouring are recorded in `static/assets/illustration-source.json`. Outfit's SIL Open Font License is included as `static/assets/Outfit-OFL.txt`. All active assets are self-hosted.

Both kitchens have six meals. Lagos Kitchen adds amala with ewedu and gbegiri, ofada rice with ayamase, and vegetarian moi moi with pap. Ember & Grain adds waakye, thieboudienne, ndole with plantain and peri-peri chicken with rice. Menu prices are fictional demo prices in naira. The server catalogue owns names, prices and kitchen membership. The order row limit follows the selected kitchen's catalogue instead of a hardcoded five-meal maximum; the existing quantity, duplicate-row, restaurant-scope and replay protections remain.

## Hosting decision | 14 November 2026

The owner selected free-only hosting and explicitly dropped PythonAnywhere. Retain Render until a clearly better free fit is established. The redesign does not remove Render's free-tier wake-up delay or its temporary-storage limits. No latency improvement is claimed without measurement.

## API

All requests use the same origin and a browser session. `GET /api/bootstrap/` initializes a random workspace with two synthetic starter orders, returns menus, and sets a CSRF cookie. Writes require the CSRF header.

| Endpoint | Behaviour |
| --- | --- |
| POST /api/role/ | Choose customer, lagos or ember demo role |
| GET /api/orders/ | Return workspace orders, restricted to restaurant for vendor roles |
| POST /api/orders/ | Validate meals/quantities and server prices; require Idempotency-Key |
| GET /api/orders/{uuid}/ | Return a scoped order with its event history |
| POST /api/orders/{uuid}/status/ | Require the next legal status and expected revision |
| GET /health/ | Side-effect-free process liveness |

## Decisions worth inspecting

- Order and initial audit event are created in one database transaction. A database uniqueness constraint on workspace/request key prevents a repeated request from creating another order. Changed payloads under an existing key return 409. Normalized meal order gives equivalent carts the same fingerprint.
- Amounts are integer naira for this menu. Client totals are ignored. Meal names and prices come from the server catalogue.
- Vendor queries include both the server session's workspace and restaurant. Passing another order ID does not bypass this filter. The browser role selector is explicitly a demo feature, not a login or a production permission boundary between the visitor and demo roles.
- Status changes use an atomic conditional update of the previous status and revision. Exactly the matching revision can advance; the audit event commits with it. Invalid stages and old revisions return 409.
- Bounded request bodies, quantities and per-workspace order count limit the demo. This is not comprehensive abuse prevention. Expired sessions/orders need scheduled cleanup before longer use.
- Network failures preserve the submission key and cart for retry. A failed request never silently becomes client-only success.

## Limits

This is a small portfolio slice, not a delivery platform. No money moves. No production login, payment provider, delivery tracking, notifications or mobile-native build. Data is temporary SQLite on the free service filesystem and can reset after restarts or deployments. Workspaces are browser-session scoped. The service runs one Gunicorn worker with two threads; database contention returns a retryable response. Tests cover deterministic API behaviour, not high-load or PostgreSQL concurrency guarantees. Multi-tab role changes share the session and are outside the guided walkthrough; real authentication and tenant membership would replace the selector.

## Hosting

Source lives in the existing portfolio repository under `demos/orderlane/`. Build from repository root:

```sh
pip install -r demos/orderlane/requirements.txt
cd demos/orderlane
python manage.py test
python manage.py collectstatic --noinput
```

Start with a stable secret provided through the hosting environment:

```sh
cd demos/orderlane && python manage.py migrate --noinput && gunicorn config.wsgi:application --bind 0.0.0.0:$PORT --workers 1 --threads 2 --timeout 30
```

Set `SECRET_KEY` outside source control. Render supplies `RENDER_EXTERNAL_HOSTNAME`; only that host and local/test hosts are allowed. Browser API and assets are served from the same service, with CSRF checks and secure production cookies.
