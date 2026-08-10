---
type: Test Operations / Testing Methods & Procedures
title: Total Ionizing Dose Test
description: Ground test method for cumulative ionizing dose susceptibility, often
  referenced through MIL-STD-883 Method 1019 heritage and NASA/NEPP discussions.
tags:
- test
- tid
- method-1019
timestamp: '2026-08-09T05:55:24Z'
---
Ground test method for cumulative ionizing dose susceptibility, often referenced through MIL-STD-883 Method 1019 heritage and NASA/NEPP discussions.

# Inputs
- Mission and shielding assumptions from [mission-profile level derivation](../../assurance-workflow/mission-profile-level-derivation.md).
- Device application conditions and part criticality from [parts assurance workflow](../../assurance-workflow/parts-selection-screening-qualification-derating.md).
- Applicable standard or guideline requirements.

# Outputs
- Test report evidence for [RHA acceptance, waiver, or mitigation decisions](../../assurance-workflow/rha-assurance-workflow.md).
- Parameter degradation, event-rate, threshold, cross-section, or pass/fail evidence as applicable.

# Related concepts
- [effects/total-ionizing-dose](../../assurance-workflow/total-ionizing-dose.md)

# Citations
- [sources/mil883](../../standards-guidelines/mil883.md)
- [sources/tm1019](../../standards-guidelines/tm1019.md)
- [sources/compendium](../../assurance-workflow/compendium.md)

# TI handbook TID test augmentation
- The handbook summarizes a basic TID flow: package/prepare DUTs, electrically test, burn-in if normally required, bias under operating conditions, irradiate to the rated level, and retest against functional and parametric limits.
- It states that TI uses MIL-STD-883 TM 1019 for TID qualification and RLAT, with cobalt-60 as the common source, and discusses HDR, LDR, MAAT/rebound, room-temperature anneal, ELDRS characterization, and electrical test time windows.
- For ELDRS characterization, it highlights split testing across HDR/LDR and biased/unbiased conditions and the risk of underestimating degradation if only HDR data is used for ELDRS-sensitive products.

# Additional citations
- [sources/ti-radiation-handbook](../../standards-guidelines/ti-radiation-handbook.md)

# ANSTO facility evidence
- ANSTO's provider page describes cobalt-60 TID capability at GATRI and the Gammacell 220, including stated photon energies, dose rates, field geometry, sample-volume constraints, and real-time measurement cabling. It also describes monochromatic synchrotron X-rays for TID, pre-screening, sensitive-area mapping, and laminography.
- These provider claims are facility-selection inputs, not a TID qualification method or acceptance criterion. Confirm source suitability, dose rate, dosimetry and calibration traceability, uniformity, bias, temperature, annealing, electrical-test timing, article geometry, uncertainty, and failure criteria against the governing method and mission assurance plan.
- The X-ray dose-rate text in the retained page is internally ambiguous and requires confirmation with ANSTO before use. X-ray pre-screening or mapping does not by itself establish cobalt-60 equivalence, qualification, certification, standards compliance, or mission acceptance.

# ANSTO citations
- [ANSTO radiation-testing capabilities](../testing-facilities/facility-capabilities/ansto-radiation-testing-capabilities.md)
- [ANSTO service and assurance boundary](../testing-facilities/facility-capabilities/ansto-radiation-testing-service-boundary.md)
- [ANSTO Radiation Testing Facilities Technical Specifications](../testing-facilities/facility-capabilities/ansto-radiation-capabilities.md)
