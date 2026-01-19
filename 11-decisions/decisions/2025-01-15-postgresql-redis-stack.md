# Decision: PostgreSQL + Redis Stack

**Date:** 2025-01-15
**Status:** Active
**ID:** D-002

---

## Context

We needed to select our data layer for the calendar application. Requirements included reliable storage for calendar events, user data, and settings, plus caching and job queue capabilities for sync operations.

---

## Decision

Use PostgreSQL as the primary database for all persistent data. Use Redis for session cache, job queues, and real-time features.

References: TD-002, TD-004

---

## Alternatives Considered

| Option | Pros | Cons |
|--------|------|------|
| PostgreSQL + Redis (chosen) | Proven reliability, JSON support, versatile caching | Two systems to manage |
| MongoDB + Redis | Flexible schemas | Weaker for relational calendar data |
| PostgreSQL only | Simpler stack | No built-in pub/sub or fast caching |

---

## Outcome

**Result:** Stack performing well. PostgreSQL handles calendar queries efficiently. Redis job queues reliable for Google sync.
**Would we decide differently?** No. The combination covers all our needs.
