# Principles

The overall feel. When a specific rule is missing, decide by these.

## Direction

Look like a default macOS app (decisions/0002). Someone opening the app should feel it
belongs on their Mac: the same type, colours, controls and window frame as Finder, Notes and
System Settings. It follows the system's light or dark appearance (decisions/0003), the
user's accent colour (decisions/0004) and Increase Contrast.

The guide doesn't invent a look. Where Apple publishes a value (system colours, the type ramp,
minimum sizes), it's Apple's, copied from the Human Interface Guidelines (decisions/0001).
Where Apple is silent, the gap is filled with what AppKit draws, and labelled *(Proposed)*.

This guide partners `Win11/`: same token names and layout, so an app can offer both
(decisions/0009). Behaviour differs where the platforms differ (button order, capitalisation,
selection), and the macOS way wins here.

## Feel *(Proposed)*

| Quality | In practice |
|---|---|
| **Native** | System font, system accent, system appearance. Nothing a Mac user would have to learn. |
| **Content first** | Content sits on solid backgrounds. Controls and navigation float above it, on glass where the platform has it. |
| **Quiet greys** | Neutral greys carry the window. Colour is the accent and status, used sparingly. |
| **Rounded and concentric** | Corners grow with size (controls 7px, boxes 10px, menus 12px, windows 16px) and nest: inner radius = outer minus padding. |
| **Smooth motion** | Short eased or spring movement that shows where things came from. Nothing loops except progress. |

## Do *(Proposed)*

- Put the default button on the trailing end, Cancel before it. Return presses the default button, Esc cancels.
- Use title case for menus, buttons, tabs and window titles; sentence case for descriptions and messages (`09-voice-and-copy.md`).
- Group settings in rounded boxes, label on the leading side, control on the trailing side.
- Put every toolbar command in the menu bar too (HIG > Toolbars).
- Let the user's settings win: appearance, accent, Increase Contrast, Reduce Transparency, Reduce Motion.

## Don't *(Proposed)*

- No brand colour in place of the user's accent, except as the "Multicolor" default.
- No glass in the content layer (HIG > Materials). Glass is for toolbars, sidebars, menus and popovers.
- No controls or critical information at the bottom of a window: people drag windows half off-screen (HIG > Layout).
- No shadows on content. Shadows are for windows, menus and popovers.
- No cute or playful details. No all caps.
- No hard-coded black or white backgrounds: use the tokens, so both appearances work.

## Reference

| Reference | Take this |
|---|---|
| Apple Human Interface Guidelines (developer.apple.com/design/human-interface-guidelines) | System colours, type ramp, tracking, minimum sizes, contrast, component behaviour, wording |
| Apple Design Resources: macOS 27 kit (Figma and Sketch) | Component shapes and sizes, to replace the *(Proposed)* values |
| AppKit `NSColor` | The semantic colour names each token mirrors |
| Finder, Notes and System Settings | How the pieces compose: sidebar, toolbar, grouped forms, lists |
