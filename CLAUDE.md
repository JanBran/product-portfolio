# CLAUDE.md

## Project Overview

Product documentation for **Simple Calendar** — a minimal, fast calendar application.

## Repository Structure

```
01-strategy-vision/             - Product strategy, vision, and personas
02-market-research/             - Competitive analysis, industry reports, pricing
03-goals-metrics/               - OKRs and quarterly goals
04-user-research/               - Interviews, surveys, personas, insights
05-usage-data/                  - Analytics, dashboards, data exports
06-opportunity-solution-trees/  - OSTs for key objectives
07-experiments-tests/           - A/B tests and experiment tracking
08-technical-context/           - Architecture, coding guardrails, tech decisions
09-feature-specs/               - Detailed feature specifications
10-roadmap/                     - Current roadmap and priorities
11-decisions/                   - Decision log and ADRs
12-customer-feedback/           - Feature requests, satisfaction data, support analysis
```

## Key Files

- [01-strategy-vision/product-strategy-vision-personas.md](01-strategy-vision/product-strategy-vision-personas.md) - Full strategy document
- [03-goals-metrics/](03-goals-metrics/) - Current quarterly goals
- [06-opportunity-solution-trees/](06-opportunity-solution-trees/) - OSTs by objective
- [08-technical-context/architecture-overview.md](08-technical-context/architecture-overview.md) - System architecture
- [09-feature-specs/](09-feature-specs/) - Feature specifications
- [10-roadmap/current-roadmap.md](10-roadmap/current-roadmap.md) - Current roadmap
- [11-decisions/decision-log.md](11-decisions/decision-log.md) - Decision log

### Quick Reference Files
- [product/vision.md](product/vision.md) - Vision summary
- [product/goals.md](product/goals.md) - Goals summary
- [product/decisions.md](product/decisions.md) - Key decisions summary
- [research/user-insights.md](research/user-insights.md) - User research summary
- [research/competitors.md](research/competitors.md) - Competitive landscape summary
- [specs/001-calendar-mvp.md](specs/001-calendar-mvp.md) - MVP specification
- [roadmap/current.md](roadmap/current.md) - Roadmap summary

## Guidelines

- Keep documents focused and concise
- Use markdown format throughout
- Link related documents
- Update roadmap when features ship
- Log decisions in `11-decisions/decision-log.md`
- Use numbered folders for detailed documentation
- Use quick reference folders for summaries

## Product spec assistant

When prompted "provide analysis" and the file is located in `09-feature-specs/`, follow a consistent format.

Specs in `09-feature-specs/` follow a consistent format. Template is available in `.github/ISSUE_TEMPLATE/feature-spec.md`.

Each spec includes:
1. Overview (problem, scope, out of scope)
2. User Stories (numbered US-XXX)
3. Definition of Done (checkboxes)

### Trigger Phrases
- "provide analysis"
- "analyze this spec"
- "review spec"

### Analysis Output Format
When analyzing a spec, provide:

1. **Completeness Check** — Are all required sections present?
2. **User Story Quality** — Are stories properly formatted (US-XXX) with clear user/action/benefit?
3. **Technical Feasibility** — Cross-reference with:
   - [architecture-overview.md](08-technical-context/architecture-overview.md) for system constraints
   - [coding-guardrails.md](08-technical-context/coding-guardrails.md) for implementation rules
   - [technical-decisions.md](08-technical-context/technical-decisions.md) for existing choices
4. **Definition of Done Coverage** — Does each user story have acceptance criteria?
5. **Scope Clarity** — Are in-scope and out-of-scope items explicit?
6. **Gaps/Risks** — Missing information, technical blockers, or dependency issues

### Technical Validation Checklist
Before approving a spec, verify:
- [ ] Feature aligns with architecture (monolith-first, edge-first caching)
- [ ] No conflicts with existing technical decisions (TD-001 through TD-008)
- [ ] Security requirements addressed (per coding-guardrails.md)
- [ ] Calendar-specific rules followed (UTC storage, timezone handling, recurring events)
- [ ] Testing approach defined (what needs unit/integration/E2E tests)

### Creating New Specs
When asked to create a spec:
1. Use template at `.github/ISSUE_TEMPLATE/feature-spec.md`
2. Naming convention: `XXX-feature-name.md` (XXX = sequential number)
3. Reference relevant technical decisions (e.g., "Per TD-005, use event sourcing for...")

## Relaying the product spec to issue tracking systems

### GitHub Integration

#### Reading from GitHub
When asked to analyze an existing issue:
1. **By number** (e.g., "Analyze issue #1"):
   - Fetch using: `gh issue view <number>`

2. **By name/keyword** (e.g., "Analyze the authentication issue"):
   - Search: `gh issue list --search "<keyword>"`
   - If multiple matches, show options and ask which one
   - Fetch the full issue: `gh issue view <number>`

