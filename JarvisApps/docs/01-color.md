# Colour

Tokens: `--palette-*` (raw) and `--color-*` (semantic) in `tokens/tokens.css`.
Components use semantic tokens only. Dark only.

## Palette

Warm, metallic, dark. Base values come from Desktop-Widgets.

| Family | Key value | Ramp |
|---|---|---|
| Black / off-white | `#060404` / `#ded2c6` | `--palette-neutral-950` to `-50`, all warm-tinted |
| Copper | `#b87333` | `--palette-copper-700` to `-300` |
| Gold | `#d4a017` | `--palette-gold-700` to `-300` |
| Silver | `#c0c0c0` | `--palette-silver-600` to `-300` |
| Red | deep `#8b0000`, crimson `#dc143c` | `--palette-red-800` to `-400` |
| Ember | `#f07a2a` | warning only *(Proposed)* |
| Chartreuse | `#a3d21f` | status lights only: OK / running |
| Arc blue | `#6ec6ff` | high-contrast accents only |

The warm metals are the identity. Chartreuse and blue are **guests**: allowed for status
lights and small high-contrast marks (decisions/0007), never for surfaces, borders,
buttons or large areas.

## Roles *(Proposed)*

| Metal | Role | Tokens |
|---|---|---|
| **Copper** | **Frame.** Hairlines, brackets, headings, primary buttons. The structure. | `--color-accent`, `--color-border*` |
| **Gold** | **Signal.** Live values, focus, selection. Where the eye should land. | `--color-highlight`, `--color-focus-ring` |
| **Silver** | **Neutral data.** Secondary series, idle state. | `--color-status-idle` |
| **Chartreuse** | **All clear.** The OK / running status light. | `--color-status-ok` |
| **Arc blue** | **Cut-through.** Info status, crosshairs, a selected point, tiny marks that must pop against copper and gold. | `--color-info`, `--color-contrast-accent` |
| **Red** | **Alarm.** Errors, destructive actions, critical thresholds. Nothing else. | `--color-status-danger`, `--color-danger-*` |
| **Off-white** | **Text.** | `--color-text*` |
| **Black** | **Field.** Background and glass tint. | `--color-bg`, `--color-surface*` |

Why red isn't the accent, even though it was listed first: when red marks everything
important, a real alarm stops standing out. Keeping red for danger makes failures jump out.
To push the overall look redder, use deep-red fills and a red app mark, not red buttons.

## Status

Service state appears in most of these apps. Each state gets one colour **and** one shape,
so it reads at a glance and without colour vision.

| State | Colour | Shape | Motion |
|---|---|---|---|
| Running / OK | `--color-status-ok` (chartreuse) | Filled diamond ◆ | Steady |
| Starting / pending | `--color-status-pending` (pale gold) | Hollow diamond ◇ | Slow pulse |
| Stopped / idle | `--color-status-idle` (grey silver) | Hollow square □ | None, dimmed |
| Warning | `--color-status-warning` (ember) | Triangle ▲ | None |
| Error / failed | `--color-status-danger` (crimson) | Filled square ■ | One pulse on entry, then steady |
| Info | `--color-info` (arc blue) | Circle ● | None |

## Contrast (measured)

Measured against WCAG with the glass composited (`python tools/contrast.py`):

| Text | On app glass | On overlay glass over **white** wallpaper |
|---|---|---|
| `--color-text` | 13.4 | 9.4 |
| `--color-text-muted` | 7.9 | 5.5 |
| `--color-highlight` (gold) | 8.4 | 5.8 |
| `--color-accent` (copper) | 5.3 | 3.7 (large text and lines only) |
| `--color-status-warning` | 7.2 | 5.0 |
| `--color-danger-text` | 5.5 | 3.8 (large or bold only) |
| `--color-status-ok` (chartreuse) | 11.2 | 7.8 |
| `--color-info` (arc blue) | 10.6 | 7.4 |
| `--color-text-dim` | 4.7 | 3.3 (not allowed on overlay) |
| crimson `#dc143c` | 4.0 | n/a, icons and large text only |

## Rules

- Small red text uses `--color-danger-text` (`#f0485f`), not crimson. Crimson is too dark at small sizes.
- Fills are translucent tints (`--color-accent-soft`, `--color-highlight-soft`,
  `--color-danger-fill`), not solid blocks. The one exception is primary buttons, which are solid copper.
- Gradients are allowed only for light effects: scan sweeps, vignettes, fading a line into
  the background. Never on text or buttons.
- Text on a solid copper or gold fill uses `--color-on-accent` (black).
