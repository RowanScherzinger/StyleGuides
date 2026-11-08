# Typography (decisions/0005)

## Typefaces

| Token | Face | Use |
|---|---|---|
| `--font-sans` | SF Pro, through `-apple-system` / `system-ui` | Everything |
| `--font-display` | Same: SF Pro switches between its Text and Display optical sizes by itself | Titles |
| `--font-rounded` | SF Pro Rounded (`ui-rounded`) | Rare: to match a round element |
| `--font-mono` | SF Mono (`ui-monospace`), then Menlo | Paths, IDs, code |

Never ship or link the SF font files: Apple licenses them for designing and building apps for
Apple platforms only (developer.apple.com/fonts). The stack asks for the installed system font,
so a Mac shows SF Pro and other systems fall back to Helvetica Neue, Helvetica or Arial. Off a
Mac the guide looks generic. That's accepted, because the guide is about the Mac.

## Text styles

The macOS built-in text styles (HIG > Typography). 1pt = 1 CSS px. Don't add sizes between them.

| Style | Size / line height | Weight | Emphasized | Class | Use |
|---|---|---|---|---|---|
| Large Title | 26 / 32 | Regular | Bold | `.text-large-title` | Rare: a page title in a big window |
| Title 1 | 22 / 26 | Regular | Bold | `.text-title-1` | Page titles |
| Title 2 | 17 / 22 | Regular | Bold | `.text-title-2` | Section titles, sheet titles |
| Title 3 | 15 / 20 | Regular | Semibold | `.text-title-3` | Group titles |
| Headline | 13 / 16 | Bold | Heavy | `.text-headline` | Alert titles, emphasis, group headers |
| Body | 13 / 16 | Regular | Semibold | `.text-body` | The default for everything |
| Callout | 12 / 15 | Regular | Semibold | `.text-callout` | Secondary blocks of text |
| Subheadline | 11 / 14 | Regular | Semibold | `.text-subheadline` | Descriptions under a setting, alert messages, tooltips, sidebar headings |
| Footnote | 10 / 13 | Regular | Semibold | `.text-footnote` | Fine print |
| Caption 1 | 10 / 13 | Regular | Medium | `.text-caption` | Labels on images, timestamps |
| Caption 2 | 10 / 13 | Medium | Semibold | `.text-caption-2` | |

Add `.is-emphasized` for the emphasized weight. Tracking (`--tracking-*`) is Apple's table for
each size, in em.

## Rules

- 13px body is the Mac default (HIG > Accessibility); 10px is the minimum. Nothing smaller.
- Title case for titles, buttons, menus and tabs; sentence case for descriptions and messages (`09-voice-and-copy.md`).
- Numbers that line up use `font-variant-numeric: tabular-nums`.
- macOS has no Dynamic Type, but the HIG asks apps to allow text up to 200%. Size in `rem`
  and let containers grow with text.
