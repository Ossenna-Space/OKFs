# Source Management

## Architecture

Every catalog project stores committed source intent and resolved provenance separately from retrieved bytes:

```text
<project>/
└── okf/
    ├── catalog/
    ├── sources/
    │   ├── source.json
    │   ├── source.lock.json
    │   └── changes/
    └── raw/
        ├── cache/
        │   ├── objects/
        │   ├── outputs/
        │   └── documents/
        └── retained/
```

Each project owns one source collection, so its manifest and lock live directly in `okf/sources/` and its evidence lives directly in `okf/raw/`; neither path repeats the project name or source ID. `cache/` is reconstructable and excluded from Git. `retained/` contains vendored or manually archived evidence and is committed. Original and normalized storage policies are independent.

## Manifest

`source.json` defines one heterogeneous collection. Each item has a stable ID, a fetch adapter, and an ordered transformation pipeline.

```json
{
  "schema_version": 1,
  "id": "research-material",
  "storage": {
    "originals": "reference-only",
    "normalized": "reference-only"
  },
  "items": [
    {
      "id": "dictionary",
      "fetch": {
        "adapter": "github-tree",
        "repository": "mattpocock/dictionary-of-ai-coding",
        "ref": "main",
        "path": "dictionary",
        "include": ["**/*.md"]
      },
      "selection": {
        "strategy": "random",
        "count": 10,
        "seed": 20260810
      },
      "transform": [
        {"name": "markdown-copy", "version": 1}
      ]
    }
  ]
}
```

Supported adapters are `github-tree`, `https`, and `local-file`. Relative local paths resolve from the catalog project root. The initial deterministic transforms are `markdown-copy`, `text-to-markdown`, and `html-to-markdown`.

The manager uses only declared adapters. Acquired content is read as data and is never imported or executed. Authentication values do not belong in manifests; a future authenticated adapter must resolve a named `credential_ref` outside committed data.

## Lock and change identity

`source.lock.json` records each expanded document's adapter, source and logical paths, URLs, resolved revision, upstream object identity, input SHA-256, media type, transformation steps and fingerprint, output SHA-256, artifact paths, and lifecycle.

Normalized output hash and pipeline fingerprint determine whether a document is semantically changed. A byte-level input change that produces identical normalized Markdown does not enter the changed set.

Every successful refresh writes a change report under `changes/`. Lock replacement occurs only after all selected retrievals and transformations succeed.

## Operations

### OKF Manager in Codex

The [OKF Manager Codex Plugin](https://github.com/DrMarty/skills/tree/master/skills/okf-manager) is the primary interface for these operations. Open the repository as the Codex workspace, then invoke `$okf-project-manager` explicitly or ask Codex to use the OKF Manager.

The plugin reads the repository `AGENTS.md`, resolves projects and committed manifests, and delegates source operations to the deterministic helper. It must not reproduce refresh, hashing, transformation, retention, or lock-writing behavior conversationally.

| Codex request | Repository operation | State and network behavior |
| --- | --- | --- |
| “Show source status for `<project>`.” | `status` | Read-only and offline. |
| “Check upstream changes for `<project>` without applying them.” | `check` | Network may be used; cache, lock, and catalog remain unchanged. |
| “Hydrate `<project>` from its committed lock.” | `hydrate` | Network may be used; ignored cache is populated; upstream revisions do not advance. |
| “Refresh `<project>` and apply the source changes.” | `check`, followed by `refresh` | Reports the proposed change set before advancing the lock. |
| “Validate `<project>` for Git portability.” | `validate --mode portable` | Read-only; reference-only caches may be absent. |
| “Validate the hydrated evidence for `<project>`.” | `validate --mode hydrated` | Read-only; all locked artifacts must be present and hash-valid. |
| “Archive unavailable document `<document-id>` and retain its evidence.” | `mark-unavailable` | Explicit write; verifies and prepares tracked retained evidence. |
| “Manually retry archived document `<document-id>`.” | targeted `refresh --include-archived` | Explicit network/write workflow; reactivates only on complete success. |

Typical explicit skill prompts are:

```text
$okf-project-manager Hydrate <project-name> from its committed source lock. Do not refresh.

$okf-project-manager Check <project-name> upstream sources. Report added, changed, removed, and unchanged normalized documents without modifying anything.

$okf-project-manager Apply the reviewed <project-name> source refresh, update only affected concepts, append the catalog log, and run the full pipeline.
```

After a refresh changes normalized outputs, the plugin maps changed source documents to affected concepts, performs reviewed concept updates, appends the catalog log, and runs the OKF catalog pipeline. Source hydration alone does not rewrite concepts or generated catalog artifacts.

### Direct command-line interface

The plugin invokes these commands from the repository root. They are also available directly for automation and troubleshooting:

```powershell
python _tools/okf_source_manager.py status --project <project> --source <id>
python _tools/okf_source_manager.py check --project <project> --source <id>
python _tools/okf_source_manager.py refresh --project <project> --source <id>
python _tools/okf_source_manager.py hydrate --project <project> --source <id>
python _tools/okf_source_manager.py validate --project <project> --source <id> --mode portable
python _tools/okf_source_manager.py validate --project <project> --source <id> --mode hydrated
```

`check` performs current retrieval and transformation in memory but does not write artifacts or advance the lock. `refresh` resolves current moving references and writes a new lock. `hydrate` retrieves the exact locations and revisions in the existing lock, verifies input hashes, repeats transformations, and verifies output hashes.

Portable validation permits absent reference-only cache files. Hydrated validation requires all locked originals, normalized outputs, and materialized documents.

## Unavailable evidence

Retrieval failure never automatically declares permanent unavailability. After review, retain the last verified evidence explicitly:

```powershell
python _tools/okf_source_manager.py mark-unavailable `
  --project <project> `
  --source <id> `
  --document <document-id> `
  --reason "Upstream owner removed the document"
```

The operation verifies cached hashes, copies the original and normalized output into `retained/archive/`, writes archival provenance, and changes lifecycle to `archived-unavailable` with manual refresh policy. Automatic refresh preserves and skips archived documents.

To test recovery, explicitly target the archived document and allow archived retrieval:

```powershell
python _tools/okf_source_manager.py refresh `
  --project <project> `
  --source <id> `
  --document <document-id> `
  --include-archived
```

Successful targeted refresh returns the document to active lifecycle. Review its reported normalized-content change before re-indexing concepts.

## Reproducibility limits

A hash detects that a mutable URL changed but cannot recover bytes that no longer exist. Important volatile inputs should use vendored original storage or an immutable external artifact service. Nondeterministic transforms are intentionally unsupported; adding one requires retention rules that preserve its exact normalized output.
