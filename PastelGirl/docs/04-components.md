# Components *(Proposed, decisions/0005)*

Classes live in `css/soft.css`.

## Shape

| Element | Radius |
|---|---|
| Checkbox, small chip inside a card | `--radius-sm` 8px |
| Input, row, tooltip | `--radius-md` 14px |
| Card | `--radius-lg` 20px |
| Modal, hero card | `--radius-xl` 28px |
| Button, chip, toggle, avatar, progress bar | `--radius-full` |

Nested corners: inner radius = outer radius minus padding, so they stay concentric.

## Cards

`.card`: frosted plum glass, a faint pink hairline, a soft lift and a top sheen.
`.card--interactive` lifts 2px on hover. `.is-active` adds the pink glow ring.

## Buttons

All pill-shaped, bold text, a small bounce on press (`scale(0.96)`).

| Class | Use |
|---|---|
| `.btn--primary` | One per view. Pink fill, dark plum text. |
| `.btn--soft` | Secondary actions. Pink tint, pink text. |
| `.btn--ghost` | Tertiary actions. Pink outline. |
| `.btn--danger` | Destructive. Cherry tint and outline. Always says what it destroys. |

## Inputs

Sunken well (`--color-surface-sunken`), `--radius-md`, a pink hairline on focus plus the
focus ring. Labels sit above, in muted text.

## Toggles

Pill track, silver knob (the hardware detail). On: pink track, the knob bounces across
(`--ease-bounce`).

## Chips

`.chip` pink tint, `.chip--lilac` secondary, `.chip--solid` for the selected filter.

## Dividers

Use spacing first, `--color-divider` hairlines second, and the silver `.chain` once or
twice per screen as the hard accent.

## Modals and toasts

Modals: `.card--raised`, `--radius-xl`, centred, the field dimmed to 60%.
Toasts: pill-ish (`--radius-lg`), bottom centre, status glyph on the left.

## Loading

A row of three soft dots pulsing in turn, or a twinkling sparkle. No spinners with hard edges.

## Empty states

A small motif (moon, sparkle, heart outline), a friendly line and one action.
