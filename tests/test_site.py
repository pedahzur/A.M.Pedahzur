from html.parser import HTMLParser
import hashlib
from pathlib import Path
from urllib.parse import unquote, urlparse
import unittest


ROOT = Path(__file__).resolve().parents[1]


class LinkCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []
        self.ids: set[str] = set()

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(values["id"] or "")
        if tag not in {"a", "link", "script"}:
            return
        target = values.get("href") or values.get("src")
        if target:
            self.links.append(target)


class SiteContractTests(unittest.TestCase):
    def test_academic_blog_is_discoverable(self) -> None:
        homepage = (ROOT / "index.html").read_text(encoding="utf-8")
        blog_path = ROOT / "blog" / "index.html"
        sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")

        self.assertTrue(blog_path.is_file())
        blog = blog_path.read_text(encoding="utf-8")
        self.assertIn('href="blog/"', homepage)
        self.assertIn('id="academic-blog"', homepage)
        self.assertIn("Between Academic Rigor and Writing for a Wider Audience", homepage)
        self.assertIn(
            'href="academic-rigor-and-writing-for-a-wider-audience/"',
            blog,
        )
        self.assertIn(
            '<link rel="canonical" href="https://pedahzur.github.io/A.M.Pedahzur/blog/">',
            blog,
        )
        self.assertIn('href="blog.css"', blog)
        self.assertIn("https://pedahzur.github.io/A.M.Pedahzur/blog/", sitemap)

    def test_internal_links_resolve(self) -> None:
        broken: list[str] = []
        for page in ROOT.rglob("*.html"):
            collector = LinkCollector()
            collector.feed(page.read_text(encoding="utf-8"))
            for target in collector.links:
                parsed = urlparse(target)
                if parsed.scheme or target.startswith(("mailto:", "data:")):
                    continue
                if not parsed.path and parsed.fragment:
                    self.assertIn(
                        unquote(parsed.fragment),
                        collector.ids,
                        f"{page.relative_to(ROOT)} -> {target}",
                    )
                    continue
                path = unquote(parsed.path)
                candidate = (page.parent / path).resolve()
                if path.endswith("/"):
                    candidate = candidate / "index.html"
                if not candidate.exists():
                    broken.append(f"{page.relative_to(ROOT)} -> {target}")
                    continue
                if parsed.fragment and candidate.suffix in {".html", ".htm"}:
                    target_page = LinkCollector()
                    target_page.feed(candidate.read_text(encoding="utf-8"))
                    if unquote(parsed.fragment) not in target_page.ids:
                        broken.append(f"{page.relative_to(ROOT)} -> {target}")
        self.assertEqual([], broken, "\n".join(broken))

    def test_field_guide_publication_contract(self) -> None:
        landing = (ROOT / "field-guide" / "index.html").read_text(encoding="utf-8")
        homepage = (ROOT / "index.html").read_text(encoding="utf-8")

        self.assertIn("Working Edition 0.2", landing)
        self.assertIn("Read the current edition", landing)
        self.assertIn("Collection as Evidence", landing)
        self.assertIn(
            'href="https://pedahzur.github.io/A.M.Pedahzur/field-guide/"',
            landing,
        )
        self.assertIn('href="guide.css"', landing)
        self.assertNotIn('href="field-guide/"', homepage)
        self.assertNotIn("Explore the Field Guide", homepage)
        self.assertNotIn("AI-Assisted Research Methods", homepage)
        self.assertNotIn("Conceptualization: defining", homepage)
        self.assertNotIn("Historical Entity Tracker", homepage)

        sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
        self.assertIn(
            "https://pedahzur.github.io/A.M.Pedahzur/field-guide/",
            sitemap,
        )

        for name in (
            "From-Question-to-Evidence.pdf",
            "From-Question-to-Evidence.docx",
            "From-Question-to-Evidence.md",
        ):
            self.assertTrue((ROOT / "field-guide" / "book" / name).is_file())

        event_chapter = (
            ROOT
            / "field-guide"
            / "book"
            / "content"
            / "19-building-event-databases-with-ai.html"
        ).read_text(encoding="utf-8")
        self.assertIn("Building Event Databases with AI", landing)
        self.assertIn("candidate record", event_chapter)
        self.assertIn("Bayesian evidence table", event_chapter)

        historical_page = (
            ROOT
            / "field-guide"
            / "book"
            / "content"
            / "20-historical-sources-as-evidence.html"
        )
        self.assertTrue(historical_page.is_file())
        historical_text = historical_page.read_text(encoding="utf-8")
        self.assertIn("Historical Sources as Evidence", landing)
        self.assertIn("historical evidence chain", historical_text.lower())
        self.assertIn("source-stated", historical_text.lower())
        self.assertIn("downstream claim audit", historical_text.lower())
        self.assertIn("Eight numbered boxes", historical_text)
        self.assertTrue(
            (
                ROOT
                / "field-guide"
                / "book"
                / "templates"
                / "historical-evidence-chain-register.md"
            ).is_file()
        )

        review_chapter = (
            ROOT
            / "field-guide"
            / "book"
            / "content"
            / "19-review-articles-and-meta-analysis.html"
        ).read_text(encoding="utf-8")
        self.assertIn("Review Articles and Meta-Analysis in Transition", landing)
        self.assertIn("dependent effect estimates", review_chapter)
        self.assertIn("conditional future", review_chapter)
        self.assertIn("Literature-discovery skill", review_chapter)
        self.assertIn("project context packet", review_chapter)
        self.assertIn("least privilege", review_chapter)

        lab_page = (
            ROOT
            / "field-guide"
            / "book"
            / "content"
            / "skills-and-agents-lab.html"
        ).read_text(encoding="utf-8")
        self.assertIn("Skills and Agents Lab", landing)
        self.assertIn("literature-discovery skill", lab_page.lower())
        self.assertIn("Three Synthetic Benchmarks", lab_page)
        self.assertIn("What the AI Got Wrong", lab_page)

        lab_archive = (
            ROOT
            / "field-guide"
            / "book"
            / "downloads"
            / "skills-and-agents-lab-v0.1.0.zip"
        )
        lab_checksum = lab_archive.with_suffix(".zip.sha256")
        digest, filename = lab_checksum.read_text(
            encoding="utf-8"
        ).strip().split("  ", 1)
        self.assertEqual(lab_archive.name, filename)
        self.assertEqual(hashlib.sha256(lab_archive.read_bytes()).hexdigest(), digest)

        pkm_ai_page = (
            ROOT
            / "field-guide"
            / "book"
            / "content"
            / "20-pkm-and-ai-research-infrastructure.html"
        )
        self.assertTrue(pkm_ai_page.is_file())
        pkm_ai_text = pkm_ai_page.read_text(encoding="utf-8").lower()
        self.assertIn("from notes to research infrastructure", landing.lower())
        self.assertIn("pkm-ai research loop", pkm_ai_text)
        self.assertIn("what ai must not do", pkm_ai_text)

        voice_page = (
            ROOT
            / "field-guide"
            / "book"
            / "content"
            / "21-writing-by-voice-revising-by-ear.html"
        )
        self.assertTrue(voice_page.is_file())
        voice_text = voice_page.read_text(encoding="utf-8").lower()
        self.assertIn("writing by voice, revising by ear", landing.lower())
        self.assertIn("round-trip method", voice_text)
        self.assertIn("code-switched", voice_text)
        self.assertIn("permitted input", voice_text)
        self.assertTrue(
            (
                ROOT
                / "field-guide"
                / "book"
                / "templates"
                / "voice-round-trip-log.md"
            ).is_file()
        )

        book_home = (
            ROOT / "field-guide" / "book" / "index.html"
        ).read_text(encoding="utf-8")
        self.assertIn("Nearly a decade ago", book_home)
        self.assertIn("What we were missing was processing power", book_home)
        book_styles = "\n".join(
            stylesheet.read_text(encoding="utf-8")
            for stylesheet in (
                ROOT / "field-guide" / "book" / "site_libs" / "bootstrap"
            ).glob("bootstrap-*.min.css")
        )
        self.assertIn("NEARLY A DECADE IN THE MAKING", book_styles)

        module = (
            ROOT
            / "field-guide"
            / "book"
            / "content"
            / "02-evidence-map-overview.html"
        ).read_text(encoding="utf-8")
        self.assertIn("data-evidence-map-pilot", module)
        self.assertIn("Interactive visual companion", module)
        self.assertTrue(
            (
                ROOT
                / "field-guide"
                / "book"
                / "assets"
                / "evidence-map-pilot.js"
            ).is_file()
        )

    def test_field_guide_uses_restrained_editorial_design(self) -> None:
        landing = (ROOT / "field-guide" / "index.html").read_text(encoding="utf-8")
        styles = (ROOT / "field-guide" / "guide.css").read_text(encoding="utf-8")

        for landmark in (
            'class="publication-header"',
            'class="publication-masthead"',
            'class="edition-register"',
            'class="module-index"',
            'class="publication-footer"',
        ):
            self.assertIn(landmark, landing)

        for token in (
            "--page: #f4f4f0;",
            "--ink: #18222d;",
            "--accent: #245f86;",
            "--measure: 68ch;",
            "font-size: clamp(2.45rem, 4.5vw, 3.9rem);",
        ):
            self.assertIn(token, styles)

        self.assertNotIn("radial-gradient", styles)
        self.assertNotIn("border-radius: 999px", styles)
        self.assertNotIn('class="guide-hero"', landing)

    def test_homepage_uses_current_cv_and_minimal_hero(self) -> None:
        homepage = (ROOT / "index.html").read_text(encoding="utf-8")
        styles = (ROOT / "styles.css").read_text(encoding="utf-8")
        cv_name = "Ami_Pedahzur_CV_July_2026.pdf"

        self.assertTrue((ROOT / cv_name).is_file())
        self.assertEqual(3, homepage.count(cv_name))
        self.assertIn('class="hero-heading"', homepage)
        self.assertIn(
            "grid-template-columns: minmax(0, 1.5fr) minmax(280px, 1fr);",
            styles,
        )
        self.assertIn(
            "grid-template-columns: repeat(4, minmax(0, 1fr));",
            styles,
        )
        self.assertIn("This work has taken me", homepage)
        for retired_content in (
            "Chaikin Institute for Geostrategy",
            "Professor of Geostrategic Studies",
            "Researching terrorism, political extremism",
            "This work that has taken me",
            'class="hero-portrait"',
            "aleph-idle.webp",
        ):
            self.assertNotIn(retired_content, homepage)

    def test_retired_method_feature_and_book_are_not_public(self) -> None:
        homepage = (ROOT / "index.html").read_text(encoding="utf-8")
        scripts = (ROOT / "script.js").read_text(encoding="utf-8")
        sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")

        high_volume_title = (
            "Managing High-Volume Digital Sources in Political Research "
            "with Emerging Technologies"
        )
        self.assertNotIn(high_volume_title, homepage)
        self.assertIn(high_volume_title, scripts)

        self.assertNotIn("Root Causes of Suicide Terrorism", scripts)
        self.assertNotIn("book-root-causes.html", sitemap)
        self.assertFalse((ROOT / "book-root-causes.html").exists())

    def test_public_pages_contain_no_private_paths(self) -> None:
        for page in ROOT.rglob("*.html"):
            text = page.read_text(encoding="utf-8")
            self.assertNotIn("/Users/", text, str(page.relative_to(ROOT)))
            self.assertNotIn("Second-Brain", text, str(page.relative_to(ROOT)))


if __name__ == "__main__":
    unittest.main()
