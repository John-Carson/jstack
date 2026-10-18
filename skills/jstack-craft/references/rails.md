# Vanilla Rails

Rails already gives you the layers you need. Reach for what the framework ships before you add a pattern. Background: [Vanilla Rails is plenty](https://dev.37signals.com/vanilla-rails-is-plenty/).

## Where code goes

- **Controllers** parse params, call one model method, and render or redirect. More than about ten lines in an action is a sign that domain logic leaked in.
- **Models** own the business logic: Active Record models for persisted things, plain Ruby or `ActiveModel::Model` objects for things that are not persisted (a signup form, a report).
- **Concerns** hold behavior shared across models, named for the capability (`Closeable`, `Event::Relaying`).
- **Delegated types** model "is-a" relations that share identity (a `Recording` that is a `Message` or a `Comment`).
- **Jobs** are shallow. They call one model method and hold no logic.
- **A separate object** is fine when it coordinates several models in one transaction, wraps an external API, or runs a multi-step workflow that no single model owns. Name it for the domain thing (`Signup`, `Account::Import`), not for the action (`CreateAccountService`).

## Routes

Model endpoints as REST resources. New behavior becomes a new resource, not a custom action:

```ruby
resources :cards do
  resource :closure
end
```

## Style

- Prefer an expanded `if`/`else` that returns from both branches over a guard clause. An early return at the top of a long method is fine.
- Order methods: class methods, then public methods with `initialize` first, then private methods. Within each group, order by call sequence so the file reads top to bottom.
- Put no blank line after `private`, and indent the methods under it. A module with only private methods puts `private` at the top, followed by a blank line, without indenting.
- Name async pairs `relay_later` (enqueues the job) and `relay_now` (does the work). The job calls `record.relay_now`.
- Use a bang method only when a non-bang counterpart exists. A bang does not mean "destructive".
- Use callbacks for side effects that always follow a model change (`after_create_commit :relay_later`).

## Red flags

- A service object for a simple create, update, or query.
- Domain rules in services while models hold only attributes and associations.
- A controller that orchestrates several services.
- Classes named `Manager`, `Handler`, or `Processor` that only forward calls.
- A new layer (repository, interactor, presenter) with one caller.

The fix is the same each time: move the logic onto the model that owns the data, and delete the extra layer.
