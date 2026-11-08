# Hardware safety gap assessment — initial screening

This is a **review checklist**, not a completed hardware audit. Existing components have not been qualified.

| Area | Existing baseline to inspect | Required investigation | Status |
|---|---|---|---|
| Base | REV MAXSwerve modules, drive firmware | Braking, torque removal, coasting, steering on fault, feedback integrity | Open |
| Arms | OpenArm-derived actuators and CAN interfaces | Safe torque removal, limits, feedback, holding on fault | Open |
| Hands | ORCA-derived servo hands | Pinch hazards, force, loss-of-grip response | Open |
| Lift | Powered vertical column and lift firmware | Anti-drop, brake capacity, power-loss behavior | Open |
| Controller | Jetson, Teensy, Pico and host bridge | Independent safety controller and safe I/O architecture | Open |
| Sensing | Cameras, LiDAR and other sensors | Protective sensing certification, diagnostic coverage, occlusion | Open |
| Power | Battery, power distribution, carrier PCB | Fusing, isolation, protective bonding, charging, thermal events | Open |
| Operator | Vision Pro, mobile app, browser | Physical E-stop access, enabling, reset, loss-of-link behavior | Open |

## Evidence to collect
Schematics, wiring diagrams, drive datasheets, brake specs, safety manuals, firmware source, stopping-time measurements, component fault behavior, safety-related diagnostic data, and current BOM revisions.

## Decision gate
Do not assign PL/SIL claims to the platform until each safety function has a defined boundary, required integrity, component evidence, fault analysis and validation plan.
