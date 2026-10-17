# Theming: dark, glass and transparency

## Dark only

There is one theme, and it is dark. Don't build a light theme or theme switching, and don't
read `prefers-color-scheme` (decisions/0002). `tokens.css` sets `color-scheme: dark` so
native scrollbars, inputs and date pickers render dark.

## The background

- App background: `--color-bg`. Optionally use `.hud-grid-bg` (a faint 24px grid plus a
  warm vignette at the top) on dashboard-style screens.
- Never use flat `#000`. The warm black (`#060404`) is the base.

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

## Per-app character

All apps share the tokens. If an app needs its own identity, the only things that change are
which metal leads and the app's icon. The semantic roles never change.
