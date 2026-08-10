---
type: Standards & Guidelines
resource: sgzy002a - TI Radiation Handbook for Electronics.pdf.md
title: TI Radiation Handbook for Electronics Guidance
description: Vendor-authored technical guidance on radiation environments, effects,
  mitigation, test approaches, and interpretation of radiation data for electronics.
tags:
- guideline
- handbook
- radiation-effects
- ti
timestamp: '2026-08-09T05:55:24Z'
---
Texas Instruments' handbook is not a NASA standard, but it is useful supporting guidance for interpreting radiation effects in electronic components and for planning qualification evidence. It explains how environment, device properties, process technology, bias, shielding, and test conditions influence observed radiation response.

# Assurance role
- Complements normative NASA, ECSS, and MIL references by explaining physical mechanisms behind [Total Ionizing Dose](../assurance-workflow/total-ionizing-dose.md), [Single Event Effects](../assurance-workflow/single-event-effects.md), [Displacement Damage Dose](../assurance-workflow/displacement-damage-dose.md), and [space radiation environment](../assurance-workflow/space-radiation-environment.md).
- Supports [Radiation Effects Test Program](../test-plans/radiation-effects-test-program.md) planning by summarizing TID, SEE, DDD, dose-rate, and terrestrial neutron/alpha test considerations.
- Supports [Parts Selection Screening Qualification and Derating](../assurance-workflow/parts-selection-screening-qualification-derating.md) by warning that process flow, lot variation, grade, product version, operating conditions, and failure criteria affect whether published radiation data applies to a selected part.

# Key guidance captured
- Mission exposure depends on orbit, duration, shielding, solar activity, and radiation-belt traversal; these factors change the accumulation of TID/DDD and the SEE rate.
- TID response can be strongly affected by technology, bias, dose rate, rebound/time-dependent effects, and ELDRS susceptibility, especially for bipolar and BiCMOS linear devices.
- SEE susceptibility depends on LET, particle trajectory, device structure, bias, circuit topology, and sensitive volume; destructive modes such as SEL, SEB, and SEGR require special attention for power and CMOS/BiCMOS technologies.
- Published test data should be checked for exact product identity, process and grade, tested conditions, failure criteria, and validity of the test setup before being reused for mission assurance.

# Related concepts
- [source evidence](ti-radiation-handbook.md)
- [Semiconductor Technology Radiation Sensitivity](../assurance-workflow/semiconductor-technology-radiation-sensitivity.md)
- [Radiation Hardening and Mitigation Techniques](../assurance-workflow/radiation-hardening-and-mitigation-techniques.md)
- [Published Radiation Test Data Applicability](../assurance-workflow/published-radiation-test-data-applicability.md)

# Citations
- [TI Radiation Handbook for Electronics](ti-radiation-handbook.md)
