#!/usr/bin/env python3
"""Structural verification for portfolio repository.

Checks semantic structure, links, assets, accessibility landmarks,
evidence-controlled URLs, required sections, and absence of placeholders.
"""

from html.parser import HTMLParser
from pathlib import Path
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

FORBIDDEN_TEXT_PATTERNS = [
    (re.compile(r"\bTODO\b", re.IGNORECASE), "TODO placeholder"),
    (re.compile(r"\bFIXME\b", re.IGNORECASE), "FIXME placeholder"),
    (re.compile(r"\blorem\s+ipsum\b", re.IGNORECASE), "Lorem ipsum placeholder text"),
]

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
        self.h1_count = 0
        self.headings = []  # (level, line_num)
        self.ids = set()
        self.main_id = None
        self.links = []  # (tag, href, text, is_nav, line_num)
        self.assets = []  # (tag, attr, val, line_num)
        self.images = []  # (attrs, line_num)
        self.in_nav = False
        self.current_a = None
        self.text_chunks = []

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        line_num = self.getpos()[0]

        if "id" in attr_dict:
            self.ids.add(attr_dict["id"])

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
            }

        if tag == "link":
            href = attr_dict.get("href")
            rel = attr_dict.get("rel", "")
            if href:
                self.assets.append(("link", "href", href, rel, line_num))

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
                )
            )
            self.current_a = None

    def handle_data(self, data):
        if self.current_a is not None:
            self.current_a["text"].append(data)
        self.text_chunks.append(data)


def verify(repo_root: Path = Path(".")) -> list[str]:
    errors = []
    index_file = repo_root / "index.html"

    if not index_file.is_file():
        return [f"Missing required file: {index_file}"]

    try:
        content = index_file.read_text(encoding="utf-8")
    except Exception as exc:
        return [f"Failed to read {index_file}: {exc}"]

    # 1. Check for machine-specific paths in index.html
    for pattern, label in MACHINE_PATH_PATTERNS:
        matches = pattern.findall(content)
        if matches:
            errors.append(f"Forbidden {label} found: {matches[:3]}")

    # 2. Check for forbidden placeholders in index.html
    for pattern, label in FORBIDDEN_TEXT_PATTERNS:
        matches = pattern.findall(content)
        if matches:
            errors.append(f"Forbidden placeholder found: {label}")

    # Parse HTML
    parser = SiteHTMLParser()
    try:
        parser.feed(content)
    except Exception as exc:
        errors.append(f"HTML parsing error: {exc}")
        return errors

    full_text = " ".join(parser.text_chunks)

    # 3. Exactly one main landmark
    if parser.main_count != 1:
        errors.append(
            f"Expected exactly one <main> landmark, found {parser.main_count}"
        )
    elif parser.main_id != "main-content":
        errors.append(
            f"Expected <main> to have id='main-content', found id='{parser.main_id}'"
        )

    # 4. Exactly one level-one heading
    if parser.h1_count != 1:
        errors.append(f"Expected exactly one <h1> heading, found {parser.h1_count}")

    # 5. Heading hierarchy (no skipping levels)
    prev_level = 0
    for level, line in parser.headings:
        if prev_level > 0 and level > prev_level + 1:
            errors.append(
                f"Line {line}: Heading level skipped from h{prev_level} to h{level}"
            )
        prev_level = level

    # 6. Skip link to #main-content
    first_link = parser.links[0] if parser.links else None
    if not first_link or first_link[1] != "#main-content":
        errors.append(
            f"Expected first link to be skip link pointing to #main-content, found {first_link}"
        )

    # 7. Navigation links and required identifiers
    nav_links = [link for link in parser.links if link[3]]  # is_nav
    if not nav_links:
        errors.append("No navigation links found in <nav>")
    for _, href, text, _, line in nav_links:
        if not href or not href.startswith("#"):
            errors.append(
                f"Line {line}: Nav link '{text}' ({href}) must be an in-page fragment"
            )
        else:
            target_id = href[1:]
            if target_id not in parser.ids:
                errors.append(
                    f"Line {line}: Nav link target id '{target_id}' does not exist in document"
                )

    # 8. All links validation (empty links, local fragments, local files, external URLs)
    found_urls = set()
    for _, href, text, _, line in parser.links:
        if href is None or href == "" or href == "#":
            errors.append(f"Line {line}: Empty or bare hash link found with text '{text}'")
            continue

        if href.startswith("#"):
            target_id = href[1:]
            if target_id not in parser.ids:
                errors.append(
                    f"Line {line}: Fragment link target id '{target_id}' does not exist"
                )
        elif href.startswith(("http://", "https://", "mailto:")):
            found_urls.add(href)
            if href not in APPROVED_EXTERNAL_URLS:
                errors.append(
                    f"Line {line}: Unapproved external URL '{href}' not in docs/content.md"
                )
        else:
            # Local relative file/asset link
            clean_href = href.split("?")[0].split("#")[0]
            local_target = repo_root / clean_href
            if not local_target.exists():
                errors.append(
                    f"Line {line}: Local link target '{clean_href}' does not exist on disk"
                )

    # 9. Asset links (<link>, <script>)
    for tag, attr, val, rel, line in parser.assets:
        if val.startswith(("http://", "https://")):
            if val not in APPROVED_EXTERNAL_URLS:
                errors.append(f"Line {line}: Unapproved external asset '{val}'")
        else:
            clean_path = val.split("?")[0].split("#")[0]
            target_file = repo_root / clean_path
            if not target_file.exists():
                errors.append(
                    f"Line {line}: Local asset '{clean_path}' in <{tag} {attr}='{val}'> does not exist"
                )

    # 10. Images check
    for attrs, line in parser.images:
        if "alt" not in attrs:
            errors.append(f"Line {line}: <img> missing required 'alt' attribute")
        src = attrs.get("src", "")
        if "photo" in src.lower() or "avatar" in src.lower() or "headshot" in src.lower():
            errors.append(f"Line {line}: Forbidden photograph or photo placeholder found")
        # Visual assets remain withheld until respective gates pass
        errors.append(f"Line {line}: Visual assets (screenshots/images) are withheld until gates pass")

    # 11. Required URLs presence
    for approved_url in APPROVED_EXTERNAL_URLS:
        if approved_url not in found_urls:
            errors.append(f"Required approved external URL missing: {approved_url}")

    # 12. Withheld content checks
    if "ayotomiwa-ojo-cv.pdf" in content or "Download CV" in content:
        errors.append("Withheld content found: CV download must not be rendered until verified PDF exists")
    if "linkedin.com" in content.lower():
        errors.append("Withheld content found: LinkedIn must not be rendered until verified profile exists")
    if re.search(r"\bjournal\b", content, re.IGNORECASE):
        errors.append("Withheld content found: Private journal must not be rendered without inspectable evidence")

    # 13. Availability message presence
    if "Lagos, Nigeria" not in content or "Available for" not in content:
        errors.append("Required availability statement from docs/content.md is missing")

    # 14. Project inspection actions presence
    has_live_demo = any("Live Demo" in text for _, _, text, _, _ in parser.links)
    has_source_code = any("Source Code" in text for _, _, text, _, _ in parser.links)
    if not (has_live_demo and has_source_code):
        errors.append("Required project inspection actions (Live Demo and Source Code) missing")

    # 15. Required sections for the portfolio system
    required_ids = {"main-content", "projects", "skills", "about", "contact"}
    missing_ids = required_ids - parser.ids
    if missing_ids:
        errors.append(f"Required section IDs missing in document: {sorted(list(missing_ids))}")

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
