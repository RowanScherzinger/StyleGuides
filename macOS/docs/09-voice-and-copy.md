# Voice and copy

Write like the Mac: direct, plain and friendly. Follow the Apple Style Guide and HIG > Writing
where this is silent.

## Capitalisation (HIG > Menus, Alerts, Tab views, Labels)

| Element | Style | Example |
|---|---|---|
| Menu titles and items | Title case | `Show in Finder`, `Save As…` |
| Buttons, tabs, window and sheet titles | Title case | `Copy Photos`, `General` |
| Labels before a control | Title case with a colon | `Copy To:` |
| Alert title, if a fragment | Title case, no full stop | `Disk Almost Full` |
| Alert title, if a sentence | Sentence case, with punctuation | `Delete 12 photos from the phone?` |
| Alert message, descriptions, check box text | Sentence case, full sentences | `You can't undo this action.` |

Title case capitalises every word except articles, coordinating conjunctions and short
prepositions, and always the last word. *(Proposed)* Buttons and check boxes follow AppKit's
habit (buttons title case, check boxes sentence case), because the HIG leaves them to the app.

## Rules

- **Talk to the user as "you"**. Contractions are fine.
- **Buttons say what they do**: "Copy 12 Photos", "Delete", "Save". Not "OK" when a verb fits (HIG > Alerts).
- **Ellipsis** (the single character …) on any command that needs more input before it acts.
- **Short**: lead with what matters. A setting's description is one line.
- **Plain, not playful**: no exclamation marks, jokes or emoji.
- **Errors** say what happened, why, and what to do next. Never "Error" or an error code as
  the title (HIG > Alerts). Put codes in details.
- **Names**: the Mac's own words. "Settings" (not "Preferences", which macOS dropped in
  version 13), "Trash" (not "Recycle Bin"), "folder", "Finder", "⌘C" shown as symbols in menus.
- **Keys**: name them as Apple does: Command (⌘), Option (⌥), Shift (⇧), Control (⌃), Return, Delete.
