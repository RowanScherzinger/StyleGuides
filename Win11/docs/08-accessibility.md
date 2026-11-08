# Accessibility

- **Contrast**: text passes WCAG AA (4.5:1) in both modes, measured by `tools/contrast.py` and
  tabled in `01-color.md`. The exception is tertiary text in light mode (3.3:1): placeholders
  and hints only.
- **Focus**: every focusable thing shows the two-ring focus visual on keyboard focus
  (`:focus-visible`): 2px outer ring in `--color-focus-outer`, 1px inner in
  `--color-focus-inner`. Never remove it without a replacement.
- **Colour is never the only signal**: status always has a glyph and words; selection has the
  edge pill as well as the fill.
- **Contrast themes**: support `forced-colors` (`07-theming.md`).
- **Text size**: sizes in `rem`, layouts that grow with text (Windows' text size setting goes to 225%).
- **Motion**: honour reduced motion (`05-motion.md`).
- **Targets**: at least 32px high for mouse, 40px for touch.
- **Keyboard**: everything reachable with Tab and arrows; Esc closes flyouts and dialogs;
  Enter activates the default button.
