# Voice and copy

## Tone

Terse and technical, like an instrument panel. Labels are nouns, buttons are verbs.
*(Proposed, and whether Jarvis gets a personality is still open.)*

## Conventions

| Thing | Rule |
|---|---|
| Labels and headings | UPPERCASE in `--font-display`, short: `GPU LOAD`, `QUEUE`, `LAST SYNC` |
| Buttons | Verb first: `START`, `STOP SERVICE`, `ADD TO BASKET` |
| Prose and messages | Sentence case |
| Numbers | Value and unit split: the value in `.hud-value`, the unit in `.hud-unit`. Keep fixed decimals for live values (`72.0`, not `72` then `72.5`). |
| Spelling | TBD (British / American) |
| Dates | TBD |
| Times | TBD (24h / 12h) |

## Messages

- Errors: what failed, then what to do. `Ollama didn't respond on :11434. Check the service is running.`
- Empty states: one line saying what will appear here, plus the action to start it.
- Destructive confirmations: name the thing and the consequence. The confirm button is a Danger button.

## Open questions

- [ ] British or American spelling?
- [ ] 24-hour clock? Date format (for example `17 OCT 2026` or `2026-10-17`)?
- [ ] Should Jarvis have a personality (a JARVIS-style voice in messages), or stay neutral?
