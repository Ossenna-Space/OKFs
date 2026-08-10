---
type: AI Coding Term
resource: https://github.com/mattpocock/dictionary-of-ai-coding/blob/251fec7ec3b08059e4203863024e6123090a54e3/dictionary/Tool%20call.md
title: Tool call
description: Structured model output that names a tool and arguments for the harness
  to validate and execute.
tags:
- ai-coding
- tools
- harness
timestamp: '2026-08-10T02:00:42+00:00'
sources:
- source_id: dictionary-of-ai-coding
  document_id: dictionary:Tool call.md
  revision: 251fec7ec3b08059e4203863024e6123090a54e3
  input_sha256: f1a1a3c6bf962ae44295888dd92fd3dd18abf82ac384ced245324c47d7f252cf
  normalized_sha256: f1a1a3c6bf962ae44295888dd92fd3dd18abf82ac384ced245324c47d7f252cf
---
# Overview

A tool call is structured text produced by a [model](./model.md) during a [model provider request](./model-provider-request.md). It names a tool and arguments, but the surrounding harness must parse, authorize, and execute it before any external action occurs.

# Operational implication

A plausible tool call can still contain incorrect paths or arguments. The harness executes the structure that was emitted, so clear tool descriptions, permission checks, and result feedback are important. Multiple tool calls commonly occur inside one [turn](./turn.md), guided by the [system prompt](./system-prompt.md).

# Citations

- [Dictionary source at locked commit](https://github.com/mattpocock/dictionary-of-ai-coding/blob/251fec7ec3b08059e4203863024e6123090a54e3/dictionary/Tool%20call.md)
