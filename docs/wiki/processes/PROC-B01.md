# PROC-B01 — Item Definition and Operating Context

**Status:** Draft for technical review · **Revision:** 0.1 · **Application:** Open MABEL Safety Edition · **Process owner:** To assign

> This is an original project procedure framework. Applicability and clause-level coverage must be checked against licensed standards and a defined robot configuration.

## 1. Purpose and scope

Establish what Open MABEL is, its boundaries and intended operating conditions for each configuration. Applies to industrial mobile manipulation reference configurations and is tailored when other application profiles are selected.

## 2. Normative references to assess

ISO 12100; ISO 10218 where applicable; ANSI/A3 R15.08 where applicable. The [standards register](standards-register.csv) records editions and decisions; a listing here does not assert full applicability.

## 3. Entry criteria and inputs

Robot hardware/software BOM, task description, environment, interfaces. All inputs must identify configuration and revision.

## 4. Responsibilities

Systems engineer, application owner, safety reviewer. The designated safety owner must confirm responsibilities and review independence before release.

## 5. Procedure

1. Identify robot variant and revision.
2. Describe base, lift, torso, arms, hands and controllers.
3. Specify tasks, payloads, workspace and human interaction.
4. Identify energy sources and retained-energy mechanisms.
5. Define modes, remote operation and fault recovery.
6. Record boundaries, foreseeable misuse and environmental constraints.
7. Approve the baseline for risk assessment.

## 6. Decision gates and acceptance criteria

No hazard analysis begins without a versioned operating context. Open assumptions and deviations must have named owners and disposition dates.

## 7. Outputs and controlled records

Item definition, operating modes, interfaces, assumptions and exclusions. Store outputs in the main repository with identifiers, revisions, approval status and links to related hazards, requirements, architecture and tests.

## 8. Traceability and change control

Any change to the robot configuration, intended use, environment, safety function or applicable standard triggers an impact review. Link changed process outputs to the [master process register](process-register.csv) and associated safety work products.

## 9. Visual learning and supporting material

Use the [animated lifecycle map](../../assets/wiki/safety-lifecycle-animated.svg) and [static fallback](../../assets/wiki/safety-lifecycle-static.svg). Process-specific diagrams and worked examples will be reviewed before publication as engineering guidance.

## 10. Review record

| Role | Reviewer | Decision | Date |
|---|---|---|---|
| Process owner | TBD | Pending | TBD |
| Technical reviewer | TBD | Pending | TBD |
| Safety reviewer | TBD | Pending | TBD |

[← Process library](README.md) · [← Wiki home](../README.md)
