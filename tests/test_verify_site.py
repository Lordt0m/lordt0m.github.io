#!/usr/bin/env python3
"""Standard-library unit tests for scripts/verify_site.py."""

from pathlib import Path
import tempfile
import unittest

from scripts.verify_site import verify


VALID_INDEX_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ayotomiwa Ojo — Python &amp; Django Developer</title>
    <link rel="stylesheet" href="assets/css/site.css">
</head>
<body>
    <a class="skip-link" href="#main-content">Skip to content</a>
    <header>
        <nav aria-label="Primary navigation">
            <a href="#projects">Projects</a>
            <a href="#skills">Skills</a>
            <a href="#about">About</a>
            <a href="#contact">Contact</a>
            <a href="https://github.com/Lordt0m">GitHub</a>
        </nav>
    </header>
    <main id="main-content">
        <section id="hero">
            <h1>Ayotomiwa Ojo</h1>
            <p>Python &amp; Django Developer</p>
            <p>I build practical web applications and backend systems with Python and Django.</p>
            <p>Self-taught developer based in Lagos, Nigeria. Open to junior developer and internship opportunities.</p>
            <div>
                <a href="#projects">View Projects</a>
                <a href="assets/documents/ayotomiwa-ojo-cv.pdf">Download CV</a>
                <a href="mailto:ayotomiwa529@gmail.com">Email</a>
                <a href="https://github.com/Lordt0m">GitHub</a>
            </div>
        </section>
        <section id="projects">
            <h2>Projects</h2>
            <article id="shelfsum" class="project-card">
                <h3>ShelfSum</h3>
                <p>Explainable inventory and business activity for small shops.</p>
                <p>271 automated tests.</p>
                <p>Owner: demo-owner@shelfsum.test / ShelfSumDemoOwner2026!</p>
                <p>Staff: demo-staff@shelfsum.test / ShelfSumDemoStaff2026!</p>
                <p>Python · Django · PostgreSQL · HTML · CSS · GitHub Actions · Render · Neon</p>
                <a href="https://shelfsum.onrender.com/">Live demo</a>
                <a href="https://github.com/Lordt0m/shelfsum">Source code</a>
                <a href="projects/shelfsum.html">Case study</a>
            </article>
            <article id="credence" class="project-card">
                <h3>Credence</h3>
                <p>Deterministic cashbook validation and financial summaries from one Python command.</p>
                <div id="credence-preview-title">Fictional sample data</div>
                <p>Processed rows: 10</p>
                <p>Valid rows: 4</p>
                <p>Invalid rows: 6</p>
                <p>Income: 75,000.00</p>
                <p>Expenses: 59,500.50</p>
                <p>Net cash movement: 15,499.50</p>
                <p>Python · Standard Library · pytest · GitHub Actions · CSV · JSON</p>
                <a href="https://github.com/Lordt0m/credence">Source code</a>
                <a href="projects/credence.html">Case study</a>
            </article>
        </section>
        <section id="skills">
            <h2>Skills</h2>
            <div class="skill-card"><h3>Python</h3></div>
            <div class="skill-card"><h3>Django</h3></div>
            <div class="skill-card"><h3>SQL &amp; PostgreSQL</h3></div>
            <div class="skill-card"><h3>HTML &amp; CSS</h3></div>
            <div class="skill-card"><h3>Git &amp; GitHub</h3></div>
        </section>
        <section id="about">
            <h2>About</h2>
            <p>Self-taught developer with an English and Literary Studies degree.</p>
        </section>
        <section id="contact">
            <h2>Contact</h2>
            <p>Feel free to reach out directly via email or view my source repositories on GitHub.</p>
            <a href="mailto:ayotomiwa529@gmail.com">Email</a>
            <a href="https://github.com/Lordt0m">GitHub</a>
            <span>LinkedIn — coming soon</span>
        </section>
    </main>
    <footer>
        <p>&copy; 2026 Ayotomiwa Ojo</p>
    </footer>
