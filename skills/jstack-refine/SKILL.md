---
name: jstack-refine
description: "Refine work before you call it done: review a diff for bugs, risk, spec gaps, bloat, and blast radius, then fix. Use for review, simplify, 'is this ready', or PR review."
---

# Refine

Review like the engineer who will be paged when this breaks. Order of importance: correct, safe, holds under load, tested, fast, lean. The best outcome of a refine is often a shorter diff.

Load `jstack-craft` first; its rules apply to every fix you make.

## 1. Scope

- **Fixed point.** Use what the person named (a SHA, branch, tag, PR number). Otherwise use the merge-base with the default branch, plus uncommitted changes. Confirm it resolves and the diff is not empty: `git diff <base>...HEAD`, `git diff HEAD`, `git log <base>..HEAD --oneline`. For a PR, `gh pr diff <n>` and `gh pr view <n>` (`glab mr diff` and `glab mr view` on GitLab).
- **Intent.** Write one paragraph on what the change is for, from the request, commit messages, and PR body.
- **Spec.** Find the source of truth: the ticket in the commits (fetch it with your tracker tool), a spec file, or the conversation. With none, the spec axis reports "no spec".
- **Standards.** List the repo's documented rules (`AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, linter config). They override the baselines in this skill.

## 2. Review

Cover five axes. For a large diff, give each axis to a read-only subagent on the fast model, all at once, each with the diff command, the intent, and its axis brief from [references/checklist.md](references/checklist.md). For a small diff, work them yourself, one axis at a time.

1. **Correctness and risk.** Wrong results, missed edge cases (empty, zero, last item, rounding, time zones), callers that disagree with a return value, security holes, data loss, races, and work that is fine for one user and wrong for many.
2. **Spec.** Requirements missing or partial, behavior nobody asked for, and requirements implemented wrongly. Quote the spec line for each.
3. **Standards.** Breaks of the repo's documented rules, plus the smell baseline in the checklist as labelled judgment calls.
4. **Lean.** What to cut, with the ponytail tags: `delete`, `stdlib`, `native`, `yagni`, `shrink`, `reuse`. Comments that narrate instead of explaining a non-obvious why. Each item names what replaces the code.
5. **Blast radius.** What the change breaks outside the diff: other callers, persisted data and migrations, wire formats and API consumers, config and feature flags, jobs, and anything another language reads. Find the **one fact** the change is safe because of, and prove it by running real code: a script or test that fails loud if you are wrong.

For UI changes, also run the `jstack-taste` critique on screenshots. For prose in the diff (docs, README, PR text), scan it with `jstack-taste`'s prose tells.

## 3. Verify each finding

- A finding needs a concrete case: "this input or state leads to this wrong result". No case, no finding.
- Before you call code unused, grep the whole tree, tests and config included.
- For a contested design or a high-stakes change, get a second opinion: the same review prompt run on a different model. Findings both raise carry the most weight.

## 4. Judge

You are the lead reviewer, not a neutral aggregator. Put every finding in one bucket, with a one-line reason:

- **Act on**: real correctness, security, or maintainability problems that would block a merge.
- **Consider**: legitimate, but the cost of fixing may outweigh it now.
- **Noted**: valid but not actionable at this stage.
- **Dismissed**: wrong, a nitpick, or missing context.

## 5. Fix and report

When the person asked you to refine, fix every **Act on** item and the cheap **Consider** items, then re-run the tests and the blast-radius proof. When they asked only for a review, change nothing. Fix defects in what the diff does. A missing requirement that needs new behavior (a new caller, screen, or wiring) goes in the report as a question with your recommendation; build it only when the person asks.

Report merge-blocking issues first, each with `file:line`, why it is wrong, and the fix. Then the other buckets, marked optional. Keep the spec and standards findings in separate lists; neither masks the other. Paste the blast-radius proof and its output. End with `net: -N lines` when lean cuts apply, or "Lean already." when there is nothing to cut.

Done when every axis has findings or an explicit "nothing found", every Act-on item is fixed (refine) or listed (review), and the tests pass.
