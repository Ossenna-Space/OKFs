---
type: Assurance Workflow
title: Space Radiation Environment
description: Mission radiation environment consisting of trapped particles, solar
  particle events, galactic cosmic rays, and shielding-dependent transport to parts.
tags:
- environment
- mission-profile
- radiation
timestamp: '2026-08-09T05:55:24Z'
---
Mission radiation environment consisting of trapped particles, solar particle events, galactic cosmic rays, and shielding-dependent transport to parts.

# Assurance implications
- Must be translated from mission environment assumptions into part-level exposure or susceptibility requirements through [mission-profile level derivation](mission-profile-level-derivation.md).
- Drives test method selection under [radiation effects test program](../test-plans/radiation-effects-test-program.md).
- Results feed residual-risk decisions in [RHA assurance workflow](rha-assurance-workflow.md).

# Related tests
- [TID testing](../test-operations/testing-methods-procedures/total-ionizing-dose-test.md)
- [SEE testing](../test-operations/testing-methods-procedures/single-event-effects-test.md)
- [DDD testing](../test-operations/testing-methods-procedures/displacement-damage-test.md)

# Citations
- [sources/standards2015](../standards-guidelines/standards2015.md)
- [sources/nesc_rha](../standards-guidelines/nesc_rha.md)

# TI handbook environment augmentation
- The TI handbook identifies GCRs, solar radiation/solar energetic particle events, and trapped radiation belts as primary natural space radiation sources that influence electronics reliability.
- It emphasizes that on-board electronics exposure depends on orbit, mission duration, shielding, solar flare/CME history, and radiation-belt/South Atlantic Anomaly traversal.
- It distinguishes the terrestrial alpha/neutron environment from space exposure, which helps keep avionics/space RHA assumptions separate from terrestrial soft-error-rate assumptions.

# Additional citations
- [sources/ti-radiation-handbook](../standards-guidelines/ti-radiation-handbook.md)
