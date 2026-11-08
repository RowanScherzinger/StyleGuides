# Accessibility *(Proposed)*

- Text meets WCAG AA 4.5:1 in both variants where it's used (see `01-color.md`). Run
  `tools/contrast.py` after any colour change.
- Text on the moss fill is `--color-on-accent`, which flips with the variant.
- **Colour blindness.** Moss, fern and rowan are a red-green trap. Every status has its own
  glyph shape and words; check new states in greyscale.
- Never show a green status without its sprout glyph and label.
- Focus: a 2px moss ring with a 3px offset on every interactive element. Never remove it.
- Hit targets are at least 40px tall.
- Motifs and glyphs are `aria-hidden`; words carry the meaning.
- Reduced motion stops sway, breathe and glow (handled in `tokens.css`).
