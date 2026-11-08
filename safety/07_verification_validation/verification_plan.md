# Preliminary verification and validation plan

All test cases are **planned, not executed**. Hazardous hardware tests require a separately approved procedure, exclusion zone, instrumentation and emergency response.

| Test ID | Linked requirements | Planned verification | Acceptance criteria status |
|---|---|---|---|
| VT-001 | SR-001 | E-stop actuation under representative motion | Safe stop time and behavior TBD |
| VT-002 | SR-002 | Person/object protective-field challenge | Detection coverage and stop distance TBD |
| VT-003 | SR-003 | Commanded speed over limit and feedback fault | Validated speed bound TBD |
| VT-004 | SR-004 | Joint/workspace overtravel request | Validated position bound TBD |
| VT-005 | SR-005 | Controlled power-loss/load-holding test | No uncontrolled descent/release within envelope; quantitative limits TBD |
| VT-006 | SR-006 | Lift/payload/arm-position stability sweep | Validated stability margins TBD |
| VT-007 | SR-007 | Network drop and stale-command injection | Safe response deadline TBD |
| VT-008 | SR-008 | Reset/restart state-machine test | No motion on reset alone |
| VT-009 | SR-009 | Electrical protection inspection and testing | Electrical acceptance criteria TBD |
| VT-010 | SR-010 | Energy isolation/service simulation | Isolation criteria TBD |

## Evidence recording
Record baseline commit SHA, hardware revision, test environment, instruments and calibration, steps, expected and actual results, failures, reviewer and approval. Store objective results separately from plans.

## Simulation first
Use MuJoCo for fault scenarios, geometry and state-machine validation. Simulation results do not replace physical stopping-distance, electrical, mechanical, or protective-device validation.
