---
author:
- Ami Pedahzur
- Jonathan Grossman
date: 2026-07-12
status: revision-draft
subtitle: A Living Field Guide for Qualitative Research
title: From Question to Evidence
updated: 2026-07-27
---

# 1. From Question to Evidence

Nearly a decade ago, we began writing this book. We already had a workflow in mind. It began with the foundations of a research project: a bounded question, explicit concepts, and a record of the assumptions that shaped the inquiry. It then followed evidence through collection, structure, preservation, analysis, and a reproducible path from source to claim.

The information environment was already expanding faster than one researcher could absorb it. Search engines, digital archives, smartphones, and cloud storage made acquisition easier, but they did not make a large and heterogeneous corpus easier to reason about. The workflow exceeded the practical capacity of the available tools. What we were missing was processing power.

The recent arrival of large language models changed that constraint. They can propose concepts, generate search terms, compare excerpts, trace patterns, and expose gaps across a body of material in minutes. Yet power is not judgment. The same systems can invent a reference, erase a minority position, disclose protected material, or present an uncertain inference as settled fact. The method came first. Large language models now make parts of it executable at a scale we could only describe when the project began.

We have revived the project around one claim: a researcher needs an evidence map before the collection becomes too large to reason about. The map links a bounded question to concepts, source families, search decisions, evaluated records, known gaps, and a stopping rule. It does not promise omniscience. It makes the limits of collection visible.

The book treats this record as a scholarly Second Brain. Its purpose is not to store more material. It connects capture, organization, distillation, and expression to a visible chain of evidence. Each stage ends with an artifact that records a consequential choice. Taken together, those artifacts show how a question became a corpus, how the corpus became an analysis, and how the analysis became a claim.

The manuscript is written for two readers. The first is beginning a substantial qualitative project and needs a sequence that can be followed without assuming years of tacit experience. The second has conducted research for years but wants to reconsider established practices after the arrival of new search systems and generative AI. Both readers face the same decisions. They differ in how much explanation, contestation, and adaptation they require.

The full field guide follows a qualitative project from its first question to a documented corpus, an analysis, and a public claim. We are publishing it in reviewed modules so readers can use, test, and challenge each part before the first edition closes. The current revision contains two complete modules. The first follows the path from a question to an evidence map. The second carries the same logic into a literature review. A new synthesis chapter examines how review articles and meta-analyses are becoming open, versioned research objects. It also shows how reusable skills, bounded agents, and versioned project context can support discovery, gap analysis, methodology, and collection without transferring scholarly authority to the system. The first [Skills and Agents Lab](content/skills-and-agents-lab.qmd) release turns that argument into an inspectable literature-discovery skill, a read-only scout agent, a context template, synthetic benchmarks, and a public revision route. A second bridge chapter shows how AI can accelerate the construction of event databases while preserving provenance, validation, and causal discipline. A third complete module will connect the collection plan to a responsibly assembled research corpus. Later modules will address preparation, analysis, disconfirmation, writing, sharing, and maintenance.

The first worked example concerns competing accounts of terrorism. It suits the method because terrorism data do not arrive as neutral observations waiting to be counted. Definitions vary. Collection systems change. Sources disappear. Governments, news organizations, researchers, and database teams record different parts of the same event. The example is familiar to our own work. But the method must also survive evidence that researchers help produce. The revised book therefore adds a composite oral-history study of how tenants experienced and remembered municipal redevelopment. That case will carry interviews, consent records, field notes, administrative documents, researcher memos, silence, refusal, and unequal access through the same sequence of decisions.

AI enters the guide as an assistant whose work must be inspected. It may help generate candidate dimensions. It may suggest neglected source families. It may challenge a search strategy. It may compare the filled and empty cells of a map. It may not decide that a source exists, that a claim is true, or that collection is complete. Those remain scholarly judgments.

This is a field guide because research proceeds through decisions made under constraint. Time runs out. Archives close. Languages exceed the research team’s competence. Files vanish. Ethical obligations place some evidence beyond reach. A useful method does not conceal these conditions. It records them.

That record is the subject of this book.

# 2. Origins and Purpose

## 2.1 The First Version

The original project began nearly a decade ago with a practical frustration. We could see the workflow a qualitative project required, from its conceptual foundations through collection, structure, preservation, analysis, and a reproducible path from evidence to claim. But the available tools could manage only fragments of that chain. Researchers were being told that digital technology had democratized knowledge, and in an important sense it had. Search engines opened routes into literatures that once required proximity to a major library. Smartphones placed a camera, recorder, scanner, map, and notebook in one pocket. Cloud storage made files available across continents. Yet each gain created another decision that methods training rarely addressed.

What should be collected? How should it be named? Which metadata should travel with it? When should a record enter a reference manager, a qualitative analysis system, a spreadsheet, or an archive? What must remain linked to the original? What does a researcher do when the same event appears in five incompatible forms?

Our early drafts tried to answer these questions by following the research process. They moved from literature review to field collection, from unstructured material to a working database, and from analysis to public communication. Some passages remain useful. Others read like records of a vanished software market. Product descriptions aged faster than the methodological problems they were meant to solve.

This failure taught us something. A book organized around tools will inherit their expiration dates. A book organized around research decisions can survive them.

## 2.2 The New Pressure

Large language models supply some of the processing power the original workflow lacked. They change the scale of the problem, but not its nature. A researcher has always relied on aids to memory and classification. Indexes, catalogues, research assistants, codebooks, and bibliographies all extend individual capacity. The new systems differ in three respects. They respond in natural language. They infer patterns across large bodies of text. They produce answers whose fluency can hide the weakness of their evidentiary basis.

The practical temptation is easy to understand. A researcher facing two hundred articles may ask a model for the dominant themes. A scholar entering an unfamiliar archive may request names, dates, and likely repositories. A doctoral student may ask for missing literature. Each request can produce a useful lead. Each can also collapse the distinction between a plausible sentence and a supported claim.

The distinction matters because qualitative research depends on context that systems often discard. A phrase changes meaning when removed from the institutional conflict that produced it. An interview gains or loses force according to who conducted it, when it was recorded, and what the speaker had reason to conceal. An official document may describe an event precisely while omitting the actors excluded from the bureaucracy that created the record. Metadata is part of the evidence.

This is why provenance sits near the center of the revived project. Provenance records three things: the record itself, the activities that created or transformed it, and the agents responsible for those activities. These are the entities, activities, and agents of the W3C provenance model.[^1] It lets a reader ask what a record is, what produced or altered it, and who answered for each step. The model was built for data workflows. Social evidence adds questions it does not name, among them intent, silence, and power. The guide borrows the vocabulary as a heuristic, not a foundation. It does not require researchers to adopt a technical ontology. It requires them to preserve the questions that ontology makes explicit.

## 2.3 The Argument

We argue that disciplined collection rests on three commitments. A bounded question limits what enters the corpus. A map of the evidence that could bear on the question guides the search. A record of the decisions that shaped the corpus preserves the reasoning. Not every tradition accepts the first commitment in the same form. Grounded and interpretive projects often hold the question open longer, and the map and the record then travel with a question still in motion.

The three commitments correct different failures. Without a bounded question, collection expands by association. Without an evidence map, the most visible sources crowd out harder forms of evidence. Without a decision record, later readers cannot distinguish absence in the world from absence in the search.

No software can resolve these failures because none is technical alone. A search engine cannot decide whether a municipal ledger matters more than a minister’s memoir. A language model cannot determine whether repeated agreement indicates corroboration or common dependence on one wire report. A reference manager cannot explain why the research team stopped collecting one source family while continuing another.

The researcher must decide. The system should help preserve the decision.

The vocabulary of this guide carries a commitment. Words such as evidence, coverage, and gap assume that a collection can be more or less complete for a stated purpose, and that a reader can judge the difference. Strong interpretive and constructivist traditions contest that assumption. They treat a field’s categories as part of the phenomenon and resist measuring a corpus against the world. This guide does not claim to serve those traditions on their own terms. It offers a structure for making collection decisions visible, and it expects researchers in every tradition to adapt or reject the parts that do not fit their own.

## 2.4 A Guide with Two Speeds

The novice path makes tacit practice explicit. It explains why a decision matters, presents a worked example, supplies a structured exercise, and identifies common errors. The advanced sections address cases in which the simple procedure breaks down. Concepts remain contested. Teams classify the same source differently. Repositories impose incompatible metadata. Ethical limits create gaps that cannot be filled. The experienced reader can move quickly through the shared method and linger where these complications begin.

The two paths remain on the same page. We do not divide readers into permanent categories. An experienced ethnographer may be a novice in digital preservation. A doctoral student may possess deep knowledge of a language or archive that the senior investigator lacks. Expertise follows the task.

## 2.5 What This Draft Does

This project is a full living field guide published in reviewed modules. The current manuscript contains the first two. One moves from a question to an evidence map and collection plan. The other turns the scholarly source family into a literature corpus, synthesis, coverage audit, and stopping rule. Both use the same page pattern, preserve consequential decisions, and assign AI bounded roles.

These modules are the first tested layers of the book, not its final boundary. The next revision makes the guide’s epistemological position explicit, adds a composite oral-history case, and carries the collection plan into a documented research corpus. Later modules will address preparation, analysis, claim testing, writing, responsible sharing, and maintenance.

The manuscript also opens a conversation between the original authors. The information environment changed; the purpose remains recognizable. We wanted to help researchers work with greater discipline and less fear of abundance. We still do.

# 3. The Evidence Map

## 3.1 The Collection Problem

A folder can contain ten thousand documents and still fail to constitute a corpus. Quantity does not establish relevance. Storage does not create an argument. Search results do not explain what was missed.

An evidence map addresses this problem by placing the research question at the center of collection. Around it sit the concepts that require clarification, the actors and institutions that may have produced records, the periods and places that bound the inquiry, and the source families capable of answering different parts of the question. As collection proceeds, the map records where evidence accumulates and where it does not.

The term echoes the evidence gap map of systematic-review practice, a matrix of interventions against outcomes that shows where published findings are dense or thin. The evidence map here serves a different task. It charts not published findings but the sources that could bear on a single question, and it grows as the collection grows.

The map borrows the discipline of reproducible search reporting without treating every qualitative project as a systematic review.[^2] A historian cannot always specify the archive’s contents in advance. An ethnographer may revise the question after entering the field. A researcher working under authoritarian rule may withhold operational detail to protect participants. Transparency must answer to method and ethics.

The purpose is not mechanical replication. The purpose is reasoned reconstruction. The record is intended to let another scholar reconstruct how the inquiry moved, why some materials entered the corpus, why others did not, and where uncertainty remains.

## 3.2 The Seven Stages

The evidence map develops through seven stages. The first frames the question. The second decomposes it into concepts and contexts. The third identifies source families. The fourth conducts and records iterative searches. The fifth evaluates individual records and collections. The sixth tests coverage. The seventh turns the accumulated artifacts into a collection plan and stopping rule.

The sequence is ordered, but research rarely follows it once. A new archive may reveal an actor missing from the original question. A contradictory interview may expose a concept that was defined too narrowly. A failed search may show that a source family never existed. Each discovery sends the researcher backward. Revision is not evidence that the method failed. Revision is the method working.

The map therefore preserves versions. The question recorded on the first day does not disappear when the question changes. The source inventory does not overwrite a mistaken expectation. A rejected AI suggestion remains in the audit log with the reason for rejection. These records show how the project learned.

### 3.2.1 Seven-stage pathway

<table style="width:85%;">
<colgroup>
<col style="width: 84%" />
</colgroup>
<tbody>
<tr>
<td style="text-align: center;"><img src="media/rId23.png" style="width:5.83333in;height:2.5in" />
<p>Figure 3.1: The evidence map develops through seven ordered but revisable stages. Discoveries can reopen an earlier decision.</p></td>
</tr>
</tbody>
</table>

## 3.3 The Worked Example

Our running question asks why accounts of terrorism patterns diverge across official records, independent databases, news sources, and scholarly research. The question does not presume that one source class is correct and the others are mistaken. It asks how distinct systems produce different pictures of violence.

The problem begins with definition. A database must decide what counts as terrorism. It must translate that decision into inclusion criteria. It must then apply those criteria to sources created for other purposes. A news report seeks to describe an event under deadline. A police record serves an administrative or legal process. A scholarly database standardizes information across cases. Each source sees something. None sees everything.

Collection practices add another layer. The official documentation for the Global Terrorism Database describes a system built across several historical collection efforts and a codebook designed to let users apply different definitional thresholds.[^3] Research using that system has also shown why domestic and transnational events may require analytical separation and why changes in coding or source coverage matter.[^4] The point here is not to settle disputes about terrorism counts. It is to reveal the chain of decisions between event and claim.

This is the pattern. Evidence reaches the researcher through institutions.

## 3.4 What the Map Contains

The map exists in two states. A working map grows and changes from the first stage, as searches run and records accumulate. A frozen map, dated and set aside at the seventh stage, marks the end of a collection phase. The frozen map contains six connected records, and the seventh stage assembles them rather than adding a record of its own. The question frame defines the inquiry and its provisional boundaries. The concept-and-context grid translates the question into searchable dimensions. The source-family inventory identifies who could have recorded each dimension and where those records might reside. The search log records routes, terms, dates, results, and revisions. The evidence register assesses each record’s relevance, provenance, and limits. The gap analysis shows empty, weak, or contradictory parts of the map.

Two of these records form a matrix. The concept-and-context grid supplies the rows, the question’s dimensions. The source-family inventory supplies the columns. Each cell asks whether a dimension has been recorded by a given family, and with what quality. Coverage testing and gap analysis read these cells: which are filled, which are empty, and which rest on a single dependent source.

The stopping rule sits across all six. It states what conditions justify ending active collection for the present phase. It identifies what remains missing, why the missing material matters, and what would cause the search to reopen.

A stopping rule is not a declaration that nothing else exists. It is an argument that the present corpus can support the next analytical task.

## 3.5 The Role of AI

AI can assist at four points in this module. It can propose dimensions after the researcher frames the question. It can expand search vocabulary and candidate source families. It can challenge a search plan by adopting neglected perspectives. It can inspect a filled map for weak cells and repeated dependence on one source stream.

These uses share one condition: the system proposes, and the researcher disposes. A plausible archive name must be verified. A suggested source family must be examined for ethical and practical access. A proposed gap must be tested against the question rather than accepted because the model stated it fluently.

The guide records every accepted suggestion and every consequential rejection. This is not a clerical burden. It is evidence of judgment.

# 4. Stage 1: Frame the Question

## 4.1 Orientation

Research often begins with a subject rather than a question. Political violence, migration, educational inequality, and collective memory can sustain careers. They cannot direct a search. A subject has no internal stopping point. Every document leads to another period, actor, or debate.

Framing creates the first limit. It states what the researcher wants to explain or understand, the unit to which the question applies, the relevant setting, and the period under examination. The limit is provisional. It exists so the collection can begin with discipline.

Framing sets an intellectual limit, not an ethical clearance. Deciding what to collect does not decide whether collection is permitted. Some source families cannot be gathered at all without ethics approval, informed consent, or a data agreement, and those permissions govern whether the work may begin, not only how it proceeds. This guide defers the mechanics of collection to a later module, but the researcher should confirm the ethical preconditions before the search starts.

## 4.2 Learn

A workable qualitative question establishes an object of inquiry and a relation that requires evidence. “Terrorism databases” names an object. “Why do major terrorism databases report different patterns for the same period?” identifies a relation among classification systems, sources, and observed trends. The second formulation tells the researcher what must be compared.

The question must also expose its assumptions. “Why did the policy fail?” presumes failure before specifying the criterion. “How did officials and affected communities evaluate the policy’s effects between 2018 and 2022?” makes evaluation itself part of the inquiry. The revised question does not eliminate judgment. It identifies where the judgment enters.

State boundaries along five dimensions in running notes: phenomenon, place, period, actors, and outcome or meaning. Not every project needs a narrow value for each dimension. Comparative and transnational studies may require wide geographical scope. Historical research may follow consequences across decades. The researcher should still record what makes the boundary appropriate.

The frame includes exclusions. Exclusion is not dismissal. A study of policy formation may set aside implementation because the causal question concerns agenda access. A study of public memory may exclude private recollection that never entered a public forum. A source can be valuable and remain outside the present question.

## 4.3 Worked Example

Our initial subject is disagreement among accounts of terrorism. The first question might ask, “Which terrorism database is most accurate?” That formulation is attractive and weak. Accuracy depends on a definition of the event universe and on evidence against which records can be checked. The question also encourages a winner rather than an explanation.

We reframe it: “How do definitions, source systems, and collection procedures produce divergent accounts of domestic and transnational terrorism within the same period?” The new question identifies three possible mechanisms and one comparison. It leaves room for a database to perform well for one purpose and poorly for another.

The frame records a second decision. The module will examine the process through which events become records. It will not estimate a corrected global trend. That task requires data access, calibration choices, and a separate analytical design.

## 4.4 Try It

Write the present version of the question in one sentence. Then write a second sentence beginning with “This project does not attempt to.” The pair forces inclusion and exclusion into the same frame.

Next, state what would count as an answer. A causal question may require evidence of sequence and mechanism. An interpretive question may require competing meanings and the settings in which actors used them. A descriptive question may require a justified account of variation. If the anticipated answer cannot be described, the question remains too loose.

Save the result as this stage’s artifact, described under Save the Artifact below.

## 4.5 Guided AI Workflow

AI can serve as a critic of the frame. Provide the question and boundary statement without confidential material. Ask the system to identify hidden assumptions, ambiguous concepts, and plausible alternative formulations. Then ask it to explain how each alternative would change the evidence required. A usable prompt: “Identify hidden assumptions and ambiguous concepts in this question, and propose alternative formulations. Do not choose the best one.”

**Permitted input:** The question, the boundary and exclusion statement, and the stated purpose, with no confidential or participant-identifying material.\
**Do not provide:** Restricted archival detail, participant identities, unpublished allegations, or partner-owned data.\
**Verify:** Test each suggested assumption, concept, or alternative against the project’s purpose and access constraints. The model lacks the study’s intellectual commitments; it cannot choose the question.\
**Record:** Log accepted changes, rejected changes, the reason for each, and the model and date.

Do not ask the model to choose the “best” question. Review each suggestion against the purpose of the study.

## 4.6 Integrity Checkpoint

Confirm before saving:

**No sensitive exposure:** the frame does not expose participant identities, restricted archival information, or unpublished allegations.\
**No question-begging definition:** no contested actor is defined in terms that decide the empirical question in advance.\
**Commitments separated:** the researcher’s normative commitments are distinguished from the evidence a descriptive or causal claim requires.

## 4.7 Save the Artifact

Save `question-framing-v0.1.docx`. Required fields are the question, purpose, unit of inquiry, boundaries along the five dimensions, exclusions, assumptions, and the evidence that would count as an answer. Date it. Link it to the project log and the later evidence map. The version number matters because later collection decisions will make sense only in relation to the question that guided them at the time. Later revisions create a new version rather than erase the first.

## 4.8 Advanced Practice

Some questions should remain open longer than this procedure implies. Ethnographic research may develop its focus through entry into a field. Archival discoveries may shift the relevant period or actor. Participatory research may require the community to redefine the problem. In these cases, framing is an explicit record of the current agreement, not a contract imposed on future evidence.

# 5. Stage 2: Decompose the Question

## 5.1 Orientation

A well-framed question can still hide several inquiries inside one sentence. Each noun may contain a dispute. Each verb may imply a mechanism. Each boundary may conceal variation. Decomposition makes those parts visible before the search engine makes its own choices for the researcher.

## 5.2 Learn

Begin with concepts. A project on radicalization, trust, resilience, or state capacity cannot search effectively until it records how the term is being used. The task is not to produce a final definition. It is to identify neighboring terms, competing definitions, observable expressions, and words used by the actors themselves.

Then identify context. Time changes institutions and vocabulary. Place changes jurisdiction and source access. Actors occupy positions that shape what they can observe and what they have reason to record. Events create documentary traces, but those traces differ according to the organizations present.

Finally, identify rival explanations and negative cases. A question about technological change may need to consider organizational reform, political pressure, or altered reporting rules. A project that collects evidence only for its favored explanation will produce a dense archive and a weak inference.

Decomposition works through a grid. Rows represent dimensions of the question. Columns record working definitions, synonyms, actor language, likely evidence, rivals, and exclusions. The cells need not be filled before searching. Empty cells are useful. They show where the project is reasoning from habit rather than evidence.

## 5.3 Worked Example

The worked question contains several terms that require separation. “Terrorism” is a contested category. “Domestic” and “transnational” may refer to the location of an attack, the identity of perpetrators, the nationality of victims, organizational ties, or movement across borders. “Divergent accounts” may mean different event totals, different classifications, or different interpretations of the same underlying record.

The decomposition also reveals institutional actors. Database designers define variables. Coders interpret reports. News organizations decide which events merit coverage. Governments classify incidents for administrative, legal, and political purposes. Researchers transform published data through exclusions, recoding, and aggregation.

Research has shown why separating domestic and transnational incidents can change the question being answered.[^5] The value of the example lies less in the resulting series than in the conceptual work required to produce it.

A fragment of the grid shows the work.

| Dimension | Working definition | Actor language | Likely evidence | Rival or exclusion |
|----|----|----|----|----|
| Terrorism | Violence by non-state actors for political aims | terrorism, extremism, insurgency, armed struggle | Inclusion criteria; codebooks; incident reports | Excludes state violence; rival: ordinary crime miscoded |
| Domestic vs. transnational | Whether actors, victims, or targets cross a border | domestic, international, home-grown | Coding of perpetrator and target nationality | Rival: reporting capacity, not real incidence, drives the gap |
| Divergent accounts | Differences in counts, classification, or interpretation | discrepancy, undercount, coding change | Cross-database comparison; codebook revisions | Excludes simple data-entry error |

The empty cells would matter as much as the filled ones.

## 5.4 Try It

Underline every substantive noun and verb in the question. For each term, write a working meaning, two alternatives, and one observable trace. Then identify actors who would use different language for the same phenomenon.

Add at least one rival explanation. If the project expects a rise in recorded events, ask whether reporting capacity changed. If it expects a shift in public attitudes, ask whether the survey instrument or sampling frame changed. If it expects institutional learning, ask whether staff replacement or external coercion could produce the same observation.

The exercise is complete when each important term has a research use rather than a dictionary definition. The grid should tell the researcher where a term would appear, who would use it, and what could make its apparent presence misleading.

## 5.5 Guided AI Workflow

Provide the framed question and the research purpose. Ask the model to separate concepts, contexts, actors, mechanisms, rival explanations, and negative cases. Require it to label each suggestion as a candidate rather than a fact. A usable prompt: “Separate this question into concepts, contexts, actors, mechanisms, and rival explanations. Label each as a candidate, and name one observable trace for each.”

**Permitted input:** The framed question, the research purpose, and the boundary statement, with no confidential or participant-identifying material.\
**Do not provide:** Restricted archival detail, participant identities, or partner-owned data.\
**Verify:** Check that each candidate follows from the question and can guide evidence collection. A broad category with no plausible evidentiary route does not enter the grid merely because it sounds inclusive.\
**Record:** Log accepted and rejected candidates, the reason for each, and the model and date.

Run a second prompt that assigns the model an adversarial task: identify dimensions omitted by the first decomposition. A third prompt can ask how the decomposition might differ from the standpoint of an actor poorly represented in official records.

## 5.6 Integrity Checkpoint

Concepts can reproduce official categories that the study should examine. They can also impose academic language that participants would reject. Confirm before saving:

**Whose vocabulary:** each term records whose language it represents.\
**No smuggled category:** no official or academic label has become the study’s own without examination.\
**Translation preserved:** every translated term keeps its original expression and the reason for the English gloss.

## 5.7 Save the Artifact

Save `concept-context-grid-v0.1.xlsx`. Give each row a stable identifier. Required columns are dimension, working definition, synonyms, actor language, likely evidence, rival explanations, and exclusions. These identifiers will connect later search terms, source families, and evidence records to the dimension they serve.

## 5.8 Advanced Practice

Team projects should decompose the question independently before reconciling their grids. Early agreement can conceal shared assumptions. Independent drafts expose differences in training, language, and field knowledge. The reconciliation record should preserve disagreements that affect collection, even when the team adopts one operational definition.

