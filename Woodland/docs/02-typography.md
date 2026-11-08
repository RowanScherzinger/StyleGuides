# Typography *(Proposed, decisions/0004)*

## Typefaces

| Token | Face | Use |
|---|---|---|
| `--font-display` | Fraunces, soft axis 100 | Page and card titles, big numbers |
| `--font-sans` | Nunito Sans | Everything else |
| `--font-mono` | Cascadia Mono | Timestamps, IDs, code |

Always pair `--font-display` with `font-variation-settings: var(--font-display-settings)`;
without it Fraunces' serifs are sharp. Fallbacks (Georgia, Segoe UI) keep things readable
offline. Load Fraunces and Nunito Sans from Google Fonts, or self-host them in the app.

## Scale

`--text-xs` 12px to `--text-4xl` 48px. Body is 15px (`--text-md`) with 1.6 line height.

## Rules

- Sentence case everywhere. Eyebrows (`.wood-eyebrow`) are small, bold, moss and lightly tracked.
- Titles: Fraunces semibold, slightly tight tracking.
- Numbers: Fraunces with tabular lining figures. Units in Nunito Sans, small and muted.
- Weights: 400 body, 600 titles, 700 buttons and eyebrows.
- No italics for emphasis in UI; use weight.
