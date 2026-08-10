---
type: Test Operations / Testing Methods & Procedures
title: Single Event Effects Test
description: Particle-beam evaluation of single-event susceptibility for device functions
  and application-specific operating conditions.
tags:
- test
- see
- heavy-ion
- proton
timestamp: '2026-08-09T05:55:24Z'
---
Particle-beam evaluation of single-event susceptibility for device functions and application-specific operating conditions.

# Inputs
- Mission and shielding assumptions from [mission-profile level derivation](../../assurance-workflow/mission-profile-level-derivation.md).
- Device application conditions and part criticality from [parts assurance workflow](../../assurance-workflow/parts-selection-screening-qualification-derating.md).
- Applicable standard or guideline requirements.

# Outputs
- Test report evidence for [RHA acceptance, waiver, or mitigation decisions](../../assurance-workflow/rha-assurance-workflow.md).
- Parameter degradation, event-rate, threshold, cross-section, or pass/fail evidence as applicable.

# Related concepts
- [effects/single-event-effects](../../assurance-workflow/single-event-effects.md)

# Citations
- [sources/compendium](../../assurance-workflow/compendium.md)
- [sources/standards2015](../../standards-guidelines/standards2015.md)

# TI handbook SEE test augmentation
- The handbook identifies heavy-ion and proton testing as primary SEE approaches and notes that test setup, equipment, LET/incident-angle choices, fluence limits, and Weibull/cross-section interpretation affect results.
- It calls out event-specific considerations for SEL, SEFI, SET, SEU, SEGR, and SEB, reinforcing the need to tailor stimuli, monitoring, and failure criteria to the device function and application.
- Published SEE data should be checked for exact test conditions and trigger thresholds before being reused for a mission-specific acceptance decision.

# Additional citations
- [sources/ti-radiation-handbook](../../standards-guidelines/ti-radiation-handbook.md)

# HIAF-SIBL facility evidence
- The provider brochure for [HIAF-SIBL](../testing-facilities/hiaf-sibl.md) describes heavy-ion and proton beams, LET/range values calculated in silicon, flux, vacuum chamber limits, movable and tilting sample positioning, electrical feedthroughs, and beam monitoring that may be relevant when assessing SEE test feasibility.
- These capability statements do not define the governing SEE test method or acceptance criteria. Before use, confirm the selected species, energy, LET at the sensitive volume, range through package and overburden, flux/fluence, uniformity, dosimetry, operating configuration, monitoring, and incident-angle plan against applicable standards and mission requirements.
- HIAF-SIBL explicitly states that it does not provide formal radiation certification; facility test results remain evidence for the responsible assurance authority to interpret.

# HIAF-SIBL citations
- [HIAF-SIBL radiation-testing capabilities](../testing-facilities/facility-capabilities/hiaf-sibl-radiation-testing-capabilities.md)
- [HIAF-SIBL service and certification boundary](../testing-facilities/facility-capabilities/hiaf-sibl-service-boundary.md)
- [HIAF-SIBL Radiation Testing Capabilities Brochure](../testing-facilities/facility-capabilities/hiaf-sibl-brochure.md)

# ANSTO facility evidence
- ANSTO's provider page describes Centre for Accelerator Science proton and heavier-ion beams, LET and range in silicon, flux, vacuum and ambient-air microbeam arrangements, scanning areas, enclosure limits, and real-time measurement cabling that may be relevant to SEE feasibility.
- These are provider-stated capabilities, not a governing SEE method or acceptance criteria. Confirm species, energy, LET at the sensitive volume, range through package and overburden, flux and fluence, uniformity, dosimetry, incident angle, device state, monitoring, and reporting against the applicable standard and mission requirements.
- Facility irradiation does not by itself establish qualification, certification, standards compliance, or mission acceptance.

# ANSTO citations
- [ANSTO radiation-testing capabilities](../testing-facilities/facility-capabilities/ansto-radiation-testing-capabilities.md)
- [ANSTO service and assurance boundary](../testing-facilities/facility-capabilities/ansto-radiation-testing-service-boundary.md)
- [ANSTO Radiation Testing Facilities Technical Specifications](../testing-facilities/facility-capabilities/ansto-radiation-capabilities.md)