# 6. Stage 3: Map Source Families

## 6.1 Orientation

Researchers often begin with the source they know how to find. Political scientists search articles and datasets. Historians enter catalogues. Sociologists recruit participants. Journalists search news archives. Expertise creates access. It also creates blind spots.

Source-family mapping asks a prior question: who could have observed, recorded, preserved, or later reconstructed each part of the inquiry?

## 6.2 Learn

A source family is a group of records produced through a related institutional process. Cabinet minutes form one family. Local newspapers form another. Oral histories, police files, organizational newsletters, court records, satellite images, social media posts, and scholarly databases each carry a production logic.

The family matters because records are not independent merely because they appear in different files. Ten articles may repeat one press release. Two databases may derive from the same news archive. A memoir and an oral-history interview may preserve the same retrospective narrative. Counting files can exaggerate corroboration.

For each dimension in the concept grid, identify prospective source families and the institutions that created them. Record what each family was designed to do, who could enter it, what it tended to omit, where it may be held, and what conditions govern access.

Mapping should include sources that challenge the project’s institutional center. Official records preserve the state well because the state creates records at scale. Marginalized actors may appear through legal proceedings, advocacy collections, private papers, community media, or testimony assembled after the event. Their relative scarcity is not evidence of lesser importance.

## 6.3 Worked Example

An incident of political violence can leave several traces. Local reporters may describe the event. Police may open a file. Hospitals may record casualties. A government may classify the incident. An organization may claim or deny responsibility. A database team may later code the event from published accounts. Researchers may then download the record and reorganize it for a new analysis.

Each trace answers a different question. A database can standardize events across time. It may be poorly suited to recovering local meaning. A court file may establish procedural facts while reflecting the categories of prosecution. A claim of responsibility may reveal strategic communication without proving operational control.

The official GTD documentation makes its inclusion criteria and data collection rules available to users.[^6] That transparency permits a researcher to map the system as a source family rather than treat each row as an unmediated event.

## 6.4 Try It

Take one row from the concept-and-context grid. Write the names of institutions and people who could have recorded it at the time. Then write who might have reconstructed it later. Separate contemporary from retrospective sources.

For each family, record five judgments in prose: what it can observe, why it creates records, who is absent, how records survive, and how access could distort the sample. Repeat the exercise until every important row has more than one plausible evidentiary route or an explicit explanation for why only one exists.

## 6.5 Guided AI Workflow

AI can generate candidate source families when the researcher supplies a concept, period, place, and actor set. Ask for institutional record types, vernacular sources, retrospective accounts, and material or visual traces. Require the model to state why each family might exist and why it might not. A usable prompt: “For this concept, period, and place, list candidate source families, including vernacular and retrospective ones. For each, state why it might exist, why it might not, and how to verify it.”

**Permitted input:** The concept, period, place, and actor set, with no sensitive source locations or participant identities.\
**Do not provide:** Restricted collection details, protected repository locations, or participant-identifying material.\
**Verify:** Confirm every named archive, collection, database, or repository through an official catalogue or institutional source. Fabricated repository names are a predictable failure.\
**Record:** Log candidate families accepted and rejected, the verification source, and the model and date. Keep fabricated suggestions as rejected rather than deleting them from the audit trail.

## 6.6 Integrity Checkpoint

Access conditions are part of the evidence map, but public disclosure can harm people and violate agreements. Confirm before saving:

**No sensitive detail exposed:** no source location, participant identity, or restricted collection detail entered an external model.\
**Abstraction where protected:** protected operational detail appears only in abstract description.\
**Access recorded:** each family’s access status and governing conditions are noted.

## 6.7 Save the Artifact

Save `source-family-inventory-v0.1.xlsx` with one row per family and links to the concept identifiers it may serve. Required fields are family, producing institution, repository, access status, language, temporal coverage, likely dependence on other families, and known silences.

## 6.8 Advanced Practice

Source families can change over time. A newspaper’s ownership, a ministry’s filing system, or a database’s collection vendor may shift within the study period. Treat a family as stable only after checking the institutions that produced it. Where the process changed, create separate records for each phase and mark the transition as part of the evidence.

# 7. Stage 4: Search Iteratively

## 7.1 Orientation

A search is not a box into which a finished question is typed. It is a sequence of encounters with the vocabulary and organization of a field. The first results teach the researcher how other actors named the subject. Those names alter the next search.

## 7.2 Learn

Begin with a search cycle rather than a master query. A cycle has a purpose, a route, a date, a set of terms, and a result. It ends with a decision: continue, revise, follow a lead, or stop using that route.

Search across systems because each system orders the world differently. Scholarly indexes privilege publications and citation relations. Archive catalogues describe collections through institutional finding aids. General search engines rank pages through opaque and changing systems. Library catalogues preserve controlled vocabularies. Human experts reveal sources that no public index exposes.

Record failures. A query that returns nothing may show that the vocabulary is wrong, the source is not digitized, the archive uses another name, or the record never existed. These possibilities have different consequences. “No results” is not yet “no evidence.”

Search reporting standards developed for systematic reviews offer a useful discipline: name the information source, preserve the search strategy, record dates, and explain how retrieved records were managed.[^7] Qualitative projects can adapt this discipline without claiming that every search can be reproduced exactly.

## 7.3 Worked Example

The terrorism example begins with official database documentation and the scholarship that has tested its classifications. It then moves backward toward originating sources and sideways toward competing databases, government records, and local reporting. Citation chaining identifies studies that transformed the data. Name and event searches reveal changes in terminology.

The log distinguishes a result derived from the database from a result that independently documents the event. This prevents a chain of later publications from being mistaken for multiple sources.

A fragment of the log shows three cycles for the database source family.

| Cycle | System | Terms | Result | Decision |
|----|----|----|----|----|
| 1 | GTD codebook and START site | inclusion criteria, domestic, transnational | Definitional thresholds and collection history located | Continue; extract coding rules |
| 2 | Scholarly index | GTD, coding change, undercount | Studies testing the classification retrieved | Follow citations backward |
| 3 | News archive | event name, place, date range | Contemporary report of a coded event | Retain as independent trace, not database-derived |

Each row records whether a result independently documents an event or derives from the database.

## 7.4 Try It

Run three short cycles for one source family. The first uses the researcher’s terms. The second uses language found in the first results. The third uses the vocabulary of an actor with a different institutional position. Write a short decision note after each cycle. Each note states one of four choices, with a reason: continue, revise the terms, follow a lead, or stop using the route.

## 7.5 Guided AI Workflow

Ask a model to expand candidate terms across historical names, acronyms, translations, institutional titles, and opposing actor vocabularies. The model can expand a query set. It cannot report what an index contains unless it has inspected the current index. A usable prompt: “Expand these search terms across historical names, acronyms, translations, and opposing actors’ vocabulary. Mark any proper noun I must verify.”

**Permitted input:** Concepts, existing search terms, and source-family names, with no protected information.\
**Do not provide:** Restricted archival detail, participant identities, or partner-owned data.\
**Verify:** Confirm every proposed proper noun before use, and test each term in an appropriate system.\
**Record:** Log terms that entered or left the query set, the query effect, and the model and date.

## 7.6 Integrity Checkpoint

Searches may reveal personal data, allegations, and material obtained outside its intended context. Discovery does not establish ethical permission to collect, analyze, or publish. Confirm before saving:

**Permission separate from discovery:** finding material is not treated as permission to collect or publish it.\
**Restrictions recorded at discovery:** any access or use restriction is noted at the moment the record is found.\
**Sensitive material quarantined:** personal data or allegations found in passing are set aside, not folded into the corpus without review.

## 7.7 Save the Artifact

Save `search-ai-audit-log-v0.1.xlsx`. Required fields for each cycle are date, system, purpose, exact terms, filters, result count when meaningful, records retained, new vocabulary, and next decision. Preserve exports when licensing permits.

## 7.8 Advanced Practice

Search ranking changes. Personalized systems may return different results to different users. Researchers working in teams should compare selected queries across accounts, locations, languages, and systems when ranking itself could shape the corpus.

# 8. Stage 5: Evaluate Evidence

## 8.1 Orientation

Collection answers “What did we find?” Evaluation asks “What can this record support?” The two questions should not collapse into one. A source can be relevant and unreliable for a specific claim. It can be accurate and still unrepresentative. It can be biased and indispensable.

## 8.2 Learn

Evaluate the record in relation to a claim. Authority alone is insufficient. A ministry may be authoritative about its own procedure and self-interested about its success. A participant may recall experience with precision and reconstruct chronology poorly. A database may standardize variables carefully while inheriting uneven news coverage.

Seven judgments belong in the evidence register. Relevance connects the source to a dimension of the question. Proximity describes its relation to the event or process. Provenance records who created and transformed it. Authority concerns competence and institutional position. Dependence identifies shared underlying sources. Representation asks whose experience enters the record. Preservation risk concerns whether the record can be checked later.

These judgments should remain separate. Combining them into one quality score hides the reason a source matters.

## 8.3 Worked Example

The Global Terrorism Database documents its methodology, inclusion criteria, and variables.[^8] That documentation makes evaluation possible. It does not make each observation equally certain. Event records depend on available sources, definitions, collection periods, and coding judgments.

Research that separates domestic and transnational incidents shows how analytical purpose can require transforming a published event universe.[^9] The transformed data may answer a new question. The transformation must remain visible.

One evidence-register entry for a single GTD event record shows the seven judgments.

| Judgment | Assessment for one GTD event record |
|----|----|
| Relevance | Bears on the divergent-accounts dimension: shows how one event is coded |
| Proximity | Retrospective; coded from published reports, not observed directly |
| Provenance | Created by GTD coders from news sources; transformed through the codebook |
| Authority | Authoritative on GTD coding rules, not on the ground truth of the event |
| Dependence | May share an originating wire report with database and news entries |
| Representation | Reflects events that reached English-language reporting; local silences likely |
| Preservation risk | Stable while START hosts the release; version and access date recorded |

The entry keeps the judgments separate rather than collapsing them into one score.

## 8.4 Try It

Select one source that appears strong and one that appears weak. Write what each can establish, what it cannot establish, and which other source family could test it. Then identify whether the two sources depend on the same originating report.

## 8.5 Guided AI Workflow

Provide a source description and the intended claim, not confidential full text. Ask the model for questions about provenance, dependence, missing actors, and temporal distance. Treat the output as an evaluation checklist. Do not ask for a verdict on credibility. A usable prompt: “Given this source description and the claim I want to make, list questions about provenance, dependence, missing actors, and temporal distance. Do not judge credibility.”

**Permitted input:** A source description and the intended claim, with no confidential full text or participant identities.\
**Do not provide:** Restricted full text, participant-identifying material, or protected collection details.\
**Verify:** Answer each question against the source itself and the source-family inventory. The model raises questions; it does not rate credibility.\
**Record:** Log which questions changed the evaluation, and the model and date.

## 8.6 Integrity Checkpoint

Evaluation can reproduce status hierarchies. Official sources should not receive an automatic presumption of truth, and participant testimony should not be romanticized as unmediated access. Confirm before saving:

**No automatic authority:** no source is trusted by rank alone; each is tied to a claim.\
**Position stated:** the source’s institutional position is recorded beside the use made of it.\
**Judgments kept separate:** the seven judgments are not collapsed into a single quality score.

## 8.7 Save the Artifact

Save `evidence-register-v0.1.xlsx` with one entry per record or coherent collection. Required fields are the seven judgments (relevance, proximity, provenance, authority, dependence, representation, preservation risk), plus links to the source-family inventory, the search cycle, the relevant concept, and any restriction on use.

## 8.8 Advanced Practice

Teams should calibrate judgments through difficult examples rather than pursue artificial agreement on every record. Preserve reasoned disagreement when it affects interpretation. Consensus can erase uncertainty that belongs in the final analysis.

# 9. Stage 6: Test Coverage

## 9.1 Orientation

Researchers stop collecting for many reasons. A deadline arrives. Access closes. New searches repeat old results. The corpus seems sufficient. These reasons should not be disguised as one claim that the evidence is complete.

## 9.2 Learn

Coverage testing compares the developing corpus with the dimensions and source families on the map. Look for empty cells, thin cells, dependent cells, contradictory cells, and cells filled by one institutional perspective. A large number of records can conceal weak coverage when they repeat one source stream.

The language of saturation has several meanings and does not fit every qualitative tradition.[^10] Information power offers another way to reason about adequacy: a focused aim, specific material, strong dialogue with the evidence, theoretical support, and an intensive analytic strategy can reduce the amount required.[^11] These ideas concern sampling and analysis. An evidence map adapts them cautiously to documentary collection.

Track information yield. A search cycle has high yield when it adds a new source family, changes a definition, reveals a rival explanation, fills an important gap, or alters the interpretation of existing evidence. Yield declines when new records repeat known information from the same underlying sources.

## 9.3 Worked Example

A terrorism corpus may contain thousands of event records while remaining thin on coding changes, local reporting gaps, or the institutional reasons that one event entered the database and another did not. Coverage testing shifts attention from event totals to the process that produced them.

A fragment of the coverage matrix marks dimensions against source families.

| Dimension (row) / family (column) | Scholarly database | Local reporting | Government records |
|----|----|----|----|
| Event counts | Adequate | Thin | Dependent on database |
| Coding changes | Thin | Empty | Empty |
| Local meaning | Empty | Thin | Contradictory |

Thousands of records can leave whole rows empty. A dependent cell repeats a source already counted elsewhere.

## 9.4 Try It

Mark each evidence-map cell as empty, thin, adequate for the present claim, contradictory, or inaccessible. Write one sentence defending every “adequate” judgment. Then rank the unresolved cells by their likely effect on the argument.

## 9.5 Guided AI Workflow

Provide a redacted summary of the map. Ask the model to identify repeated dependence, absent actor perspectives, unsupported comparisons, and claims resting on one source family. A usable prompt: “From this summary of an evidence map, identify repeated dependence, absent perspectives, and claims resting on a single source family.”

**Permitted input:** A redacted summary of the map, with no participant identities or protected locations.\
**Do not provide:** The evidence itself, restricted records, or protected collection detail.\
**Verify:** Check each observation against the actual register. A model with web or retrieval access may consult sources you cannot see; treat its inputs as unverified.\
**Record:** Log which observations changed the gap analysis, and the model and date.

The model sees the summary supplied to it, not the evidence, unless the tool has retrieval access. When the map cannot be summarized without exposing protected material, run this stage without the model.

## 9.6 Integrity Checkpoint

Some gaps should remain. Ethical restrictions, participant safety, legal obligations, and community agreements can make collection improper. Confirm before saving:

**Protected gaps marked:** gaps that ethics or agreements require are recorded as protected, not as failures.\
**Overlooked gaps separated:** a gap left by oversight is distinguished from one left by principle.\
**No pressure to fill:** no protected gap is filled to improve apparent coverage.

## 9.7 Save the Artifact

Save `gap-analysis-v0.1.xlsx`. Required fields are the cell (dimension and source family), status (empty, thin, adequate, dependent, contradictory, or inaccessible), priority, consequence, proposed action, access constraint, and decision date. A later researcher should be able to distinguish an overlooked gap from a known limit.

## 9.8 Advanced Practice

Contradiction is not a defect to eliminate. It may reveal distinct institutional views, temporal change, strategic deception, or differences in measurement. The map should preserve disagreement until the analysis explains why it exists.

# 10. Stage 7: Produce the Evidence Map

## 10.1 Orientation

The final stage does not end research. It converts collection from accumulation into a reasoned plan. The map now shows what the project asks, what evidence bears on it, where the corpus is weak, and what further work is worth its cost.

## 10.2 Learn

Assemble the six prior artifacts without flattening them into one table. The question frame supplies boundaries. The concept grid supplies dimensions. The source inventory supplies possible record-producing institutions. The search log supplies routes and revisions. The evidence register supplies claim-specific judgments. The gap analysis supplies uncertainty and priority.

The collection plan assigns the next action to each important gap. Search further, seek access, consult an expert, add language competence, triangulate, narrow the claim, or accept the limit. Every action has a reason and a review date.

The stopping rule states when active collection ends for the present phase. It should refer to coverage of important dimensions, diversity of source families, declining information yield, treatment of rivals and negative cases, unresolved contradictions, and practical or ethical constraints. It should also state what new evidence would reopen collection.

## 10.3 Worked Example

The terrorism map may support a claim about how database procedures create divergent accounts while remaining unable to adjudicate the true global number of events. That is an acceptable result. The map narrows the claim to what the evidence can bear.

The stopping rule might close active collection after the main methodological periods are documented, competing classification systems are represented, important transformations are traced, and new searches yield only dependent repetition. It would reopen if a new codebook, originating archive, or independent event series became available.

## 10.4 Try It

Write the strongest claim the present corpus can support. Write the strongest claim it cannot support. Then draft the stopping rule in one paragraph that names both evidence and limits.

## 10.5 Guided AI Workflow

Ask the model to attack the stopping rule. Require it to identify unsupported confidence, neglected rivals, circular dependence, and vague language. Revise only after checking the critique against the map. A usable prompt: “Attack this stopping rule. Identify unsupported confidence, neglected rivals, circular dependence, and vague language.”

**Permitted input:** The stopping rule and a redacted summary of coverage, with no protected records.\
**Do not provide:** The evidence itself, restricted records, or protected collection detail.\
**Verify:** Check each objection against the map before revising. An objection is a prompt to reexamine, not a verdict.\
**Record:** Log which objections changed the stopping rule, and the model and date.

## 10.6 Integrity Checkpoint

Do not convert inaccessible evidence into presumed support. Do not treat silence as absence without examining the record-producing institution. Do not present a practical deadline as methodological sufficiency. Confirm before saving:

**No presumed support:** inaccessible evidence is not counted as if it agreed.\
**Silence examined:** an absence is traced to the record-producing institution before it is read as evidence.\
**Constraint named:** a deadline or access limit is stated as itself, not as sufficiency.

## 10.7 Save the Artifact

Save `evidence-map-stopping-rule-v1.0.xlsx`, a dated release that links the six prior artifacts rather than flattening them: the question frame, concept grid, source-family inventory, search log, evidence register, and gap analysis, together with the collection plan and stopping rule. Preserve editable working files and a stable review copy. Link the release to the question version it answers.

## 10.8 Advanced Practice

In team projects, the map becomes an instrument of governance. It assigns responsibility, records disagreements, and makes handoffs possible. The map should not become a surveillance device for counting activity. Its unit is a research decision, not an hour worked.

# 11. Literature as Evidence

## 11.1 The Review Problem

A literature review can contain hundreds of summaries and still fail as research.[^12] The failure occurs when selection, purpose, relationships, and exclusions remain unexplained. Accumulation is not synthesis. A long bibliography proves that material was found; it does not show that the material was assembled into an argument.

Discovery now returns more publications and citation paths than one person can follow. Generative systems add fluent accounts without necessarily revealing their basis. Abundance lowers the cost of finding *something* and raises the cost of explaining why the selected literature is adequate.

This module treats scholarly literature as evidence. A publication can provide evidence of a concept’s history, a theoretical dispute, an empirical pattern, a methodological choice, or the way a community has organized a problem. It can also repeat an unsupported claim, inherit a classification from an earlier source, exclude cases through its research design, or become influential for reasons that have little to do with evidentiary strength. Reading literature as evidence means asking of a publication many of the questions we ask of an interview, archival record, or dataset: Who produced it? For what purpose? From which materials? Through which transformations? What can it support, and what remains beyond its reach?

The aim is not suspicion for its own sake. It is to make the relation between a review and its claims inspectable.

## 11.2 From Evidence Map to Literature Corpus

The evidence map identifies scholarship as one source family. This module turns that family into a literature corpus whose composition and limits the researcher can explain.

Scholarly literature performs several jobs at once. It supplies concepts, explanations, methods, cases, and source leads. A work may define a concept, establish a historical baseline, provide a method, or matter because later authors repeatedly cite it. Treating all four as generically “relevant” obscures the work each performs.

The module uses four distinctions:

- A **bibliography** records publications and the information needed to retrieve them.
- A **reading list** orders publications for learning or teaching.
- A **literature corpus** is the bounded set of works selected for a stated research purpose.
- A **synthesis** explains patterns, disputes, lineages, methods, and absences across that corpus.

These objects overlap but are not interchangeable. The protocol and search log explain how the corpus was assembled; the matrix and memo show how it became an account of the field.

## 11.3 The Six Stages

The first stage defines the review.[^13] It states what the review must accomplish, which question it answers, which boundaries guide inclusion, and which exclusions remain provisional. A review designed to clarify a concept will not collect or read in exactly the same way as one designed to identify a causal explanation or compare methods.

The second stage maps concepts and vocabulary. Search systems retrieve strings, while researchers care about meanings. The same phenomenon may travel under different names across periods, languages, and disciplines. The same term may refer to incompatible concepts. A vocabulary map does not resolve those disputes in advance. It makes them searchable.

The third stage discovers publications through multiple routes. Database queries provide one route. Backward and forward citation chaining provide others. Author, institution, journal, handbook, review-article, and targeted web searches reveal work that an initial query can miss. Each route has a different selection mechanism. Recording the route helps distinguish a diverse search from repeated dependence on the same index.

The fourth stage evaluates sources and claims. Evaluation asks whether a work bears on the review question, what evidence supports its claims, how its methods shape what it can see, what lineage it inherits, and what role it should play in the eventual synthesis. Venue and citation counts can provide context. They cannot substitute for reading.

The fifth stage reads, annotates, and compares. Notes preserve the difference between an author’s claim, the material offered in support, and the reviewer’s interpretation. A synthesis matrix then reorganizes those notes across works. The unit of thought shifts from “What does this article say?” to “What do these works reveal about this concept, mechanism, case, or dispute?”

The sixth stage synthesizes, audits, and stops. Synthesis builds an account across sources. Audit looks for disciplinary, linguistic, geographical, methodological, and citation-network distortions. The stopping rule explains why active searching can end for the present task, what remains missing, and what would cause the review to reopen.

The sequence is recursive. New vocabulary, a shared citation lineage, or an empty matrix cell can reopen an earlier stage. Preserve earlier versions because they show how the review learned.

## 11.4 Two Worked Examples

The primary example continues our inquiry into terrorism databases. Scholars define categories, select data, transform events, and cite earlier decisions. A review that records conclusions without tracing those choices risks treating constructed categories as found facts.

The secondary example follows a researcher studying how a municipal housing agency changed its treatment of informal settlements between the 1970s and the 1990s. The relevant scholarship is dispersed across urban history, public administration, planning, law, and local-language publications. Terminology changes across the period: the people, places, and administrative practices are not described consistently. Digitization is uneven. The example shows why absence from a database is not evidence of absence from scholarship, and why a review can become narrower than its question without the researcher noticing.

## 11.5 The Artifact Chain

Five resources connect the workflow: review protocol, concept-and-vocabulary map, search-and-AI log, source-evaluation register, and synthesis-and-stopping workbook.

Stable identifiers connect concepts, searches, sources, claims, and synthesis cells. They prevent the prose from becoming detached from the record that produced it.

## 11.6 The Role of AI

AI can generate vocabulary, transform researcher-written notes into a provisional table, compare entries across a matrix, and audit the review for missing perspectives. It can do these tasks quickly because the researcher supplies a bounded object and a defined operation. It becomes less reliable when asked to “review the literature” without a corpus, a purpose, or a verification rule.

The division of labor is simple. The system may propose. It may reorganize. It may point to possible inconsistencies. The researcher decides which publications enter the corpus, reads the works that carry argumentative weight, verifies every citation and quotation, and writes the synthesis. A model output is a lead or transformation record, not a scholarly source unless the model itself is the object of study.

The audit log records consequential assistance rather than every keystroke. Document AI actions that could change the corpus or the claims drawn from it.

# 12. Stage 1: Define the Review

## 12.1 Orientation

A review begins to drift when its purpose remains implicit. “I need to know the literature” sounds responsible but supplies no rule for deciding what to find, read, compare, or leave outside. The researcher alternates between fear of missing a canonical work and fascination with whatever appeared most recently. Every reference opens another branch. Because the task has no defined answer, it has no defensible stopping point.

