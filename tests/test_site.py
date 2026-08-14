from html.parser import HTMLParser
import hashlib
import json
from pathlib import Path
import re
import subprocess
from tempfile import TemporaryDirectory
from urllib.parse import unquote, urlparse
import unittest
from unittest.mock import patch

import scripts.build_hebrew_blog as build_hebrew_blog


ROOT = Path(__file__).resolve().parents[1]
ARTICLE_PATH = (
    ROOT
    / "blog"
    / "academic-rigor-and-writing-for-a-wider-audience"
    / "index.html"
)
NEWSPAPER_ARTICLE_PATH = (
    ROOT
    / "blog"
    / "from-one-report-to-two-histories"
    / "index.html"
)
def css_declarations(
    styles: str, selector: str, required_property: str | None = None
) -> dict[str, str]:
    """Return declarations for one exact selector outside or inside media rules."""
    matches: list[dict[str, str]] = []
    for selector_group, body in re.findall(r"([^{}@]+)\{([^{}]*)\}", styles):
        selectors = [" ".join(item.split()) for item in selector_group.split(",")]
        if selector not in selectors:
            continue
        declarations: dict[str, str] = {}
        for declaration in body.split(";"):
            if ":" not in declaration:
                continue
            name, value = declaration.split(":", 1)
            declarations[name.strip()] = " ".join(value.split())
        if required_property is None or required_property in declarations:
            matches.append(declarations)
    if len(matches) != 1:
        raise AssertionError(
            f"Expected one CSS rule for {selector!r}, found {len(matches)}"
        )
    return matches[0]


class MetadataCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.values: dict[str, list[str]] = {}
        self.json_ld: list[str] = []
        self._json_ld_parts: list[str] | None = None

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        values = dict(attrs)
        if tag == "meta":
            key = values.get("property") or values.get("name")
            content = values.get("content")
            if key and content is not None:
                self.values.setdefault(key, []).append(content)
        if tag == "script" and values.get("type") == "application/ld+json":
            self._json_ld_parts = []

    def handle_endtag(self, tag: str) -> None:
        if tag == "script" and self._json_ld_parts is not None:
            self.json_ld.append("".join(self._json_ld_parts))
            self._json_ld_parts = None

    def handle_data(self, data: str) -> None:
        if self._json_ld_parts is not None:
            self._json_ld_parts.append(data)


class ArticleProseCollector(HTMLParser):
    """Canonicalize approved scholarly content, not presentation markup.

    The boundary includes the article title and deck plus every h2, h3,
    paragraph, list item, table header/cell, and each of the 16 endnote bodies
    in source order. It excludes dates/read-time labels, desktop/mobile TOCs,
    note-call numbers, backlink glyphs, aria-hidden separators, navigation,
    wrappers, IDs, classes, links, and other presentation-only attributes.
    Whitespace runs are normalized so harmless formatting changes do not alter
    the digest; changing any source-visible scholarly text does.
    """

    def __init__(self) -> None:
        super().__init__()
        self.records: list[tuple[str, str]] = []
        self._article_depth = 0
        self._header_depth = 0
        self._body_depth = 0
        self._excluded_depth = 0
        self._current_kind: str | None = None
        self._current_tag: str | None = None
        self._parts: list[str] = []

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        values = dict(attrs)
        classes = set((values.get("class") or "").split())
        if tag == "article" and "essay" in classes:
            self._article_depth = 1
        elif self._article_depth:
            self._article_depth += 1
        if not self._article_depth:
            return

        if tag == "header" and "article-header" in classes:
            self._header_depth = 1
        elif self._header_depth:
            self._header_depth += 1
        if "essay-body" in classes:
            self._body_depth = 1
        elif self._body_depth:
            self._body_depth += 1

        presentation_only = (
            values.get("role") in {"doc-noteref", "doc-backlink"}
            or values.get("aria-hidden") == "true"
            or "footnote-back" in classes
        )
        if presentation_only or self._excluded_depth:
            self._excluded_depth += 1
            return
        if self._current_kind is not None:
            return

        kind: str | None = None
        if self._header_depth and (
            tag == "h1" or (tag == "p" and "article-deck" in classes)
        ):
            kind = tag
        elif self._body_depth:
            if tag == "li" and values.get("role") == "doc-endnote":
                kind = "note"
            elif tag in {"h2", "h3", "p", "li", "th", "td"}:
                kind = tag
        if kind is not None:
            self._current_kind = kind
            self._current_tag = tag
            self._parts = []

    def handle_endtag(self, tag: str) -> None:
        if self._excluded_depth:
            self._excluded_depth -= 1
        elif self._current_kind is not None and tag == self._current_tag:
            text = " ".join("".join(self._parts).split())
            self.records.append((self._current_kind, text))
            self._current_kind = None
            self._current_tag = None
            self._parts = []
        if self._body_depth:
            self._body_depth -= 1
        if self._header_depth:
            self._header_depth -= 1
        if self._article_depth:
            self._article_depth -= 1

    def handle_data(self, data: str) -> None:
        if self._current_kind is not None and not self._excluded_depth:
            self._parts.append(data)

    def digest(self) -> str:
        payload = "\n".join(
            f"{kind}\t{text}" for kind, text in self.records
        ).encode("utf-8")
        return hashlib.sha256(payload).hexdigest()


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


