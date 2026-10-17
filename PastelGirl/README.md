# Pastel Girl Style Guide

A very cute, softer, rounder pastel look that's feminine. Lots of pinks and creams: by
default glowing on a plum-black field, with a light variant on blush cream. Frosted round
cards, pill buttons, hearts, moons and sparkles, and bouncy little motions.

Open `examples/preview.html` in a browser to see it. The button at the top switches dark and light.

## Who uses it

TBD. Planned: iPhone Explorer will offer it as an optional theme.

## Layout

```
README.md          you are here
CLAUDE.md          rules for an agent editing or applying this guide
tokens/
  tokens.css       every value: colour, type, space, shape, shadow, motion
css/
  soft.css         shared classes and keyframes: .card, .btn, .chip, .chain, .sparkle...
examples/
  preview.html     a live sample of the tokens and components
tools/
  contrast.py      WCAG contrast check for both variants, plus accent vs danger separation
docs/
  00-principles.md       the feel, do/don't, lessons from the references
  01-color.md            palette, roles, status, measured contrast
  02-typography.md       typefaces, scale, rules
  03-spacing-layout.md   4px scale, density, composition, breakpoints
  04-components.md       shapes, cards, buttons, inputs, toggles, chips, modals
  05-motion.md           tokens, signature motions, budget
  06-iconography.md      icon set and motifs
  07-theming.md          dark default, light variant, the field, glass
  08-accessibility.md    contrast, focus, motion
  09-voice-and-copy.md   tone and wording
  10-data-viz.md         series order, rings, bars, lines
decisions/
  NNNN-*.md        one file per decision, with the reason (accepted / proposed)
```

## How to use it from another project

Add this to the consuming project's `CLAUDE.md`:

```markdown
## Visual style
Follow the style guide at `<path to StyleGuides clone>/PastelGirl` (read its CLAUDE.md first).
Copy `tokens/tokens.css` and `css/soft.css` into the app; never hardcode a colour, size or duration.
```

## Status

Decided by the user: the direction (0002), the typefaces (0004), a light variant (0008) and
"very cute" (0009). Everything else is **proposed**: decisions 0001, 0005, 0006 and 0010,
and every *(Proposed)* label in `docs/`.
