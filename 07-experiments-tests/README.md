# Experiments & Tests

This section documents product experiments including A/B tests, beta programs, and validation tests. Experiments allow us to test assumptions and validate solutions before committing to full implementation.

---

## Purpose

Experiments answer critical questions:
- Does this solution actually solve the user problem?
- What is the measurable impact of this change?
- Should we ship, iterate, or kill this idea?

Experimentation reduces risk by gathering evidence before making large investments. It turns opinions into data-driven decisions.

---

## Contents

| Folder | Description |
|--------|-------------|
| [experiment-backlog/](./experiment-backlog/) | Ideas and planned experiments |
| [active-experiments/](./active-experiments/) | Currently running experiments |
| [completed-experiments/](./completed-experiments/) | Finished experiments with results |
| [templates/](./templates/) | Experiment documentation templates |

## Workflow

**Backlog** → **Active** → **Completed** → **Decision** (ship, iterate, or kill)

## Templates

- [Experiment Template](../.github/ISSUE_TEMPLATE/experiment.md) — GitHub issue template for creating experiments

Each experiment should document:
- **Hypothesis**: What we believe and why
- **Metrics**: Primary success metric and guardrails
- **Design**: Type (A/B, beta, prototype), audience, duration
- **Results**: Data, analysis, and decision

---

## Related Folders

- [Opportunity Solution Trees](../06-opportunity-solution-trees/) — Experiments validate solutions from OSTs
- [Usage Data](../05-usage-data/) — Analytics data informs experiment design and results
- [Feature Specs](../09-feature-specs/) — Successful experiments become feature specs
