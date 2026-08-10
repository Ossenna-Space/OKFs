---
type: Assurance Workflow
title: Single Event Effects (SEE)
description: Prompt effects caused by a single energetic particle interaction, including
  destructive and non-destructive event modes.
tags:
- radiation-effect
- see
- particle
timestamp: '2026-08-09T05:55:24Z'
---
Prompt effects caused by a single energetic particle interaction, including destructive and non-destructive event modes.

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

# TI handbook SEE augmentation
- The handbook frames single-event transients as the archetype for SEE responses and distinguishes nondestructive soft errors from destructive effects.
- It covers SEU, SET/ASET/DSET, SEFI, SEL, SEGR, SEB, and prompt-dose-like transients, emphasizing that LET, trajectory, charge collection, bias, layout, and circuit topology determine observed response.
- Destructive events such as SEL, SEB, and SEGR require power control, current limiting, derating, and explicit test evidence rather than assuming recovery from soft errors.

# Additional citations
- [sources/ti-radiation-handbook](../standards-guidelines/ti-radiation-handbook.md)
