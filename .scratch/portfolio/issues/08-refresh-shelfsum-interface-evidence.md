# 08: Refresh ShelfSum interface evidence

Status: complete

## Outcome

Refresh the portfolio's ShelfSum screenshots from the released interface and review the animated public landing page. Prepare the portfolio update locally; do not publish it in this slice.

## Acceptance

- Capture current live landing, Owner dashboard, movement report and phone dashboard using only fictional demo data.
- Replace public references to the earlier screenshots and add the landing preview with clear captions and a link to experience its motion.
- Update evidence-controlled wording to the verified 288-test PostgreSQL release baseline.
- Review live normal/reduced motion, keyboard actions, interruption and responsive behaviour. Report material findings without claiming performance or hardware measurements not made.
- Pass structural verification and unit tests; inspect affected portfolio pages at 360, 768, 1024 and 1440 CSS pixels.
- Keep review evidence, source ref, capture dimensions, test results and publication state accurate.

## Completion record

- Ref: the local commit containing this ticket on codex/refresh-shelfsum-evidence; parent f7b315d. No push or publication.
- Replaced public screenshot references with four fresh captures of the live ShelfSum release e4f4acd415c294a29e4dcf30ecf6fc56a16137b2. Desktop images are 1425 by 990 from a 1440 by 1000 viewport; phone image is 390 by 844. All captures were visually inspected and show only fictional demo information.
- Added the landing preview, a live motion link, explanatory caption and native full-size screenshot links. Fixed excessive horizontal figure margins and kept focus outlines inside linked images. Homepage and case study now cite the verified 288-test PostgreSQL release. Corrected the case study's imprecise cash-flow wording.
- A regression for stale 271-test wording failed before the verifier repair. Final structural verifier passed with zero errors; all 33 unit tests passed; whitespace check passed. Both pages had no page overflow at 360, 768, 1024 and 1440 CSS pixels. Verified image loading and keyboard full-size access; visually inspected desktop and phone evidence sections.
- Motion review: Approve, no material motion finding. Live desktop Purchase/rapid replay/final settlement, immediate Enter replay, and reduced motion at desktop/phone widths passed. No ShelfSum code changed. A supplementary JavaScript-disabled browser pass was not completed after tab synchronization failed; previous release evidence is not relabelled as a new test. Physical devices and measured rendering performance remain outside this review.
- Review report is retained in programme outputs/shelfsum-landing/animated-landing-review.md, not public website content. Updated docs/content.md and docs/architecture.md agree with the implementation.
- Next safe action: obtain the user's publication instruction, then push/review and verify Cloudflare Pages serves the new images and case-study wording. The current live portfolio remains unchanged.
