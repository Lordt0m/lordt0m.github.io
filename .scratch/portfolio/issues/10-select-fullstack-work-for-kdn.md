# 10: Select full-stack work and prepare KDN application evidence

Status: implementation and local verification complete; publication being verified

## Outcome

Publish an evidence-led full-stack portfolio selection led by ShelfSum, SpecShift and Nobelese. Preserve the pending full-stack refresh and the current remote CrewCast wording. Keep the KDN contribution brief separate from the general public portfolio.

## Acceptance

- Homepage presents React/TypeScript, Django/DRF and PostgreSQL evidence accurately.
- ShelfSum, SpecShift and Nobelese lead; existing projects remain inspectable.
- New case studies describe independent demonstrations and retain their limits.
- Native mobile, client employment and unverified deployment claims are withheld.
- Keep the existing CV honestly labelled Backend CV (PDF).
- Structural checks, existing verifier suite and responsive/keyboard review pass.
- Preserve current remote changes and verify the published site before declaring release.

## Completion record

- Reviewed local work based on `bb2f100`, with current remote main `ee8756b0c454890d66d8affc72c7b812454ff160` used to preserve CrewCast evidence and images.
- Homepage leads with ShelfSum, SpecShift and Nobelese; three other projects remain in a native expandable section. Added two case studies and evidence-backed React/TypeScript and REST API wording.
- `python scripts/verify_site.py`: pass, zero errors. `python -m unittest discover -s tests -q`: 33 passed. `git diff --check`: pass after newline normalization.
- Homepage and both new case studies checked at 320, 360, 768, 1024 and 1440 CSS pixels: no document overflow. Homepage had zero visible broken images. Desktop and phone screenshots inspected; native summary responds to Enter and shows a solid focus outline.
- Existing backend CV retains its accurate label. Native mobile and current Nobelese deployment claims remain withheld. SpecShift recorded sample and project limits remain explicit.
- One-page KDN contribution brief is a separate application artifact, outside the public portfolio checkout. No employer message or application was sent.
- Production commit and final deployed checks are recorded in the programme shared status after release.