Define the review before searching. The definition is provisional, just as the research question is provisional, but it should state what the review must enable the researcher to do. It converts reading from an aspiration into an inquiry.

## 12.2 Learn

Begin by naming the review’s function.[^14] Most reviews supporting empirical projects combine several functions, but one should lead.

A **conceptual review** clarifies how a term has been defined, contested, measured, or used in practice. A **theoretical review** compares explanations, mechanisms, or expectations. An **empirical review** establishes what is known about a phenomenon, population, case, period, or relationship. A **methodological review** examines how research designs, sources, instruments, or analytical procedures shape findings. An **orienting review** helps a researcher enter an unfamiliar field and learn its central questions, lineages, and vocabulary. A review may also justify a new study by showing a consequential limitation or unanswered question. “Finding a gap,” however, is too weak as a purpose on its own. A gap matters only when filling it could change understanding.

Turn the function into a review question. “The literature on terrorism databases” names a collection. “How have scholars explained divergence among terrorism databases, and what roles do definitions, source systems, and coding procedures play in those explanations?” names an analytical task. The review question should be narrower than the book or dissertation question because literature is only one source family. It should also state what kind of answer the review will produce: a taxonomy, a comparison, a causal account of intellectual change, an assessment of evidence, or a set of propositions to test.

Next define boundaries. Relevant dimensions include period of publication, period studied, geography, language, discipline, publication type, population, method, and evidentiary threshold. These are not filters to apply mechanically. They are decisions to justify. A review of contemporary municipal governance might include historical studies because present administrative categories emerged earlier. A review conducted in English may need local-language search routes if the institutions under study operate elsewhere. A dissertation chapter may include unpublished doctoral work when it contains the only close examination of a particular archive, while treating its status explicitly.

Write inclusion and exclusion logic as sentences, not only as filter settings. “Include publications that compare at least two event datasets or examine how terrorism events are defined, sourced, or coded” tells a reader why a work belongs. “Exclude works that use a single dataset without discussing its construction” identifies a defensible limit. The excluded work may remain important to the larger project; it simply does not answer this review question.

Separate substantive exclusions from practical constraints. Being outside scope differs from remaining unread because of access, language, or time. The first defines the corpus; the second may bias it.

State the anticipated product, audience, deadline, collaborators, and threshold for full-text reading. A dissertation section and a review article require different depth. The protocol makes later changes visible.

## 12.3 Worked Example

For the terrorism-database inquiry, the initial purpose combines conceptual, methodological, and empirical functions. We want to understand how scholars define divergence, what explanations they offer, and how their own data choices affect the patterns they report. We are not attempting a complete review of terrorism research or a ranking of every database.

The review question becomes: “How has research since the expansion of event-based terrorism datasets explained divergent counts and patterns, and what evidence supports claims about the effects of definitions, sources, and coding?” We include comparative database studies, methodological articles on event-data construction, validation studies, codebook analyses, and empirical articles that demonstrate a consequential change caused by database choice. We exclude studies that merely name a database in the methods section. They may later enter the project as evidence of usage, but they cannot answer the present review question.

Both protocols record language and access constraints and assign reopening triggers.

## 12.4 Try It

Write a one-sentence review question. Under it, complete four prompts:

1.  “This review will enable me to…”
2.  “A work belongs when…”
3.  “A work remains outside when…”
4.  “The review will be adequate for its purpose when…”

Then list the boundaries you expect to use and label each one **substantive**, **ethical**, or **practical**. A substantive boundary follows from the question. An ethical boundary protects people or restricted information. A practical boundary reflects time, access, language, or resources. Do not hide the third category inside the first.

Write what would change the protocol, such as a new historical term, revised period, or added language capacity. These are version triggers.

The exercise is complete when another researcher can apply the inclusion logic to three sample publications and explain their decisions. Agreement is not required. If the protocol cannot support a reasoned disagreement, it remains too vague.

## 12.5 Guided AI Workflow

Use AI as a protocol critic, not as an authority on the field. Give the system the review question, purpose, boundaries, and inclusion/exclusion statements. Ask it to identify hidden assumptions, ambiguous terms, boundary conflicts, and types of scholarship that the protocol may systematically miss. Request alternative formulations and require an explanation of how each would change the corpus.

**Permitted input:** The review protocol, public project description, and invented examples.\
**Do not provide:** Confidential peer-review material, restricted research plans, participant information, or unpublished allegations.\
**Verify:** Test every suggested boundary or publication type against the research purpose and an independently verified example. The model’s claim that a field uses a term is not evidence that it does.\
**Record:** Save suggestions that change scope, inclusion logic, language coverage, or the anticipated product. Record rejected consequential suggestions and the reason for rejection.

A useful prompt ends with a required table: assumption; why it matters; possible revision; effect on evidence required; verification action. The structure makes proposals easier to inspect. Do not ask the model to select the “best” protocol. That choice depends on the project’s intellectual commitments and constraints.

## 12.6 Integrity Checkpoint

Scope can encode bias while appearing neutral. Language limits may remove scholarship produced by the communities being studied. Date limits may privilege contemporary terminology. Journal-only rules may exclude books in fields where books carry central arguments, or reports in fields where institutions produce the relevant evidence. Citation thresholds can exclude new work and scholarship outside dominant networks.

Review protocols also create strategic temptations. A researcher may define inclusion after seeing which works support the preferred argument. Versioning does not prohibit change; it distinguishes learning from retrospective tailoring. Date the initial protocol, state why it changed, and preserve both versions.

Copyright and access deserve separate attention. A paywall is not evidence of low relevance. An illegally obtained copy does not become safe to redistribute because it supports open scholarship. Record access barriers and seek lawful routes through libraries, authors, repositories, or interlibrary services.

## 12.7 Save the Artifact

Save `literature-review-protocol-v0.1.docx`. Required fields are project ID, review question, leading function, secondary functions, anticipated product, audience, boundaries, inclusion logic, exclusion logic, languages, publication types, discovery routes to be attempted, full-text threshold, AI/data restrictions, practical constraints, initial stopping rule, reopening triggers, date, author, and reviewer.

Link the protocol to the evidence map and project log. When it changes, create version 0.2 and add a short change note. Do not overwrite the reasoning that governed earlier searches.

## 12.8 Advanced Practice

Some reviews cannot specify all inclusion criteria in advance. An interpretive review may discover that the field’s categories are part of the phenomenon under study. A critical review may deliberately trace how a dominant vocabulary excluded alternative traditions. A realist synthesis may refine its program theory while searching. In these cases, the protocol should define the process of adaptation rather than pretend that the final boundaries existed at the start.

Team reviews should calibrate inclusion rules on a shared small set before scaling. Living reviews also require monitoring routes, maintenance ownership, and conditions for a new synthesis.

# 13. Stage 2: Map Concepts and Vocabulary

## 13.1 Orientation

Researchers ask questions in concepts; search systems retrieve representations of words. Between the two sits a translation problem. A well-framed review can still retrieve a distorted literature if the query uses only the researcher’s preferred term. Older scholarship may use a discarded label. Another discipline may study the same process under a different name. A local-language literature may divide one English concept into several terms. Conversely, a familiar word may collect incompatible meanings and flood the search with false matches.

The concept-and-vocabulary map turns this problem into an explicit research task. It links what the researcher means to the terms that different authors, institutions, periods, and systems may use.

## 13.2 Learn

Start with the concepts in the review question, but do not treat them as settled.[^15] For each concept, record a working meaning, rival meanings, observable implications, and exclusions. The working meaning is a provisional guide, not a definition imposed on every source. A literature review often needs to discover how the concept has changed.

Build several vocabulary families around each concept:

- **Preferred terms** are the labels used in the current review.
- **Synonyms and near-synonyms** identify alternative labels while noting differences in meaning.
- **Broader and narrower terms** connect the concept to categories above and below it.
- **Historical terms** capture labels used during earlier periods, including terms now considered inaccurate or offensive.
- **Disciplinary terms** record how neighboring fields formulate the issue.
- **Actor terms** preserve the vocabulary used by institutions, participants, or communities.
- **Translations and transliterations** record language variants, scripts, spelling systems, and false equivalents.
- **Acronyms, abbreviations, and names** capture institutional and technical shorthand.
- **Exclusion terms** reduce recurring irrelevant results without erasing genuinely ambiguous uses.

Do not collapse these entries into one undifferentiated synonym list. A historical administrative label is not equivalent to a community’s self-description. A legal category may resemble a social-scientific concept while carrying a different threshold. Those differences belong in the map because they may later explain disagreements in the literature.

Vocabulary comes from several places. Begin with the research question and a small orientation set: a recent handbook chapter, authoritative review, known foundational work, codebook, glossary, or policy document. Extract terms from titles, abstracts, keywords, subject headings, indexes, and the vocabulary authors use when disagreeing. Search promising terms and inspect what they retrieve. New results supply new vocabulary. The map and the search therefore develop together.

Controlled vocabulary can connect inconsistent language but represents a cataloguing system whose coverage varies. Record the heading and system. Treat names as concepts when institutions, programs, places, or authors have consequential variants.

The map should also preserve relationships. Mark terms as equivalent, overlapping, nested, opposed, historically successive, actor-specific, or contested. These relations help construct queries and later interpret results. If two terms are only partially overlapping, searching them with `OR` broadens retrieval but does not make them conceptually identical.

## 13.3 Worked Example

The terrorism review begins with apparently stable terms: *terrorism*, *event data*, *domestic*, *transnational*, *database*, *dataset*, *coding*, and *validation*. Each quickly divides.

Research may distinguish terrorism from insurgency, guerrilla violence, hate crime, state repression, or armed conflict, while particular datasets include or exclude boundary cases differently. *Domestic* may describe the nationality of perpetrators and victims, the location of an event, the target’s identity, or the absence of foreign involvement. *Event data* appears alongside incident data, conflict events, political violence data, and machine-coded events. Validation may mean checking events against sources, comparing datasets, measuring coding reliability, or assessing whether a variable captures a theoretical construct.

The vocabulary map records these as contested relations rather than interchangeable strings. A query cycle might join `(terror* OR political violence)` with `(database* OR dataset* OR event data)` and `(valid* OR compar* OR coverage OR coding)`, then test narrower terms learned from relevant works. The researcher records which additions improve retrieval and which create noise. A model’s suggestion to add *benchmark* may be useful in computational work but less so in historical validation; the map keeps that decision visible.

In the municipal case, agency names and settlement labels change across periods and actors. The map connects terms to period, actor, language, and evidentiary risk so historical vocabulary can support retrieval without becoming the researcher’s unmarked description.

## 13.4 Try It

Choose three concepts central to the review. For each, create entries for working meaning, at least two rival meanings, one broader term, one narrower term, two disciplinary or actor terms, relevant historical terms, translations, and exclusions. If a category does not apply, record why rather than leaving an unexplained blank.

Select one orientation source and trace its vocabulary. Highlight the terms used in the title and abstract, the keywords supplied by the author, subject headings supplied by an index, and alternative terms used in the body. Mark who supplied each term. This small exercise shows how a publication receives several layers of description.

Construct three query variants from the map:

1.  a precise query using the preferred term and one methodological term;
2.  a broad query using synonyms, historical terms, or disciplinary variants;
3.  a boundary query designed to find neighboring concepts that may challenge the review’s definition.

Run the queries in one appropriate system. Sample the results rather than collecting everything. Record which kinds of work each query reveals, which irrelevant literatures appear, and which new terms deserve another cycle. Revise the map, retaining the earlier version.

## 13.5 Guided AI Workflow

AI can accelerate vocabulary expansion when it is given a defined concept and asked to separate kinds of terms. Provide the working meaning, period, setting, disciplines, and languages. Ask for candidate historical labels, disciplinary variants, actor vocabulary, translations, acronyms, and neighboring concepts. Require a reason for each candidate and a proposed way to verify actual usage.

**Permitted input:** Public definitions, verified excerpts, project scope, languages, and non-sensitive example queries.\
**Do not provide:** Restricted archival descriptions, participant language that could identify a person, unpublished peer-review text, or entire copyrighted works.\
**Verify:** Confirm every candidate term in a source created by the relevant field, actor, institution, or period. Test the term in an appropriate search system and inspect results.\
**Record:** Log terms that enter or leave the map, the model and date, the verification source, query effect, and the researcher’s decision.

Ask the system to flag false friends and semantic drift rather than merely translate. A literal translation may be linguistically correct and absent from the field. A term used today may not have existed during the period under study. A model can propose these risks; it cannot establish historical usage without sources.

A second pass can ask for terms associated with a neighboring discipline or affected community. Treat the output as a coverage challenge, never as a substitute for scholarship or testimony from that community.

## 13.6 Integrity Checkpoint

Vocabulary is never merely technical. Labels can stigmatize, legitimize, or erase. Preserve historically necessary terms with context and quotation marks when appropriate. Distinguish the language used to find a source from the language used to describe people in the manuscript.

Search vocabulary can also reproduce disciplinary hierarchy. Terms familiar to dominant English-language journals may crowd out local conceptual traditions. Translation into English can make distinct categories appear equivalent. Record the original-language term beside the translation and note whether equivalence is exact, approximate, contested, or unknown.

Do not optimize only for recall. Adding every imaginable synonym can produce a corpus so noisy that selection becomes opaque. Each term needs a relation to the concept and a reason for inclusion. Exclusion terms require equal care: removing a word to reduce noise may also remove a relevant minority usage.

## 13.7 Save the Artifact

Save `literature-concept-vocabulary-map-v0.1.xlsx`. Assign stable concept IDs and term IDs. Required concept fields are working meaning, rival meanings, boundaries, observable implications, period, setting, and linked review-question component. Required vocabulary fields are term, language, script or transliteration, term type, actor or discipline, period of use, relation to concept, verification source, query tested, retrieval effect, decision, and notes on responsible usage.

Link every consequential query in the search log to the relevant term IDs. When a term changes the corpus, preserve the map version that preceded the change. The provenance of the term matters: a candidate proposed by a model and verified in an archival thesaurus has a different history from a subject heading copied from a database.

## 13.8 Advanced Practice

Concept formation may be the review’s central analytical task rather than a preliminary step. In that case, do not force all works into a single definition. Build a definition matrix that compares attributes, extension, cases included and excluded, causal role, normative content, and measurement. Track lineages: which authors adopt, modify, or reject earlier definitions? The resulting map can reveal that an apparent empirical disagreement is conceptual, or that verbal disagreement hides similar case boundaries.

Multilingual teams should calibrate concepts, not only translate queries, and record non-equivalence as a finding. Stable IDs and explicit relations usually suffice; formalize the map only for a real downstream task.

# 14. Stage 3: Discover Through Multiple Routes

## 14.1 Orientation

No single discovery route reveals “the literature.” A database query retrieves records covered by that database, described in the fields it indexes, and matched by the query at that moment. Citation chaining follows relationships created by authors and indexing systems. An author search follows careers. A handbook follows an editor’s map of a field. Each route makes some scholarship visible and leaves other scholarship in shadow.

Discovery becomes more defensible when routes are combined and recorded. The aim is not to search everywhere. It is to understand how each route selects and to use complementary routes for the review’s purpose.

## 14.2 Learn

Begin with a small orientation set rather than a massive download. Select a recent authoritative review or handbook chapter, one or two known foundational works, and a work close to the empirical setting. Read enough to learn the field’s vocabulary, main disputes, cited lineages, relevant publication types, and likely indexes. Orientation sources are maps, not automatic members of the final corpus.

Use **structured database searching** when bibliographic fields and repeatable queries matter. Record the system, collection or index, date, exact query, fields searched, filters, result count, and records retained. A query copied from one system may behave differently in another because field codes, stemming, phrase handling, subject vocabularies, and coverage differ. Preserve the executed form rather than an idealized description.

Use **backward citation chaining** to inspect the works a relevant publication cites.[^16] This route can reveal concepts, methods, datasets, and disputes that predate the vocabulary used in the query. It can also reproduce the author’s exclusions. Follow references selectively and record why a cited work appears promising.

Use **forward citation chaining** to find later works that cite a relevant publication. This route shows uptake, criticism, replication, application, or ceremonial citation. A citing work may mention the source without engaging its argument. Screen the citation context when possible.

Use **author and institution tracing** when a research program, laboratory, archive, public agency, or data-producing organization shapes the field. Search name variants, affiliations, project pages, series titles, and successor institutions. This route is especially important when outputs include reports, documentation, working papers, or datasets that journal indexes handle unevenly.

Use **venue browsing** when indexing is incomplete, while recognizing that it overrepresents one scholarly community.

Use **targeted web discovery** for institutional publications, repositories, conference programs, preprints, data documentation, and hard-to-index material. Record the domain, query, date, and access status. General web ranking is personalized and unstable; save enough metadata to retrieve the item independently.

Discovery proceeds in cycles.[^17] Each cycle has a purpose: test a concept, locate a lineage, fill a geographical gap, follow a method, or challenge a suspected consensus. Screen enough results to decide whether the route is productive. Retain records with a reason, not because downloading is easy. At the end of the cycle, record new vocabulary, new source types, duplications, and the next decision.

Deduplicate at the work level while linking preprint, conference, accepted, and published versions. Do not count manifestations as independent evidence.

## 14.3 Worked Example

The terrorism review begins with an orientation set: database codebooks, a methodological comparison, and an empirical study whose findings depend on the domestic/transnational distinction. From these works we learn terms such as *event data*, *inclusion criteria*, *source coverage*, *duplicate events*, *classification*, and *validation*. We also identify data-producing institutions and earlier collection projects.

The first database cycle combines terrorism terms with dataset and validation terms. It retrieves direct comparisons but also many articles that validate predictive models rather than data construction. We record that ambiguity and refine the methodological vocabulary. A second cycle searches the names and acronyms of major datasets with terms for coding, coverage, and bias. A third follows references from comparison studies to codebooks and earlier critiques. Forward chaining shows whether documented limitations were later addressed, repeated, or ignored.

The routes reveal that several later articles repeat one methodological source. The search log marks the shared lineage rather than treating repetition as independent confirmation.

For the municipal agency, backward chaining reveals a former agency name; a local catalogue then uncovers dissertations and reports, while legal journals reveal a tenure vocabulary absent from planning queries. Each route corrects another’s selection mechanism.

## 14.4 Try It

Plan three discovery cycles, each with a different route and purpose. For example:

1.  a structured query to test the current concept vocabulary;
2.  backward and forward chaining from one anchor work;
3.  author, institution, venue, or repository tracing to address a known coverage risk.

Before running a cycle, write what success would look like. A cycle may succeed by finding relevant works, exposing a vocabulary problem, showing that a route is exhausted, or revealing that the expected literature does not exist in that form. “More results” is not a sufficient criterion.

For every retained record, assign a provisional source ID and one retention reason: concept, theory, empirical finding, method, lineage, context, critique, or source lead. Use “uncertain” only with a next action. Sample rejected records and record the recurring rejection reasons. This helps determine whether the query is poorly calibrated or the corpus boundaries are working.

At the end, identify where routes converged and where the search depends on a single index or citation lineage. Mark that area as a coverage risk for Stage 6.

## 14.5 Guided AI Workflow

AI can help design and audit search routes when it operates on verified vocabulary and source metadata. Provide the review question, concept map, attempted routes, and a list of verified anchor works. Ask for candidate query variations and complementary routes. Require the system to state which coverage risk each proposal addresses.

**Permitted input:** Public bibliographic metadata, verified search terms, route summaries, and non-sensitive project boundaries.\
**Do not provide:** Licensed full text in violation of terms, confidential manuscripts, private reviewer comments, credentials, or participant data.\
**Verify:** Run proposed queries in the named system; independently verify every title, author, DOI, repository, and dataset. Reject invented or untraceable items.\
**Record:** Save consequential query proposals, route suggestions, dates, model/version, executed forms, result effects, accepted and rejected recommendations, and verification actions.

Do not ask a model for “the ten most important sources.” Importance depends on the review purpose, and the response may reproduce popularity, language, and training-data biases. A safer task is: “Given these attempted routes, propose three *types of route* that might reveal scholarship selected by a different mechanism. Do not provide publication titles.” The researcher can then search those routes directly.

When a model does propose citations, quarantine them in a candidate table. Nothing enters the bibliography or source register until it resolves to an authentic record and has been screened against the protocol. Fluency does not lower the verification threshold.

## 14.6 Integrity Checkpoint

Discovery systems observe users. Queries may reveal sensitive topics, populations, locations, or intentions. Use institutional or privacy-preserving access where appropriate, and do not paste sensitive project descriptions into external services merely to improve convenience.

Access affects visibility. Scholarship behind paywalls, in print, in other languages, or outside major indexes is more expensive to discover. Do not translate cost into quality. Record inaccessible items and the lawful steps attempted to obtain them. If access limitations cluster by region, language, or publication type, treat that as a potential bias in the corpus.

Citation networks encode social structure as well as intellectual relevance. Highly connected works become easier to find and then more likely to be cited again. Forward chaining can amplify prestige. Backward chaining can reproduce canonical exclusions. Complement citation routes with searches designed around cases, actors, concepts, and venues outside the dominant network.

Automated bulk retrieval may violate platform terms or overload services. Follow access rules, rate limits, and copyright restrictions. The fact that a script can download material does not establish permission to do so or to redistribute it.

## 14.7 Save the Artifact

Save `literature-search-ai-log-v0.1.xlsx`. The Search Routes sheet should include cycle ID, date, purpose, route type, system or repository, exact query or action, fields, filters, result count, screened count, retained source IDs, rejection pattern, new vocabulary, coverage risk, decision, and next step.

The Citation Chaining sheet should include chain ID, seed source ID, backward or forward direction, candidate citation, citation context, authenticity check, relevance decision, shared-lineage warning, and resulting action. The AI Audit sheet should include model/version, task, input description, protected data status, output summary, accepted and rejected suggestions, verification, reviewer, and decision.

Export or save search histories when systems permit, but keep the human-readable log. Platform exports can become unreadable when subscriptions or interfaces change.

## 14.8 Advanced Practice

Complex reviews benefit from route-level sampling. Instead of screening an unbounded result set, define a reproducible slice appropriate to the route: all results through a date, the first fixed number under a documented sort order, or all citations linked to an anchor work. Explain the trade-off. Ranking-based samples are convenient but inherit opaque ranking systems.

Research librarians can improve recall and documentation. Record who designed and checked each strategy. Living reviews should separate the multi-route baseline from monitoring and version both.

# 15. Stage 4: Evaluate Sources and Claims

## 15.1 Orientation

Discovery produces candidates, not authorities. A publication can be relevant to the question and weak support for a claim. It can be methodologically rigorous and irrelevant to the present review. It can be widely cited because it supplied a memorable label, a convenient dataset, or a position that later scholars reject. Evaluation separates these dimensions before prestige or familiarity turns them into one vague judgment of “quality.”

The purpose is not to assign every publication a universal score. It is to decide what work a source can responsibly perform in this review.

## 15.2 Learn

Evaluate first for **relevance**. Identify which review-question component, concept, case, method, or dispute the work addresses. Relevance can be direct or contextual. A direct source analyzes database divergence. A contextual source may explain how news production shapes the reports on which databases depend. Record the relation rather than relying on a tag called “relevant.”

Then identify **publication context and provenance**. Who wrote the work, in what role, for which audience, and through what review or editorial process? Is it a journal article, scholarly book, chapter, dissertation, report, working paper, preprint, codebook, commentary, or correction? Publication type affects expectations but does not decide value. A codebook may be the primary source for a dataset’s stated rules. A peer-reviewed article may be necessary to test whether those rules were applied as intended.

Move to the **claim level**. What does the author claim? Is the claim descriptive, conceptual, causal, interpretive, normative, or methodological? What evidence supports it? Which cases, sources, observations, or data transformations connect the evidence to the claim? A single publication often contains several claims with different support. Evaluating the work as one unit can hide that variation.

Assess **method-claim fit**. A close archival study may provide strong evidence about sequence and institutional meaning in one case but weak evidence for prevalence across cases. A large database comparison may show systematic differences but say little about how a particular event was recorded. An interview study may reveal actors’ interpretations while requiring care about retrospective memory and selection. The question is not whether one method is superior. It is whether the method can support the claim for which the review will use it.

