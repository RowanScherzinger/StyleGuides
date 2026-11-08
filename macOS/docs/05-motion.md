# Motion

Purposeful and brief (HIG > Motion). Motion gives feedback and shows where things came from.
Avoid it on things that happen often, and never make people wait for it.

## Tokens

| Token | Value | Use | Source |
|---|---|---|---|
| `--duration-fast` | 150ms | Hover, press, colour | *(Proposed)* |
| `--duration-normal` | 250ms | Switches, menus, alerts | Core Animation's default duration |
| `--duration-slow` | 500ms | Sheets, larger moves | SwiftUI's `.smooth` default duration |
| `--ease-default` | `cubic-bezier(0.25, 0.1, 0.25, 1)` | Most motion | `CAMediaTimingFunction` default |
| `--ease-in-out` | `cubic-bezier(0.42, 0, 0.58, 1)` | Things moving from one place to another | `easeInEaseOut` |
| `--ease-out` | `cubic-bezier(0, 0, 0.58, 1)` | Entrances | `easeOut` |
| `--ease-in` | `cubic-bezier(0.42, 0, 1, 1)` | Exits | `easeIn` |
| `--ease-spring` | `cubic-bezier(0.2, 0.9, 0.25, 1)` | Knobs, alerts appearing | *(Proposed)* a no-bounce spring, approximated |

Native apps use the system's own animations and springs, not these tokens.

## Patterns

- **Hover and press**: colour only. Nothing scales or jumps.
- **Menus**: appear at once or fade in quickly. They don't slide. They fade out on close.
- **Alerts**: fade in and settle from a little larger (1.08 to 1).
- **Sheets**: slide in from the top edge of the window's content area, about `--duration-slow`.
- **Switches**: the knob slides with `--ease-spring`, the track colour fades.
- **Exits** are faster than entrances, or instant.

## Budget

- Nothing loops except progress indicators.
- Never animate layout that shifts what the user is reading.
- Reduce Motion (System Settings > Accessibility > Display; `prefers-reduced-motion` on the
  web): durations go to 0 and loops stop. `tokens.css` handles it. Replace any slide with a fade.
