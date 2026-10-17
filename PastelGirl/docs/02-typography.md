# Typography *(Proposed, decisions/0004)*

## Typefaces

| Token | Face | Use |
|---|---|---|
| `--font-sans` | Nunito | Everything by default. Rounded terminals, friendly, very readable. |
| `--font-display` | Fredoka | Page and card titles, big numbers. Round and bubbly. |
| `--font-mono` | Cascadia Mono | Timestamps, IDs, code. The one crisp, "cool" face. |

Fallbacks are Segoe UI Variable so nothing breaks offline. Load Nunito and Fredoka from
Google Fonts, or self-host them in the app.

## Scale

`--text-xs` 12px to `--text-4xl` 48px. Body is 15px (`--text-md`): this look is roomier
than a dense dashboard.

## Rules

- Sentence case everywhere. No all-caps labels. Eyebrows (`.soft-eyebrow`) are small,
  bold, pink, lightly tracked, and still sentence case.
- Titles: Fredoka semibold, slightly tight tracking.
- Numbers: Fredoka with `tabular-nums`, in cream. Units small and muted.
- Weights: 400 body, 600 titles, 700 buttons and eyebrows. No light weights on dark: they shimmer.
- Line height 1.55 for body text.
