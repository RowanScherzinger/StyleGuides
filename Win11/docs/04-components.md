# Components

Classes live in `css/fluent.css`. They copy the WinUI control templates' look; anything not in
WinUI is marked *(Proposed)*.

## Shape

| Element | Radius |
|---|---|
| Button, text box, combo box, check box, list item, menu item, InfoBar, tooltip | `--radius-control` 4px |
| Card, flyout, menu, dialog, window, content layer | `--radius-overlay` 8px |
| Toggle switch, radio button, progress bar, badge | `--radius-full` |

Buttons are never pills. Nested corners: inner radius = outer minus padding.

## Cards

`.card`: `--color-surface`, a `--color-card-border` hairline, 8px corners, 16px padding, no
shadow. Stack related cards with 4px between them.

`.card--row` is the Settings row: an icon, a title with a caption-sized description under
it, and the control on the right, at least 68px high. `.card--clickable` darkens slightly on
hover and opens something (add a chevron on the right).

## Buttons

32px high, 4px corners, at least 120px wide with text, body text (regular weight).

| Class | Use |
|---|---|
| `.btn` | Standard: most actions. Control fill, hairline, darker bottom edge. |
| `.btn--accent` | The primary action. One per view, and the default button in a dialog. |
| `.btn--subtle` | No fill at rest: toolbar buttons, icon buttons (`.btn--icon`), "Learn more". |
| `.btn--danger` | *(Proposed)* A destructive action outside a dialog. Critical tint and text. Inside a confirming dialog, the destructive button is the accent button. |

Pressed buttons dim their text instead of moving. Disabled buttons use the disabled fill and text.

## Text box

`.input`: control fill, hairline, with a stronger bottom stroke. On focus the fill turns solid
(`--color-input-active`) and the bottom edge becomes a 2px accent line. Placeholder in
`--color-text-dim`. The label sits above, in body text (`.field`).

## Check box, radio, toggle

- `.check`: 20px, 4px corners, strong stroke. Checked: accent fill, on-accent tick.
- `.radio`: 20px circle. Checked: accent fill with an on-accent dot.
- `.toggle`: 40×20 pill, a 12px knob that grows on hover. On: accent track, on-accent knob.
  Use a toggle for settings that take effect at once; a check box for choices that are applied
  with a button.

Wrap a control and its text in `.choice` so the text is clickable.

## Lists and navigation

`.list-item` (40px) and `.nav-item` (36px): no fill at rest, a subtle fill on hover. Selected
rows keep the subtle fill and show a 3×16px accent pill on the left edge. Rows are inset 4px
from the edge with 4px corners.

## InfoBar

`.infobar` for messages in the page: a status icon, a body-strong title, the message, and
optionally an action or close button. `--ok`, `--warning`, `--danger`; the default is info.
It stays until the problem is fixed or the user closes it. Don't use toasts inside the app.

## Progress

- `.progress`: a 1px track with a 3px accent bar. `.progress--indeterminate` sweeps.
- `.progress-ring`: 32px spinner for "working" when there's no bar to fill.

Show progress after about a second; below that, show nothing.

## Badges

`.badge`: an accent pill with an 11px semibold number (InfoBadge). `.badge--dot` for "new"
without a count; `.badge--danger` for errors.

## Flyouts, menus, tooltips

`.flyout`: `--color-surface-raised`, 8px corners, a flyout hairline, `--shadow-flyout`, 4px
vertical padding. `.flyout--acrylic` blurs what's behind where the browser can.

`.menu-item`: 32px rows inset 4px, a subtle fill on hover, the shortcut right-aligned in
caption size. Icons, when one item has one, on all of them.

`.tooltip`: caption size, 4px corners, at most 320px wide.

## Dialog

`.dialog` over `.dialog-smoke` (black at 30%): 8px corners, 320–548px wide, the title in
subtitle size, 24px padding, and a footer bar in `--color-dialog-footer` with equal-width
buttons. The primary button is the accent button and comes first (left). Every dialog has a
way out ("Cancel" or "Close").

## Empty states

A 48px icon in `--color-text-dim`, a subtitle-size line saying what's missing, a body line
saying how to fill it, and at most one button.
