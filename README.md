# Agentic PR Demo

A deliberately small Python repository for learning GitHub PR automation and AI-assisted code review.

## Run tests

```bash
python -m unittest discover -s tests -v
```

## Learning exercise

1. Push this working baseline to `main`.
2. Create a GitHub Issue: `AUTH-101 — Fix login validation` (or use the issue's actual number).
3. Create branch `feature/AUTH-101-login` from `main`.
4. In `app/auth.py`, intentionally change `{3,20}` to `{2,20}`.
5. Commit and push the branch. The `test_short_username` test will fail.
6. Later, your separate AI agent service will detect the push, create a PR, analyze the failing test, and notify the maintainer.

Do not merge the intentionally broken feature branch into `main`.
