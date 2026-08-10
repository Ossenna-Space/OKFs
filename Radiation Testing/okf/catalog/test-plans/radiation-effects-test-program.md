---
type: Test Plans
title: Radiation Effects Test Program
description: Integrated test planning and execution program for evaluating candidate
  spacecraft electronics against TID, SEE, and DDD risk.
tags:
- test
- program
- rha
timestamp: '2026-08-09T05:55:24Z'
---
Integrated test planning and execution program for evaluating candidate spacecraft electronics against TID, SEE, and DDD risk.

# Inputs
- Mission and shielding assumptions from [mission-profile level derivation](../assurance-workflow/mission-profile-level-derivation.md).
- Device application conditions and part criticality from [parts assurance workflow](../assurance-workflow/parts-selection-screening-qualification-derating.md).
- Applicable standard or guideline requirements.

# Outputs
- Test report evidence for [RHA acceptance, waiver, or mitigation decisions](../assurance-workflow/rha-assurance-workflow.md).
- Parameter degradation, event-rate, threshold, cross-section, or pass/fail evidence as applicable.

# Related concepts
- [tests/total-ionizing-dose-test](../test-operations/testing-methods-procedures/total-ionizing-dose-test.md)
- [tests/single-event-effects-test](../test-operations/testing-methods-procedures/single-event-effects-test.md)
- [tests/displacement-damage-test](../test-operations/testing-methods-procedures/displacement-damage-test.md)

# Citations
- [sources/compendium](../assurance-workflow/compendium.md)
- [sources/nesc_rha](../standards-guidelines/nesc_rha.md)
- [sources/standards2015](../standards-guidelines/standards2015.md)

# TI handbook test-program augmentation
- The handbook states that its testing chapter is an overview, not a substitute for the governing standards; the actual standards remain authoritative for qualification details.
- It expands program planning considerations to include TID, SEE, DDD, prompt-dose/dose-rate effects, terrestrial neutron/alpha testing, sample preparation, source selection, dose-rate selection, application bias/load, and report applicability.
- It supports treating vendor reports as evidence inputs that must be checked against exact device identity, tested conditions, and mission failure criteria.

# Additional citations
- [sources/ti-radiation-handbook](../standards-guidelines/ti-radiation-handbook.md)

# HIAF-SIBL facility planning evidence
- The provider brochure for [HIAF-SIBL](../test-operations/testing-facilities/hiaf-sibl.md) supplies facility-selection inputs for heavy-ion and proton campaigns: stated species and energies, SRIM-derived LET/range in silicon, flux, chamber and irradiation-area limits, vacuum operation, positioning, feedthroughs, mounts, beam monitoring, access arrangements, and fees.
- Treat these as provider-stated capabilities to be confirmed during test planning, not as standards requirements or proof that a proposed setup satisfies a qualification method.
- The program must separately identify the governing standards, mission-derived levels, device configuration, dosimetry and uncertainty controls, test conditions, acceptance criteria, reporting needs, and assurance authority.
- HIAF-SIBL explicitly says it does not provide formal radiation certification; its test output can support an assurance decision but does not replace that decision.

# HIAF-SIBL citations
- [HIAF-SIBL radiation-testing capabilities](../test-operations/testing-facilities/facility-capabilities/hiaf-sibl-radiation-testing-capabilities.md)
- [HIAF-SIBL service and certification boundary](../test-operations/testing-facilities/facility-capabilities/hiaf-sibl-service-boundary.md)
- [HIAF-SIBL Radiation Testing Capabilities Brochure](../test-operations/testing-facilities/facility-capabilities/hiaf-sibl-brochure.md)

# ANSTO facility planning evidence
- The provider page for [ANSTO radiation-testing facilities](../test-operations/testing-facilities/ansto-radiation-testing-facilities.md) supplies facility-selection inputs for SEE ion beams, DDD proton beams, cobalt-60 TID, and synchrotron X-ray TID or pre-screening work.
- Treat its technical values and service descriptions as provider claims requiring current confirmation, not as standards requirements or proof of qualification, certification, standards compliance, or mission acceptance.
- The program must separately establish governing methods, mission-derived levels, article configuration, dosimetry and uncertainty controls, bias and monitoring, acceptance criteria, reporting, and assurance authority.
- Confirm the ambiguous X-ray dose-rate expression with ANSTO before using it in a test plan.

# ANSTO citations
- [ANSTO radiation-testing capabilities](../test-operations/testing-facilities/facility-capabilities/ansto-radiation-testing-capabilities.md)
- [ANSTO radiation-testing access](../test-operations/testing-facilities/facility-access/ansto-radiation-testing-access.md)
- [ANSTO service and assurance boundary](../test-operations/testing-facilities/facility-capabilities/ansto-radiation-testing-service-boundary.md)
- [ANSTO Radiation Testing Facilities Technical Specifications](../test-operations/testing-facilities/facility-capabilities/ansto-radiation-capabilities.md)