Record **source dependence**. Authors may cite the same dataset, document collection, press archive, or foundational claim. Apparent agreement across publications can arise from common input. Trace citations when a proposition carries considerable argumentative weight. If five works repeat a statistic from one report, the review has one evidentiary origin and five instances of uptake.

Identify **limitations and uncertainty** as reported by the author and as observed by the reviewer. Preserve the difference. “The authors note that source coverage changes after 1997” is not the same as “we infer that the reported trend may reflect coverage change.” Both can be useful if attributed correctly.

Finally, assign an **intended role** in the synthesis. Possible roles include definition, theoretical proposition, empirical support, counterevidence, method, historical context, lineage, boundary case, source lead, or limitation. A work may have several roles, but each should point to a specific claim or section.

Metrics enter only after these judgments. They vary by field, age, language, document type, and index. Influence and validity are different variables.

## 15.3 Worked Example

Consider an article reporting that domestic and transnational terrorism follow different temporal patterns. Its relevance is direct because the review concerns divergent accounts and definitional choices. At the claim level, however, the article does several things. It defines categories, decomposes event records, estimates trends, and interprets the differences. Each step depends on the database’s inclusion criteria and on the operational rule used to classify domestic and transnational events.

The source-evaluation register therefore creates separate claim entries. One records the conceptual distinction and its rationale. Another records the empirical pattern, data source, period, and transformation. A third records the causal or policy interpretation. The article may strongly support the existence of different patterns within its operationalization while providing less support for the claim that the categories represent distinct causal processes. The review can use the first without silently adopting the third.

Now suppose several later studies cite the empirical pattern. We inspect whether they reproduce the analysis, apply it to another dataset, or cite the result as settled background. The source register marks shared dependence. Agreement in prose does not automatically become independent corroboration.

## 15.4 Try It

Select five candidates from at least two discovery routes. For each, write one sentence answering each question:

1.  Which part of the review question does this work bear on?
2.  What are its two most consequential claims for this review?
3.  What evidence and method support each claim?
4.  What can the design not establish?
5.  Which earlier source, dataset, or classification does it depend on?
6.  What role might it play in the synthesis?

Then compare the five works without using citation counts or venue rankings. Rank neither the authors nor the publications. Instead, group claim entries by the kind of support they offer. Only after that exercise, add publication context and influence indicators. Note whether the new information changes an intended role and why.

Trace one repeated proposition back a citation step and read the cited passage. Record qualification loss, miscitation, or common dependence.

## 15.5 Guided AI Workflow

AI can help normalize researcher-written evaluation notes and expose missing fields. Supply a fixed schema and notes derived from works you have read. Ask the system to separate author claims, evidence, methods, author-stated limitations, reviewer inferences, and proposed synthesis roles. Require it to quote only text included in the prompt and to mark absent information as unknown.

**Permitted input:** Your own notes, public abstracts, short lawfully quoted excerpts, verified bibliographic metadata, and a blank evaluation schema.\
**Do not provide:** Full copyrighted texts without permission, confidential manuscripts, identifiable participant material, or notes whose disclosure violates agreements.\
**Verify:** Compare every populated field with the publication and your notes. Confirm that author claims and reviewer interpretations remain distinct. Independently verify citations and metrics.\
**Record:** Save model/version, input description, schema, output, corrected fields, consequential classifications, reviewer, and final decision.

A useful prompt forbids global scores and flags unsupported fields, shared sources, and roles that exceed the method. The answers remain hypotheses until checked against the publications.

Do not ask a model to evaluate a work from its title or abstract. Abstracts are selective representations designed to communicate contribution. They rarely provide enough information to judge evidence, transformations, limitations, or citation dependence.

## 15.6 Integrity Checkpoint

Evaluation can become a disguise for status judgment. Researchers may treat unfamiliar venues, regions, languages, methods, or institutional authors as inherently weak. Apply the same claim-level questions to every source while retaining relevant differences in publication process and conflicts of interest.

Do not punish transparency. Record stated uncertainty as guidance for interpretation, not an automatic negative score.

Conflicts of interest and institutional position matter when they bear on source production. A database team’s methods article is indispensable for understanding stated procedures and may also have an interest in defending the project. An advocacy report may provide unique evidence and a normative purpose. Position does not erase evidence; it shapes the questions asked of it.

Avoid laundering unsupported claims through citation. If a statement matters to the synthesis, verify that the cited source supports it. If the source cannot be obtained, label the claim as second-hand or exclude it from load-bearing prose.

## 15.7 Save the Artifact

Save `literature-source-evaluation-v0.1.xlsx`. The Source Register should include source ID, complete citation, version, source type, publication context, discovery route, review-question linkage, full-text status, method, evidence base, population or cases, period, declared limitations, conflicts or position, dependence, intended roles, reviewer, date, and decision.

The Claim Register should include claim ID, source ID, claim type, accurate paraphrase, page or location, supporting evidence, transformation or analytical step, author qualification, reviewer assessment, linked concept IDs, related or dependent claim IDs, synthesis role, and verification status.

Do not place long copyrighted passages in the workbook. Use short quotations only when necessary for precision and record page numbers. Keep the source file in its lawful location and link through a stable source ID.

## 15.8 Advanced Practice

Team evaluation benefits from claim-level calibration on a shared small set. Compare extracted claims and roles, then revise ambiguous rules before scaling.

Use formal appraisal tools only when they fit the claims and design. Computational reviews should preserve seed sets, thresholds, validation samples, errors, and versions; relevance scores are system outputs, not source properties.

# 16. Stage 5: Read, Annotate, and Compare

## 16.1 Orientation

The easiest literature notes to write are often the hardest to use. A page of prose beginning “Smith argues…” may preserve an article’s order while doing little for the reviewer’s question. When every note mirrors one publication, the eventual review tends to become a procession of authors. The reader learns that Smith said one thing and Jones said another, but not what the disagreement concerns, which evidence separates them, or how the field changed.

Reading for synthesis requires two linked records: a faithful source note and a comparison structure that reorganizes information across sources. The first protects accuracy. The second enables analysis.

## 16.2 Learn

Read in passes. Screen for identity, relevance, version, and role; analyze claims, evidence, method, and relations; then verify passages and locations that will carry the synthesis.

Start each source note with retrieval and version information. Record the source ID, complete citation, file or lawful location, version, date read, and reviewer. Preprints and published versions may differ. Pagination can change. A stable record prevents later quotations from pointing to the wrong manifestation.

Within the note, distinguish four voices:

1.  **Author:** an accurate account of what the work claims.
2.  **Evidence:** the material and analytical steps offered in support.
3.  **Reviewer:** your interpretation, questions, and assessment.
4.  **Relation:** agreements, disputes, dependencies, or contrasts with other works.

Use explicit labels or separate fields. Without them, a critical observation written beside a paraphrase can later be mistaken for the author’s admission. This is especially dangerous when notes are transformed by software or AI.

Annotate selectively. Highlighting everything records attention, not meaning. Each annotation should have a function tied to the review: definition, mechanism, empirical pattern, case, method, source lead, limitation, counterevidence, quotation candidate, or synthesis connection. A small controlled set of annotation types improves retrieval; free-form memos preserve ideas that do not fit the scheme.

After reading, write a source memo stating contribution, strongest support, important limit, and the work to which it should be compared.

Then move information into a **synthesis matrix**. Rows usually represent works or claim IDs. Columns represent questions that cut across them: concept definition, mechanism, cases, period, evidence base, method, finding, limitation, lineage, or another dimension derived from the review protocol. The right columns depend on the intended synthesis. A matrix for concept formation will differ from one comparing causal explanations.

Cells should be concise and traceable. Include a claim ID or page location. Do not paste whole abstracts. Empty cells are informative: the source may not address the dimension, the information may be unavailable, or the reviewer may not yet have read the relevant section. Use explicit states such as not addressed, not reported, not yet checked, inaccessible, or not applicable.

Comparison produces **analytic memos**. Ask what patterns appear across columns. Which differences follow method, period, case selection, definition, or source base? Which works appear to disagree only because they answer different questions? Which share a conclusion but rely on one lineage? Memos capture these emerging relations without pretending that the final synthesis is settled.

## 16.3 Worked Example

In the terrorism review, the matrix columns include definition of terrorism, domestic/transnational rule, event unit, database or source system, period, handling of ambiguous cases, analytical transformation, reported divergence, explanation, and limitation. One article compares aggregate counts. Another validates individual events. A third decomposes domestic and transnational series. Their findings cannot be placed in a single “result” column without losing the level at which each comparison occurs.

The source notes preserve this difference. The aggregate article claims that trends diverge after a particular date and supports the claim with time-series comparison. The validation study reports mismatched events found through record linkage and source checking. The decomposition study shows that a combined series conceals different dynamics under its classification rule. A synthesis memo observes that “database divergence” names at least three problems: universe coverage, event matching, and category construction. The literature becomes more intelligible when those problems are separated.

The matrix also exposes dependence. Several works describe historical collection changes using the same documentation. Their cells receive different source IDs but the same dependence marker. The synthesis can report broad acknowledgment of the issue while avoiding the claim that multiple independent studies established it.

## 16.4 Try It

Choose six evaluated works that differ in route, method, period, or position. Create a source note for each with the four voices distinctly marked. Limit the initial source memo to four sentences: contribution, support, limit, comparison.

Design five to eight matrix columns from the review question. Before filling the matrix, write what each column means and what an acceptable cell contains. Add explicit missing-value states. Populate the matrix from your notes, including source or claim IDs.

Read by column. Write three analytic memos:

- one pattern or convergence that survives comparison;
- one apparent disagreement that may be caused by definition, method, period, or case selection;
- one silence, dependence, or empty cell that requires another search or closer reading.

Return to two publications and verify the passages on which the memos depend. Revise the matrix if the comparison overstated what an author claimed. This return is essential: abstraction increases the risk of losing qualification.

## 16.5 Guided AI Workflow

AI can transform structured notes into a provisional matrix or compare populated cells. It should not read unseen publications on the researcher’s behalf. Provide a fixed schema, source IDs, and notes whose author/evidence/reviewer/relation voices are already separated. Ask the model to populate only supported fields, preserve identifiers, and mark uncertainty.

**Permitted input:** Researcher-authored notes, short verified excerpts, bibliographic metadata, source/claim IDs, and the blank matrix schema.\
**Do not provide:** Full copyrighted publications without permission, confidential manuscripts, restricted archives, identifiable participant information, or mixed notes whose attribution is unclear.\
**Verify:** Compare every populated cell and proposed pattern with the source notes and, for load-bearing claims, the publication. Check quotations, page locations, negation, attribution, and qualifications.\
**Record:** Save the schema, model/version, input description, output, corrected cells, accepted patterns, rejected patterns, reviewer, and decision date.

A second prompt can flag reviewer inferences, false independence, and patterns resting on one source. These audit questions do not grant the system authority to resolve them.

Do not ask the model to write the final review from the matrix. The matrix is a compressed representation. It omits rhetoric, context, uncertainty, and many source details. Drafting directly from it can turn analytical shorthand into unsupported certainty.

## 16.6 Integrity Checkpoint

Notes can expose copyrighted text, confidential arguments, peer-review identities, or sensitive source descriptions. Store them according to the most restrictive material they contain. A collaborative matrix should not become an accidental redistribution channel.

Compression can also create epistemic harm. Removing qualifiers may make a cautious finding appear universal. Combining historically offensive actor language under a neutral category may hide how classification operated. Preserve meaningful wording and context where the language itself is evidence.

AI transformation introduces another source of error: attribution drift. A model may merge the author’s claim with the reviewer’s criticism or assign a finding to the wrong source. Voice labels and stable IDs reduce the risk but do not remove the need for verification.

Accessible formats often receive deeper analysis. Record and correct that imbalance when the review purpose requires.

## 16.7 Save the Artifact

Save `literature-synthesis-stopping-rule-v0.1.xlsx` after populating its Synthesis Matrix sheet. Required row identifiers are source ID and relevant claim IDs. Required columns follow the review question and must include method, evidence base, finding or contribution, limitation, dependence, reviewer interpretation, and verification location.

Save source notes in the project’s notes environment using the source ID in the filename or metadata. Link notes to lawful source locations rather than embedding entire publications. Save analytic memos with dates and the matrix version they interpret.

When the matrix changes substantially, preserve the earlier version so the synthesis remains connected to the corpus state that produced it.

## 16.8 Advanced Practice

Qualitative analysis software can support document-level coding, retrieval, queries, and memos when the corpus warrants it. A spreadsheet may be better for a smaller review whose central operation is cross-source comparison. A database may suit a team handling many claims and relations. Choose the environment from the analytical task, collaboration needs, exportability, and preservation requirements, not from the number of available features.

Large reviews may sample for deep reading while retaining a broader screened corpus. Team projects should calibrate a shared schema while preserving minority interpretations that reveal genuine ambiguity.

# 17. Stage 6: Synthesize, Audit, and Stop

## 17.1 Orientation

Synthesis is the point at which a literature corpus becomes an argument. The researcher no longer asks what each publication says in turn. The task is to explain a pattern across works while preserving the differences that make the pattern meaningful. This requires compression, and compression creates risk: distinct questions become one debate, common dependence becomes consensus, and missing scholarship becomes absence in the world.

The final stage therefore joins three activities.[^18] Synthesize what the corpus can support. Audit how the corpus was assembled and represented. State why searching and reading can stop for the present purpose.

## 17.2 Learn

Begin with the review question and the matrix, not a blank document. Select an organizing logic that answers the question. Common structures include:

- **Problem or proposition:** organize around the explanations or claims the review must assess.
- **Conceptual dispute:** compare definitions, attributes, extensions, and consequences.
- **Intellectual lineage:** trace adoption, modification, criticism, and abandonment across time.
- **Method or evidence base:** show how sources, cases, measures, or analytical procedures shape findings.
- **Empirical pattern:** compare findings across settings, periods, populations, or case types.
- **Tension or paradox:** explain why apparently incompatible findings coexist.

Chronology can support any of these structures, but a year-by-year list rarely constitutes synthesis. Neither does a sequence of author summaries. Each section should make a claim across multiple works, identify the evidence and dependence behind that claim, explain consequential variation, and state the limit.

For each section, state the pattern, show its basis, explain variation, and state the consequence for the review question.

Distinguish consensus, convergence, and repetition. Consensus refers to a field-level pattern of agreement, which requires evidence about coverage and dissent. Convergence refers to different sources or methods reaching compatible conclusions. Repetition means that multiple publications state the same proposition. The third can occur without the first two. Use the dependence fields and citation chains to decide which term is warranted.

Integrate counterevidence early. A contrary work should not be placed in a final “criticism” paragraph after the main account has already hardened. Ask whether it identifies a boundary condition, uses different definitions, observes another population, relies on another evidence base, or directly contradicts the pattern. A synthesis becomes stronger when it explains what would have to be true for different findings to coexist.

Run a **coverage audit** before finalizing. Compare the corpus with the protocol and evidence map across language, geography, period, discipline, publication type, method, actor perspective, discovery route, and citation lineage. Count where useful, but interpret the counts. Ten articles from one special issue may provide less source diversity than three works found through independent routes.

Audit expected literatures or perspectives that did not appear. Classify the absence as substantive, terminological, index-related, inaccessible, ethical, or protocol-produced. A failed search does not prove that no scholarship exists.

The stopping rule asks whether additional searching is likely to change the answer needed for the current product. Criteria may include conceptual coverage, representation of principal explanations, route diversity, attention to counterevidence, stabilized vocabulary, diminishing returns in relevant new claims, and completion of verification for load-bearing sources. Stopping is a decision under limits, not a discovery that the literature has ended.

Add **reopening triggers**. A newly released archive, a major review, a revised dataset, an unsearched language, a credible contrary study, or a change in the research question may justify another cycle. Living scholarship requires a way to change without pretending that every page is continuously current.

## 17.3 Worked Example

The terrorism review does not conclude that databases “disagree” for one reason. Its matrix supports a more differentiated synthesis. Divergence appears at several layers: inclusion definitions shape the event universe; source systems affect what becomes observable; matching and deduplication affect whether records refer to the same event; category rules alter domestic/transnational assignments; and historical collection changes can create apparent trends. Different studies illuminate different layers.

The written review organizes sections around those layers. Within each, it distinguishes direct comparisons from repeated methodological warnings. It shows where works converge across databases or source-checking procedures and where later authors cite a single earlier account. It identifies a limit: English-language publications and publicly documented datasets are better represented than local validation work or proprietary systems. The consequence for the empirical project is a validation design that samples events at each transformation layer rather than searching for one universally correct count.

The coverage audit exposes an imbalance. Many works analyze outputs, fewer examine the news and administrative sources feeding the databases, and few center people or places whose experiences are reduced to event records. The review cannot repair that gap through one more database query. It records the gap in the evidence map and redirects collection toward source production.

In the municipal case, planning, legal, and local histories observe different institutional arenas and actors. The synthesis explains why they produce different chronologies instead of selecting one as universally correct.

The stopping rule notes that searches across five routes now recover familiar conceptual and empirical patterns; key works have been verified; local-language and dissertation coverage has been attempted; and contrary accounts are represented. It also records incomplete access to older internal reports. Discovery stops for the chapter, while a newly digitized report series or evidence that another agency name was used would reopen it.

## 17.4 Try It

Write a one-sentence answer to the review question using only claims supported by the matrix. Underline every term that implies coverage: words such as *most*, *widely*, *consensus*, *established*, or *the field*. For each, identify the evidence that justifies it. Replace terms that exceed the corpus.

Draft a synthesis outline with three to five section claims. Under each claim, list:

1.  representative claim IDs;
2.  contrary or boundary claim IDs;
3.  shared-dependence risks;
4.  the source of variation;
5.  the consequence for the research question;
6.  the limit that the section must state.

Next complete the coverage audit. Choose at least six dimensions appropriate to the review and mark coverage as strong, adequate for purpose, weak, constrained, or unknown. Provide evidence and an action for every weak or unknown dimension. Some actions will be another search. Others will be a limitation statement or a change to the empirical design.

Finally, write the stopping rule in one paragraph and a separate list of reopening triggers. Give the corpus and protocol versions to which the rule applies. Ask a colleague to identify what evidence would make the stopping decision unreasonable.

## 17.5 Guided AI Workflow

AI can audit a populated synthesis plan for overclaiming and missing contrasts. Provide the review question, section claims, matrix rows represented by source/claim IDs, dependence markers, coverage table, and proposed stopping rule. Ask the system to identify claims resting on one source, words that imply unsupported coverage, neglected contrary entries, and stopping criteria not backed by the audit.

**Permitted input:** Researcher-authored synthesis plans, structured matrix excerpts, verified metadata, IDs, and non-sensitive coverage summaries.\
**Do not provide:** Copyrighted full text, confidential manuscripts, restricted source descriptions, participant data, or sensitive findings that should not leave the approved environment.\
**Verify:** Trace every critique to the supplied matrix and then to the underlying source for load-bearing issues. Confirm that the model did not treat empty cells as negative findings or dependence as independence.\
**Record:** Save model/version, input description, audit output, accepted revisions, rejected critiques with reasons, reviewer, matrix/protocol versions, and date.

Use the system as an adversarial reader, not a ghostwriter. A useful prompt asks: “What is the strongest alternative account compatible with these entries?” The response can reveal a missing comparison. It does not establish that the alternative is true.

Do not ask a model to infer field-level consensus from citation counts or snippets. Do not allow it to fill gaps with general knowledge. Require it to say “not supported by the supplied record” when the matrix lacks evidence.

## 17.6 Integrity Checkpoint

Synthesis allocates visibility. Cite works that contribute evidence or ideas, not only surveys, and preserve credit across languages, regions, and publication forms.

Avoid false transparency. A public search log can expose sensitive topics, proprietary access routes, reviewer identities, or the location of vulnerable archives. Release a calibrated record or redacted version when necessary, and explain the omission.

Do not convert lawful access limits, unsuccessful searches, or a model’s failure to recall a source into evidence that no scholarship exists.

Corrections are part of a living review. Provide a version, review date, citation form, change log, and route for reporting errors. Preserve previous releases when feasible so readers can identify which account they used.

## 17.7 Save the Artifact

Complete the workbook’s Coverage Audit, Memo Plan, and Stopping Rule sheets. Record evidence, dependence, constraints, claims, counterevidence, limits, decisions, owners, and reopening triggers.

Save a synthesis memo keyed to the workbook version. State the review’s answer, strongest basis, most consequential disagreement, coverage limit, implications for empirical collection, and stopping decision. The memo is the bridge between the working artifacts and the written chapter.

Archive the review artifacts together, prefer open formats, and preserve only material that rights and ethics permit.

## 17.8 Advanced Practice

Formal synthesis traditions require their own standards. Living reviews additionally require ownership, review intervals, corrections, and version rules.

# 18. Review Articles and Meta-Analysis in Transition

## 18.1 Orientation

A review article once appeared to be a retrospective product. Its authors surveyed an established literature, organized its main findings, and published a settled account. That model still has value, but it no longer describes the entire task. Digital discovery produces larger and more varied corpora. Open research practices expose protocols, coding decisions, data, and analysis. New studies can make a synthesis stale soon after publication. AI can accelerate several clerical operations, while also multiplying plausible errors.

These changes are turning the review from a static article into a form of research infrastructure. The article remains an argument, but the argument now rests on inspectable and potentially reusable objects: a protocol, search history, screening record, coded corpus, analysis, sensitivity tests, and update policy. A trustworthy review links these objects without pretending that procedural detail can replace judgment.

This chapter explains the present and plausible future of review articles and meta-analyses in the social sciences. Its central claim is simple. New tools can shorten discovery, screening, extraction, and updating, but they cannot decide what evidence is comparable or what variation means. The durable unit of progress is therefore not an automated summary. It is a versioned chain of decisions that another researcher can inspect, challenge, and extend.

## 18.2 Learn

### 18.2.1 Begin with the review family

The term *literature review* covers several products with different purposes. A narrative or integrative review may clarify a concept, reconstruct an intellectual debate, or develop a theoretical account. A scoping review maps the extent and characteristics of a broad body of work. A systematic review answers a bounded question through explicit, reproducible procedures. A qualitative evidence synthesis interprets meanings or mechanisms across studies. An evidence and gap map describes the distribution of evidence without necessarily estimating a common effect. An umbrella review examines existing reviews. A rapid review makes declared concessions to produce a timely answer. Meta-analysis statistically synthesizes estimates that meet defined comparability conditions.[^19]

This review family is not a hierarchy. A systematic review is not automatically superior to an interpretive review. A meta-analysis is not a badge of rigor that can be added to any corpus. Each form answers a different question and makes different assumptions. The first design decision is therefore functional: what must the review allow its reader to understand, estimate, compare, or decide?

A review of how a concept changed across disciplines may require close comparison of definitions and citation lineages. A review of whether an intervention changes an outcome may support statistical synthesis. A review of how participants experience that intervention may require qualitative synthesis. A review of an emerging field may first need a scoping map because its populations, measures, and outcomes remain unstable. Combining these products can be useful, but their inferential roles must remain distinct.

Method names do not settle the design. Authors sometimes label a broad database search a systematic review even when eligibility decisions and synthesis rules remain unclear. Other reviews apply a narrow checklist to a question that requires historical or conceptual interpretation. The defensible sequence runs from question to evidence type, from evidence type to review form, and from review form to procedure.

### 18.2.2 Understand what meta-analysis adds

Meta-analysis is not a synonym for systematic review. It is a set of statistical methods for describing and explaining a distribution of comparable effect estimates within a defined corpus.[^20] The systematic review establishes how studies entered that corpus. The meta-analysis addresses what their estimates imply under declared statistical assumptions.

This distinction matters because a precise pooled estimate can conceal a weak evidence base. Studies may use different constructs under the same label, compare unlike populations, report incompatible outcomes, or estimate effects under different causal conditions. A statistical model can combine the numbers, but it cannot make the underlying questions equivalent.

Before pooling, construct an estimand table. Each row should record the population, treatment or exposure, comparison, outcome, timing, design, effect measure, and adjustment set. Add the unit of assignment, unit of analysis, and level at which uncertainty was estimated. The table makes comparability a visible decision instead of an assumption hidden inside software.

The pooled mean is only one possible target. A review may seek the average association across settings, the distribution of effects, an expected effect in a new setting, or the moderators that account for variation. These are different questions. A model chosen for one should not be interpreted as if it answered the others.

