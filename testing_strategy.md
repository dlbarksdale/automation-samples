# Testing Strategy Notes

## Guiding Principles

- Favor fast, reliable tests over brittle end-to-end suites
- Push validation as early as possible (CI, pre-merge)
- Treat test code as production code

## API Testing Philosophy

- Validate contracts and invariants, not just happy paths
- Focus on observability: logs, status codes, error messages
- Avoid over-mocking in integration-level tests

## CI Considerations

- Tests should provide signal, not noise
- Flaky tests are worse than missing tests
- Fail fast on smoke-level validation
