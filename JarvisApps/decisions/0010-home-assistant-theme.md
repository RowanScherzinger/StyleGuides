# 0010. Home Assistant follows the guide through a generated theme

Date: 2026-10-19
Status: accepted (Home Assistant as a consumer; gold for active state). The mappings listed
under "Proposed mappings" are proposed.

## Decision
- Home Assistant is a consumer of this guide.
- In HA, an entity's active state ("light on" and the like) is gold, because it's a live value.
  Chartreuse stays the small OK / running status light only (0007).
- HA can't load `tokens.css` as an app stylesheet, so a build script copies every token into an
  HA theme as theme variables, then maps HA's own variables onto the semantic tokens. The theme
  only has a dark mode (0002).

## Why
User decisions: add Home Assistant to the apps using the guide, and map "light on" (amber by
default in HA) to gold. Generating the theme from `tokens.css` keeps the tokens the single
source of truth (0001), the same way 0008 does for native apps.

Rejected: a hand-written theme with hex literals. It would drift from the tokens.

## Proposed mappings
- HA's named colours are remapped: amber → gold, orange → ember, deep orange → copper,
  red → crimson, green and lime → chartreuse, blue/cyan → arc blue, purple and pink → pale
  copper, indigo and greys → silver. This pulls built-in state colours into the warm range.
- Chart series 1–5 follow the categorical order in `10-data-viz.md`.
- card-mod adds `.glass` blur, corner brackets (45%, lock on hover) and `.hud-heading` card
  titles to every card. There's no boot flicker: card-mod re-mounts cards on every view switch,
  and boot animation is allowed on first load only (`05-motion.md`).
- button-card templates provide the readout, hero readout, status light (◆ ◇ ▬ ▲ ■ ●) and
  270° ring gauge. "Unavailable" shows the error square; "unknown" shows idle.

## Affects
`README.md` (apps table), `docs/07-theming.md` (Home Assistant section). No token values changed.
