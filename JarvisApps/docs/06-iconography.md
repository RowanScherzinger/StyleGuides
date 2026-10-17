# Iconography

Icons carry a lot of the glanceability, so they have to read instantly at small sizes.

## Icon set *(Proposed)*

| Property | Value |
|---|---|
| Library | [Lucide](https://lucide.dev): thin line style, React and vanilla packages, open licence |
| Stroke width | 1.5px (`--line-thin`) |
| Line ends | Square caps and miter joins (override Lucide's round defaults with CSS) for a machined look |
| Sizes | 12, 16, 20px. 16 is the default. |
| Colour | `currentColor`. Muted at rest, copper or gold when active. |

```css
.icon { stroke-width: var(--line-thin); stroke-linecap: square; stroke-linejoin: miter; }
```

## HUD glyphs

Beyond icons, the HUD look depends on a small set of geometric marks. Draw them as inline SVG:

| Glyph | Meaning |
|---|---|
| ◆ ◇ □ ▲ ■ | Status shapes (see `01-color.md`) |
| Corner brackets | Focus or targeting, panel frame |
| Tick ruler | A scale on gauges and chart edges |
| Arc / ring segment | A percentage, a gauge, loading |
| Chevrons » | Direction, expand, a trend |
| Crosshair | A selected point, the current position |

## Rules

- Filled icons only for status. Everything else is outline.
- Icon-only buttons need an `aria-label` and a tooltip.
- No emoji in the UI.

## App icons and favicons

Each app gets a monoline glyph inside a copper ring or chamfered square, on black.

## Open questions

- [ ] Happy with Lucide, or is there another icon set you prefer?
