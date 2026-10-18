---
name: jstack-diagnose
description: "Diagnose broken, flaky, or slow behavior: build a red feedback loop before any theory, then fix the root cause. Use when something fails, throws, regresses, hangs, or is slow."
---

# Diagnose

A bug with a **tight** feedback loop gets found; bisection, hypotheses, and instrumentation all just consume that loop. Without one, reading code is guessing. Work the phases in order.

Load `jstack-craft` first; its rules apply to every edit and test you write here.

Redact every secret you show: write `<REDACTED>` in its place, keep credentials in environment variables, and quote only the log lines that carry the signal.

## 1. Build the loop

Spend most of your effort here. Build a command that goes **red** on this exact bug, trying these in order:

1. A failing test at whatever seam reaches the bug.
2. A curl or HTTP script against a running dev server.
3. A CLI run with a fixture input, diffed against a known-good output.
4. A headless browser script that drives the UI and asserts on the DOM, console, or network.
5. A replay of a captured request, payload, or event log through the code path.
6. A throwaway harness that runs the smallest part of the system that reaches the bug.
7. A property or fuzz loop for "sometimes wrong" output.
8. A bisection script for "it worked at version X", run with `git bisect run`.
9. A differential run: the same input through the old and new version, outputs diffed.
10. A human in the loop, as a last resort, driven by [scripts/hitl-loop.template.sh](scripts/hitl-loop.template.sh) so the loop stays structured.

Then tighten it: faster (narrow the scope, cache setup), sharper (assert the exact symptom, not "did not crash"), deterministic (pin time, seed randomness, isolate the filesystem and network). For a flaky bug, raise the reproduction rate (loop it 100 times, add load, narrow timing windows) until it is high enough to debug.

If you cannot build a loop, stop and say so. List what you tried, and ask for access to an environment that reproduces it, a redacted artifact (log, HAR file, recording with timestamps), or permission to add temporary instrumentation.

Done when you can name **one command** you have already run that drives the real code path, asserts the user's exact symptom, gives the same verdict each run, finishes in seconds, and runs unattended.

## 2. Reproduce and minimize

Run the loop and watch it go red with the failure the user described, not a nearby one. Then cut inputs, callers, config, data, and steps one at a time, re-running after each cut. Done when every remaining element is load-bearing: removing any one turns the loop green.

## 3. Hypothesize

Write three to five ranked hypotheses before you test any. Each states its prediction: "If X is the cause, changing Y makes the bug disappear." A hypothesis without a prediction gets sharpened or dropped. Show the ranked list to the user, who may re-rank it at once, and continue with your ranking if they are away.

When two fixes on one premise have failed, write that premise down and test it directly before the next fix.

## 4. Instrument

Each probe tests one prediction; change one variable at a time. Prefer a debugger or REPL, then targeted logs at the boundaries that separate hypotheses. Tag every debug log with a unique prefix such as `[DEBUG-a4f2]` so cleanup is one grep.

For slowness, measure instead of logging: take a baseline with a timing harness, profiler, or query plan, then bisect. Report each number with its run count, spread, and what limits it.

## 5. Fix at the root

Ask whether the state that triggered the symptom is legitimate. If it is, the code that broke on it is the bug. If it is not, trace back to what produced it; a guard, retry, or clamp at the symptom hides the fault. When something fails only after a restart, suspect persisted state first: caches, lock files, config, serialized data. Find every place with the same fault and fix them all.

Write the regression test before the fix, at a seam that exercises the real bug pattern. Watch it fail, apply the fix, watch it pass, then re-run the original un-minimized loop. If no correct seam exists, that is a finding; report it.

## 6. Clean up

Done when all of these hold:

- The original loop is green.
- The regression test passes, or the missing seam is reported.
- `grep` finds no `[DEBUG-` prefix.
- Throwaway harnesses are deleted.
- The commit message states the hypothesis that proved correct.
- If the deciding fact took a deep dig, you proposed the cheap, always-on signal (a log line, a metric, a check) that would have shown it at once.
