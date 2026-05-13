# Review Example

```markdown
## Findings

- **High** `src/auth/session.py:87` - Expired sessions can be reused because the expiration check is skipped when the cache returns a session object. Add an expiration check before returning cached sessions and cover it with a regression test.

## Open Questions

- None.

## Summary

Reviewed the session handling change. The main gap is a missing regression test for cached expired sessions.
```
