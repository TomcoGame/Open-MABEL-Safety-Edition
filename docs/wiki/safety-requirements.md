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

## Requirements engineering worksheet — guided example

Read **left to right** across the first row. Each column is a decision the engineer must make, not just a workflow milestone.

| Hazard link | Trigger / operating mode | Required safety behavior | Allocation | Acceptance criteria | Verification / evidence |
|---|---|---|---|---|---|
| Example: unintended lift descent | Loss of monitored lift-holding condition during lift operation | Initiate the defined load-retention response | Safety-related lift control and holding mechanism (candidate) | Derive and document reaction time, load range and fault response | Planned fault-injection and load-holding tests; results pending |
| Mobile base unintended travel | To be analyzed | To be derived | TBD | TBD | TBD |
| Manipulator unexpected contact | To be analyzed | To be derived | TBD | TBD | TBD |

**Walkthrough:** (1) Start with the hazardous situation and its risk-reduction objective. (2) Define the exact condition that activates the function. (3) Write a single, testable required behavior and safe state. (4) Allocate responsibility and interfaces. (5) Derive measurable criteria. (6) Link a test and its reviewed evidence. Revisit the requirement whenever the hazard, configuration or design changes.

**Animated source:** [Open requirements workflow SVG](../assets/wiki/safety-requirements-animated.svg) · [Static SVG](../assets/wiki/safety-requirements-static.svg)

GitHub Wiki may not display externally hosted SVG images inline. The worksheet above is the always-visible teaching version; SVGs are optional linked supplements.

## Worked example — illustrative only

**Parent scenario:** unintended lift descent. **Candidate requirement:** “When the monitored lift holding condition is lost, the safety-related control shall command the defined load-retention response within a validated reaction time under the specified operating conditions.” The reaction-time limit, sensing architecture, and safe state require engineering derivation; none are assumed here.

## Quality review

- [ ] One independently testable behavior per requirement
- [ ] Trigger and operating mode defined
- [ ] Safe state and fault response defined
- [ ] Performance criteria derived and measurable
- [ ] Bidirectional links to hazard, architecture and test

[Requirements review template](templates/requirements-review-template.csv)
