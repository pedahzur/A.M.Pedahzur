const publications = [
  {
    title: "From Captive to Catalyst: The Militant Utility of Female Childbearing During Captivity",
    authors: "Yochim Berger and Ami Pedahzur",
    venue: "Studies in Conflict & Terrorism, 2022",
    links: [
      { label: "Google Scholar", url: "https://scholar.google.com/scholar?q=From+Captive+to+Catalyst+The+Militant+Utility+of+Female+Childbearing+During+Captivity" }
    ]
  },
  {
    title: "The Human-Machine Team: How New Technologies Shape the Contemporary Battlefield",
    authors: "Todd M. Sweeney, Yochim Berger, and Ami Pedahzur",
    venue: "Armed Forces & Society, 2021",
    links: [
      { label: "Google Scholar", url: "https://scholar.google.com/scholar?q=The+Human-Machine+Team+How+New+Technologies+Shape+the+Contemporary+Battlefield" }
    ]
  },
  {
    title: "The Posse and the Revolving Door: A New Dataset on Israeli Special Operations Units and Their Veterans in Politics",
    authors: "Guy D. Grossman and Ami Pedahzur",
    venue: "Terrorism and Political Violence, 2021",
    links: [
      { label: "Google Scholar", url: "https://scholar.google.com/scholar?q=The+Posse+and+the+Revolving+Door+A+New+Dataset+on+Israeli+Special+Operations+Units+and+Their+Veterans+in+Politics" }
    ]
  },
  {
    title: "Civil-Military Relations and Regime Stability in Arab Dictatorships",
    authors: "Guy D. Grossman and Ami Pedahzur",
    venue: "International Journal of Comparative Sociology, 2020",
    links: [
      { label: "Google Scholar", url: "https://scholar.google.com/scholar?q=Civil-Military+Relations+and+Regime+Stability+in+Arab+Dictatorships" }
    ]
  },
  {
    title: "The Triumph of Israel's Radical Right",
    authors: "Ami Pedahzur",
    venue: "Oxford University Press, 2012",
    links: [
      { label: "Google Scholar", url: "https://scholar.google.com/scholar?q=The+Triumph+of+Israel%27s+Radical+Right+Ami+Pedahzur" }
    ]
  }
];

function renderPublications() {
  const container = document.getElementById("publication-list");
  if (!container) return;

  container.innerHTML = publications
    .map((publication) => {
      const linksHtml = publication.links
        .map((link) => `<a href="${link.url}" target="_blank" rel="noopener noreferrer">${link.label}</a>`)
        .join("");

      return `
        <article class="pub-item">
          <h3>${publication.title}</h3>
          <p class="pub-meta">${publication.authors}</p>
          <p class="pub-meta">${publication.venue}</p>
          <div class="pub-links">${linksHtml}</div>
        </article>
      `;
    })
    .join("");
}

function activateReveal() {
  const revealItems = document.querySelectorAll(".reveal");
  if (!("IntersectionObserver" in window)) {
    revealItems.forEach((item) => item.classList.add("is-visible"));
    return;
  }

  const observer = new IntersectionObserver(
    (entries, obs) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          obs.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.15 }
  );

  revealItems.forEach((item, index) => {
    item.style.transitionDelay = `${Math.min(index * 70, 240)}ms`;
    observer.observe(item);
  });
}

function setYear() {
  const yearNode = document.getElementById("year");
  if (yearNode) {
    yearNode.textContent = String(new Date().getFullYear());
  }
}

renderPublications();
activateReveal();
setYear();
