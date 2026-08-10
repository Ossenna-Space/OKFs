# OKF Catalog Repository

This repository holds multiple independent Open Knowledge Format (OKF) catalog projects. Each project owns its catalog, source definitions, provenance locks, optional retained evidence, requirements, and documentation. Repository-management folders use an underscore prefix—such as `_Documentation`, `_Requirements`, and `_tools`—so catalog project folders remain visually distinct.

> Use with the [OKF Manager Codex Plugin](https://github.com/DrMarty/skills/tree/master/skills/okf-manager) to manage catalog evolution.

## Manage catalogs from Codex

Open this repository as the Codex workspace and ask the OKF Manager plugin to operate on a catalog. You can invoke its skill explicitly with `$okf-project-manager` or ask for the OKF Manager in natural language.

Examples:

```text
$okf-project-manager Show source status for every OKF project in this repository.

$okf-project-manager Hydrate <project-name> from its committed source lock. Do not refresh upstream revisions.

$okf-project-manager Check <project-name> upstream sources and report changes without modifying its lock or catalog.

$okf-project-manager Refresh <project-name>, update only concepts affected by normalized-document changes, and run the catalog validation pipeline.

$okf-project-manager Run portable source and catalog validation for every project in this repository.

$okf-project-manager Mark source document <document-id> unavailable, retain its last verified evidence for the next Git commit, and report every file prepared for check-in.

$okf-project-manager Manually retry archived source document <document-id>. Reactivate it only after retrieval, transformation, and hash validation succeed.
```

The repository's `AGENTS.md` directs the plugin to resolve committed source manifests and use the deterministic source helper. If a project or source is ambiguous, the plugin must ask which one to use.

Source definitions are committed while reference-only hydrated content is ignored. Hydration reconstructs the locked evidence; refresh deliberately advances an upstream revision.

## Direct command-line operation

The plugin runs the same repository-local helper shown below. These commands are useful for automation and troubleshooting, but the normal user interface is the OKF Manager within Codex.

A clone can reconstruct exact locked evidence with:

```powershell
python _tools/okf_source_manager.py hydrate --project <project-folder> --source <source-id>
```

Use `check` to compare current upstream content without changing local state and `refresh` to deliberately advance the committed lock:

```powershell
python _tools/okf_source_manager.py check --project <project-folder> --source <source-id>
python _tools/okf_source_manager.py refresh --project <project-folder> --source <source-id>
```

See [source-management documentation](_Documentation/source-management.md) and the [requirements index](_Requirements/Index.md).

## Verification

```powershell
python -m py_compile _tools/okf_source_manager.py
python -m unittest discover -s _tools/tests -v
```
