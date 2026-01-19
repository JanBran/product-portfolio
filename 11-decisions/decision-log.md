# Decision Log

Chronological record of significant product decisions.

---

## Active Decisions

| Date | ID | Decision | Category | Doc |
|------|----|----------|----------|-----|
| 2025-01-15 | [D-001](decisions/2025-01-15-nextjs-monolith.md) | Launch with Next.js monolith | Technical | TD-001, TD-006 |
| 2025-01-15 | [D-002](decisions/2025-01-15-postgresql-redis-stack.md) | PostgreSQL + Redis stack | Technical | TD-002, TD-004 |
| 2025-01-20 | [D-003](decisions/2025-01-20-event-sourcing.md) | Event sourcing for calendar data | Technical | TD-005 |
| 2025-02-01 | [D-004](decisions/2025-02-01-defer-mobile.md) | Defer mobile to Phase 2 | Strategic | — |
| 2025-02-10 | [D-005](decisions/2025-02-10-free-tier-limits.md) | Free tier: 3 calendars, 1000 events | Pricing | — |
| 2025-03-01 | [D-006](decisions/2025-03-01-mvp-scope.md) | MVP scope: core calendar + Google sync only | Scope | Spec 001 |
| 2025-03-15 | [D-007](decisions/2025-03-15-soft-launch.md) | Soft launch to waitlist (500 users) | Go-to-market | — |
| 2025-04-01 | [D-008](decisions/2025-04-01-clerk-auth.md) | Choose Clerk for authentication | Technical | TD-007 |
| 2025-04-20 | [D-009](decisions/2025-04-20-outlook-sync.md) | Add Outlook sync for Q2 | Feature | Spec 002 |
| 2025-05-01 | [D-010](decisions/2025-05-01-expand-free-tier.md) | Expand free tier to 5 calendars | Pricing | — |
| 2026-01-19 | D-014 | Calendar Sync & Integration moved to development | Feature | [Issue #1](https://github.com/JanBran/product-portfolio/issues/1) |
| 2026-01-19 | D-015 | Client Booking Links moved to development | Feature | [Issue #2](https://github.com/JanBran/product-portfolio/issues/2) |
| 2026-01-19 | D-016 | Focus Time Blocking moved to development | Feature | [Issue #3](https://github.com/JanBran/product-portfolio/issues/3) |

---

## Pending Decisions

| ID | Decision | Options | Due |
|----|----------|---------|-----|
| D-011 | Mobile development approach | React Native vs Expo vs PWA | 2025-06-01 |
| D-012 | AI scheduling assistant scope | Basic suggestions vs full automation | 2025-06-15 |
| D-013 | Enterprise tier pricing | Per-seat vs flat rate | 2025-07-01 |

---

## Reversed/Superseded

| Date | ID | Original Decision | Reversal | Reason |
|------|----|-------------------|----------|--------|
| 2025-05-01 | [D-005](decisions/2025-02-10-free-tier-limits.md) | Free tier: 3 calendars | [Expanded to 5 calendars](decisions/2025-05-01-expand-free-tier.md) | User feedback: 3 too restrictive for adoption |
