#!/usr/bin/env python3
"""Structural verification for portfolio repository.

Checks semantic structure, links, assets, accessibility landmarks,
evidence-controlled URLs, required sections, image alternative text,
and absence of placeholders across all public HTML documents.
"""

from html.parser import HTMLParser
from pathlib import Path
from collections import Counter
import re
import sys
from urllib.parse import urlparse

# Approved external destinations from docs/content.md
APPROVED_EXTERNAL_URLS = {
    "https://github.com/Lordt0m",
    "https://shelfsum.onrender.com/",
    "https://github.com/Lordt0m/shelfsum",
    "https://github.com/Lordt0m/credence",
    "mailto:ayotomiwa529@gmail.com",
}

CANONICAL_URLS = {
    "index.html": "https://ayotomiwa.pages.dev/",
    "projects/shelfsum.html": "https://ayotomiwa.pages.dev/projects/shelfsum.html",
    "projects/credence.html": "https://ayotomiwa.pages.dev/projects/credence.html",
}

FORBIDDEN_TEXT_PATTERNS = [
    (re.compile(r"\bTODO\b", re.IGNORECASE), "TODO placeholder"),
    (re.compile(r"\bFIXME\b", re.IGNORECASE), "FIXME placeholder"),
    (re.compile(r"\blorem\s+ipsum\b", re.IGNORECASE), "Lorem ipsum placeholder text"),
]

FORBIDDEN_PUBLIC_FACT_PATTERNS = [
    (re.compile(r"\bproduction-ready\b", re.IGNORECASE), "unsupported 'production-ready' claim"),
    (re.compile(r"\bdemo_owner\b", re.IGNORECASE), "stale ShelfSum demo username 'demo_owner'"),
    (re.compile(r"\bdemo_staff\b", re.IGNORECASE), "stale ShelfSum demo username 'demo_staff'"),
    (re.compile(r"\b268\s+automated\s+tests?\b", re.IGNORECASE), "stale ShelfSum test total"),
    (re.compile(r"\batomic\s+staged", re.IGNORECASE), "unsupported atomic publication claim"),
    (re.compile(r"09151855301"), "phone number withheld from the website"),
    (re.compile(r"lordt0m\.github\.io", re.IGNORECASE), "stale GitHub Pages production URL"),
]

SHELFSUM_DEMO_CREDENTIALS = (
    "demo-owner@shelfsum.test",
    "ShelfSumDemoOwner2026!",
    "demo-staff@shelfsum.test",
    "ShelfSumDemoStaff2026!",
)

CREDENCE_FIXTURE_VALUES = (
    "Processed rows: 10",
    "Valid rows: 4",
    "Invalid rows: 6",
    "75,000.00",
    "59,500.50",
    "15,499.50",
)

MACHINE_PATH_PATTERNS = [
    (re.compile(r"[a-zA-Z]:[\\/][a-zA-Z0-9_.\-\\]+"), "Windows absolute path"),
    (re.compile(r"file:///", re.IGNORECASE), "file:/// URI"),
    (re.compile(r"/(?:Users|home)/[a-zA-Z0-9_.\-]+"), "User home directory path"),
]


class SiteHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.main_count = 0
        self.main_id = None
        self.h1_count = 0
        self.headings = []  # (level, line_num)
        self.ids = set()
        self.duplicate_ids = set()
        self.class_counts = Counter()
        self.inline_style_lines = []
        self.links = []  # (tag, href, text, is_nav, line_num, attrs)
        self.assets = []  # (tag, attr, val, rel, line_num)
        self.meta_properties = []  # (property, content, line_num)
        self.images = []  # (attrs, line_num)
        self.in_nav = False
        self.current_a = None
        self.text_chunks = []

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        line_num = self.getpos()[0]

        if "id" in attr_dict:
            element_id = attr_dict["id"]
            if element_id in self.ids:
                self.duplicate_ids.add(element_id)
            self.ids.add(element_id)

        for class_name in attr_dict.get("class", "").split():
            self.class_counts[class_name] += 1

        if "style" in attr_dict:
            self.inline_style_lines.append(line_num)

        if tag == "main":
            self.main_count += 1
            if "id" in attr_dict:
                self.main_id = attr_dict["id"]

        if tag == "h1":
            self.h1_count += 1

        if re.match(r"^h[1-6]$", tag):
            self.headings.append((int(tag[1]), line_num))

        if tag == "nav":
            self.in_nav = True

        if tag == "a":
            href = attr_dict.get("href")
            self.current_a = {
                "href": href,
                "text": [],
                "is_nav": self.in_nav,
                "line": line_num,
                "attrs": attr_dict,
            }

        if tag == "link":
            href = attr_dict.get("href")
            rel = attr_dict.get("rel", "")
            if href:
                self.assets.append(("link", "href", href, rel, line_num))

        if tag == "meta" and "property" in attr_dict:
            self.meta_properties.append(
                (attr_dict["property"], attr_dict.get("content", ""), line_num)
            )

        if tag == "script":
            src = attr_dict.get("src")
            if src:
                self.assets.append(("script", "src", src, "", line_num))

        if tag == "img":
            self.images.append((attr_dict, line_num))

    def handle_endtag(self, tag):
        if tag == "nav":
            self.in_nav = False
        if tag == "a" and self.current_a:
            text = "".join(self.current_a["text"]).strip()
            self.links.append(
                (
                    "a",
                    self.current_a["href"],
                    text,
                    self.current_a["is_nav"],
                    self.current_a["line"],
                    self.current_a["attrs"],
                )
            )
            self.current_a = None

    def handle_data(self, data):
        if self.current_a is not None:
            self.current_a["text"].append(data)
        self.text_chunks.append(data)


def parse_and_collect_ids(file_path: Path) -> set[str]:
    """Extract all IDs from an HTML file."""
    if not file_path.is_file():
        return set()
    try:
        content = file_path.read_text(encoding="utf-8")
        parser = SiteHTMLParser()
        parser.feed(content)
        return parser.ids
    except Exception:
        return set()


