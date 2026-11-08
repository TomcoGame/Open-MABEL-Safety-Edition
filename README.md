<p align="center"><img src=".github/banner.png" width="100%" alt="Open MABEL mobile bimanual robot"></p>

# Open MABEL Safety Edition

**An open, safety-engineering-focused development variant of [Open MABEL](https://github.com/robotmabel/open_mabel).**

> **STATUS: PRELIMINARY — NOT SAFETY-CERTIFIED.** This repository combines an upstream research robot baseline with a proposed safety engineering workstream. It is not validated for unsupervised operation, close human interaction, public environments or safety-critical deployment. Existing software gates must not be assumed safety-rated.

## Mission

Make Open MABEL a **safety-capable, general-purpose mobile manipulation platform** through risk-based requirements, independent protective-control architecture, documented hardware changes, verification and an auditable safety case. This is a standalone robotics project, **not specific to moving, cleaning or logistics**.

## Maturity and claims

| Area | Status |
|---|---|
| Upstream MABEL software, hardware and simulation | Imported baseline; not safety qualified |
| Item definition, hazard register, safety requirements | Preliminary draft |
| Independent safety controller and protective sensing | Proposed; not implemented |
| Safe drives, braking and load retention | Hardware gap assessment pending |
| Required PL/SIL and applicable product standards | Undetermined |
| Safety Edition verification and independent assessment | Not performed |
| Certification or deployment approval | None |

## Safety engineering workstream

Begin at **[safety/README.md](safety/README.md)**.

| Work product | Link |
|---|---|
| Item definition and operating boundaries | [Draft](safety/00_item_definition/item_definition.md) |
| Preliminary hazard register | [CSV](safety/01_risk_assessment/hazard_register.csv) |
| Candidate safety requirements | [CSV](safety/02_safety_requirements/safety_requirements.csv) |
| Independent safety architecture concept | [Draft](safety/03_safety_architecture/architecture.md) |
| Hardware gap assessment | [Checklist](safety/04_hardware_safety/gap_assessment.md) |
| Software safety boundary | [Draft](safety/05_software_safety/software_boundary.md) |
| Verification and validation plan | [Plan](safety/07_verification_validation/verification_plan.md) |
| Preliminary safety case | [Open claims](safety/08_safety_case/claim_evidence.md) |

**Safety principle:** ROS 2, teleoperation, learned policies and the upstream controller may propose motion, but must not be the sole enforcement mechanism for protective functions requiring safety integrity. The appropriate safe state is axis-dependent: removing torque from a vertical lift or loaded arm may create a falling-load hazard.

## Upstream robot capabilities

Open MABEL is a 56-DOF mobile bimanual robot featuring a three-module swerve base, vertical lift, pitching torso, active stereo head, two 7-DOF OpenArm-derived arms, two 17-DOF ORCA-derived hands, Apple Vision Pro teleoperation, ROS 2 Jazzy, MuJoCo simulation and learning pipelines.

```text
safety/             New safety engineering work products (draft)
hardware/           BOM, build guide and CAD
electrical/         PCB and electrical designs
firmware/           Base, arm, lift and hand firmware
hardware_bridge/    Device ownership and hardware abstraction
controller/         Whole-body controller and operational safety gates
ros/                ROS 2, SLAM and Nav2
simulation/         MuJoCo models and scenes
simulation_bridge/  Simulated hardware abstraction
server/             Teleoperation gateway and recording
web_gui/            Browser control studios
apps/               iOS and visionOS applications
sensors/            Sensor integration
calibration/        Actuator and system identification
robot_learning/     Data curation, imitation and reinforcement learning
```

## Getting started: upstream simulation

The following is the **upstream research simulation**, not a validated safety controller. Requirements include Python 3.10+, appropriate platform dependencies and a supported development environment.

```bash
git clone https://github.com/TomcoGame/Open-MABEL-Safety-Edition.git
cd Open-MABEL-Safety-Edition
conda create -n mabel python=3.11 -y
conda activate mabel
pip install -e controller/
pip install -r server/requirements.txt
python3 -m pytest controller/tests -q
bash server/run.sh --test
```

For the browser simulation studio, run `bash server/run.sh` and open `http://localhost:8097`. See [simulation](simulation/README.md), [server](server/README.md), [controller](controller/README.md), [hardware](hardware/README.md) and [ROS](ros/README.md) for subsystem guidance.

**These commands and tests have not been executed as part of the Safety Edition baseline.** Do not energize physical hardware on the assumption that this branch provides validated safety functions.

## Roadmap

1. Audit actuation paths, electrical protection, stopping behavior, motor capabilities and existing software gates.
2. Complete the item definition and ISO 12100-based risk assessment.
3. Derive safety functions, safe states, required integrity, diagnostics and response times.
4. Implement independent safety control, appropriate protective sensing, braking and load retention.
5. Verify via simulation, fault injection and controlled physical tests.
6. Build traceability and a reviewed safety case for a defined configuration and use.

Potential standards for applicability review: ISO 12100, ISO 13849-1/-2, ISO 13482, ISO 10218, ISO 3691-4 and IEC 60204-1. Listing a standard is **not** a compliance claim.

## Contributions

Contributions to risk assessment, protective architecture, fault handling, electrical and mechanical safeguards, tests and evidence are welcome. Safety-related changes should identify affected hazards, requirements, verification and configuration. Do not claim PL, SIL, certification or suitability for human collaboration without supporting evidence.

## Attribution and licensing

Based on **[robotmabel/open_mabel](https://github.com/robotmabel/open_mabel)**; not an official upstream safety release or certification.

- Software: [Apache-2.0](LICENSE)
- Hardware: [CERN-OHL-S-2.0](LICENSE-HARDWARE.txt)
- Documentation/media: [CC BY 4.0](LICENSE-DOCS.txt)
- Upstream and third-party attribution: [NOTICE](NOTICE) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)

Licenses do not grant trademark rights; confirm naming and branding rights before commercial distribution.
