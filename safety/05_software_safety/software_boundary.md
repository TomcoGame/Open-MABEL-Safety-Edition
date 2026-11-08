# Software safety boundary — draft

## Existing control components to audit
- `controller/mabel/motion_model/tip_over.py`: stability-related operational gate.
- `controller/mabel/safety/engagement.py`: engagement logic.
- `controller/mabel/teleop_engine/safety.py`: teleoperation safety-related behavior.
- `hardware_bridge/`: sole hardware ownership claim in upstream architecture.
- `server/`: teleoperation gateway and command transport.
- `firmware/`: drive, arm, lift and hand interfaces.

These paths are **audit targets**; their existence is not evidence of safety integrity.

## Required software architecture
- Non-safety control may propose motion, but may not bypass safety-related hardware enforcement.
- Define freshness, sequencing, range and authorization checks for command interfaces.
- Define startup inhibit, mode transitions, fault latching, reset and restart requirements.
- Safety-related controller software shall have a lifecycle and evidence appropriate to its assigned integrity target.
- Maintain traceability: hazard → safety function → safety requirement → architecture → implementation → verification → residual risk.
- Include negative tests for stale commands, malformed messages, bus faults, sensor disagreement and actuator feedback faults.

## Immediate engineering tasks
1. Trace every command path from application through controller to physical actuator.
2. Identify direct actuator access and bypass possibilities.
3. Document all current stop mechanisms and their dependencies.
4. Establish a reproducible baseline test suite before altering motion code.
5. Implement simulation-only safety state-machine tests before selecting hardware.

**No changes to motion-control firmware are included in this v0.1 documentation baseline.**
