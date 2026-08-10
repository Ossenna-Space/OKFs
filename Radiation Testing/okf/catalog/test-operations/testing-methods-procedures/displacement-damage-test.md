---
type: Test Operations / Testing Methods & Procedures
title: Displacement Damage Test
description: Radiation test approach for displacement damage degradation, typically
  requiring particle species, fluence, and application-specific degradation criteria.
tags:
- test
- ddd
- fluence
timestamp: '2026-08-09T05:55:24Z'
---
Radiation test approach for displacement damage degradation, typically requiring particle species, fluence, and application-specific degradation criteria.

# Inputs
- Mission and shielding assumptions from [mission-profile level derivation](../../assurance-workflow/mission-profile-level-derivation.md).
- Device application conditions and part criticality from [parts assurance workflow](../../assurance-workflow/parts-selection-screening-qualification-derating.md).
- Applicable standard or guideline requirements.

# Outputs
- Test report evidence for [RHA acceptance, waiver, or mitigation decisions](../../assurance-workflow/rha-assurance-workflow.md).
- Parameter degradation, event-rate, threshold, cross-section, or pass/fail evidence as applicable.

# Related concepts
- [effects/displacement-damage-dose](../../assurance-workflow/displacement-damage-dose.md)

# Citations
- [sources/compendium](../../assurance-workflow/compendium.md)
- [sources/standards2015](../../standards-guidelines/standards2015.md)

# TI handbook DDD test augmentation
- The handbook treats displacement damage testing as species-, energy-, fluence-, and device-technology-dependent, with neutron testing included in the qualification overview.
- DDD interpretation should focus on application-critical electrical or optical parameter degradation rather than only accumulated fluence.

# Additional citations
- [sources/ti-radiation-handbook](../../standards-guidelines/ti-radiation-handbook.md)

# ANSTO facility evidence
- ANSTO's provider page describes Centre for Accelerator Science proton-beam DDD capability up to 15 MeV, with stated silicon range up to 2000 µm and flux from 10⁴ to 10⁹ particles/(cm²·s), plus vacuum and ambient-air microbeam and scanning arrangements.
- These values are facility-selection inputs, not a DDD test method or mission acceptance criterion. Confirm species, spectrum, fluence, displacement-damage equivalence, dosimetry, uniformity, article configuration, monitored parameters, uncertainty, and degradation limits against the governing assurance plan.
- Facility irradiation does not by itself establish qualification, certification, standards compliance, or mission acceptance.

# ANSTO citations
- [ANSTO radiation-testing capabilities](../testing-facilities/facility-capabilities/ansto-radiation-testing-capabilities.md)
- [ANSTO service and assurance boundary](../testing-facilities/facility-capabilities/ansto-radiation-testing-service-boundary.md)
- [ANSTO Radiation Testing Facilities Technical Specifications](../testing-facilities/facility-capabilities/ansto-radiation-capabilities.md)
