---
type: Assurance Workflow
title: Radiation Hardness Assurance Workflow
description: End-to-end workflow for identifying mission radiation risks, deriving
  levels, selecting tests, evaluating parts, documenting margins, and managing residual
  risk.
tags:
- workflow
- rha
- assurance
timestamp: '2026-08-09T05:55:24Z'
---
End-to-end workflow for identifying mission radiation risks, deriving levels, selecting tests, evaluating parts, documenting margins, and managing residual risk.

# Procedure
1. Identify the mission radiation environment and applicable standards.
2. Derive part-level TID, SEE, and DDD requirements with margin and shielding assumptions.
3. Select candidate EEE parts and identify existing qualification, screening, derating, and radiation data.
4. Plan focused ground testing when existing evidence is insufficient for the application.
5. Evaluate test results against mission needs, document residual risk, and record mitigations or waivers.

# Related concepts
- [workflow/mission-profile-level-derivation](mission-profile-level-derivation.md)
- [workflow/parts-selection-screening-qualification-derating](parts-selection-screening-qualification-derating.md)
- [tests/radiation-effects-test-program](../test-plans/radiation-effects-test-program.md)

# Citations
- [sources/nesc_rha](../standards-guidelines/nesc_rha.md)
- [sources/ecss2025](../standards-guidelines/ecss2025.md)
- [sources/aires](../standards-guidelines/aires.md)

# TI handbook workflow augmentation
- Use the TI handbook as explanatory guidance when mapping mission environment to device mechanisms, selecting tests, and reviewing vendor evidence, while relying on NASA/ECSS/MIL standards for controlling requirements.
- Add technology-family review, mitigation review, and published-data applicability review before accepting existing radiation evidence for a part.
- Feed unresolved product identity, process-flow, grade, test-condition, failure-criteria, or setup-validity issues into waiver, mitigation, supplier question, or new-test decisions.

# Additional citations
- [sources/ti-radiation-handbook](../standards-guidelines/ti-radiation-handbook.md)
