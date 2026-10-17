# Accessibility

Baseline rules. The HUD look doesn't override them. The measured contrast values are in `01-color.md`.

## Rules

- Body text contrast is at least 4.5:1 against its background, measured on the glass
  composited over the worst backdrop. Large text, icons and UI lines need 3:1 (WCAG AA).
- Every interactive element has a visible `:focus-visible` style: a 1.5px gold outline
  with 2px offset (set globally in `css/hud.css`). Never remove it without a replacement.
- Colour is never the only signal. Status always has a shape and a label (`01-color.md`).
- Everything works with the keyboard alone.
- Motion respects `prefers-reduced-motion`. This is handled globally in `tokens.css`.
- No text smaller than 10px. Text under 12px is for labels, units and captions only.
- Click targets are at least 24x24px. Apps used by touch (see the open question in
  `03-spacing-layout.md`) need 44x44px.
- Flicker effects stay under 3 flashes per second (the boot flicker is a single 600ms sequence).
