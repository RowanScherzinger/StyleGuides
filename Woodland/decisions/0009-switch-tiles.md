# 0009. On/off controls on dense screens are one-row switch tiles

Date: 2026-11-13
Status: accepted (the tile, its state circle, the level fill, long-press for the rarer
action, and the on/off colours as shown on the Home Assistant dashboard); proposed (sizes,
the corner flag, and how a lock is coloured, which is still open)

## Decision
- **Accepted.** On a dense dashboard an on/off control is a one-row tile: an icon in a small
  circle, then the name, no state text. The circle carries the state.
- **Accepted.** A dimmable light's tile fills left to right to its level, and dragging
  left-right sets it. Tap still toggles. Long-press is for one rarer action on the same thing.
- **Accepted.** State colours: a light that is on is walnut (`--color-secondary*`, a
  lantern), anything else that is on is moss (`--color-accent*`), off is
  `--color-status-idle`. The small labels are sentence case in `--font-sans`.
- **Proposed.** Sizes: one grid row tall, a 28px circle, the name in `--text-md`, the level
  and the corner flag in `--text-xs`. The flag uses `--color-status-warning`.
- **Open.** A lock's circle. The Home Assistant dashboard currently shows a secured lock in
  fern green and an unsecured one in rowan red, with a padlock icon. That breaks two rules
  in this guide: green status always carries the sprout glyph, and rowan red is only for
  danger. It was inherited from the dashboard's other theme. Decide the Woodland colours.

## Why
The user designed this control on the Home Assistant dashboards, first under the other theme
there, then asked for a pass so Woodland was properly supported, and approved the result.
The tile is a different thing from `.toggle` (a setting inside a row) and from `.chip` (a
label or filter), so it has its own class.

Walnut for a lit light follows the Home Assistant theme mapping already in use: a lamp is a
warm thing, and moss is kept for everything else that is active. `01-color.md` says never to
use walnut for a status. A light being on is an entity's state, not a health status, and it
never appears with a status glyph, so the two don't collide.

Rejected: one colour for everything that is on (a lit lamp and a running fan looked the
same), and the other theme's capitals and monospace for the small labels.

## Affects
`css/woodland.css` (`.switch-tile`), `docs/04-components.md` (Switch tiles),
`docs/07-theming.md` (Home Assistant), `examples/preview.html` (Controls). No token values
changed.
