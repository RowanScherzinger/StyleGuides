# 0001. Tokens mirror WinUI

Date: 2026-11-08
Status: proposed

## Decision
Every colour comes from WinUI's `Common_themeresources_any.xaml` (microsoft/microsoft-ui-xaml),
with the WinUI resource name in a comment beside it. Type, corners, spacing and motion come from
the WinUI control defaults and Microsoft's Windows design guidance. Tokens are CSS custom
properties in three layers (palette, semantic, scales), like the other guides.

## Why
The goal is to look like a default Windows 11 app (0002), so the values should be Microsoft's,
not approximations. Naming the source resource makes them easy to re-copy when WinUI changes,
and lets a native app map them one to one. Inventing a "Windows-like" palette was rejected: it
would drift from the real thing.

## Affects
All of `tokens/tokens.css`; `docs/01-color.md`.