</body>
</html>
"""

VALID_SHELFSUM_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"><title>ShelfSum Case Study</title>
    <link rel="stylesheet" href="../assets/css/site.css">
</head>
<body>
    <a class="skip-link" href="#main-content">Skip to content</a>
    <main id="main-content">
        <h1>ShelfSum Case Study</h1>
        <p>271 automated tests.</p>
        <p>Owner: demo-owner@shelfsum.test / ShelfSumDemoOwner2026!</p>
        <p>Staff: demo-staff@shelfsum.test / ShelfSumDemoStaff2026!</p>
        <a href="../index.html">Back</a>
        <a href="https://shelfsum.onrender.com/">Live demo</a>
        <a href="https://github.com/Lordt0m/shelfsum">Source code</a>
    </main>
</body>
</html>"""

VALID_CREDENCE_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"><title>Credence Case Study</title>
    <link rel="stylesheet" href="../assets/css/site.css">
</head>
<body>
    <a class="skip-link" href="#main-content">Skip to content</a>
    <main id="main-content">
        <h1>Credence Case Study</h1>
        <div id="fixture-sample-title">Fictional sample data</div>
        <p>Processed rows: 10</p>
        <p>Valid rows: 4</p>
        <p>Invalid rows: 6</p>
        <p>Income: 75,000.00</p>
        <p>Expenses: 59,500.50</p>
        <p>Net cash movement: 15,499.50</p>
        <a href="../index.html">Back</a>
        <a href="https://github.com/Lordt0m/credence">Source code</a>
    </main>
</body>
</html>"""

VALID_404_HTML = """<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>404 Not Found</title><link rel="stylesheet" href="assets/css/site.css"></head>
<body>
    <a class="skip-link" href="#main-content">Skip</a>
    <main id="main-content"><h1>Page Not Found</h1><a href="index.html">Home</a></main>
