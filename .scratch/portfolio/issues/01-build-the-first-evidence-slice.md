# 01: Build the first evidence slice

**Status:** ready

## Outcome

Deliver a coherent local page containing the approved hero, the complete ShelfSum Featured Project proof, the Credence Supporting Project proof, and verified contact actions, with the repository's structural verification interface in place.

## Read

- `AGENTS.md`
- `.scratch/portfolio/spec.md`
- `docs/content.md`: Identity and positioning; Featured Project: ShelfSum; Supporting Project: Credence; Contact actions
- `docs/architecture.md`: Public document, Presentation, Asset, and Verification modules
- `docs/adr/0001-use-a-static-progressively-enhanced-site.md`

## Acceptance

- [ ] Create semantic `index.html` with a skip link, header navigation, hero, `main-content`, `projects`, one complete ShelfSum Project Proof Block, one complete Credence Project Proof Block, `contact`, and a minimal footer.
- [ ] Use the approved wording and verified actions from `docs/content.md`; render GitHub and the confirmed recruiter email, but do not render withheld CV, LinkedIn, screenshots, About, Skills, or journal content.
- [ ] Render the verified GitHub destination and `mailto:ayotomiwa529@gmail.com` in the Contact section; GitHub may also appear in the hero when the action hierarchy remains clear.
- [ ] Create `assets/css/site.css` with named tokens, visible focus, bounded reading widths, and responsive behaviour from 320 CSS pixels upward.
- [ ] Keep the page fully usable without JavaScript. Create no JavaScript file unless an accepted interaction proves necessary.
- [ ] Create `scripts/verify_site.py` with the stable interface and checks defined in `docs/architecture.md` for the content that exists in this slice.
- [ ] Add focused standard-library tests for the verifier's pass and material failure cases.
- [ ] Provide accurate title, description, canonical-ready metadata, and social text; do not invent a deployed canonical URL or social image.
- [ ] Run the verifier and its tests.
- [ ] Serve the site locally and inspect 360, 768, 1024, and 1440 CSS-pixel widths, including keyboard navigation and visible focus.
- [ ] Confirm local and external links, no page-level horizontal overflow, and no withheld content or placeholders.
- [ ] Review the final diff against this ticket, commit one truthful slice, and append the completion record.

## Write boundary

This ticket may create only the first public slice, its stylesheet, verification module, verifier tests, and directly required documentation repairs. It must not add deployment configuration, speculative sections, claims beyond `docs/content.md`, a framework, a CMS, or visual assets.

## Completion record

Append only after every acceptance item is proved.
