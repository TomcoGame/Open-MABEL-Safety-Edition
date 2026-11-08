# Architecture model notes

The README includes Mermaid views for the conceptual system architecture, control authority, structural breakdown, proposed state machine, traceability and roadmap. GitHub renders these diagrams natively.

The accompanying `mabel-safety-model.sysml` is a **SysML v2-style illustrative sketch**, not a validated or executable model. It is not authoritative for safety allocations or interface definitions.

## Interpretation
- Solid architecture connections represent intended logical interactions, not verified physical wiring.
- The safety controller and associated protective components are **proposed**.
- No safe torque off, brake, sensor or stop performance is implied.
- Detailed IBD ports, item flows, requirement satisfaction, verification relationships, units and configuration variants remain future work.

## Model acceptance criteria (future)
1. Establish a toolchain and parse a normative SysML v2 model.
2. Define explicit interfaces, port types, allocations and failure responses.
3. Trace requirements to blocks and verification cases.
4. Validate architecture against as-built hardware and firmware.
5. Baseline models under change control.
