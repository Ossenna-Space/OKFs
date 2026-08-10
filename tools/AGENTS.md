# Source Management Tools

## Purpose

- Provide deterministic, local-first source acquisition, transformation, provenance, hydration, refresh, retention, and validation.

## Ownership

- `okf_source_manager.py` owns the command-line implementation.
- `tests/` owns deterministic workflow coverage.

## Local Contracts

- Use the Python standard library only.
- Never execute or import acquired evidence.
- Write JSON deterministically and replace committed state atomically.
- Keep network adapters explicit and source-scoped.
- Keep secrets outside manifests, locks, output, and logs.

## Work Guidance

- Prefer content hashes and stable document IDs over timestamps for change identity.
- Keep fetch adapters and transform implementations narrow and independently testable.

## Verification

- Run `python -m unittest discover -s tools/tests -v` from the repository root.
- Run `python -m py_compile tools/okf_source_manager.py`.

## Child DOX Index

- `tests/AGENTS.md` governs source-manager tests.
