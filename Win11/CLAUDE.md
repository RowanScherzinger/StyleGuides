# CLAUDE.md

This folder is a style guide, not an app. There is nothing to build, run or test.
It is independent of the other guides in this repo: don't copy rules across from them.

## When editing this guide

- A decision has three homes, and all three change together:
  1. the value in `tokens/tokens.css`,
  2. the rule (when and how to use it) in the matching `docs/NN-*.md`,
  3. the reason in a new `decisions/NNNN-short-title.md`.
- Colour values come from WinUI's `Common_themeresources_any.xaml` (decisions/0001). Keep the
  WinUI resource name in the comment beside each token. To update, re-copy from WinUI rather
  than adjusting by eye, and change the copy date in the file header.
- Do not invent preferences. If you must fill a gap WinUI leaves, label it *(Proposed)* in the
  doc and the token comment, and log it with `Status: proposed` in `decisions/`. Never write it
  up as if the user decided it.
- Every semantic colour is one `light-dark(light, dark)` pair (decisions/0008). Change both halves together.
- After changing any colour token, update `tools/contrast.py` to match, run it, and update the
  contrast table in `docs/01-color.md`.
- `examples/preview.html` must keep working in light, dark and with another accent: update it
  when tokens or classes change.
- Remove an open question from a doc once it is answered.
- Keep docs short and prescriptive.

## When applying this guide inside another project

1. Read `docs/00-principles.md` first, then the docs for what you are building.
2. Use tokens (`var(--...)`) for every colour, font size, space, radius, shadow and
   duration. A literal value in app CSS is a bug unless the guide allows it.
3. Use semantic tokens (`--color-accent`), never palette tokens (`--palette-accent-dark-1`):
   only semantic tokens switch between light and dark.
4. Follow the system: don't force a mode unless the app has a setting for it, and use the
   system accent where the platform exposes it (`docs/07-theming.md`).
5. The accent marks one primary action, selection and "on" states. Status colours mean status
   only. No other colours.
6. Plain, not playful: sentence case, no decoration, no exclamation marks.
7. Native apps mirror the tokens in one theme class (`docs/07-theming.md`).
8. If the guide is silent, do what WinUI does. If WinUI is silent too, ask the user, then record
   the answer here.

Decisions 0002 and 0003 are the user's own. Everything else is proposed until the user confirms
it, so follow it, but raise anything that seems wrong.
