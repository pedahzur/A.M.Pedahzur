#!/usr/bin/env python3
"""Build the two Hebrew blog editions from their reviewed Markdown sources."""

from __future__ import annotations

import html
import json
from pathlib import Path
import re
import subprocess


ROOT = Path(__file__).resolve().parents[1]
BLOG = ROOT / "blog"
TRANSLATION_STATUSES = {"draft", "editor-reviewed", "author-approved"}


POSTS = {
    "academic-rigor-and-writing-for-a-wider-audience": {
        "title": "בין קפדנות אקדמית לכתיבה לקהל רחב",
        "description": (
            "ספר אקדמי צריך לעמוד בשתי דרישות מלאות: מחקר משכנע "
            "וכתיבה המובילה את הקורא בבהירות, בתנופה ובכבוד."
        ),
        "date": "2026-08-12",
        "date_label": "12 באוגוסט 2026",
        "read_time": "45 דקות קריאה",
        "keywords": "ספרים אקדמיים, כתיבה אקדמית, שיטות מחקר, מחקר ציבורי",
        "toc": (
            ("שני החשדות כלפי כתיבה נגישה", "שני-החשדות-כלפי-כתיבה-נגישה"),
            ("המחקר הוא זכות הקיום של הספר", "המחקר-הוא-זכות-הקיום-של-הספר"),
            ("ספר אינו מאמר ארוך", "ספר-אינו-מאמר-ארוך"),
            ("החוזה הכפול עם הקורא", "החוזה-הכפול-עם-הקורא"),
            ("ממחקר לכתב יד: החלטות מעשיות", "ממחקר-לכתב-יד-החלטות-מעשיות"),
            ("מבחני הלחץ: הסכנות שבדרך", "מבחני-הלחץ-הסכנות-שבדרך"),
            ("ללמוד מספרים שעשו זאת היטב", "ללמוד-מספרים-שעשו-זאת-היטב"),
            ("הערות ומקורות", "notes-and-sources"),
        ),
    },
    "from-one-report-to-two-histories": {
        "title": "מאותה ידיעה לשתי היסטוריות: בניית סוכן לחקר עיתונות היסטורית",
        "description": (
            "תהליך עבודה שניתן לשחזר לאיתור, אימות והשוואה של עדויות "
            "עיתונאיות רב־לשוניות, בלי שהבינה המלאכותית תחליף את שיקול דעתו של ההיסטוריון."
        ),
        "date": "2026-08-13",
        "date_label": "13 באוגוסט 2026",
        "read_time": "12 דקות קריאה",
        "keywords": (
            "עיתונות היסטורית, היסטוריה דיגיטלית, מחקר בסיוע בינה מלאכותית, "
            "ביקורת מקורות, ארכיונים רב־לשוניים"
        ),
        "toc": (
            ("ממחסור בגישה לעודף מידע", "ממחסור-בגישה-לעודף-מידע"),
            ("מחמש שאלות לשחזור אירוע", "מחמש-שאלות-לשחזור-אירוע"),
            ("בין העמוד לטענה", "בין-העמוד-לטענה"),
            ("מן הפיילוט לסקיל", "מן-הפיילוט-לסקיל"),
            ("מה השיטה מוסיפה", "מה-השיטה-מוסיפה"),
            ("הערות ומקורות", "notes-and-sources"),
        ),
    },
}


