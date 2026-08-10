---
type: Assurance Workflow
title: Radiation Hardening and Mitigation Techniques
description: Workflow concept for selecting process, layout, circuit, shielding, and
  system-level mitigations against electronics radiation effects.
tags:
- workflow
- mitigation
- rhbp
- rhbd
- redundancy
timestamp: '2026-08-09T05:55:24Z'
---
Radiation mitigation should be matched to the dominant effect, the technology family, and the mission environment. The TI handbook distinguishes shielding, radiation hardening by process (RHBP), radiation hardening by design (RHBD), layout techniques, circuit redundancy, and system-level error handling.

# Procedure
1. Identify dominant mission threats: [TID](total-ionizing-dose.md), [SEE](single-event-effects.md), [DDD](displacement-damage-dose.md), prompt dose, terrestrial neutron/alpha, or mixed exposure.
2. Check whether shielding is physically and mass-budget practical; in many space or terrestrial particle environments, intrinsic device robustness and design mitigation are still required.
3. For process mitigation, evaluate substrate/epi choices, SOI/BOX isolation, removal of alpha or boron-10 sources, oxide/isolation changes, and vendor-controlled radiation-hard process flows.
4. For layout and circuit mitigation, evaluate guard rings, enclosed/annular layouts, transistor sizing, DICE latches, triplicated logic, memory interleaving, parity, ECC/EDAC, and lockstep or voting architectures.
5. Verify the mitigation with radiation testing or supplier evidence under representative application bias, voltage, load, frequency, temperature, and failure criteria.

# Related concepts
- [Semiconductor Technology Radiation Sensitivity](semiconductor-technology-radiation-sensitivity.md)
- [Radiation Effects Test Program](../test-plans/radiation-effects-test-program.md)
- [Published Radiation Test Data Applicability](published-radiation-test-data-applicability.md)

# Citations
- [TI Radiation Handbook for Electronics](../standards-guidelines/ti-radiation-handbook.md)
