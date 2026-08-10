# Dictionary of AI Coding Catalog Requirements

## Source outcomes

### R-DOAC-001: Authoritative source

The project shall track Markdown documents beneath `dictionary/` in `mattpocock/dictionary-of-ai-coding` on the `main` ref.

### R-DOAC-002: Reference-only evidence

The initial project shall commit its source manifest, resolved lock, hashes, URLs, and change reports while excluding hydrated original and normalized bytes from Git.

### R-DOAC-003: Repeatable trial sample

The initial catalog shall use a deterministic pseudo-random sample of 10 eligible Markdown documents selected with seed `20260810`.

## Catalog outcomes

### R-DOAC-004: One source concept per sampled document

The initial catalog shall contain one concept derived from each selected source document.

### R-DOAC-005: Source provenance

Every derived concept shall identify its source collection, source document ID, upstream revision, input and normalized-output SHA-256 values, and immutable GitHub URL.

### R-DOAC-006: Valid portable bundle

The resulting source state shall pass portable and hydrated validation, and the OKF catalog shall pass lint, glossary, index, visualization, and graph verification with at least 10 concepts.

### R-DOAC-007: Flat project source paths

The source manifest, lock, change reports, and plans shall live directly beneath `okf/sources/`, while cache and retained evidence shall live directly beneath `okf/raw/`, without a repeated `dictionary-of-ai-coding` directory.
