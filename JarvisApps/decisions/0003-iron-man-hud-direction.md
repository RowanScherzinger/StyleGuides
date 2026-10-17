# 0003. Iron Man HUD visual direction

Date: 2026-10-17
Status: accepted

## Decision
- Style: the Iron Man / Avengers HUD (Territory Studio, Jayse Hansen). Futuristic and kinetic.
- Density: packed but clean. Lines, shapes and icons for information you can read at a glance.
- Shape: sharp or slightly rounded corners. Frosted glass and transparency.
- Colour: warm, metallic, dark. Red, gold, copper, silver, black, off-white.
- Type: monospace (the user's terminal uses Cascadia Mono with the Campbell scheme), plus an easy-to-read sans.

## Why
User decision, with reference links in `docs/00-principles.md`. Desktop-Widgets already
looked like this, so its values became the starting tokens.

## Affects
All of `tokens/tokens.css`, `css/hud.css`, and `docs/`.
