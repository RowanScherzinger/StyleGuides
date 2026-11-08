# Principles

The overall feel. When a specific rule is missing, decide by these.

## Direction

Look like a default Windows 11 app (decisions/0002). Someone opening the app should feel it
belongs on their PC: the same type, colours, corners and controls as Settings, File Explorer
and the Microsoft Store. It follows the system's light or dark mode (decisions/0003) and the
user's accent colour (decisions/0004).

The guide doesn't invent a look. Its values are Microsoft's own, mirrored from WinUI
(decisions/0001). Where WinUI is silent, the gap is filled in the plainest way that fits, and
labelled *(Proposed)*.

## Feel *(Proposed)*

| Quality | In practice |
|---|---|
| **Native** | System font, system accent, system light/dark. Nothing a Windows user would have to learn. |
| **Calm** | Neutral greys carry the page. Colour is the accent, used sparingly, and status colours. |
| **Layered** | Window background, then a content layer, then cards. Each step is a slight tint and a hairline, not a shadow. |
| **Soft-edged** | 4px on controls, 8px on cards and overlays. Never sharp, never pill-shaped buttons. |
| **Quiet motion** | Short, decelerating movement that confirms what happened. Nothing loops except progress. |

## Do *(Proposed)*

- Use the accent for one primary action per view, selection, and things that are "on".
- Build pages from cards on the content layer, with 4px between related cards.
- Write in sentence case, plainly (`09-voice-and-copy.md`).
- Use the Fluent icon set (`06-iconography.md`) at 16px in controls.
- Let the user's settings win: light/dark, accent, text size, contrast themes, animation effects.

## Don't *(Proposed)*

- No custom brand colours in place of the accent. Status colours mean status only.
- No heavy drop shadows on cards. Shadows are for things that float: flyouts, tooltips, dialogs.
- No all-caps labels, letter-spaced headings or decorative fonts.
- No cute or playful details (hearts, sparkles, "Yay!"). Plain is the point.
- No hard-coded black or white backgrounds: use the tokens, so both modes work.

## Reference

| Reference | Take this |
|---|---|
| WinUI `Common_themeresources_any.xaml` (microsoft/microsoft-ui-xaml) | Every colour token |
| Microsoft Learn: Windows app design (Fluent for Windows 11) | Type ramp, corners, spacing, motion, materials |
| Windows Settings and File Explorer | How the pieces compose: navigation pane, cards, lists |
