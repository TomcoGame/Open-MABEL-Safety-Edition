# Safety requirements and traceability

[← Wiki home](README.md)

![Engineering thread](<../assets/branding/Open MABEL Safety Engineering Thread-4.png>)

## Purpose
Translate identified hazards and risk controls into verifiable, configuration-specific requirements.

## Workflow
1. Link each requirement to a hazard or parent requirement.
2. Specify the triggering condition, required behavior, safe state and relevant timing/performance constraints.
3. Identify allocated subsystem, interfaces, operating modes and fault assumptions.
4. Define objective acceptance criteria and verification method.
5. Review for ambiguity, feasibility, independence and conflicts.
6. Baseline revisions and propagate changes to architecture, tests and evidence.

## Source of truth
[Safety requirements register](../../safety/02_safety_requirements/safety_requirements.csv) · [Hazard register](../../safety/01_risk_assessment/hazard_register.csv).

A requirement is not evidence of implementation. Record verification results separately.

## Animated requirements workflow

![Safety requirements workflow](../assets/wiki/safety-requirements-animated.svg)

[Static accessible version](../assets/wiki/safety-requirements-static.svg)

## Worked example — illustrative only

**Parent scenario:** unintended lift descent. **Candidate requirement:** “When the monitored lift holding condition is lost, the safety-related control shall command the defined load-retention response within a validated reaction time under the specified operating conditions.” The reaction-time limit, sensing architecture, and safe state require engineering derivation; none are assumed here.

## Quality review

- [ ] One independently testable behavior per requirement
- [ ] Trigger and operating mode defined
- [ ] Safe state and fault response defined
- [ ] Performance criteria derived and measurable
- [ ] Bidirectional links to hazard, architecture and test

[Requirements review template](templates/requirements-review-template.csv)