### 18.2.3 Treat heterogeneity as substantive evidence

Social science effects often vary because institutions, histories, populations, measures, and implementation differ. Heterogeneity is therefore more than noise around a universal effect. It may be the principal finding.

A random-effects model acknowledges variation among the effects represented by the included studies. It does not prove that those studies form one meaningful population. Nor does it license an inference to every setting beyond them. The review must explain which sources of variation were expected before analysis and which appeared only after inspecting the data.

Report the distribution of effects, not only its mean. A confidence interval describes uncertainty around an estimated parameter. A prediction interval addresses a different question: where an effect from a comparable future setting might plausibly fall. When heterogeneity is substantial, the prediction interval may cross thresholds that the pooled mean does not. Its width can be more informative for policy than the significance of the mean.

Moderator analyses can examine theoretically specified variation, but they are vulnerable to low power, multiple testing, and ecological interpretation. A moderator measured at the study level cannot establish the corresponding individual-level mechanism. Separate planned tests from exploratory ones. Record which coding distinctions existed before results were examined.

Qualitative and quantitative synthesis can inform each other here. Close reading may identify institutional differences that define plausible moderator categories. Quantitative patterns may identify cases that deserve renewed interpretation. Mixed evidence becomes valuable when the forms remain legible, not when one is used to decorate the other.

### 18.2.4 Preserve dependence and multiplicity

Many social science studies report several outcomes, time points, subgroups, models, or treatment contrasts. Several articles may also analyze the same dataset. These estimates share observations and design decisions. Treating them as independent produces excessive precision and gives prolific studies or datasets disproportionate influence.

Every effect table should therefore include a study identifier, sample identifier, dataset identifier, outcome family, time point, and model family. This structure reveals dependent effect estimates before analysis. The reviewer can then select one estimate under a preregistered rule, model the hierarchy, use an appropriate multivariate method, or apply robust variance estimation when its assumptions and sample requirements fit the corpus.[^21]

Dependence is also intellectual. A set of studies may repeat one operationalization, share code, or inherit the same measurement error. Statistical correction for clustered standard errors does not remove that shared conceptual ancestry. The written synthesis should distinguish repeated analysis from independent replication.

Model multiplicity creates another problem. Authors can often report many defensible specifications. Reviews that select one estimate per study after seeing the results may reproduce selective reporting. Collecting all relevant estimates and modeling their dependence can be preferable, but it requires careful coding and a declared strategy. Contemporary social science guidance identifies dependence, systematic heterogeneity, and publication selection as recurring issues that every quantitative synthesis should address.[^22]

### 18.2.5 Examine selective reporting without a mechanical verdict

The available literature is not a neutral sample of completed research. Statistically striking results may be more likely to be written, submitted, accepted, or emphasized. Outcomes and specifications can also be selected within a published study. Gray literature searches may reduce some forms of selection while introducing new differences in reviewability and metadata.

No single funnel plot, regression, or adjustment method can diagnose and repair every form of publication bias. Small-study patterns can arise from heterogeneity, design quality, or genuine differences in populations. Statistical corrections rely on assumptions that may not fit the selection process. Use several sources of evidence: prospective registrations where available, dissertations and reports, requests for unreported results, outcome comparison within studies, sensitivity analyses, and a substantive account of incentives in the field.

The review should state what would have to be missing to change its conclusion. That question turns a generic limitation into a sensitivity claim. It also prevents the adjusted estimate from appearing as a recovered truth. A corrected result remains conditional on a model of what became observable.

### 18.2.6 Make the synthesis reproducible

Open practice changes a meta-analysis from a report about an analysis into a rerunnable research object. A strong public package includes the protocol, complete search strategies, screening decisions, extraction definitions, coded data, transformation code, analysis code, output tables, and a record of deviations. When materials cannot be shared, the package should describe the restriction and expose the largest safe portion.

Preregistration does not freeze a review against learning. It distinguishes planned decisions from changes made after contact with the evidence. A deviation log can record what changed, why it changed, when the team decided, and which outputs the change affected. Open materials allow readers to evaluate those decisions and allow later teams to update the review rather than reconstruct it.[^23]

Transparency must extend to the quantitative data structure. A spreadsheet of final effect sizes is insufficient if it omits study relationships, transformation rules, excluded estimates, and coding uncertainty. Preserve raw extracted values alongside derived values. Give every effect a stable identifier that links it to its source location and coding decision.

Meta-research has found persistent gaps in the transparency and reproducibility of published meta-analyses.[^24] A long methods section does not by itself solve the problem. Reproducibility depends on whether the released objects recreate the stated result and make consequential judgment visible.

### 18.2.7 Design living reviews as governed projects

A living review incorporates new evidence under a continuing workflow. It is an update mode, not another review question type. The same systematic review can be maintained in living form when new research arrives frequently and could change a consequential conclusion.[^25]

Living status requires more than an editable webpage. The team needs a surveillance strategy, update trigger, review interval, ownership rule, version number, correction process, and retirement condition. Each release should preserve a citable snapshot. Readers must be able to identify which evidence and analysis supported the version they used.

Updates also create statistical problems. Repeatedly recalculating and testing a pooled effect as new studies arrive can change error rates. A living meta-analysis therefore needs a declared updating method, especially when policy decisions depend on crossing a threshold. The correct method depends on the inferential target, expected evidence flow, heterogeneity, and cost of error. No universal update rule replaces these design choices.

Maintenance should be selective. A slowly changing historical literature may not justify continuous surveillance. A fast-moving policy question might. A review can leave living mode when new studies become unlikely, the conclusion stabilizes for its decision purpose, or resources no longer support responsible maintenance. Calling every online review living would conceal these commitments.

### 18.2.8 Give AI bounded work

AI can assist with query expansion, deduplication, screening prioritization, structured extraction, citation checking, code explanation, and update surveillance. Earlier machine-learning research found some mature applications for study identification, while extraction and judgment-intensive tasks required more development.[^26] Later reviews documented rapid growth in available systems, especially around search, screening, extraction, and synthesis.[^27]

The number of tools does not establish their reliability for a particular review. Performance depends on the question, source type, language, study design, prevalence of eligible records, and definition of an error. A system that ranks relevant records near the top may save labor without being safe for autonomous exclusion. A fluent extraction may still assign a number to the wrong group, outcome, or time point.

Use AI as a proposal layer. The system can suggest records, fields, links, and checks. A controlled review step decides what enters the evidence base. For screening, validate recall on a representative researcher-coded sample and inspect every false exclusion. For extraction, require an exact source span and abstention option. For risk-of-bias assessment, causal interpretation, and final inclusion, retain human adjudication.

Human validation is not a ceremonial final glance. It is a measured procedure. Record the validation sample, sampling rule, reference coding, error categories, model and prompt version, decision threshold, and response to failure. Revalidate after material changes in the corpus or system.

### 18.2.9 Build skills, agents, and project context as separate layers

Repeated AI use becomes more reliable when a project separates procedure, execution, and memory. A **skill is a reusable research procedure**. It specifies when a task should run, what inputs it accepts, which steps it follows, what it must produce, and how its output will be checked. An **agent is a bounded executor** that receives a goal, approved tools, selected context, stopping conditions, and an output schema. It may combine several skills and adjust its plan as evidence appears. Neither should become the authority that decides what the project means.

This distinction prevents a common design error. A long prompt may contain a useful procedure, but it remains difficult to test, version, and reuse. A general agent may take many actions, but breadth makes its errors harder to locate. Skills should hold stable method. Agents should coordinate bounded work. Human gates should control consequential changes to the corpus, protocol, argument, and public record.

#### 18.2.9.1 Design a minimal research skill stack

A skill should encode knowledge that the project would otherwise have to reconstruct. Its manifest should name its purpose, triggers, required inputs, procedure, output schema, verification rules, failure conditions, permissions, version, and benchmark cases. High-risk operations need narrow instructions and deterministic checks. Interpretive tasks need room for alternatives, but they still require evidence identifiers and an abstention route.

Five skills provide a useful starting stack for review-based social research:

| Research function | Reusable skill | Required artifact | Human gate |
|----|----|----|----|
| Literature discovery | **Literature-discovery skill** | Candidate register, query history, discovery-route coverage | Approve final inclusion and exclusion |
| Gap identification | **Gap-analysis skill** | Gap-claim register with supporting and contrary corpus entries | Authorize any claim that a field lacks evidence |
| Methodology | **Methodology-audit skill** | Question-design alignment memo, threat register, proposed tests | Approve protocol or analysis changes |
| Data collection | **Data-collection skill** | Candidate records, provenance links, validation report | Promote records into the research corpus |
| Project continuity | **Project-context skill** | Versioned project context packet and proposed change log | Modify the project charter, concepts, or accepted claims |

The literature-discovery skill should translate concepts into search vocabulary, vary discovery routes, preserve queries, deduplicate candidates, and flag coverage risks. It should not produce a list of “the most important” publications from model recall. Its unit of output is a candidate with a discovery route and verification status.

The gap-analysis skill should distinguish several kinds of gap. A corpus may lack evidence about a population, setting, period, mechanism, measure, comparison, or method. It may contain contradictory findings, weak replication, or a concept that has not been operationalized consistently. These are different research problems. The skill must also distinguish absence in the bounded corpus from absence in the field. A **false gap** occurs when failed retrieval, unfamiliar vocabulary, access limits, language bias, or an incorrect boundary is presented as a missing body of knowledge.

The methodology-audit skill should compare the research question with the evidence, design, unit of analysis, estimand, inferential claim, and known threats. It can propose alternative designs or sensitivity tests. It should not silently rewrite the approved protocol. Every recommendation needs a location, a reason, the evidence affected, and the decision that remains with the researcher.

The data-collection skill should enforce the transformations defined elsewhere in this book. It can create candidate records, check required fields, preserve source spans, detect likely duplicates, and route uncertain cases. It should write only to a staging area. Promotion into the verified corpus requires source review, rights and ethics checks, and a named human decision.

The project-context skill is different from the other four. Its task is not to perform a substantive review operation. It prepares the smallest sufficient account of the project for another task. It retrieves the current research question, approved scope, working concepts, source hierarchy, ethical limits, corpus and codebook versions, accepted decisions, unresolved disputes, artifact locations, and active release. It also reports conflicts among these objects rather than resolving them through a plausible summary.

Skills need tests before routine use. Discovery can be evaluated through recall, false exclusions, route diversity, and labor saved. Gap analysis needs cases where a missing concept is genuine and cases where it is only hidden by vocabulary or indexing. Methodology audits need known design defects and defensible designs that should not be criticized. Data collection needs stratified extraction and provenance benchmarks. Project-context tests should include stale decisions, conflicting versions, renamed concepts, and inaccessible artifacts.

#### 18.2.9.2 Assign agents work packages, not identities

Language-model agents can interleave planning, retrieval, tool use, and revision.[^28] Research prototypes have also combined observation, retrieval, reflection, and planning in persistent agent architectures.[^29] These patterns make multi-step research assistance possible. They do not show that an agent can independently establish relevance, a scholarly gap, methodological validity, or causal interpretation.

A research agent should therefore receive a work order. The order names one goal, the skill versions it may invoke, permitted collections and tools, project context version, expected artifacts, prohibited actions, stopping rule, and escalation conditions. The agent should return evidence-linked proposals and an execution log. It should not inherit an open-ended instruction to “finish the literature review.”

The five skills above can support corresponding agents. A literature scout executes searches and updates the candidate register but cannot reject the final record. A gap analyst compares the verified corpus with the review protocol and produces candidate gap claims with counterevidence. A methodology critic tests alignment and assumptions without editing the protocol. A collection steward prepares and validates candidate data while leaving promotion to a reviewer. A context curator assembles the current project packet and proposes corrections without overwriting canonical project records.

Agent specialization should reduce ambiguity, not imitate an academic department. Adding several agents that use the same model, sources, and instructions does not create independent corroboration. Their errors remain correlated. Agreement among them is not consensus, and disagreement is not automatically informative. Use multiple agents when tasks can be separated by evidence, method, or validation role. Do not create a panel merely to generate more text.

Apply least privilege. A discovery agent usually needs search and read access, not permission to change the corpus. A methodology critic needs the protocol and selected artifacts, not participant data. A context curator needs approved project records, but it should not publish, delete, or revise them. Rights, privacy, security, and cost boundaries belong in the work order rather than in an informal reminder.

Consequential decisions require explicit human gates. These include approving inclusion and exclusion, declaring a research gap, changing the research question or protocol, promoting a candidate record, accepting a new variable, interpreting a causal relationship, and releasing a public claim. The gate should record who decided, which agent output was reviewed, what evidence supported the decision, and what changed downstream.

#### 18.2.9.3 Preserve broad context through governed retrieval

The broad project context should live outside the conversation. A chat transcript mixes instructions, exploration, corrections, and obsolete claims. Treating all of it as memory makes current and superseded decisions difficult to distinguish. Supplying the entire project archive is not a solution either. Empirical work on long-context models shows that access to a long input does not ensure reliable use of information throughout that input.[^30]

Create a **project context packet** with three layers. The stable layer contains the research question, scope, central concepts, evidence standards, ethics and rights constraints, and authority for decisions. The current-state layer names the active stage, corpus and codebook versions, accepted claims, unresolved questions, recent decisions, and release status. The task layer contains only the materials, instructions, and stopping rule needed for the present work.

Use progressive disclosure. Every agent receives a short project card and the task layer. It retrieves method, corpus, or source details only when the work requires them. Each retrieved item carries a stable identifier, version, date, and authority status. This design preserves the global argument while reducing irrelevant material and exposure of sensitive records.

The project context packet is a map, not a substitute for evidence. It may say that a definition was adopted in decision `D-014`, that corpus `C-03` supports claim `CL-08`, and that a contrary memo remains unresolved. The agent must follow those identifiers to the relevant artifact before making a consequential recommendation. A compressed statement without provenance remains a lead.

Context updates should follow the same proposal boundary as data extraction. An agent may identify that the active question conflicts with the latest protocol or that a manuscript cites an obsolete corpus. It writes the proposed correction to a staging area. A researcher decides whether to update the canonical packet, records the reason, and increments its version.

This architecture supports continuity across literature review, gap analysis, methodology, and collection. The literature scout sees the current vocabulary and boundaries. The gap analyst sees the verified coverage audit. The methodology critic sees the approved estimand and threats. The collection steward sees the source frame and codebook. The context curator sees how their artifacts connect, but it does not turn their provisional outputs into settled project knowledge.

Evaluate the system as a chain. Record whether a task used the correct context version, whether the appropriate skill triggered, whether the agent stayed within permissions, whether its evidence links resolved, whether it abstained when required, and whether the human gate caught consequential errors. Productivity matters, but speed without these measures can make an incoherent project move faster.

### 18.2.10 Separate the present from the forecast

The current review article can already be modular and open. Protocols, machine-readable data, executable analysis, linked corrections, and citable releases are available practices. Semi-automated screening and extraction are emerging practices whose value must be demonstrated in the local corpus. Continuous synthesis across interoperable evidence registries remains a conditional future.

| Horizon | Review form | Required safeguard |
|----|----|----|
| Current practice | An article linked to protocol, corpus, code, and a citable release | Reproducibility, provenance, and disclosed deviations |
| Emerging practice | A living review with AI-assisted surveillance, prioritization, and extraction | Local validation, human adjudication, and version governance |
| Conditional future | A continuously updated evidence service built from interoperable study, claim, and effect objects | Durable standards, equitable access, preservation, and accountable ownership |

The conditional future is technically plausible but institutionally demanding. Journals and repositories would need stable citation rules for changing objects. Research teams would need credit for maintenance, correction, data stewardship, and negative updates. Shared schemas would need to preserve construct differences rather than forcing every study into one vocabulary.

The review article may become an interface over a versioned evidence system. Readers could inspect the current conclusion, trace it to effects or qualitative findings, change defensible assumptions, and compare releases. Such an interface would not eliminate authorship. Its design would make authorship more visible by showing where inclusion, coding, modeling, and interpretation shaped the answer.

This future also carries risks. Well-resourced fields may maintain sophisticated living syntheses while other regions and languages remain poorly indexed. Proprietary systems may make public evidence dependent on private infrastructure. Continuous updating can create an illusion of completeness and exhaust the teams responsible for it. The goal is not permanent motion. It is controlled revision when new evidence matters.

## 18.3 Worked Example

Consider a review asking whether community-policing programs increase public trust in police. The first search identifies experiments, quasi-experiments, surveys, qualitative interviews, and program evaluations across several countries. A single pooled estimate would answer the wrong question because the studies do not share one treatment, outcome, or causal design.

The team divides the project into linked products. A scoping map describes programs, populations, research designs, trust measures, and geographic coverage. A systematic review evaluates studies with a defensible comparison group. A qualitative synthesis examines how residents describe contact, legitimacy, safety, and unequal treatment. The products share a source register but maintain separate eligibility and synthesis rules.

The quantitative subset still contains hidden multiplicity. Several reports use one national survey. Individual studies report trust immediately after contact and again months later. Some programs combine foot patrols with public meetings, while others change only officer assignment. The estimand table exposes these differences. The effect table links multiple estimates to samples, outcomes, and program families.

The main model estimates an average across a defined family of programs. It also reports a prediction interval and planned comparisons by intervention component and institutional setting. A dependence-aware analysis prevents one large survey and its related articles from dominating precision. The review treats the remaining heterogeneity as a finding: program labels conceal distinct mechanisms and political contexts.

Publication-bias analysis finds that small published studies report more favorable estimates. The team does not declare the pattern corrected after one adjustment. It searches evaluation repositories and dissertations, compares registered outcomes where possible, and reports sensitivity to several selection assumptions. The conclusion becomes conditional: favorable average results do not establish that every program or setting will improve trust.

The public package contains the protocol, search histories, decision log, coded corpus, effect transformations, analysis code, and a redacted qualitative matrix. The team schedules annual surveillance but triggers an earlier update if a large multisite evaluation appears. Release 1.0 remains frozen and citable when release 1.1 adds new evidence.

An AI system expands intervention names and ranks new search results. It proposes extraction fields with source spans. Researchers validate screening recall on a stratified sample and adjudicate all exclusions near the decision boundary. The system never decides whether a program belongs in the same causal family or whether a trust measure is substantively comparable. Those judgments remain part of the review’s argument.

The team implements this arrangement as separate skills and agents. The literature-discovery skill records every query and route. A scout agent runs that skill against approved databases and deposits candidates in a staging register. The gap-analysis skill compares the verified corpus with the protocol. Its agent proposes a geographic gap, but the coverage audit shows that two relevant local-language indexes were never searched. The team records an unresolved coverage limit instead of claiming that no such research exists.

The context curator prepares project packet 1.3 for the annual update. It includes the current question, intervention taxonomy, approved trust measures, corpus release, open disagreement about quasi-experimental designs, and links to every decision. The methodology critic identifies that a proposed new synthesis would mix immediate and long-term outcomes. It recommends a protocol amendment but cannot make it. Researchers review the affected records, approve a revised timing rule, and issue packet 1.4 before the other agents resume work.

## 18.4 Try It

Start with one review question and write the decision it must support. Name the review form that best fits that purpose. Then state why two neighboring forms would answer different questions.

Create an estimand table for five candidate studies. Record population, exposure or intervention, comparison, outcome, timing, design, and effect measure. Add sample and dataset identifiers. Mark which studies could enter one quantitative synthesis and explain every exclusion from pooling.

For the eligible estimates, draw a dependence map. Connect effects that share participants, datasets, outcomes, authorship pipelines, or measurement instruments. Choose a strategy for each connection and state what assumption the strategy requires.

Draft a result paragraph that reports the mean, its uncertainty, heterogeneity, a prediction interval, and one limitation arising from the corpus. Remove any sentence that treats statistical significance as a complete substantive conclusion.

Finally, write an update policy. Specify surveillance sources, cadence, update triggers, owner, release format, correction route, and retirement condition. Label each planned feature as current, emerging, or conditional future. This prevents an aspiration from being presented as an implemented method.

Design one research skill for the review. Write its trigger, required inputs, procedure, output schema, verification rule, permissions, failure condition, and three benchmark cases. Then write an agent work order that may invoke the skill. Give the agent one goal, a context version, approved tools, a stopping rule, and an escalation route.

Create project context packet 0.1. Limit its stable layer to one page. Add a current-state table and a task layer for one operation. Ask a colleague to locate one accepted decision, one unresolved dispute, and one source artifact using only the packet. Revise any entry that cannot be traced.

## 18.5 Guided AI Workflow

Begin by issuing a versioned project context packet and work order. Then use AI in four bounded passes. In the design pass, provide the research question and intended decision. Ask the system to compare plausible review forms and list the evidence each would require. In the structure pass, provide verified study metadata and researcher-defined fields. Ask it to flag possible construct mismatch, dependence, and missing values without deciding eligibility. In the audit pass, provide the analysis plan and output. Ask for unsupported inferences, omitted sensitivity tests, and discrepancies between the estimand and conclusion. In the update pass, ask it to rank new candidate records and explain each ranking.

A useful audit prompt is:

> Review this estimand table, effect structure, analysis plan, and draft conclusion. Identify claims that exceed the eligible corpus, effect estimates that may be dependent, sources of heterogeneity not represented in the model, and statements that confuse a pooled mean with an expected effect in a new setting. Cite only the supplied record identifiers. Return “not established” when the record is insufficient.

**Permitted input:** Verified metadata, researcher-authored protocols, rights-cleared text, structured extraction fields, de-identified effect data, code, and public analytical output.\
**Do not provide:** Licensed full text without permission, confidential peer-review material, protected participant data, restricted archives, or identifiable sensitive records.\
**Verify:** Check every proposed inclusion, exclusion, extracted value, source span, transformation, dependence link, citation, and analytical claim. Test screening and extraction performance on a representative human-coded sample.\
**Record:** Save model and version, skill and agent versions, project context packet, work order, prompt, input description, tool actions, output, reviewer decision, error category, protocol and corpus versions, analysis release, and date.

Do not ask a model to select the final review form, infer missing statistics without a declared method, adjudicate risk of bias alone, or choose a publication-bias correction after seeing which result is favorable. Do not accept a causal or policy conclusion that cannot be reconstructed from the reviewed evidence objects.

## 18.6 Integrity Checkpoint

A comprehensive search can still reproduce unequal visibility. Dominant databases index some journals, languages, regions, and publication forms more completely than others. AI systems inherit those boundaries and may rank familiar terminology above locally specific concepts. Audit discovery by language, geography, discipline, publication form, and institutional access.

Quantitative synthesis can erase difference through a common effect measure. Before converting outcomes, ask whether they represent the same construct and decision. Preserve original scales and definitions alongside transformed values. Report exclusions from pooling without treating unpooled studies as inferior evidence.

Open release also has limits. Study-level data may contain confidential information or enable reidentification. Search histories can expose sensitive research interests or restricted holdings. Release a calibrated public package and document the withheld components, access basis, and responsible contact.

AI assistance creates additional disclosure duties. Name the operations it supported, the system version, validation procedure, and known failures. Do not list a general-purpose model as an author or allow it to conceal who made consequential decisions.

Agent delegation can obscure responsibility. A coordinating agent may summarize another agent’s output and remove its qualifications. Several agents may repeat one mistaken extraction and make it appear independently confirmed. Preserve the complete provenance chain, label shared models and inputs, and route agent outputs through the same evidence checks as direct model output.

Project context can contain unpublished arguments, access credentials, participant information, and restricted source locations. Give each agent only the layer required for its task. A context packet prepared for discovery should not expose material needed only for confidential analysis.

Finally, resist prestige by method. A complex model cannot compensate for a weak corpus. A transparent narrative synthesis can be more informative than an invalid pooled estimate. The review earns trust by matching its claim to its evidence and preserving the path between them.

## 18.7 Save the Artifact

Save a review design memo that links the question, intended decision, review form, eligible evidence, and synthesis method. Preserve the protocol and every dated amendment.

Maintain a source register, screening log, extraction dictionary, coded corpus, dependence map, and synthesis memo. For meta-analysis, add raw and transformed effect data, executable code, session information, model diagnostics, prediction intervals, and sensitivity results.

