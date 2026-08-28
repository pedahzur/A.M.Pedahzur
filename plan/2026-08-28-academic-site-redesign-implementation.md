# Academic Site Editorial Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Improve the academic homepage's hierarchy, navigation, accessibility, book presentation, and publication browsing while preserving its editorial identity and GitHub Pages URLs.

**Architecture:** Keep the existing static HTML/CSS/JavaScript architecture. Add static Current Work content in `index.html`, extend the canonical book and publication data flows in `script.js`, and build all new presentation from the existing design tokens in `styles.css`; no framework or runtime dependency is added.

**Tech Stack:** HTML5, CSS3, browser-native JavaScript, Python `unittest`, GitHub Pages.

**Spec:** `plan/2026-08-28-academic-site-redesign-design.md`

## Global Constraints

- Preserve the existing Literata and IBM Plex Sans typography, navy-and-copper palette, academic copy, citation behavior, and public URLs.
- Keep the existing 1100-pixel content width and the 900- and 600-pixel responsive breakpoints as the foundation.
- Use only static HTML, CSS, browser-native JavaScript, and locally stored images; add no client-side framework, analytics package, image CDN, or runtime dependency.
- Use relative asset and page URLs so the GitHub Pages project path `/A.M.Pedahzur/` remains valid.
- Do not add a hamburger menu or another primary-navigation link.
- Keep the full Google Scholar link visible in every publication state.
- On screens up to 600 pixels wide, relevant navigation links and buttons must have a minimum 44-by-44 CSS-pixel hit area.
- Support `prefers-reduced-motion: reduce` and a high-contrast branded `:focus-visible` treatment.
- Verify at 375, 768, 1280, and 1920 CSS pixels with no horizontal overflow.
- Follow red-green-refactor: add each contract first, run it and observe the expected failure, implement the smallest matching change, rerun the focused test, then run the full suite.
- Run the full suite with `python3 -m unittest discover -s tests -q`; bare `python3 -m unittest` is not an accepted verification command.

## File Structure

- Modify `index.html`: header wrapper and navigation hooks, hero action tiers, Current Work cards, and publication-disclosure control.
- Modify `styles.css`: aligned header, target offsets, mobile hit areas, hero hierarchy, Current Work grid, cover layout, disclosure styling, active/focus states, and reduced-motion behavior.
- Modify `script.js`: cover metadata/rendering, publication view state, filter integration, disclosure behavior, and active-section observation.
- Create `assets/book-covers/suicide-terrorism.jpg`: locally optimized Polity cover.
- Create `assets/book-covers/israeli-secret-services.jpg`: locally optimized Columbia University Press cover.
- Create `assets/book-covers/jewish-terrorism-in-israel.jpg`: locally optimized Columbia University Press cover.
- Create `assets/book-covers/triumph-israels-radical-right.jpg`: locally optimized Oxford University Press cover.
- Modify `tests/test_site.py`: homepage structure, accessibility, local-asset, and JavaScript behavior contracts.

---

### Task 1: Align the Header and Fix Navigation Targets

**Files:**
- Modify: `tests/test_site.py:1519-1545`
- Modify: `index.html:49-77`
- Modify: `styles.css:50-94, 1149-1174`

**Interfaces:**
- Consumes: existing `#top`, `#about`, `#books`, `#articles`, and `#contact` fragment identifiers.
- Produces: `.header-inner`, `.nav-link`, `.nav-home`, `data-nav-target`, `[data-nav-section]`, mobile 44-pixel hit areas, and fragment-offset CSS used by Task 5.

- [ ] **Step 1: Add the failing header and accessibility contract**

Add this method to `SiteContractTests` immediately after `test_homepage_uses_current_cv_and_minimal_hero`:

```python
def test_homepage_header_navigation_is_aligned_and_accessible(self) -> None:
    homepage = (ROOT / "index.html").read_text(encoding="utf-8")
    styles = (ROOT / "styles.css").read_text(encoding="utf-8")

    self.assertIn('class="header-inner"', homepage)
    self.assertIn('class="nav-link nav-home"', homepage)
    self.assertEqual(5, homepage.count('data-nav-target="'))
    self.assertIn('data-nav-section="top"', homepage)
    for target in ("about", "books", "articles", "contact"):
        self.assertIn(f'data-nav-section="{target}"', homepage)
    for token in (
        ".header-inner {",
        "max-width: 1100px;",
        "scroll-margin-top:",
        "min-height: 44px;",
        "min-width: 44px;",
        ":focus-visible",
        ".nav-home {",
        "display: none;",
    ):
        self.assertIn(token, styles)
```

