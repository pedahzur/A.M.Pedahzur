(() => {
  "use strict";

  const root = document.querySelector("[data-evidence-map-pilot]");
  if (!root) return;

  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

  const stages = {
    frame: {
      number: "01",
      label: "Frame the question",
      title: "Decide what the inquiry is trying to explain.",
      summary:
        "State the purpose, unit of analysis, provisional boundaries, and what the project will not attempt to answer.",
      decision:
        "Which question is specific enough to guide collection without foreclosing discovery?",
      artifact: "Question-framing worksheet",
      ai: "Challenge boundaries after the researcher has stated the purpose.",
      href: "03-frame.html",
    },
    decompose: {
      number: "02",
      label: "Decompose concepts and contexts",
      title: "Translate the question into dimensions that can be investigated.",
      summary:
        "Separate contested concepts, actors, periods, places, mechanisms, and observable traces.",
      decision:
        "Which dimensions must be clarified or observed before the question can be answered?",
      artifact: "Concept-and-context grid",
      ai: "Propose omitted dimensions and vocabulary; the researcher accepts, revises, or rejects each one.",
      href: "04-decompose.html",
    },
    sources: {
      number: "03",
      label: "Map source families",
      title: "Identify who could have recorded each dimension and why.",
      summary:
        "Connect dimensions to institutions, communities, archives, databases, and other source-producing systems.",
      decision:
        "Which independent source streams can illuminate or challenge each dimension?",
      artifact: "Source-family inventory",
      ai: "Suggest candidate source families, never assert that an archive or collection exists.",
      href: "05-map-source-families.html",
    },
    search: {
      number: "04",
      label: "Search iteratively",
      title: "Treat search as a documented cycle of learning.",
      summary:
        "Record routes, terms, dates, results, failures, citation chains, and revisions to the plan.",
      decision:
        "What did this search teach us about vocabulary, access, and the structure of the evidence?",
      artifact: "Search and AI audit log",
      ai: "Expand vocabulary and generate routes while preserving every consequential suggestion and rejection.",
      href: "06-search-iteratively.html",
    },
    evaluate: {
      number: "05",
      label: "Evaluate records and collections",
      title: "Assess relevance, provenance, dependence, and limits.",
      summary:
        "Separate what a source says from how it was produced, what it can support, and what remains uncertain.",
      decision:
        "What claim can this record support, and what should it not be asked to prove?",
      artifact: "Evidence register",
      ai: "Extract candidate metadata or tensions, followed by verification against the original source.",
      href: "07-evaluate.html",
    },
    coverage: {
      number: "06",
      label: "Test coverage",
      title: "Locate empty, weak, dependent, and contradictory cells.",
      summary:
        "Read across concepts and source families to distinguish abundance from genuine evidentiary coverage.",
      decision:
        "Where does the map rely on one stream, reproduce the same blind spot, or contain no usable evidence?",
      artifact: "Gap analysis",
      ai: "Challenge the map for repeated dependence and missing perspectives without declaring saturation.",
      href: "08-test-coverage.html",
    },
    freeze: {
      number: "07",
      label: "Freeze the evidence map",
      title: "Justify ending the present collection phase.",
      summary:
        "Assemble the records into a dated collection plan and a conditional stopping rule.",
      decision:
        "Why is the corpus adequate for the next analytical task, and what finding would reopen collection?",
      artifact: "Frozen evidence map and stopping rule",
      ai: "Stress-test the stated rule; only the researcher can authorize closure or reopening.",
      href: "09-produce-evidence-map.html",
    },
  };

  const stageButtons = [...root.querySelectorAll("[data-stage]")];
  const stagePanel = root.querySelector("#stage-detail");
  const stageNumber = root.querySelector(".stage-detail-number");
  const stageLabel = root.querySelector(".stage-detail-label");
  const stageTitle = root.querySelector(".stage-detail-copy h5");
  const stageSummary = root.querySelector(".stage-detail-summary");
  const stageDecision = root.querySelector('[data-stage-field="decision"]');
  const stageArtifact = root.querySelector('[data-stage-field="artifact"]');
  const stageAI = root.querySelector('[data-stage-field="ai"]');
  const stageLink = root.querySelector("[data-stage-link]");

  const selectStage = (key, moveFocus = false) => {
    const stage = stages[key];
    const selected = stageButtons.find((button) => button.dataset.stage === key);
    if (!stage || !selected) return;

    stageButtons.forEach((button) => {
      const isSelected = button === selected;
      button.classList.toggle("is-active", isSelected);
      button.setAttribute("aria-selected", String(isSelected));
      button.tabIndex = isSelected ? 0 : -1;
    });

    stagePanel.setAttribute("aria-labelledby", selected.id);
    stageNumber.textContent = stage.number;
    stageLabel.textContent = stage.label;
    stageTitle.textContent = stage.title;
    stageSummary.textContent = stage.summary;
    stageDecision.textContent = stage.decision;
    stageArtifact.textContent = stage.artifact;
    stageAI.textContent = stage.ai;
    stageLink.href = stage.href;

    if (!reducedMotion.matches) {
      stagePanel.classList.remove("is-updated");
      window.requestAnimationFrame(() => stagePanel.classList.add("is-updated"));
    }
    if (moveFocus) selected.focus();
  };

  stageButtons.forEach((button, index) => {
    button.addEventListener("click", () => selectStage(button.dataset.stage));
    button.addEventListener("keydown", (event) => {
      let nextIndex = null;
      if (event.key === "ArrowRight" || event.key === "ArrowDown") {
        nextIndex = (index + 1) % stageButtons.length;
      } else if (event.key === "ArrowLeft" || event.key === "ArrowUp") {
        nextIndex = (index - 1 + stageButtons.length) % stageButtons.length;
      } else if (event.key === "Home") {
        nextIndex = 0;
      } else if (event.key === "End") {
        nextIndex = stageButtons.length - 1;
      }
      if (nextIndex === null) return;
      event.preventDefault();
      selectStage(stageButtons[nextIndex].dataset.stage, true);
    });
  });

  const mapDetails = {
    question: {
      title: "Research question",
      copy: "The question organizes collection without presuming that one source family contains the complete or correct account.",
      status: "Anchor",
    },
    definition: {
      title: "Definition",
      copy: "Each system operationalizes terrorism differently. Inclusion rules must be compared before counts or trends can be interpreted.",
      status: "Mixed evidence",
    },
    coverage: {
      title: "Coverage",
      copy: "Temporal, geographic, linguistic, and media coverage vary. Missing events may reflect observation systems rather than the underlying pattern.",
      status: "Weak or missing",
    },
    institutions: {
      title: "Institutional purpose",
      copy: "Police, journalists, database coders, and scholars create records for different purposes. Those purposes shape what becomes visible.",
      status: "Strong context",
    },
    official: {
      title: "Official records",
      copy: "Administrative and legal records can be detailed, but access, jurisdiction, classification, and institutional incentives constrain them.",
      status: "Mixed evidence",
    },
    independent: {
      title: "Independent databases",
      copy: "Standardized coding makes comparison possible while introducing definitional thresholds, historical collection regimes, and source dependence.",
      status: "Strong, bounded",
    },
    news: {
      title: "News sources",
      copy: "Reporting supplies contemporaneous detail but varies with deadlines, language, access, editorial attention, and event salience.",
      status: "Mixed evidence",
    },
    scholarship: {
      title: "Scholarly research",
      copy: "Research offers explicit concepts and analytical comparison, yet it often inherits the coverage and coding choices of earlier source systems.",
      status: "Mixed evidence",
    },
    register: {
      title: "Evidence register",
      copy: "The register separates source content from provenance, relevance, dependence, limitations, and the claims each record may support.",
      status: "Reviewable record",
    },
    gaps: {
      title: "Gap analysis",
      copy: "The gap analysis marks empty, weak, dependent, or contradictory cells rather than treating a high document count as adequate coverage.",
      status: "Weak or missing",
    },
    stopping: {
      title: "Stopping rule",
      copy: "The rule explains why the present corpus can support the next task, what remains missing, and which discovery would reopen collection.",
      status: "Conditional closure",
    },
  };

  const filters = [...root.querySelectorAll("[data-map-filter]")];
  const nodes = [...root.querySelectorAll("[data-map-node]")];
  const mapTitle = root.querySelector("[data-map-detail-title]");
  const mapCopy = root.querySelector("[data-map-detail-copy]");
  const mapStatus = root.querySelector("[data-map-detail-status]");
  const canvas = root.querySelector(".evidence-map-canvas");
  const svg = root.querySelector(".evidence-map-edges");
  const svgNamespace = "http://www.w3.org/2000/svg";

  const inspectNode = (node) => {
    const detail = mapDetails[node.dataset.mapNode];
    if (!detail) return;
    nodes.forEach((candidate) => {
      candidate.classList.toggle("is-selected", candidate === node);
      candidate.setAttribute("aria-pressed", String(candidate === node));
    });
    mapTitle.textContent = detail.title;
    mapCopy.textContent = detail.copy;
    mapStatus.textContent = detail.status;
  };

  nodes.forEach((node) => {
    node.setAttribute("aria-pressed", "false");
    node.addEventListener("click", () => inspectNode(node));
  });

  const nodeMatchesFilter = (node, filter) => {
    if (filter === "all") return true;
    if (filter === "gap") return node.dataset.status === "gap";
    return node.dataset.layer === filter || node.dataset.layer === "question";
  };

  const drawEdges = () => {
    const canvasBox = canvas.getBoundingClientRect();
    svg.setAttribute("viewBox", `0 0 ${canvasBox.width} ${canvasBox.height}`);
    svg.replaceChildren();

    nodes.forEach((node) => {
      const connections = (node.dataset.connects || "").split(/\s+/).filter(Boolean);
      const nodeBox = node.getBoundingClientRect();
      connections.forEach((connection) => {
        const source = root.querySelector(`[data-map-node="${connection}"]`);
        if (!source) return;
        const sourceBox = source.getBoundingClientRect();
        const x1 = sourceBox.left + sourceBox.width / 2 - canvasBox.left;
        const y1 = sourceBox.bottom - canvasBox.top;
        const x2 = nodeBox.left + nodeBox.width / 2 - canvasBox.left;
        const y2 = nodeBox.top - canvasBox.top;
        const midpoint = y1 + (y2 - y1) / 2;
        const path = document.createElementNS(svgNamespace, "path");
        path.setAttribute("d", `M ${x1} ${y1} C ${x1} ${midpoint}, ${x2} ${midpoint}, ${x2} ${y2}`);
        path.classList.toggle(
          "is-dimmed",
          source.classList.contains("is-dimmed") || node.classList.contains("is-dimmed"),
        );
        svg.append(path);
      });
    });
  };

  const applyFilter = (filter) => {
    filters.forEach((button) => {
      const isActive = button.dataset.mapFilter === filter;
      button.classList.toggle("is-active", isActive);
      button.setAttribute("aria-pressed", String(isActive));
    });
    nodes.forEach((node) => {
      node.classList.toggle("is-dimmed", !nodeMatchesFilter(node, filter));
    });
    drawEdges();
  };

  filters.forEach((button) => {
    button.addEventListener("click", () => applyFilter(button.dataset.mapFilter));
  });

  let resizeFrame = null;
  window.addEventListener("resize", () => {
    if (resizeFrame) window.cancelAnimationFrame(resizeFrame);
    resizeFrame = window.requestAnimationFrame(drawEdges);
  });

  if (document.fonts?.ready) {
    document.fonts.ready.then(drawEdges);
  } else {
    drawEdges();
  }
  inspectNode(nodes[0]);
})();