class TranslationRenderingCollector(HTMLParser):
    """Collect user-visible and accessible translation-status rendering."""

    def __init__(self) -> None:
        super().__init__()
        self.article_status: str | None = None
        self.notice_parts: list[str] = []
        self.hebrew_links: dict[str, tuple[str | None, str]] = {}
        self._notice_depth = 0
        self._link_href: str | None = None
        self._link_aria_label: str | None = None
        self._link_parts: list[str] = []

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        values = dict(attrs)
        classes = set((values.get("class") or "").split())
        if tag == "article" and values.get("data-translation-status"):
            self.article_status = values["data-translation-status"]
        if tag == "aside" and "translation-status" in classes:
            self._notice_depth = 1
        elif self._notice_depth:
            self._notice_depth += 1
        if tag == "a" and values.get("lang") == "he":
            self._link_href = values.get("href")
            self._link_aria_label = values.get("aria-label")
            self._link_parts = []

    def handle_endtag(self, tag: str) -> None:
        if tag == "a" and self._link_href is not None:
            self.hebrew_links[self._link_href] = (
                self._link_aria_label,
                " ".join("".join(self._link_parts).split()),
            )
            self._link_href = None
            self._link_aria_label = None
            self._link_parts = []
        if self._notice_depth:
            self._notice_depth -= 1

    def handle_data(self, data: str) -> None:
        if self._notice_depth:
            self.notice_parts.append(data)
        if self._link_href is not None:
            self._link_parts.append(data)

    @property
    def notice_text(self) -> str:
        return " ".join("".join(self.notice_parts).split())


class ArticleContractCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: list[str] = []
        self.subsection_titles: list[str] = []
        self.noterefs: list[tuple[str, str]] = []
        self.endnote_ids: set[str] = set()
        self.footnote_back_hrefs: list[str] = []
        self.tables: list[tuple[set[str], list[list[str]]]] = []
        self.table_wraps: list[dict[str, str | None]] = []
        self.table_header_scopes: list[str | None] = []
        self.heading_ids: dict[str, str] = {}
        self.unordered_lists: list[list[str]] = []
        self._heading_parts: list[str] | None = None
        self._heading_id: str | None = None
        self._unordered_list_stack: list[tuple[list[str], list[str] | None]] = []
        self._table_classes: set[str] | None = None
        self._table_rows: list[list[str]] = []
        self._table_row: list[str] | None = None
        self._table_cell_parts: list[str] | None = None

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        values = dict(attrs)
        element_id = values.get("id")
        if element_id is not None:
            self.ids.append(element_id)
        classes = set((values.get("class") or "").split())
        if tag == "h3":
            self._heading_parts = []
            self._heading_id = element_id
        if tag == "div" and "article-table-wrap" in classes:
            self.table_wraps.append(values)
        if tag == "th" and self._table_row is not None:
            self.table_header_scopes.append(values.get("scope"))
        if tag == "table":
            self._table_classes = classes
            self._table_rows = []
        if tag == "tr" and self._table_classes is not None:
            self._table_row = []
        if tag in {"th", "td"} and self._table_row is not None:
            self._table_cell_parts = []
        if tag == "ul":
            self._unordered_list_stack.append(([], None))
        if tag == "li" and self._unordered_list_stack:
            items, _ = self._unordered_list_stack[-1]
            self._unordered_list_stack[-1] = (items, [])
        if values.get("role") == "doc-endnote" and element_id:
            self.endnote_ids.add(element_id)
        if tag != "a":
            return
        href = values.get("href")
        if values.get("role") == "doc-noteref":
            self.noterefs.append((element_id or "", href or ""))
        if "footnote-back" in classes and href:
            self.footnote_back_hrefs.append(href)

    def handle_endtag(self, tag: str) -> None:
        if tag == "h3" and self._heading_parts is not None:
            title = "".join(self._heading_parts).strip()
            self.subsection_titles.append(title)
            if self._heading_id:
                self.heading_ids[title] = self._heading_id
            self._heading_parts = None
            self._heading_id = None
        if tag in {"th", "td"} and self._table_cell_parts is not None:
            self._table_row.append("".join(self._table_cell_parts).strip())
            self._table_cell_parts = None
        if tag == "tr" and self._table_row is not None:
            self._table_rows.append(self._table_row)
            self._table_row = None
        if tag == "table" and self._table_classes is not None:
            self.tables.append((self._table_classes, self._table_rows))
            self._table_classes = None
            self._table_rows = []
        if tag == "li" and self._unordered_list_stack:
            items, item_parts = self._unordered_list_stack[-1]
            if item_parts is not None:
                items.append("".join(item_parts).strip())
                self._unordered_list_stack[-1] = (items, None)
        if tag == "ul" and self._unordered_list_stack:
            items, _ = self._unordered_list_stack.pop()
            self.unordered_lists.append(items)

    def handle_data(self, data: str) -> None:
        if self._heading_parts is not None:
            self._heading_parts.append(data)
        if self._table_cell_parts is not None:
            self._table_cell_parts.append(data)
        if self._unordered_list_stack:
            items, item_parts = self._unordered_list_stack[-1]
            if item_parts is not None:
                item_parts.append(data)
                self._unordered_list_stack[-1] = (items, item_parts)


