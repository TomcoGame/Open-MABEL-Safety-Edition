# Safety architecture concept — draft v0.1

## Separation principle

```text
Vision Pro / Browser / AI policy / ROS 2 / Nav2
                     |
              Motion command
                     v
        MABEL application controller
                     |
              Command interface
                     v
             Actuator subsystem
                     ^
                     | independent inhibit / safe stop interface
                     |
   Safety-related controller (candidate)
       ^           ^            ^
       |           |            |
 E-stop chain   Protective    Safe feedback
                sensors       / drive status
```

The drawing represents **proposed functions and interfaces**, not installed hardware. Existing MABEL software gates are retained as defense in depth, not credited as safety-rated controls.

## Design rules
1. Protective stop shall not depend on a functioning AI model, ROS 2 node, cloud service, browser or Wi-Fi connection.
2. Determine the safe state **per axis and configuration**. Removing torque can be unsafe for the vertical lift or a loaded arm; use validated brakes or mechanical retention as appropriate.
3. Evaluate stop categories and stopping times against applicable machinery requirements; do not assume an emergency stop can replace safeguarding.
4. Independent monitoring must detect faults in protective sensing, feedback, communication and final switching elements to the degree required by risk assessment.
5. Restart after stop requires deliberate action; reset alone shall not initiate hazardous motion.
6. Safe limits must account for changing mass distribution, payload, arm extension and lift height.
7. Distinguish operational collision avoidance from safety-rated protective detection.
8. Preserve diagnostic and fault logs without making logging a prerequisite for a protective response.

## Interfaces to define
- E-stop inputs and fault detection.
- Protective scanner/field inputs and mode selection.
- Safe motion feedback and actuator inhibit / STO availability.
- Lift brake command and brake-state monitoring.
- Power management and safe shutdown.
- Status-only interface from safety controller to ROS 2.
- Safe recovery and manual reset interface.

## Open questions
- Which existing drives offer certified STO or safe motion features, if any?
- Can the swerve drive achieve predictable stopping and steering behavior after torque removal?
- Does the lift have mechanical holding/braking independent of its motion controller?
- How will protective sensing cover moving arms and occluded areas?
- What product standard and required PLr/SIL apply to each safety function?

**Do not wire or deploy this concept as a safety system without component-level design and validation.**
