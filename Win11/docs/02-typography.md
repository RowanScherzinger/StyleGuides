# Typography (decisions/0005)

## Typefaces

| Token | Face | Use |
|---|---|---|
| `--font-sans` | Segoe UI Variable Text | Everything by default (14px and up) |
| `--font-small` | Segoe UI Variable Small | Captions and anything under 14px |
| `--font-display` | Segoe UI Variable Display | Subtitle and larger |
| `--font-mono` | Cascadia Mono | Paths, IDs, code |
| `--font-icons` | Segoe Fluent Icons | Icons (`06-iconography.md`) |

All ship with Windows 11. The fallback is Segoe UI, so Windows 10 still looks right. The
three Variable faces are optical sizes of one family: use the one meant for the size.

## Type ramp

The Windows ramp. Don't add sizes between steps.

| Style | Size / line height | Weight | Class | Use |
|---|---|---|---|---|
| Caption | 12 / 16 | Regular | `.text-caption` | Descriptions under a setting, timestamps, hints |
| Body | 14 / 20 | Regular | `.text-body` | The default for everything |
| Body strong | 14 / 20 | Semibold | `.text-body-strong` | Group headers, emphasis, InfoBar titles |
| Body large | 18 / 24 | Regular | `.text-body-large` | Lead paragraphs |
| Subtitle | 20 / 28 | Semibold | `.text-subtitle` | Dialog titles, card titles |
| Title | 28 / 36 | Semibold | `.text-title` | Page titles |
| Title large | 40 / 52 | Semibold | `.text-title-large` | Rare: a hero heading |
| Display | 68 / 92 | Semibold | `.text-display` | Rare: one big number |

The one exception is the 11px number in a badge (`.badge`), as WinUI's InfoBadge has it.

## Rules

- Sentence case everywhere: titles, buttons, labels, menu items. No all caps, no letter-spacing.
- Two weights only: regular and semibold. No light or bold.
- Numbers that line up in columns use `font-variant-numeric: tabular-nums`.
- Respect the user's text size (Settings > Accessibility > Text size): size in `rem`, never
  fix a container's height around text.