#### Creating Issues from Specs
When asked to create GitHub issues from a spec file:
1. Read the spec file to understand the full context
2. Create the parent issue first with the Overview and full user stories
3. Create sub-issues for each work breakdown item
4. Link sub-issues to parent using the GraphQL API:
   ```
   gh api graphql -f query='
   mutation {
     addSubIssue(input: {issueId: "<parent_node_id>", subIssueId: "<child_node_id>"}) {
       issue { number }
       subIssue { number title }
     }
   }'
   ```
5. Get node IDs with: `gh issue view <number> --json id --jq .id`

#### Useful GitHub CLI Commands
- `gh issue list` - List open issues
- `gh issue list --state all` - List all issues (open and closed)
- `gh issue list --label <label>` - Filter by label
- `gh issue list --search "<query>"` - Search issues by title/body
- `gh issue view <number>` - View full issue details
- `gh issue create --title "..." --body "..."` - Create new issue

---

### Move to Development

When the user says "move to development" (or similar), execute the following workflow:

#### Prerequisites
- User must specify which spec file to move (or be working on one in context)
- Spec must have all required sections: Overview, User Stories, Definition of Done
- Spec should pass technical validation (see Product spec assistant section)

#### Workflow Steps

1. **Validate Technical Alignment**
   - Quick check against `08-technical-context/architecture-overview.md`
   - Flag any conflicts with `08-technical-context/technical-decisions.md`
   - If issues found, report them and ask user how to proceed

2. **Create GitHub Issue**
   - Create a parent issue with the full spec content
   - Title format: `[Spec Name] - [Brief Description]`
   - Include all user stories and definition of done as checkboxes
   - Add labels: `spec`, `feature`, and priority if known
   - Add footer linking back to source spec file
   - Format: `**Source Spec:** [09-feature-specs/XXX-spec-name.md](https://github.com/[org]/[repo]/blob/main/09-feature-specs/XXX-spec-name.md)`

3. **Add GitHub Link to Spec File**
   - Add status banner at top of spec file:
   ```markdown
   > **Status:** MOVED TO DEVELOPMENT
   > **GitHub Issue:** [#XX - Issue Title](https://github.com/.../issues/XX)
   > **Date:** YYYY-MM-DD
   ```

4. **Log the Decision**
   - Add entry to `11-decisions/decision-log.md`:
   ```markdown
   | YYYY-MM-DD | Spec XXX moved to development | Issue #XX | [link] |
   ```

5. **Confirm Completion**
   - Report the GitHub issue URL to the user
   - Confirm spec file and decision log have been updated

#### Error Handling
- **GitHub API error**: Report error, do not modify local files
- **Missing spec sections**: List missing sections, ask user to complete
- **Spec already moved**: Warn user, offer to update existing issue instead
- **Technical conflicts**: List conflicts, require user decision before proceeding

#### Example
```
User: "move to development"
AI: [Validates spec against technical context]
    [Executes workflow for current/specified spec]
    - Created issue #17: https://github.com/.../issues/17
    - Added status banner to spec file
    - Updated 11-decisions/decision-log.md
```

---

## Technical Context Integration

When implementing features or analyzing specs, always reference `08-technical-context/`.

### Key Files to Consult

| File | When to Reference |
|------|-------------------|
| [architecture-overview.md](08-technical-context/architecture-overview.md) | System design questions, scaling concerns, integration points |
| [coding-guardrails.md](08-technical-context/coding-guardrails.md) | Code style, testing requirements, security rules, AI agent rules |
| [technical-decisions.md](08-technical-context/technical-decisions.md) | Before proposing new technology or patterns |

### Active Technical Decisions
Reference these when writing specs or code:
- **TD-001**: Next.js as primary framework
- **TD-002**: PostgreSQL for all persistent data
- **TD-003**: Python/FastAPI for AI/ML services (separate from main app)
- **TD-004**: Redis for caching and queues
- **TD-005**: Event sourcing for calendar data
- **TD-006**: Monorepo structure

### Pending Decisions (require user input)
- **TD-007**: Authentication provider (NextAuth.js vs Clerk vs Auth0)
- **TD-008**: Mobile development approach (React Native vs Expo vs Native vs PWA)

### Architecture Constraints
When proposing features, consider these system boundaries:
- **Monolith-first**: Avoid proposing microservices unless scaling requires it
- **Edge-first for reads**: Calendar data should be cacheable at CDN
- **AI as separate service**: ML features go in Python/FastAPI, not Node.js
- **Event sourcing**: Calendar changes must support undo/redo and sync

### Calendar-Specific Rules
All calendar features must follow:
- Store times in UTC
- Include timezone with user-facing dates
- Handle recurring events as patterns (not expanded instances)
- Validate conflicts server-side

