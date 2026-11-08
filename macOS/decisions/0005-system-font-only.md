# 0005. The system font, never shipped

Date: 2026-11-08
Status: proposed

## Decision
SF Pro and SF Mono through `-apple-system` / `system-ui` / `ui-monospace`, never as font files.
The macOS text styles (26, 22, 17, 15, 13, 12, 11, 10) with Apple's weights and tracking.

## Why
They are the Mac's own fonts and ramp, and they're installed on every Mac. Apple licenses the
SF fonts for Apple-platform app design only, so they can't go in a public repo, a web page or
an Electron app's bundle. Off a Mac the stack falls back to Helvetica Neue or Arial, which is
acceptable for a guide that is about the Mac.

## Affects
`--font-*`, `--text-*`, `--leading-*`, `--tracking-*`, `--weight-*` in `tokens/tokens.css`; `docs/02-typography.md`.