def pandoc_fragment(source: Path) -> str:
    return subprocess.run(
        [
            "pandoc",
            "--from",
            "markdown+smart",
            "--to",
            "html5",
            "--section-divs",
            "--wrap=none",
            str(source),
        ],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout


def split_body_and_notes(fragment: str) -> tuple[str, str]:
    marker = '<section id="footnotes"'
    body, notes_tail = fragment.split(marker, 1)
    body = re.sub(
        r'^<section[^>]+class="level1">\n<h1>.*?</h1>\n',
        "",
        body,
        count=1,
        flags=re.DOTALL,
    )
    body = body.rsplit("</section>", 1)[0].rstrip()
    body = body.replace(
        '<section id="הערות-ומקורות" class="level2">\n<h2>הערות ומקורות</h2>',
        '<section class="level2">\n<h2 id="notes-and-sources">הערות ומקורות</h2>',
    )
    notes = marker + notes_tail
    return body, notes


def academic_body() -> str:
    slug = "academic-rigor-and-writing-for-a-wider-audience"
    fragment = pandoc_fragment(BLOG / "sources" / "he" / f"{slug}.md")
    body, _ = split_body_and_notes(fragment)
    body = body.replace('class="level2"', 'class="numbered-section"')
    body = body.replace(
        '<section id="כלי-אבחון" class="level3">\n<h3>כלי אבחון</h3>',
        '<section id="כלי-אבחון" class="level3">\n'
        '<h3 id="a-diagnostic-tool-heading">כלי אבחון</h3>',
    )
    body = body.replace("<th>", '<th scope="col">')
    body = body.replace(
        "<table>",
        '<div class="article-table-wrap" tabindex="0" role="region" '
        'aria-labelledby="a-diagnostic-tool-heading">\n'
        '<table class="article-table">',
        1,
    ).replace("</table>", "</table>\n</div>", 1)

    # Pandoc numbers repeated Markdown footnotes as new notes. The English
    # edition deliberately reuses the original 16 note definitions, so map
    # the 20 Hebrew calls back to the same note graph.
    targets = (
        (13, ""), (14, ""), (1, ""), (2, ""), (3, ""), (3, "-2"),
        (4, ""), (5, ""), (15, ""), (16, ""), (6, ""), (7, ""),
        (8, ""), (9, ""), (16, "-2"), (10, ""), (11, ""),
        (11, "-2"), (12, ""), (12, "-2"),
    )
    counter = 0

    def remap_call(match: re.Match[str]) -> str:
        nonlocal counter
        note, suffix = targets[counter]
        counter += 1
        return (
            f'<a href="#fn{note}" class="footnote-ref" '
            f'id="fnref{note}{suffix}" role="doc-noteref">'
            f"<sup>{note}</sup></a>"
        )

    body = re.sub(
        r'<a href="#fn\d+" class="footnote-ref" id="fnref\d+" '
        r'role="doc-noteref"><sup>\d+</sup></a>',
        remap_call,
        body,
    )
    if counter != len(targets):
        raise RuntimeError(f"Expected {len(targets)} academic note calls, found {counter}")

    english = (
        BLOG / slug / "index.html"
    ).read_text(encoding="utf-8")
    notes = re.search(
        r'<section id="footnotes".*?</section>', english, re.DOTALL
    )
    if notes is None:
        raise RuntimeError("Could not locate the academic endnotes")
    hebrew_notes = (
        notes.group(0)
        .replace("Back to reference", "חזרה להפניה")
        .replace(", occurrence", ", מופע")
    )
    return body + "\n" + hebrew_notes


def newspaper_body() -> str:
    slug = "from-one-report-to-two-histories"
    fragment = pandoc_fragment(BLOG / "sources" / "he" / f"{slug}.md")
    body, notes = split_body_and_notes(fragment)
    body = body.replace('class="level2"', 'class="numbered-section"')
    body = body.replace("<th>", '<th scope="col">')

    table_pattern = re.compile(
        r"<table>(.*?)</table>\n<p><em>(איור 1\..*?)</em></p>", re.DOTALL
    )
    body, table_count = table_pattern.subn(
        '<figure class="source-figure">\n'
        '<div class="article-table-wrap" tabindex="0" role="region" '
        'aria-labelledby="source-cards-caption">\n'
        '<table class="article-table">\\1</table>\n</div>\n'
        '<figcaption id="source-cards-caption">\\2</figcaption>\n</figure>',
        body,
        count=1,
    )
    if table_count != 1:
        raise RuntimeError("Could not build the newspaper source table")

    flow = """<figure class="workflow-figure">
<div class="workflow-scroll" tabindex="0" role="region" aria-labelledby="workflow-caption">
<ol class="evidence-flow">
<li><strong>שאלה ממוקדת</strong><span>הגדירו את הטענה, טווח התאריכים, השפות ונקודות המבט.</span></li>
<li><strong>מטריצת חיפוש רב־לשונית</strong><span>שלבו שמות, כתיבים, מקומות, פעולות ותוצאות.</span></li>
<li><strong>איתור מועמדים</strong><span>תעדו כל שאילתה, לרבות חיפושים שלא הניבו תוצאות.</span></li>
<li><strong>מניפסט מקורות</strong><span>שמרו מזהים, מטא־דאטה, קישורים, מצב אימות וזכויות.</span></li>
<li><strong>OCR גולמי</strong><span>הפרידו בין פלט המכונה לבין התיקונים המוצעים.</span></li>
<li><strong>אימות חזותי</strong><span>בדקו את הסריקה לפני אישור נוסח או פרט.</span></li>
<li><strong>התאמת אירועים</strong><span>דרשו התאמה בתאריך, במקום ולפחות בשני מאפיינים נוספים.</span></li>
<li><strong>הערכת מקורות</strong><span>בחנו עצמאות, סתירות ומסגור.</span></li>
<li><strong>שער אישור אנושי</strong><span>אשרו, דחו או החזירו את המועמד לבדיקה נוספת.</span></li>
<li><strong>חבילת ראיות</strong><span>הפיקו מראי מקום, טבלת הצלבה וסינתזה מסויגת.</span></li>
</ol>
</div>
<p class="workflow-return">מועמד שאינו עובר את שער האישור חוזר ליומן החיפוש. הוא נשאר חלק מנתיב הביקורת ואינו נעלם מן התיעוד.</p>
<figcaption id="workflow-caption">איור 2. מן השאלה אל חבילת הראיות. מועמד שאינו עובר את שער האישור נשמר ביומן וחוזר לבדיקה.</figcaption>
</figure>"""
    body, flow_count = re.subn(
        r'<pre class="mermaid">.*?</pre>\n<p><em>איור 2\..*?</em></p>',
        flow,
        body,
        count=1,
        flags=re.DOTALL,
    )
    if flow_count != 1:
        raise RuntimeError("Could not build the newspaper evidence flow")

    notes = notes.replace(
        'role="doc-endnotes">',
        'role="doc-endnotes" aria-labelledby="notes-and-sources">',
        1,
    )
    notes = re.sub(
        r'<li id="fn(\d+)">',
        r'<li id="fn\1" role="doc-endnote">',
        notes,
    )
    notes = re.sub(
        r'<a href="#fnref(\d+)" class="footnote-back" role="doc-backlink">',
        r'<a href="#fnref\1" class="footnote-back" role="doc-backlink" '
        r'aria-label="חזרה להפניה \1">',
        notes,
    )
    return body + "\n" + notes


def toc_html(items: tuple[tuple[str, str], ...]) -> str:
    return "\n".join(
        f'              <li><a href="#{fragment}">{html.escape(label)}</a></li>'
        for label, fragment in items
    )


def read_translation_status(slug: str) -> str:
    source = BLOG / "sources" / "he" / f"{slug}.md"
    document = source.read_text(encoding="utf-8")
    frontmatter_match = re.match(
        r"\A---[ \t]*\r?\n(?P<metadata>.*?)\r?\n---[ \t]*(?:\r?\n|\Z)",
        document,
        re.DOTALL,
    )
    if frontmatter_match is None:
        raise RuntimeError(f"Missing translation_status in {source}")
    statuses = re.findall(
        r"^translation_status[ \t]*:[ \t]*(.*?)[ \t]*$",
        frontmatter_match.group("metadata"),
        re.MULTILINE,
    )
    if not statuses:
        raise RuntimeError(f"Missing translation_status in {source}")
    if len(statuses) != 1:
        raise RuntimeError(f"Duplicate translation_status in {source}")
    status = statuses[0]
    if status not in TRANSLATION_STATUSES:
        raise RuntimeError(f"Unsupported translation_status {status!r} in {source}")
    return status


def page(slug: str, body: str, status: str) -> str:
    data = POSTS[slug]
    title = data["title"]
    description = data["description"]
    english_url = f"https://pedahzur.github.io/A.M.Pedahzur/blog/{slug}/"
    hebrew_url = english_url + "he/"
    structured = {
        "@context": "https://schema.org",
        "@type": "ScholarlyArticle",
        "headline": title,
        "description": description,
        "keywords": data["keywords"],
        "author": {"@type": "Person", "name": "Ami Pedahzur"},
        "datePublished": data["date"],
        "inLanguage": "he",
        "url": hebrew_url,
        "isTranslationOf": {
            "@type": "ScholarlyArticle",
            "inLanguage": "en",
            "url": english_url,
        },
    }
    contents = toc_html(data["toc"])
    status_notice = ""
    if status != "author-approved":
        status_notice = """      <aside class="translation-status" role="note" aria-labelledby="translation-status-title">
        <p id="translation-status-title"><strong>טיוטת תרגום בעריכה</strong></p>
        <p>המהדורה העברית עוברת כעת עריכה לשונית. המהדורה האנגלית היא הגרסה המאושרת בשלב זה.</p>
      </aside>
"""
    return f"""<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(title)} | עמי פדהצור</title>
  <meta name="description" content="{html.escape(description)}">
  <link rel="canonical" href="{hebrew_url}">
  <link rel="alternate" hreflang="he" href="{hebrew_url}">
  <link rel="alternate" hreflang="en" href="{english_url}">
  <link rel="alternate" hreflang="x-default" href="{english_url}">
  <link rel="icon" type="image/svg+xml" href="../../../favicon.svg">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="Ami Pedahzur">
  <meta property="og:title" content="{html.escape(title)}">
  <meta property="og:description" content="{html.escape(description)}">
  <meta property="og:url" content="{hebrew_url}">
  <meta property="article:published_time" content="{data['date']}">
  <meta property="og:locale" content="he_IL">
  <meta property="og:locale:alternate" content="en_US">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="{html.escape(title)}">
  <meta name="twitter:description" content="{html.escape(description)}">
  <script type="application/ld+json">
{json.dumps(structured, ensure_ascii=False, indent=2)}
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Hebrew:wght@400;500;600;700&amp;family=Noto+Serif+Hebrew:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../../blog.css">
</head>
<body>
  <a class="skip-link" href="#main-content">דילוג לתוכן המרכזי</a>
  <header class="site-header">
    <a class="wordmark" href="../../../">עמי פדהצור</a>
    <nav aria-label="ניווט ראשי">
      <a href="../../../">בית</a>
      <a href="../../../#about">אודות</a>
      <a href="../../../#books">ספרים</a>
      <a href="../../../#articles">מאמרים</a>
      <a href="../../" aria-current="location">בלוג</a>
      <a href="../../../#contact">יצירת קשר</a>
    </nav>
  </header>
  <main id="main-content">
    <article class="essay" data-translation-status="{status}" aria-labelledby="article-title">
      <header class="article-header">
        <div class="article-utility">
          <p class="eyebrow">הבלוג האקדמי</p>
          <p class="language-switch" aria-label="בחירת שפה"><a href="../" hreflang="en" lang="en">English</a> <span aria-hidden="true">·</span> <strong aria-current="page">עברית</strong></p>
        </div>
        <h1 id="article-title">{html.escape(title)}</h1>
        <p class="article-deck">{html.escape(description)}</p>
        <p class="essay-meta"><time datetime="{data['date']}">{data['date_label']}</time> <span aria-hidden="true">·</span> {data['read_time']}</p>
      </header>
{status_notice}      <details class="mobile-toc">
        <summary>תוכן המאמר</summary>
        <nav aria-label="תוכן המאמר">
          <ol>
{contents}
          </ol>
        </nav>
      </details>
      <div class="article-layout">
        <aside class="article-toc">
          <nav aria-label="תוכן המאמר">
            <p>תוכן המאמר</p>
            <ol>
{contents}
            </ol>
          </nav>
        </aside>
        <div class="article-body essay-body">
{body}
        </div>
      </div>
    </article>
  </main>
  <footer class="site-footer">
    <p>&copy; 2026 עמי פדהצור. כל הזכויות שמורות.</p>
  </footer>
</body>
</html>
"""


def translation_link_labels(status: str) -> tuple[str, str]:
    if status == "author-approved":
        return "עברית", "עברית"
    return "עברית (טיוטה בעריכה)", "עברית, טיוטה בעריכה"


def render_index_translation_link(
    document: str, href: str, status: str, source: Path
) -> str:
    visible_label, aria_label = translation_link_labels(status)
    pattern = re.compile(
        r'(<a\b(?=[^>]*\bhref="' + re.escape(href) + r'")'
        r'(?=[^>]*\blang="he")[^>]*\baria-label=")[^"]*'
        r'("[^>]*>).*?(</a>)',
        re.DOTALL,
    )
    rendered, count = pattern.subn(
        lambda match: (
            f"{match.group(1)}{aria_label}{match.group(2)}"
            f"{visible_label}{match.group(3)}"
        ),
        document,
        count=1,
    )
    if count != 1:
        raise RuntimeError(
            f"Could not locate Hebrew edition link {href!r} in {source}"
        )
    return rendered


def render_translation_indexes(statuses: dict[str, str]) -> dict[Path, str]:
    indexes = (
        (BLOG / "index.html", "{slug}/he/"),
        (ROOT / "index.html", "blog/{slug}/he/"),
    )
    rendered_indexes: dict[Path, str] = {}
    for index_path, href_template in indexes:
        document = index_path.read_text(encoding="utf-8")
        for slug, status in statuses.items():
            document = render_index_translation_link(
                document,
                href_template.format(slug=slug),
                status,
                index_path,
            )
        rendered_indexes[index_path] = document
    return rendered_indexes


def write_site(rendered_bodies: dict[str, str]) -> None:
    statuses = {slug: read_translation_status(slug) for slug in POSTS}
    rendered_articles = {
        BLOG / slug / "he" / "index.html": page(
            slug, rendered_bodies[slug], statuses[slug]
        )
        for slug in POSTS
    }
    rendered_indexes = render_translation_indexes(statuses)

    for destination, document in rendered_articles.items():
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(document, encoding="utf-8")
    for destination, document in rendered_indexes.items():
        destination.write_text(document, encoding="utf-8")


def main() -> None:
    write_site(
        {
            "academic-rigor-and-writing-for-a-wider-audience": academic_body(),
            "from-one-report-to-two-histories": newspaper_body(),
        }
    )


if __name__ == "__main__":
    main()
