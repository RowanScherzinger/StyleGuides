# Woodland Style Guide

Soft, earthy and natural. Moss greens on oat paper, bark-brown ink, and a quiet woodland
cast of leaves, ferns, pines, mushrooms, acorns and pinecones. Light by default, like a
sunlit clearing, with a dark variant for the forest at night.

Open `examples/preview.html` in a browser to see it. The button at the top switches day and night.

## Who uses it

TBD. No app has adopted it yet.

## Layout

```
README.md          you are here
CLAUDE.md          rules for an agent editing or applying this guide
tokens/
  tokens.css       every value: colour, type, space, shape, shadow, motion
css/
  woodland.css     shared classes, icons and keyframes: .card, .btn, .chip, .motif, .glyph...
examples/
  preview.html     a live sample of the tokens and components
tools/
  contrast.py      WCAG contrast check for both variants, plus hue separation of the status colours
docs/
  00-principles.md       the feel, do/don't
  01-color.md            palette, roles, status, measured contrast
  02-typography.md       typefaces, scale, rules
  03-spacing-layout.md   4px scale, density, composition, breakpoints
  04-components.md       shapes, cards, buttons, inputs, toggles, chips, modals
  05-motion.md           tokens, signature motions, budget
  06-iconography.md      forest motifs, status glyphs, icon set
  07-theming.md          light default, dark variant, the field, grain, glass
  08-accessibility.md    contrast, focus, motion, colour blindness
  09-voice-and-copy.md   tone and wording
  10-data-viz.md         series order, rings, bars, lines
decisions/
  NNNN-*.md        one file per decision, with the reason (accepted / proposed)
```

## How to use it from another project

Add this to the consuming project's `CLAUDE.md`:

```markdown
## Visual style
Follow the style guide at `<path to StyleGuides clone>/Woodland` (read its CLAUDE.md first).
Copy `tokens/tokens.css` and `css/woodland.css` into the app; never hardcode a colour, size or duration.
```

## Status

Decided by the user: the direction (0002). Everything else is **proposed**: decisions 0001
and 0003 to 0008, and every *(Proposed)* label in `docs/`.
