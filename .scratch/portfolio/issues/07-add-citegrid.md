# 07: Add CiteGrid to the public portfolio

**Status:** in progress

## Outcome

Add a concise CiteGrid project proof block and case study with verified links to the public source and hosted simulated demo.

## Acceptance

- [x] Verify the PythonAnywhere demo serves the Explore, Revisions, About, Replay, and example briefing pages with an explicit simulated-data label.
- [x] Update approved public wording and the four-project portfolio structure.
- [x] Add the homepage proof block and case study without implying the fixture values are live World Bank observations.
- [x] Pass structural verification and unit tests; inspect the affected page at 320, 360, 768, 1024, and 1440 CSS pixels.
- [ ] Push, verify CI and Cloudflare Pages production, and record the public ref and remaining limitations.

## Local evidence

- `python scripts/verify_site.py` passed with zero errors.
- `python -m unittest discover tests` passed 32 tests.
- Homepage and CiteGrid case study had no page-level horizontal overflow at 320, 360, 768, 1024, or 1440 CSS pixels. The new preview and case study were visually inspected at phone and desktop sizes.
- The CiteGrid preview title contrast was corrected after the desktop inspection.
