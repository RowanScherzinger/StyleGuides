# 0004. The user's accent colour

Date: 2026-11-08
Status: proposed

## Decision
The accent is the user's Windows accent colour. The tokens hold the seven shades Windows derives
from it (defaulting to Windows blue), and apps that can read the system accent overwrite them.
Light mode uses Dark1 for fills and Dark2 for text; dark mode uses Light2 and Light3, as WinUI does.

## Why
A default Windows 11 app uses the system accent; a fixed blue would look out of place for
anyone who picked another colour. Phone Explorer already does this. Using Windows' own shades
(rather than deriving them) keeps contrast where Windows put it; `tools/contrast.py` can check
any palette.

## Affects
`--palette-accent-*` and `--color-accent*` in `tokens/tokens.css`; `docs/01-color.md`,
`docs/07-theming.md`.
