# 0009. Stopped state is a flat bar, not a hollow square

Date: 2026-10-17
Status: proposed (the user rejected the square; the bar is Claude's replacement). Partly supersedes 0004.

## Decision
The stopped / idle status shape is a short flat bar ▬ in `--color-status-idle`, dimmed,
like an unlit LED segment. The full set is now ◆ ◇ ▬ ▲ ■.

## Why
User feedback on Jarvis: "The empty grey squares look like failed image loads." A small
grey outlined square is exactly what a browser draws for a broken image, so a dashboard of
stopped services looked broken rather than calm.

A flat bar reads as "off" and is still a distinct shape from the other four, so state stays
readable without colour vision. Rejected: a hollow circle (circles already mean info) and
a dimmer hollow square (still reads as a missing image).

## Affects
`docs/01-color.md`, `docs/06-iconography.md`, `examples/preview.html`.
