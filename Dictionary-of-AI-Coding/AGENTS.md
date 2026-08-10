# Dictionary of AI Coding Catalog

## Purpose

- Maintain a provenance-aware OKF catalog derived from Matt Pocock's Dictionary of AI Coding.

## Ownership

- `okf/catalog/` owns generated and curated OKF concepts.
- `okf/sources/` owns committed source intent, locks, and change reports.
- `okf/raw/` owns ignored hydrated caches and any tracked retained evidence.
- `Requirements/` owns project intent.
- `Documentation/` describes the project source and catalog workflow.

## Local Contracts

- Track `mattpocock/dictionary-of-ai-coding` at the `main` ref and restrict acquisition to `dictionary/**/*.md`.
- Use source ID `dictionary-of-ai-coding` and a committed deterministic random selection of 10 documents with seed `20260810` for the initial trial.
- Keep originals and normalized Markdown reference-only unless a later reviewed decision changes their storage policy.
- Cite immutable commit-pinned GitHub URLs and preserve source document IDs, revisions, and hashes in concept frontmatter.
- Do not manually modify hydrated evidence under `okf/raw/dictionary-of-ai-coding/cache/`.

## Work Guidance

- Use the root OKF Manager Codex workflow for status, check, hydrate, refresh, validation, archival, and recovery.
- Update only concepts whose normalized source output changes.

## Verification

- Run portable and hydrated source validation with `tools/okf_source_manager.py` from the repository root.
- Run the OKF Manager `pipeline` command after concept changes.
- Require at least 10 concepts in graph verification for the initial catalog.

## Child DOX Index

- `Requirements/AGENTS.md` governs project requirements.
- `Documentation/AGENTS.md` governs project documentation.
