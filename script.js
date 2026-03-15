/* ── Data ── */

const books = [
  {
    title: "Suicide Terrorism",
    publisher: "Polity Press",
    year: "2005",
    description: "A comprehensive cross-cultural analysis of suicide terrorism, tracing its emergence in Lebanon, Israel, Sri Lanka, Turkey, Chechnya, Iraq, and Al-Qaeda's global jihad.",
    page: "book-suicide-terrorism.html",
    links: [
      { label: "Publisher", url: "https://politybooks.com/bookdetail/?isbn=9780745633824" }
    ]
  },
  {
    title: "The Israeli Secret Services and the Struggle Against Terrorism",
    publisher: "Columbia University Press",
    year: "2009",
    description: "Examines Israel's counterterrorism strategies from 1948 onward, arguing that defensive measures have proven more effective than offensive operations and targeted killings.",
    page: "book-israeli-secret-services.html",
    links: [
      { label: "Publisher", url: "https://cup.columbia.edu/book/the-israeli-secret-services-and-the-struggle-against-terrorism/9780231140430" }
    ]
  },
  {
    title: "Jewish Terrorism in Israel",
    publisher: "Columbia University Press",
    year: "2009",
    description: "Explores how religious terrorism emerges from totalistic communities, spanning from the ancient sicarii to the assassination of Prime Minister Yitzhak Rabin.",
    page: "book-jewish-terrorism.html",
    links: [
      { label: "Publisher", url: "https://cup.columbia.edu/book/jewish-terrorism-in-israel/9780231154468" }
    ]
  },
  {
    title: "The Triumph of Israel's Radical Right",
    publisher: "Oxford University Press",
    year: "2012",
    description: "Documents the radical right's ascendance in Israeli politics and its institutional networks, tracing the movement from fringe ideology to mainstream governance.",
    page: "book-triumph-radical-right.html",
    links: [
      { label: "Publisher", url: "https://global.oup.com/academic/product/the-triumph-of-israels-radical-right-9780199744701" }
    ]
  }
];

const publications = [
  {
    title: "Territorial Control and the Militarization of Violent Non-State Actors: Transformation, Opportunities, and Vulnerabilities",
    authors: "Ofir Dayan and Ami Pedahzur",
    venue: "Studies in Conflict & Terrorism",
    year: "2025",
    type: "journal",
    featured: true,
    summary: "Examines how territorial control changes the structure, capabilities, and weaknesses of violent non-state actors.",
    links: [{ label: "DOI", url: "https://doi.org/10.1080/1057610X.2025.2528333" }]
  },
  {
    title: "The Munich Massacre and the Proliferation of Counter-Terrorism Special Operation Forces",
    authors: "Ronit Berger and Ami Pedahzur",
    venue: "Israel Affairs",
    year: "2022",
    type: "journal",
    summary: "Connects the Munich massacre to the international spread of specialized counter-terrorism units and doctrine.",
    links: [{ label: "Google Scholar", url: "https://scholar.google.com/scholar?q=The+Munich+Massacre+and+the+Proliferation+of+Counter-Terrorism+Special+Operation+Forces+Pedahzur" }]
  },
  {
    title: "Reconstructing the Theater of Terror",
    authors: "Matthew Sweeney, Arie Perliger, and Ami Pedahzur",
    venue: "Small Wars & Insurgencies",
    year: "2021",
    type: "journal",
    summary: "Investigates the operational theater of terrorism and how spatial and organizational factors shape violent campaigns.",
    links: [{ label: "Google Scholar", url: "https://scholar.google.com/scholar?q=Reconstructing+the+Theater+of+Terror+Sweeney+Perliger+Pedahzur" }]
  },
  {
    title: "Can We Do Better? Replication and Online Appendices in Political Science",
    authors: "Jonathan Grossman and Ami Pedahzur",
    venue: "Perspectives on Politics",
    year: "2021",
    type: "methods",
    summary: "Assesses replication practices and the quality of online appendices in political science research.",
    links: [{ label: "Google Scholar", url: "https://scholar.google.com/scholar?q=Can+We+Do+Better+Replication+Online+Appendices+Political+Science+Grossman+Pedahzur" }]
  },
  {
    title: "Political Science and Big Data: Why We Need Unstructured Big Data and How to Use It",
    authors: "Jonathan Grossman and Ami Pedahzur",
    venue: "Political Science Quarterly",
    year: "2020",
    type: "methods",
    summary: "Argues for the use of unstructured big data in political science and outlines practical strategies for analysis.",
    links: [{ label: "Google Scholar", url: "https://scholar.google.com/scholar?q=Political+Science+Big+Data+Unstructured+Grossman+Pedahzur" }]
  },
  {
    title: "Counter-Cultures, Group Dynamics and Religious Terrorism",
    authors: "Arie Perliger and Ami Pedahzur",
    venue: "Political Studies",
    year: "2016",
    type: "journal",
    summary: "Explores the interaction between group dynamics, counter-cultures, and the emergence of religious terrorism.",
    links: [{ label: "Google Scholar", url: "https://scholar.google.com/scholar?q=Counter-Cultures+Group+Dynamics+Religious+Terrorism+Perliger+Pedahzur" }]
  },
  {
    title: "Social Network Analysis in the Study of Terrorism and Political Violence",
    authors: "Arie Perliger and Ami Pedahzur",
    venue: "PS: Political Science and Politics",
    year: "2011",
    type: "methods",
    summary: "Shows how social network analysis can reveal structure, diffusion, and hierarchy in violent organizations.",
    links: [{ label: "Google Scholar", url: "https://scholar.google.com/scholar?q=Social+Network+Analysis+Study+Terrorism+Political+Violence+Perliger+Pedahzur" }]
  },
  {
    title: "The Changing Nature of Suicide Attacks: A Social Network Perspective",
    authors: "Ami Pedahzur and Arie Perliger",
    venue: "Social Forces",
    year: "2006",
    type: "journal",
    summary: "Uses a social network perspective to explain changes in suicide attack organization and execution.",
    links: [{ label: "Google Scholar", url: "https://scholar.google.com/scholar?q=The+Changing+Nature+of+Suicide+Attacks+Social+Network+Perspective+Pedahzur+Perliger" }]
  }
];

