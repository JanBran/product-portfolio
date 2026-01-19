# Coding Guardrails

Rules and constraints for AI coding agents and developers working on this codebase.

---

## Purpose

These guardrails ensure consistency, prevent common mistakes, and help AI agents make good decisions without extensive context about every part of the system.

---

## General Principles

### Simplicity First

- Avoid over-engineering; match product positioning (lightweight, fast)
- No premature abstractions; wait until pattern repeats 3+ times
- Prefer standard library solutions over adding dependencies
- Delete unused code; don't comment it out

### Explicit Over Implicit

- Use clear, descriptive names even if longer
- Avoid magic numbers; use named constants
- Document "why" not "what" in comments
- Make dependencies explicit in function signatures

### Fail Fast and Loud

- Validate inputs at system boundaries
- Throw errors early rather than passing bad data
- Log errors with context for debugging
- Never silently swallow exceptions

---

## Code Style

### TypeScript/JavaScript

- Use TypeScript strict mode
- Prefer `const` over `let`; avoid `var`
- Use async/await over raw Promises
- Destructure objects for cleaner code
- Use optional chaining (`?.`) and nullish coalescing (`??`)

### File Organization

- One component/class per file
- Co-locate tests with source files (`*.test.ts` next to `*.ts`)
- Group by feature, not by type (e.g., `/features/calendar/` not `/components/`, `/hooks/`)
- Keep files under 300 lines; split if larger

### Naming Conventions

- Files: `kebab-case.ts`
- Components: `PascalCase`
- Functions/variables: `camelCase`
- Constants: `UPPER_SNAKE_CASE`
- Database tables: `snake_case`

---

## Architecture Rules

### API Design

- Use RESTful conventions for CRUD operations
- Return consistent response shapes
- Include pagination for list endpoints
- Version APIs in URL path (`/api/v1/`)

### Database

- Always use migrations; never modify schema directly
- Add indexes for frequently queried columns
- Use transactions for multi-step operations
- Avoid N+1 queries; use eager loading

### State Management

- Keep server state in React Query or similar
- Minimize global client state
- Use URL state for shareable/bookmarkable views
- Avoid prop drilling; use context sparingly

### Calendar-Specific Rules

- Always store times in UTC
- Include timezone information with user-facing dates
- Handle recurring events as patterns, not expanded instances
- Validate event conflicts server-side

---

## Security Requirements

### Authentication/Authorization

- Never trust client-side auth state for sensitive operations
- Validate user ownership on every data access
- Use short-lived tokens; implement refresh flow
- Log authentication failures

### Data Handling

- Sanitize all user input
- Use parameterized queries (never string concatenation for SQL)
- Encrypt sensitive data at rest
- Don't log PII or credentials

### API Security

- Implement rate limiting
- Validate request origins (CORS)
- Use HTTPS everywhere
- Validate webhook signatures

---

## Performance Guidelines

### Frontend

- Lazy load routes and heavy components
- Optimize images and assets
- Minimize bundle size; monitor with bundle analyzer
- Use React.memo() sparingly and measure impact

### Backend

- Cache read-heavy endpoints
- Use database connection pooling
- Implement request timeouts
- Stream large responses

### Calendar-Specific

- Limit event queries to visible date range
- Prefetch adjacent weeks/months
- Debounce rapid updates
- Batch sync operations

---

## Testing Requirements

### What Must Be Tested

- Business logic and calculations
- API endpoints (happy path + error cases)
- Data validation
- Authentication/authorization

### What Can Skip Tests

- Pure UI components without logic
- Third-party library wrappers
- Generated code

### Testing Approach

- Unit tests for pure functions
- Integration tests for API routes
- E2E tests for critical user flows only
- Mock external services in tests

---

## AI Agent-Specific Rules

### Before Writing Code

- Read existing code in the target area first
- Check for existing utilities that solve the problem
- Understand the data model involved
- Review related tests for expected behavior

### When Writing Code

- Match the style of surrounding code
- Prefer editing existing files over creating new ones
- Don't add dependencies without explicit approval
- Include error handling for external calls

### After Writing Code

- Run existing tests to check for regressions
- Add tests for new functionality
- Update types if data shapes change
- Remove any debug/console statements

### What NOT to Do

- Don't refactor unrelated code
- Don't add features beyond the request
- Don't change configuration without approval
- Don't modify database schema without migration
- Don't hardcode environment-specific values

---

## Dependency Rules

### Adding Dependencies

Before adding a dependency, check:
- Is there a simpler solution without it?
- Is it actively maintained (commits in last 6 months)?
- What's the bundle size impact?
- Are there security vulnerabilities?

### Approved Categories

- **Use freely**: Testing, linting, build tools
- **Evaluate carefully**: UI components, state management
- **Require approval**: Database drivers, auth libraries, payment SDKs

### Avoid

- Packages with no TypeScript types
- Packages with excessive transitive dependencies
- Abandoned packages (no updates in 12+ months)

---

## Error Handling

### User-Facing Errors

- Show clear, actionable messages
- Don't expose technical details
- Provide recovery paths when possible
- Log full error details server-side

### System Errors

- Include correlation IDs for tracing
- Log stack traces and context
- Alert on error rate spikes
- Have fallback behavior for non-critical features

---

## Git and Deployment

### Commit Messages

- Use conventional commits: `feat:`, `fix:`, `docs:`, `refactor:`
- Keep subject under 72 characters
- Reference issue numbers when applicable

### Branch Strategy

- `main` is always deployable
- Feature branches from `main`
- PR required for merging
- Squash merge preferred

### Deployment

- All changes go through CI
- Tests must pass before merge
- Use feature flags for risky changes
- Monitor after deployment
