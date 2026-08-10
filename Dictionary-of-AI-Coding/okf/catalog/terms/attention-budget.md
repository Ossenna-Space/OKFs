---
type: AI Coding Term
resource: https://github.com/mattpocock/dictionary-of-ai-coding/blob/251fec7ec3b08059e4203863024e6123090a54e3/dictionary/Attention%20budget.md
title: Attention budget
description: The finite influence each token can distribute across the rest of a model's
  context.
tags:
- ai-coding
- attention
- context
timestamp: '2026-08-10T02:00:42+00:00'
sources:
- source_id: dictionary-of-ai-coding
  document_id: dictionary:Attention budget.md
  revision: 251fec7ec3b08059e4203863024e6123090a54e3
  input_sha256: a25faffd26d815132f844d66ad2fe26ba7435026097fff52747afa2aad6c9c6b
  normalized_sha256: a25faffd26d815132f844d66ad2fe26ba7435026097fff52747afa2aad6c9c6b
---
# Overview

An attention budget describes the limited influence available to each token across a context. As context grows, important instructions compete with more surrounding material even though their text has not changed. This declining signal-to-noise ratio can look like forgetting or disobedience.

# Operational implication

Keep task context focused, remove material that no longer contributes, and restate critical constraints when a long session makes them less prominent.

# Citations

- [Dictionary source at locked commit](https://github.com/mattpocock/dictionary-of-ai-coding/blob/251fec7ec3b08059e4203863024e6123090a54e3/dictionary/Attention%20budget.md)
