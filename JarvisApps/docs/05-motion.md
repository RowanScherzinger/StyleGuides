# Motion

Tokens: `--duration-*`, `--ease-*`, `--stagger`, `--loop-*`. Keyframes are in `css/hud.css`.

Kinetic, but every movement has a reason: it shows a change, confirms an action, or
signals that the system is alive.

## Tokens

| Token | Value | Used for |
|---|---|---|
| `--duration-instant` | 80ms | Press feedback |
| `--duration-fast` | 120ms | Hover colour changes |
| `--duration-normal` | 220ms | Bracket lock, toggles, menus |
| `--duration-slow` | 400ms | Panel enter, modals |
| `--duration-boot` | 600ms | Boot flicker |
| `--stagger` | 30ms | Delay between items in a reveal |
| `--ease-out-expo` | `cubic-bezier(0.16, 1, 0.3, 1)` | The house curve: fast start, precise settle |
| `--ease-exit` | `cubic-bezier(0.7, 0, 0.84, 0)` | Leaving |
| `--loop-pulse` | 1.6s | Pending states |
| `--loop-scan` | 5s | Radar sweeps |
| `--loop-ring` | 30s | Decorative rotating rings |

## Signature motions

| Motion | Class / keyframe | Where |
|---|---|---|
| **Boot**: a quick flicker to full opacity | `.hud-boot` | Panels on first load, modals |
| **Staggered reveal** | `.hud-enter` with `style="--i: n"` | Lists and panel grids on load |
| **Bracket lock**: corners scale in from 115% | built into `.hud-corner` | Hover and focus on panels |
| **Line draw**: strokes draw on | `draw-line` with `--path-length` | Charts and rings on first render |
| **Scan sweep** | `.hud-scan-line` | Radar or "searching" states |
| **Ring spin** | `.hud-ring-spin` | Ambient decoration only |
| **Value settle**: numbers count to the new value over `--duration-slow` | JS | Live readouts *(Proposed)* |

## Budget

These rules come from the film designers, who tuned how many elements animate at once:

- At most **one ambient loop** (ring, scan) per screen region, and at most two on screen.
- **Blinking or pulsing is for state only**: pending pulses, and an error pulses once.
  Never pulse decoration.
- Boot animations play on the first load only, never on every data refresh.
- Live data updates do not move the layout. Values change in place.

## Reduced motion

`tokens.css` handles `prefers-reduced-motion: reduce` globally. Durations go to 0 and
loops stop after one cycle. Don't override this.
