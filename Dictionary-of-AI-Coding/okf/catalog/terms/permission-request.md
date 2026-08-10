---
type: AI Coding Term
resource: https://github.com/mattpocock/dictionary-of-ai-coding/blob/251fec7ec3b08059e4203863024e6123090a54e3/dictionary/Permission%20request.md
title: Permission request
description: A harness checkpoint that asks a user to approve a tool call that is
  not already authorized.
tags:
- ai-coding
- permissions
- human-in-the-loop
timestamp: '2026-08-10T02:00:42+00:00'
sources:
- source_id: dictionary-of-ai-coding
  document_id: dictionary:Permission request.md
  revision: 251fec7ec3b08059e4203863024e6123090a54e3
  input_sha256: 9bc1edfbcc96392a4d223c13d14be6f79d196695829977b8db7ad4034d79a969
  normalized_sha256: 9bc1edfbcc96392a4d223c13d14be6f79d196695829977b8db7ad4034d79a969
---
# Overview

A permission request is the harness mechanism that pauses an unapproved [tool call](./tool-call.md) for human authorization. Approval allows execution; denial is returned to the [model](./model.md) as feedback that can steer a different approach.

# Operational implication

Permission requests keep people in the loop for risky actions, but each request introduces a synchronous wait. Permission policy should pre-authorize genuinely safe actions while retaining review for meaningful risk.

# Citations

- [Dictionary source at locked commit](https://github.com/mattpocock/dictionary-of-ai-coding/blob/251fec7ec3b08059e4203863024e6123090a54e3/dictionary/Permission%20request.md)
