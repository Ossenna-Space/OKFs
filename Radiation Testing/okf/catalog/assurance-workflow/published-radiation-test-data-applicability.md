---
type: Assurance Workflow
title: Published Radiation Test Data Applicability
description: Review workflow for deciding whether published radiation reports and
  vendor data can support a mission-specific part-use decision.
tags:
- workflow
- evidence
- test-data
- parts-selection
timestamp: '2026-08-09T05:55:24Z'
---
Published radiation data can reduce test burden, but the TI handbook cautions that reports are only usable when the tested device, process, operating conditions, and failure criteria match the intended application closely enough for the risk decision.

# Procedure
1. Confirm exact product identity: manufacturer, part number, grade, die revision, package, lot/date code meaning, wafer fab/process flow, and any post-transfer or die-shrink history.
2. Confirm radiation test conditions: radiation source or particle, dose or fluence, dose rate, LET/proton energy, bias state, supply voltage, load, clock/frequency, temperature, shielding, sample size, and electrical test windows.
3. Confirm failure criteria: monitored parameters, data-sheet limits, transient thresholds, destructive-current thresholds, functional-reset criteria, and whether all mission-critical parameters were tested.
4. Check for known ambiguity or misdiagnosis, especially between SET, SEU, SEFI, SEL, SEB, SEGR, and prompt-dose effects.
5. Decide whether existing evidence is directly applicable, applicable with margin/mitigation, usable only as screening evidence, or insufficient and requiring new test.

# Related concepts
- [Parts Selection Screening Qualification and Derating](parts-selection-screening-qualification-derating.md)
- [Evidence and Provenance Model](evidence-and-provenance.md)
- [Radiation Effects Test Program](../test-plans/radiation-effects-test-program.md)
- [TI Radiation Handbook for Electronics Guidance](../standards-guidelines/ti-radiation-handbook-guidance.md)

# Citations
- [TI Radiation Handbook for Electronics](../standards-guidelines/ti-radiation-handbook.md)
