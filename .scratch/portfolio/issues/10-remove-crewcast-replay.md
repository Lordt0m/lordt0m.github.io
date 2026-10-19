# 10: Remove retired CrewCast replay

Status: verified; authorised for publication

## Outcome

Remove the retired failure replay from the homepage and CrewCast case study. Replace the verbose comparison disclaimer with concise example wording. Refresh actual entry and Operations screenshots after the application cleanup. Preserve portfolio identity, other projects and honest demo/planning boundaries.

## Acceptance

- No public failure-replay action, capability claim or screenshot.
- Screenshots match the cleaned application.
- Structural verification and unit tests pass.
- Inspect affected pages at 360, 768, 1024 and 1440 pixels.
- Publish through the existing Git/Cloudflare integration and verify public content.

## Completion record

- Reviewed branch: codex/remove-crewcast-replay, based on production main. Application release 563aaa2 is live on Render.
- Removed replay actions, capability copy and screenshot from homepage/case study. Replaced the comparison disclaimer with concise window/conditions/reason copy and actual 19 October entry/Operations captures.
- CrewCast CI 39207360080 passed 102 PostgreSQL/Redis application tests and six frontend tests. Public Operations still exposes real retrieval history; forecast policies and demo restrictions are unchanged.
- Portfolio structural verification passed with zero errors; all 33 unit tests passed. Whitespace check passed.
- Inspected case study at 360, 768, 1024 and 1440 CSS pixels; homepage layouts at those widths had no document overflow. Screenshot assets loaded at 1425 pixels wide, current actions contain no replay destination, and screenshot links expose solid keyboard focus.
- Old application replay bookmarks redirect to /#planning, including with JavaScript disabled. Physical low-end devices and production Core Web Vitals were not measured in this cleanup.
- Next safe action: publish the reviewed portfolio branch through the existing main/Cloudflare integration, verify its public content and record the production ref in the programme output.
