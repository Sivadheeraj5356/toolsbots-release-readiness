# Toolsbots Release Readiness

A small, dependency-free release readiness checker for the kind of production work described in Toolsbots Innovatix's Software Engineering Intern role: staged delivery, code review, automated tests, accessibility/security checks, and clear documentation.

## What it checks

The CLI reads a JSON release summary and reports whether the change is ready for staging review. It verifies that the release has:

- a named feature and owner
- a staging environment
- code review recorded
- automated tests passing
- documentation updated
- accessibility and security checks recorded
- an audit note for regulated client work

## Run

```bash
python3 release_readiness.py sample_release.json
```

## Test

```bash
python3 -m unittest -v
```

The sample uses a hypothetical citizen-service form update and is not employer code or data.