- [ ] **Step 2: Run the focused test and verify the red state**

Run:

```bash
python3 -m unittest tests.test_site.SiteContractTests.test_homepage_header_navigation_is_aligned_and_accessible -v
```

Expected: FAIL because `.header-inner` and the new navigation hooks do not exist.

- [ ] **Step 3: Add the aligned wrapper and stable navigation hooks**

Replace the direct contents of `.site-header` with this structure and add `data-nav-section` to the observed homepage sections:

```html
<header class="site-header">
  <div class="header-inner">
    <a class="wordmark" href="#top">A. Pedahzur</a>
    <nav aria-label="Primary">
      <a class="nav-link nav-home" data-nav-target="top" href="#top">Home</a>
      <a class="nav-link" data-nav-target="about" href="#about">About</a>
      <a class="nav-link" data-nav-target="books" href="#books">Books</a>
      <a class="nav-link" data-nav-target="articles" href="#articles">Articles</a>
      <a href="blog/">Blog</a>
      <a class="nav-link" data-nav-target="contact" href="#contact">Contact</a>
    </nav>
  </div>
</header>
```

Set `data-nav-section="top"` on `.hero`, and set matching `data-nav-section` values on the About, Books, Articles, and Contact sections.

- [ ] **Step 4: Add aligned, offset, focus, and mobile hit-area CSS**

Make `.site-header` own only sticky presentation, and place its layout on `.header-inner`:

```css
.site-header {
  position: sticky;
  top: 0;
  z-index: 50;
  background: rgba(255, 255, 255, .88);
  backdrop-filter: blur(14px);
  border-bottom: 1px solid var(--border);
  box-shadow: 0 8px 26px rgba(31, 41, 51, .055);
}

.header-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  max-width: 1100px;
  margin: 0 auto;
  padding: .85rem 1.25rem;
}

main#top,
[data-nav-section] {
  scroll-margin-top: 5rem;
}

:where(a, button):focus-visible {
  outline: 3px solid rgba(184, 92, 56, .55);
  outline-offset: 3px;
  border-radius: var(--radius-sm);
}
```

Inside the existing 600-pixel media query, move the column layout from `.site-header` to `.header-inner`, set the mobile fragment offset to `7.5rem`, hide `.nav-home`, and add:

```css
.nav-link,
.filter-btn,
.cite-btn,
.btn {
  min-height: 44px;
  min-width: 44px;
  display: inline-flex;
  align-items: center;
}
```

- [ ] **Step 5: Run the focused and full test suites**

Run:

```bash
python3 -m unittest tests.test_site.SiteContractTests.test_homepage_header_navigation_is_aligned_and_accessible -v
python3 -m unittest discover -s tests -q
```

Expected: PASS. If the old hero contract still expects the four-column action grid, leave it unchanged until Task 2; this task must not change hero markup.

- [ ] **Step 6: Commit the header slice**

```bash
git add index.html styles.css tests/test_site.py
git commit -m "fix(site): improve homepage navigation accessibility"
```

---

### Task 2: Establish the Hero Hierarchy and Add Current Work

**Files:**
- Modify: `tests/test_site.py:1519-1545`
- Modify: `index.html:63-100`
- Modify: `styles.css:96-197, 1091-1196`

**Interfaces:**
- Consumes: existing CV, Google Scholar, University Profile, GitHub, Field Guide, blog, and DOI destinations.
- Produces: `.hero-actions`, `.hero-primary-actions`, `.hero-secondary-actions`, `#current-work`, `.current-work-grid`, and `.current-work-card`.

- [ ] **Step 1: Replace the obsolete hero-grid assertion and add a failing content contract**

In `test_homepage_uses_current_cv_and_minimal_hero`, remove the assertion for `grid-template-columns: repeat(4, minmax(0, 1fr));`. Add a new test:

```python
def test_homepage_prioritizes_primary_actions_and_current_work(self) -> None:
    homepage = (ROOT / "index.html").read_text(encoding="utf-8")
    styles = (ROOT / "styles.css").read_text(encoding="utf-8")

    self.assertIn('class="hero-primary-actions"', homepage)
    self.assertIn('class="hero-secondary-actions"', homepage)
    self.assertLess(
        homepage.index("Curriculum Vitae"),
        homepage.index("University Profile"),
    )
    self.assertIn('id="current-work"', homepage)
    self.assertEqual(3, homepage.count('class="current-work-card"'))
    for destination in (
        "field-guide/",
        "blog/from-one-report-to-two-histories/",
        "https://doi.org/10.1080/1057610X.2025.2528333",
    ):
        self.assertIn(f'href="{destination}"', homepage)
    for token in (
        ".hero-primary-actions {",
        ".hero-secondary-actions {",
        ".current-work-grid {",
        "grid-template-columns: repeat(3, minmax(0, 1fr));",
    ):
        self.assertIn(token, styles)
```

- [ ] **Step 2: Run the focused tests and verify the red state**

```bash
python3 -m unittest tests.test_site.SiteContractTests.test_homepage_uses_current_cv_and_minimal_hero tests.test_site.SiteContractTests.test_homepage_prioritizes_primary_actions_and_current_work -v
```

Expected: FAIL because the hero tiers and Current Work section do not exist.

- [ ] **Step 3: Replace the four equal hero actions with two explicit tiers**

Use this structure after the quote:

```html
<div class="hero-actions">
  <div class="hero-primary-actions">
    <a class="btn btn-primary" href="Ami_Pedahzur_CV_August_2026.pdf" target="_blank" rel="noopener">Curriculum Vitae</a>
    <a class="btn btn-outline" href="https://scholar.google.com/citations?hl=en&amp;user=wAMQjZ0AAAAJ" target="_blank" rel="noopener">Google Scholar</a>
  </div>
  <div class="hero-secondary-actions" aria-label="Additional profiles">
    <a href="https://marsci.haifa.ac.il/en/ami-pedahzur/" target="_blank" rel="noopener">University Profile <span aria-hidden="true">↗</span></a>
    <a href="https://github.com/pedahzur" target="_blank" rel="noopener">GitHub Research <span aria-hidden="true">↗</span></a>
  </div>
</div>
```

- [ ] **Step 4: Add the three static Current Work cards after About**

Add a `section-alt` section with `id="current-work"`, a section header, and these three cards:

```html
<section id="current-work" class="section section-alt">
  <div class="section-header">
    <p class="section-kicker">Now</p>
    <h2>Current Work</h2>
    <p class="section-sub">New research, methods, and writing.</p>
  </div>
  <div class="current-work-grid">
    <article class="current-work-card">
      <p class="current-work-type">Field Guide</p>
      <h3><a href="field-guide/">From Question to Evidence</a></h3>
      <p>A practical guide to framing questions, mapping sources, evaluating evidence, and documenting a defensible research process.</p>
      <a class="current-work-link" href="field-guide/">Explore the guide <span aria-hidden="true">→</span></a>
    </article>
    <article class="current-work-card">
      <p class="current-work-type">Latest Essay</p>
      <h3><a href="blog/from-one-report-to-two-histories/">From One Report to Two Histories</a></h3>
      <p>How a multilingual, AI-assisted workflow can reduce information overload while keeping source criticism in human hands.</p>
      <a class="current-work-link" href="blog/from-one-report-to-two-histories/">Read the essay <span aria-hidden="true">→</span></a>
    </article>
    <article class="current-work-card">
      <p class="current-work-type">Latest Research</p>
      <h3><a href="https://doi.org/10.1080/1057610X.2025.2528333" target="_blank" rel="noopener">Territorial Control and the Militarization of Violent Non-State Actors</a></h3>
      <p>How territorial control changes the structure, opportunities, and vulnerabilities of violent non-state actors.</p>
      <a class="current-work-link" href="https://doi.org/10.1080/1057610X.2025.2528333" target="_blank" rel="noopener">Open the article <span aria-hidden="true">↗</span></a>
    </article>
  </div>
</section>
```

- [ ] **Step 5: Add the responsive hero and Current Work presentation**

Replace `.hero-buttons` rules with `.hero-actions`, `.hero-primary-actions`, and `.hero-secondary-actions`. Keep the primary pair compact and use the existing button tokens. Add:

```css
.current-work-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1rem;
}

.current-work-card {
  display: flex;
  flex-direction: column;
  min-width: 0;
  padding: 1.25rem;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  box-shadow: 0 14px 38px rgba(31, 41, 51, .055);
}

.current-work-link {
  margin-top: auto;
  padding-top: 1rem;
  color: var(--accent-dark);
  font-weight: 700;
}
```

At 900 pixels use two Current Work columns; at 600 pixels use one column. At 600 pixels keep `.hero-primary-actions` in two columns down to 420 pixels, then stack it in a new 420-pixel media query.

- [ ] **Step 6: Run the focused and full suites**

```bash
python3 -m unittest tests.test_site.SiteContractTests.test_homepage_uses_current_cv_and_minimal_hero tests.test_site.SiteContractTests.test_homepage_prioritizes_primary_actions_and_current_work -v
python3 -m unittest discover -s tests -q
```

Expected: PASS with the CV filename still appearing exactly three times across the homepage.

- [ ] **Step 7: Commit the hierarchy slice**

```bash
git add index.html styles.css tests/test_site.py
git commit -m "feat(site): surface current academic work"
```

---

### Task 3: Add Verified Local Book Covers

**Files:**
- Create: `assets/book-covers/suicide-terrorism.jpg`
- Create: `assets/book-covers/israeli-secret-services.jpg`
- Create: `assets/book-covers/jewish-terrorism-in-israel.jpg`
- Create: `assets/book-covers/triumph-israels-radical-right.jpg`
- Modify: `tests/test_site.py:1519-1560`
- Modify: `script.js:3-163`
- Modify: `styles.css:566-604, 1091-1147`

**Interfaces:**
- Consumes: the four canonical publisher URLs already present in `books[].links`.
- Produces: `books[].cover`, `books[].coverAlt`, `.book-cover`, `.book-card-body`, four local image files, and `<img width="180" height="270" loading="lazy">` markup.

- [ ] **Step 1: Add the failing cover contract**

Add this method to `SiteContractTests`:

```python
def test_homepage_books_use_local_accessible_covers(self) -> None:
    scripts = (ROOT / "script.js").read_text(encoding="utf-8")
    styles = (ROOT / "styles.css").read_text(encoding="utf-8")
    filenames = (
        "suicide-terrorism.jpg",
        "israeli-secret-services.jpg",
        "jewish-terrorism-in-israel.jpg",
        "triumph-israels-radical-right.jpg",
    )

    for filename in filenames:
        path = ROOT / "assets" / "book-covers" / filename
        self.assertTrue(path.is_file(), filename)
        self.assertGreater(path.stat().st_size, 10_000, filename)
        self.assertIn(f'assets/book-covers/{filename}', scripts)
    self.assertEqual(4, scripts.count("coverAlt:"))
    for token in (
        'class="book-cover"',
        "book-cover-placeholder",
        'loading="lazy"',
        'width="180"',
        'height="270"',
    ):
        self.assertIn(token, scripts)
    self.assertIn(".book-card-body {", styles)
    self.assertIn("object-fit: contain;", styles)
```

- [ ] **Step 2: Run the focused test and verify the red state**

```bash
python3 -m unittest tests.test_site.SiteContractTests.test_homepage_books_use_local_accessible_covers -v
```

Expected: FAIL because the local cover directory and metadata do not exist.

- [ ] **Step 3: Retrieve the four covers from the canonical publisher records**

Use the official records already linked from the site:

```text
https://politybooks.com/bookdetail/?isbn=9780745633824
https://cup.columbia.edu/book/the-israeli-secret-services-and-the-struggle-against-terrorism/9780231140430
https://cup.columbia.edu/book/jewish-terrorism-in-israel/9780231154468
https://global.oup.com/academic/product/the-triumph-of-israels-radical-right-9780199744701
```

For each record, verify that the publisher page identifies the same title and save its catalog cover to the exact target filename. Convert each image to RGB JPEG, resize it to a maximum height of 720 pixels without cropping, and preserve the full portrait cover. Record the final dimensions and source URL in the implementation notes for review.

Verify the files:

```bash
file assets/book-covers/*.jpg
sips -g pixelWidth -g pixelHeight assets/book-covers/*.jpg
```

Expected: four readable JPEG images, each portrait-oriented and larger than 10 KB.

- [ ] **Step 4: Extend the book data and rendering**

Add these exact fields to the matching records:

```javascript
cover: "assets/book-covers/suicide-terrorism.jpg",
coverAlt: "Cover of Suicide Terrorism",

cover: "assets/book-covers/israeli-secret-services.jpg",
coverAlt: "Cover of The Israeli Secret Services and the Struggle Against Terrorism",

cover: "assets/book-covers/jewish-terrorism-in-israel.jpg",
coverAlt: "Cover of Jewish Terrorism in Israel",

cover: "assets/book-covers/triumph-israels-radical-right.jpg",
coverAlt: "Cover of The Triumph of Israel's Radical Right",
```

Render each card as a cover plus body. Define `coverHtml` before returning the card so a missing verified source has the intentional typographic fallback required by the design:

```javascript
const coverHtml = b.cover
  ? `<img class="book-cover" src="${b.cover}" alt="${b.coverAlt}" width="180" height="270" loading="lazy">`
  : `<div class="book-cover book-cover-placeholder" role="img" aria-label="${b.coverAlt}"><span>${b.title}</span></div>`;

<div class="book-card">
  ${coverHtml}
  <div class="book-card-body">
    <h3>${b.title}</h3>
    <p class="book-meta">${b.authors} &middot; ${b.publisher}, ${b.year}</p>
    <p>${b.description}</p>
    <div class="cite-buttons">
      <a class="cite-btn" href="${b.page}">Read More</a>
      <button class="cite-btn" type="button" data-cite-kind="book" data-cite-index="${index}">Cite</button>
      ${b.links.map(l => `<a class="cite-btn" href="${l.url}" target="_blank" rel="noopener">${l.label}</a>`).join("")}
    </div>
  </div>
</div>
```

- [ ] **Step 5: Add the book-cover layout**

Use a compact internal grid while preserving the outer two-column book grid:

```css
.book-card {
  display: grid;
  grid-template-columns: 112px minmax(0, 1fr);
  gap: 1.1rem;
  align-items: start;
}

.book-cover {
  width: 112px;
  aspect-ratio: 2 / 3;
  object-fit: contain;
  background: var(--bg-soft);
  border: 1px solid var(--border);
  box-shadow: 0 8px 20px rgba(31, 41, 51, .12);
}

.book-card-body {
  display: flex;
  flex-direction: column;
  min-width: 0;
  height: 100%;
}

.book-cover-placeholder {
  display: grid;
  place-items: center;
  padding: .75rem;
  color: #fff;
  background: var(--accent-dark);
  font-family: var(--font-serif);
  font-size: .78rem;
  line-height: 1.25;
  text-align: center;
}
```

At 600 pixels retain the cover-and-copy grid when the card permits it; at 420 pixels reduce the cover width to 88 pixels. Do not crop covers.

- [ ] **Step 6: Run focused and full verification**

```bash
python3 -m unittest tests.test_site.SiteContractTests.test_homepage_books_use_local_accessible_covers -v
python3 -m unittest discover -s tests -q
git diff --check
```

Expected: PASS and no whitespace errors.

- [ ] **Step 7: Commit the cover slice**

```bash
git add assets/book-covers script.js styles.css tests/test_site.py
git commit -m "feat(site): add local book cover thumbnails"
```

---

### Task 4: Add the Publication Disclosure State Model

**Files:**
- Modify: `tests/test_site.py:1519-1560`
- Modify: `index.html:108-127`
- Modify: `script.js:165-229, 415-425`
- Modify: `styles.css:625-690, 1084-1088`

**Interfaces:**
- Consumes: the canonical `publications` array and existing `data-type` and `data-topics` attributes.
- Produces: `DEFAULT_PUBLICATION_LIMIT`, `publicationView`, `publicationMatches(pub, filter)`, `updatePublicationView()`, `setupPublicationToggle()`, and `#publication-toggle`.

- [ ] **Step 1: Add the failing disclosure contract**

Add this method to `SiteContractTests`:

```python
def test_homepage_publications_default_to_five_and_filters_stay_complete(self) -> None:
    homepage = (ROOT / "index.html").read_text(encoding="utf-8")
    scripts = (ROOT / "script.js").read_text(encoding="utf-8")

    self.assertIn('id="publication-toggle"', homepage)
    self.assertIn('hidden aria-controls="article-list"', homepage)
    self.assertIn('aria-controls="article-list"', homepage)
    self.assertIn('aria-expanded="false"', homepage)
    self.assertIn("Show all publications", homepage)
    for token in (
        "const DEFAULT_PUBLICATION_LIMIT = 5;",
        'activeFilter: "all"',
        "expanded: false",
        "function publicationMatches(pub, filter)",
        "function updatePublicationView()",
        "function setupPublicationToggle()",
        'toggle.hidden = publicationView.activeFilter !== "all"',
        'publicationView.expanded = false;',
        '`${visibleCount} of ${publications.length} entries shown`',
    ):
        self.assertIn(token, scripts)
```