class TranslationStatusBuildTests(unittest.TestCase):
    SLUGS = tuple(build_hebrew_blog.POSTS)
    TARGET_SLUG = "academic-rigor-and-writing-for-a-wider-audience"

    @staticmethod
    def _write_source(
        blog: Path, slug: str, metadata: str, body: str = "Body"
    ) -> None:
        source = blog / "sources" / "he" / f"{slug}.md"
        source.parent.mkdir(parents=True, exist_ok=True)
        source.write_text(
            f"---\ntitle: probe\n{metadata}---\n\n{body}\n",
            encoding="utf-8",
        )

    def _write_index_fixtures(self, root: Path) -> None:
        blog_links = "\n".join(
            f'<a class="hebrew-edition-link" href="{slug}/he/" '
            'hreflang="he" lang="he" aria-label="stale">stale</a>'
            for slug in self.SLUGS
        )
        homepage_links = "\n".join(
            f'<a class="btn btn-outline" href="blog/{slug}/he/" '
            'hreflang="he" lang="he" aria-label="stale">stale</a>'
            for slug in self.SLUGS
        )
        (root / "blog").mkdir(parents=True, exist_ok=True)
        (root / "blog" / "index.html").write_text(
            f"<main>{blog_links}</main>\n", encoding="utf-8"
        )
        (root / "index.html").write_text(
            f"<main>{homepage_links}</main>\n", encoding="utf-8"
        )

    def test_translation_status_accepts_only_one_supported_frontmatter_value(
        self,
    ) -> None:
        for status in ("draft", "editor-reviewed", "author-approved"):
            with self.subTest(status=status), TemporaryDirectory() as directory:
                blog = Path(directory) / "blog"
                self._write_source(
                    blog,
                    self.TARGET_SLUG,
                    f"translation_status: {status}\n",
                )
                with patch.object(build_hebrew_blog, "BLOG", blog):
                    self.assertEqual(
                        status,
                        build_hebrew_blog.read_translation_status(self.TARGET_SLUG),
                    )

    def test_translation_status_rejects_invalid_frontmatter_states(self) -> None:
        cases = (
            ("missing", "", "Body", "Missing translation_status"),
            (
                "duplicate",
                "translation_status: draft\ntranslation_status: author-approved\n",
                "Body",
                "Duplicate translation_status",
            ),
            (
                "unsupported",
                "translation_status: machine-approved\n",
                "Body",
                "Unsupported translation_status 'machine-approved'",
            ),
            (
                "body-only",
                "",
                "translation_status: draft",
                "Missing translation_status",
            ),
        )
        for name, metadata, body, message in cases:
            with self.subTest(case=name), TemporaryDirectory() as directory:
                blog = Path(directory) / "blog"
                self._write_source(blog, self.TARGET_SLUG, metadata, body)
                with patch.object(build_hebrew_blog, "BLOG", blog):
                    with self.assertRaisesRegex(RuntimeError, message):
                        build_hebrew_blog.read_translation_status(self.TARGET_SLUG)

    def test_each_status_drives_article_notice_and_both_index_labels(self) -> None:
        cases = (
            (
                "draft",
                True,
                "עברית (טיוטה בעריכה)",
                "עברית, טיוטה בעריכה",
            ),
            (
                "editor-reviewed",
                True,
                "עברית (טיוטה בעריכה)",
                "עברית, טיוטה בעריכה",
            ),
            ("author-approved", False, "עברית", "עברית"),
        )
        for status, notice_expected, visible_label, aria_label in cases:
            with self.subTest(status=status), TemporaryDirectory() as directory:
                root = Path(directory)
                blog = root / "blog"
                self._write_index_fixtures(root)
                for slug in self.SLUGS:
                    source_status = status if slug == self.TARGET_SLUG else "draft"
                    self._write_source(
                        blog,
                        slug,
                        f"translation_status: {source_status}\n",
                    )

                rendered = {slug: "<p>Rendered body</p>" for slug in self.SLUGS}
                with (
                    patch.object(build_hebrew_blog, "ROOT", root),
                    patch.object(build_hebrew_blog, "BLOG", blog),
                ):
                    build_hebrew_blog.write_site(rendered)

                article_collector = TranslationRenderingCollector()
                article_collector.feed(
                    (
                        blog / self.TARGET_SLUG / "he" / "index.html"
                    ).read_text(encoding="utf-8")
                )
                self.assertEqual(status, article_collector.article_status)
                self.assertEqual(
                    notice_expected,
                    "טיוטת תרגום בעריכה" in article_collector.notice_text,
                )

                expected_links = (
                    (blog / "index.html", f"{self.TARGET_SLUG}/he/"),
                    (root / "index.html", f"blog/{self.TARGET_SLUG}/he/"),
                )
                for index_path, href in expected_links:
                    with self.subTest(status=status, index=index_path.name):
                        index_collector = TranslationRenderingCollector()
                        index_collector.feed(index_path.read_text(encoding="utf-8"))
                        self.assertEqual(
                            (aria_label, visible_label),
                            index_collector.hebrew_links[href],
                        )


