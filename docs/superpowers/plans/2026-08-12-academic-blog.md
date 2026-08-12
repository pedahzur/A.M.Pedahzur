# Academic Blog Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a discoverable academic-blog index and publish “Between Academic Rigor and Writing for a Wider Audience” as a polished, accessible long-form post on the existing GitHub Pages site.

**Architecture:** Keep the site static and dependency-free at runtime. Add one blog index, one nested article page, and a blog-specific stylesheet; connect them from the existing homepage and sitemap. Convert the approved Markdown manuscript with Pandoc, then wrap and refine the generated semantic HTML without changing the article or its sixteen notes.

**Tech Stack:** Static HTML5, CSS3, Python `unittest`, Pandoc 3.10, GitHub Pages Actions.

## Global Constraints

- Reuse Literata for article prose and display headings and IBM Plex Sans for navigation, metadata, labels, and controls.
- Reuse the site's paper, ink, muted, rule, and accent colors.
- Keep the article measure near `68ch`; use a sticky table of contents at widths of at least `1100px` and an inline disclosure below that width.
- Preserve seven numbered sections, fifteen subsections, the diagnostic table, practical lists, all sixteen note calls, and all sixteen note definitions.
- Add no illustrations, stock images, comments, search, RSS, CMS, or runtime dependency.
- Expose no local filesystem path and change no book, field-guide, CV, or unrelated homepage content.
- Publish from `agent/add-academic-blog` through a pull request to `main`; merge only after checks pass.

---

### Task 1: Blog Discovery and Index

**Files:**
- Create: `blog/index.html`
- Create: `blog/blog.css`
- Modify: `index.html:49-139`
- Modify: `sitemap.xml:2-11`
- Modify: `tests/test_site.py`

**Interfaces:**
- Consumes: existing homepage header, `.section`, `.section-alt`, `.section-header`, `.section-sub`, `.pub-item`, `.btn`, and `.btn-outline` patterns.
- Produces: public `/blog/` route, homepage `#academic-blog` section, primary `Blog` navigation link, and shared `blog/blog.css` for Task 2.

- [ ] **Step 1: Write the failing discovery test**

Add this method to `SiteContractTests`:

```python
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
```

- [ ] **Step 2: Run the test and verify RED**

Run:

```bash
python3 -m unittest tests.test_site.SiteContractTests.test_academic_blog_is_discoverable -v
```

Expected: FAIL because `blog/index.html` does not exist.

- [ ] **Step 3: Add homepage discovery**

Use `apply_patch` to add `<a href="blog/">Blog</a>` after `Articles` in the primary navigation. Insert this section between `Articles` and `Contact`:

```html
<section id="academic-blog" class="section section-alt">
  <div class="section-header">
    <p class="section-kicker">Academic Blog</p>
    <h2>Writing Research for Readers</h2>
    <p class="section-sub">Essays on research, evidence, and academic craft.</p>
  </div>
  <article class="pub-item">
    <div>
      <p class="pub-meta">August 12, 2026 · 49 min read</p>
      <h3>Between Academic Rigor and Writing for a Wider Audience</h3>
      <p>A scholarly book should not force readers to choose between credibility and interest.</p>
    </div>
    <a class="btn btn-outline" href="blog/academic-rigor-and-writing-for-a-wider-audience/">Read the essay &rarr;</a>
  </article>
</section>
```

- [ ] **Step 4: Create the blog index and base stylesheet**

Create a complete HTML5 page with canonical URL `https://pedahzur.github.io/A.M.Pedahzur/blog/`, the existing Google Font imports, `blog.css`, a skip link, a relative homepage wordmark (`../`), primary navigation, an editorial masthead, and one lead card whose relative post URL is `academic-rigor-and-writing-for-a-wider-audience/`. The post card must display `August 12, 2026`, `49 min read`, the exact title, and this deck:

```text
Research gives an academic book its right to exist. Writing gives that research a form readers can enter, examine, and remember.
```

Start `blog/blog.css` with the exact shared tokens used by both blog pages:

```css
:root {
  --paper: #f8f7f2;
  --paper-deep: #efede5;
  --ink: #1f2933;
  --muted: #626b74;
  --accent: #17324d;
  --accent-warm: #a66a2c;
  --rule: #d6d3ca;
  --reading-measure: 68ch;
  --font-serif: 'Literata', Georgia, serif;
  --font-sans: 'IBM Plex Sans', 'Helvetica Neue', sans-serif;
}
```

- [ ] **Step 5: Add both blog URLs to the sitemap**

Insert entries dated `2026-08-12` for:

```text
https://pedahzur.github.io/A.M.Pedahzur/blog/
https://pedahzur.github.io/A.M.Pedahzur/blog/academic-rigor-and-writing-for-a-wider-audience/
```

- [ ] **Step 6: Run discovery and link tests and verify GREEN**

Run:

```bash
python3 -m unittest \
  tests.test_site.SiteContractTests.test_academic_blog_is_discoverable \
  tests.test_site.SiteContractTests.test_internal_links_resolve -v
```

