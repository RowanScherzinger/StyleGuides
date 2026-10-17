# Motion *(Proposed)*

Soft and bouncy, never twitchy. Very cute (decisions/0009) means things react: they pop,
boop and wiggle.

## Tokens

| Token | Value | Use |
|---|---|---|
| `--duration-instant` | 90ms | Colour changes |
| `--duration-fast` | 160ms | Presses, hovers |
| `--duration-normal` | 260ms | Cards, toggles |
| `--duration-slow` | 450ms | Entrances, modals |
| `--ease-soft` | gentle settle | Most motion |
| `--ease-bounce` | small overshoot | Presses, pops, toggle knobs, chips appearing |
| `--ease-exit` | accelerate out | Leaving |

## Signature motions

- **Pop in** (`.soft-enter`): rise 8px and scale from 0.97 with a small overshoot,
  staggered by `--stagger` via `--i`.
- **Press**: buttons squish to 0.96.
- **Twinkle** (`.soft-twinkle`): sparkles breathe and rotate slightly. The pending moon uses the slower `.soft-pulse`.
- **Float** (`.soft-float`): a decorative motif drifts 6px.
- **Wiggle** (`.soft-wiggle`): icons and motifs wiggle on hover.
- **Boop** (`.soft-boop`): a happy scale pop when a heart is tapped or something succeeds.

## Budget

- At most three ambient loops visible at once. Reactions (wiggle, boop) don't count: they run once.
- Bounce only on small things (under about 120px). Big cards settle with `--ease-soft`.
- Reduced motion: tokens go to 0ms, the bounce becomes the soft ease, loops stop
  (handled in `tokens.css`).
