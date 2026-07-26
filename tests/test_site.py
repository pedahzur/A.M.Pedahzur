from html.parser import HTMLParser
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
        self.assertIn('href="field-guide/"', homepage)
        self.assertIn("Explore the Field Guide", homepage)

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

    def test_public_pages_contain_no_private_paths(self) -> None:
        for page in ROOT.rglob("*.html"):
            text = page.read_text(encoding="utf-8")
            self.assertNotIn("/Users/", text, str(page.relative_to(ROOT)))
            self.assertNotIn("Second-Brain", text, str(page.relative_to(ROOT)))


if __name__ == "__main__":
    unittest.main()