Expected: both tests PASS.

- [ ] **Step 7: Commit the independently working blog index**

```bash
git add index.html sitemap.xml blog/index.html blog/blog.css tests/test_site.py
git commit -m "feat(site): add academic blog index"
```

### Task 2: Long-Form Article Publication

**Files:**
- Create: `blog/academic-rigor-and-writing-for-a-wider-audience/index.html`
- Modify: `tests/test_site.py`
- Source artifact: `/Users/amipedahzur/Documents/Codex/2026-08-09/new-chat/academic-book-writing-chapter-en.md`

**Interfaces:**
- Consumes: `blog/blog.css`, the `/blog/` route, and the exact approved English Markdown manuscript.
- Produces: semantic article route, article metadata, desktop and mobile contents navigation, table markup, note calls, note definitions, and note return links.

- [ ] **Step 1: Write the failing article contract**

Add this method to `SiteContractTests`:

```python
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
    self.assertEqual(16, post.count('role="doc-noteref"'))
    self.assertEqual(16, post.count('role="doc-endnote"'))
    self.assertEqual(16, post.count('class="footnote-back"'))
    self.assertIn(
        "It makes credibility interesting and interest worthy of trust.",
        post,
    )
```

- [ ] **Step 2: Run the test and verify RED**

Run:

```bash
python3 -m unittest tests.test_site.SiteContractTests.test_academic_blog_post_preserves_article_contract -v
```

Expected: FAIL because the nested article page does not exist.

- [ ] **Step 3: Convert the approved Markdown to semantic HTML**

Generate an HTML5 conversion in a temporary directory:

```bash
blog_build_dir="$(mktemp -d)"
pandoc \
  /Users/amipedahzur/Documents/Codex/2026-08-09/new-chat/academic-book-writing-chapter-en.md \
  --from=markdown+footnotes \
  --to=html5 \
  --section-divs \
  --output="$blog_build_dir/article-fragment.html"
```

Read the fragment, then create the final page with `apply_patch`. Wrap it in a complete HTML5 document containing the existing site identity, canonical and social metadata, and this exact JSON-LD core:

```json
{
  "@context": "https://schema.org",
  "@type": "ScholarlyArticle",
  "headline": "Between Academic Rigor and Writing for a Wider Audience",
  "author": {"@type": "Person", "name": "Ami Pedahzur"},
  "datePublished": "2026-08-12",
  "url": "https://pedahzur.github.io/A.M.Pedahzur/blog/academic-rigor-and-writing-for-a-wider-audience/"
}
```

Use a visible deck reading:

```text
An academic book should meet two full demands: persuasive research and writing that leads readers through it with clarity, momentum, and respect.
```

Add a desktop `<aside class="article-toc">` and mobile `<details class="mobile-toc">` with links to all seven numbered section IDs and `notes-and-sources`. Wrap each numbered section in a class of `numbered-section`, add `class="article-table"` to the diagnostic table, retain Pandoc's `role="doc-noteref"` and `role="doc-endnote"`, and normalize all sixteen return anchors to `class="footnote-back"`.

- [ ] **Step 4: Verify content parity before styling**

Run a read-only Python check that compares the Markdown and HTML for the seven numbered headings, fifteen subsection titles, sixteen note definitions, and final sentence. It must print `CONTENT PARITY PASS` and exit zero.

- [ ] **Step 5: Run article and link tests and verify GREEN**

```bash
python3 -m unittest \
  tests.test_site.SiteContractTests.test_academic_blog_post_preserves_article_contract \
  tests.test_site.SiteContractTests.test_internal_links_resolve -v
```

Expected: both tests PASS.

- [ ] **Step 6: Commit the article publication**

```bash
git add blog/academic-rigor-and-writing-for-a-wider-audience/index.html tests/test_site.py
git commit -m "feat(blog): publish academic writing essay"
```

### Task 3: Editorial Reading Design and Accessibility

**Files:**
- Modify: `blog/blog.css`
- Modify: `tests/test_site.py`

**Interfaces:**
- Consumes: classes and semantic landmarks created in Tasks 1 and 2.
- Produces: responsive editorial layout, readable long-form typography, visible focus states, safe table and note wrapping, and reduced-motion behavior.

- [ ] **Step 1: Write the failing design contract**

Add this method to `SiteContractTests`:

```python
def test_academic_blog_uses_accessible_editorial_design(self) -> None:
    styles = (ROOT / "blog" / "blog.css").read_text(encoding="utf-8")
    post = (
        ROOT
        / "blog"
        / "academic-rigor-and-writing-for-a-wider-audience"
        / "index.html"
    ).read_text(encoding="utf-8")

    for token in (
        "--reading-measure: 68ch;",
        "grid-template-columns: minmax(0, 68ch) minmax(13rem, 17rem);",
        "position: sticky;",
        "line-height: 1.78;",
        "overflow-x: auto;",
        "@media (prefers-reduced-motion: reduce)",
        ":focus-visible",
    ):
        self.assertIn(token, styles)
    self.assertIn('href="#main-content"', post)
    self.assertIn('id="main-content"', post)
```

