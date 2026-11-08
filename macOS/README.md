# macOS Style Guide

The default macOS app look: SF Pro, neutral greys, the user's accent colour, rounded concentric
controls, a sidebar and unified toolbar, Liquid Glass for the control layer, and Mac wording
(title case, default button on the trailing end). Light or dark to match the Mac, following
Increase Contrast, Reduce Transparency and Reduce Motion.

It partners `Win11/`: same layout and the same semantic token names where the role matches,
so an app can offer both looks by swapping files.

Where Apple publishes a value it's Apple's, copied from the Human Interface Guidelines
(system colours in all four variants, the macOS text styles, minimum sizes, contrast targets).
Where Apple doesn't, the value is close to what AppKit draws and is labelled *(Proposed)*.

Open `examples/preview.html` in a browser to see it. It follows your system appearance; the
controls at the top force light or dark and try other accent colours.

## Who uses it

No app yet.

## Layout

```
README.md          you are here
CLAUDE.md          rules for an agent editing or applying this guide
tokens/
  tokens.css       every value: colour (light, dark, increased contrast), type, space, shape, elevation, motion
css/
  macos.css        shared classes: .btn, .input, .switch, .group, .list, .sidebar, .menu, .alert, .glass...
examples/
  preview.html     a live sample of the tokens and components
tools/
  contrast.py      WCAG contrast check for both appearances and Increase Contrast, any accent
                   (uses the shared helpers in the repo's root tools/wcag.py)
docs/
  00-principles.md       the feel, do/don't, references
  01-color.md            system colours, roles, status, measured contrast
  02-typography.md       the system font, the macOS text styles, rules
  03-spacing-layout.md   spacing, sizes, the window frame
  04-components.md       shapes, grouped forms, buttons, fields, switches, lists, menus, alerts
  05-motion.md           durations, curves, patterns
  06-iconography.md      SF Symbols and the off-Mac substitute, status glyphs
  07-theming.md          appearance, accent, Increase Contrast, native apps, Liquid Glass
  08-accessibility.md    contrast, focus, text size, targets, keyboard
  09-voice-and-copy.md   capitalisation, tone and wording
  10-data-viz.md         series, bars, lines
decisions/
  NNNN-*.md        one file per decision, with the reason (accepted / proposed)
```

## How to use it from another project

Add this to the consuming project's `CLAUDE.md`:

```markdown
## Visual style
Follow the style guide at `<path to StyleGuides clone>/macOS` (read its CLAUDE.md first).
Copy `tokens/tokens.css` and `css/macos.css` into the app; never hardcode a colour, size or duration.
```

Native Mac apps use AppKit or SwiftUI system colours by name instead (`docs/07-theming.md`).

## Sources

Apple Human Interface Guidelines, fetched 2026-11-08: Color, Typography, Accessibility,
Materials, Buttons, Toggles, Menus, The menu bar, Alerts, Sidebars, Focus and selection,
Writing. Apple's macOS 27 design kit (Figma and Sketch) has the component values still
marked *(Proposed)*.

## Status

Decided by the user: the default macOS look (0002), and using Apple's official values where
they exist (0001). Everything else is **proposed**: the gap-filling values in 0001, decisions
0003 to 0010, and every *(Proposed)* label in `docs/`.
