# Motion *(Proposed)*

Slow and gentle, like wind in leaves. Nothing bounces or overshoots.

## Tokens

| Token | Value | Use |
|---|---|---|
| `--duration-instant` | 100ms | Colour changes |
| `--duration-fast` | 180ms | Presses, hovers |
| `--duration-normal` | 300ms | Cards, toggles |
| `--duration-slow` | 520ms | Entrances, modals |
| `--ease-natural` | settles like a leaf landing | Most motion |
| `--ease-sway` | symmetric in-out | Ambient loops |
| `--ease-exit` | accelerate out | Leaving |

## Signature motions

- **Grow in** (`.wood-enter`): rise 6px and fade in, staggered by `--stagger` via `--i`.
- **Sway** (`.wood-sway`): a motif rocks ±3° from its base over 5 seconds.
- **Rustle** (`.wood-rustle`): an icon or motif shakes once on hover.
- **Breathe** (`.wood-breathe`): the pending glyph fades in and out.
- **Firefly** (`.wood-glow`): a small lichen dot glows. Dark variant decoration only.

## Budget

- At most three ambient loops visible at once. Rustle runs once and doesn't count.
- Big things (cards, modals) only fade and rise; they never sway.
- Reduced motion: tokens go to 0ms and loops stop (handled in `tokens.css`).
