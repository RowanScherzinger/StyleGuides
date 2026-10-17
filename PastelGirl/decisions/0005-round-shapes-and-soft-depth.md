# 0005. Round shapes and soft depth

Date: 2026-10-17
Status: proposed

## Decision
Radii 8 / 14 / 20 / 28px plus pills; buttons, chips and toggles are always pills. Depth comes
from blurred lifts, a top sheen and a faint pink glow ring, never from hard offset shadows.
Cards are frosted plum glass.

## Why
"Softer, rounder" (0002). Pills read as friendly and tappable; 20px cards are clearly round
without looking like bubbles. A soft-vs-sharp balance comes from silver hardware details
instead of sharp corners.

## Affects
`--radius-*`, `--shadow-*`, `--glow-*`, `--color-surface*`, `css/soft.css`, `docs/04-components.md`.
