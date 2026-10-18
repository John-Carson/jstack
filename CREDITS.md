# Credits

jstack merges and rewrites material from four MIT-licensed collections. Each pin is the upstream commit last reviewed. Each project's copyright notice is below. Each project uses the same MIT permission notice as [LICENSE](LICENSE).

| Source | Pin | Copyright | Used in |
| --- | --- | --- | --- |
| [mattpocock/skills](https://github.com/mattpocock/skills) | `49dd158` | Copyright (c) 2026 Matt Pocock | jstack-design (grilling, domain-modeling, codebase-design), jstack-diagnose (diagnosing-bugs, `hitl-loop.template.sh`), jstack-craft (tdd), jstack-refine (code-review) |
| [cursor/plugins pstack](https://github.com/cursor/plugins/tree/main/pstack) | `0317eb8` | Copyright (c) 2026 Lauren Tan | jstack-craft (principles), jstack-explain (how, why, teach), jstack-design (architect red flags), jstack-refine (interrogate, blast-radius), jstack-taste (unslop) |
| [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | `16352ac` | Copyright (c) 2026 DietrichGebert | jstack-craft (the ladder), jstack-refine (ponytail-review, ponytail-audit) |
| [leonxlnx/taste-skill](https://github.com/leonxlnx/taste-skill) | `f624f37` | Copyright (c) 2026 Leonxlnx | jstack-taste (house rules, critique rubric, redesign audit) |

`jstack-craft/references/rails.md` restates the approach in 37signals' [Vanilla Rails is plenty](https://dev.37signals.com/vanilla-rails-is-plenty/) in new words.

## Updating from upstream

To pick up upstream changes, read `git log <pin>..HEAD` in each source repo, fold in what earns its place, and move the pin. Not included on purpose: taste-skill's `draw.mjs`, `inspect.mjs`, and direction library, which need Node 22 and Chrome and are built for marketing pages.
