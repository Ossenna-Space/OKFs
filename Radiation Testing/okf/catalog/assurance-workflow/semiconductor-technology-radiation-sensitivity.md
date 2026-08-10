---
type: Assurance Workflow
title: Semiconductor Technology Radiation Sensitivity
description: Device-technology guidance for assessing how CMOS, bipolar, BiCMOS, SOI,
  power, memory, and analog products respond differently to TID, SEE, DDD, and dose-rate
  effects.
tags:
- device-family
- technology
- cmos
- bipolar
- soi
- power
timestamp: '2026-08-09T05:55:24Z'
---
Radiation response is product- and process-specific; the TI handbook emphasizes that similar device types, process nodes, packages, or wafer flows can show materially different radiation performance. Use technology trends as screening heuristics, not as acceptance evidence.

# Technology sensitivity notes
- CMOS TID survivability often improves as gate oxides and feature sizes shrink, but isolation oxides such as LOCOS or STI can still drive leakage and functional failure.
- Bias during irradiation can change TID response; CMOS products often show worse TID degradation at higher operating voltage, while some bipolar products can be worse when unbiased.
- Linear bipolar and BiCMOS products require ELDRS attention because low dose-rate exposure can produce more degradation than high dose-rate testing predicts.
- Older CMOS, high-resistivity substrate, and deep sensitive-volume technologies can be more SEE-sensitive; SOI, thin active layers, and appropriate isolation can reduce charge collection but do not automatically guarantee SEL immunity.
- Power MOSFET/DMOS technologies require SEB and SEGR evaluation and voltage derating rather than relying only on generic logic SEE assumptions.

# Use in parts assurance
- Treat vendor radiation data as applicable only when the tested grade, die revision, wafer fab/process flow, package, bias, operating conditions, and failure criteria match the mission use case.
- Escalate to new test or supplier clarification when process transfer, die shrink, alternate assembly/test site, product grade substitution, or missing test conditions could change radiation response.

# Related concepts
- [Total Ionizing Dose](total-ionizing-dose.md)
- [Single Event Effects](single-event-effects.md)
- [Displacement Damage Dose](displacement-damage-dose.md)
- [Parts Selection Screening Qualification and Derating](parts-selection-screening-qualification-derating.md)
- [Published Radiation Test Data Applicability](published-radiation-test-data-applicability.md)

# Citations
- [TI Radiation Handbook for Electronics](../standards-guidelines/ti-radiation-handbook.md)
