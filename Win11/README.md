# Win11 Style Guide

The default Windows 11 app look (Fluent): Segoe UI Variable, neutral greys, the user's accent
colour, 4px controls and 8px cards on a layered window, plain words. Light or dark to match
Windows, following changes live.

The values aren't invented: they're mirrored from WinUI, Microsoft's own control library, with
the source resource named beside each one.

Open `examples/preview.html` in a browser to see it. It follows your system mode; the buttons
at the top force light or dark and try other accent colours.

## Who uses it

Phone Explorer: its default "Windows" theme is this guide, mirrored by hand for WinForms.

## Layout

```
README.md          you are here
CLAUDE.md          rules for an agent editing or applying this guide
tokens/
  tokens.css       every value: colour (light and dark), type, space, shape, elevation, motion
css/
  fluent.css       shared classes: .card, .btn, .input, .toggle, .list-item, .infobar, .flyout, .dialog...
examples/
  preview.html     a live sample of the tokens and components
tools/
  contrast.py      WCAG contrast check for both modes, for the default or any accent palette
docs/
  00-principles.md       the feel, do/don't, references
  01-color.md            accent palette, roles, status, measured contrast
  02-typography.md       typefaces, the Windows type ramp, rules
  03-spacing-layout.md   4px grid, sizes, the window/layer/card frame, breakpoints
  04-components.md       shapes, cards, buttons, inputs, toggles, lists, InfoBar, dialogs
  05-motion.md           durations, curves, patterns
  06-iconography.md      Segoe Fluent Icons, status glyphs
  07-theming.md          light/dark, the system accent, native apps, materials, contrast themes
  08-accessibility.md    contrast, focus, text size, motion
  09-voice-and-copy.md   tone and wording
  10-data-viz.md         series, bars, lines
decisions/
  NNNN-*.md        one file per decision, with the reason (accepted / proposed)
```

## How to use it from another project

Add this to the consuming project's `CLAUDE.md`:

```markdown
## Visual style
Follow the style guide at `<path to StyleGuides clone>/Win11` (read its CLAUDE.md first).
Copy `tokens/tokens.css` and `css/fluent.css` into the app; never hardcode a colour, size or duration.
```

## Status

Decided by the user: the default Windows 11 look (0002) and following the system's light or
dark mode (0003). The values come from WinUI (0001). Everything else is **proposed**:
decisions 0001 and 0004 to 0008, and every *(Proposed)* label in `docs/`.
