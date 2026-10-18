# Review checklist

Paste the matching section into each axis subagent's prompt, with the diff command, the commit list, and the intent paragraph. Every brief ends: "Give each finding a concrete failing case and a `file:line`. Under 400 words."

Adapted from Matt Pocock's `code-review` (MIT), DietrichGebert's `ponytail-review` and `ponytail-audit` (MIT), and pstack's `interrogate` and `blast-radius` (Lauren Tan, MIT).

## Correctness and risk

- **Bug**: wrong result, crash, missed edge case (empty, zero, last item, rounding, time zones, encodings), callers that disagree with what a function returns, one rule applied differently in two places.
- **Risk**: injection, secrets in code, weak randomness, missing checks on user input, auth gaps, errors swallowed, writes in the wrong order, no transaction around a multi-step write.
- **Scale**: check-then-write races, a query per item, lists or memory that only grow, O(n²) on large input, per-process state that must be shared, the same work done by every process.
- **Missing test**: risky logic (a branch, a parser, money, security, a data write) with no test that fails when it breaks. Ask for one good test, not coverage.

## Spec

Report (a) requirements missing or partial, (b) behavior in the diff nobody asked for, (c) requirements that look implemented but are wrong. Quote the spec line for each.

## Standards

Cite each documented repo rule the diff breaks (file and rule). Then check the smell baseline below. Each smell is a judgment call labelled "possible X", and a documented repo rule that endorses the pattern suppresses it. Skip what tooling already enforces.

- **Mysterious name**: the name does not reveal what it does or holds. Rename it; if no honest name comes, the design is murky.
- **Duplicated code**: one logic shape in more than one hunk or file. Extract it and call it from both.
- **Feature envy**: a method that reaches into another object's data more than its own. Move it onto that data.
- **Data clumps**: the same few fields or parameters travel together. Bundle them into one type.
- **Primitive obsession**: a string or number standing in for a domain concept. Give the concept a small type.
- **Repeated switches**: the same conditional cascade on the same type in several places. Use one map or polymorphism.
- **Shotgun surgery**: one logical change forces edits across many files. Gather what changes together.
- **Divergent change**: one module edited for several unrelated reasons. Split it by reason.
- **Speculative generality**: parameters, hooks, or abstractions for needs nobody has. Inline them.
- **Message chains**: long `a.b().c().d()` navigation. Hide the walk behind one method.
- **Middle man**: a class or function that only delegates. Call the target directly.
- **Refused bequest**: an implementer that ignores most of what it inherits. Use composition.

## Lean

One line per finding: `file:line: tag: what to cut. what replaces it.`

- `delete`: dead code, unused options and config, speculative features. Nothing replaces it.
- `reuse`: a helper that already exists in the codebase. Name its path.
- `stdlib`: hand-rolled code the standard library ships. Name the function.
- `native`: code or a dependency doing what the platform does. Name the feature.
- `yagni`: an interface with one implementation, a factory with one product, a wrapper that only passes calls through.
- `shrink`: the same logic in fewer lines. Show the shorter form.
- `split`: one function doing several unrelated jobs. Split by job, never by line count.

A smoke test or one `assert`-based check is the minimum, never bloat. End with `net: -N lines possible`.

## Blast radius

1. State what the change does, including the part the diff does not spell out.
2. Find the one fact it is safe because of (for example, "this call only drops cache entries that are already dead").
3. Look where grep stops: the source and pinned version of libraries you call, when code runs (callbacks, teardown, background jobs), JSON an API returns, database columns, wire formats, feature flags, code in another language reading the same bytes.
4. Rate each risk by how likely and how costly it is, with `file:line`. List what you checked and cleared separately.
5. Prove the one fact with a script or test that runs the real code, and paste the command and its output.
