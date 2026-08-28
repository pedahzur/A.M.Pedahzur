# Academic Site Editorial Redesign

Date: 2026-08-28
Status: Approved in chat; awaiting written-spec review

## Purpose

Improve the academic homepage's hierarchy, navigation, accessibility, and mobile usability while preserving its established editorial identity. The redesign should help a first-time visitor understand Ami Pedahzur's current work quickly, reach the CV and Google Scholar profile without searching, and browse publications without scrolling through the entire archive.

## Scope

The work covers the homepage at `index.html`, its shared presentation in `styles.css`, its homepage rendering and interaction logic in `script.js`, locally stored book-cover assets, and the relevant contracts in `tests/test_site.py`.

The redesign will:

1. Align the sticky header with the homepage content grid.
2. Fix in-page navigation so section headings remain visible below the sticky header.
3. Provide touch targets of at least 44 by 44 CSS pixels on narrow screens.
4. Add an active-section state and a branded keyboard focus treatment.
5. Clarify the hero action hierarchy.
6. Add a compact Current Work section immediately after About.
7. Add locally hosted, source-verified cover thumbnails to the four book cards.
8. Collapse the default publication view to five entries while preserving all filters and the Google Scholar link.
9. Preserve the current responsive one- and two-column layout, editorial typography, navy-and-copper palette, URLs, citations, and content.

## Non-goals

- Rebranding the site or replacing the existing typography and color system.
- Migrating away from static HTML, CSS, and JavaScript.
- Rewriting academic descriptions, publication metadata, book pages, or blog articles.
- Adding a hamburger menu, client-side framework, analytics package, or external image CDN.
- Changing the GitHub Pages project path or creating a second hosted copy.

## Considered Approaches

### 1. Editorial evolution — selected

Retain the current visual identity and static architecture while restructuring the homepage hierarchy and adding small, progressively enhanced interactions. This option directly addresses the usability findings with the least maintenance cost and the lowest risk to existing URLs and content.

### 2. CSS-only refresh

Improve spacing, tap targets, and book presentation without changing the content order or publication behavior. This would be lower risk, but it would not shorten the page or surface current work earlier, so it does not satisfy the complete request.

### 3. Full visual redesign

Replace the layout and visual system with a new brand direction. This offers more visual novelty but would discard a successful existing identity, require broader regression testing, and add no clear scholarly or usability benefit.

## Information Architecture

The homepage order will be:

1. Sticky header
2. Hero
3. About
4. Current Work
5. Books
6. Articles and Chapters
7. Academic Blog
8. Contact and footer

Current Work will contain three compact editorial cards drawn from content already published on the site:

- the public From Question to Evidence Field Guide;
- the latest academic-blog essay, From One Report to Two Histories;
- the newest listed research article, Territorial Control and the Militarization of Violent Non-State Actors.

Each card will identify its content type, title, short existing description, and a single clear destination. These are navigation summaries, not duplicate publication records.

## Header and Navigation

The header will gain an inner wrapper using the same maximum width and horizontal padding as `main`, so the wordmark and final navigation link align with the content grid on wide screens.

Same-page navigation links will continue to use stable fragment identifiers. Sections will receive a `scroll-margin-top` value based on the sticky-header height, with a larger mobile value for the two-row header. This ensures that the section heading is visible after a fragment jump.

On screens up to 600 pixels wide:

- the redundant Home text link will be visually hidden because the centered wordmark already links to the top;
- the remaining links will stay visible rather than moving into a hamburger menu;
- navigation links, filters, citation controls, and action buttons will have a minimum 44-pixel hit area.

An `IntersectionObserver` will track the same-page sections and assign `aria-current="location"` plus an active visual state to the corresponding navigation link. The top state will map to Home on larger screens and to the wordmark on mobile. The Blog link remains a normal page link on the homepage and is not controlled by the observer.

All interactive controls will receive a high-contrast `:focus-visible` ring using the existing accent colors. Pointer hover styling will remain distinct from keyboard focus.

## Hero Hierarchy

The hero will retain the University of Haifa label, name, and quotation. Its four equal-weight actions will become two tiers:

- Primary actions: Curriculum Vitae and Google Scholar, presented as prominent buttons.
- Secondary actions: University Profile and GitHub Research, presented as quieter text links.

The primary actions will remain side by side when space allows and stack only on the narrowest screens. This reduces the hero's vertical height on mobile while preserving all destinations.

## Current Work

The new `#current-work` section will sit after About and use a three-card grid at desktop widths, a two-column intermediate layout where space permits, and a single column on mobile. It will use existing type, border, and card tokens rather than introduce a second design system.

The header navigation will not add another link for Current Work; keeping the existing link count prevents crowding. The section will instead be visible immediately after the short About block.

## Book Covers

Each book record in `script.js` will gain a local `cover` path and descriptive `coverAlt` value. `renderBooks()` will produce a cover-and-details layout inside each card.

