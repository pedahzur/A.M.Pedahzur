/* ── Data ──
   Books and articles are pre-rendered into index.html by
   scripts/build_publications.py from data/publications.json.
   The same data is embedded as JSON for filters and citations. */

function readPublicationData() {
  const el = document.getElementById("publication-data");
  if (!el) return { books: [], publications: [] };
  try {
    return JSON.parse(el.textContent);
  } catch (error) {
    console.error("Could not read publication data", error);
    return { books: [], publications: [] };
  }
}

const { books, publications } = readPublicationData();

const DEFAULT_PUBLICATION_LIMIT = 5;
const DOCUMENT_BOTTOM_TOLERANCE = 2;
const publicationView = { activeFilter: "all", expanded: false };
let activeNavigationSection = "top";

// hidden="until-found" keeps collapsed entries searchable with Find in page.
// Browsers without it (Safari) treat the value as plain `hidden`, and the
// "Show all publications" button still reveals them.
const SUPPORTS_HIDDEN_UNTIL_FOUND = typeof HTMLElement !== "undefined"
  && "onbeforematch" in HTMLElement.prototype;

/* ── Filters ── */
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
    item.hidden = !matches;
    if (matches && withinLimit) visibleCount += 1;
  });

  const more = document.getElementById("more-publications");
  if (more) {
    const collapsed = publicationView.activeFilter === "all" && !publicationView.expanded;
    more.hidden = collapsed ? (SUPPORTS_HIDDEN_UNTIL_FOUND ? "until-found" : true) : false;
  }

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
  const more = document.getElementById("more-publications");
  if (more) {
    // Find in page or a text-fragment link matched a collapsed entry: expand
    // the list so the button, count and remaining entries stay consistent.
    more.addEventListener("beforematch", () => {
      publicationView.expanded = true;
      updatePublicationView();
    });
  }
  if (!toggle) return;
  toggle.addEventListener("click", () => {
    publicationView.expanded = !publicationView.expanded;
    updatePublicationView();
    toggle.focus({ preventScroll: true });
  });
}

function setupFilters() {
  const buttons = document.querySelectorAll(".filter-btn");
  if (!buttons.length) return;

  buttons.forEach(btn => {
    btn.addEventListener("click", () => {
      buttons.forEach(b => {
        b.classList.remove("active");
        b.setAttribute("aria-pressed", "false");
      });
      btn.classList.add("active");
      btn.setAttribute("aria-pressed", "true");
      publicationView.activeFilter = btn.getAttribute("data-filter");
      publicationView.expanded = false;
      updatePublicationView();
    });
  });
}

/* ── Citation Modal ── */
function closeCiteModal() {
  const modal = document.getElementById("cite-modal");
  if (modal) {
    modal.hidden = true;
    modal.style.display = "none";
    if (modal._previousFocus && typeof modal._previousFocus.focus === "function") {
      modal._previousFocus.focus();
    }
  }
}

function openCiteModal(title, bibtex, ris, slug) {
  const modal = document.getElementById("cite-modal");
  const titleEl = document.getElementById("cite-modal-title");
  const contentEl = document.getElementById("cite-content");
  if (!modal || !contentEl) return;
  if (titleEl) titleEl.textContent = "Cite: " + title;
  contentEl.textContent = bibtex || "";
  modal.hidden = false;
  modal.style.display = "";
  modal._bibtex = bibtex;
  modal._ris = ris;
  modal._slug = slug || slugify(title);
  modal._previousFocus = document.activeElement;
  document.querySelectorAll(".modal-tab").forEach(tab => {
    const isBib = tab.getAttribute("data-format") === "bib";
    tab.classList.toggle("active", isBib);
    tab.setAttribute("aria-pressed", isBib ? "true" : "false");
  });
  updateCitationDownload("bib");
  const panel = modal.querySelector(".modal");
  if (panel) panel.focus();
}

function copyCitation() {
  const contentEl = document.getElementById("cite-content");
  if (contentEl) navigator.clipboard.writeText(contentEl.textContent);
}

/* ── Modal Tab Switching ── */
function setupModalTabs() {
  const tabs = document.querySelectorAll(".modal-tab");
  tabs.forEach(tab => {
    tab.addEventListener("click", () => {
      tabs.forEach(t => {
        t.classList.remove("active");
        t.setAttribute("aria-pressed", "false");
      });
      tab.classList.add("active");
      tab.setAttribute("aria-pressed", "true");
      const format = tab.getAttribute("data-format");
      const modal = document.getElementById("cite-modal");
      const contentEl = document.getElementById("cite-content");
      if (modal && contentEl) {
        contentEl.textContent = format === "ris" ? (modal._ris || "") : (modal._bibtex || "");
        updateCitationDownload(format);
      }
    });
  });
}

/* ── Modal overlay click to close ── */
function setupModalOverlay() {
  const modal = document.getElementById("cite-modal");
  if (modal) {
    modal.addEventListener("click", (e) => {
      if (e.target === modal) closeCiteModal();
    });
  }
}

