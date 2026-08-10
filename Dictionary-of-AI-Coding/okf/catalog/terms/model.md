---
type: AI Coding Term
resource: https://github.com/mattpocock/dictionary-of-ai-coding/blob/251fec7ec3b08059e4203863024e6123090a54e3/dictionary/Model.md
title: Model
description: A stateless parameterized system that predicts output tokens from input
  tokens.
tags:
- ai-coding
- model
- inference
timestamp: '2026-08-10T02:00:42+00:00'
sources:
- source_id: dictionary-of-ai-coding
  document_id: dictionary:Model.md
  revision: 251fec7ec3b08059e4203863024e6123090a54e3
  input_sha256: c3ceb17b0b3c36120385189e4196e5d481cc82660f4e1b4c0bceecc5e420b1a5
  normalized_sha256: c3ceb17b0b3c36120385189e4196e5d481cc82660f4e1b4c0bceecc5e420b1a5
---
# Overview

A model is the stateless parameter set that performs next-token prediction. It receives tokens and returns tokens during a [model provider request](./model-provider-request.md); capabilities such as reading files, running commands, and iterating arise from the surrounding harness rather than from the model alone.

# Operational implication

Model tier affects capability, latency, and cost, but diagnosis should also consider the context, tools, and harness that shape the model's work.

# Citations

- [Dictionary source at locked commit](https://github.com/mattpocock/dictionary-of-ai-coding/blob/251fec7ec3b08059e4203863024e6123090a54e3/dictionary/Model.md)
