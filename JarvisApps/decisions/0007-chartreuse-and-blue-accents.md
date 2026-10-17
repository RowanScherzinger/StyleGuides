# 0007. Chartreuse status lights and blue high-contrast accents

Date: 2026-10-17
Status: accepted (partly supersedes 0004)

## Decision
- Status lights can use colours outside the warm palette. OK / running is chartreuse
  (`--palette-chartreuse-500`, `#a3d21f`).
- Blue accents are allowed in high-contrast areas: arc blue (`--palette-arc-400`, `#6ec6ff`)
  for info status, crosshairs, selected points and other small marks that must pop.
- Both are for small accents only. Surfaces, borders, buttons and the main accent stay warm.

## Why
User decision: "Other colours can be used for status lights, I quite like chartreuse for
green, and blue accents for high contrast areas is ok." A non-warm OK colour also makes
"running" easy to tell apart from gold live values at a glance.

The specific hex values are Claude's picks. Chartreuse is pushed slightly towards yellow
so it sits with the gold. Measured contrast: chartreuse 11.2:1 and blue 10.6:1 on app
glass, 7.8 and 7.4 on overlay glass over white.

## Affects
`tokens/tokens.css`, `docs/01-color.md`, `docs/00-principles.md`, `CLAUDE.md`, `tools/contrast.py`.
