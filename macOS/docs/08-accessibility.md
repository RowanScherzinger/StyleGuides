# Accessibility

- **Contrast**: HIG > Accessibility asks for 4.5:1 for text up to 17pt, and 3:1 for 18pt and
  up or bold. Measured by `tools/contrast.py` and tabled in `01-color.md`. The known gaps are
  Apple's own: secondary text and coloured text on the light window, and white on the accent.
  Increase Contrast closes most of them.
- **Increase Contrast**: support `prefers-contrast: more` (`07-theming.md`).
- **Focus**: every focusable thing shows the accent focus ring on keyboard focus
  (`:focus-visible`), 3px, following the control's shape. Text and search fields use the ring;
  lists show focus through the accent selection instead (HIG > Focus and selection). Never
  remove it without a replacement.
- **Colour is never the only signal**: status always has a glyph and words; selection has a
  fill as well as colour.
- **Text size**: body 13px, never under 10px. Sizes in `rem`, layouts that grow with text, up to 200%.
- **Targets**: 28×28px by default, never under 20×20px (HIG > Accessibility).
- **Motion and transparency**: honour Reduce Motion and Reduce Transparency (`05-motion.md`, `07-theming.md`).
- **Keyboard**: Tab moves between controls (all controls when Keyboard Navigation is on);
  Return presses the default button; Esc and ⌘. cancel; every toolbar command has a menu item
  and, where it's common, a shortcut.
- **VoiceOver**: every icon-only control has an accessible name.
