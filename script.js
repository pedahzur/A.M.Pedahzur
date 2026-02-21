const publications = [
  {
    title: "Territorial Control and the Militarization of Violent Non-State Actors: Transformation, Opportunities, and Vulnerabilities",
    authors: "Ofir Dayan and Ami Pedahzur",
    venue: "Studies in Conflict and Terrorism, 2025",
    links: [
      { label: "DOI", url: "https://doi.org/10.1080/1057610X.2025.2528333" }
    ]
  },
  {
    title: "The Munich Massacre and the Proliferation of Counter-Terrorism Special Operation Forces",
    authors: "Ronit Berger and Ami Pedahzur",
    venue: "Israel Affairs, Vol. 28, No. 4, Pp. 625–637, 2022",
    links: [
      { label: "Google Scholar", url: "https://scholar.google.com/scholar?q=The+Munich+Massacre+and+the+Proliferation+of+Counter-Terrorism+Special+Operation+Forces+Pedahzur" }
    ]
  },
  {
    title: "Reconstructing the Theater of Terror",
    authors: "Matthew Sweeney, Arie Perliger, and Ami Pedahzur",
    venue: "Small Wars & Insurgencies, Vol. 32, No. 3, Pp. 469–489, 2021",
    links: [
      { label: "Google Scholar", url: "https://scholar.google.com/scholar?q=Reconstructing+the+Theater+of+Terror+Sweeney+Perliger+Pedahzur" }
    ]
  },
  {
    title: "Can We Do Better? Replication and Online Appendices in Political Science",
    authors: "Jonathan Grossman and Ami Pedahzur",
    venue: "Perspectives on Politics, Vol. 19, No. 3, Pp. 906–911, 2021",
    links: [
      { label: "Google Scholar", url: "https://scholar.google.com/scholar?q=Can+We+Do+Better+Replication+Online+Appendices+Political+Science+Grossman+Pedahzur" }
    ]
  },
  {
    title: "Political Science and Big Data: Why We Need Unstructured Big Data and How to Use It",
    authors: "Jonathan Grossman and Ami Pedahzur",
    venue: "Political Science Quarterly, Vol. 135, No. 2, Pp. 225–257, 2020",
    links: [
      { label: "Google Scholar", url: "https://scholar.google.com/scholar?q=Political+Science+Big+Data+Unstructured+Grossman+Pedahzur" }
    ]
  },
  {
    title: "Counter-Cultures, Group Dynamics and Religious Terrorism",
    authors: "Arie Perliger and Ami Pedahzur",
    venue: "Political Studies, Vol. 64, No. 2, Pp. 297–314, 2016",
    links: [
      { label: "Google Scholar", url: "https://scholar.google.com/scholar?q=Counter-Cultures+Group+Dynamics+Religious+Terrorism+Perliger+Pedahzur" }
    ]
  },
  {
    title: "Social Network Analysis in the Study of Terrorism and Political Violence",
    authors: "Arie Perliger and Ami Pedahzur",
    venue: "PS: Political Science and Politics, Vol. 44, No. 1, Pp. 45–50, 2011",
    links: [
      { label: "Google Scholar", url: "https://scholar.google.com/scholar?q=Social+Network+Analysis+Study+Terrorism+Political+Violence+Perliger+Pedahzur" }
    ]
  },
  {
    title: "The Changing Nature of Suicide Attacks: A Social Network Perspective",
    authors: "Ami Pedahzur and Arie Perliger",
    venue: "Social Forces, Vol. 84, No. 4, Pp. 1983–2004, 2006",
    links: [
      { label: "Google Scholar", url: "https://scholar.google.com/scholar?q=The+Changing+Nature+of+Suicide+Attacks+Social+Network+Perspective+Pedahzur+Perliger" }
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