- [ ] **Step 2: Run the test and verify RED**

```bash
python3 -m unittest tests.test_site.SiteContractTests.test_academic_blog_uses_accessible_editorial_design -v
```

Expected: FAIL because the base stylesheet does not yet contain the complete article layout.

- [ ] **Step 3: Implement the complete editorial stylesheet**

Expand `blog/blog.css` using these binding rules:

```css
.article-layout {
  display: grid;
  grid-template-columns: minmax(0, 68ch) minmax(13rem, 17rem);
  gap: clamp(3rem, 7vw, 7rem);
  align-items: start;
}

.essay-body {
  font-family: var(--font-serif);
  font-size: clamp(1.05rem, .45vw + .95rem, 1.22rem);
  line-height: 1.78;
}

.article-toc {
  position: sticky;
  top: 6rem;
}

.article-table-wrap {
  overflow-x: auto;
}

:focus-visible {
  outline: 3px solid var(--accent-warm);
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    scroll-behavior: auto !important;
    transition: none !important;
    animation: none !important;
  }
}
```

At `max-width: 1099px`, switch `.article-layout` to one column, hide `.article-toc`, and show `.mobile-toc`. At `min-width: 1100px`, hide `.mobile-toc`. Ensure notes and URLs use `overflow-wrap: anywhere` and that the article page has no horizontal overflow at `375px`.

- [ ] **Step 4: Run the full test suite and verify GREEN**

```bash
python3 -m unittest discover -s tests -q
```

Expected: all tests PASS with no failures or errors.

- [ ] **Step 5: Serve and inspect four viewports**

Start the server:

```bash
python3 -m http.server 4173
```

Inspect `/`, `/blog/`, and `/blog/academic-rigor-and-writing-for-a-wider-audience/` at widths `375`, `768`, `1280`, and `1920`. Confirm no overlap or overflow, body measure near 68 characters, visible focus, readable notes, working table scrolling, sticky desktop contents, mobile contents disclosure, and coherent navigation.

- [ ] **Step 6: Fix only issues observed in the visual review**

Apply source-level fixes to `blog/blog.css` or the two blog pages, then repeat the affected viewport and the full test suite.

- [ ] **Step 7: Commit the verified visual layer**

```bash
git add blog/blog.css blog/index.html blog/academic-rigor-and-writing-for-a-wider-audience/index.html tests/test_site.py
git commit -m "style(blog): refine long-form reading"
```

### Task 4: Review, Pull Request, Merge, and Live Verification

**Files:**
- Review: every file changed from `origin/main...HEAD`
- Modify only when review finds a concrete issue.

**Interfaces:**
- Consumes: the green branch from Tasks 1 through 3.
- Produces: reviewed pull request, merged `main`, successful Pages deployment, and verified public homepage, blog index, and article URLs.

- [ ] **Step 1: Run final local verification**

```bash
git diff --check origin/main...HEAD
python3 -m unittest discover -s tests -q
git status -sb
```

Expected: clean diff check, all tests PASS, and only intended branch commits.

- [ ] **Step 2: Request code review and fix actionable findings**

Ask the code-reviewer to inspect `origin/main...HEAD` for correctness, security, accessibility, maintainability, and scope. Apply only evidenced fixes, then rerun Step 1.

- [ ] **Step 3: Push the branch and open a draft pull request**

```bash
git push -u origin agent/add-academic-blog
gh pr create \
  --draft \
  --base main \
  --head agent/add-academic-blog \
  --title "feat(site): add academic blog" \
  --body-file "/Users/amipedahzur/Documents/Codex/2026-08-09/new-chat/temp/academic-blog-pr.md"
```

Create the PR body at that exact path with `apply_patch`. It must state what changed, why, public impact, and the exact test and viewport matrix. Keep the PR in draft while checks run.

- [ ] **Step 4: Wait for checks, merge, and watch Pages deployment**

```bash
pr_number="$(gh pr view --json number --jq .number)"
gh pr checks "$pr_number" --watch
gh pr ready "$pr_number"
gh pr merge "$pr_number" --squash --delete-branch
pages_run_id="$(gh run list --workflow pages.yml --branch main --limit 1 --json databaseId --jq '.[0].databaseId')"
gh run watch "$pages_run_id" --exit-status
```

Expected: PR merged and the `Deploy static site to GitHub Pages` run completes successfully.

- [ ] **Step 5: Verify the public result**

Confirm HTTP 200 and inspect the rendered pages at:

```text
https://pedahzur.github.io/A.M.Pedahzur/
https://pedahzur.github.io/A.M.Pedahzur/blog/
https://pedahzur.github.io/A.M.Pedahzur/blog/academic-rigor-and-writing-for-a-wider-audience/
```

Verify that the live homepage links to the blog, the blog links to the post, the post title and sixteen notes render, and no private path appears in public HTML.
