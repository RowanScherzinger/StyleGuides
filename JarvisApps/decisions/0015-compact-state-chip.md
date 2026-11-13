# 0015. On/off controls are compact chips; brightness is the chip's fill

Date: 2026-11-13
Status: accepted (the chip, the state circle, the fill slider, hold for the secondary
action, read-only instead of an unused control); proposed (sizes, the corner flag, lock
colours)

## Decision
- **Accepted.** A dense dashboard's on/off control is a one-row chip: icon in a small
  circle, then the name, no state text. The circle carries the state so it reads at a glance.
- **Accepted.** For a dimmable light the chip's background is the level: it fills left to
  right, and dragging left-right sets it. Tap still toggles.
- **Accepted.** A second, rarer action on the same thing (a lock that stops automation from
  changing it) is a long-press on the chip, not a tile of its own.
- **Accepted.** A setting the user never changes, or that another system sets, is shown as a
  read-only value, not as a control.
- **Proposed.** The sizes: chip one grid row tall, 28px circle (the button height), name in
  `--text-md`. A small uppercase flag in the top-right corner, in `--color-status-warning`,
  shows while the long-press state is on. The level shows bottom-right in `--text-2xs`.
- **Proposed.** A lock's circle is `--color-status-ok` when secured and
  `--color-status-danger` when not. This uses red for something that isn't a fault, which
  bends 0004. It was carried over from the lock tile it replaced. Confirm or change it.

## Why
User decisions, made on the Home Assistant dashboards. The two-row tiles took too much room
for controls that are tapped a few times a day, so they were halved in height. Dropping the
state text made the state hard to see, so the user asked for the circle under the icon "like
in the bigger buttons". Brightness then had no home, so the user asked for the chip
background to be the slider, with hold kept for locking. Separately, the user asked for
controls that are never used, or that the energy supplier sets, to become read-only status.

Rejected: a half-width one-row tile (still too wide, three would not fit across), state as
text colour only (too subtle), a separate slider row per light (the height came straight
back), and a separate lock tile beside each light (one more thing to scan past).

## Affects
`docs/04-components.md` (Chips), `docs/07-theming.md` (Home Assistant), `examples/preview.html`
(Controls panel). No token values changed.
