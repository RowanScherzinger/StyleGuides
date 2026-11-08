# Iconography

## Icon set

**SF Symbols** in native Mac apps: thousands of symbols that match the system font and scale
with text (HIG > SF Symbols). Use the monochrome rendering mode by default, hierarchical for
depth, and multicolor only when the colour means something (a red `trash.slash`).

SF Symbols are licensed for apps on Apple platforms only. Never put them in a web page, an
Electron app or this repo. Off native, use a plain open-licence outline set with rounded ends
and a similar stroke weight, for example Lucide (ISC), and keep to one set.

| Where | Size | Style |
|---|---|---|
| Toolbar | 16–17px, regular weight | Outline |
| Sidebar | 16px (medium sidebar size) | Outline, accent colour |
| Buttons, menus, list rows | 13–16px, matching the text | Outline |
| Empty states | 48px | Outline, `--color-text-dim` |

Symbols take the text colour of what they're in. Sidebar icons take the accent. An icon-only
button needs a tooltip and an accessible name.

## Status glyphs *(Proposed, decisions/0006)*

Small, plain shapes for status in dense places, always next to words. Drawn as shapes, never
emoji. `.status--*` in `macos.css`.

| State | Glyph | Native SF Symbol |
|---|---|---|
| OK | Filled dot | `circle.fill` (green) |
| Pending | Ring, left half filled | `circle.lefthalf.filled` |
| Idle | Ring | `circle` |
| Warning | Triangle | `exclamationmark.triangle.fill` |
| Error | Octagon | `xmark.octagon.fill` |
| Info / new | Small filled dot | `circle.fill` (accent, small) |

The octagon is Apple's own shape for stop and error, so it reads as "error" on a Mac.

Use the caution triangle sparingly in alerts: only when an action might lose data
unexpectedly (HIG > Alerts).

## Don't

- No hearts, sparkles or other decorative motifs.
- Don't mix icon sets on one screen.
- Don't reuse a status glyph as decoration.