class SiteContractTests(unittest.TestCase):
    def test_hebrew_translation_status_is_visible_and_enforced(self) -> None:
        sources = tuple(sorted((ROOT / "blog" / "sources" / "he").glob("*.md")))
        self.assertGreaterEqual(len(sources), 2)
        index_collectors = {}
        for index_path in (ROOT / "blog" / "index.html", ROOT / "index.html"):
            collector = TranslationRenderingCollector()
            collector.feed(index_path.read_text(encoding="utf-8"))
            index_collectors[index_path] = collector

        for source in sources:
            slug = source.stem
            status = build_hebrew_blog.read_translation_status(slug)
            article_collector = TranslationRenderingCollector()
            article_collector.feed(
                (ROOT / "blog" / slug / "he" / "index.html").read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual(status, article_collector.article_status)
            draft_expected = status != "author-approved"
            self.assertEqual(
                draft_expected,
                "טיוטת תרגום בעריכה" in article_collector.notice_text,
            )
            expected_label = (
                ("עברית, טיוטה בעריכה", "עברית (טיוטה בעריכה)")
                if draft_expected
                else ("עברית", "עברית")
            )
            expected_links = (
                (ROOT / "blog" / "index.html", f"{slug}/he/"),
                (ROOT / "index.html", f"blog/{slug}/he/"),
            )
            for index_path, href in expected_links:
                with self.subTest(post=slug, index=index_path.name):
                    self.assertEqual(
                        expected_label,
                        index_collectors[index_path].hebrew_links[href],
                    )

    def test_every_blog_post_has_a_complete_linked_hebrew_edition(self) -> None:
        blog = (ROOT / "blog" / "index.html").read_text(encoding="utf-8")
        homepage = (ROOT / "index.html").read_text(encoding="utf-8")
        sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
        english_posts = tuple(sorted((ROOT / "blog").glob("*/index.html")))
        pairs = tuple(
            (english_path, english_path.parent / "he" / "index.html")
            for english_path in english_posts
        )
        self.assertGreaterEqual(len(pairs), 2)

        for english_path, hebrew_path in pairs:
            with self.subTest(post=english_path.parent.name):
                self.assertTrue(hebrew_path.is_file())
                english = english_path.read_text(encoding="utf-8")
                hebrew = hebrew_path.read_text(encoding="utf-8")
                english_url = (
                    "https://pedahzur.github.io/A.M.Pedahzur/"
                    + english_path.relative_to(ROOT).parent.as_posix()
                    + "/"
                )
                hebrew_url = english_url + "he/"

                self.assertIn('<html lang="he" dir="rtl">', hebrew)
                self.assertIn(
                    f'<link rel="alternate" hreflang="he" href="{hebrew_url}">',
                    english,
                )
                self.assertIn(
                    f'<link rel="alternate" hreflang="en" href="{english_url}">',
                    hebrew,
                )
                self.assertIn(
                    f'<link rel="canonical" href="{hebrew_url}">',
                    hebrew,
                )
                self.assertIn('class="language-switch"', english)
                self.assertIn('class="language-switch"', hebrew)
                self.assertIn('hreflang="he" lang="he"', english)
                self.assertIn('hreflang="en" lang="en"', hebrew)
                self.assertEqual(
                    english.count('role="doc-noteref"'),
                    hebrew.count('role="doc-noteref"'),
                )
                self.assertEqual(
                    english.count('role="doc-endnote"'),
                    hebrew.count('role="doc-endnote"'),
                )
                self.assertEqual(english.count("<h2"), hebrew.count("<h2"))
                self.assertEqual(english.count("<h3"), hebrew.count("<h3"))
                self.assertEqual(
                    english.count('class="article-table"'),
                    hebrew.count('class="article-table"'),
                )
                self.assertEqual(
                    english.count('class="evidence-flow"'),
                    hebrew.count('class="evidence-flow"'),
                )
                self.assertIn(hebrew_url, sitemap)
                self.assertIn(
                    'href="'
                    + hebrew_path.relative_to(ROOT).parent.as_posix()
                    + '/"',
                    homepage,
                )

        self.assertEqual(
            len(pairs), blog.count('class="hebrew-edition-link"')
        )

    def test_academic_blog_uses_accessible_editorial_design(self) -> None:
        styles = (ROOT / "blog" / "blog.css").read_text(encoding="utf-8")
        post = ARTICLE_PATH.read_text(encoding="utf-8")

        for token in (
            "--reading-measure: 68ch;",
            "position: sticky;",
            "line-height: 1.78;",
            "overflow-x: auto;",
            "@media (prefers-reduced-motion: reduce)",
            ":focus-visible",
        ):
            self.assertIn(token, styles)
        self.assertIn('href="#main-content"', post)
        self.assertIn('id="main-content"', post)
        self.assertIn(
            ".footnote-ref { color: var(--accent);",
            styles,
        )
        self.assertIn(
            '<h2 id="notes-and-sources">Notes and Sources</h2>',
            post,
        )
        self.assertNotIn(
            '<section id="notes-and-sources" class="level2">',
            post,
        )
        self.assertIn(
            'role="doc-endnotes" aria-labelledby="notes-and-sources"',
            post,
        )

    def test_academic_blog_measure_uses_literata_grid_context(self) -> None:
        styles = (ROOT / "blog" / "blog.css").read_text(encoding="utf-8")
        root_rule = css_declarations(styles, ":root")
        layout_rule = css_declarations(
            styles, ".article-layout", required_property="font-family"
        )
        body_rule = css_declarations(
            styles, ".essay-body", required_property="font-family"
        )
        desktop_toc_rule = css_declarations(
            styles, ".article-toc", required_property="font-family"
        )
        mobile_toc_rule = css_declarations(
            styles, ".mobile-toc", required_property="font-family"
        )

        self.assertEqual("68ch", root_rule["--reading-measure"])
        self.assertEqual(
            "clamp(1.05rem, .45vw + .95rem, 1.22rem)",
            root_rule["--article-font-size"],
        )
        self.assertEqual("var(--font-serif)", layout_rule["font-family"])
        self.assertEqual("var(--article-font-size)", layout_rule["font-size"])
        self.assertEqual(
            "var(--reading-measure) minmax(13rem, 17rem)",
            layout_rule["grid-template-columns"],
        )
        self.assertEqual("inherit", body_rule["font-family"])
        self.assertEqual("inherit", body_rule["font-size"])
        self.assertEqual("var(--font-sans)", desktop_toc_rule["font-family"])
        self.assertEqual("var(--font-sans)", mobile_toc_rule["font-family"])
        self.assertIn("@media (min-width: 1100px)", styles)
        self.assertIn("@media (max-width: 1099px)", styles)

        for page in (ROOT / "blog" / "index.html", ARTICLE_PATH):
            html = page.read_text(encoding="utf-8")
            self.assertIn("family=Literata:wght@400;500;600;700", html)

    def test_academic_blog_table_region_is_keyboard_accessible(self) -> None:
        collector = ArticleContractCollector()
        collector.feed(ARTICLE_PATH.read_text(encoding="utf-8"))

        self.assertEqual("a-diagnostic-tool-heading", collector.heading_ids.get(
            "A Diagnostic Tool"
        ))
        self.assertEqual(1, len(collector.table_wraps))
        table_wrap = collector.table_wraps[0]
        self.assertEqual("0", table_wrap.get("tabindex"))
        self.assertEqual("region", table_wrap.get("role"))
        self.assertEqual(
            "a-diagnostic-tool-heading", table_wrap.get("aria-labelledby")
        )
        self.assertEqual(["col"] * 5, collector.table_header_scopes)

        focus_rule = css_declarations(
            (ROOT / "blog" / "blog.css").read_text(encoding="utf-8"),
            ".article-table-wrap:focus-visible",
        )
        self.assertEqual("3px solid var(--accent-warm)", focus_rule["outline"])
        self.assertEqual("4px", focus_rule["outline-offset"])

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
        self.assertIn(
            "<loc>https://pedahzur.github.io/A.M.Pedahzur/</loc>\n"
            "    <lastmod>2026-08-14</lastmod>",
            sitemap,
        )

    def test_newspaper_agent_post_is_discoverable(self) -> None:
        homepage = (ROOT / "index.html").read_text(encoding="utf-8")
        blog = (ROOT / "blog" / "index.html").read_text(encoding="utf-8")
        sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
        title = "From One Report to Two Histories"
        slug = "from-one-report-to-two-histories/"

        self.assertTrue(NEWSPAPER_ARTICLE_PATH.is_file())
        self.assertIn(title, homepage)
        self.assertIn(title, blog)
        self.assertIn(f'href="{slug}"', blog)
        self.assertIn(
            "https://pedahzur.github.io/A.M.Pedahzur/blog/" + slug,
            sitemap,
        )

    def test_academic_blog_discovery_metadata_is_complete(self) -> None:
        blog_collector = MetadataCollector()
        blog_collector.feed((ROOT / "blog" / "index.html").read_text(
            encoding="utf-8"
        ))
        expected_blog_metadata = {
            "og:type": "website",
            "og:site_name": "Ami Pedahzur",
            "og:title": "Writing Research for Readers | Ami Pedahzur",
            "og:description": (
                "Essays on research, evidence, and academic craft by Ami Pedahzur."
            ),
            "og:url": "https://pedahzur.github.io/A.M.Pedahzur/blog/",
            "twitter:card": "summary",
            "twitter:title": "Writing Research for Readers | Ami Pedahzur",
            "twitter:description": (
                "Essays on research, evidence, and academic craft by Ami Pedahzur."
            ),
        }
        for key, value in expected_blog_metadata.items():
            self.assertEqual([value], blog_collector.values.get(key), key)

        article_collector = MetadataCollector()
        article_collector.feed(ARTICLE_PATH.read_text(encoding="utf-8"))
        self.assertEqual(1, len(article_collector.json_ld))
        article_data = json.loads(article_collector.json_ld[0])
        self.assertEqual(
            "An academic book should meet two full demands: persuasive research "
            "and writing that leads readers through it with clarity, momentum, "
            "and respect.",
            article_data.get("description"),
        )
        self.assertEqual(
            "academic books, academic writing, research methods, public scholarship",
            article_data.get("keywords"),
        )

        newspaper_collector = MetadataCollector()
        newspaper_collector.feed(
            NEWSPAPER_ARTICLE_PATH.read_text(encoding="utf-8")
        )
        self.assertEqual(1, len(newspaper_collector.json_ld))
        newspaper_data = json.loads(newspaper_collector.json_ld[0])
        self.assertEqual(
            "From One Report to Two Histories: Building an Agent for Historical Newspaper Research",
            newspaper_data.get("headline"),
        )
        self.assertEqual("2026-08-13", newspaper_data.get("datePublished"))
        self.assertEqual(
            "historical newspapers, digital history, AI-assisted research, source criticism, multilingual archives",
            newspaper_data.get("keywords"),
        )

    def test_academic_blog_navigation_has_visible_home_links(self) -> None:
        blog = (ROOT / "blog" / "index.html").read_text(encoding="utf-8")
        article = ARTICLE_PATH.read_text(encoding="utf-8")

        self.assertIn('<a href="../">Home</a>', blog)
        self.assertIn('<a href="./" aria-current="page">Blog</a>', blog)
        self.assertIn('<a href="../../">Home</a>', article)
        self.assertIn('<a href="../" aria-current="location">Blog</a>', article)

    def test_primary_navigation_links_to_blog_on_all_root_pages(self) -> None:
        root_pages = [ROOT / "index.html", *sorted(ROOT.glob("book-*.html"))]

        for page in root_pages:
            with self.subTest(page=page.name):
                html = page.read_text(encoding="utf-8")
                self.assertIn('<a href="blog/">Blog</a>', html)

    def test_academic_blog_post_preserves_article_contract(self) -> None:
        post_path = (
            ROOT
            / "blog"
            / "academic-rigor-and-writing-for-a-wider-audience"
            / "index.html"
        )
        self.assertTrue(post_path.is_file())
        post = post_path.read_text(encoding="utf-8")

        self.assertIn('"@type": "ScholarlyArticle"', post)
        self.assertIn(
            '<link rel="canonical" href="https://pedahzur.github.io/A.M.Pedahzur/blog/academic-rigor-and-writing-for-a-wider-audience/">',
            post,
        )
        self.assertIn('href="../blog.css"', post)
        self.assertIn('class="essay"', post)
        self.assertIn('class="article-toc"', post)
        self.assertIn('class="mobile-toc"', post)
        self.assertIn('class="article-table"', post)
        self.assertEqual(7, post.count('class="numbered-section"'))
        self.assertEqual(20, post.count('role="doc-noteref"'))
        self.assertEqual(16, post.count('role="doc-endnote"'))
        self.assertEqual(20, post.count('class="footnote-back"'))
        self.assertIn(
            "It makes credibility interesting and interest worthy of trust.",
            post,
        )

    def test_newspaper_agent_post_preserves_article_contract(self) -> None:
        post = NEWSPAPER_ARTICLE_PATH.read_text(encoding="utf-8")

        self.assertIn('"@type": "ScholarlyArticle"', post)
        self.assertIn(
            '<link rel="canonical" href="https://pedahzur.github.io/A.M.Pedahzur/blog/from-one-report-to-two-histories/">',
            post,
        )
        self.assertIn('href="../blog.css"', post)
        self.assertIn('class="essay"', post)
        self.assertIn('class="article-toc"', post)
        self.assertIn('class="mobile-toc"', post)
        self.assertIn('class="article-table"', post)
        self.assertIn('class="evidence-flow"', post)
        self.assertEqual(5, post.count('class="numbered-section"'))
        self.assertEqual(9, post.count('role="doc-noteref"'))
        self.assertEqual(9, post.count('role="doc-endnote"'))
        self.assertEqual(9, post.count('class="footnote-back"'))
        self.assertIn(
            "It made the path to the answer visible, open to inspection, and open to correction.",
            post,
        )
        self.assertNotIn("<img", post)
        self.assertNotIn(".pdf", post.lower())

        collector = LinkCollector()
        collector.feed(post)
        self.assertEqual(len(collector.ids), len(set(collector.ids)))

        contract = ArticleContractCollector()
        contract.feed(post)
        self.assertEqual(["col"] * 5, contract.table_header_scopes)
        self.assertEqual(1, len(contract.table_wraps))
        self.assertEqual("0", contract.table_wraps[0].get("tabindex"))
        self.assertEqual("region", contract.table_wraps[0].get("role"))

    def test_academic_blog_post_preserves_source_structure_and_note_graph(self) -> None:
        collector = ArticleContractCollector()
        collector.feed(ARTICLE_PATH.read_text(encoding="utf-8"))

        self.assertEqual(
            [
                "The Claim and the Promise",
                "The Three Maps",
                "From a Table of Contents to Chapter Cards",
                "Writing That Continues the Research",
                "Opening the Chapter and Writing the Introduction",
                "Revision, Removal, and Test Readers",
                "When the Desire to Engage Harms the Research",
                "When the Desire for Protection Harms the Book",
                "The Promise a Book Cannot Make",
                "A Diagnostic Tool",
                "A Portable Idea That Connects Worlds: Seeing Like a State",
                "A Layered Journey of Proof: Making Democracy Work",
                "From General Pattern to Mechanism: Why Civil Resistance Works",
                "Academic Expertise in a Public-Facing Book: How Democracies Die",
                "What the Four Books Teach",
            ],
            collector.subsection_titles,
        )
        self.assertEqual(len(collector.ids), len(set(collector.ids)))
        self.assertTrue(all(collector.ids))

        call_ids = [call_id for call_id, _ in collector.noterefs]
        self.assertEqual(20, len(call_ids))
        self.assertEqual(20, len(set(call_ids)))
        self.assertEqual(16, len(collector.endnote_ids))
        endnote_targets = {href.removeprefix("#") for _, href in collector.noterefs}
        for call_id, href in collector.noterefs:
            self.assertTrue(call_id)
            self.assertTrue(href.startswith("#"))
            self.assertIn(href.removeprefix("#"), collector.endnote_ids)
        self.assertEqual(collector.endnote_ids, endnote_targets)

        for href in collector.footnote_back_hrefs:
            self.assertTrue(href.startswith("#"))
        backlink_targets = [href.removeprefix("#") for href in collector.footnote_back_hrefs]
        self.assertEqual(20, len(backlink_targets))
        self.assertEqual(20, len(set(backlink_targets)))
        self.assertEqual(set(call_ids), set(backlink_targets))

        diagnostic_table_rows = [
                    [
                        "Danger",
                        "Temptation",
                        "Scholarly cost",
                        "Reader’s experience",
                        "Repair",
                    ],
                    [
                        "Sensationalism",
                        "Magnify the book’s importance",
                        "Claim exceeds the evidence",
                        "The promise goes unfulfilled",
                        "Calibrate title and opening to the actual contribution",
                    ],
                ]
        self.assertTrue(
            any(
                "article-table" in classes and rows[:2] == diagnostic_table_rows
                for classes, rows in collector.tables
            )
        )
        self.assertIn(
            [
                "Role in the whole: why the book needs this chapter.",
                "Work of the chapter: the claim, theme, comparison, or process it develops.",
                "Central evidence: the materials that support that work.",
                "Entry point: what the reader already knows and still seeks to understand.",
                "Exit point: what has changed in the reader’s understanding and what draws the reader into the next chapter.",
            ],
            collector.unordered_lists,
        )

    def test_academic_blog_preserves_all_source_visible_scholarly_content(self) -> None:
        collector = ArticleProseCollector()
        collector.feed(ARTICLE_PATH.read_text(encoding="utf-8"))

        note_bodies = [text for kind, text in collector.records if kind == "note"]
        self.assertEqual(194, len(collector.records))
        self.assertEqual(16, len(note_bodies))
        self.assertEqual(16, len(set(note_bodies)))
        self.assertEqual(
            "e6976fe8ae6f2a754ef6d04780602d3e840369d260ff68261f72c57afe4400e9",
            collector.digest(),
        )

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

    def test_tracked_public_text_contains_no_private_paths(self) -> None:
        result = subprocess.run(
            [
                "git",
                "ls-files",
                "-z",
                "--",
                "*.html",
                "*.css",
                "*.xml",
                "*.md",
            ],
            cwd=ROOT,
            check=True,
            capture_output=True,
        )
        tracked_paths = [
            ROOT / path
            for path in result.stdout.decode("utf-8").split("\0")
            if path
        ]
        self.assertTrue(tracked_paths)
        forbidden_markers = (
            "/Users/",
            "file" + "://",
            "/Users/" + "amipedahzur" + "/",
        )
        for page in tracked_paths:
            text = page.read_text(encoding="utf-8")
            for marker in forbidden_markers:
                self.assertNotIn(marker, text, str(page.relative_to(ROOT)))


if __name__ == "__main__":
    unittest.main()
