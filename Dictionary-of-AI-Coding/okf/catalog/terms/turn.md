---
type: AI Coding Term
resource: https://github.com/mattpocock/dictionary-of-ai-coding/blob/251fec7ec3b08059e4203863024e6123090a54e3/dictionary/Turn.md
title: Turn
description: One user message and all agent activity that follows before control returns
  to the user.
tags:
- ai-coding
- session
- interaction
timestamp: '2026-08-10T02:00:42+00:00'
sources:
- source_id: dictionary-of-ai-coding
  document_id: dictionary:Turn.md
  revision: 251fec7ec3b08059e4203863024e6123090a54e3
  input_sha256: 4a49db30413ed104232ccd5d342289f13439f330b6df8c8ec5d0c72affe913d7
  normalized_sha256: 4a49db30413ed104232ccd5d342289f13439f330b6df8c8ec5d0c72affe913d7
---
# Overview

A turn begins with one user message and includes everything the agent does before returning control. It may contain one or many [model provider requests](./model-provider-request.md), particularly when the agent chains [tool calls](./tool-call.md).

# Operational implication

Turn length determines how much autonomous work happens between opportunities for user steering. Longer turns support unattended progress but allow more drift before feedback; shorter turns create more frequent review points.

# Citations

- [Dictionary source at locked commit](https://github.com/mattpocock/dictionary-of-ai-coding/blob/251fec7ec3b08059e4203863024e6123090a54e3/dictionary/Turn.md)
