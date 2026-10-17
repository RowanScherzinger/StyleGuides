# 0004. Colour roles: copper frames, gold signals, red alarms

Date: 2026-10-17
Status: proposed. The "no green, blue or cyan" and "OK is gold" parts are superseded by 0007.

## Decision
- Copper is the accent: hairlines, brackets, headings, primary buttons.
- Gold is the signal: live values, the running state, focus.
- Silver is neutral data and idle state.
- Red is only for danger and critical states.
- Warning uses a new ember orange (`#f07a2a`). There is no green, blue or cyan anywhere,
  including "OK" status, which is gold.
- Status always pairs colour with a shape (◆ ◇ □ ▲ ■).

## Why
- The user listed red first, but red as the accent would make alarms blend in with ordinary
  emphasis. Keeping red for danger means a failure stands out instantly.
- Copper and gold are already the accent and highlight in Desktop-Widgets.
- Green for "OK" would break the warm palette. Gold reads as nominal and keeps the heat.
- Warning had to differ from both copper and red, so ember sits between them, brighter than both.

Rejected: red as the accent (it collides with danger), and a cyan/blue HUD (cool, and
not what the user asked for).

## Affects
`tokens/tokens.css` semantic colours, `docs/01-color.md`, `docs/10-data-viz.md`.
