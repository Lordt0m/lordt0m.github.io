# 06: Add CrewCast Lagos to the public portfolio

**Status:** complete

## Outcome

Publish an evidence-controlled CrewCast Lagos project proof block and case study after the automatic forecast schedule has been observed successfully on the live demo.

## Acceptance

- [x] Confirm a successful automatic GitHub Actions `schedule` event and its shared-database effect on the public Operations page.
- [x] Review the Antigravity changes, correct public-demo presentation and cache fallback, and pass CrewCast tests and CI.
- [x] Update the portfolio content register, specification, architecture, homepage, case study, and structural verifier.
- [x] Pass local portfolio structural verification and unit tests.
- [x] Inspect responsive layout and primary links.
- [x] Push the portfolio change, verify GitHub CI and Cloudflare Pages production, then record the public ref and remaining limitations.

## Evidence and claim boundary

- Automatic forecast run: `https://github.com/Lordt0m/crewcast-lagos/actions/runs/36246262643` (`schedule`, success, 26 September 2026).
- Reviewed CrewCast CI: `https://github.com/Lordt0m/crewcast-lagos/actions/runs/36247508159` (success).
- Public Operations page displayed six site attempts from the scheduled run. Some provider timeouts left sites stale; do not describe the whole board as fresh.
- Example jobs and sites are synthetic, retrieved forecasts are real, and the public demo is read-only.

## Completion record

- **Published portfolio ref:** `4be3ae12f84fcf32b9f64162d04d3ec91d2affe2` on `main`.
- **Portfolio CI:** [run 36250380908](https://github.com/Lordt0m/lordt0m.github.io/actions/runs/36250380908) passed for that ref.
- **Production:** `https://ayotomiwa.pages.dev/` displayed the three-project overview and CrewCast card; `https://ayotomiwa.pages.dev/projects/crewcast-lagos.html` opened the CrewCast case study with the verified schedule evidence and demo boundary.
- **Local checks:** `python scripts/verify_site.py` passed; `python -m unittest discover tests` passed 31 tests; `git diff --cached --check` passed before the release commit.
- **Responsive review:** Homepage and CrewCast case study were checked at 320, 360, 768, 1024, and 1440 CSS-pixel widths with no page-level horizontal overflow. The CrewCast preview was visually inspected at 360 px and primary card links met the 44 px target check.
- **CrewCast release:** Automatic `schedule` run [36246262643](https://github.com/Lordt0m/crewcast-lagos/actions/runs/36246262643) and final CrewCast CI [36248342118](https://github.com/Lordt0m/crewcast-lagos/actions/runs/36248342118) passed. The live Operations page showed the scheduled attempts, synthetic-job demo boundary, and generic public error wording without raw provider text.
- **Remaining limitations:** GitHub's schedule may be delayed or skipped, and Open-Meteo can time out; the demo's freshness display is essential. No real customers, always-on worker, or hosted Redis are claimed. The preview is an illustrative HTML/CSS rendering, not a screenshot of the live product.
- **Next safe action:** Keep the portfolio evidence current if deployment behaviour or the scheduled job changes; no further release action is required for this ticket.