Create a release manifest. It should name the corpus version, protocol version, codebook version, analysis commit, public files, restricted files, license, citation, review date, correction route, update trigger, and retirement condition. Give each release a stable identifier and preserve earlier releases.

Maintain a research-automation register. For every skill, save its manifest, instructions, scripts or schemas, benchmark set, evaluation results, permissions, owner, and version. For every agent, save its work-order template, permitted skills and tools, expected output, escalation rule, and tests. Archive each project context packet and its approved change log. Do not store credentials or protected source content in these public or reusable definitions.

The accompanying [Skills and Agents Lab](skills-and-agents-lab.qmd) provides the first complete implementation of this architecture. Release 0.1.0 contains a literature-discovery skill, a read-only scout agent, a three-layer project-context packet, three synthetic benchmark cases, a candidate-register validator, an explicit failure report, and a versioned download. It is a pilot procedure to inspect and test, not evidence that autonomous discovery is reliable.

The article, dataset, code, and review website should point to the same manifest. This shared reference prevents a current webpage from silently changing the evidence behind an older citation.

## 18.8 Advanced Practice

Prospective meta-analysis coordinates eligible studies and analyses before their results become known. It can reduce some forms of outcome selection and harmonize measures while preserving study-level independence. It requires governance that protects local study ownership and records any changes made after results arrive.

Individual-participant-data meta-analysis can examine common definitions and participant-level variation that published aggregates cannot support. Its advantages depend on data access, harmonization quality, missingness, and representation of studies that cannot share data. The unavailable studies remain part of the inference problem.

Bayesian meta-analysis can encode uncertainty about heterogeneity, combine prior information with new evidence, and support sequential updating. Priors should be justified, sensitivity-tested, and separated from evidence supplied by the included studies. Bayesian computation does not make incomparable effects comparable.

Multiverse meta-analysis can reveal how defensible choices about inclusion, effect selection, dependence, and modeling affect the conclusion. The set of specifications must follow substantive and methodological reasoning. A large grid of arbitrary models can obscure judgment as easily as one preferred model.

The mature review program connects these methods to a Second Brain without collapsing private work into public evidence. Source notes, decision records, and synthesis memos support learning. Stable public releases support scrutiny and reuse. The boundary between them is deliberate.

An advanced system may use a coordinating agent to divide a review update into discovery, gap analysis, methods audit, and collection tasks. Coordination should occur through artifacts rather than conversational summaries. Each specialist receives the same approved project card, a distinct work order, and only the context needed for its task. The coordinator can detect missing outputs and schema conflicts, but human reviewers still control the gates between candidate, verified, accepted, and published states.

Treat the context curator as a librarian, not an executive. It maintains indexes, reports contradictions, assembles task packets, and proposes version changes. It does not decide that a disputed claim has become accepted or that an old limitation no longer matters. Keeping this boundary protects the project’s intellectual history from being rewritten for the convenience of the current task.

The future review article is therefore neither a traditional essay with added links nor a database without an argument. It is a governed scholarly claim over a versioned evidence system. Its authority comes from the fit among question, corpus, method, and interpretation. Its capacity to change becomes a strength only when readers can see what changed, why it changed, and which conclusion the earlier evidence supported.

# 19. Building Event Databases with AI

## 19.1 Orientation

Event databases convert dispersed accounts into comparable records. A researcher may begin with a question about protest, repression, political violence, institutional reform, migration, or disaster response. The relevant traces may appear across newspapers, archival catalogues, government reports, organizational records, and born-digital collections. Before generative AI, much of the work required repetitive searching, copying, normalization, and initial classification. These tasks consumed time that researchers needed for interpretation.

AI changes the feasible scale of this work. A system can expand queries, search an authorized collection, extract candidate fields, compare reports, and flag records that may describe the same occurrence. It can apply a preliminary codebook to thousands of passages and identify dimensions the original codebook omitted. Studies of text annotation show that language models can perform some bounded classification tasks quickly and inexpensively. Performance, however, varies substantially across tasks and datasets, which makes local validation indispensable.[^31]

The resulting speed creates a methodological danger. A fluent extraction can make an uncertain mention look like an observed event. Several articles can make one wire report look like independent confirmation. A model can produce a precise code for an ambiguous passage or a causal probability without defining the comparison that gives the number meaning. Faster processing does not remove these problems. It can reproduce them at scale.

This chapter presents an auditable alternative. AI compresses clerical stages while the researcher preserves a visible chain from source to record, record to event, event to variable, and written evidence to causal inference. Every transition produces an artifact that can be reviewed, corrected, and versioned.

## 19.2 Learn

### 19.2.1 Begin with the unit, not the model

An event database requires a declared unit of observation. The unit might be an attack, demonstration, arrest, policy decision, organizational founding, public statement, or interaction between named actors. Its boundary must state what counts as one event, when two reports refer to the same event, and when one report contains several events.

Write the boundary before retrieval. Record inclusion and exclusion rules, temporal and geographic scope, actor and action definitions, and the minimum evidence required for a verified record. The first codebook should follow the research question and hypotheses. It should identify the variables needed to describe the event, evaluate rival explanations, and document the reporting process.

This order matters because a model will readily propose whatever categories are easy to extract. Extractability is not theoretical importance. If the system defines the unit through its output, the database may record what the model recognizes instead of what the research design requires.

### 19.2.2 Build a source frame

Manual newspaper searching often proceeds title by title and query by query. A digital source frame allows the researcher to define a collection before searching it. The frame records each newspaper, archive, database, date range, language, access route, known gap, and relevant restriction. Open news infrastructures can support large-scale retrieval, while library archives can expose searchable historical newspapers and catalogue records.[^32] The frame should also include local and oppositional sources that a prominent aggregator may not index.

Digitized collections are not transparent windows onto the past. Selection, survival, digitization, OCR quality, licensing, and search interfaces shape what becomes discoverable. Studies of newspaper digitization show why collection composition must be examined before researchers interpret search results as historical coverage.[^33] A failed query may indicate absence, vocabulary mismatch, OCR error, unavailable dates, or a source omitted from the platform. Record which explanation remains plausible.

AI can accelerate work inside the source frame. It can translate query concepts, generate historical names, adapt syntax across archives, and rank retrieved documents for review. A search-connected system may also query an approved interface directly. These operations remain collection procedures. The search log should preserve the source collection, query, date, filters, result count, model or script, and review decision. Access must comply with archive rules, licenses, privacy obligations, and research ethics.

### 19.2.3 Separate discovery from verification

The first extraction produces a **candidate record**, not an event. A candidate record reports that a particular source span may describe an event within scope. It should preserve the document identifier, publication date, page or URL, exact source span, retrieval route, proposed event date, actors, action, target, location, and model output. The preserved span allows a reviewer to return to the evidence without trusting the summary.

A candidate becomes a **verified record** only after the relevant passage and metadata have been checked. Verification asks whether the source exists, whether the passage supports the proposed fields, whether uncertainty has been preserved, and whether the item satisfies the inclusion rule. The decision may be accepted, rejected, or marked unresolved. It must name the reviewer and date.

This separation allows wide retrieval without lowering the evidentiary threshold. The system can favor recall during discovery because false positives remain outside the verified dataset. Reviewers can then favor precision when deciding what enters the database. A model should have an abstention route for passages that do not support a stable classification.

### 19.2.4 Resolve reports into events

News collections rarely provide one document per event. The same account may be syndicated, translated, updated, quoted by another outlet, or repeated in a retrospective report. Conversely, one article may describe several occurrences. The database therefore needs an event-resolution stage between verified records and analytical events.

AI can compare names, dates, places, actions, and source spans to generate possible matches. Event extraction research shows, however, that simple zero-shot prompting can perform poorly when reports contain ambiguity, hypothetical language, or several interacting actors.[^34] A match score should therefore open a review task instead of merging records automatically.

The **event resolution log** records every merge, split, and non-match. It links source-record identifiers to a stable event identifier and gives the rule, evidence, reviewer, and confidence category. It also records dependence. Five newspapers repeating one wire dispatch represent broad circulation, not five independent observations. Preserving that distinction prevents source abundance from becoming false corroboration.

### 19.2.5 Let the codebook learn without moving silently

An initial codebook should express the research hypotheses, but it should not be treated as complete. Early records may reveal unanticipated actors, mechanisms, event sequences, source effects, or confounders. AI can scan verified records and propose additional variables that distinguish rival explanations or capture recurrent variation.

Dynamic coding requires controlled change. The codebook should contain a stable core and an experimental extension layer. Core variables remain fixed during a declared release. Proposed variables enter the extension layer with a definition, rationale, allowed values, inclusion and exclusion rules, supporting examples, and an account of the hypothesis or comparison they serve. The **codebook version** must accompany every coded record.

A proposed variable should be tested on a validation sample before promotion. Reviewers ask whether it can be observed consistently, whether it duplicates an existing field, whether it encodes an inference as a fact, and whether it reflects reporting practice instead of the event itself. If promoted, the team either recodes earlier events or records that prior values are missing by design. Silent addition would make change over time indistinguishable from a change in measurement.

This workflow turns AI into a critic of the original design. The model may notice a missing variable, but it does not decide that the variable belongs in the database. That decision remains theoretical, empirical, and comparative.

### 19.2.6 Validate before scaling

Automated coding should be evaluated against researcher-coded material drawn from the intended corpus. The validation sample should include different periods, sources, languages, common classes, rare classes, and difficult boundary cases. A temporal holdout helps expose drift. A source holdout tests whether the system has learned one outlet’s style instead of the event concept.

Report performance by variable and class. Overall accuracy can conceal failure on rare but substantively important events. Precision, recall, and error types usually provide more useful guidance. Double-code a consequential or ambiguous subset, adjudicate disagreements, and record whether each error arose from retrieval, source quality, event resolution, the codebook, or the model. Contemporary event-data research treats this as a measurement problem, not merely a software benchmark.[^35]

Validation has a scope. A model that performs well on English national newspapers from one decade has not been validated for local-language archives or another period. Record the tested population, prompt, model, codebook version, and decision threshold. Revalidate after a material change to any of them.

### 19.2.7 Use Bayesian updating as a declared argument

Written evidence can change the relative plausibility of rival causal explanations. Bayesian reasoning makes this change explicit. Suppose (H_1) and (H_0) are rival explanations and (E) is a verified item of evidence. The update can be expressed as:

``` math
\frac{P(H_{1} \mid E)}{P(H_{0} \mid E)} = \frac{P(H_{1})}{P(H_{0})} \times \frac{P(E \mid H_{1})}{P(E \mid H_{0})}
```

The first ratio represents prior odds. The second is the **likelihood ratio**: how much more expected the evidence would be under one explanation than the other. Explicit Bayesian process tracing can discipline comparison among explanations, but priors and likelihoods are not mechanically supplied by a document.[^36]

AI can help prepare the reasoning. It can extract passages bearing on each hypothesis, identify temporal sequence, propose rival explanations, detect duplicated evidence, and ask what each hypothesis predicts. It can calculate posterior odds from declared inputs and run a sensitivity analysis across plausible likelihood ranges.

The researcher assigns the prior and likelihood judgments. The researcher also decides whether a report is independent, authentic, contemporaneous, and diagnostic. A percentage generated from model confidence is not a likelihood ratio. Research on confidence elicitation shows that a language model’s stated certainty requires separate calibration and cannot substitute for a causal model.[^37]

The Bayesian evidence table should therefore record the hypothesis pair, evidence identifier, provenance, predicted observation under each hypothesis, dependence group, likelihood range, rationale, reviewer, update, and sensitivity result. The model may draft alternatives for review. It may not convert fluent interpretation into causal probability.

## 19.3 Worked Example

Consider a project examining whether a campaign of coordinated attacks followed a central directive or emerged from local imitation. The source frame includes national and local newspapers, organizational statements, judicial records, and a digitized archive. Retrieval returns 8,000 documents. An AI-assisted classifier identifies 730 candidate records, while human verification accepts 412 and leaves 28 unresolved.

The event-resolution pass finds that many accepted records repeat the same wire stories. It also finds articles that combine several incidents in one retrospective account. Reviewers link the 412 verified records to 167 resolved events. The database retains every source relationship, but analytical counts operate on event identifiers instead of article counts.

The original codebook records date, location, actor, target, tactic, casualties, and claimed responsibility. During a pilot, the model repeatedly proposes three additional fields: prior local confrontation, evidence of tactical imitation, and evidence of communication before the event. The first two can be coded from defined written traces. The third is too inferential as phrased. The team revises it into separate observable fields for a documented meeting, a message, and an attributed statement. After a stratified validation sample, the new fields enter codebook version 1.1 and earlier events are recoded.

For causal analysis, similar tactics across several events initially appear to favor coordination. The evidence table reveals that newspapers copied descriptions from one source and that imitation predicts similarity as well. The likelihood ratio stays close to one. An authenticated message sent before several events would be more diagnostic if its content distinguishes a directive from general encouragement. The model helps compare these implications and calculate sensitivity across researcher-assigned ranges. It does not determine which mechanism caused the campaign.

The final database is smaller than the first extraction and stronger than a manually assembled spreadsheet. AI shortened retrieval, comparison, and preliminary coding. The audit chain preserved the difference between speed and evidence.

## 19.4 Try It

Choose a research question that could be represented as events. Write one paragraph defining the unit, the event boundary, the source frame, and the minimum evidence required for a verified record. Then create ten candidate records from a small, rights-compliant sample. Preserve a source span for every proposed field.

Resolve the ten records into events without using automatic merges. Record one merge, split, or non-match decision for each plausible pair. Identify shared wire copy, quotation, translation, or retrospective dependence.

Draft codebook version 0.1 from the research hypotheses. Ask an AI system to propose up to five additional variables that might distinguish rival explanations. For each proposal, require an observable definition, exclusion rule, two positive examples, one difficult boundary case, and the decision it would support. Reject at least one proposal and record why.

Finally, select two rival hypotheses and one verified item of written evidence. State what each hypothesis predicts, assign a transparent likelihood range, and calculate the posterior odds across that range. Repeat the calculation after treating two apparently separate reports as dependent. Explain why the answer changed or remained stable.

## 19.5 Guided AI Workflow

Use three bounded passes. In the extraction pass, provide the event definition, codebook version, required output schema, and rights-cleared text. Require the model to return candidate records with exact source spans, uncertainty markers, and an abstention option. In the challenge pass, provide de-identified candidate records and ask for likely duplicates, boundary violations, missing variables, and rival interpretations. In the causal pass, provide only verified evidence identifiers, hypothesis predictions, and researcher-declared likelihood ranges. Ask for arithmetic and sensitivity checks, not a causal verdict.

A usable codebook prompt is:

> Compare these verified records with codebook version 0.1. Propose no more than five additional variables that could distinguish the stated rival hypotheses. For each, provide an observable definition, allowed values, an exclusion rule, supporting record IDs, one boundary case, and the decision the variable would inform. Do not code the full corpus and do not treat an inference as an observed fact.

**Permitted input:** Rights-cleared source text, public records, verified metadata, redacted event descriptions, declared hypotheses, codebook versions, and stable record identifiers.\
**Do not provide:** Restricted archives, personal data, confidential allegations, protected participant material, or documents whose licenses prohibit external processing.\
**Verify:** Check every source span, metadata field, event match, promoted variable, dependence judgment, and causal evidence assignment against the underlying record. Validate automated codes on a stratified researcher-coded sample.\
**Record:** Save collection and query details, model and version, prompt, codebook version, candidate output, reviewer disposition, event resolution log, validation results, and accepted or rejected codebook changes.

The model should return structured candidates, not silently edit the database. A human-controlled import step provides the boundary between proposal and record.

## 19.6 Integrity Checkpoint

Speed can redistribute visibility. Large searchable newspapers may dominate because they are technically accessible, while local publications, minority languages, ephemeral media, and undigitized collections disappear. Audit the source frame before interpreting the event distribution.

Source reports can contain allegations, state narratives, strategic claims, and copied errors. Preserve attribution. Do not transform “officials alleged” into an event fact. Distinguish event variables from variables about the reporting process.

An event database can expose people who never consented to systematic aggregation. Public availability does not remove privacy, security, or ethical risk. Minimize personal data, document the lawful and ethical basis for processing, and restrict or aggregate sensitive fields when release could cause harm.

Dynamic coding can also produce retrospective confirmation. A variable proposed after seeing the outcome may be analytically useful, but its origin must be disclosed. Mark exploratory variables and test them against new material where possible.

## 19.7 Save the Artifact

Save six linked artifacts: the source frame and search log; the candidate record table with source spans; the verification register; the event resolution log; the versioned codebook with its change log; and the validation report. For causal work, add a Bayesian evidence table that preserves hypothesis predictions, dependence, likelihood ranges, rationales, and sensitivity results.

Each analytical export should name the source-frame version, codebook version, model-assisted workflow version, and validation report. Preserve stable identifiers so a correction to one source record can propagate to the resolved event and every downstream analysis.

Release only what rights, privacy, security, and ethics permit. A public methodological register can describe restricted evidence without exposing it.

## 19.8 Advanced Practice

A mature pipeline separates retrieval, extraction, verification, resolution, coding, and inference into distinct operations. Each operation can be rerun without silently overwriting the preceding layer. This structure supports multilingual retrieval, active learning, model comparison, and targeted human review.

Consider a model cascade. A low-cost system can rank documents, a stronger system can extract difficult candidates, and a researcher can adjudicate the consequential cases. Route rare classes, low-confidence outputs, conflicting source spans, and causal evidence to expert review. Measure how the routing rule changes both error and labor.

Test model and source drift. Recode a fixed benchmark after provider updates. Sample new records by period and outlet. Compare human disagreement with model error without treating one as a substitute for the other.

For causal inference, compare several defensible prior and likelihood specifications. Run the analysis with and without dependent reports, contested documents, and exploratory variables. The aim is not to manufacture a precise posterior. It is to show which evidence changes the argument, which assumptions carry the result, and what new observation would alter the conclusion.

AI improves an event database when it makes the pipeline faster and the transformations more visible. It weakens the database when convenience conceals where evidence ended and inference began.

# 20. AI and Research Integrity

## 20.1 A Division of Labor

Generative AI can accelerate parts of evidence mapping. It can propose synonyms, group candidate records, compare definitions, and question a stopping rule. These are acts of assistance. They are not transfers of authorship or responsibility.

The researcher defines the purpose. The researcher controls the material supplied to the system. The researcher verifies claims and sources. The researcher decides what enters the corpus. The researcher accounts for the result.

This division of labor is necessary because fluent output can contain fabricated references, unsupported inference, privacy disclosure, and bias inherited from training data or the prompt. Current risk guidance treats these as properties that require management across the system’s use, not as rare accidents.[^38]

## 20.2 Model-Neutral Workflows

The guide avoids instructions that depend on one product interface. A workflow states the research task, required input, prompt sequence, verification procedure, and audit record. The model may change. The scholarly obligation does not.

A useful prompt gives the system a bounded role. “Identify candidate dimensions missing from this question frame” is inspectable. “Research this topic for me” conceals the stages at which error can enter. Prompts should request candidates, alternatives, or critiques. They should not request certainty the system cannot establish.

Run more than one pass when the task matters. The first pass generates. The second challenges. The third compares the output with the evidence map. Repetition does not guarantee truth, but role separation makes error easier to see.

Model neutrality has a limit worth stating. The verification-heavy workflows in this guide assume access to a capable model, and capable models often cost money. The privacy fallback assumes a local or institutional system that many researchers do not have. Capability also varies by tool, language, and region. For these reasons the method does not depend on AI. The map, the search log, the evidence register, and the stopping rule stand on their own. A researcher without access to a frontier model loses an assistant, not the method.

## 20.3 Privacy and Data Minimization

Do not place material into an external system merely because it accepts text. Interview transcripts, archival restrictions, personal data, allegations, unpublished findings, and partner-owned datasets may carry legal and ethical limits. Removing names does not lift those limits. De-identification of qualitative data is unreliable, and re-identification is often possible from context alone. Under most data-protection regimes and ethics approvals, pseudonymized participant data remains regulated personal data, and many approvals and data agreements forbid sending it to a third-party processor at all. Consumer tools may also retain inputs or train on them. Before any participant-derived material enters an external system, confirm that the ethics approval and the data agreements permit third-party processing. Use an abstract description when the full record is unnecessary. Prefer a local or institutionally approved system when protection requires it. When in doubt, do not upload, and consult the ethics board or the data-protection officer.

The audit log records what category of material entered the system. It need not reproduce protected content. It should record the model, date, task, input description, relevant settings, output disposition, and human reviewer.

## 20.4 Verification

Verification follows the claim. A proposed publication must be located through a DOI resolver, library catalogue, publisher, or trusted index. A named archive must be checked through the institution. A quotation must be compared with the source. A classification must be traced to the evidence and decision rule.

An AI-generated reference is not a citation. It is a search lead.

The same rule applies to summaries. A model may produce an elegant account of a document while missing a qualification that changes its meaning. Verify against the original and record which passages support the summary.

## 20.5 Bias and Missing Perspectives

Models can reproduce the visibility structure of their training material. Well-indexed English-language institutions may appear central because they are easier for the system to name. Local archives, non-English terms, and informal records may disappear from the response. This weakness makes AI useful as one critic among several, never as the sole designer of a source map.

Ask what position the response assumes. Ask which actors it treats as authoritative. Ask which language and region dominate its suggestions. Then use domain expertise and human consultation to correct the map.

## 20.6 Reproducibility and Drift

The same prompt may produce different outputs across runs. A provider may change the model without preserving the prior version. Search-connected systems may draw on a changing index. The audit record should therefore support reconstruction of the decision, not promise exact reproduction of the text.

Preserve consequential outputs when terms permit. Record accepted and rejected suggestions. State when AI assistance changed the question, search vocabulary, source inventory, or stopping rule. The manuscript needs the decision trail more than it needs a transcript of every exchange.

## 20.7 The Standard

AI use is defensible when it makes judgment more visible. It fails when it hides judgment behind convenience.

# 21. From Notes to Research Infrastructure

## 21.1 A Library Begins to Remember

At 9:20 on the morning of November 29, 2022, a cluster of items entered my Readwise library. One promised “networked thought.” Another explained how smart notes could turn reading into writing. Others addressed exports, associative links, and the Zettelkasten. Their shared premise was simple: the researcher needed an external memory that preserved ideas beyond the moment of reading.[^39]

The tools changed. The underlying problem did not. A social scientist may spend years gathering articles, archival records, interview transcripts, observations, code, and partial arguments. The problem is not only how to store these materials. It is how to recover the right piece at the right time, reconstruct why it mattered, connect it to a changing question, and preserve the line from source to claim.

AI entered the same library within days. The early items treated it as a knowledge-aware writing assistant and an unusually productive partner for idea generation. The promise was speed and variation. The warning was already present: an output could be inventive and wrong at the same time.[^40]

I argue that PKM and AI solve different research problems. Personal knowledge management supplies persistent context, provenance, and continuity. AI reduces the cost of searching, comparing, transforming, and testing that context. Each remains incomplete without the other. PKM without computation can become an orderly archive that rarely produces an argument. AI without a governed knowledge base can produce fluent answers that have no stable relation to the research record.

Their integration creates something more useful than a better note-taking system or a more informed chatbot. It creates research infrastructure. The infrastructure remembers what the researcher has read. It records what the researcher decided. It lets machines perform bounded work across those records. It also preserves the human gates that separate a candidate from evidence and evidence from a claim.

This chapter develops that argument from an audit of my Readwise library. On July 27, 2026, the library contained 567 entries tagged `📄Academic Article`, 499 tagged `🗃️PKM`, and 3,196 tagged `🤖AI`. These labels overlap, and the AI category contains news, product announcements, social-media threads, and duplicate records as well as scholarly material. The counts therefore describe attention, not evidence. I use the complete PKM set, the connector-accessible academic and AI samples, their overlaps, and sixteen inspected records to reconstruct the movement from capture to research infrastructure.[^41]

## 21.2 From Capture to Connection

The first generation of PKM tools treated forgetting as the central constraint. Researchers read more than they could remember, saved more than they could retrieve, and divided related ideas among folders created at different moments. The proposed remedy was to externalize memory. Notes would become smaller, searchable, and linked. Daily writing would reduce the cost of capture. Backlinks would allow an idea recorded for one purpose to reappear in another.

