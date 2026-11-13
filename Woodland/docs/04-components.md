# Components *(Proposed, decisions/0005)*

Classes live in `css/woodland.css`.

## Shape

| Element | Radius |
|---|---|
| Checkbox, small chip inside a card | `--radius-sm` 6px |
| Button, input, row, tooltip | `--radius-md` 12px |
| Card | `--radius-lg` 18px |
| Modal | `--radius-xl` 26px |
| Hero card (one per screen) | `--radius-pebble`, an uneven river stone |
| Chip, toggle, avatar, progress bar | `--radius-full` |

Nested corners: inner radius = outer radius minus padding.

## Cards

`.card`: linen in light, moss glass in dark, a faint moss hairline, a soft warm shadow and a
top sheen. `.card--interactive` lifts 2px on hover. `.is-active` adds the moss ring.
`.card--pebble` gives the hero card its stone outline.

## Buttons

Bold text, 12px corners, press down 1px.

| Class | Use |
|---|---|
| `.btn--primary` | One per view. Moss fill, `--color-on-accent` text. |
| `.btn--soft` | Secondary actions. Moss tint, moss text. |
| `.btn--ghost` | Tertiary actions. Moss outline. |
| `.btn--danger` | Destructive. Rowan tint and outline. Always says what it destroys. |

## Inputs

Sunken well (`--color-surface-sunken`), `--radius-md`, a stronger moss hairline on focus plus
the focus ring. Labels sit above, in muted text.

## Toggles

`.toggle` with `role="switch"` and `aria-checked`. Pill track; off, the knob is bark (pine-300
in dark); on, the track is moss and the knob takes `--color-on-accent`.

## Chips

`.chip` moss tint, `.chip--walnut` secondary, `.chip--solid` for the selected filter.

## Switch tiles

For on/off things on a dense dashboard (decisions/0009). Not a `.toggle` (a setting inside
a row) and not a `.chip` (a label or filter).

```html
<button class="switch-tile switch-tile--light is-on" style="--level: 60%">
  <span class="switch-tile__icon">…</span><span class="switch-tile__name">Desk lamp</span>
  <span class="switch-tile__flag">Locked</span><span class="switch-tile__level">60%</span>
</button>
```

- One row tall. Icon in a 28px circle, then the name. No state text: the circle is the state.
- On is moss (`--color-accent-text`). A light that is on is walnut
  (`--color-secondary-text`), like a lantern. Off is `--color-status-idle`.
- Tap toggles. Long-press is for one rarer action on the same thing, such as a lock. While
  that state is on, a small sentence-case flag shows top-right in `--color-status-warning`
  *(Proposed)*.
- A dimmable light fills left to right to its level in `--color-secondary-soft`, with the
  level bottom-right. Dragging left-right sets it. A vertical drag still scrolls.
- A setting nobody changes, or that another system sets, is a read-only value, not a tile.
- How a lock's circle is coloured is not decided. See decisions/0009.

## Dividers

Spacing first, `--color-divider` hairlines second. `.wood-twig` (a hairline with a small leaf
in the middle) at most once per card.

## Modals and toasts

Modals: `.card--raised`, centred, the field dimmed to 60%. Toasts: `--radius-lg`, bottom
centre, status glyph on the left.

## Loading

A leaf swaying (`.wood-sway`) or three dots breathing in turn. No spinning rings.

## Empty states

A small motif (mushroom, acorn, sprouting fern), one calm line and one action.