def verify_html_document(
    html_file: Path, repo_root: Path
) -> tuple[list[str], SiteHTMLParser, str]:
    errors = []
    rel_path = html_file.relative_to(repo_root).as_posix()

    try:
        content = html_file.read_text(encoding="utf-8")
    except Exception as exc:
        return [f"{rel_path}: Failed to read file: {exc}"], None, ""

    # Check for machine-specific paths
    for pattern, label in MACHINE_PATH_PATTERNS:
        matches = pattern.findall(content)
        if matches:
            errors.append(f"{rel_path}: Forbidden {label} found: {matches[:3]}")

    # Check for forbidden placeholders
    for pattern, label in FORBIDDEN_TEXT_PATTERNS:
        matches = pattern.findall(content)
        if matches:
            errors.append(f"{rel_path}: Forbidden placeholder found: {label}")

    for pattern, label in FORBIDDEN_PUBLIC_FACT_PATTERNS:
        if pattern.search(content):
            errors.append(f"{rel_path}: Forbidden public content found: {label}")

    parser = SiteHTMLParser()
    try:
        parser.feed(content)
    except Exception as exc:
        errors.append(f"{rel_path}: HTML parsing error: {exc}")
        return errors, parser, content

    # Exactly one main landmark with id="main-content"
    if parser.main_count != 1:
        errors.append(
            f"{rel_path}: Expected exactly one <main> landmark, found {parser.main_count}"
        )
    elif parser.main_id != "main-content":
        errors.append(
            f"{rel_path}: Expected <main> to have id='main-content', found id='{parser.main_id}'"
        )

    # Exactly one level-one heading
    if parser.h1_count != 1:
        errors.append(
            f"{rel_path}: Expected exactly one <h1> heading, found {parser.h1_count}"
        )

    if parser.duplicate_ids:
        errors.append(
            f"{rel_path}: Duplicate element IDs found: {sorted(parser.duplicate_ids)}"
        )

    if parser.inline_style_lines:
        errors.append(
            f"{rel_path}: Inline style attributes found on lines {parser.inline_style_lines}; use assets/css/site.css"
        )

    expected_canonical = CANONICAL_URLS.get(rel_path)
    if expected_canonical:
        canonical_links = [
            val for tag, _, val, rel, _ in parser.assets
            if tag == "link" and rel.lower() == "canonical"
        ]
        if canonical_links != [expected_canonical]:
            errors.append(
                f"{rel_path}: Expected one canonical URL '{expected_canonical}', found {canonical_links}"
            )
        og_urls = [
            value for prop, value, _ in parser.meta_properties if prop.lower() == "og:url"
        ]
        if og_urls != [expected_canonical]:
            errors.append(
                f"{rel_path}: Expected one og:url '{expected_canonical}', found {og_urls}"
            )

    # Heading hierarchy (no skipping levels)
    prev_level = 0
    for level, line in parser.headings:
        if prev_level > 0 and level > prev_level + 1:
            errors.append(
                f"{rel_path}:{line}: Heading level skipped from h{prev_level} to h{level}"
            )
        prev_level = level

    # Skip link pointing to #main-content
    first_link = parser.links[0] if parser.links else None
    if not first_link or first_link[1] != "#main-content":
        errors.append(
            f"{rel_path}: Expected first link to be skip link pointing to #main-content, found {first_link[1] if first_link else 'none'}"
        )

    # Links verification
    for _, href, text, is_nav, line, attrs in parser.links:
        if href is None or href == "" or href == "#":
            errors.append(
                f"{rel_path}:{line}: Empty or bare hash link found with text '{text}'"
            )
            continue

        if href.startswith("#"):
            target_id = href[1:]
            if target_id not in parser.ids:
                errors.append(
                    f"{rel_path}:{line}: Fragment link target id '{target_id}' does not exist in document"
                )
        elif href.startswith(("http://", "https://", "mailto:")):
            if "linkedin.com" in href.lower():
                errors.append(
                    f"{rel_path}:{line}: LinkedIn link is withheld until verified profile exists"
                )
            elif href not in APPROVED_EXTERNAL_URLS:
                errors.append(
                    f"{rel_path}:{line}: Unapproved external URL '{href}' not in docs/content.md"
                )
        else:
            # Local relative path
            path_part, _, fragment = href.partition("#")
            clean_path = path_part.split("?")[0]
            if clean_path:
                target_file = (html_file.parent / clean_path).resolve()
                if not target_file.is_relative_to(repo_root):
                    errors.append(
                        f"{rel_path}:{line}: Local link target '{clean_path}' escapes the repository"
                    )
                elif not target_file.exists():
                    errors.append(
                        f"{rel_path}:{line}: Local link target '{clean_path}' does not exist on disk"
                    )
                elif fragment and target_file.suffix == ".html":
                    target_ids = parse_and_collect_ids(target_file)
                    if fragment not in target_ids:
                        errors.append(
                            f"{rel_path}:{line}: Target id '{fragment}' does not exist in '{clean_path}'"
                        )

    # Asset verification (<link>, <script>)
    for tag, attr, val, rel, line in parser.assets:
        if tag == "link" and rel.lower() == "canonical":
            continue
        if val.startswith(("http://", "https://")):
            if val not in APPROVED_EXTERNAL_URLS:
                errors.append(f"{rel_path}:{line}: Unapproved external asset '{val}'")
        else:
            clean_path = val.split("?")[0].split("#")[0]
            target_asset = (html_file.parent / clean_path).resolve()
            if not target_asset.is_relative_to(repo_root):
                errors.append(
                    f"{rel_path}:{line}: Local asset '{clean_path}' escapes the repository"
                )
            elif not target_asset.exists():
                errors.append(
                    f"{rel_path}:{line}: Local asset '{clean_path}' in <{tag} {attr}='{val}'> does not exist"
                )

    # Image verification
    for attrs, line in parser.images:
        src = attrs.get("src", "")
        alt = attrs.get("alt")
        if alt is None:
            errors.append(f"{rel_path}:{line}: <img> missing required 'alt' attribute")
        elif not alt.strip():
            errors.append(f"{rel_path}:{line}: <img> has empty 'alt' attribute")

        if any(term in src.lower() for term in ("photo", "avatar", "headshot")):
            errors.append(
                f"{rel_path}:{line}: Forbidden photograph or photo placeholder found in '{src}'"
            )

        if src:
            clean_src = src.split("?")[0].split("#")[0]
            target_img = (html_file.parent / clean_src).resolve()
            if not target_img.is_relative_to(repo_root):
                errors.append(
                    f"{rel_path}:{line}: Image path '{clean_src}' escapes the repository"
                )
            elif not target_img.exists():
                errors.append(
                    f"{rel_path}:{line}: Image file '{clean_src}' does not exist on disk"
                )

    return errors, parser, content


