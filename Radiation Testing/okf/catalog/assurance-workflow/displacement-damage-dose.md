---
type: Assurance Workflow
title: Displacement Damage Dose (DDD)
description: Non-ionizing damage from particle displacement in material lattices that
  can degrade optoelectronic, semiconductor, and detector performance.
tags:
- radiation-effect
- ddd
- non-ionizing
timestamp: '2026-08-09T05:55:24Z'
---
Non-ionizing damage from particle displacement in material lattices that can degrade optoelectronic, semiconductor, and detector performance.

# Assurance implications
- Must be translated from mission environment assumptions into part-level exposure or susceptibility requirements through [mission-profile level derivation](mission-profile-level-derivation.md).
- Drives test method selection under [radiation effects test program](../test-plans/radiation-effects-test-program.md).
- Results feed residual-risk decisions in [RHA assurance workflow](rha-assurance-workflow.md).

# Related tests
- [TID testing](../test-operations/testing-methods-procedures/total-ionizing-dose-test.md)
- [SEE testing](../test-operations/testing-methods-procedures/single-event-effects-test.md)
- [DDD testing](../test-operations/testing-methods-procedures/displacement-damage-test.md)

# Citations
- [sources/compendium](compendium.md)
- [sources/standards2015](../standards-guidelines/standards2015.md)

# TI handbook DDD augmentation
- The handbook describes displacement damage as non-ionizing lattice damage caused by energetic electrons, protons, neutrons, and secondary particles, with damage distributed through the active volume rather than only at surfaces or interfaces.
- Device sensitivity varies by technology: BJTs and optoelectronic devices can be sensitive through recombination and gain degradation, while many MOSFETs tolerate higher displacement damage before switching-speed or drive-strength degradation dominates.
- DDD mission relevance depends on orbit, shielding, particle species and energy, fluence, and mission lifetime.

# Additional citations
- [sources/ti-radiation-handbook](../standards-guidelines/ti-radiation-handbook.md)
