# CLAUDE.md

This folder is a style guide, not an app. There is nothing to build, run or test.
It partners `Win11/` and shares its token names (decisions/0009), but its values and rules
come from Apple: don't copy rules across from Win11 or the other guides.

## When editing this guide

- A decision has three homes, and all three change together:
  1. the value in `tokens/tokens.css`,
  2. the rule (when and how to use it) in the matching `docs/NN-*.md`,
  3. the reason in a new `decisions/NNNN-short-title.md`.
- Values Apple publishes come from the Human Interface Guidelines (decisions/0001). The
  HIG pages are readable as JSON at
  `developer.apple.com/tutorials/data/design/human-interface-guidelines/<page>.json`; colour
  values are in the swatch images' `alt` text under `references`. To update, re-copy rather
  than adjusting by eye, and change the fetch date in the `tokens.css` header.
- Keep the AppKit or SwiftUI name in the comment beside each token.
- Values Apple doesn't publish are *(Proposed)*. Replace them from Apple's macOS design kit
  or a real Mac when possible, and drop the label when you do. Never fill a gap from memory
  without the label, and never write it up as if the user decided it.
- Every semantic colour is one `light-dark(light, dark)` pair (decisions/0008). Change both
  halves together, and the `prefers-contrast: more` override if there is one.
- After changing any colour token, update `tools/contrast.py` to match, run it, and update the
  contrast table in `docs/01-color.md`.
- `examples/preview.html` must keep working in light, dark and with another accent: update it
  when tokens or classes change.
- Never add SF Pro, SF Mono, New York or SF Symbols files to this repo (Apple's licence).
- Remove an open question from a doc once it is answered.
- Keep docs short and prescriptive.

## When applying this guide inside another project

1. Read `docs/00-principles.md` first, then the docs for what you are building.
2. Use tokens (`var(--...)`) for every colour, font size, space, radius, shadow and
   duration. A literal value in app CSS is a bug unless the guide allows it.
3. Use semantic tokens (`--color-accent`), never palette tokens (`--palette-blue`):
   only semantic tokens switch between light, dark and Increase Contrast.
4. Follow the system: don't force an appearance unless the app has a setting for it, and use
   the system accent where the platform exposes it (`docs/07-theming.md`).
5. The accent marks the default button, selection and "on" states. Status colours mean status
   only. No other colours.
6. Mac conventions: default button on the trailing end with Cancel before it, title case for
   menus and buttons, ellipsis on commands that need more input.
7. Native Mac apps use AppKit or SwiftUI system colours by name, not these tokens (decisions/0007).
8. If the guide is silent, do what the HIG says. If the HIG is silent too, ask the user, then
   record the answer here.

Decision 0002 and the "official values" part of 0001 are the user's own. Everything else is
proposed until the user confirms it, so follow it, but raise anything that seems wrong.
