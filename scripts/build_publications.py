#!/usr/bin/env python3
"""Pre-render the homepage book and article lists from data/publications.json.

The lists used to be generated in the browser, so crawlers, AI agents and
readers without JavaScript saw empty sections. This script writes the same
markup into index.html between build markers and embeds the data that
script.js needs for filters and citations.

Usage:
    python3 scripts/build_publications.py          # rewrite index.html
    python3 scripts/build_publications.py --check  # exit 1 if index.html is stale
"""

from __future__ import annotations

import argparse
from html import escape
import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "publications.json"
INDEX = ROOT / "index.html"

DEFAULT_PUBLICATION_LIMIT = 5
TYPE_LABELS = {"journal": "Journal Article", "methods": "Methods", "chapter": "Book Chapter"}


def esc(value: object) -> str:
    """Escape a value for an HTML attribute."""
    return escape(str(value), quote=True)


def txt(value: object) -> str:
    """Escape a value for HTML text content (apostrophes stay readable)."""
    return escape(str(value), quote=False)


def external_links(links: list[dict]) -> str:
    return "".join(
        f'<a class="cite-btn" href="{esc(link["url"])}" target="_blank" rel="noopener">'
        f'{txt(link["label"])}</a>'
        for link in links
    )


def render_books(books: list[dict]) -> str:
    cards = []
    for index, book in enumerate(books):
        if book.get("cover"):
            cover = (
                f'<img class="book-cover" src="{esc(book["cover"])}" alt="{esc(book["coverAlt"])}" '
                'width="180" height="270" loading="lazy">'
            )
        else:
            cover = (
                f'<div class="book-cover book-cover-placeholder" role="img" '
                f'aria-label="{esc(book["coverAlt"])}"><span>{txt(book["title"])}</span></div>'
            )
        cards.append(
            f"""      <div class="book-card">
        {cover}
        <div class="book-card-body">
          <h3>{txt(book["title"])}</h3>
          <p class="book-meta">{txt(book["authors"])} &middot; {txt(book["publisher"])}, {txt(book["year"])}</p>
          <p>{txt(book["description"])}</p>
          <div class="cite-buttons">
            <a class="cite-btn" href="{esc(book["page"])}">Read More</a>
            <button class="cite-btn" type="button" data-cite-kind="book" data-cite-index="{index}">Cite</button>
            {external_links(book["links"])}
          </div>
        </div>
      </div>"""
        )
    return "\n".join(cards)


def render_articles(publications: list[dict]) -> str:
    items = []
    for index, pub in enumerate(publications):
        featured = pub.get("featured", False)
        badge = pub.get("label") or TYPE_LABELS.get(pub["type"], pub["type"])
        eyebrow = '\n        <p class="pub-eyebrow">Featured Work</p>' if featured else ""
        summary = (
            f'\n        <p class="pub-summary">{txt(pub["summary"])}</p>' if pub.get("summary") else ""
        )
        items.append(
            f"""      <article class="pub-item{' pub-item-featured' if featured else ''}" data-type="{esc(pub["type"])}" data-topics="{esc(" ".join(pub.get("topics", [])))}">{eyebrow}
        <h3>{txt(pub["title"])}</h3>
        <p class="pub-meta">{txt(pub["authors"])} &middot; {txt(pub["venue"])}</p>
        <div class="pub-badges">
          <span class="pub-badge">{txt(badge)}</span>
          <span class="pub-badge">{txt(pub["year"])}</span>
        </div>{summary}
        <div class="cite-buttons">
          <button class="cite-btn" type="button" data-cite-kind="article" data-cite-index="{index}">Cite</button>
          {external_links(pub["links"])}
        </div>
      </article>"""
        )
    visible, more = items[:DEFAULT_PUBLICATION_LIMIT], items[DEFAULT_PUBLICATION_LIMIT:]
    if not more:
        return "\n".join(visible)
    # Entries past the default limit stay in the DOM: crawlers and agents read
    # them, and Find in page or a text-fragment link reveals them. The wrapper
    # carries hidden="until-found" so the styled cards leave no empty boxes.
    return (
        "\n".join(visible)
        + '\n      <div class="pub-more" id="more-publications" hidden="until-found">\n'
        + "\n".join(more)
        + "\n      </div>"
    )


def render_count(publications: list[dict]) -> str:
    shown = min(len(publications), DEFAULT_PUBLICATION_LIMIT)
    return f"{shown} of {len(publications)} entries shown"


def render_data(data: dict) -> str:
    # Escape "</" so a value can never close the <script> element early.
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return f'<script type="application/json" id="publication-data">{payload}</script>'


def replace_block(page: str, name: str, content: str) -> str:
    pattern = re.compile(
        rf"(<!-- build:{name} -->)(.*?)(<!-- /build:{name} -->)", re.DOTALL
    )
    if not pattern.search(page):
        raise SystemExit(f"index.html is missing the build:{name} markers")
    return pattern.sub(lambda m: f"{m.group(1)}{content}{m.group(3)}", page, count=1)


def build(page: str, data: dict) -> str:
    page = replace_block(page, "books", "\n" + render_books(data["books"]) + "\n    ")
    page = replace_block(page, "articles", "\n" + render_articles(data["publications"]) + "\n    ")
    page = replace_block(page, "article-count", render_count(data["publications"]))
    page = replace_block(page, "data", render_data(data))
    return page


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="fail if index.html is out of date")
    args = parser.parse_args()

    data = json.loads(DATA.read_text(encoding="utf-8"))
    current = INDEX.read_text(encoding="utf-8")
    updated = build(current, data)

    if args.check:
        if updated != current:
            print("index.html is out of date. Run: python3 scripts/build_publications.py")
            return 1
        print("index.html is up to date.")
        return 0

    if updated != current:
        INDEX.write_text(updated, encoding="utf-8")
        print("index.html updated.")
    else:
        print("index.html already up to date.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
