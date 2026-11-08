# Theming

## Light and dark (decisions/0003)

Both variants are first-class, and by default the app follows Windows: Settings >
Personalization > Colors > "Choose your mode".

| Variant | How |
|---|---|
| Follow the system (default) | nothing to set |
| Force light | `<html data-theme="light">` |
| Force dark | `<html data-theme="dark">` |

Every semantic colour is one `light-dark(light, dark)` pair, picked by `color-scheme`. That
also switches native form controls and scrollbars. Offer a "Light / Dark / Use system
setting" choice only if the app has a settings page; otherwise just follow the system.

`light-dark()` needs Chrome 123, Firefox 120 or Safari 17.5 (2024); Electron 30 and later.

## Accent colour (decisions/0004)

The accent is the user's Windows accent colour. Override the seven `--palette-accent-*`
shades with the system's, and every accent token follows:

- **Electron**: `systemPreferences.getAccentColor()` gives the base; listen for
  `accent-color-changed`. Electron doesn't give the shades, so derive them, or read them as below.
- **Native Windows apps**: the shades are in the registry,
  `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Accent`, value `AccentPalette`:
  32 bytes, eight RGBA entries in the order Light3, Light2, Light1, Base, Dark1, Dark2, Dark3,
  then one unused. WinUI apps get them as `SystemAccentColorLight2` and so on.
- **A plain web page** can't read the accent. Keep the default blue.

Accent changes and light/dark changes both happen while the app runs. Follow them live
(native: `WM_SETTINGCHANGE` / `SystemEvents.UserPreferenceChanged`; web: the `color-scheme`
media query does it for you).

## Native apps (decisions/0007)

A native Windows app can't use `tokens.css`. Mirror the tokens by hand in one place (a theme
class) and read them only from there. Then:

- Read light/dark from `HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize`,
  `AppsUseLightTheme` (0 = dark; missing = light).
- Leave the title bar to Windows. Set `DWMWA_USE_IMMERSIVE_DARK_MODE` to match the mode and
  leave caption, border and text colours at their defaults, so the user's "accent colour on
  title bars" setting still works.
- Native controls can't draw translucent fills: pre-blend the translucent tokens over
  `--color-bg` (or whatever they sit on).
- Switch native scrollbars with `SetWindowTheme(hwnd, "DarkMode_Explorer" | "Explorer")`.
- Check "Animation effects" (`SPI_GETCLIENTAREAANIMATION`) for reduced motion.

Phone Explorer does all of this: its theme is the reference implementation.

## Materials

Windows 11 apps use **Mica** for the window background and **Acrylic** for flyouts.

- Mica tints the window with the desktop wallpaper. Browsers can't do it. The tokens use its
  solid fallback (`--color-bg`), which is what Windows itself shows when Mica is off. Native
  apps may enable Mica (`DWMWA_SYSTEMBACKDROP_TYPE`) only if every surface over it is
  translucent; otherwise stay solid.
- Acrylic: `.flyout--acrylic` blurs behind a flyout where `backdrop-filter` works. The solid
  `--color-surface-raised` is the default and always acceptable.

## Contrast themes

When Windows uses a contrast theme (`forced-colors: active`), the browser replaces colours with
the user's. `fluent.css` keeps every edge visible and maps accents to `Highlight`. Native apps
should detect high contrast (`SystemInformation.HighContrast`) and use system colours.
