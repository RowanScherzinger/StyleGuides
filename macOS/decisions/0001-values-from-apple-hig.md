# 0001. Values come from Apple's HIG; gaps are proposed

Date: 2026-11-08
Status: accepted (use official Apple values); proposed (how the gaps are filled)

## Decision
Every value Apple publishes is copied from the Human Interface Guidelines: the system colours
in four variants (HIG > Color > Specifications, from the swatch images' alt text), the macOS
text styles and tracking (HIG > Typography), minimum text and control sizes and contrast
targets (HIG > Accessibility), and the menu bar height. Each token names its AppKit or SwiftUI
colour. Values Apple doesn't publish (neutral AppKit colours, radii, most sizes, durations)
are filled with what AppKit draws and marked *(Proposed)*.

## Why
The user asked for official Apple references where available. The HIG is Apple's public
source, versioned by its change log. Apple's macOS 27 design kit has the missing component
values, but it is only on Figma and Sketch's web viewer, so it couldn't be read on
2026-11-08. Copying approximate values without saying so was rejected: they would pass for
Apple's. When the kit or a Mac is available, replace the *(Proposed)* values from it.

## Affects
All of `tokens/tokens.css`; `docs/01-color.md`, `docs/02-typography.md`, `docs/03-spacing-layout.md`.