def verify(repo_root: Path = Path(".")) -> list[str]:
    errors = []
    repo_root = repo_root.resolve()

    index_file = repo_root / "index.html"
    if not index_file.is_file():
        return [f"Missing required file: {index_file}"]

    required_html_files = {
        repo_root / "index.html",
        repo_root / "404.html",
        repo_root / "projects" / "shelfsum.html",
        repo_root / "projects" / "credence.html",
    }
    for required_file in sorted(required_html_files):
        if not required_file.is_file():
            errors.append(
                f"Missing required HTML document: {required_file.relative_to(repo_root).as_posix()}"
            )

    public_html_files = set(repo_root.glob("*.html"))
    projects_dir = repo_root / "projects"
    if projects_dir.is_dir():
        public_html_files.update(projects_dir.rglob("*.html"))

    parsed_documents = {}
    for html_file in sorted(public_html_files):
        document_errors, parser, content = verify_html_document(html_file, repo_root)
        errors.extend(document_errors)
        parsed_documents[html_file] = (parser, content)

    index_parser, index_content = parsed_documents.get(index_file, (None, ""))
    if index_parser is None:
        return errors
    index_visible_text = re.sub(r"\s+", " ", " ".join(index_parser.text_chunks)).strip()

    # Check required section IDs on index.html
    required_ids = {"main-content", "projects", "skills", "about", "contact"}
    missing_ids = required_ids - index_parser.ids
    if missing_ids:
        errors.append(
            f"index.html: Required section IDs missing: {sorted(list(missing_ids))}"
        )

    if index_parser.class_counts["project-card"] != 2:
        errors.append(
            f"index.html: Expected exactly 2 project cards, found {index_parser.class_counts['project-card']}"
        )

    if index_parser.class_counts["skill-card"] != 5:
        errors.append(
            f"index.html: Expected exactly 5 skill groups, found {index_parser.class_counts['skill-card']}"
        )

    # Check required external URLs present on index.html
    found_external_urls = {
        href
        for _, href, _, _, _, _ in index_parser.links
        if href and href.startswith(("http://", "https://", "mailto:"))
    }
    for approved_url in APPROVED_EXTERNAL_URLS:
        if approved_url not in found_external_urls:
            errors.append(
                f"index.html: Required approved external URL missing: {approved_url}"
            )

    # Check inspection actions (Live demo and Source code)
    has_live_demo = any(
        "live demo" in text.lower() for _, _, text, _, _, _ in index_parser.links
    )
    has_source_code = any(
        "source code" in text.lower() for _, _, text, _, _, _ in index_parser.links
    )
    if not (has_live_demo and has_source_code):
        errors.append(
            "index.html: Required project inspection actions (Live demo and Source code) missing"
        )

    # Check availability statement on index.html
    if (
        "lagos, nigeria" not in index_content.lower()
        or not any(term in index_content.lower() for term in ("junior", "internship", "available for"))
    ):
        errors.append("index.html: Required availability statement is missing or incomplete")

    # Check LinkedIn inert text (must not be an active link)
    if "linkedin — coming soon" not in index_content and "linkedin — coming soon" not in index_content.lower():
        errors.append(
            "index.html: Expected 'LinkedIn — coming soon' inert text for unreleased profile"
        )

    # Check CV download link and asset existence
    has_cv_link = any(
        "ayotomiwa-ojo-cv.pdf" in (href or "") for _, href, _, _, _, _ in index_parser.links
    )
    cv_asset = repo_root / "assets" / "documents" / "ayotomiwa-ojo-cv.pdf"
    if not has_cv_link:
        errors.append("index.html: Missing link to verified CV PDF")
    if not cv_asset.is_file():
        errors.append(f"Missing required CV document: {cv_asset.relative_to(repo_root)}")
    else:
        cv_bytes = cv_asset.read_bytes()
        if not cv_bytes.startswith(b"%PDF-"):
            errors.append("assets/documents/ayotomiwa-ojo-cv.pdf: File is not a valid PDF header")
        if b"https://ayotomiwa.pages.dev/" not in cv_bytes:
            errors.append("assets/documents/ayotomiwa-ojo-cv.pdf: Missing verified portfolio URL")
        if b"lordt0m.github.io" in cv_bytes.lower():
            errors.append("assets/documents/ayotomiwa-ojo-cv.pdf: Stale GitHub Pages URL")

    # Check Case Study links on index.html
    has_shelfsum_cs = any(
        "projects/shelfsum.html" in (href or "") for _, href, _, _, _, _ in index_parser.links
    )
    has_credence_cs = any(
        "projects/credence.html" in (href or "") for _, href, _, _, _, _ in index_parser.links
    )
    if not has_shelfsum_cs:
        errors.append("index.html: Missing link to ShelfSum case study (projects/shelfsum.html)")
    if not has_credence_cs:
        errors.append("index.html: Missing link to Credence case study (projects/credence.html)")

    # 2. Verify project-specific evidence
    shelfsum_page = repo_root / "projects" / "shelfsum.html"
    if shelfsum_page.is_file():
        ss_parser, ss_content = parsed_documents.get(shelfsum_page, (None, ""))
        ss_visible_text = re.sub(r"\s+", " ", " ".join(ss_parser.text_chunks)).strip()
        for credential in SHELFSUM_DEMO_CREDENTIALS:
            if credential not in index_content:
                errors.append(f"index.html: Missing exact ShelfSum demo credential '{credential}'")
            if credential not in ss_content:
                errors.append(
                    f"projects/shelfsum.html: Missing exact ShelfSum demo credential '{credential}'"
                )
        if "271 automated tests" not in index_content.lower():
            errors.append("index.html: Missing verified ShelfSum total of 271 automated tests")
        if "271 automated tests" not in ss_visible_text.lower():
            errors.append(
                "projects/shelfsum.html: Missing verified ShelfSum total of 271 automated tests"
            )

    credence_page = repo_root / "projects" / "credence.html"
    if credence_page.is_file():
        cr_parser, cr_content = parsed_documents.get(credence_page, (None, ""))
        cr_visible_text = re.sub(r"\s+", " ", " ".join(cr_parser.text_chunks)).strip()
        for value in CREDENCE_FIXTURE_VALUES:
            if value not in index_visible_text:
                errors.append(f"index.html: Missing verified Credence fixture value '{value}'")
            if value not in cr_visible_text:
                errors.append(
                    f"projects/credence.html: Missing verified Credence fixture value '{value}'"
                )
        if "credence-preview-title" not in index_parser.ids:
            errors.append("index.html: Missing semantic Credence preview")
        if cr_parser and "fixture-sample-title" not in cr_parser.ids:
            errors.append("projects/credence.html: Missing semantic fictional fixture sample")

    # 3. Verification-only CI; GitHub Pages publication is retired.
    deploy_workflow = repo_root / ".github" / "workflows" / "deploy.yml"
    if deploy_workflow.exists():
        errors.append("Retired GitHub Pages deployment workflow must not remain")
    verify_workflow = repo_root / ".github" / "workflows" / "verify.yml"
    if not verify_workflow.is_file():
        errors.append("Missing verification-only workflow (.github/workflows/verify.yml)")
    else:
        try:
            wf_content = verify_workflow.read_text(encoding="utf-8")
            for required in ("scripts/verify_site.py", "python -m unittest discover tests", "pull_request:"):
                if required not in wf_content:
                    errors.append(f"verify.yml: Missing required CI step or trigger '{required}'")
            for forbidden in ("deploy-pages", "upload-pages-artifact", "configure-pages", "pages: write", "id-token: write"):
                if forbidden in wf_content:
                    errors.append(f"verify.yml: Retired GitHub Pages deployment setting '{forbidden}' remains")
        except Exception as exc:
            errors.append(f"Failed to read verify.yml: {exc}")

    return errors


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    errors = verify(repo_root)

    if errors:
        print(f"FAILED: {len(errors)} structural verification issue(s):")
        for err in errors:
            print(f"  - {err}")
        return 1

    print("PASS: Site structural verification succeeded with zero errors.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
