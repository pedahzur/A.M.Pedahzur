---
title: "Historical Evidence Chain Register"
version: "1.0"
date: "2026-08-03"
license: "CC BY 4.0"
---

# Historical Evidence Chain Register

Use one stable identifier per record. Preserve prior versions and add a supersession link when a correction changes a consequential field.

## 1. Source Witness

| Field | Entry |
|---|---|
| Source witness ID | |
| Holding institution or repository | |
| Collection and catalogue locator | |
| Stable URL or local authorized locator | |
| Image, page, folio, track, or segment | |
| Creator and intended audience | |
| Date as written | |
| Document type and boundary basis | |
| Rights and access status | |
| Selection rationale | |
| Known gaps or source-quality limits | |

## 2. Transcription Version

| Field | Entry |
|---|---|
| Transcription ID and version | |
| Source witness ID | |
| Convention used | |
| Transcriber or model run | |
| Date and time | |
| Uncertain or illegible regions | |
| Review status and reviewer | |
| Supersedes | |

## 3. Passage and Source-Bound Observation

| Observation ID | Passage locator | Exact source form | Observation | Epistemic status | Certainty | Uncertainty reason |
|---|---|---|---|---|---|---|
| | | | | source-stated / normalized / inferred | | |

For every normalized value, record the rule or authority. For every inference, record the source-stated basis and rationale.

## 4. Claim in Source

| Claim ID | Immutable proposition | Claimant or attribution | Passage ID | Polarity and modality | Validation status |
|---|---|---|---|---|---|
| | | | | | supported / partially supported / unsupported / contradicted / not assessable |

## 5. Historical Claim and Dependencies

| Historical Claim ID | Immutable proposition | Supporting claim or observation IDs | Inferential step | Contrary evidence IDs | Status |
|---|---|---|---|---|---|
| | | | | | |

## 6. Audit Decision

| Field | Entry |
|---|---|
| Audit ID | |
| Claim ID and version | |
| Passages and dependencies checked | |
| Decision | supported / partially supported / unsupported / contradicted / not assessable |
| Explanation | |
| Smallest supported revision | |
| Certainty and uncertainty reason | |
| Needs adjudication | |
| Auditor and date | |

## 7. Adjudication and Change History

| New record ID | Prior record ID | Disagreement type | Decision | Rationale | Adjudicator | Date |
|---|---|---|---|---|---|---|
| | | transcription / normalization / identity / inference / provenance / procedure | | | | |

## Completion Check

Confirm that every consequential observation reaches an exact passage, every passage reaches a fixed transcription and source witness, every normalization preserves the source form, every inference states its basis, and every Historical Claim can be audited through declared dependencies.