- [ ] **Step 2: Run the focused test and verify the red state**

```bash
python3 -m unittest tests.test_site.SiteContractTests.test_homepage_publications_default_to_five_and_filters_stay_complete -v
```

Expected: FAIL because the disclosure control and state model do not exist.

- [ ] **Step 3: Add the accessible disclosure control**

Place the control between `#article-list` and `.scholar-link`:

```html
<div class="publication-disclosure">
  <button id="publication-toggle" class="btn btn-outline publication-toggle" type="button" hidden aria-controls="article-list" aria-expanded="false">Show all publications</button>
</div>
```

- [ ] **Step 4: Implement one state model for filters and disclosure**

Add:

```javascript
const DEFAULT_PUBLICATION_LIMIT = 5;
const publicationView = { activeFilter: "all", expanded: false };

function publicationMatches(pub, filter) {
  if (filter === "all") return true;
  if (filter.startsWith("topic-")) {
    return (pub.topics || []).includes(filter.replace("topic-", ""));
  }
  return pub.type === filter;
}

function updatePublicationView() {
  const items = [...document.querySelectorAll("#article-list .pub-item")];
  const toggle = document.getElementById("publication-toggle");
  let visibleCount = 0;

  items.forEach((item, index) => {
    const pub = publications[index];
    const matches = publicationMatches(pub, publicationView.activeFilter);
    const withinLimit = publicationView.activeFilter !== "all"
      || publicationView.expanded
      || index < DEFAULT_PUBLICATION_LIMIT;
    item.hidden = !(matches && withinLimit);
    if (!item.hidden) visibleCount += 1;
  });

  const count = document.getElementById("article-count");
  if (count) count.textContent = `${visibleCount} of ${publications.length} entries shown`;
  if (!toggle) return;
  toggle.hidden = publicationView.activeFilter !== "all"
    || publications.length <= DEFAULT_PUBLICATION_LIMIT;
  toggle.setAttribute("aria-expanded", String(publicationView.expanded));
  toggle.textContent = publicationView.expanded
    ? "Show fewer publications"
    : "Show all publications";
}

function setupPublicationToggle() {
  const toggle = document.getElementById("publication-toggle");
  if (!toggle) return;
  toggle.addEventListener("click", () => {
    publicationView.expanded = !publicationView.expanded;
    updatePublicationView();
    toggle.focus({ preventScroll: true });
  });
}
```

Change `setupFilters()` so each click updates pressed states, assigns `publicationView.activeFilter`, assigns `publicationView.expanded = false;`, and calls `updatePublicationView()` instead of directly changing each article's `hidden` property.

After `renderArticles()` in initialization, call `setupFilters()`, `setupPublicationToggle()`, then `updatePublicationView()`.

- [ ] **Step 5: Style the disclosure without competing with Google Scholar**

```css
.publication-disclosure {
  display: flex;
  justify-content: center;
  margin-top: 1.25rem;
}

.publication-toggle[hidden] {
  display: none;
}
```

Keep `.scholar-link` and its margin below this control.

- [ ] **Step 6: Run focused and full verification**

```bash
python3 -m unittest tests.test_site.SiteContractTests.test_homepage_publications_default_to_five_and_filters_stay_complete -v
python3 -m unittest discover -s tests -q
```

Expected: PASS. The source must still contain all nine publication objects and all existing citation buttons.

- [ ] **Step 7: Commit the publication slice**

```bash
git add index.html script.js styles.css tests/test_site.py
git commit -m "feat(site): add progressive publication disclosure"
```

---

### Task 5: Add Active-Section Navigation and Reduced-Motion Behavior

**Files:**
- Modify: `tests/test_site.py:1519-1585`
- Modify: `script.js:388-425`
- Modify: `styles.css:79-88, 1084-1215`

