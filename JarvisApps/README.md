# Jarvis Apps Style Guide

How my apps should look and feel. This repo holds no application code. It is the
reference that every personal app reads before it makes a visual decision.

**The look:** an Iron Man style HUD. Dark only, warm metallic colours (copper, gold,
silver, red on warm black), sharp corners, frosted glass, monospace readouts, and motion
with a purpose. Packed but clean.

Open `examples/preview.html` in a browser to see it.

## Who uses it

| App | Stack | Notes |
|---|---|---|
| Jarvis | Bun, Express, HTML | Home-lab service dashboard |
| Larder | React + Vite | Grocery / recipes / meal planner |
| Desktop-Widgets | Electron, React | Transparent desktop overlay. The reference implementation of this look. |
| Plox | Vanilla JS | Media viewer |

## Layout

```
README.md          you are here
CLAUDE.md          rules for an agent applying this guide inside another project
tokens/
  tokens.css       every value: colour, type, space, shape, glow, motion
css/
  hud.css          shared keyframes and classes: .glass, .hud-corner, .hud-label, .hud-value...
examples/
  preview.html     a live sample of the tokens and components
tools/
  contrast.py      WCAG contrast check, including glass over a white wallpaper
docs/
  00-principles.md       the feel, do/don't, lessons from the references
  01-color.md            palette, roles, status, measured contrast
  02-typography.md       typefaces, scale, readout rules
  03-spacing-layout.md   4px scale, density, composition, breakpoints
  04-components.md       panels, buttons, inputs, tables, modals, toasts, loading
  05-motion.md           tokens, signature motions, animation budget
  06-iconography.md      icon set and HUD glyphs
  07-theming.md          dark only, glass in apps vs over the desktop
  08-accessibility.md    contrast, focus, keyboard, reduced motion
  09-voice-and-copy.md   labels, buttons, numbers, messages
  10-data-viz.md         readouts, ring gauges, segmented bars, sparklines
decisions/
  NNNN-*.md        one file per decision, with the reason (accepted / proposed)
```

## How to use it from another project

Add this to the consuming project's `CLAUDE.md`:

```markdown
## Visual style
Follow the style guide at `<path to StyleGuides clone>/JarvisApps` (read its CLAUDE.md first).
Copy `tokens/tokens.css` and `css/hud.css` into the app; never hardcode a colour, size or duration.
```

Copy both CSS files into the app, and re-copy them when the guide changes.

## Status

The direction is decided (decisions 0002, 0003 and 0007). Everything more specific in `docs/`
is **proposed** and waiting for confirmation: decisions 0004–0006, the *(Proposed)* labels,
and the component, layout and data-viz details. Remaining open questions are listed at the
end of each doc.
