# Accessibility *(Proposed)*

- Text meets WCAG AA 4.5:1 in both variants (see `01-color.md`). Run `tools/contrast.py` after any colour change.
- Text on any pastel fill is dark plum (`--color-on-accent`).
- Status always has a glyph and words, not just colour. OK and error are both hearts, so the
  words matter: never show a status heart without its label.
- Focus: a 2px light-pink ring with a 3px offset on every interactive element. Never remove it.
- Hit targets are at least 40px tall. Pills make this easy.
- Decorative motifs are `aria-hidden`.
- Reduced motion turns off bounce and loops (handled in `tokens.css`).
