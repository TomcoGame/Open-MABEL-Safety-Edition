# Item definition — ID-001 (draft v0.1)

## Purpose
Open MABEL Safety Edition is a proposed safety-capable variant of a mobile, dual-arm, dexterous research robot. The baseline includes a swerve mobile base, vertical lift, pitching torso, active head, two arms, two hands, teleoperation and learned-policy interfaces.

## Intended use — preliminary
- Controlled research and development by trained operators.
- Indoor, level, dry environments with controlled access during initial testing.
- Simulation, teleoperation and supervised autonomous manipulation within validated limits.
- Safety engineering infrastructure reusable across future application configurations.

## Excluded from this baseline
- Unsupervised operation in occupied homes or public spaces.
- Carrying people, medical care, hazardous materials, stair climbing, or outdoor road operation.
- Any assertion of safe human-robot collaboration, safety certification or PL/SIL attainment.

## System boundary
Includes mechanical structure, mobile base, arms, hands, lift, actuators, brakes (if fitted), power distribution, sensors, safety controller (proposed), host computer, ROS 2, gateway, teleoperation interfaces, firmware and physical operator controls.

External interfaces: operator, bystanders, environment, mains charger, network, service tools and carried objects.

## Operating states (candidate)
De-energized; startup/self-test; standby; enabled/manual; enabled/autonomous; protective stop; emergency stop; fault latched; controlled recovery. Entry/exit criteria and reset behavior are TBD.

## Parameters requiring measurement
Mass and center of gravity across lift/arm positions; maximum payload; stopping distances; maximum speeds; joint torque limits; brake holding capacity; power-loss behavior; sensor coverage; network watchdog latency; expected environmental conditions.

## Assumptions and dependencies
Safety functions and required performance levels must be derived from a documented ISO 12100 risk assessment. Determine applicability of ISO 13482, ISO 10218, ISO 3691-4, ISO 13849 and IEC 60204-1 by intended use and product classification; do not assume all apply.

**Approval:** not approved. **Evidence:** none.
