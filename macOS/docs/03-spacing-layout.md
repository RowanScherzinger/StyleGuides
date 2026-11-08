# Spacing and layout

## Scale *(Proposed)*

A 4px scale, `--space-1` (4px) to `--space-10` (40px). Apple publishes no grid for macOS. The
two anchors are AppKit's: 8px standard spacing between controls, and a 20px window margin.

| Gap | Value | Where |
|---|---|---|
| Between controls | 8px (`--space-2`) | Buttons in a row |
| Between a label and its control | 8px | `Name:` and its text field |
| Between groups of controls | 12–20px | Boxes in a form |
| Window margin | 20px (`--space-5`) | Content to the window edge, sheet padding |
| Grouped box padding | 12px sideways (`--space-3`) | `.group` |

## Sizes

| Thing | Size | Token | Source |
|---|---|---|---|
| Control (button, field, pop-up) | 28px | `--control-height` | HIG > Accessibility: default control size |
| Small control | 20px | `--control-height-small` | HIG > Accessibility: minimum control size |
| Menu bar | 24px | `--menubar-height` | HIG > The menu bar |
| Sidebar row | 28px | `--row-height` | *(Proposed)*: the medium sidebar size |
| Table row | 24px | `--row-height-table` | *(Proposed)* |
| Toolbar (unified with title bar) | 52px | `--toolbar-height` | *(Proposed)* |
| Sidebar | 220px | `--sidebar-width` | *(Proposed)* |
| Click targets | at least 20×20px, 28×28px by default | | HIG > Accessibility |

The user can set the sidebar to small, medium or large (System Settings > Appearance >
Sidebar icon size). Native sidebars follow it; web sidebars use medium.

## Composition

The standard Mac window:

1. **Toolbar** across the top, unified with the title bar: window controls on the leading
   side, then the title, then toolbar items. Over scrolling content it's glass.
2. **Sidebar** on the leading side, full height, for navigation. On glass where the
   platform has it (`07-theming.md`); otherwise `--color-sidebar`.
3. **Content** on `--color-bg` (forms, settings) or `--color-content` (lists, tables,
   documents). Settings use grouped boxes (`.group`) in a centred column up to about 640px.
4. Optionally an **inspector** on the trailing side.

Nothing important at the bottom of a window: no bottom-only buttons except a sheet's or
alert's, and a bottom bar only for a small summary, like Finder's status bar (HIG > Windows).

## Narrow windows *(Proposed)*

| Width | Sidebar |
|---|---|
| Under 640px | Collapsed. A toolbar button shows it. |
| 640px and up | Shown, 220px |

Collapse the sidebar on its own as the window shrinks, as Mail does (HIG > Sidebars).
