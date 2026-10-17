# 0003. Dark only

Date: 2026-10-17
Status: superseded by 0008

## Decision
No light theme. `color-scheme: dark`, no `prefers-color-scheme` branch.

## Why
The brief says "dark" (0002), and the user's other guide is dark only. A light variant would
turn this into a generic pastel look; the dark field is what makes the pastels glow.
Not confirmed: the user said dark, not explicitly "never light".

## Affects
`tokens/tokens.css`, `docs/07-theming.md`.
