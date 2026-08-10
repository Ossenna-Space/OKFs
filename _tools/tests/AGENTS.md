# Source Manager Tests

## Purpose

- Exercise source-manager behavior without external services.

## Ownership

- Test modules create isolated temporary OKF projects and local evidence.

## Local Contracts

- Do not require internet access or credentials.
- Verify hashes, lifecycle transitions, storage paths, and validation results.

## Work Guidance

- Use fixed content and seeds.

## Verification

- Run `python -m unittest discover -s _tools/tests -v`.

## Child DOX Index

- No child `AGENTS.md` files are required.
