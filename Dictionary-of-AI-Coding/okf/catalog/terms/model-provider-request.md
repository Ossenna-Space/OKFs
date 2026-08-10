---
type: AI Coding Term
resource: https://github.com/mattpocock/dictionary-of-ai-coding/blob/251fec7ec3b08059e4203863024e6123090a54e3/dictionary/Model%20provider%20request.md
title: Model provider request
description: One round trip in which a harness sends context to a model provider and
  receives a response.
tags:
- ai-coding
- model-provider
- request
timestamp: '2026-08-10T02:00:42+00:00'
sources:
- source_id: dictionary-of-ai-coding
  document_id: dictionary:Model provider request.md
  revision: 251fec7ec3b08059e4203863024e6123090a54e3
  input_sha256: 97f1169b6a7adcb2b33fe58d9a79caa89c1cab4d8696383bcb3d87002b296a63
  normalized_sha256: 97f1169b6a7adcb2b33fe58d9a79caa89c1cab4d8696383bcb3d87002b296a63
---
# Overview

A model provider request is a single round trip between a harness and a [model](./model.md). The harness sends the current context and receives either a [tool call](./tool-call.md) or a final response. Tool results can cause several requests inside one [turn](./turn.md).

# Cost and context

Each request can resend the accumulated context, including the [system prompt](./system-prompt.md), while billing counts input and [output tokens](./output-tokens.md) at the request level. Request count and context size therefore both affect cost.

# Citations

- [Dictionary source at locked commit](https://github.com/mattpocock/dictionary-of-ai-coding/blob/251fec7ec3b08059e4203863024e6123090a54e3/dictionary/Model%20provider%20request.md)