**Interfaces:**
- Consumes: Task 1's `.nav-link`, `data-nav-target`, and `[data-nav-section]` hooks.
- Produces: `setActiveNavigation(sectionId)`, `setupActiveNavigation()`, `.nav-link[aria-current="location"]`, wordmark current state on mobile, and a site-wide reduced-motion rule.

- [ ] **Step 1: Add the failing enhancement contract**

Add this method to `SiteContractTests`:

```python
def test_homepage_tracks_active_sections_and_respects_reduced_motion(self) -> None:
    scripts = (ROOT / "script.js").read_text(encoding="utf-8")
    styles = (ROOT / "styles.css").read_text(encoding="utf-8")

    for token in (
        "function setActiveNavigation(sectionId)",
        "function setupActiveNavigation()",
        'if (!("IntersectionObserver" in window)) return;',
        'aria-current", "location"',
        'window.matchMedia("(max-width: 600px)")',
        "setupActiveNavigation();",
    ):
        self.assertIn(token, scripts)
    for token in (
        '.nav-link[aria-current="location"]',
        '.wordmark[aria-current="location"]',
        "@media (prefers-reduced-motion: reduce)",
        "transition-duration: .01ms !important;",
    ):
        self.assertIn(token, styles)
```

- [ ] **Step 2: Run the focused test and verify the red state**

```bash
python3 -m unittest tests.test_site.SiteContractTests.test_homepage_tracks_active_sections_and_respects_reduced_motion -v
```

Expected: FAIL because active-section functions and homepage reduced-motion CSS do not exist.

- [ ] **Step 3: Implement capability-guarded active navigation**

Add a module-level `activeNavigationSection = "top"`. Implement `setActiveNavigation(sectionId)` to remove `aria-current` from the wordmark and every `.nav-link`, then apply `aria-current="location"` to the wordmark for `top` when `window.matchMedia("(max-width: 600px)").matches`, otherwise to the matching `.nav-link[data-nav-target]`.

Implement `setupActiveNavigation()` with this observer contract:

```javascript
let activeNavigationSection = "top";

function setActiveNavigation(sectionId) {
  activeNavigationSection = sectionId;
  const wordmark = document.querySelector(".wordmark");
  const links = [...document.querySelectorAll(".nav-link[data-nav-target]")];
  [wordmark, ...links].filter(Boolean).forEach(link => link.removeAttribute("aria-current"));
  const useWordmark = sectionId === "top"
    && window.matchMedia("(max-width: 600px)").matches;
  const current = useWordmark
    ? wordmark
    : links.find(link => link.dataset.navTarget === sectionId);
  if (current) current.setAttribute("aria-current", "location");
}

function setupActiveNavigation() {
  setActiveNavigation("top");
  if (!("IntersectionObserver" in window)) return;
  const sections = [...document.querySelectorAll("[data-nav-section]")];
  const observer = new IntersectionObserver(entries => {
    const visible = entries
      .filter(entry => entry.isIntersecting)
      .sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
    if (visible[0]) setActiveNavigation(visible[0].target.dataset.navSection);
  }, { rootMargin: "-90px 0px -65% 0px", threshold: 0 });
  sections.forEach(section => observer.observe(section));
  window.matchMedia("(max-width: 600px)").addEventListener("change", () => {
    setActiveNavigation(activeNavigationSection);
  });
}
```

Call `setupActiveNavigation();` once during initialization. Do not alter the ordinary Blog link.

- [ ] **Step 4: Add current-state and reduced-motion CSS**

```css
.nav-link[aria-current="location"],
.wordmark[aria-current="location"] {
  color: var(--accent-dark);
  text-decoration-color: var(--accent);
  text-decoration-thickness: 2px;
  text-underline-offset: .35rem;
}

@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    scroll-behavior: auto !important;
    transition-duration: .01ms !important;
    animation-duration: .01ms !important;
    animation-iteration-count: 1 !important;
  }
}
```

- [ ] **Step 5: Run focused and full verification**

```bash
python3 -m unittest tests.test_site.SiteContractTests.test_homepage_tracks_active_sections_and_respects_reduced_motion -v
python3 -m unittest discover -s tests -q
git diff --check
```

Expected: PASS with no JavaScript syntax error.

- [ ] **Step 6: Validate JavaScript syntax**

```bash
node --check script.js
```

Expected: exit code 0 and no output.

- [ ] **Step 7: Commit the active-navigation slice**

```bash
git add script.js styles.css tests/test_site.py
git commit -m "feat(site): highlight active homepage sections"
```

