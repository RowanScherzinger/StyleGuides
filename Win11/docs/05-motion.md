# Motion

Quick and quiet. Motion confirms what the user did and shows where things came from. It never
decorates.

## Tokens

| Token | Value | Use |
|---|---|---|
| `--duration-faster` | 83ms | Colour and opacity changes (hover, press) |
| `--duration-fast` | 167ms | Small moves, toggles' track |
| `--duration-normal` | 250ms | Flyouts and dialogs opening, toggle knobs, expanders |
| `--duration-slow` | 333ms | Page transitions |
| `--ease-decelerate` | `cubic-bezier(0, 0, 0, 1)` | Entrances and most motion ("fast out, slow in") |
| `--ease-accelerate` | `cubic-bezier(1, 0, 1, 1)` | Exits ("slow out, fast in") |
| `--ease-point` | `cubic-bezier(0.55, 0.55, 0, 1)` | Something moving from one place to another |

The three durations are WinUI's `ControlFaster/Fast/NormalAnimationDuration`. *(Proposed)*
`--duration-slow`.

## Patterns

- **Hover and press**: colour only, `--duration-faster`, linear. Nothing scales or jumps.
- **Flyouts and menus**: fade in and slide 8px from the side they open on, `--duration-normal`, decelerate.
- **Dialogs**: fade in and scale from 1.05 to 1.
- **Page change**: the new page rises a little (about 40px) and fades in; the old one just fades.
- **Exits** are faster than entrances, or instant.

## Budget

- Nothing loops except progress indicators.
- Never animate layout that shifts what the user is reading.
- Reduced motion (Windows: Settings > Accessibility > Visual effects > Animation effects off,
  `prefers-reduced-motion` on the web): durations go to 0 and loops stop. `tokens.css`
  handles it; native apps check the setting themselves (`07-theming.md`).
