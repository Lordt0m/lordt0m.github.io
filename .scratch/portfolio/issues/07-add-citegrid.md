# 07: Add CiteGrid to the public portfolio

**Status:** complete

## Outcome

Add a concise CiteGrid project proof block and case study with verified links to the public source and hosted simulated demo.

## Acceptance

- [x] Verify the PythonAnywhere demo serves the Explore, Revisions, About, Replay, and example briefing pages with an explicit simulated-data label.
- [x] Update approved public wording and the four-project portfolio structure.
- [x] Add the homepage proof block and case study without implying the fixture values are live World Bank observations.
- [x] Pass structural verification and unit tests; inspect the affected page at 320, 360, 768, 1024, and 1440 CSS pixels.
- [x] Push, verify CI and Cloudflare Pages production, and record the public ref and remaining limitations.

## Local evidence

- `python scripts/verify_site.py` passed with zero errors.
- `python -m unittest discover tests` passed 32 tests.
- Homepage and CiteGrid case study had no page-level horizontal overflow at 320, 360, 768, 1024, or 1440 CSS pixels. The new preview and case study were visually inspected at phone and desktop sizes.
- The CiteGrid preview title contrast was corrected after the desktop inspection.

## Completion record

- **Published portfolio ref:** `48ccfe16288fbf90b404a07a2566f92b120f89b5` on `main`.
- **Portfolio CI:** [run 36878831848](https://github.com/Lordt0m/lordt0m.github.io/actions/runs/36878831848) passed.
- **Production:** `https://ayotomiwa.pages.dev/` displayed the four-project overview and CiteGrid demo/source links. `https://ayotomiwa.pages.dev/projects/citegrid.html` opened the case study with the simulated-data boundary and working inspection links.
- **Local checks:** `python scripts/verify_site.py` passed; `python -m unittest discover tests` passed 32 tests; `git diff --cached --check` passed before the release commit.
- **Responsive review:** Homepage and CiteGrid case study were checked at 320, 360, 768, 1024, and 1440 CSS-pixel widths without page-level horizontal overflow. The CiteGrid preview and case study were visually inspected at phone and desktop widths.
- **Remaining limitations:** The PythonAnywhere site contains simulated SQLite demo values and must be renewed monthly in the Web tab. The PostgreSQL-only concurrency test was skipped on SQLite.
- **Next safe action:** Keep the PythonAnywhere demo active by extending its date before 1 November 2026, and revisit the portfolio link if the demo hostname changes.
