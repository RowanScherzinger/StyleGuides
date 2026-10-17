# CLAUDE.md

This folder is a style guide, not an app. There is nothing to build, run or test.
It is independent of the other guides in this repo: don't copy rules across from them.

## When editing this guide

- A decision has three homes, and all three change together:
  1. the value in `tokens/tokens.css`,
  2. the rule (when and how to use it) in the matching `docs/NN-*.md`,
  3. the reason in a new `decisions/NNNN-short-title.md`.
- Do not invent preferences. If you must fill a gap, label it *(Proposed)* in the doc and
  log it with `Status: proposed` in `decisions/`. Never write it up as if the user decided it.
- There are two variants: dark (`:root`) and light (`:root[data-theme="light"]`). Every
  semantic colour change is made in both.
- After changing any colour or glass token, update `tools/contrast.py` to match, run it,
  and update the contrast tables in `docs/01-color.md`.
- `examples/preview.html` must keep working in both variants: update it when tokens or classes change.
- Remove an open question from a doc once it is answered.
- Keep docs short and prescriptive.

## When applying this guide inside another project

1. Read `docs/00-principles.md` first, then the docs for what you are building.
2. Use tokens (`var(--...)`) for every colour, font size, space, radius, shadow and
   duration. A literal value in app CSS is a bug unless the guide allows it.
3. Prefer semantic tokens (`--color-accent`) over palette tokens (`--palette-pink-500`).
   Only semantic tokens switch with the variant, so palette tokens in app code break light mode.
   Pink or lilac words and icons use `--color-accent-text` / `--color-secondary-text`; the
   plain `--color-accent` is for fills, rings and glows.
4. If the guide is silent, ask the user, then record the answer here.
5. Pink and cream lead. At most two guest pastels per screen. Text on any pastel fill is
   `--color-on-accent` (dark plum), never cream.
6. Cherry red is only for danger. Never use it as decoration or a chart series.
7. Round everything (see `docs/04-components.md`); buttons, chips and toggles are pills.
8. Make it very cute (decisions/0009): motifs, bounce and playful copy are welcome. Errors
   still say clearly what went wrong.

Decisions 0002, 0004, 0008 and 0009 are the user's own. Everything else is proposed until the
user confirms it, so follow it, but raise anything that seems wrong.
