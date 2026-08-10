# Radiation Testing Catalog

## Structure

The project is a self-contained OKF bundle under `okf/`. Concept documents live in `okf/catalog/`, migrated evidence lives in `okf/raw/`, and deterministic source metadata lives in `okf/sources/`.

The catalog uses an assurance and test lifecycle structure:

```text
Assurance Workflow/
Standards & Guidelines/
Test Operations/
├── Testing Methods & Procedures/
└── Testing Facilities/
    ├── Facility Capabilities/
    └── Facility Access/
Test Plans/
```

Assurance concepts include radiation-effect, device-sensitivity, evidence, and workflow knowledge. Standards and their retained source-document concepts are grouped together. Test methods, facilities, capabilities, and access information follow the operational hierarchy. Integrated test-program concepts are indexed as test plans. Generated `index.md` files provide progressive disclosure, `glossary.md` provides shared terminology, `log.md` records catalog evolution, and `viz.html` contains the interactive relationship graph.

Concept frontmatter types use canonical hierarchical paths: `Assurance Workflow`, `Standards & Guidelines`, `Test Operations / Testing Methods & Procedures`, `Test Operations / Testing Facilities`, `Test Operations / Testing Facilities / Facility Capabilities`, `Test Operations / Testing Facilities / Facility Access`, and `Test Plans`. The graph uses these values for node coloring and filtering, so shared prefixes expose parent-child relationships.

## Migration provenance

The initial catalog and evidence were migrated without content changes from `C:\Users\marty\Code\RadiationTesting\okf`. The source catalog contained 52 concepts and 16 Markdown evidence documents. Existing concept IDs and relative citations were preserved.

`okf/sources/source.json` identifies each migrated evidence document as an independently retrievable local file. `source.lock.json` records hashes and transformation fingerprints produced by `_tools/okf_source_manager.py`. The readable migrated evidence remains versioned directly under `okf/raw/`; reconstructed materializations under `okf/raw/cache/` are ignored.

## Validation

From the repository root, validate source provenance with:

```powershell
python _tools/okf_source_manager.py validate --project "Radiation Testing" --source radiation-testing-evidence --mode portable
```

Use the OKF Manager catalog pipeline for concept, link, glossary, index, and graph validation.