Cover images will be sourced from official publisher catalog records, saved under `assets/book-covers/`, and referenced with relative URLs so GitHub Pages project-path hosting remains reliable. Images will be resized for thumbnail use, assigned intrinsic dimensions to limit layout shift, and lazy-loaded. The card layout will reserve a consistent portrait-shaped cover area without cropping the cover artwork.

If an official source cannot provide a usable cover for a title, that card will use a typographic placeholder built from HTML and CSS rather than a generated or unrelated image.

## Publication Disclosure and Filtering

The publication data remains the single canonical `publications` array. The default All view will show the first five entries in their existing order. A control after the list will read `Show all publications`, expose `aria-expanded="false"`, and disclose the remaining entries in place.

Interaction rules:

- Activating Show all reveals every publication, changes the label to `Show fewer publications`, and sets `aria-expanded="true"`.
- Activating Show fewer restores the five-entry All view and moves focus to the control without changing scroll position unexpectedly.
- Selecting any non-All filter reveals every matching publication and hides the disclosure control because the filtered set is already complete.
- Returning to All restores the five-entry collapsed state.
- The live status announces the number currently visible and the total available, for example `5 of 9 entries shown`.
- The full Google Scholar link remains visible below the disclosure control in every state.

The interaction will be implemented as a small explicit state model in `script.js`: active filter plus expanded/collapsed state. One rendering function will derive item visibility, count text, and disclosure-control state from that model, avoiding overlapping click handlers that can disagree.

## Responsive and Motion Behavior

The existing 1100-pixel content width and breakpoints will remain the foundation. The redesign will be checked at 375, 768, 1280, and 1920 CSS pixels.

At all checked widths:

- there must be no horizontal page overflow;
- body text and controls must not be clipped;
- covers must retain their aspect ratio;
- header content must remain aligned and usable;
- the current-work and book grids must collapse cleanly;
- fragment navigation must leave headings visible.

Motion will stay restrained. The existing subtle hover transitions may remain, but a `prefers-reduced-motion: reduce` rule will remove nonessential transition and smooth-scroll effects.

## Progressive Enhancement and Failure Behavior

No new external runtime dependency will be introduced. Existing destinations and content remain ordinary links. The new Current Work links are static HTML and therefore work without JavaScript.

Books and publications already depend on `script.js`; the redesign will preserve that boundary. Image failures will not hide a book title or its actions because cover and text are separate elements. The publication disclosure button will be created or activated only when the publication list is available, so it cannot become a dead control.

`IntersectionObserver` behavior will be guarded by capability detection. If it is unavailable, fragment navigation and focus states still work; only automatic active-section highlighting is omitted.

## Files and Responsibilities

- `index.html`: header wrapper, hero action tiers, Current Work markup, and publication disclosure mount/control.
- `styles.css`: aligned header, responsive action hierarchy, current-work grid, cover layout, hit targets, fragment offsets, active/focus states, and reduced-motion behavior.
- `script.js`: book cover metadata/rendering, publication view state, disclosure behavior, filter integration, and active-section observer.
- `assets/book-covers/*`: optimized local cover thumbnails.
- `tests/test_site.py`: static contracts for structure, paths, accessible control state, and key CSS/JavaScript behaviors.

## Test-Driven Implementation

Implementation will proceed in small red-green-refactor slices:

1. Add failing contracts for the header wrapper, fragment offsets, focus state, and 44-pixel mobile targets; then implement them.
2. Add failing contracts for hero action tiers and Current Work destinations; then implement them.
3. Add failing contracts for local cover paths, alt text, intrinsic dimensions, and lazy loading; then add assets and rendering.
4. Add failing contracts for the five-item default, disclosure control, filter-state behavior, and live count; then implement the JavaScript state model.
5. Add failing contracts for active-section enhancement and reduced motion; then implement them.

The repository suite will run with:

```sh
python3 -m unittest discover -s tests -q
```

After automated tests pass, the homepage will receive keyboard-only and browser checks at the four target widths. The checks will cover fragment positions, active navigation, touch-target dimensions, publication disclosure and filters, image loading, console errors, and horizontal overflow.

## Deployment and Verification

After code review and a clean final test run, only the intended site files and cover assets will be committed using a Conventional Commit. The commit will be pushed to `main`, allowing the existing GitHub Pages workflow to deploy the same validated source.

The live site at `https://pedahzur.github.io/A.M.Pedahzur/` will then be rechecked for the deployed commit, working relative paths, functional interactions, responsive behavior, and absence of console errors. Deployment is complete only when the live page reflects the changes and the browser checks pass.

## Acceptance Criteria

The redesign is complete when:

- all eight approved improvements are present;
- the existing academic identity and content remain intact;
- fragment targets are not hidden by the sticky header;
- relevant mobile targets measure at least 44 by 44 CSS pixels;
- CV and Google Scholar have clear visual priority;
- Current Work appears immediately after About with three valid destinations;
- all four books have verified local covers or an intentional typographic fallback;
- the default publication view shows five of nine entries and all filters remain complete;
- active navigation, focus visibility, and reduced-motion behavior work as specified;
- automated tests and four-width browser checks pass;
- the GitHub Pages deployment is live and verified.
