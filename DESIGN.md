# juns.page Design Notes

The shared visual language for `juns.page`. Follow it when adding or changing pages. Reference implementations:

- `index.html`: the home page (wordmark + one-line links)
- `lab/index.html`: the card list, covers and filters

Copy tokens and rules from those files. There is no shared CSS file yet. Extract one only once a third page needs the same components.

## 1. Principles

- Quiet and typographic. Use the neutral palette, one font family and generous whitespace. No hero images, background textures, emoji icons, decorative illustration or gratuitous animation.
- Restraint over decoration. Each element gets one emphasis signal (weight **or** colour **or** underline). Don't stack several.
- Work in light and dark mode, follow the system (`prefers-color-scheme`) and offer no manual theme toggle.
- Ship static pages with zero dependencies: plain HTML, CSS and vanilla JS, no build step and no web fonts.
- Mobile first. Check 375 px and 390 px phones, 820 px tablet and 1280 px desktop for no horizontal scroll.

## 2. Interface layer (tokens, type, layout)

### Colour tokens

| Token | Light | Dark | Use |
|---|---|---|---|
| `--canvas` | `#f6f6f3` | `#11110f` | page background |
| `--surface` | `#fdfdfb` | `#1c1c1a` | card background |
| `--ink` | `#171716` | `#f3f2ec` | primary text, active states |
| `--muted` | `#6e6e68` | `#b4b3ac` | secondary text, meta |
| `--rule` | `#d9d9d2` | `#3a3a35` | borders, dividers |
| `--rule-strong` | `#acaca2` | `#66665d` | hover borders, primary pill |
| `--accent` | `#2f7d4f` | `#7fd1a0` | the **only** accent: "daily use / live" states |
| `--accent-soft` | `rgba(47,125,79,.08)` | `rgba(127,209,160,.1)` | accent chip background |
| `--card-shadow` | `0 6px 20px rgba(0,0,0,.06)` | `none` | card hover only |

Colour beyond these tokens appears only inside covers (section 4).

### Type

- Body font: `ui-rounded, "Avenir Next", Avenir, "SF Pro Rounded", system-ui, sans-serif`.
- Meta and numbers: `ui-monospace, SFMono-Regular, Menlo, monospace`, small (0.75–0.82 rem), `--muted`.
- Page title or wordmark: `clamp(3rem, 11vw, 5.6rem)`, weight 650, `letter-spacing: -0.075em`, `line-height: 0.9`.
- Section h2: 1 rem / 650, `--ink`. Card h3: 1.05 rem / 600.
- Body: line-height 1.55–1.6, with `text-wrap: pretty` and `overflow-wrap: anywhere`. Use `font-variant-numeric: tabular-nums` for dates and counts.

### Layout

- Home: a single left-aligned column, `min(100%, 38rem)`, centred on the viewport.
- Content pages: `max-width: 64rem`. Keep the title and intro to ≤ 40 rem. Body padding is `1.5rem 1.25rem 3rem` on phones and `2rem 1.5rem 4rem` from 600 px.
- Top nav: the "Juns" text link (back to `/`) on the left, utility controls (such as the language toggle) on the right.
- Footer: a hairline `--rule` top border and a muted line, e.g. "Updated YYYY-MM-DD".

### Controls

- Buttons and chips are pill-shaped (`border-radius: 2rem`) with a 1 px `--rule` border and transparent fill.
  - Active state: `--ink` fill with `--canvas` text.
  - Touch targets: ≥ 44 px for standalone buttons, ≥ 36 px for filter chips.
- A filter chip carries its count in a `.count` span at reduced opacity. Chips wrap instead of scrolling sideways. Keep filter state in the URL (`?f=writing`) so it can be shared.
- Bilingual pages:
  - `?lang=en|zh` plus `localStorage` (`lab-lang`).
  - The toggle shows the *other* language's name ("EN" / "中文").
  - Swap all copy from a single strings table.
- Text links: underline with `text-underline-offset: 0.2em`. On hover, change one thing only (colour or underline strength).
- Focus: `outline: 2px solid var(--ink); outline-offset: 4px`, on every interactive element.

### Motion

- Durations are 160 ms for UI and 400 ms for covers, with `ease`. Movement is limited to small translations (2–3 px) or a ≤ 6 % scale.
- Apply hover effects only under `@media (hover: hover) and (pointer: fine)`.
- `prefers-reduced-motion: reduce` removes every transition and transform.

### Home → section entry pattern

Sections are linked from the home page as one sentence-style link under the tagline, not as a nav bar or cards:

```
A small corner of the internet.
Things I've made with AI → Lab        ← whole line clickable, "Lab" bold + underline
19 items · updated 2026-10-23         ← mono, muted, read live from the section's JSON; hidden if fetch fails
```

Add a sibling line for each new section. Once there are three or more, switch to a single row such as `Lab · Writing · GitHub`.

## 3. Cards

Use cards for any list of things a visitor can open.

- Container:
  - `--surface` background, 1 px `--rule` border, `border-radius: 14px`, padding `1.1rem 1.2rem`.
  - Flex column, so the footer is pinned with `margin-top: auto` and footers align across a row.
- The whole card is clickable.
  - The title `<a class="card-link">` gets a stretched `::after { position:absolute; inset:0 }`.
  - Secondary links are `.pill` elements with `position: relative; z-index: 1` so they stay independently clickable.
  - Focus ring goes on the card via `.card:has(.card-link:focus-visible)`.
- Content order: optional cover, meta row, title, summary, bottom row.
  - **Meta row:** type · status chip · destination host. Small and `--muted`.
  - **Summary:** `--muted`, 0.92 rem, clamped to 3 lines in dense grids.
  - **Bottom row:** date on the left, pill links on the right. Each pill has an `↗` arrow and the primary pill uses a `--rule-strong` border.
- Status chips, which are always small and never loud:

  | Status | Style |
  |---|---|
  | daily use / live | accent text on `--accent-soft` |
  | default (works, merged, snapshot) | `--canvas` fill, `--ink` text |
  | experimental | transparent with a 1 px dashed `--rule-strong` outline |
  | archived | 70 % opacity |

  Articles have no status chip.
- Hover (fine pointers only): lift 2 px, border to `--rule-strong`, `--card-shadow`, arrow nudges ↗ 2 px. Press: `scale(.99)`.
- Grid:
  - One column on phones.
  - From 640 px, featured items use 2 columns and the rest use `repeat(auto-fill, minmax(16rem, 1fr))`.

## 4. Covers (header art) and how to generate them

Article-type cards get a CSS-only "glow" cover. Never use page screenshots or stock images. Screenshots were tried on 2026-10-24 and rejected as not good-looking: noisy, low-contrast, and inconsistent between cards.

**Data:** each item supplies two fields in its JSON:

```json
{ "mark": "Penguins", "hue": 160 }
```

**Choosing `mark`:**
- One short English word or tag (≤ 10 characters, e.g. `AirPods`, `Podcast`, `HKG · 8h`).
- Name the subject, not the category.
- Use English even on the Chinese UI. It is a visual label, so mark the cover `aria-hidden="true"`.

**Choosing `hue`** (0–360, HSL):
- Pick a hue that evokes the subject: sea or penguins → 160–190, food → 10–35, Apple/tech → 205–235, audio/podcast → 275, WeChat → 150, Hong Kong night → 340.
- Make sure neighbouring cards differ by ≥ 20°.
- Avoid low-saturation browns. Hues around 30–40 can look muddy in dark mode, so check them.

**Rendering rules** (see `.cover` in `lab/index.html`):
- The cover sits flush with the card top (negative margins), at `aspect-ratio: 3 / 1` with `border-radius: 13px 13px 0 0`.
- **Light mode:**
  - Base `hsl(h 45% 94%)`, mark colour `hsl(h 45% 26%)`.
  - A `::before` layer at `inset:-30%` with `filter: blur(18px)` holds two radial glows. The main one is `hsl(h 85% 72% / .75)` at `(--x, --y)`. The secondary is `hsl(h+40 80% 80% / .4)` at `(100% − --x, 55%)`.
- **Dark mode:** base `hsl(h 30% 13%)`, mark `hsl(h 70% 86%)`, and only the main glow, at `hsl(h 70% 52% / .5)`.
- **Glow position:** derived from the id so the cards don't look templated and stay stable between builds. With `seed = sum of id char codes`:
  - `--x = 60 + seed % 30` %
  - `--y = 10 + (seed × 7) % 40` %
- **Mark:** bottom-left, 1.9 rem, weight 650, `letter-spacing: -0.04em`.
- **Hover:** the glow drifts with `translate(-4%, 3%) scale(1.06)` over 400 ms.

Tool and project cards stay cover-less and compact, so covers signal "reading material".

## 5. Checklist before shipping a page

1. Uses the tokens above. Only the tokens and cover hues introduce colour.
2. Works in light and dark mode at 375, 390, 820 and 1280 px, with no horizontal overflow and no console errors.
3. Whole-card click, pill click, keyboard focus and reduced-motion behaviour all verified.
4. Tested locally or on the LAN first (see `AGENTS.md`). Push only once it's verified.