---

### Task 6: Review, Browser-Verify, Deploy, and Verify Live

**Files:**
- Review: `index.html`
- Review: `styles.css`
- Review: `script.js`
- Review: `assets/book-covers/*.jpg`
- Review: `tests/test_site.py`
- Review: `plan/2026-08-28-academic-site-redesign-design.md`

**Interfaces:**
- Consumes: the complete implementation from Tasks 1-5 and the existing GitHub Pages workflow.
- Produces: reviewer-approved source, automated test evidence, four-width browser evidence, a pushed `main`, and a verified live deployment.

- [ ] **Step 1: Run the complete local verification gate**

```bash
git diff --check HEAD~5..HEAD
node --check script.js
python3 -m unittest discover -s tests -q
git status --short
```

Expected: no diff-check errors, JavaScript syntax success, all tests passing, and no uncommitted changes.

- [ ] **Step 2: Request a code review of the complete implementation**

Give the reviewer the design spec, implementation plan, five implementation commits, and these review priorities:

```text
Check spec coverage, regressions in existing content and citation behavior, relative-path safety for GitHub Pages, accessible names and states, publication-state correctness, responsive CSS conflicts, image provenance, and tests that could pass without proving the intended behavior.
```

Address every actionable finding. For any correction, first add or tighten a failing regression test, run it red, implement the correction, rerun the focused and full suites, and commit with `fix(site): address redesign review findings`.

- [ ] **Step 3: Start a local static server for browser verification**

```bash
python3 -m http.server 8765
```

Open `http://127.0.0.1:8765/` in the browser and keep the server session available until the local browser checks finish.

- [ ] **Step 4: Verify the four responsive widths**

At 375, 768, 1280, and 1920 CSS pixels, record these values from the rendered page:

```text
document.documentElement.scrollWidth === document.documentElement.clientWidth
document.querySelector(".header-inner").getBoundingClientRect()
document.querySelector("#current-work").getBoundingClientRect()
document.querySelectorAll(".book-cover").length === 4
document.querySelectorAll("#article-list .pub-item:not([hidden])").length === 5
```

Expected: no horizontal overflow; header aligned to the main grid; Current Work visible after About; four covers loaded with positive `naturalWidth`; five publications visible initially.

- [ ] **Step 5: Verify interactions and accessibility**

Using keyboard and pointer input:

1. Tab through wordmark, visible navigation, hero actions, Current Work cards, filters, disclosure, citation buttons, Google Scholar, and Contact.
2. Confirm every focused control has the branded focus ring and no focus is hidden beneath the sticky header.
3. Activate About, Books, Articles, and Contact navigation links; confirm each heading appears below the header and receives the active state while in view.
4. At 375 pixels, measure visible navigation links, filters, citation controls, and action buttons; each must be at least 44 pixels high.
5. Activate Show all; confirm nine visible entries, `aria-expanded="true"`, and the label `Show fewer publications`.
6. Activate Show fewer; confirm five visible entries, focus retained on the control, and `aria-expanded="false"`.
7. Activate every non-All filter; confirm all matching entries are visible, the disclosure control is hidden, the live count is accurate, and citation controls still open and close their modal.
8. Return to All; confirm five entries and the disclosure control restored.
9. Emulate reduced motion and confirm reveal content is immediately available without meaningful animation.
10. Confirm the console contains no errors or failed local asset requests.

- [ ] **Step 6: Re-run the final gate immediately before publication**

```bash
git diff --check
node --check script.js
python3 -m unittest discover -s tests -q
git status --short
git log --oneline -7
```

Expected: all checks pass and the worktree is clean. Do not claim completion from an earlier test run.

- [ ] **Step 7: Push the validated main branch**

```bash
git push origin main
```

Expected: the remote advances from the pre-redesign commit through the specification, plan, and reviewed implementation commits.

- [ ] **Step 8: Verify the GitHub Pages deployment**

Open `https://pedahzur.github.io/A.M.Pedahzur/` after the Pages workflow completes. Repeat the 375- and 1280-pixel smoke checks, verify all four cover requests return successfully under `/A.M.Pedahzur/assets/book-covers/`, activate the publication disclosure and one filter, click the Field Guide card, and confirm the browser console has no errors.

Expected: the live page matches the reviewed local source, relative paths work under the project subpath, and the eight approved improvements are visible and functional.
