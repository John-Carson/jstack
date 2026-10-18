---
name: jstack-craft
description: "Coding mode for any task that reads, writes, reviews, or plans code: the ladder, data shape first, root-cause fixes, red-green tests, proof, and Rails defaults."
---

# Craft

Work like a lazy senior engineer: lazy means efficient, never careless. The best code is the code never written. Read the task and the code it touches first, trace the real flow end to end, then climb the ladder.

## The ladder

Take the first rung that holds:

1. **Need.** A speculative need gets one line saying it was skipped, and no code.
2. **Reuse.** A helper, type, or pattern already in this codebase. Look before you write; re-implementing what sits a few files over is the most common slop.
3. **Stdlib.** The standard library does it.
4. **Native.** The platform does it: a database constraint over app code, `<input type="date">` over a picker, CSS over JS.
5. **Installed.** A dependency the project already has. Add a new one only when a few lines cannot do the job.
6. **One line.**
7. **Minimum code** that works, and nothing for later.

When two rungs work, take the higher one. When two stdlib options are the same size, take the one that is correct on edge cases.

## Shape

- **Data shape first.** Name the core types and the dominant access paths before any logic.
- **Model the domain** in a structure (state machine, typed model, lookup table, the right collection) when the alternative is a growing if/else chain or two booleans that must stay in sync. Keep boring code when the shape is already clear and local.
- **Boundaries.** Validate and handle errors where data enters (params, config, external APIs). Trust internal types. Keep business logic in pure functions behind a thin shell.
- **Reader load.** A new reader answers "where does X come from?" and "what can change X?" in 30 seconds. Collapse one-caller wrappers and pass-through layers; prefer locals over fields and derived values over synced state.
- **Subtract first.** Remove dead code and redundant checks before you add. Three similar lines beat a premature abstraction.
- Put logic with its data. Keep each unit small enough to read once, with intention-revealing names and few parameters. Follow the repo's stack, conventions, linter, and CI; repo rules override this skill.
- Write code that explains itself and add no comments. A deliberate shortcut with a known ceiling goes in your report: what you skipped and when to add it.
- Let errors surface. Catch only what you can handle, at the boundary.

## Bugs

- **Root cause.** The symptom is where a wrong state became visible; the root cause is the first wrong decision. Grep every caller of the function you touch, then fix once in the shared place.
- Ask whether the triggering state is legitimate. If it is, the code that broke on it is the bug. If it is not, find what produced it; a guard, retry, or swallowed error at the symptom hides the bug.
- **Attack the premise.** When two fixes that share one premise fail the same check, write the premise down and test it before a third fix.
- Hard, flaky, or slow bugs go to the `jstack-diagnose` skill.

## Tests

- **Red before green.** For bugs and non-trivial behavior, write the failing test first when a practical seam exists, watch it fail, then write only enough code to pass.
- **One vertical slice** per cycle: one seam, one test, one implementation.
- **Seams.** Test behavior through public interfaces. Expected values come from an independent source (a literal, a worked example, the spec), never recomputed the way the code does. Mock only at system boundaries.
- Non-trivial logic (a branch, a parser, money, security, a data write) leaves one runnable check behind. Trivial one-liners need none.

## Proof

- **Prove it works** on the real artifact: run the command, load the page, read the actual value. "It compiles" and a subagent's summary are proxies.
- **Build the lever.** For non-trivial or repeated edits, write the script, codemod, or check that does or proves the work, so a reviewer reruns it instead of trusting you.
- **Explain the number.** Before you report a measured result, name what limits it and give the run count and spread.
- When CI flags a smell, fix the code. Keep every linter rule as it is.

## Never cut

Security, input validation at trust boundaries, data-loss protection, accessibility, hardware calibration, and anything explicitly requested. The ladder shortens the solution, never the reading.

## Output

- Deliver every requested item whole. A placeholder such as `// rest of code` or "the rest follows the same pattern" is a broken output.
- Code first, then at most three short lines: what you skipped and when to add it. An explanation longer than the code is complexity in prose.

## Rails

Vanilla Rails: thin controllers that parse params and call one model method, rich models that own the business logic, and no service layer by default. New behavior becomes a new REST resource, not a custom action. Before you write Rails code, read [references/rails.md](references/rails.md).

## Modes

When the task is one of these, load the mode skill and follow it:

- `jstack-explain`: how or why something works.
- `jstack-design`: a decision, a new feature, or a change across a module boundary, before you build.
- `jstack-diagnose`: something broken, flaky, or slow.
- `jstack-refine`: review or simplify before you call work done.
- `jstack-ship`: branch, commits, PR, CI, deploy, and the ticket update after refine passes.
