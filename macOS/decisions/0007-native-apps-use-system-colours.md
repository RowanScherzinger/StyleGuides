# 0007. Native apps use the system colours by name

Date: 2026-11-08
Status: proposed

## Decision
Native Mac apps (AppKit, SwiftUI) don't copy these tokens. They use `NSColor` and SwiftUI
system colours by name, the system font and standard controls. The tokens are for web and
Electron apps, and each one names the AppKit colour it stands for.

## Why
On the Mac the system colours adapt to appearance, accent, Increase Contrast, Reduce
Transparency, vibrancy and desktop tinting by themselves; copied hex values would break all of
that. The HIG says not to hard-code system colour values. Win11 mirrors tokens by hand only
because WinForms has no such colours.

## Affects
`docs/07-theming.md`.
