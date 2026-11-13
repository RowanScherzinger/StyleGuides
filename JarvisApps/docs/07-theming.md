# Theming: dark, glass and transparency

## Dark only

There is one theme, and it is dark. Don't build a light theme or theme switching, and don't
read `prefers-color-scheme` (decisions/0002). `tokens.css` sets `color-scheme: dark` so
native scrollbars, inputs and date pickers render dark.

## The background

- Every app's page background is `.hud-grid-bg`: `--color-bg` with a faint 24px grid and
  a warm copper vignette at the top (decisions/0012). Put it on `<body>`, next to `.hud-root`.
  It's the staple backdrop of the family, on every screen, including text-heavy ones.
- The grid stays put while the page scrolls (`background-attachment: fixed`), so panels
  move over it like a HUD over a fixed field, and the vignette stays at the top of the view.
- Exception: Desktop-Widgets has no page background (it floats over the wallpaper), so no grid.
- Never use flat `#000`. The warm black (`#060404`) is the base.

```html
<body class="hud-root hud-grid-bg">
```

## Glass over the app (Jarvis, Larder, Plox)

Use `.glass`. The panel tint is `--color-surface` at 62% with a 12px backdrop blur over
the app's own background. Here the content behind the glass is known, so the blur works
as designed.

## Glass over the desktop (Desktop-Widgets)

The widgets float over an unknown wallpaper, and that changes two things:

1. **CSS `backdrop-filter` can't see the desktop.** In a transparent Electron window it
   only blurs the window's own content, so the wallpaper is never blurred. Real frosted glass
   over the desktop needs the native window material (`backgroundMaterial: 'acrylic'` on
   Windows 11). That applies to the whole window, not to each widget, so it doesn't suit a
   full-screen overlay. In practice, widget glass is **tint only**.
2. **The tint has to carry contrast by itself.** Use `.glass--overlay`
   (`--color-surface-overlay`, 84%). This is the lowest tint where body text, muted text,
   gold and ember still pass 4.5:1 over a pure white wallpaper. Desktop-Widgets' current
   38% tint fails over any bright wallpaper (text measures 1.8:1).
   - Copper and danger text on the overlay: large or bold only.
   - `--color-text-dim` is not allowed on the overlay.
   - Bare text with no panel needs `text-shadow: 0 0 3px #000, 0 0 8px #000`.

## Native Windows apps (iPhone Explorer)

Native apps can't read `tokens.css`. Mirror it in a single theme file instead (decisions/0008):

- Name each member after its token, and put the path to `tokens.css` and the copy date in the
  file header. Re-copy the values by hand when the tokens change.
- Never use a colour, font, size or duration literal outside that file.
- Glass is tint only, with no blur. Blend translucent tokens over `--color-bg` before using them
  as a native control background *(Proposed)*.
- Use `Application.SetColorMode(Dark)` for native chrome, and replace message boxes with a modal
  in the guide's style *(Proposed)*.
- The Windows "Animation effects" setting stands in for reduced motion *(Proposed)*.

## Home Assistant

HA is themed through its own theme YAML, not by copying `tokens.css` (decisions/0010):

- The theme copies every token as a theme variable, so card CSS can use `var(--color-*)`.
  It is generated from `tokens.css`. Re-run the build when the tokens change.
- The theme has a dark mode only, so HA can't switch to light.
- Entity state: active ("light on", "switch on") is **gold**, a live value. Inactive is idle
  silver. Chartreuse is only the small OK / running status light. Never use it for active
  state fills or icons.
- HA's named colours (`--amber-color`, `--purple-color`...) are remapped into the warm range
  *(Proposed)*. Cool names map to arc blue or chartreuse, so they stay small marks.
- Glass, corner brackets and HUD headings come from card-mod. Readout tiles, status lights and
  ring gauges come from button-card templates *(Proposed)*.
- On/off controls are chips (`04-components.md`: Chips), built as a button-card template,
  because a standard tile can't be both one row tall and a third of a column wide. Dimmable
  lights are chips too, full width where the level needs a longer track.
- Fonts are self-hosted from HA's `www/` folder and loaded on every page.

## Per-app character

All apps share the tokens. If an app needs its own identity, the only things that change are
which metal leads and the app's icon. The semantic roles never change.
