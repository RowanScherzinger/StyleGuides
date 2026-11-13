# Components

Tokens: `--radius-*`, `--chamfer-*`, `--line-*`, `--glow-*`, plus colour and spacing.
Ready-made classes are in `css/hud.css`. A live sample is in `examples/preview.html`.

## Shape

- Corners are sharp or slightly rounded: `--radius-sm` (2px) for small controls,
  `--radius-md` (4px) for panels and buttons, and `--radius-lg` (6px) as the ceiling.
- `.chamfer` clips two corners for a machined look. Use it for one hero element per screen
  at most. `clip-path` also clips borders, glows and children, so put `.chamfer` on an
  inner element and keep any brackets on the unclipped wrapper around it.
- Circles (`--radius-full`) only for rings, gauges, dots and avatars.

## Depth

Glass and glow, not shadow:

- Panels: `.glass`, which is a translucent warm-black tint, 12px backdrop blur and a 1px copper hairline.
- Hover or active: the tint darkens, the border strengthens, and `--glow-md` appears.
- Floating layers (menus, modals) add `--shadow-float`. It's the only drop shadow allowed.

## Required states

Every interactive component defines: default, hover, active, focus-visible (gold
outline), disabled (40% opacity, no glow), plus loading and error where relevant.

## Panel

```html
<section class="glass">
  <span class="hud-corner hud-corner--tl"></span><span class="hud-corner hud-corner--tr"></span>
  <span class="hud-corner hud-corner--bl"></span><span class="hud-corner hud-corner--br"></span>
  <div class="hud-label">GPU Load</div>
  <div class="hud-value">72<span class="hud-unit">%</span></div>
</section>
```

Brackets sit at 45% opacity and lock on (scale in, full opacity) on hover.

## Buttons

| Variant | Look |
|---|---|
| Primary | Solid copper, black text, `--font-display` uppercase. One per view. |
| Secondary | `--color-accent-soft` fill, copper hairline, copper text |
| Ghost | No fill, `--color-divider` border, muted text, becomes copper on hover |
| Danger | `--color-danger-fill`, `--color-danger-border`, `--color-danger-text` |

All buttons use `--radius-sm` or `--radius-md`, and are 28px tall (32px for primary).
Desktop-Widgets' current 6–10px button radii should come down to these.

## Inputs

Mono text, `rgba(255,255,255,0.04)` fill, copper hairline that strengthens on focus,
gold focus ring. Toggles are rectangular tracks with a square thumb, not pills *(Proposed)*.
Selects are the same input, 24px tall, with the value in gold tabular mono and a small copper
chevron on the right. Their label sits beside them in the toggle's label style *(Proposed)*.

## Chips (compact on/off controls)

Use a chip for anything that is on or off on a dense dashboard (decisions/0015).

```html
<button class="chip is-on" style="--level: 60%">
  <span class="chip-ico">◉</span><span class="chip-name">Desk</span>
  <span class="chip-flag">Locked</span><span class="chip-level">60%</span>
</button>
```

- One row tall. Icon in a 28px circle, then the name in `--text-md`. No state text.
- The circle is the state: `--color-highlight` icon on a 24% highlight fill when on,
  `--color-text-muted` on a 12% fill when off, `--color-text-dim` when unavailable.
- Tap toggles. Long-press is for one rarer action on the same thing, such as a lock.
  While that state is on, show a `--text-2xs` uppercase flag top-right in
  `--color-status-warning` *(Proposed)*.
- A dimmable light fills its background left to right to the level, in a 20% highlight
  tint, with the level bottom-right in `--text-2xs`. Dragging left-right sets the level and
  sends it on release. A vertical drag still scrolls the page.
- If a tap would be costly (a plug feeding a computer), make tap open the detail view.
- Never make a chip for a setting the user doesn't change or another system sets. Show it
  as a read-only readout.
- Three chips fit across a narrow column when names stay under about ten characters.
- A lock's circle is `--color-status-ok` when secured and `--color-status-danger` when not
  *(Proposed, see decisions/0015: this bends the red-is-danger rule)*.

## Readouts and stat tiles

Label (`.hud-label`), value (`.hud-value`, gold, light mono), unit (`.hud-unit`), and
optionally a sparkline or delta beneath it. See `10-data-viz.md`.

## Status indicator

A shape and an uppercase label, using the state table in `01-color.md`. For example `◆ RUNNING`.

## Tables and lists

No zebra stripes. Rows are separated by `--color-divider` hairlines, and the hovered row
gets `--color-accent-soft`. Headers are `.hud-label`. Numbers are right-aligned and tabular.

## Modals

`--color-surface-raised` glass, `--shadow-float`, brackets always visible, boot-in
animation. The backdrop is `rgba(6,4,4,0.6)` with blur.

## Toasts

Top-right stack. A glass panel with a 2px left edge in the status colour. They auto-dismiss
after 5s, except errors, which stay until dismissed.

## Loading

A thin indeterminate scan bar, or a rotating arc segment for small spaces. Skeletons are
hairline outlines of the final layout, not grey blocks. No generic spinners.
