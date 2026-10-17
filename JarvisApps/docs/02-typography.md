# Typography

Tokens: `--font-*`, `--text-*`, `--weight-*`, `--leading-*`, `--tracking-*`.

## Typefaces

| Use | Token | Family | Status |
|---|---|---|---|
| Data, values, UI text | `--font-mono` | **Cascadia Mono** (the Windows Terminal default, used with the Campbell scheme), falling back to DM Mono | Decided: monospace |
| Longer prose: descriptions, help, settings explanations | `--font-sans` | Inter, falling back to Segoe UI | *(Proposed)* |
| Uppercase labels and headings | `--font-display` | Orbitron, falling back to Bahnschrift | Taken from Desktop-Widgets |

Monospace is the default voice: tables, readouts, buttons and inputs. Switch to sans when
someone has to read a full sentence or more.

Self-host fonts as `woff2` inside each app. These apps run on a home LAN and shouldn't
depend on Google Fonts. Cascadia Mono and Bahnschrift ship with Windows. Other machines
(the Pi, a phone) need the files bundled.

Desktop-Widgets currently also uses Syne for settings headings. That's a fourth face, and
the guide drops it *(Proposed)*.

## Scale

Packed, so the steps are small at the bottom and big at the top, where readouts live.

| Token | Size | Used for |
|---|---|---|
| `--text-2xs` | 10px | Uppercase tracked labels only. Never sentences. |
| `--text-xs` | 11px | Units, captions, badges |
| `--text-sm` | 12px | Dense body text, table cells, inputs |
| `--text-md` | 13px | Default body |
| `--text-lg` | 15px | Panel titles |
| `--text-xl` | 18px | Page titles |
| `--text-2xl` | 24px | Section readouts |
| `--text-3xl` | 32px | Stat-tile values |
| `--text-4xl` | 44px | The one hero readout per screen |

## Rules

- Every changing number uses `font-variant-numeric: tabular-nums` (class `.tabular`, built
  into `.hud-value`) so digits don't jump around.
- Labels: `--font-display`, uppercase, `--tracking-label` (0.18em), `--color-text-muted`.
- Readout values: mono, `--weight-light`, gold. Units sit after them in `--text-xs` muted.
  Light weight at large sizes keeps the precise, instrument look.
- Nothing smaller than 10px. Orbitron at 10px is the floor, and only for short uppercase labels.
- Sentence case for prose and messages. UPPERCASE only for labels, headings and button text
  in `--font-display`.

## Open questions

- [ ] Is Inter right for prose, or should it all stay mono?
