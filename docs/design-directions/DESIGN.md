# Locked design: direction C (warm)

Approved by Ravi on 2026-11-21. The visual design is locked. **The copy is not approved.** All text in the mockups is placeholder, and the positioning and wording will be decided separately.

Reference implementation: `c/style.css`, plus the page structure produced by `build.py` (`c_*` and `a_*` templates) and `shared/menu.js`.

## Feedback that shaped it

- A was rejected because its fonts were too obscure.
- B was rejected because its rounded cards looked cartoonish and its bright red was jarring.
- The first plain version of C was rejected as too sterile. The current C adds warmth through parchment bands, brass highlights, per-stage accents and a hero illustration.

## Tokens

| Role | Token | Value |
|---|---|---|
| Page background (warm white) | `--paper` | `#fbfaf7` |
| Warm band (parchment) | `--parchment` | `#f2ebdd` |
| Text and dark bands (charcoal) | `--ink` | `#1d1e21` |
| Secondary text | `--grey` | `#5e5c57` |
| Hairlines | `--hair` | `#e3e0d9` (on parchment: `#ddd2bd`) |
| Selected-card tint | `--tint` | `#f3f1ec` |
| Action red (oxblood) | `--red` / `--red-dark` | `#8c1d26` / `#721720` |
| Brass highlight | `--gold` | `#a8894a`, tint `rgba(168,137,74,.26)` |

Type: **Source Serif 4** (500) for headings and **Inter** for everything else, both from Google Fonts. Labels are Inter at 11–12px, uppercase, with .06em tracking. Do not add a third face.

## Rules

- Red is only for actions: primary buttons, plus one red item in the hero sheet. Never use it for large fills.
- Brass is only for small accents: eyebrow labels, step numerals, the selection dot, the headline marker highlight, and the short rule under the footer line.
- Card corners are 4–6px with 1px borders and no glow. Pills are not used.
- Section rhythm alternates warm white, parchment and charcoal. Never put two charcoal bands next to each other.
- Layout: a 220px label rail on the left and content on the right. Desktop content is at most 1240px wide, and it collapses to one column under 980px.
- The services menu has three columns, one per stage, each with a 3px accent: brass for Diagnostic, oxblood for Prescription, charcoal for Operation. A selected card takes its stage's color. A sticky charcoal tray holds the count and the CTA.
- The hero visual is a CSS-drawn document (a checklist sheet), slightly rotated and captioned as an illustration. Use no stock photos and no headshot.
- The intake is two steps: a form, then scheduling. It has a numbered progress rail.
- The primary CTA appears on every page. The compliance line sits quietly in the footer and on Services.
