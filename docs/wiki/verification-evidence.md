# Verification and evidence

[← Wiki home](README.md)

![Digital thread](<../assets/branding/Open MABEL Safety Engineering Thread-4.png>)

## Purpose
Demonstrate the behavior of each allocated safety function for a defined configuration.

## Process
1. Select a baselined requirement and define acceptance criteria.
2. Specify test setup, robot configuration, instrumentation and preconditions.
3. Include nominal, fault, boundary and recovery scenarios as applicable.
4. Record measured outcomes and raw artifacts.
5. Review discrepancies and link changes to impacted requirements and hazards.
6. Approve results and connect them to the evolving safety argument.

## Source of truth
[Verification plan](../../safety/07_verification_validation/verification_plan.md) · [Claim and evidence register](../../safety/08_safety_case/claim_evidence.md).

## Evidence checklist
Configuration ID; requirement ID; procedure version; test environment; date; executor/reviewer; raw data; acceptance result; deviations; change reference.

## Animated verification workflow

![Verification and evidence workflow](../assets/wiki/verification-evidence-animated.svg)

[Static accessible version](../assets/wiki/verification-evidence-static.svg)

## Worked example — illustrative only

For a future lift-holding safety function, record the hardware revision, payload and lift position, triggering fault, commanded response, measured displacement and stopping/holding behavior, acceptance limits, raw sensor logs, and reviewer disposition. A successful demonstration in one setup does not establish performance across other configurations.

## Verification review gate

- [ ] Test references an approved requirement and configuration
- [ ] Preconditions and fault injection are reproducible
- [ ] Acceptance limits are explicit
- [ ] Raw data and deviations are retained
- [ ] Results have independent review where required
- [ ] Safety argument references the exact evidence version

[Evidence record template](templates/evidence-record-template.csv)