/* ── Render Books ── */
function renderBooks() {
  const container = document.getElementById("book-list");
  if (!container) return;
  container.innerHTML = books.map(b => `
    <div class="book-card">
      <h3>${b.title}</h3>
      <p class="book-meta">${b.publisher}, ${b.year}</p>
      <p>${b.description}</p>
      <div class="cite-buttons">
        <a class="cite-btn" href="${b.page}">Read More</a>
        ${b.links.map(l => `<a class="cite-btn" href="${l.url}" target="_blank" rel="noopener">${l.label}</a>`).join("")}
      </div>
    </div>
  `).join("");
}

/* ── Render Articles ── */
function renderArticles() {
  const container = document.getElementById("article-list");
  if (!container) return;
  renderArticleList(container, publications);
}

function renderArticleList(container, items) {
  container.innerHTML = items.map(pub => {
    const linksHtml = pub.links.map(l =>
      `<a class="cite-btn" href="${l.url}" target="_blank" rel="noopener">${l.label}</a>`
    ).join("");
    const featuredClass = pub.featured ? " pub-item-featured" : "";
    const eyebrow = pub.featured ? `<p class="pub-eyebrow">Featured Work</p>` : "";
    return `
      <article class="pub-item${featuredClass}">
        ${eyebrow}
        <h3>${pub.title}</h3>
        <p class="pub-meta">${pub.authors} &middot; ${pub.venue}</p>
        <div class="pub-badges">
          <span class="pub-badge">${pub.type === "journal" ? "Journal Article" : pub.type === "methods" ? "Methods" : pub.type === "chapter" ? "Book Chapter" : pub.type}</span>
          <span class="pub-badge">${pub.year}</span>
        </div>
        ${pub.summary ? `<p class="pub-summary">${pub.summary}</p>` : ""}
        <div class="cite-buttons">${linksHtml}</div>
      </article>
    `;
  }).join("");
}

/* ── Filters ── */
function setupFilters() {
  const buttons = document.querySelectorAll(".filter-btn");
  const container = document.getElementById("article-list");
  if (!buttons.length || !container) return;

  buttons.forEach(btn => {
    btn.addEventListener("click", () => {
      buttons.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      const filter = btn.getAttribute("data-filter");
      if (filter === "all") {
        renderArticleList(container, publications);
      } else {
        renderArticleList(container, publications.filter(p => p.type === filter));
      }
    });
  });
}

/* ── Citation Modal ── */
function closeCiteModal() {
  const modal = document.getElementById("cite-modal");
  if (modal) {
    modal.hidden = true;
    modal.style.display = "none";
  }
}

function openCiteModal(title, bibtex, ris) {
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
}

function copyCitation() {
  const contentEl = document.getElementById("cite-content");
  if (contentEl) navigator.clipboard.writeText(contentEl.textContent);
}

/* ── Modal Tab Switching ── */
function setupModalTabs() {
  document.querySelectorAll(".modal-tab").forEach(tab => {
    tab.addEventListener("click", () => {
      document.querySelectorAll(".modal-tab").forEach(t => t.classList.remove("active"));
      tab.classList.add("active");
      const format = tab.getAttribute("data-format");
      const modal = document.getElementById("cite-modal");
      const contentEl = document.getElementById("cite-content");
      if (modal && contentEl) {
        contentEl.textContent = format === "ris" ? (modal._ris || "") : (modal._bibtex || "");
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

/* ── Year ── */
function setYear() {
  const el = document.getElementById("year");
  if (el) el.textContent = new Date().getFullYear();
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
renderBooks();
renderArticles();
setupFilters();
setupModalTabs();
setupModalOverlay();
closeCiteModal();
setYear();
activateReveal();
