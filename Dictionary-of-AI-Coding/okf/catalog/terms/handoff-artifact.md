---
type: AI Coding Term
resource: https://github.com/mattpocock/dictionary-of-ai-coding/blob/251fec7ec3b08059e4203863024e6123090a54e3/dictionary/Handoff%20artifact.md
title: Handoff artifact
description: A durable document written by one session to carry relevant state into
  another session.
tags:
- ai-coding
- handoff
- documentation
timestamp: '2026-08-10T02:00:42+00:00'
sources:
- source_id: dictionary-of-ai-coding
  document_id: dictionary:Handoff artifact.md
  revision: 251fec7ec3b08059e4203863024e6123090a54e3
  input_sha256: 22927bc869e426dd4f345f1bb99e6b282790dc671d817f40d7bbd15ad7f7278a
  normalized_sha256: 22927bc869e426dd4f345f1bb99e6b282790dc671d817f40d7bbd15ad7f7278a
---
# Overview

A handoff artifact moves decisions, constraints, progress, and remaining work from one session into a durable environment that another session can read. It compensates for the fact that a [model](./model.md) does not retain session state by itself.

# Operational implication

A useful artifact assumes a fresh reader with no prior context, gives concrete paths and decisions, and distinguishes its secondary account from primary evidence such as code and tests.

# Citations

- [Dictionary source at locked commit](https://github.com/mattpocock/dictionary-of-ai-coding/blob/251fec7ec3b08059e4203863024e6123090a54e3/dictionary/Handoff%20artifact.md)
