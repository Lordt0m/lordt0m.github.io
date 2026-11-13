# Orderlane

A compact, working customer-to-vendor ordering concept by Ayotomiwa Ojo. Independently inspired by FufuPlanet's publicly advertised vendor/order features. No affiliation with KDN, and no claim that these features are missing from its products.

## Review in two minutes

1. In Customer view, add meals and place a fictional order.
2. Switch to Vendor desk, choose the same restaurant, and progress the order through accepted, preparing, ready and completed.
3. Return to Customer and refresh to see its history.
4. Open Under the hood and run the live API checks. These call the server and show actual responses, not simulated assertions.

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
