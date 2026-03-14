const publications = [
  {
    title: "Territorial Control and the Militarization of Violent Non-State Actors: Transformation, Opportunities, and Vulnerabilities",
    authors: "Ofir Dayan and Ami Pedahzur",
    venue: "Studies in Conflict & Terrorism",
    year: "2025",
    type: "Journal Article",
    featured: true,
    summary:
      "Examines how territorial control changes the structure, capabilities, and weaknesses of violent non-state actors.",
    links: [
      { label: "DOI", url: "https://doi.org/10.1080/1057610X.2025.2528333" }
    ]
  },
  {
    title: "The Munich Massacre and the Proliferation of Counter-Terrorism Special Operation Forces",
    authors: "Ronit Berger and Ami Pedahzur",
    venue: "Israel Affairs",
    year: "2022",
    type: "Journal Article",
    summary:
      "Connects the Munich massacre to the international spread of specialized counter-terrorism units and doctrine.",
    links: [
      {
        label: "Google Scholar",
        url: "https://scholar.google.com/scholar?q=The+Munich+Massacre+and+the+Proliferation+of+Counter-Terrorism+Special+Operation+Forces+Pedahzur"
      }
    ]
  },
  {
    title: "Reconstructing the Theater of Terror",
    authors: "Matthew Sweeney, Arie Perliger, and Ami Pedahzur",
    venue: "Small Wars & Insurgencies",
    year: "2021",
    type: "Journal Article",
    summary:
      "Investigates the operational theater of terrorism and how spatial and organizational factors shape violent campaigns.",
    links: [
      {
        label: "Google Scholar",
        url: "https://scholar.google.com/scholar?q=Reconstructing+the+Theater+of+Terror+Sweeney+Perliger+Pedahzur"
      }
    ]
  },
  {
    title: "Can We Do Better? Replication and Online Appendices in Political Science",
    authors: "Jonathan Grossman and Ami Pedahzur",
    venue: "Perspectives on Politics",
    year: "2021",
    type: "Methods",
    summary:
      "Assesses replication practices and the quality of online appendices in political science research.",
    links: [
      {
        label: "Google Scholar",
        url: "https://scholar.google.com/scholar?q=Can+We+Do+Better+Replication+Online+Appendices+Political+Science+Grossman+Pedahzur"
      }
    ]
  },
  {
    title: "Political Science and Big Data: Why We Need Unstructured Big Data and How to Use It",
    authors: "Jonathan Grossman and Ami Pedahzur",
    venue: "Political Science Quarterly",
    year: "2020",
    type: "Methods",
    summary:
      "Argues for the use of unstructured big data in political science and outlines practical strategies for analysis.",
    links: [
      {
        label: "Google Scholar",
        url: "https://scholar.google.com/scholar?q=Political+Science+Big+Data+Unstructured+Grossman+Pedahzur"
      }
    ]
  },
  {
    title: "Counter-Cultures, Group Dynamics and Religious Terrorism",
    authors: "Arie Perliger and Ami Pedahzur",
    venue: "Political Studies",
    year: "2016",
    type: "Journal Article",
    summary:
      "Explores the interaction between group dynamics, counter-cultures, and the emergence of religious terrorism.",
    links: [
      {
        label: "Google Scholar",
        url: "https://scholar.google.com/scholar?q=Counter-Cultures+Group+Dynamics+Religious+Terrorism+Perliger+Pedahzur"
      }
    ]
  },
  {
    title: "Social Network Analysis in the Study of Terrorism and Political Violence",
    authors: "Arie Perliger and Ami Pedahzur",
    venue: "PS: Political Science and Politics",
    year: "2011",
    type: "Methods",
    summary:
      "Shows how social network analysis can reveal structure, diffusion, and hierarchy in violent organizations.",
    links: [
      {
        label: "Google Scholar",
        url: "https://scholar.google.com/scholar?q=Social+Network+Analysis+Study+Terrorism+Political+Violence+Perliger+Pedahzur"
      }
    ]
  },
  {
    title: "The Changing Nature of Suicide Attacks: A Social Network Perspective",
    authors: "Ami Pedahzur and Arie Perliger",
    venue: "Social Forces",
    year: "2006",
    type: "Journal Article",
    summary:
      "Uses a social network perspective to explain changes in suicide attack organization and execution.",
    links: [
      {
        label: "Google Scholar",
        url: "https://scholar.google.com/scholar?q=The+Changing+Nature+of+Suicide+Attacks+Social+Network+Perspective+Pedahzur+Perliger"
      }
    ]
  }
];

function renderPublications() {
  const container = document.getElementById("publication-list");
  if (!container) return;

  container.innerHTML = publications
    .map((publication) => {
      const linksHtml = publication.links
        .map(
          (link) =>
            `<a class="pub-link" href="${link.url}" target="_blank" rel="noopener noreferrer">${link.label}</a>`
        )
        .join("");

      const badges = `
        <div class="pub-badges">
          <span class="pub-badge">${publication.type}</span>
          <span class="pub-badge">${publication.year}</span>
        </div>
      `;

      const featuredClass = publication.featured ? " pub-item-featured" : "";
      const eyebrow = publication.featured
        ? `<p class="pub-eyebrow">Featured Work</p>`
        : "";
      const summary = publication.summary
        ? `<p class="pub-summary">${publication.summary}</p>`
        : "";

      return `
        <article class="pub-item${featuredClass}">
          ${eyebrow}
          <div class="pub-head">
            <div>
              <h3>${publication.title}</h3>
              <p class="pub-meta">${publication.authors}</p>
              <p class="pub-meta">${publication.venue}</p>
            </div>
            ${badges}
          </div>
          ${summary}
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
    { threshold: 0.12 }
  );

  revealItems.forEach((item, index) => {
    item.style.transitionDelay = `${Math.min(index * 80, 280)}ms`;
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
