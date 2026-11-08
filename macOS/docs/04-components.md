# Components

Classes live in `css/macos.css`. Behaviour follows the HIG. Sizes and radii are *(Proposed)*
until checked against Apple's macOS 27 design kit (`03-spacing-layout.md`).

## Shape *(Proposed)*

| Element | Radius |
|---|---|
| Check box, menu-item highlight, list row, tooltip | `--radius-small` 4px |
| Push button, text field, pop-up button, segmented control, sidebar row | `--radius-control` 7px |
| Grouped box, list, callout | `--radius-box` 10px |
| Menu, popover, alert, sheet | `--radius-overlay` 12px |
| Window | `--radius-window` 16px |
| Switch, radio, search field, toolbar capsule, badge | `--radius-full` |

Corners are concentric: an inner radius is the outer radius minus the padding between them.

## Grouped forms

`.group` is a System Settings box: a faint fill, 10px corners, rows separated by hairlines.
Each `.group__row` has the label (and an optional `.group__desc` in subheadline size) on the
leading side and the control on the trailing side. Put a `.group-heading` above a box when the
boxes need names. Use a mini switch (`.switch--mini`) in rows so they keep the same height
(HIG > Toggles).

## Buttons

28px high, 7px corners, body text, title case. A button that opens another window or view ends
with an ellipsis: "Export…" (HIG > Buttons).

| Class | Use |
|---|---|
| `.btn` | Push button: most actions. White bezel, hairline, slight lift. |
| `.btn--default` | The default button: accent fill, pressed by Return. One per window or sheet, on the trailing end. Never a destructive action (HIG > Buttons). |
| `.btn--destructive` | A destructive action the user didn't deliberately choose, in system red, bold: red text on the bezel in light, *(Proposed)* a red fill with white text in dark, where red text on the grey bezel is 2.0:1. Not for "Empty Trash" after choosing Empty Trash (HIG > Alerts). |
| `.btn--borderless` | Toolbar items and icon buttons (`.btn--icon`): no bezel until hovered. In a toolbar, group related items in a `.btn--capsule`. |

In a row of buttons the default button is last (trailing), Cancel just before it, and other
buttons further towards the leading side. Always "Cancel", never "No" or "Close", for the
button that backs out.

## Segmented control

`.segmented` switches between views in a toolbar or inspector. In the window body, use tabs
instead (HIG > Segmented controls). The selected segment is a raised white piece, not accent.

## Text field

`.input`: white (dark: faint white) fill, a stroke, 7px corners. On focus, the accent focus
ring. Placeholder in `--color-text-dim`. Labels go on the leading side, end with a colon and are
title case: `Name:` (HIG > Combo boxes). `.input--search` is the round search field.

## Check box, radio, switch

- `.check`: 14px, 4px corners. On: accent fill, white tick. Mixed (`:indeterminate`): a dash.
- `.radio`: 14px circle. On: accent fill, white dot. Two to five in a set; more than that, use a pop-up button.
- `.switch`: 38×22, white knob, accent track when on. `.switch--mini` in form rows.

Prefer a check box for a single setting. Use a switch to turn a group of settings on or off.
Keep both in the window body, never in a toolbar (HIG > Toggles). Wrap the control and its text
in `.choice`.

## Lists, tables and sidebars

- `.list` with `.list-item`: a selected row is accent-filled with white text while the list has
  focus, and grey (`--color-selection-inactive`) when it doesn't (HIG > Focus and selection).
  `.list--alternating` stripes rows in multicolumn tables.
- `.sidebar-item`: a selected row gets a quiet grey highlight, never the accent fill. Icons
  are accent-coloured. Headings (`.sidebar__heading`) are small, bold and dim.

## Callout *(Proposed)*

macOS has no standard in-page message bar. When one is needed, `.callout` shows a status glyph,
a bold title and the message on a faint status tint (`--ok`, `--warning`, `--danger`; the
default is info). Interruptions are alerts; everything else should be a callout or inline text.

## Progress

- `.progress`: a 6px rounded track with an accent bar. `.progress--indeterminate` sweeps.
- `.spinner`: the 16px spinning wheel, for background work or tight spaces. Don't label it
  (HIG > Progress indicators).

## Badges

`.badge`: a grey count capsule, for sidebar and list counts. `.badge--danger` (red) only for
things that need attention.

## Menus, popovers, tooltips

`.menu`: `--color-surface-raised` (or `.glass`), 12px corners, a menu shadow, 5px padding.
`.menu-item` rows are 22px high. The highlighted item is accent-filled with white text.
Shortcuts are right-aligned in `--color-text-dim`, using the symbols ⌘ ⌥ ⇧ ⌃. Items that need
more input end with an ellipsis: "Save As…". Menu titles and items are title case (HIG > Menus).

`.popover` for a small piece of UI anchored to a control. `.tooltip`: subheadline size, a short
phrase that says what the control does.

## Alerts and sheets

`.alert` over `.smoke`: the app icon (64px), a bold title, a short message in subheadline
size, and the buttons. The default button is on the trailing side and Cancel on the leading
side. Esc and ⌘. cancel. Don't use "OK" unless the alert only informs (HIG > Alerts). Use an
alert only for something the user must know now. Common, undoable actions don't need one.

`.sheet`: a card over its parent window, for a task tied to that window. Buttons sit in a
row at the bottom trailing corner, default last.

## Empty states

A 48px symbol in `--color-text-dim`, a Title 2 line saying what's missing, a body line saying
how to fill it, and at most one button.
