# Catalog Migration Requirements

## Portable knowledge outcomes

### R-RT-001: Preserve catalog knowledge

The project shall preserve the source catalog's concept documents, concept identifiers, relationships, and citations during migration.

### R-RT-002: Preserve evidence

The project shall retain every source evidence document used by the migrated catalog without modifying its content.

### R-RT-003: Record source provenance

The project shall define and lock the migrated evidence as a heterogeneous local-file source collection with per-document hashes.

### R-RT-004: Maintain derived artifacts

The project shall provide valid generated indexes, glossary content, an update log, and an interactive graph consistent with the migrated concepts.

### R-RT-005: Support deterministic validation

The project shall pass portable source validation and the OKF Manager catalog pipeline without unresolved link, frontmatter, index, glossary, or graph issues.

## Catalog navigation outcomes

### R-RT-006: Assurance and test lifecycle structure

The catalog shall organize its concepts around `Assurance Workflow`, `Standards & Guidelines`, `Test Operations`, and `Test Plans`. `Test Operations` shall contain `Testing Methods & Procedures` and `Testing Facilities`; `Testing Facilities` shall contain `Facility Capabilities` and `Facility Access`.

### R-RT-007: Hierarchy-derived concept types

Each concept's frontmatter `type` shall match its hierarchical schema path: `Assurance Workflow`, `Standards & Guidelines`, `Test Operations / Testing Methods & Procedures`, `Test Operations / Testing Facilities`, `Test Operations / Testing Facilities / Facility Capabilities`, `Test Operations / Testing Facilities / Facility Access`, or `Test Plans`.
