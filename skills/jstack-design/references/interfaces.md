# Interfaces

Adapted from Matt Pocock's `codebase-design` (MIT) and pstack's `architect` red flags (Lauren Tan, MIT).

## Vocabulary

Use these terms exactly.

- **Module**: anything with an interface and an implementation, at any scale: a function, a class, a package, a slice across tiers.
- **Interface**: everything a caller must know to use the module correctly: the signature, plus invariants, ordering rules, error modes, required configuration, and performance characteristics.
- **Implementation**: the code inside the module.
- **Depth**: behavior a caller can use per unit of interface it must learn. A **deep** module hides a lot behind a small interface; a **shallow** one has an interface nearly as complex as its implementation.
- **Seam**: the place where behavior can change without editing in that place; where the interface lives and where tests attach.
- **Adapter**: a concrete thing that fills a seam (a Postgres repository, an in-memory fake).
- **Leverage**: what callers gain from depth. One implementation pays back across every call site and test.
- **Locality**: what maintainers gain from depth. Change, bugs, and verification concentrate in one place.

## Principles

- **Depth belongs to the interface.** A deep module can be built from small internal parts; they are not part of its interface.
- **The deletion test.** Imagine deleting the module. If the complexity vanishes, it was a pass-through. If it reappears in every caller, it earns its place.
- **The interface is the test surface.** Callers and tests cross the same seam. Wanting to test past the interface means the module is the wrong shape.
- **One adapter is a hypothetical seam; two adapters is a real one.** Add a seam only when something varies across it.
- **Accept dependencies, return results.** Pass collaborators in rather than constructing them inside, and return values rather than mutating shared state.
- When choosing between interfaces, ask: can I reduce the number of methods, simplify the parameters, or hide more inside?

## Red flags

Screen every candidate. A red flag is a reason to revise or reject the shape.

- **Shallow module.** Callers coordinate several methods to finish one operation, public options expose internal stages, or learning the interface does not spare the caller from learning the implementation. A deep module is not a deep call chain: the chain scatters understanding, the module concentrates it.
- **Information leakage.** One internal decision (a representation, a policy, a wire format) appears in several modules, so changing it needs coordinated edits. Re-exported transport or storage types are leakage; parse external data into domain types behind the interface.
- **Temporal decomposition.** Modules named for execution order (load, validate, transform, save) that repeat one representation and its invariants across each step. Group code by the knowledge it owns instead.
- **Pass-through method.** A method that forwards the same arguments to another method of the same shape. Remove it, or move the responsibility to the module that can finish the operation.
