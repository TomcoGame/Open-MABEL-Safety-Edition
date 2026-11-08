# Visual documentation authoring guide

[← Wiki home](README.md)

## Design tokens
- Background: white `#FFFFFF`
- Ink: charcoal `#171D26`
- Accent: safety yellow `#FFCF32`
- Neutral: `#69717C`
- Use the actual upstream MABEL imagery with attribution when depicting the physical baseline.

## Visual package per process
1. Hero infographic with purpose, system context and inputs/outputs.
2. Animated SVG showing the process sequence and decision points.
3. Static SVG fallback with identical substantive information.
4. Step-by-step Markdown guide with stable links to source artifacts.
5. Change history, reviewer and configuration applicability.

## Animation requirements
SVG must have accessible `<title>` and `<desc>`; avoid flashing, fast transitions and motion-dependent meaning. Include a static fallback. Prefer short sequential emphasis using SVG animation elements; GitHub may suppress animation depending on rendering context.

## Engineering integrity
Visuals are navigation and explanation aids. Status badges must come from reviewed records. Avoid asserting a safety function is implemented, tested or verified merely because an illustration depicts it. Distinguish conceptual sensors and safety zones from installed hardware.

## Review checklist
Technical owner validates interfaces and labels; safety reviewer validates terminology; documentation reviewer validates readability and links; release owner approves publication.
