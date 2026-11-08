# 0005. Segoe UI Variable and the Windows type ramp

Date: 2026-11-08
Status: proposed

## Decision
Segoe UI Variable (Text, Small and Display optical sizes), falling back to Segoe UI; Cascadia
Mono for code; the Windows type ramp (12, 14, 18, 20, 28, 40, 68) with regular and semibold only.

## Why
These are Windows 11's own fonts and ramp, installed on every Windows 11 PC, so nothing needs
loading. Segoe UI is the Windows 10 equivalent. Off Windows the stack falls to `system-ui`,
which is acceptable for a guide that is about Windows.

## Affects
`--font-*`, `--text-*`, `--leading-*`, `--weight-*` in `tokens/tokens.css`; `docs/02-typography.md`.
