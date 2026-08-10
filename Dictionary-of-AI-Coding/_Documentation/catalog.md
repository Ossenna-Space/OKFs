# Dictionary of AI Coding Catalog

This project derives an OKF catalog from a deterministic random sample of ten Markdown documents in Matt Pocock's [Dictionary of AI Coding](https://github.com/mattpocock/dictionary-of-ai-coding/tree/main/dictionary).

The committed `okf/sources/source.json` manifest follows `main`, restricts acquisition to `dictionary/**/*.md`, and uses random seed `20260810`. Its reference-only storage policy keeps the Git repository compact by hydrating into `okf/raw/cache/`, while `okf/sources/source.lock.json` preserves the exact commit, file hashes, transformation fingerprint, and immutable upstream links needed for hydration.

Use the OKF Manager Codex Plugin from the repository root:

```text
$okf-project-manager Hydrate the Dictionary of AI Coding sources from the committed lock. Do not refresh.

$okf-project-manager Check the Dictionary of AI Coding source for upstream changes without modifying the lock.

$okf-project-manager Apply the reviewed source refresh, update affected concepts, and run the full catalog pipeline.
```

## Initial catalog state

The source lock resolves the upstream `main` ref to commit `251fec7ec3b08059e4203863024e6123090a54e3`. Seed `20260810` selected:

- `AFK.md`
- `Attention budget.md`
- `Handoff artifact.md`
- `Model provider request.md`
- `Model.md`
- `Output tokens.md`
- `Permission request.md`
- `System prompt.md`
- `Tool call.md`
- `Turn.md`

Each document is normalized with `markdown-copy` version 1 and indexed as one `AI Coding Term` concept. Every concept records the source document ID, locked revision, input SHA-256, normalized SHA-256, and immutable upstream URL.

The completed OKF pipeline verifies 10 concepts, 23 directed concept edges, and one concept type. Portable and hydrated source validation both pass with no issues. The generated root index, terms index, glossary, catalog log, and `viz.html` are committed catalog artifacts.
