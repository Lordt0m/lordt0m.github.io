# 09: Refresh CrewCast interface evidence

Status: verified locally; authorised for publication

## Outcome

Update and publish the existing CrewCast homepage proof block and case study for release e7bcb5076d0c6d131952efbd397d7b449922d667. Preserve the portfolio's existing design and other project evidence.

## Acceptance

- Replace the old illustrative preview with an actual screenshot of the published app; show Operations and replay evidence on the case study.
- Record the verified 94-test PostgreSQL/Redis CI result and six frontend tests, progressive day navigation and current motion/accessibility limits.
- Preserve read-only, synthetic-job, scripted-replay and planning-aid boundaries; do not imply real users or a populated current live week.
- Pass the structural verifier and unit tests; inspect homepage and case study at 360, 768, 1024 and 1440px.
- Publish through the existing main/Cloudflare Pages integration; confirm the public pages and images and record the release evidence.

## Completion record

- Reviewed branch: codex/refresh-crewcast-evidence, based on production ref db33602. The release commit containing this record owns the source changes.
- Replaced the illustrative CrewCast homepage preview with an actual live entry capture; added entry, Operations and scripted caution-replay screenshots and full-size links to the case study. All are 1425 × 990 images from 1440 × 1000 viewports and were visually inspected.
- Updated docs/content.md first, then public wording and approved links. Current CrewCast release e7bcb50 and CI 38928513370 support the 94 PostgreSQL/Redis application-test and six frontend-test claims. Preserved real-retrieval versus synthetic-example distinctions, empty current-week capture context, planning limitations and physical-device/performance measurement limits.
- The verifier initially rejected three new unapproved evidence links. After their approval matched the content register, python scripts/verify_site.py passed with zero errors and python -m unittest discover tests passed all 33 tests. Whitespace check passed.
- Homepage and case study were inspected at 360, 768, 1024 and 1440 CSS pixels; no page-level horizontal overflow. Images loaded at their expected dimensions, phone galleries stacked, keyboard focus remained visible on full-size screenshot links. Fixed the new preview caption sharing a flex row with its image by using a scoped column layout.
- Publication is authorised by the user's request. Next safe action: publish this reviewed branch through main, wait for verification and Cloudflare Pages, then confirm the public homepage, case study and new image assets. Retain the final deployment ref and evidence in the programme's output report.
