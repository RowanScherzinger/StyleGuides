# 0008. Native Windows apps mirror the tokens in code

Date: 2026-10-17
Status: accepted (the approach). The native mappings listed under "Proposed mappings" are proposed.
Amends 0001: `tokens/tokens.css` stays the single source of truth; native apps copy from it.

## Decision
A native Windows app (first one: iPhone Explorer, C# WinForms) follows the guide by mirroring
`tokens/tokens.css` into one theme file in its own language (`Hud/Theme.cs`). Each member is
named after its token (`ColorAccent` for `--color-accent`). The file header gives the path to
`tokens.css` and the date it was copied. No colour, font, size or duration literal appears
anywhere else in the app.

When the guide's tokens change, re-copy the values into the theme file by hand.

## Why
User decision: keep the app a small native exe rather than rewriting its UI in WebView2 just
to use the CSS directly. 0001 said to revisit if a non-web consumer appeared. One has, and a
token generator still isn't worth it for one native app.

Rejected: a WebView2 UI that uses `tokens.css` and `hud.css` directly. It would always match the
guide exactly (real glass blur, CSS animation), but it means a bigger rewrite and a heavier app.

## Proposed mappings
These fill gaps the CSS-only guide doesn't cover. They're in use but not yet confirmed:

- **Translucent tokens:** native controls can't draw translucent backgrounds, so an rgba token
  used as a control background is blended over `--color-bg` first. Owner-drawn surfaces keep the
  real alpha.
- **Glass:** tint only, no blur. WinForms has no backdrop filter.
- **Fonts:** the installed fallbacks from the font stacks are used: Cascadia Mono, Bahnschrift for
  Orbitron, and Segoe UI for Inter. GDI text can't use bundled fonts without extra work.
- **Letter-spacing:** GDI has no tracking, so labels are drawn one character at a time.
- **Reduced motion:** the Windows "Animation effects" setting stands in for
  `prefers-reduced-motion`.
- **Native chrome:** `Application.SetColorMode(Dark)` handles scrollbars and common controls.
  The title bar uses the elevated black with a copper border through DWM.
- **Message boxes:** replaced by a modal in the guide's style, because a native MessageBox has a
  white surface.
- **The Windows folder picker** stays native. It's the one surface the app can't restyle.
- **Check boxes** (the guide only defines toggles): a square box with a copper hairline that
  turns gold with a gold tick when checked.
- **Context menus:** raised glass with a strong border and brackets. Items use uppercase display
  text. The hovered item gets `--color-accent-soft` and a 2px copper edge.
- **Badges over photos** (NEW, LIVE, EDITED, VIDEO): small sharp chips on `--color-bg` at 80%.
  NEW uses the info status (arc blue and a circle). The others use silver for neutral data.

## Affects
`README.md` (apps table), `docs/07-theming.md` (native section), and 0001, which this amends.
No token values changed.
