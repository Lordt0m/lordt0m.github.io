# Align the portfolio and downloadable CV

Written against: `0322363b30253c9266b8a0d42133428861ab258c`

## Evidence chain

- Surface: the owner-supplied `Ayotomiwa_Ojo_Python_Django_CV.docx`, homepage identity and About copy, skills, contact actions, and CV download.
- Problem: the portfolio omits the CV, while its current wording repeats broad claims. The supplied CV provides authoritative personal details but its selected-work section lists earlier concepts rather than the stronger, currently verifiable ShelfSum and Credence repositories.
- Design evidence: the owner asked for the portfolio and CV to agree, fewer important tools, accurate wording, and a beautiful recruiter-facing result.
- Owner: `docs/content.md` owns approved public claims; the CV source owns personal facts; ShelfSum and Credence own project facts.
- Scope and affected surfaces: downloadable CV, hero, skills, About, Contact, metadata, and verification rules.
- Uncertainty: no LinkedIn URL is available. Do not infer one.

## Design decision

Use the supplied CV for identity, contact, education, certifications, background, and positioning. Use ShelfSum and Credence as the authoritative source for project claims. Produce a refreshed recruiter CV whose project evidence matches the portfolio, then publish its inspected PDF as the homepage download.

Do not import the older GridAware, IntakeGuard, FixFlow, StockGuard API, or book-scraper concepts into the homepage. They may be omitted from the revised CV because the owner selected ShelfSum and Credence as the portfolio projects. Do not invent work history to fill the space.

## Reuse

- Owner-supplied source: `Ayotomiwa_Ojo_Python_Django_CV.docx`.
- Verified personal facts: Ayotomiwa Ojo; Python & Django Developer; Lagos, Nigeria; `ayotomiwa529@gmail.com`; `github.com/Lordt0m`; B.A. English and Literary Studies from Federal University Oye-Ekiti, completed October 2023; NYSC Certificate of National Service, February 2025; Nigerian Red Cross Society certificate.
- Verified project evidence: ShelfSum and Credence repositories and their current documentation.

## Changes

1. Revised CV source and PDF
   - Change: create a polished, ATS-friendly CV with clear hierarchy and no decorative columns that damage text extraction. Keep it concise and ideally within two pages.
   - Recommended order: name and contact; profile; selected projects; core skills; education; certifications.
   - Projects: ShelfSum and Credence only, with two or three factual achievement bullets each and direct repository links; include ShelfSum's live demo.
   - Core skills: Python, Django, SQL/PostgreSQL, HTML/CSS, Git/GitHub, and testing. Keep CSV, JSON, REST, pytest, CI, Render, Neon, requests, BeautifulSoup, pathlib, and virtual environments inside project bullets or omit them when space is tight.
   - Preserve: phone `09151855301` in the downloadable CV unless the owner later asks to remove it. Do not publish the phone number on the webpage.
   - Verify: DOCX and PDF contain no unsupported work experience, dates, customers, usage metrics, coverage percentages, or responsibilities.

2. `assets/documents/ayotomiwa-ojo-cv.pdf`
   - Change: save the final visually inspected PDF at this stable path and wire `Download CV` to it with a descriptive filename.
   - Preserve: a working browser download and readable print output.
   - Verify: PDF opens, all links work, text is selectable, contact details are correct, and no text is clipped.

3. `docs/content.md`
   - Change: make the following copy authoritative:
     - Hero statement: `I build practical web applications and backend systems with Python and Django.`
     - Availability: `Self-taught developer based in Lagos, Nigeria. Open to junior developer and internship opportunities.`
     - About: `I am a self-taught developer focused on backend web development with Python, Django, and SQL. I hold a B.A. in English and Literary Studies from Federal University Oye-Ekiti. My background helps me communicate technical decisions clearly and document the systems I build.`
   - Change: mark the inspected CV PDF as verified.
   - Change: record LinkedIn as intentionally visible but unavailable: render only the inert text `LinkedIn — coming soon` until the owner supplies the exact URL.
   - Preserve: GitHub and email destinations.
   - Verify: no repeated availability paragraph, no broad `production-ready` wording, and no unsupported strength claim.

4. Public metadata
   - Change: update title, description, Open Graph, and sharing copy to match the new concise positioning.
   - Preserve: no invented canonical domain before Cloudflare deployment succeeds.
   - Verify: metadata contains Ayotomiwa Ojo, Python/Django positioning, and no stale GitHub Pages URL after migration.

5. Verification
   - Change: require the CV file and correct download path, reject placeholder LinkedIn anchors, and permit the exact inert LinkedIn status text.
   - Preserve: machine-path, missing-link, placeholder, and evidence checks.
   - Verify: removing the CV, adding `href="#"` to LinkedIn, or publishing an unapproved external profile fails verification.

## Scope

- Inherit: hero, skills, About, Contact, metadata, and CV download.
- Verify: CV text, PDF rendering, links, responsive presentation, and evidence register.
- Exclude: employment-history invention, reference letters, cover letters, LinkedIn profile creation, telephone display on the webpage, or changing the two project repositories.

## Validation

- Product: the website and CV agree on identity, role, location, education, strongest projects, essential skills, email, and GitHub.
- Interface: `Download CV` is visible in the opening section and works on mobile and desktop; LinkedIn is visibly pending without behaving like a link.
- System: the CV is the only downloadable resume artifact and uses the stable asset path.
- Repository: `python scripts/verify_site.py` and `python -m unittest discover tests` pass.

## Stop conditions

- Stop if CV generation would require inventing work history or unsupported project claims.
- Stop if the supplied contact details differ from owner-confirmed repository evidence; report the conflict instead of choosing silently.
- Do not add LinkedIn until the owner supplies the exact profile URL.

## Design documentation

- After acceptance and validation: record the final CV state and exact public wording in `docs/content.md`; record the stable CV asset contract in `docs/architecture.md`.