</body></html>"""


class TestVerifySite(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)

        # Create assets
        css_dir = self.root / "assets" / "css"
        css_dir.mkdir(parents=True)
        (css_dir / "site.css").write_text("/* test css */", encoding="utf-8")

        docs_dir = self.root / "assets" / "documents"
        docs_dir.mkdir(parents=True)
        (docs_dir / "ayotomiwa-ojo-cv.pdf").write_bytes(b"%PDF-1.4 mock")

        # Create project case studies
        proj_dir = self.root / "projects"
        proj_dir.mkdir(parents=True)
        (proj_dir / "shelfsum.html").write_text(VALID_SHELFSUM_HTML, encoding="utf-8")
        (proj_dir / "credence.html").write_text(VALID_CREDENCE_HTML, encoding="utf-8")

        # Create 404 page
        (self.root / "404.html").write_text(VALID_404_HTML, encoding="utf-8")

        # Create index.html
        self.create_index(VALID_INDEX_HTML)

    def tearDown(self):
        self.temp_dir.cleanup()

    def create_index(self, content: str):
        (self.root / "index.html").write_text(content, encoding="utf-8")

    def test_valid_minimal_site_passes(self):
        errors = verify(self.root)
        self.assertEqual(errors, [])

    def test_missing_index_html(self):
        (self.root / "index.html").unlink()
        errors = verify(self.root)
        self.assertTrue(any("Missing required file" in e for e in errors))

    def test_multiple_or_missing_main_landmark(self):
        content = VALID_INDEX_HTML.replace('<main id="main-content">', '<div id="main-content">').replace('</main>', '</div>')
        self.create_index(content)
        errors = verify(self.root)
        self.assertTrue(any("<main> landmark" in e for e in errors))

        content = VALID_INDEX_HTML.replace('</main>', '</main><main id="extra"></main>')
        self.create_index(content)
        errors = verify(self.root)
        self.assertTrue(any("Expected exactly one <main>" in e for e in errors))

    def test_h1_heading_count(self):
        content = VALID_INDEX_HTML.replace("<h1>Ayotomiwa Ojo</h1>", "<h2>Ayotomiwa Ojo</h2>")
        self.create_index(content)
        errors = verify(self.root)
        self.assertTrue(any("Expected exactly one <h1>" in e for e in errors))

        content = VALID_INDEX_HTML.replace("<h1>Ayotomiwa Ojo</h1>", "<h1>Ayotomiwa Ojo</h1><h1>Duplicate</h1>")
        self.create_index(content)
        errors = verify(self.root)
        self.assertTrue(any("Expected exactly one <h1>" in e for e in errors))

    def test_skipped_heading_level(self):
        content = VALID_INDEX_HTML.replace("<h2>Projects</h2>", "<h4>Projects</h4>")
        self.create_index(content)
        errors = verify(self.root)
        self.assertTrue(any("Heading level skipped" in e for e in errors))

    def test_skip_link_missing_or_incorrect(self):
        content = VALID_INDEX_HTML.replace('<a class="skip-link" href="#main-content">Skip to content</a>', '')
        self.create_index(content)
        errors = verify(self.root)
        self.assertTrue(any("skip link" in e for e in errors))

    def test_nav_link_target_missing(self):
        content = VALID_INDEX_HTML.replace('<a href="#projects">Projects</a>', '<a href="#nonexistent">Projects</a>')
        self.create_index(content)
        errors = verify(self.root)
        self.assertTrue(any("nonexistent" in e for e in errors))

    def test_missing_local_asset(self):
        content = VALID_INDEX_HTML.replace('assets/css/site.css', 'assets/css/missing.css')
        self.create_index(content)
        errors = verify(self.root)
        self.assertTrue(any("Local asset 'assets/css/missing.css'" in e for e in errors))

    def test_empty_or_bare_hash_link(self):
        content = VALID_INDEX_HTML.replace('<a href="#projects">View Projects</a>', '<a href="#">View Projects</a>')
        self.create_index(content)
        errors = verify(self.root)
        self.assertTrue(any("Empty or bare hash link" in e for e in errors))

    def test_forbidden_placeholders(self):
        content = VALID_INDEX_HTML.replace('Ayotomiwa Ojo', 'Ayotomiwa Ojo TODO check this')
        self.create_index(content)
        errors = verify(self.root)
        self.assertTrue(any("TODO placeholder" in e for e in errors))

        content = VALID_INDEX_HTML.replace('Ayotomiwa Ojo', 'Ayotomiwa Ojo Lorem Ipsum dolor')
        self.create_index(content)
        errors = verify(self.root)
        self.assertTrue(any("Lorem ipsum" in e for e in errors))

    def test_machine_specific_paths(self):
        content = VALID_INDEX_HTML.replace('assets/css/site.css', 'C:\\Users\\Lord\\site.css')
        self.create_index(content)
        errors = verify(self.root)
        self.assertTrue(any("Windows absolute path" in e for e in errors))

    def test_unapproved_external_url(self):
        content = VALID_INDEX_HTML.replace('https://github.com/Lordt0m', 'https://twitter.com/unapproved')
        self.create_index(content)
        errors = verify(self.root)
        self.assertTrue(any("Unapproved external URL" in e for e in errors))

    def test_active_linkedin_link_rejected(self):
        content = VALID_INDEX_HTML.replace(
            '<span>LinkedIn — coming soon</span>',
            '<a href="https://linkedin.com/in/test">LinkedIn</a>'
        )
        self.create_index(content)
        errors = verify(self.root)
        self.assertTrue(any("LinkedIn" in e for e in errors))

    def test_missing_linkedin_inert_text(self):
        content = VALID_INDEX_HTML.replace('<span>LinkedIn — coming soon</span>', '')
        self.create_index(content)
        errors = verify(self.root)
        self.assertTrue(any("LinkedIn — coming soon" in e for e in errors))

    def test_missing_cv_pdf_file(self):
        (self.root / "assets" / "documents" / "ayotomiwa-ojo-cv.pdf").unlink()
        errors = verify(self.root)
        self.assertTrue(any("Missing required CV document" in e for e in errors))

    def test_missing_cv_link(self):
        content = VALID_INDEX_HTML.replace('<a href="assets/documents/ayotomiwa-ojo-cv.pdf">Download CV</a>', '')
        self.create_index(content)
        errors = verify(self.root)
        self.assertTrue(any("Missing link to verified CV PDF" in e for e in errors))

    def test_missing_case_study(self):
        (self.root / "projects" / "shelfsum.html").unlink()
        errors = verify(self.root)
        self.assertTrue(any("projects/shelfsum.html" in e for e in errors))

    def test_missing_required_sections(self):
        content = VALID_INDEX_HTML.replace('<section id="skills">', '<section id="other-skills">')
        self.create_index(content)
        errors = verify(self.root)
        self.assertTrue(any("skills" in e for e in errors))

    def test_missing_availability_statement(self):
        content = VALID_INDEX_HTML.replace(
            'Self-taught developer based in Lagos, Nigeria. Open to junior developer and internship opportunities.',
            ''
        )
        self.create_index(content)
        errors = verify(self.root)
        self.assertTrue(any("availability statement" in e for e in errors))

    def test_image_checks(self):
        # Missing alt
        content = VALID_INDEX_HTML.replace(
            '<h3>ShelfSum</h3>',
            '<h3>ShelfSum</h3><img src="assets/images/favicon.svg">'
        )
        self.create_index(content)
        errors = verify(self.root)
        self.assertTrue(any("missing required 'alt'" in e for e in errors))

        # Missing image file on disk
        content = VALID_INDEX_HTML.replace(
            '<h3>ShelfSum</h3>',
            '<h3>ShelfSum</h3><img src="assets/images/missing.png" alt="Missing screenshot">'
        )
        self.create_index(content)
        errors = verify(self.root)
        self.assertTrue(any("does not exist on disk" in e for e in errors))

        # Forbidden avatar / photo
        content = VALID_INDEX_HTML.replace(
            '<h3>ShelfSum</h3>',
            '<h3>ShelfSum</h3><img src="assets/images/my-photo.jpg" alt="Author photo">'
        )
        self.create_index(content)
        errors = verify(self.root)
        self.assertTrue(any("Forbidden photograph" in e for e in errors))

    def test_stale_or_unsupported_public_claims(self):
        replacements = {
            "271 automated tests.": "268 automated tests.",
            "Explainable inventory": "Production-ready inventory",
            "demo-owner@shelfsum.test": "demo_owner",
            "demo-staff@shelfsum.test": "demo_staff",
        }
        for current, stale in replacements.items():
            with self.subTest(stale=stale):
                self.create_index(VALID_INDEX_HTML.replace(current, stale))
                errors = verify(self.root)
                self.assertTrue(any("Forbidden public content" in e for e in errors))

    def test_phone_number_is_withheld_from_html(self):
        self.create_index(VALID_INDEX_HTML.replace("Lagos, Nigeria", "Lagos, Nigeria 09151855301"))
        errors = verify(self.root)
        self.assertTrue(any("phone number withheld" in e for e in errors))

    def test_exact_project_and_skill_counts(self):
        self.create_index(VALID_INDEX_HTML.replace(' class="project-card"', '', 1))
        errors = verify(self.root)
        self.assertTrue(any("exactly 2 project cards" in e for e in errors))

        self.create_index(VALID_INDEX_HTML.replace(' class="skill-card"', '', 1))
        errors = verify(self.root)
        self.assertTrue(any("exactly 5 skill groups" in e for e in errors))

    def test_inline_styles_are_rejected(self):
        self.create_index(VALID_INDEX_HTML.replace('<section id="about">', '<section id="about" style="padding: 1rem">'))
        errors = verify(self.root)
        self.assertTrue(any("Inline style attributes" in e for e in errors))

    def test_additional_public_html_is_verified(self):
        (self.root / "projects" / "extra.html").write_text(
            "<html><body><h1>Missing main and skip link</h1></body></html>",
            encoding="utf-8",
        )
        errors = verify(self.root)
        self.assertTrue(any("projects/extra.html" in e for e in errors))

    def test_relative_link_cannot_escape_repository(self):
        self.create_index(VALID_INDEX_HTML.replace('href="#projects">View Projects', 'href="../outside.html">View Projects'))
        errors = verify(self.root)
        self.assertTrue(any("escapes the repository" in e for e in errors))

    def test_valid_and_invalid_404_page(self):
        (self.root / "404.html").write_text("<html><body><h1>404</h1></body></html>", encoding="utf-8")
        errors = verify(self.root)
        self.assertTrue(any("404.html: Expected exactly one <main>" in e for e in errors))

    def test_deploy_workflow_validation(self):
        wf_dir = self.root / ".github" / "workflows"
        wf_dir.mkdir(parents=True, exist_ok=True)
        (wf_dir / "deploy.yml").write_text("name: Deploy\nsteps: []", encoding="utf-8")
        errors = verify(self.root)
        self.assertTrue(any("must run scripts/verify_site.py" in e for e in errors))

        (wf_dir / "deploy.yml").write_text("name: Deploy\nsteps: [run: python scripts/verify_site.py]", encoding="utf-8")
        errors = verify(self.root)
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
