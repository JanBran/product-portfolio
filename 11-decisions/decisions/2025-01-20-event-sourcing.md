# Decision: Event Sourcing for Calendar Data

**Date:** 2025-01-20
**Status:** Active
**ID:** D-003

---

## Context

Calendar applications need undo/redo, sync conflict resolution, and audit history. We also want to power AI features by learning from user patterns. Traditional CRUD would lose this history.

---

## Decision

Store calendar changes as an event log alongside current state. Use materialized views for read queries. Events enable undo/redo, conflict resolution, and analytics.

References: TD-005

---

## Alternatives Considered

| Option | Pros | Cons |
|--------|------|------|
| Event sourcing + state (chosen) | Undo/redo, audit trail, AI learning | More storage, query complexity |
| CRUD only | Simple queries | Loses history, no undo |
| Full event sourcing (no state) | Pure event model | Complex reconstruction, slower reads |

---

## Outcome

**Result:** Undo/redo working smoothly. Sync conflicts resolved cleanly. Event data feeding early AI experiments.
**Would we decide differently?** No. The added complexity is worth the capabilities.
