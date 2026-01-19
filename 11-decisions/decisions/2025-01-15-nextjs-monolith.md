# Decision: Launch with Next.js Monolith

**Date:** 2025-01-15
**Status:** Active
**ID:** D-001

---

## Context

We needed to choose a framework for the Simple Calendar MVP. Speed to market was critical, and the team is small. We wanted to minimize infrastructure complexity while retaining the ability to scale later.

---

## Decision

Use Next.js 14+ with App Router as the primary framework, deployed as a monolith. API routes handle backend logic initially. Extract services only when scaling demands it.

References: TD-001, TD-006

---

## Alternatives Considered

| Option | Pros | Cons |
|--------|------|------|
| Next.js monolith (chosen) | Full-stack, fast iteration, strong TypeScript support | Vercel coupling, App Router still maturing |
| Remix | Similar benefits, good data loading | Smaller ecosystem |
| Separate React + Express | More flexibility | More ops overhead, slower to ship |

---

## Outcome

**Result:** MVP shipped on schedule. Development velocity high. No scaling issues at current user count.
**Would we decide differently?** No. Monolith-first was the right call for our stage.
