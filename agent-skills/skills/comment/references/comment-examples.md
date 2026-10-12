# Comment examples

Use these patterns when deciding whether a comment belongs in the scoped code.

## Add a why-comment

Complex or non-obvious behavior:

```text
# Retry with jitter because the upstream rate-limits synchronized clients.
for attempt in range(max_attempts):
    ...
```

Important decision:

```text
# Keep the legacy payload key; mobile clients still parse `user_id` only.
body["user_id"] = account.id
```

## Do not add a what-comment

Redundant narration of self-explanatory code:

```text
# Bad: increment the counter
counter += 1

# Bad: get the user name
name = user.name
```

Leave those lines uncommented.

## Rewrite or remove

Before:

```text
# Loop through items
for item in items:
    process(item)
```

After: remove the comment; the loop already states what happens.

Before:

```text
# Set flag to false
enabled = False
```

After: remove it, or rewrite only if the reason is non-obvious:

```text
# Disable until migration finishes; partial writes corrupt the cache.
enabled = False
```
