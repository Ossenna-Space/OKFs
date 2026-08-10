# Source Management Requirements

## Repository and catalog outcomes

### R-SRC-001: Multi-catalog repository

The repository shall contain independent OKF projects as direct child folders. Each project shall own its catalog, raw evidence, source definitions, requirements, and documentation.

### R-SRC-002: Git-portable catalogs

Catalog concepts, source manifests, resolved source locks, provenance, requirements, and documentation shall be suitable for Git version control. Hydrated caches may be excluded from Git without invalidating portable catalog metadata.

## Source definition outcomes

### R-SRC-003: Heterogeneous collections

A named source collection shall support multiple independently identified documents acquired from disparate adapters. The initial implementation shall support GitHub repository trees, HTTPS documents, and local files.

### R-SRC-004: Declarative transformations

Each source item shall declare an ordered transformation pipeline. The initial implementation shall provide deterministic Markdown copy, plain-text-to-Markdown, and HTML-to-Markdown transformations and shall reject unknown transformations explicitly.

### R-SRC-005: Complete provenance

For every materialized document, the lock shall retain its source-item identity, logical source path, requested and resolved locations, resolved revision when available, media type, byte size, input SHA-256, transformation definition and fingerprint, output SHA-256, logical output path, and lifecycle state.

### R-SRC-006: Credential separation

Source definitions may name credential references but shall not store credential values in committed manifests, locks, logs, or raw evidence.

## Hydration and refresh outcomes

### R-SRC-007: Locked hydration

Hydration shall reconstruct the committed lock state without advancing moving upstream references. It shall verify retrieved input and transformed output hashes and fail rather than accept mismatched content.

### R-SRC-008: Explicit refresh

Refresh shall resolve current upstream state, retrieve and transform changed documents, preserve immutable provenance, and advance the lock only after successful processing. Archived-unavailable documents shall be skipped by automatic refresh.

### R-SRC-009: Incremental change identity

Refresh shall report added, changed, unchanged, and removed logical documents. Semantic re-indexing eligibility shall be based on normalized-output hashes, including transformation fingerprint changes.

### R-SRC-010: Deterministic selection

Collections may select a deterministic pseudo-random sample from an ordered candidate set using a committed count and seed.

## Storage and unavailability outcomes

### R-SRC-011: Independent storage policies

Original and normalized evidence shall each support `reference-only` or `vendored` storage. Reference-only artifacts shall occupy an ignored cache; vendored artifacts shall occupy a tracked retained-evidence area.

### R-SRC-012: Explicit unavailable transition

A failed availability check shall not permanently change lifecycle state. Only an explicit user operation may mark a document `archived-unavailable`.

### R-SRC-013: Last-known evidence retention

Before marking a document unavailable, the manager shall verify the last cached or retained original and normalized hashes, copy them into tracked retained evidence, write archival provenance, and fail if exact evidence is unavailable.

### R-SRC-014: Manual recovery

Archived-unavailable documents shall require an explicit recovery workflow before returning to active automatic refresh.

## Safety and validation outcomes

### R-SRC-015: Immutable and non-executable evidence

Retrieved evidence shall be treated as immutable data and shall never be imported or executed by the manager.

### R-SRC-016: Portable validation

Portable validation shall verify manifests, locks, provenance, lifecycle state, and any retained evidence without requiring reference-only cache content.

### R-SRC-017: Hydrated validation

Hydrated validation shall additionally require and hash-check every locked original, normalized output, and materialized document.

### R-SRC-018: Atomic state updates

Lock and lifecycle changes shall use atomic file replacement after all corresponding artifacts have been verified.

## Codex plugin workflow outcomes

### R-SRC-019: OKF Manager operation

Repository instructions shall make the OKF Manager Codex Plugin the primary user interface for catalog evolution. They shall provide natural-language and explicit skill-invocation examples for source status, check, hydrate, refresh, validation, unavailable-source archival, manual recovery, concept re-indexing, and catalog pipeline validation.

### R-SRC-020: Deterministic plugin delegation

When operating in this repository, the OKF Manager workflow shall delegate source state changes to `_tools/okf_source_manager.py`, resolve projects and source IDs from committed manifests, distinguish read-only checks from writes, and report the helper's deterministic results instead of recreating its behavior conversationally.

## Repository layout outcomes

### R-SRC-021: Distinguished management folders

Repository and catalog-project folders that contain management requirements, documentation, or tools shall use an underscore prefix, including `_Requirements`, `_Documentation`, and `_tools`, so they are visually distinct from OKF catalog project folders.

### R-SRC-022: Flat project source layout

Each catalog project shall store its single source-collection manifest and lock directly under `okf/sources/`, and its cache and retained evidence directly under `okf/raw/`. The project name or source ID shall not be repeated as an intermediate directory beneath those paths.