function setupCitationButtons() {
  document.addEventListener("click", (event) => {
    const button = event.target.closest("[data-cite-kind]");
    if (!button) return;

    const kind = button.getAttribute("data-cite-kind");
    const index = Number(button.getAttribute("data-cite-index"));
    const item = kind === "book" ? books[index] : publications[index];
    if (!item) return;

    openCiteModal(
      item.title,
      makeBibTex(item, kind),
      makeRis(item, kind),
      slugify(`${item.authors || "ami-pedahzur"}-${item.year}-${item.title}`)
    );
  });
}

function setupEscapeToClose() {
  document.addEventListener("keydown", (event) => {
    const modal = document.getElementById("cite-modal");
    if (event.key === "Escape" && modal && !modal.hidden) {
      closeCiteModal();
    }
  });
}

function updateCitationDownload(format) {
  const modal = document.getElementById("cite-modal");
  const link = document.getElementById("cite-download");
  if (!modal || !link) return;
  const isRis = format === "ris";
  const text = isRis ? (modal._ris || "") : (modal._bibtex || "");
  const extension = isRis ? "ris" : "bib";
  link.href = `data:text/plain;charset=utf-8,${encodeURIComponent(text)}`;
  link.download = `${modal._slug || "citation"}.${extension}`;
}

function makeBibTex(item, kind) {
  const key = slugify(`${item.authors || "pedahzur"}-${item.year}-${item.title}`);
  const type = item.bibtexType || (kind === "book" ? "book" : "article");
  const sourceField = kind === "book"
    ? ["publisher", item.publisher]
    : item.bibtexType === "unpublished"
      ? ["note", item.venue]
      : ["journal", item.venue];
  const fields = [
    ["author", item.authors],
    ["title", item.title],
    ["year", item.year],
    sourceField,
    ["url", item.links && item.links[0] ? item.links[0].url : ""]
  ].filter(([, value]) => value);

  return `@${type}{${key},\n${fields.map(([name, value]) => `  ${name} = {${value}}`).join(",\n")}\n}`;
}

function makeRis(item, kind) {
  const type = item.risType || (kind === "book" ? "BOOK" : "JOUR");
  const authorLines = (item.authors || "")
    .split(/\s+and\s+|,\s*/)
    .filter(Boolean)
    .map(author => author.replace(/^and\s+/i, ""))
    .map(author => `AU  - ${author}`)
    .join("\n");
  const source = kind === "book" ? item.publisher : item.venue;
  return [
    `TY  - ${type}`,
    authorLines,
    `TI  - ${item.title}`,
    source ? `T2  - ${source}` : "",
    item.year ? `PY  - ${item.year}` : "",
    "ER  -"
  ].filter(Boolean).join("\n");
}

function slugify(value) {
  return String(value)
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "")
    .slice(0, 80);
}

/* ── Year ── */
function setYear() {
  const el = document.getElementById("year");
  if (el) el.textContent = new Date().getFullYear();
}

/* ── Active Navigation ── */
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

function syncActiveNavigationAtDocumentBottom() {
  const documentHeight = Math.max(
    document.documentElement.scrollHeight,
    document.body.scrollHeight
  );
  const atDocumentBottom = window.scrollY + window.innerHeight
    >= documentHeight - DOCUMENT_BOTTOM_TOLERANCE;
  if (atDocumentBottom) setActiveNavigation("contact");
  return atDocumentBottom;
}

function setupActiveNavigation() {
  setActiveNavigation("top");
  window.addEventListener("scroll", syncActiveNavigationAtDocumentBottom, { passive: true });
  window.addEventListener("resize", syncActiveNavigationAtDocumentBottom);
  window.addEventListener("hashchange", () => {
    if (window.location.hash === "#contact") setActiveNavigation("contact");
  });
  if (window.location.hash === "#contact") {
    setActiveNavigation("contact");
  } else {
    syncActiveNavigationAtDocumentBottom();
  }
  if (!("IntersectionObserver" in window)) return;
  const sections = [...document.querySelectorAll("[data-nav-section]")];
  const intersectingSections = new Set();
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) intersectingSections.add(entry.target);
      else intersectingSections.delete(entry.target);
    });
    if (syncActiveNavigationAtDocumentBottom()) return;
    const visible = [...intersectingSections]
      .sort((a, b) => b.getBoundingClientRect().top - a.getBoundingClientRect().top);
    if (visible[0]) setActiveNavigation(visible[0].dataset.navSection);
  }, { rootMargin: "-90px 0px -65% 0px", threshold: 0 });
  sections.forEach(section => observer.observe(section));
  window.matchMedia("(max-width: 600px)").addEventListener("change", () => {
    setActiveNavigation(activeNavigationSection);
  });
}

/* ── Scroll Reveal ── */
function activateReveal() {
  const items = document.querySelectorAll(".reveal");
  if (!("IntersectionObserver" in window)) {
    items.forEach(item => item.classList.add("is-visible"));
    return;
  }
  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        obs.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });
  items.forEach((item, i) => {
    item.style.transitionDelay = `${Math.min(i * 80, 280)}ms`;
    observer.observe(item);
  });
}

/* ── Init ── */
setupFilters();
setupPublicationToggle();
updatePublicationView();
setupCitationButtons();
setupModalTabs();
setupModalOverlay();
setupEscapeToClose();
closeCiteModal();
setYear();
setupActiveNavigation();
activateReveal();
