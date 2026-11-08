# Theming

## Light and dark (decisions/0003)

Both appearances are first-class, and by default the app follows macOS: System Settings >
Appearance (Light, Dark or Auto).

| Variant | How |
|---|---|
| Follow the system (default) | nothing to set |
| Force light | `<html data-theme="light">` |
| Force dark | `<html data-theme="dark">` |

Every semantic colour is one `light-dark(light, dark)` pair, picked by `color-scheme`. That
also switches native form controls and scrollbars. Offer "Light / Dark / Auto" only if the app
has a settings window.

`light-dark()` needs Safari 17.5, Chrome 123 or Firefox 120 (2024); Electron 30 and later.

## Accent colour (decisions/0004)

macOS offers Multicolor, Blue, Purple, Pink, Red, Orange, Yellow, Green and Graphite
(System Settings > Appearance > Accent colour). Multicolor means "the app's own accent", which
for this guide is blue.

The four `--palette-accent*` tokens hold the accent. To follow the user, set them from the
matching system colour (`--palette-purple`, `--palette-purple-dark`, `--palette-purple-ic`,
`--palette-purple-ic-dark`; graphite is gray). *(Proposed)* The named accents are treated as
the system colours of the same name. On a Mac, read the real value instead where you can:

- **Electron**: `systemPreferences.getAccentColor()` gives the colour as RGBA hex without a
  `#` (`"0088ffff"`). Listen with
  `systemPreferences.subscribeNotification('AppleColorPreferencesChangedNotification', ...)`.
  Electron gives one shade, so set it as the light and dark accent and keep the IC shades of
  the nearest named colour for text.
- **Native apps** use `NSColor.controlAccentColor` and never need these tokens.
- **A plain web page** can't read the accent. Keep the default blue.

Accent and appearance both change while the app runs. Follow them live.

## Increase Contrast

System Settings > Accessibility > Display > Increase contrast. On the web this is
`prefers-contrast: more`. `tokens.css` swaps in Apple's increased-contrast colours and
stronger greys and strokes. Electron: `nativeTheme.shouldUseHighContrastColors`. The one
exception is the dark accent fill, which keeps its default shade so white text stays readable
(`01-color.md`).

## Native apps (decisions/0007)

A native Mac app (AppKit or SwiftUI) doesn't mirror these tokens. It uses the system colours
by name (`NSColor.windowBackgroundColor`, `.labelColor`, `.controlAccentColor`), the system
font and standard controls, which follow appearance, accent, Increase Contrast and Reduce
Transparency by themselves. Each token's comment names its AppKit colour for that mapping.
Use the tokens only for custom-drawn views, and only through those named colours.

## Materials

macOS 26 and later use **Liquid Glass** for the control layer: toolbars, sidebars, menus,
popovers. Content stays on solid backgrounds (HIG > Materials).

- `.glass` blurs what's behind where the browser supports `backdrop-filter`. The solid tokens
  (`--color-bg-elevated`, `--color-sidebar`, `--color-surface-raised`) are the default and
  always acceptable.
- Only use glass where content scrolls beneath it. A glass panel over a flat window colour
  looks like a grey panel with extra cost.
- Over photos and video, put chips on `--color-scrim` with `--color-on-scrim` text.
  *(Proposed)* Black at 55%: the HIG's 35% dimming layer is for under clear glass, and gives
  white text only 2.4:1 over a white photo; 55% gives 4.7.
- **Reduce Transparency** makes glass solid. `tokens.css` handles it through
  `prefers-reduced-transparency: reduce`, which works in Chrome 118+ and Electron but **not in
  Safari** (MDN compatibility data, November 2026). In Safari glass stays on, so keep glass
  optional and never put text on it that is unreadable without the blur. Electron can also read
  `nativeTheme.prefersReducedTransparency`.

## Inactive windows

macOS dims windows that aren't key. Selected rows go grey, and window controls go grey. A web
app can do the same with `window` `blur` and `focus` events: swap `--color-selection` for
`--color-selection-inactive` while the window is blurred. Electron gets this from the system.
