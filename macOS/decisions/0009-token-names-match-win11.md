# 0009. Token names match the Win11 guide

Date: 2026-11-08
Status: proposed

## Decision
Where a role is the same on both platforms, the semantic token has the same name as in
`Win11/`: `--color-bg`, `--color-bg-elevated`, `--color-surface`, `--color-surface-raised`,
`--color-control`, `--color-border*`, `--color-text*`, `--color-accent*`, `--color-on-accent`,
`--color-status-*`, the `*-fill` tokens, `--font-*`, `--space-*`, `--radius-control`,
`--radius-overlay`, `--duration-normal`. Tokens for things only one platform has keep their
own names (`--color-content`, `--color-sidebar`, `--text-headline`). One exception:
`--color-scrim` is a dark dimming layer here (the HIG's), so chip text over it uses
`--color-on-scrim`, where Win11 uses `--color-text`.

## Why
The user asked for a guide to partner Win11. An app that offers both looks can then switch
by loading the other `tokens.css`. Only the component classes and behaviour (button order,
capitalisation) differ. This shares names, not rules: each guide's values and rules come from
its own platform.

## Affects
`tokens/tokens.css`; `docs/00-principles.md`.
