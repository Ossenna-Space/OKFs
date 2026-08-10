# Radiation Testing OKF project

## Purpose

- Maintain the portable Radiation Testing knowledge catalog and its source provenance.
- Cover radiation effects, test methods, assurance workflows, standards, facilities, and evidence applicable to electronic systems.

## Ownership

- `okf/catalog/` contains OKF concept documents and generated discovery artifacts.
- `okf/sources/` contains the project source manifest, lock, and change reports.
- `okf/raw/` contains migrated source evidence and optional ignored hydration cache.
- `_Requirements/` defines project outcomes.
- `_Documentation/` describes the catalog structure and migration provenance.

## Local Contracts

- Organize catalog concept IDs around `assurance-workflow/`, `standards-guidelines/`, `test-operations/`, and `test-plans/`.
- Under `test-operations/`, keep method concepts in `testing-methods-procedures/` and facility concepts in `testing-facilities/`, including its `facility-capabilities/` and `facility-access/` branches.
- Set each concept's frontmatter `type` to the canonical hierarchical schema path, using ` / ` between parent and child branches.
- Preserve citations and update every relative link when an explicit reindex changes concept IDs.
- Treat files in `okf/raw/` as immutable evidence.
- Use the OKF Manager deterministic pipeline after graph-visible concept changes.
- Use `_tools/okf_source_manager.py` from the repository root for source status, refresh, hydration, and validation.

## Work Guidance

- Keep source manifest and lock directly under `okf/sources/`.
- Keep project evidence directly under `okf/raw/` without repeating the project name.
- Record durable catalog changes in `okf/catalog/log.md`.

## Verification

- Run portable source validation for source ID `radiation-testing-evidence`.
- Run the OKF Manager catalog pipeline and graph verification.

## Child DOX Index

- `_Requirements/AGENTS.md` governs project requirements; `_Requirements/Index.md` indexes them.
- `_Documentation/AGENTS.md` governs project documentation; `_Documentation/Index.md` indexes it.
