# Open MABEL Safety Edition — assurance workspace

**Status: CONCEPT / PRELIMINARY. Not safety-certified or validated for operation around people.**

This directory defines a controlled safety-engineering workstream for a general-purpose mobile bimanual robot. It does **not** imply that the existing hardware, ROS 2 stack, controller or proposed safety mechanisms meet a particular PL, SIL or product safety standard.

## Baseline and boundaries

- Upstream baseline: [robotmabel/open_mabel](https://github.com/robotmabel/open_mabel).
- Product concept: safety-capable research and development platform, not a safety-certified product.
- No moving, cleaning or other vertical-specific application is assumed.
- The existing `controller` tip-over gate and software stop logic are **non-safety-rated until independently assessed**.
- Never use a network, browser, AI policy or ROS 2 process as the sole protective stop path.

## Work products

1. [Item definition](00_item_definition/item_definition.md)
2. [Preliminary hazard register](01_risk_assessment/hazard_register.csv)
3. [Candidate safety requirements](02_safety_requirements/safety_requirements.csv)
4. [Safety architecture concept](03_safety_architecture/architecture.md)
5. [Hardware safety gap assessment](04_hardware_safety/gap_assessment.md)
6. [Software safety boundary](05_software_safety/software_boundary.md)
7. [Verification plan](07_verification_validation/verification_plan.md)
8. [Safety case status](08_safety_case/claim_evidence.md)

## Evidence maturity

| State | Meaning |
|---|---|
| Proposed | Requirement or architecture concept; no implementation evidence |
| Implemented, unverified | Code or hardware exists but has not been validated |
| Verified | Objective evidence demonstrates defined test criteria |
| Assessed | Independent review of scope, assumptions and evidence |

All work products here start **Proposed**. No safety integrity claim is made.

## Change control

Changes affecting protective sensing, actuator control, braking, power, fault responses, limits, or safety interfaces require documented impact analysis, updated traceability and appropriate re-verification. Preserve upstream notices and license boundaries.
