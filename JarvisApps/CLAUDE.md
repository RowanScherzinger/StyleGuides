# CLAUDE.md

This repo is a style guide, not an app. There is nothing to build, run or test.

## When editing this repo

- A decision has three homes, and all three change together:
  1. the value in `tokens/tokens.css`,
  2. the rule (when and how to use it) in the matching `docs/NN-*.md`,
  3. the reason in a new `decisions/NNNN-short-title.md`.
- Do not invent preferences. If a section says **TBD**, leave it TBD until the user
  decides. If you must fill a gap, label it *(Proposed)* in the doc and log it with
  `Status: proposed` in `decisions/`. Never write it up as if the user decided it.
- After changing any colour or glass token, update `tools/contrast.py` to match, run it,
  and update the contrast table in `docs/01-color.md`.
- `examples/preview.html` must keep working: update it when tokens or classes change.
- Remove an open question from a doc once it is answered.
- Keep docs short and prescriptive: "do X", "never Y", with a small example.

## When applying this guide inside another project

1. Read `docs/00-principles.md` first, then the docs for what you are building.
2. Use tokens (`var(--...)`) for every colour, font size, space, radius, shadow and
   duration. A literal value in app CSS is a bug unless the guide allows it.
3. Prefer semantic tokens (`--color-surface`, `--color-danger`) over raw palette
   tokens (`--palette-red-500`) in component code.
4. If the guide is silent on something, ask the user, then record the answer here.
   Do not fill the gap with a generic default.
5. Respect each app's context: Desktop-Widgets sits on a transparent overlay, so
   see `docs/07-theming.md` before choosing backgrounds.
6. Dark only. Never add a light theme or a `prefers-color-scheme` branch.
7. Use the colour roles in `docs/01-color.md`. Warm metals carry the look. Chartreuse
   (OK status) and arc blue (info, high-contrast marks) are only for small accents
   (decisions/0007). Red is only for danger (proposed, decisions/0004).

Only decisions 0002, 0003 and 0007 are the user's own. Everything else in `docs/` is
proposed until the user confirms it, so follow it, but raise anything that seems wrong.
