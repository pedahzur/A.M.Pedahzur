# Academic Blog Design

## Purpose and success criteria

Add a permanent academic-blog surface to Ami Pedahzur's public GitHub Pages site and publish the first long-form post, “Between Academic Rigor and Writing for a Wider Audience.” The result should feel like an editorial extension of the existing academic site rather than a separate product.

The feature succeeds when visitors can discover the blog from the primary navigation and homepage, scan the blog index, read the complete article comfortably on mobile and desktop, follow all 16 notes, and return to the main site without encountering a broken link.

## Chosen direction

Use a restrained academic-journal aesthetic. Literata will carry the article body and display headings; IBM Plex Sans will carry navigation, metadata, labels, and controls. The palette will reuse the site's paper, ink, muted, rule, and accent colors. The memorable element will be the reading composition: a quiet editorial column paired with a slim, sticky table of contents on wide screens.

The design will not add illustrations, decorative stock imagery, comments, search, an RSS feed, or a content-management system. These are outside the present need and can be added after the blog contains more than one post.

## Information architecture

- `/blog/` will be the blog index. It will introduce the academic blog and display the first post as a lead article card.
- `/blog/academic-rigor-and-writing-for-a-wider-audience/` will contain the complete English article.
- The homepage primary navigation will gain a `Blog` link.
- The homepage will gain a compact `Academic Blog` section between `Articles` and `Contact`, with the post title, description, date, reading time, and direct link.
- Both new pages will link back to the site homepage and use the site's existing footer and identity.
- `sitemap.xml` will include the blog index and post.

## Page composition

### Blog index

The index will use a concise masthead, one-sentence editorial statement, and a lead-post card. The card will expose enough of the argument to establish intellectual value without reproducing the article opening. The page must remain useful when future posts are added as sibling cards.

### Article page

The article will use semantic `<article>` markup with a visible category label, title, short deck, publication date, reading time, and a direct path back to the blog index. The main body will preserve the seven numbered sections, fifteen subsections, practical lists, diagnostic table, and sixteen source notes from the approved English manuscript.

On screens at least 1100 pixels wide, the article will use a two-column reading grid: a text column capped near 68 characters and a narrow sticky table of contents. On smaller screens, the table of contents will become an inline disclosure before the article body. The table will scroll horizontally when needed rather than force the page wider than the viewport.

Each note call will link to its note, and every note will include a return link. Focus styles must remain visible. Motion will be limited to restrained hover and entry transitions and disabled when `prefers-reduced-motion` is active.

## Files and boundaries

The implementation will add:

- `blog/index.html`
- `blog/blog.css`
- `blog/academic-rigor-and-writing-for-a-wider-audience/index.html`

It will modify only:

- `index.html`
- `sitemap.xml`
- `tests/test_site.py`

The article source remains outside the public repository and will be converted into semantic HTML without exposing a local path. Existing book pages, the field guide, the CV, and unrelated homepage sections will not change.

## Metadata and discovery

Both pages will include unique titles, descriptions, canonical URLs, Open Graph metadata, and Twitter-card metadata. The post will include `ScholarlyArticle` JSON-LD with author, date published, headline, description, URL, and subject keywords. The page will not claim a journal venue or peer-review status.

## Failure handling

The site is static, so failure control centers on build-time verification. Relative paths will be tested from both nested routes. Every table-of-contents anchor, footnote call, footnote return, stylesheet, and homepage link must resolve. Long URLs and bibliographic entries must wrap without causing horizontal page overflow.

## Test strategy

1. Extend `tests/test_site.py` before implementation with a blog publication contract. It will require both routes, homepage discovery, canonical URLs, article metadata, seven numbered sections, sixteen note definitions, return links, the shared stylesheet, and sitemap entries.
2. Run the new test and observe the expected failure because the blog files do not yet exist.
3. Implement the smallest static pages and styles that satisfy the contract, then run the full test suite.
4. Serve the repository locally and inspect the homepage, blog index, and article at widths of 375, 768, 1280, and 1920 pixels. Check keyboard focus, overflow, text measure, navigation, and reduced-motion behavior.
5. Run a code review on the final diff, fix actionable findings, rerun tests, and publish through a pull request.

## Deployment

Work will remain on `agent/add-academic-blog`. Only the explicit blog, homepage, sitemap, test, and design files will be staged. After validation, the branch will be pushed and a pull request opened against `main`. The PR will be merged only after its checks succeed, after which the GitHub Pages deployment and both public URLs will be verified.
