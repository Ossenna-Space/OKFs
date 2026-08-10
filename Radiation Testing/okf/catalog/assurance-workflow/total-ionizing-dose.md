---
type: Assurance Workflow
title: Total Ionizing Dose (TID)
description: Cumulative ionizing radiation effect that can shift device parameters
  and degrade electronic function over mission life.
tags:
- radiation-effect
- tid
- dose
timestamp: '2026-08-09T05:55:24Z'
---
Cumulative ionizing radiation effect that can shift device parameters and degrade electronic function over mission life.

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
- [sources/tm1019](../standards-guidelines/tm1019.md)
- [sources/standards2015](../standards-guidelines/standards2015.md)

# TI handbook TID augmentation
- The handbook describes TID as cumulative trapped charge and interface-state damage, especially in oxides and isolation structures, causing parameter shifts, leakage, or functional failure.
- Dose-rate, bias, process, oxide thickness, package, and post-fabrication factors can materially affect response; ELDRS is a key concern for some linear bipolar and BiCMOS products.
- Rebound/time-dependent effects and low-dose-rate application environments should be considered when interpreting high-dose-rate qualification data.

# Additional citations
- [sources/ti-radiation-handbook](../standards-guidelines/ti-radiation-handbook.md)