This was a major improvement over a hierarchy of project folders. A folder asks where a note belongs. A network asks what the note is related to. That difference matters in social research because the same source can perform several jobs. An interview may provide evidence about an event, reveal an actor’s vocabulary, expose a retrospective justification, and suggest a new comparison. A single folder cannot express all four relations.

The early library also connected note-making to writing. The point was not to collect quotations. It was to leave one’s future self a usable intellectual object: a claim, a question, a disagreement, a definition, or an unresolved connection. One item from December 2022 defined PKM as a response to information abundance and unreliable memory. Its stronger implication was that thinking had to become visible outside the head before it could become cumulative.[^42]

For academic work, this first phase contributed four capacities. It preserved memory across semesters and projects. It let concepts travel between literatures. It separated source material from the researcher’s interpretation. It made intellectual development observable through dated notes and links.

These capacities support more than productivity. They support reflexivity. A qualitative researcher can return to an early memo and see which explanation once seemed plausible, which case disrupted it, and when the coding scheme changed. A historical researcher can distinguish a contemporaneous reading from an interpretation formed after later evidence appeared. A collaborative team can trace a concept to the person, source, and decision that introduced it.

But connection did not solve selection. A graph could display thousands of notes without explaining which ones bore on a claim. A search could find every mention of “violence” without distinguishing an event report from a theoretical definition. PKM made the research memory durable. It did not yet make that memory easy to interrogate.

## 21.3 When AI Entered the Notebook

The next phase reduced the cost of transforming source material. OCR converted scanned pages into text. Speech recognition converted interviews and lectures into transcripts. Translation brought sources in additional languages into a shared workspace. Summarization produced initial descriptions. Semantic search retrieved passages that did not share the researcher’s exact vocabulary.

The library recorded both the gain and the danger. In December 2023, an item described using a multimodal model to transcribe a handwritten journal. The system outperformed conventional text recognition because it used context to infer unclear words. It also changed the date from 20 to 28. Context rescued words whose meaning could be inferred. Context corrupted a number that could not.[^43]

This is the central methodological problem of AI-assisted transformation. The same capacity that repairs incomplete text can invent plausible detail. A model may standardize an institutional name correctly in ninety-nine records and silently merge two different organizations in the hundredth. It may translate a political term fluently while erasing the ambiguity that made the term analytically important. It may summarize an interview and omit the hesitation that changes how the answer should be read.

The solution is not to reject transformation. It is to preserve the original, the transformed object, the procedure, and the verification status as separate artifacts. The scan remains the source. The OCR text remains a derivative. A correction log records changes. A human validates fields whose error would alter the analysis.

The same period changed scholarly reading. Entries in the library moved from global search and backlinks toward semantic readers, citation maps, paper explainers, and interfaces that connected articles to videos and related work. The PDF remained the publication object, but it no longer had to remain the research interface.[^44]

For social scientists, this shift expanded access to evidence whose form had once made it prohibitively expensive. A researcher can now search a large newspaper archive, transcribe oral histories, extract tables from reports, compare terminology across languages, and locate names in thousands of pages. A recent library entry describing the digitization of nearly twenty million historical census images shows the scale of this change. It also shows why the work remains a research design problem: models, prompts, schemas, validation samples, and error rates shape the resulting data.[^45]

AI made more material computable. It did not make all computed material evidence.

## 21.4 From Retrieval to Workflow

By 2025, the library’s focus had shifted from individual features to academic workflows. One entry paired a citation manager with a local Markdown vault. The citation manager held bibliographic authority and source files. The vault held reading notes, concepts, project memos, and draft arguments. The value came from the division of labor, not from forcing one application to perform every function.[^46]

Another entry placed an AI agent inside a structured note environment and asked it to find weaknesses in arguments drawn from writing, meetings, and journals. This was a different relationship between researcher and machine. The model no longer responded only to a prompt. It operated over a body of prior material and returned an analytical artifact for inspection.[^47]

The change can be stated in three sentences. First, PKM externalized memory. Next, AI made that memory searchable and transformable. Then workflows connected repeated operations to named inputs, outputs, and checks.

This is where the integration becomes valuable for academic research. A prompt is disposable. A workflow can be inspected, repeated, compared, and revised. A prompt asks for sources. A workflow receives a review protocol, maps vocabulary, searches approved databases, records every query, stages candidates, resolves identities, tests coverage, and stops before final inclusion. A prompt asks for themes. A workflow preserves the transcript, coding instructions, proposed codes, rejected codes, uncertainty, and researcher approval.

The distinction also changes how researchers evaluate AI. The unit of analysis is not the model alone. It is the system consisting of the model, context, tools, permissions, stopping rule, output schema, verifier, and human gate. A weaker model inside a well-specified workflow may produce more trustworthy research artifacts than a stronger model inside an unconstrained conversation.

## 21.5 Persistent Context and the Agentic Turn

The 2026 PKM records in the library differ sharply from the early collection. Among the 79 PKM entries saved that year, 48 also carry the AI tag, 56 refer to Obsidian, and 14 concern agents. The object of interest is no longer the isolated note. It is the relationship between a durable, local knowledge base and an agent that can act across it.

Several records describe the vault as a permanent memory layer. A project file states the question, scope, standards, active decisions, and prohibited actions. Markdown notes preserve the source record. An agent reads the smallest set of files required for a task. Repeated procedures become skills. Scheduled workflows process an inbox, prepare a briefing, identify connections, or stage a research memo.[^48]

One of the strongest entries in this group proposes a continuous system in which Readwise supplies captured material, Obsidian preserves it, an AI layer reasons across it, and an automation layer moves artifacts between stages. My note on that item identified the deeper claim: knowledge gains value over time when the cost of maintenance falls and new work can repeatedly encounter old material.[^49]

The attractive phrase is “a second brain that thinks back.” The phrase is useful, but it can mislead. A vault does not become reliable because an agent can read it. Old notes may contain errors. Duplicates may look like corroboration. A summary may have lost the source’s qualification. A private record may be outside the agent’s authorized scope. Persistent context amplifies whatever the system contains.

The operative design therefore requires three components. The first is a specification that defines acceptable work before execution. The second is a knowledge base that supplies bounded context and authoritative artifacts. The third is a verifier that tests the output against the specification. A recent library item formulated this pattern as “spec, verifier, knowledge base.” It also recorded a decisive warning: a verifier measures only what it was designed to measure.[^50]

This pattern now appears in more ambitious claims about AI scientists. One saved item distinguishes retrieval, search within a fixed schema, and discovery that changes the schema itself. Its proposal remains provisional for the social sciences, but the distinction is productive. Retrieval finds a known object. Search explores a defined space. Discovery proposes that the space was defined incorrectly. Only the third requires the researcher to reconsider the concepts, boundaries, or variables that organized the project.[^51]

AI may propose such a revision. It may not ratify it.

## 21.6 What PKM Contributes to Social Science

Personal knowledge management contributes temporal depth. Social-science projects often outlast software, funding cycles, and individual bursts of attention. A durable note records not only a result but the state of the inquiry when the result appeared. This matters when a concept changes meaning or when later events make an earlier interpretation look inevitable.

PKM contributes conceptual continuity. Political and social concepts travel under different names across disciplines, countries, institutions, and periods. Linked notes can connect an indigenous term, an archival label, a theoretical category, and a coding variable without pretending they are identical.

PKM contributes provenance. A useful research note identifies its source, locator, date of capture, transformation history, and relation to the project. The note does not replace the source. It points back to it.

PKM contributes negative evidence. Researchers usually save what supports an argument. A governed system can also preserve failed searches, rejected explanations, excluded cases, unresolved contradictions, and missing records. This negative evidence protects against repeating work and against rewriting the research history after the conclusion becomes clear.

The same principle applies at institutional scale. A retrospective account of a long-running conflict-research program attributes its achievements not to data volume alone but to the combination of social-scientific method, practitioner knowledge, flexible support, and contextual interpretation. Data became useful because an institutional memory connected collection to the circumstances that gave the records meaning.[^52]

PKM contributes cumulative comparison. A case memo can share fields with other case memos while retaining material that does not fit the common schema. This combination is important in qualitative and comparative work. Structure supports comparison. Free text preserves surprise.

Finally, PKM contributes ownership and durability when it relies on open, inspectable formats. Plain-text notes can survive the application that created them. They can be versioned, searched, diffed, backed up, and read by both humans and machines. This is not a preference for one note application. It is a preservation decision.

## 21.7 What AI Contributes

AI contributes scale. It can prepare candidate records from more documents than one researcher can read line by line. It can locate names, dates, events, institutions, quotations, and relations across a large corpus. Candidate is the operative word. Extraction creates material for validation.

AI contributes flexible retrieval. Keyword search depends on shared vocabulary. Language models can suggest synonyms, historical terms, translations, rival concepts, and proxy measures. This capacity can prevent a false gap produced by a poor query. It can also drift beyond the review’s scope, which is why vocabulary expansion must remain logged and reviewable.

AI contributes comparison. A model can apply the same questions to a set of documents, identify points of agreement and conflict, and prepare a matrix that a researcher can inspect. It can ask which source supports a date, which cases violate an emerging pattern, or which paragraphs depend on one unverified claim.

AI contributes transformation. OCR, transcription, translation, classification, entity resolution, and structured extraction can move evidence among forms. The result becomes methodologically useful only when the transformation retains a link to the original.

AI contributes iteration. It can rerun a procedure after the codebook changes, compare versions, and report which records changed. This makes dynamic coding possible without hiding the consequences of revision.

AI also contributes disciplined opposition when instructed to do so. It can search for disconfirming evidence, propose rival mechanisms, detect scope changes, and ask which observation would distinguish two explanations. It cannot decide the substantive importance of those findings. But it can make it harder for a researcher to avoid them.

## 21.8 The PKM-AI Research Loop

The integrated system works when every stage produces an artifact and every consequential transition includes a human gate. The following PKM-AI research loop can support a literature review, archival project, interview study, event database, or comparative case analysis.

| Stage | Durable artifact | Permitted AI work | Human gate |
|----|----|----|----|
| Bound | Versioned project-context packet | Test ambiguity; propose missing terms and boundaries | Approve the question, scope, ethics, and stopping rule |
| Capture | Source note with stable identity and locator | Import metadata; transcribe or OCR into a derivative file | Confirm rights, identity, and source-derivative relation |
| Distill | Claim, evidence, question, and uncertainty notes | Propose summaries, entities, claims, and contradictions | Compare each consequential claim with the source |
| Connect | Concept map and evidence map | Suggest links, aliases, rival concepts, and missing source families | Accept relations and reject false equivalence |
| Compute | Candidate register, query log, or coding table | Search, classify, compare, extract, and propose new variables | Approve inclusion, exclusions, codebook changes, and promotions |
| Verify | Validation sample, discrepancy log, and coverage memo | Run schema checks, known-item tests, consistency checks, and adversarial review | Judge adequacy, residual error, and whether to stop |
| Express | Versioned manuscript, dataset, appendix, or public release | Draft from approved artifacts; generate alternative explanations and formats | Take responsibility for claims, citations, interpretation, and release |

The loop is recursive. A contradiction found during writing may change the concept map. A new archival term may change the search protocol. A validation failure may require a new codebook version. The system should permit revision while preserving the prior state.

Consider a researcher building an event database from daily newspapers. The PKM layer holds the research question, source inventory, codebook versions, decisions, and notes about access or political context. The AI layer scans permitted newspapers, stages event candidates, extracts dates and actors, proposes additional variables, and identifies possible duplicates. The researcher validates a sample, resolves ambiguous events, approves codebook changes, and records why a candidate entered or left the verified corpus.

The result is not merely a larger dataset. It is a dataset with a memory.

## 21.9 An Operative Chapter Exercise

This chapter can be tested on one active research question. Begin with no more than twenty source notes. Write a one-page context packet containing the question, population, period, concepts, source boundaries, ethics, current artifact versions, and decision authority. Select five known items that any adequate search must recover.

Ask an AI system to map the vocabulary and stage a candidate register. Require a stable source identifier, discovery route, bibliographic status, relevance rationale, uncertainty, and verification status for every row. Do not permit a final inclusion field.

Inspect the result in three passes. First, check identity and provenance. Second, look for missing terms, false equivalences, and scope drift. Third, examine what the system failed to recover. Record every correction in an audit log and rerun the same task with the revised context packet.

The exercise succeeds if the second run becomes easier to inspect and if the record explains why it changed. It does not succeed because the prose sounds better or because the model returns more candidates.

The downloadable [Skills and Agents Lab](skills-and-agents-lab.qmd) provides a literature-discovery skill, bounded scout agent, project-context template, three synthetic benchmarks, and a failure report for this exercise.

## 21.10 What AI Must Not Do

AI must not convert a retrieval failure into a claim that no literature exists. It must not treat repeated records as independent corroboration. It must not overwrite the canonical note, codebook, or corpus without a versioned proposal. It must not use restricted or personal material merely because that material is technically accessible. It must not hide uncertainty behind a completed field.

AI must not collapse source, derivative, note, and claim into one object. It must not turn a retrospective interview into a contemporaneous record. It must not translate a disputed concept into a stable English equivalent without preserving the original. It must not infer causal direction from narrative order alone.

Most of all, AI must not become the unnamed author of consequential research decisions. A final inclusion, exclusion, codebook revision, causal judgment, or public claim requires a responsible researcher. The system may prepare the decision. It may preserve the reasons. It may expose inconsistency. The researcher still decides.

## 21.11 The Research System That Remembers

The evolution recorded in my library begins with a familiar anxiety: too much to read, too much to remember, and too many tools. It ends, for now, with a different question. How should a researcher govern a system that can read and act across years of accumulated intellectual work?

The answer is not a fully autonomous scholar. It is a partnership built from asymmetry. PKM remembers slowly and precisely. AI processes quickly and probabilistically. PKM preserves the path. AI explores possible paths. PKM holds the source record. AI prepares transformations and comparisons. Human judgment defines the question, interprets the evidence, and accepts responsibility for the claim.

This integration pushes social research forward by changing the feasible scale of careful work. It lets one researcher inspect more archives, follow more conceptual variants, compare more cases, and rerun more coding decisions. But the gain comes from governed iteration, not automation alone.

The durable principle is simple. Build a knowledge base that another person can inspect. Give AI a bounded task within that base. Require it to return an artifact, not an answer. Verify the artifact against the source and the specification. Then write the next version without erasing the last.

# 22. Skills and Agents Lab

## 22.1 Method in the Book, Procedure in the Lab

The book explains why a literature search requires a protocol, multiple discovery routes, verified bibliographic identities, a coverage argument, and a human stopping decision. The lab turns that method into inspectable working objects. It does not transfer scholarly authority to an automated system.

Release **0.1.0** is a pilot. It operationalizes one bounded part of the literature module: moving from an approved review protocol to a staged register of bibliographic candidates. The skill and agent cannot decide final eligibility, declare a research gap, or promote a record into the verified corpus.

