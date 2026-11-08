# Iconography

## Icon set

**Segoe Fluent Icons** (`--font-icons`), which ships with Windows 11, falling back to Segoe
MDL2 Assets on Windows 10. On the web or off Windows, use **Fluent UI System Icons**
(Microsoft, MIT licence): the same shapes as SVG.

| Where | Size | Style |
|---|---|---|
| In buttons, menus, list rows | 16px | Regular (outline) |
| Navigation pane | 16px (20px for touch) | Regular; filled when selected is allowed |
| Settings card | 20px | Regular |
| Empty states | 48px | Regular, `--color-text-dim` |

Icons take the text colour of what they're in. Accent-coloured icons only for "on" states.
An icon-only button needs a tooltip and an accessible name.

## Status glyphs *(Proposed, decisions/0006)*

Small, plain shapes for status in dense places (lists, a device panel, a badge on a
thumbnail), always next to words. Drawn as shapes, never emoji. `.status--*` in `fluent.css`.

| State | Glyph |
|---|---|
| OK | Filled dot |
| Pending | Ring, left half filled |
| Idle | Ring |
| Warning | Triangle |
| Error | Ring with a cross |
| Info / new | Small filled dot |

In messages (InfoBar) use the full Fluent status icons instead: a check in a circle (OK),
an exclamation in a triangle (warning), a cross in a circle (error), an "i" in a circle (info),
filled, in the status colour.

## Don't

- No hearts, sparkles, stars or other decorative motifs.
- Don't mix icon sets on one screen.
- Don't reuse a status glyph as decoration.
