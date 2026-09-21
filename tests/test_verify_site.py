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
        </nav>
    </header>
    <main id="main-content">
        <section id="hero">
            <h1>Ayotomiwa Ojo</h1>
            <p>Python &amp; Django Developer</p>
            <p>I build practical web applications and backend systems with Python, Django, and SQL.</p>
            <p>Focused on clean code, reliable systems, and solving real-world problems.</p>
            <p>Based in Lagos, Nigeria. Available for internship, graduate, associate, and junior Python or Django/backend opportunities, with onsite, hybrid, and Nigeria-remote roles prioritized.</p>
            <div>
                <a href="#projects">View Projects</a>
                <a href="https://github.com/Lordt0m">GitHub</a>
                <a href="#about">About</a>
            </div>
        </section>
        <section id="projects">
            <h2>Projects</h2>
            <article id="shelfsum">
                <h3>ShelfSum</h3>
                <p>Explainable inventory and business activity for small shops.</p>
                <p>Python · Django · PostgreSQL · HTML · CSS · GitHub Actions · Render · Neon</p>
                <a href="https://shelfsum.onrender.com/">Live Demo</a>
                <a href="https://github.com/Lordt0m/shelfsum">Source Code</a>
            </article>
            <article id="credence">
                <h3>Credence</h3>
                <p>Deterministic cashbook validation and financial summaries from one Python command.</p>
                <p>Python · Standard Library · pytest · GitHub Actions · CSV · JSON</p>
                <a href="https://github.com/Lordt0m/credence">Source Code</a>
            </article>
        </section>
        <section id="skills">
            <h2>Skills</h2>
            <p>Python, Django, SQL, HTML/CSS, Git, Testing, Deployment.</p>
        </section>
        <section id="about">
            <h2>About</h2>
            <p>Self-taught developer with an English and Literary Studies degree.</p>
        </section>
        <section id="contact">
            <h2>Contact</h2>
            <p>Based in Lagos, Nigeria. Available for internship, graduate, associate, and junior Python or Django/backend opportunities, with onsite, hybrid, and Nigeria-remote roles prioritized.</p>
            <a href="mailto:ayotomiwa529@gmail.com">Email</a>
            <a href="https://github.com/Lordt0m">GitHub</a>
        </section>
    </main>
    <footer>
        <p>&copy; 2026 Ayotomiwa Ojo</p>
    </footer>
</body>
</html>
"""


class TestVerifySite(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        # Create css asset for valid baseline
        css_dir = self.root / "assets" / "css"
        css_dir.mkdir(parents=True)
        (css_dir / "site.css").write_text("/* test css */", encoding="utf-8")

    def tearDown(self):
        self.temp_dir.cleanup()

    def create_index(self, content: str):
        (self.root / "index.html").write_text(content, encoding="utf-8")

    def test_valid_minimal_site_passes(self):
        self.create_index(VALID_INDEX_HTML)
        errors = verify(self.root)
        self.assertEqual(errors, [])

    def test_missing_index_html(self):
        errors = verify(self.root)
        self.assertTrue(any("Missing required file" in e for e in errors))

    def test_multiple_or_missing_main_landmark(self):
        # Missing main
        content = VALID_INDEX_HTML.replace('<main id="main-content">', '<div id="main-content">').replace('</main>', '</div>')
        self.create_index(content)
        errors = verify(self.root)
        self.assertTrue(any("<main> landmark" in e for e in errors))

        # Duplicate main
        content = VALID_INDEX_HTML.replace('</main>', '</main><main id="extra"></main>')
        self.create_index(content)
        errors = verify(self.root)
        self.assertTrue(any("Expected exactly one <main>" in e for e in errors))

    def test_h1_heading_count(self):
        # Missing h1
        content = VALID_INDEX_HTML.replace("<h1>Ayotomiwa Ojo</h1>", "<h2>Ayotomiwa Ojo</h2>")
        self.create_index(content)
        errors = verify(self.root)
        self.assertTrue(any("Expected exactly one <h1>" in e for e in errors))

        # Multiple h1
        content = VALID_INDEX_HTML.replace("<h1>Ayotomiwa Ojo</h1>", "<h1>Ayotomiwa Ojo</h1><h1>Duplicate</h1>")
        self.create_index(content)
        errors = verify(self.root)
        self.assertTrue(any("Expected exactly one <h1>" in e for e in errors))

    def test_skipped_heading_level(self):
        # h1 followed directly by h3
        content = VALID_INDEX_HTML.replace("<h2>Projects</h2>", "<h3>Projects</h3>")
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
        # Point to missing CSS
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

    def test_withheld_content(self):
        # CV download
        content = VALID_INDEX_HTML.replace('<footer>', '<a href="assets/documents/ayotomiwa-ojo-cv.pdf">Download CV</a><footer>')
        self.create_index(content)
        errors = verify(self.root)
        self.assertTrue(any("CV download" in e for e in errors))

        # LinkedIn
        content = VALID_INDEX_HTML.replace('<footer>', '<a href="https://linkedin.com/in/test">LinkedIn</a><footer>')
        self.create_index(content)
        errors = verify(self.root)
        self.assertTrue(any("LinkedIn" in e for e in errors))

    def test_missing_required_sections(self):
        # Missing skills
        content = VALID_INDEX_HTML.replace('<section id="skills">', '<section id="other-skills">')
        self.create_index(content)
        errors = verify(self.root)
        self.assertTrue(any("skills" in e for e in errors))

        # Missing about
        content = VALID_INDEX_HTML.replace('<section id="about">', '<section id="other-about">')
        self.create_index(content)
        errors = verify(self.root)
        self.assertTrue(any("about" in e for e in errors))

    def test_missing_availability_statement(self):
        content = VALID_INDEX_HTML.replace('Based in Lagos, Nigeria. Available for internship, graduate, associate, and junior Python or Django/backend opportunities, with onsite, hybrid, and Nigeria-remote roles prioritized.', '')
        self.create_index(content)
        errors = verify(self.root)
        self.assertTrue(any("availability statement" in e for e in errors))

    def test_valid_and_invalid_404_page(self):
        self.create_index(VALID_INDEX_HTML)
        # Add invalid 404.html missing skip link and main
        (self.root / "404.html").write_text("<html><body><h1>404</h1></body></html>", encoding="utf-8")
        errors = verify(self.root)
        self.assertTrue(any("404.html: Expected exactly one <main>" in e for e in errors))

        # Fix 404.html with valid structure
        valid_404 = """<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>404</title><link rel="stylesheet" href="assets/css/site.css"></head>
<body>
    <a class="skip-link" href="#main-content">Skip</a>
    <main id="main-content"><h1>Page Not Found</h1><a href="index.html">Home</a></main>
</body></html>"""
        (self.root / "404.html").write_text(valid_404, encoding="utf-8")
        errors = verify(self.root)
        self.assertEqual(errors, [])

    def test_deploy_workflow_validation(self):
        self.create_index(VALID_INDEX_HTML)
        wf_dir = self.root / ".github" / "workflows"
        wf_dir.mkdir(parents=True, exist_ok=True)
        # Invalid workflow without verify_site.py
        (wf_dir / "deploy.yml").write_text("name: Deploy\nsteps: []", encoding="utf-8")
        errors = verify(self.root)
        self.assertTrue(any("must run scripts/verify_site.py" in e for e in errors))

        # Valid workflow with verify_site.py
        (wf_dir / "deploy.yml").write_text("name: Deploy\nsteps: [run: python scripts/verify_site.py]", encoding="utf-8")
        errors = verify(self.root)
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