[Download ZIP 0.1.0](../downloads/skills-and-agents-lab-v0.1.0.zip) [Verify checksum](../downloads/skills-and-agents-lab-v0.1.0.zip.sha256) [Inspect source](https://github.com/pedahzur/from-question-to-evidence/tree/revise/referee-pass-2026-07-14/lab)

## 22.2 What the Release Contains

### 22.2.1 Literature-discovery skill

The skill receives an approved review protocol, a versioned project-context packet, and a list of permitted sources. It maps vocabulary, plans and records discovery routes, stages candidates, resolves bibliographic identities, tests known-item and route coverage, and returns the work to a researcher.

Its outputs are:

1.  a candidate register;
2.  a query log;
3.  a coverage memo;
4.  an unresolved-leads file.

A bundled validator checks that candidate registers contain provenance and verification fields and do not contain final-eligibility fields.

### 22.2.2 Bounded literature-scout agent

The scout is a read-only executor. It can read approved local artifacts and search public sources. It cannot write project files, change a protocol, access protected material, make a final inclusion decision, or modify a corpus. If the work requires one of those actions, it stops and returns a bounded question.

This is a deliberate division of labor. The skill holds the reusable procedure. The agent executes one work order in a fresh context. The researcher controls the gates.

### 22.2.3 Project-context packet

The template separates context into three layers:

- a **stable layer** for the question, scope, concepts, evidence standards, ethics, and decision authority;
- a **current-state layer** for active artifact versions, accepted decisions, unresolved disputes, and coverage limits;
- a **task layer** for one work order, its permitted sources, required output, and stopping rule.

The packet points to authoritative artifacts. It is not itself evidence and should not contain an entire project archive.

## 22.3 Three Synthetic Benchmarks

The release includes small, inspectable cases rather than an opaque aggregate score. All names, records, identifiers, and source locations are synthetic.

| Benchmark | What it tests | Failure condition |
|----|----|----|
| Known-item recovery | Recover known records, resolve an exact duplicate, and preserve both discovery routes | A route is erased or recovery is called comprehensive |
| False-gap prevention | Expand vocabulary through a conceptual proxy and an approved Spanish term | A zero-result English query becomes a field-level gap claim |
| Boundary and abstention | Preserve a temporal scope signal, refuse restricted material, and isolate an unsupported citation | Metadata is invented, a final exclusion is made, or protected material is accessed |

These fixtures test the procedure’s boundaries. They do not establish performance on real databases. A later release should report recall, false-exclusion rates, bibliographic-resolution errors, labor, cost, and cross-language performance on an independently prepared corpus.

## 22.4 What the AI Got Wrong

The package contains an explicit failure report. The authoring run exposed five risks:

- a plausible but unsupported citation entering the candidate register;
- a zero-result query becoming a research-gap claim;
- deduplication erasing the route by which a source was found;
- a scope signal becoming a final eligibility decision;
- broad context encouraging access to a restricted artifact.

Each failure is connected to a control in the skill, agent, schema, template, or benchmark. Residual risks remain visible. The report also states what this pilot has not established.

## 22.5 Use and Inspect the Package

Unpack the ZIP and begin with `MANIFEST.yml`. The manifest names every public file, the release status, the benchmark cases, and the licenses.

To install the skill in Codex, copy the complete `skills/literature-discovery/` directory into the local Codex skills directory. Keep the folder intact so its references, UI metadata, and validator remain available. The `agents/literature-scout.md` file can be installed in an agent host that supports Markdown agent definitions or used directly as a transparent work-order specification.

Before using the workflow on a real review:

1.  complete and approve the project-context packet;
2.  adapt the source list and stopping rule to the review;
3.  run the synthetic benchmarks;
4.  test the skill on a researcher-coded sample;
5.  inspect false exclusions, invented identities, and route loss;
6.  keep all outputs in staging until a named researcher approves them.

## 22.6 Feedback and Revision

This lab is intended to improve through reported use rather than silent rewriting. Every report should name the package version, affected artifact, input conditions, observed output, expected behavior, and privacy status.

[Report a problem](https://github.com/pedahzur/from-question-to-evidence/issues/new?template=lab-problem.yml) [Propose a revision](https://github.com/pedahzur/from-question-to-evidence/issues/new?template=lab-revision.yml)

Do not attach participant data, credentials, restricted archives, confidential manuscripts, or copyrighted full text. Use a synthetic or redacted reproduction. Accepted changes should identify their evidentiary or benchmark basis and appear in the changelog and a numbered release.

# 23. Building the Full Field Guide

## 23.1 What the Current Modules Establish

The evidence map connects an intellectual question to the practical work of finding material. *Literature as Evidence* carries that logic into discovery, reading, comparison, and synthesis. Together, they show that one page pattern can support distinct tasks while keeping method separate from volatile products, giving AI bounded roles, and leaving a record another researcher can inspect.

The two modules share one architecture at different lengths. The evidence map runs seven stages and stops before analysis. The literature review runs six stages and includes reading, because synthesis is its product. Grouped by function, they align as follows.

| Function | Evidence map | Literature review |
|----|----|----|
| Frame | Frame the question | Define the review |
| Decompose | Decompose into concepts | Map concepts and vocabulary |
| Discover | Map source families; search iteratively | Discover through multiple routes |
| Evaluate | Evaluate evidence | Evaluate sources and claims |
| Read | Outside this module | Read, annotate, and compare |
| Close | Test coverage; produce the map | Synthesize, audit, and stop |

The evidence map devotes two stages to discovery where the review devotes one, because a collection project separates who could have recorded evidence from how to search for it. The review adds a reading stage because it must interpret what it finds.

The modules also reveal what remains outside the draft. They do not collect an interview, preserve a website, prepare a full archival corpus, or write the final empirical analysis. The synthesis chapter extends the literature workflow into open, living, and quantitative reviews. The bridge chapter on event databases introduces document extraction, dynamic coding, validation, and explicit causal updating. Each still requires fuller treatment across source types and analytical traditions.

## 23.2 The Full Field Guide

The next module treats collection as evidence. It addresses documents, interviews, observations, images, audio, video, and web material. It connects capture to consent, metadata, storage, naming, backup, preservation, and chain of custody. A composite oral-history case will show where evidence co-produced with participants requires different decisions from retrieved documentary evidence.

A preparation module will extend the event-database chapter across transcription, OCR, translation, coding, memoing, temporal ordering, entity resolution, and other conversions of unstructured records into structured fields. The original project devoted substantial attention to this border between qualitative material and databases. We will reconstruct that contribution around transformations whose lineage remains visible.

An analysis module will resist a false division between qualitative and quantitative work. Researchers move between close reading, comparison, counting, visualization, and model-based inference. The relevant distinction concerns the claim and evidence, not the brand of software.

A communication module will cover manuscripts, presentations, public data, visual explanation, repositories, and long-term access. Sharing is not the final act after research. Decisions made during collection determine what can later be verified, reused, or protected.

## 23.3 A Hebrew Edition

English remains the canonical language during the pilot. A Hebrew edition should follow after the content model and navigation stabilize. Translation will require more than sentence substitution. Search terms, institutional examples, interfaces, and right-to-left design must be adapted. Stable page identifiers will keep the two editions connected without forcing them to change at the same pace.

## 23.4 An Invitation

This draft is an argument and a test. It argues that researchers need a visible structure between question, corpus, analysis, and claim. It tests whether two different modules can carry novices and experienced scholars through the same page pattern at different depths.

The next step is both editorial and empirical. We will test the current modules with readers, carry the municipal oral-history example through every stage, and build the Collection as Evidence module from the strongest legacy material.

The old project began with abundance. The revived project begins with limits, artifacts, and reviewable decisions. This is progress.

# 24. References

Autio, Chloe, Reva Schwartz, Jesse Dunietz, Shomik Jain, Martin Stanley, Elham Tabassi, Patrick Hall, and Kamie Roberts. “Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile.” National Institute of Standards and Technology, 2024. <https://doi.org/10.6028/NIST.AI.600-1>.

Beelen, Kaspar, Jon Lawrence, Daniel C. S. Wilson, and David Beavan. “Bias and Representativeness in Digitized Newspaper Collections: Introducing the Environmental Scan.” *Digital Scholarship in the Humanities* 38, no. 1 (2023): 1–22. <https://doi.org/10.1093/llc/fqac037>.

Blaizot, Aymeric, Sajesh K. Veettil, Pantakarn Saidoung, Carlos Francisco Moreno-Garcia, Nirmalie Wiratunga, Magaly Aceves-Martins, Nai Ming Lai, and Nathorn Chaiyakunapruk. “Using Artificial Intelligence Methods for Systematic Review in Health Sciences: A Systematic Review.” *Research Synthesis Methods* 13, no. 3 (2022): 353–62. <https://doi.org/10.1002/jrsm.1553>.

Booth, Andrew, Anthea Sutton, and Diana Papaioannou. *Systematic Approaches to a Successful Literature Review*. 2nd ed. London: SAGE Publications, 2016.

Brandt, Patrick T., and Marcus Sianan. “Measurement of Event Data from Text.” *Frontiers in Political Science* 6 (2025): 1453640. <https://doi.org/10.3389/fpos.2024.1453640>.

Braun, Virginia, and Victoria Clarke. “One Size Fits All? What Counts as Quality Practice in (Reflexive) Thematic Analysis?” *Qualitative Research in Psychology* 18, no. 3 (2021): 328–52. <https://doi.org/10.1080/14780887.2020.1769238>.

Cai, Erica, and Brendan O’Connor. “A Monte Carlo Language Model Pipeline for Zero-Shot Sociopolitical Event Extraction.” In *NeurIPS 2023 Workshop on Instruction Tuning and Instruction Following*, 2023. <https://doi.org/10.48550/arXiv.2305.15051>.

Elliott, Julian H., Anneliese Synnot, Tari Turner, Mark Simmonds, Elie A. Akl, Steve McDonald, Georgia Salanti, et al. “Living Systematic Review: 1. Introduction, the Why, What, When, and How.” *Journal of Clinical Epidemiology* 91 (2017): 23–30. <https://doi.org/10.1016/j.jclinepi.2017.08.010>.

Enders, Walter, Todd Sandler, and Khusrav Gaibulloev. “Domestic Versus Transnational Terrorism: Data Decomposition and Dynamics.” *Journal of Peace Research* 48, no. 3 (2011): 319–37. <https://doi.org/10.1177/0022343311398926>.

Fairfield, Tasha, and Andrew E. Charman. “Explicit Bayesian Analysis for Process Tracing: Guidelines, Opportunities, and Caveats.” *Political Analysis* 25, no. 3 (2017): 363–80. <https://doi.org/10.1017/pan.2017.14>.

Gerring, John. *Social Science Methodology: A Unified Framework*. 2nd ed. Cambridge: Cambridge University Press, 2012.

Gilardi, Fabrizio, Meysam Alizadeh, and Maël Kubli. “ChatGPT Outperforms Crowd Workers for Text-Annotation Tasks.” *Proceedings of the National Academy of Sciences* 120, no. 30 (2023): e2305016120. <https://doi.org/10.1073/pnas.2305016120>.

Grant, Maria J., and Andrew Booth. “A Typology of Reviews: An Analysis of 14 Review Types and Associated Methodologies.” *Health Information*\
*& Libraries Journal* 26, no. 2 (2009): 91–108. <https://doi.org/10.1111/j.1471-1842.2009.00848.x>.

Greenhalgh, Trisha, and Richard Peacock. “Effectiveness and Efficiency of Search Methods in Systematic Reviews of Complex Evidence: Audit of Primary Sources.” *BMJ* 331, no. 7524 (2005): 1064–65. <https://doi.org/10.1136/bmj.38636.593461.68>.

Hedges, Larry V., Elizabeth Tipton, and Matthew C. Johnson. “Robust Variance Estimation in Meta-Regression with Dependent Effect Size Estimates.” *Research Synthesis Methods* 1, no. 1 (2010): 39–65. <https://doi.org/10.1002/jrsm.5>.

Irsova, Zuzana, Hristos Doucouliagos, Tomas Havranek, and T. D. Stanley. “Meta-Analysis of Social Science Research: A Practitioner’s Guide.” *Journal of Economic Surveys* 38, no. 5 (2024): 1547–66. <https://doi.org/10.1111/joes.12595>.

Lebo, Timothy, Satya Sahoo, and Deborah McGuinness. “PROV-O: The PROV Ontology.” W3C Recommendation. World Wide Web Consortium, 2013. <https://www.w3.org/TR/prov-o/>.

Littell, Julia H. “Conceptual and Practical Classification of Research Reviews and Other Evidence Synthesis Products.” *Campbell Systematic Reviews* 14, no. 1 (2018): 1–21. <https://doi.org/10.4073/cmdp.2018.1>.

Liu, Nelson F., Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, and Percy Liang. “Lost in the Middle: How Language Models Use Long Contexts.” *Transactions of the Association for Computational Linguistics* 12 (2024): 157–73. <https://doi.org/10.1162/tacl_a_00638>.

Malterud, Kirsti, Volkert Dirk Siersma, and Ann Dorrit Guassora. “Sample Size in Qualitative Interview Studies: Guided by Information Power.” *Qualitative Health Research* 26, no. 13 (2016): 1753–60. <https://doi.org/10.1177/1049732315617444>.

Marshall, Iain J., and Byron C. Wallace. “Toward Systematic Review Automation: A Practical Guide to Using Machine Learning Tools in Research Synthesis.” *Systematic Reviews* 8, no. 1 (2019): 163. <https://doi.org/10.1186/s13643-019-1074-9>.

Moreau, David, and Beau Gamble. “Conducting a Meta-Analysis in the Age of Open Science: Tools, Tips, and Practical Recommendations.” *Psychological Methods* 27, no. 3 (2022): 426–32. <https://doi.org/10.1037/met0000351>.

National Consortium for the Study of Terrorism and Responses to Terrorism. “Global Terrorism Database Codebook: Methodology Inclusion Criteria and Variables,” 2024. <https://www.start.umd.edu/gtd/downloads/Codebook.pdf>.

Page, Matthew J., Joanne E. McKenzie, Patrick M. Bossuyt, Isabelle Boutron, Tammy C. Hoffmann, Cynthia D. Mulrow, et al. “The PRISMA 2020 Statement: An Updated Guideline for Reporting Systematic Reviews.” *BMJ* 372 (2021): n71. <https://doi.org/10.1136/bmj.n71>.

Pangakis, Nicholas, Samuel Wolken, and Sergio Fasching. “Automated Annotation with Generative AI Requires Validation.” *arXiv*, 2023. <https://doi.org/10.48550/arXiv.2306.00176>.

Park, Joon Sung, Joseph C. O’Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, and Michael S. Bernstein. “Generative Agents: Interactive Simulacra of Human Behavior.” In *Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology*, 1–22, 2023. <https://doi.org/10.1145/3586183.3606763>.

Pigott, Terri D., and Joshua R. Polanin. “Methodological Guidance Paper: High-Quality Meta-Analysis in a Systematic Review.” *Review of Educational Research* 90, no. 1 (2020): 24–46. <https://doi.org/10.3102/0034654319877153>.

Polanin, Joshua R., Emily A. Hennessy, and Sho Tsuji. “Transparency and Reproducibility of Meta-Analyses in Psychology: A Meta-Review.” *Perspectives on Psychological Science* 15, no. 4 (2020): 1026–41. <https://doi.org/10.1177/1745691620906416>.

Rethlefsen, Melissa L., Shona Kirtley, Siw Waffenschmidt, Ana Patricia Ayala, David Moher, Matthew J. Page, and Jonathan B. Koffel. “PRISMA-s: An Extension to the PRISMA Statement for Reporting Literature Searches in Systematic Reviews.” *Systematic Reviews* 10, no. 1 (2021): 39. <https://doi.org/10.1186/s13643-020-01542-z>.

Roberts, Hal, Rahul Bhargava, Linas Valiukas, Dennis Jen, Momin M. Malik, Cindy Bishop, Emily B. Ndulue, et al. “Media Cloud: Massive Open Source Collection of Global News on the Open Web.” *Proceedings of the International AAAI Conference on Web and Social Media* 15, no. 1 (2021): 1034–45. <https://doi.org/10.1609/icwsm.v15i1.18127>.

Saunders, Benjamin, Julius Sim, Tom Kingstone, Shula Baker, Jackie Waterfield, Bernadette Bartlam, Heather Burroughs, and Clare Jinks. “Saturation in Qualitative Research: Exploring Its Conceptualization and Operationalization.” *Quality & Quantity* 52 (2018): 1893–1907. <https://doi.org/10.1007/s11135-017-0574-8>.

Snyder, Hannah. “Literature Review as a Research Methodology: An Overview and Guidelines.” *Journal of Business Research* 104 (2019): 333–39. <https://doi.org/10.1016/j.jbusres.2019.07.039>.

Sousa, M. Sharmila A., Sasha Peiris, Mabel F. Figueiró, Michelle M. Haby, Ana Cyntia Baraldi, Ludovic Reveiz, and João Paulo Souza. “The Landscape of Artificial Intelligence Tools and Platforms for Evidence Synthesis: A Scoping Review.” *Systematic Reviews* 15, no. 1 (2026): 82. <https://doi.org/10.1186/s13643-025-02842-y>.

Uttley, Lesley, Yuliang Weng, and Louise Falzon. “What’s the Meta Now? More Updates on the Problems with Systematic Reviews.” *Journal of Clinical Epidemiology* 198 (2026): 112393. <https://doi.org/10.1016/j.jclinepi.2026.112393>.

Wohlin, Claes. “Guidelines for Snowballing in Systematic Literature Studies and a Replication in Software Engineering.” In *Proceedings of the 18th International Conference on Evaluation and Assessment in Software Engineering*, 1–10. Association for Computing Machinery, 2014. <https://doi.org/10.1145/2601248.2601268>.

Xiong, Miao, Zhiyuan Hu, Xinyang Lu, Yifei Li, Jie Fu, Junxian He, and Bryan Hooi. “Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs.” In *The Twelfth International Conference on Learning Representations*, 2024. <https://openreview.net/forum?id=gjeQKFxFpZ>.

Yao, Shunyu, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao. “ReAct: Synergizing Reasoning and Acting in Language Models.” In *The Eleventh International Conference on Learning Representations*, 2023. <https://openreview.net/forum?id=WE_vluYUL-X>.

Zaks, Sherry. “Updating Bayesian(s): A Critical Evaluation of Bayesian Process Tracing.” *Political Analysis* 29, no. 1 (2021): 58–74. <https://doi.org/10.1017/pan.2020.10>.

Ziems, Caleb, William Held, Omar Shaikh, Jiaao Chen, Zhehao Zhang, and Diyi Yang. “Can Large Language Models Transform Computational Social Science?” *Computational Linguistics* 50, no. 1 (2024): 237–91. <https://doi.org/10.1162/coli_a_00502>.

[^1]: The formal vocabulary of entities, activities, and agents follows the W3C provenance model. See Timothy Lebo, Satya Sahoo, and Deborah McGuinness, “PROV-O: The PROV Ontology,” W3C Recommendation (World Wide Web Consortium, 2013), <https://www.w3.org/TR/prov-o/>.

[^2]: For current reporting standards on information sources, search strategies, and record management, see Melissa L. Rethlefsen et al., “PRISMA-s: An Extension to the PRISMA Statement for Reporting Literature Searches in Systematic Reviews,” *Systematic Reviews* 10, no. 1 (2021): 39, <https://doi.org/10.1186/s13643-020-01542-z> and Matthew J. Page et al., “The PRISMA 2020 Statement: An Updated Guideline for Reporting Systematic Reviews,” *BMJ* 372 (2021): n71, <https://doi.org/10.1136/bmj.n71>.

[^3]: See National Consortium for the Study of Terrorism and Responses to Terrorism, “Global Terrorism Database Codebook: Methodology Inclusion Criteria and Variables,” 2024, <https://www.start.umd.edu/gtd/downloads/Codebook.pdf>.

[^4]: See Walter Enders, Todd Sandler, and Khusrav Gaibulloev, “Domestic Versus Transnational Terrorism: Data Decomposition and Dynamics,” *Journal of Peace Research* 48, no. 3 (2011): 319–37, <https://doi.org/10.1177/0022343311398926>.

[^5]: See Enders, Sandler, and Gaibulloev.

[^6]: See National Consortium for the Study of Terrorism and Responses to Terrorism, “Global Terrorism Database Codebook”.

[^7]: See Rethlefsen et al., “PRISMA-s”.

[^8]: See National Consortium for the Study of Terrorism and Responses to Terrorism, “Global Terrorism Database Codebook”.

[^9]: See Enders, Sandler, and Gaibulloev, “Domestic Versus Transnational Terrorism”.

[^10]: See Benjamin Saunders et al., “Saturation in Qualitative Research: Exploring Its Conceptualization and Operationalization,” *Quality & Quantity* 52 (2018): 1893–1907, <https://doi.org/10.1007/s11135-017-0574-8> and Virginia Braun and Victoria Clarke, “One Size Fits All? What Counts as Quality Practice in (Reflexive) Thematic Analysis?” *Qualitative Research in Psychology* 18, no. 3 (2021): 328–52, <https://doi.org/10.1080/14780887.2020.1769238>.

[^11]: See Kirsti Malterud, Volkert Dirk Siersma, and Ann Dorrit Guassora, “Sample Size in Qualitative Interview Studies: Guided by Information Power,” *Qualitative Health Research* 26, no. 13 (2016): 1753–60, <https://doi.org/10.1177/1049732315617444>.

[^12]: Hannah Snyder, “Literature Review as a Research Methodology: An Overview and Guidelines,” *Journal of Business Research* 104 (2019): 333–39, <https://doi.org/10.1016/j.jbusres.2019.07.039>; Maria J. Grant and Andrew Booth, “A Typology of Reviews: An Analysis of 14 Review Types and Associated Methodologies,” *Health Information*\
    *& Libraries Journal* 26, no. 2 (2009): 91–108, <https://doi.org/10.1111/j.1471-1842.2009.00848.x>.

[^13]: Julia H. Littell, “Conceptual and Practical Classification of Research Reviews and Other Evidence Synthesis Products,” *Campbell Systematic Reviews* 14, no. 1 (2018): 1–21, <https://doi.org/10.4073/cmdp.2018.1>.

[^14]: Grant and Booth, “A Typology of Reviews”; Littell, “Conceptual and Practical Classification of Research Reviews and Other Evidence Synthesis Products.”

[^15]: John Gerring, *Social Science Methodology: A Unified Framework*, 2nd ed. (Cambridge: Cambridge University Press, 2012).

[^16]: Claes Wohlin, “Guidelines for Snowballing in Systematic Literature Studies and a Replication in Software Engineering,” in *Proceedings of the 18th International Conference on Evaluation and Assessment in Software Engineering* (Association for Computing Machinery, 2014), 1–10, <https://doi.org/10.1145/2601248.2601268>.

[^17]: Trisha Greenhalgh and Richard Peacock, “Effectiveness and Efficiency of Search Methods in Systematic Reviews of Complex Evidence: Audit of Primary Sources,” *BMJ* 331, no. 7524 (2005): 1064–65, <https://doi.org/10.1136/bmj.38636.593461.68>; Andrew Booth, Anthea Sutton, and Diana Papaioannou, *Systematic Approaches to a Successful Literature Review*, 2nd ed. (London: SAGE Publications, 2016).

[^18]: Page et al., “The PRISMA 2020 Statement”; Rethlefsen et al., “PRISMA-s.”

[^19]: Grant and Booth, “A Typology of Reviews”; Littell, “Conceptual and Practical Classification of Research Reviews and Other Evidence Synthesis Products”; Snyder, “Literature Review as a Research Methodology.”

[^20]: Terri D. Pigott and Joshua R. Polanin, “Methodological Guidance Paper: High-Quality Meta-Analysis in a Systematic Review,” *Review of Educational Research* 90, no. 1 (2020): 24–46, <https://doi.org/10.3102/0034654319877153>.

[^21]: Larry V. Hedges, Elizabeth Tipton, and Matthew C. Johnson, “Robust Variance Estimation in Meta-Regression with Dependent Effect Size Estimates,” *Research Synthesis Methods* 1, no. 1 (2010): 39–65, <https://doi.org/10.1002/jrsm.5>.

[^22]: Zuzana Irsova et al., “Meta-Analysis of Social Science Research: A Practitioner’s Guide,” *Journal of Economic Surveys* 38, no. 5 (2024): 1547–66, <https://doi.org/10.1111/joes.12595>.

[^23]: David Moreau and Beau Gamble, “Conducting a Meta-Analysis in the Age of Open Science: Tools, Tips, and Practical Recommendations,” *Psychological Methods* 27, no. 3 (2022): 426–32, <https://doi.org/10.1037/met0000351>.

[^24]: Joshua R. Polanin, Emily A. Hennessy, and Sho Tsuji, “Transparency and Reproducibility of Meta-Analyses in Psychology: A Meta-Review,” *Perspectives on Psychological Science* 15, no. 4 (2020): 1026–41, <https://doi.org/10.1177/1745691620906416>; Lesley Uttley, Yuliang Weng, and Louise Falzon, “What’s the Meta Now? More Updates on the Problems with Systematic Reviews,” *Journal of Clinical Epidemiology* 198 (2026): 112393, <https://doi.org/10.1016/j.jclinepi.2026.112393>.

[^25]: Julian H. Elliott et al., “Living Systematic Review: 1. Introduction, the Why, What, When, and How,” *Journal of Clinical Epidemiology* 91 (2017): 23–30, <https://doi.org/10.1016/j.jclinepi.2017.08.010>.

[^26]: Iain J. Marshall and Byron C. Wallace, “Toward Systematic Review Automation: A Practical Guide to Using Machine Learning Tools in Research Synthesis,” *Systematic Reviews* 8, no. 1 (2019): 163, <https://doi.org/10.1186/s13643-019-1074-9>.

[^27]: Aymeric Blaizot et al., “Using Artificial Intelligence Methods for Systematic Review in Health Sciences: A Systematic Review,” *Research Synthesis Methods* 13, no. 3 (2022): 353–62, <https://doi.org/10.1002/jrsm.1553>; M. Sharmila A. Sousa et al., “The Landscape of Artificial Intelligence Tools and Platforms for Evidence Synthesis: A Scoping Review,” *Systematic Reviews* 15, no. 1 (2026): 82, <https://doi.org/10.1186/s13643-025-02842-y>.

[^28]: Shunyu Yao et al., “ReAct: Synergizing Reasoning and Acting in Language Models,” in *The Eleventh International Conference on Learning Representations*, 2023, <https://openreview.net/forum?id=WE_vluYUL-X>.

[^29]: Joon Sung Park et al., “Generative Agents: Interactive Simulacra of Human Behavior,” in *Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology*, 2023, 1–22, <https://doi.org/10.1145/3586183.3606763>.

[^30]: Nelson F. Liu et al., “Lost in the Middle: How Language Models Use Long Contexts,” *Transactions of the Association for Computational Linguistics* 12 (2024): 157–73, <https://doi.org/10.1162/tacl_a_00638>.

[^31]: Fabrizio Gilardi, Meysam Alizadeh, and Maël Kubli, “ChatGPT Outperforms Crowd Workers for Text-Annotation Tasks,” *Proceedings of the National Academy of Sciences* 120, no. 30 (2023): e2305016120, <https://doi.org/10.1073/pnas.2305016120>; Nicholas Pangakis, Samuel Wolken, and Sergio Fasching, “Automated Annotation with Generative AI Requires Validation,” *arXiv*, 2023, <https://doi.org/10.48550/arXiv.2306.00176>; Caleb Ziems et al., “Can Large Language Models Transform Computational Social Science?” *Computational Linguistics* 50, no. 1 (2024): 237–91, <https://doi.org/10.1162/coli_a_00502>.

[^32]: Hal Roberts et al., “Media Cloud: Massive Open Source Collection of Global News on the Open Web,” *Proceedings of the International AAAI Conference on Web and Social Media* 15, no. 1 (2021): 1034–45, <https://doi.org/10.1609/icwsm.v15i1.18127>.

[^33]: Kaspar Beelen et al., “Bias and Representativeness in Digitized Newspaper Collections: Introducing the Environmental Scan,” *Digital Scholarship in the Humanities* 38, no. 1 (2023): 1–22, <https://doi.org/10.1093/llc/fqac037>.

[^34]: Erica Cai and Brendan O’Connor, “A Monte Carlo Language Model Pipeline for Zero-Shot Sociopolitical Event Extraction,” in *NeurIPS 2023 Workshop on Instruction Tuning and Instruction Following*, 2023, <https://doi.org/10.48550/arXiv.2305.15051>.

[^35]: Patrick T. Brandt and Marcus Sianan, “Measurement of Event Data from Text,” *Frontiers in Political Science* 6 (2025): 1453640, <https://doi.org/10.3389/fpos.2024.1453640>.

[^36]: Tasha Fairfield and Andrew E. Charman, “Explicit Bayesian Analysis for Process Tracing: Guidelines, Opportunities, and Caveats,” *Political Analysis* 25, no. 3 (2017): 363–80, <https://doi.org/10.1017/pan.2017.14>; Sherry Zaks, “Updating Bayesian(s): A Critical Evaluation of Bayesian Process Tracing,” *Political Analysis* 29, no. 1 (2021): 58–74, <https://doi.org/10.1017/pan.2020.10>.

[^37]: Miao Xiong et al., “Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs,” in *The Twelfth International Conference on Learning Representations*, 2024, <https://openreview.net/forum?id=gjeQKFxFpZ>.

[^38]: See Chloe Autio et al., “Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile” (National Institute of Standards and Technology, 2024), <https://doi.org/10.6028/NIST.AI.600-1>.

[^39]: Roam Research, “A Note-Taking Tool for Networked Thought,” accessed July 27, 2026, <https://roamresearch.com>; Tiago Forte, “How To Take Smart Notes: 10 Principles to Revolutionize Your Note-Taking and Writing,” February 4, 2020, <https://fortelabs.co/blog/how-to-take-smart-notes/>.

[^40]: Mem, “Introducing the World’s First Knowledge-Aware AI Assistant,” December 8, 2022, saved as a forwarded email in Readwise Reader; Ethan Mollick, “How to Use AI to Generate Ideas,” December 3, 2022, <https://oneusefulthing.substack.com/p/how-to-use-ai-to-generate-ideas>.

[^41]: Readwise Reader library audit conducted July 27, 2026. Reader reported 567 records tagged `📄Academic Article`, 499 tagged `🗃️PKM`, and 3,196 tagged `🤖AI`. Detailed metadata retrieval returned all 499 PKM records and connector-limited samples of 500 academic and 500 AI records. The audit treated tags as organizational labels rather than quality judgments, inspected sixteen representative full-text records, and made no changes to the library. See `editorial/readwise-pkm-ai-source-register.md`.

[^42]: Sébastien Dubois, “What Is Personal Knowledge Management (PKM)?,” December 16, 2022, <https://pkmjournal.com/why-is-personal-knowledge-management-pkm-useful-5f23405c2a2f>.

[^43]: Tiago Forte, “Great Use Case for ChatGPT Vision: Transcribing Handwritten Journal Entries,” December 11, 2023, <https://x.com/fortelabs/status/1734284384537333813>.

[^44]: Andy Stapleton, “Is This the End of Traditional Academic Papers? See What Every Researcher Needs to Know!,” video, December 6, 2023, <https://www.youtube.com/watch?v=kQp7EbxHcKA>.

[^45]: Noah Dasanaike, “What I’ve Learned From Digitizing 20 Million Historical Documents,” February 4, 2026, <https://noahdasanaike.github.io/posts/digitizing-census.html>.

[^46]: Len_dde, “My Academic Workflow with Obsidian and Zotero,” April 5, 2025, <https://medium.com/%40lennart.dde/my-academic-workflow-with-obsidian-and-zotero-53ac44ebdc28>.

[^47]: Andrew Altshuler, “The Argument Analyst Tana Template Is Out,” March 7, 2025, <https://x.com/1eo/status/1898034427579531367/>.

[^48]: CyrilXBT, “Most People Use Obsidian as a Note-Taking App,” May 5, 2026, <https://x.com/cyrilXBT/status/2051589237880009026/>. The library note marks this item as a redundant, shorter version of a longer guide; the chapter uses it only to document the persistent-context argument.

[^49]: CyrilXBT, “Obsidian Plus Vellum: A Second Brain That Never Stops,” May 27, 2026, <https://x.com/cyrilxbt/status/2059486502401569047/>.

[^50]: “Karpaty’s Second Brain,” shared Claude conversation saved July 18, 2026, <https://claude.ai/share/9263ec7c-827e-48da-8ddf-65375205f96b>. This is a derivative conversation about a video, not an independently verified account of the original presentation.

[^51]: Markus J. Buehler, “We’ve Made a Breakthrough in Self-Evolving AI Scientists,” June 5, 2026, <https://x.com/profbuehlermit/status/2062865983459475830/>. The saved item cites F. Y. Wang and M. J. Buehler, “Self-Revising Discovery Systems for Science: A Categorical Framework for Agentic Artificial Intelligence,” arXiv:2606.01444 (2026). The claim requires verification against the paper before scholarly citation.

[^52]: Eli Berman and Jacob N. Shapiro, “Big Data Seeks Context, for Long-Term Relationship: Reflections on the Empirical Studies of Conflict Project (ESOC),” August 17, 2023, <https://www.stimson.org/2023/reflections-on-the-empirical-studies-of-conflict-project-esoc/>. The byline and date were verified against the publisher page; the record has not yet been checked against Zotero.
