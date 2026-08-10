---
type: AI Coding Term
resource: https://github.com/mattpocock/dictionary-of-ai-coding/blob/251fec7ec3b08059e4203863024e6123090a54e3/dictionary/System%20prompt.md
title: System prompt
description: The standing instructions a harness places before user context in each
  model provider request.
tags:
- ai-coding
- prompting
- harness
timestamp: '2026-08-10T02:00:42+00:00'
sources:
- source_id: dictionary-of-ai-coding
  document_id: dictionary:System prompt.md
  revision: 251fec7ec3b08059e4203863024e6123090a54e3
  input_sha256: aca2bebd8be3afb8bef83f56217f8f1406cfe6b837e65f34cebb56ef924fbb39
  normalized_sha256: aca2bebd8be3afb8bef83f56217f8f1406cfe6b837e65f34cebb56ef924fbb39
---
# Overview

A system prompt is the harness-provided standing brief included in every [model provider request](./model-provider-request.md). It describes behavior, tools, conventions, and constraints that shape how the [model](./model.md) responds and emits [tool calls](./tool-call.md).

# Operational implication

Because it remains stable across a session, the system prompt commonly forms the beginning of a reusable request prefix. Its higher instruction priority can explain persistent differences between harnesses or conflicts with instructions given later in a [turn](./turn.md).

# Citations

- [Dictionary source at locked commit](https://github.com/mattpocock/dictionary-of-ai-coding/blob/251fec7ec3b08059e4203863024e6123090a54e3/dictionary/System%20prompt.md)
