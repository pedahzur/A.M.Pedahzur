# Bilingual Blog Publication Contract

English is the canonical drafting language for this blog. Every published English essay must have a complete Hebrew edition at the same slug under `he/`.

## Required pair

For an English post at:

```text
blog/<slug>/index.html
```

publish its Hebrew edition at:

```text
blog/<slug>/he/index.html
```

The pair must include:

- reciprocal, visible language links;
- canonical and `hreflang` metadata for English and Hebrew;
- `lang="he"` and `dir="rtl"` on the Hebrew page;
- the same argument, sections, tables, figures, source calls, and endnote graph;
- independent descriptions and reading-time labels in each language;
- links to both editions from the blog index and homepage;
- both URLs in `sitemap.xml`.

## Hebrew editorial standard

The Hebrew edition is a faithful translation, not a word-for-word conversion. It must preserve the English argument, evidence, qualifications, names, dates, links, and citation structure while using native Hebrew syntax and rhythm. Avoid literal English transitions and em-dash sentence habits. Do not introduce a new claim, omit uncertainty, or repair a source silently during translation.

## Current source and build path

Reviewed Hebrew Markdown lives in `blog/sources/he/`. Run:

```bash
python3 scripts/build_hebrew_blog.py
python3 -m unittest discover -s tests -q
```

The build is deterministic: running it twice should leave the generated Hebrew HTML unchanged. The bilingual test discovers every English post automatically, so adding an English post without a matching Hebrew edition fails the publication contract.
