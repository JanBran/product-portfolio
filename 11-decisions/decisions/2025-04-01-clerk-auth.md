# Decision: Choose Clerk for Authentication

**Date:** 2025-04-01
**Status:** Active
**ID:** D-008

---

## Context

TD-007 was pending: we needed to select an authentication provider. Requirements included social login (Google, Apple), magic links, and MFA support. Team wanted minimal auth code to maintain.

---

## Decision

Use Clerk as the authentication provider. Managed service reduces development time and maintenance burden. Accept vendor dependency for faster shipping.

References: TD-007

---

## Alternatives Considered

| Option | Pros | Cons |
|--------|------|------|
| Clerk (chosen) | Fast setup, great DX, built-in UI components | Vendor lock-in, cost at scale |
| NextAuth.js | Self-hosted, flexible | More setup, maintain ourselves |
| Auth0 | Enterprise features | Overkill for current needs, expensive |

---

## Outcome

**Result:** Auth implemented in 2 days. Zero auth-related bugs since launch. Cost acceptable at current scale (~$50/mo).
**Would we decide differently?** No. Time saved was worth the vendor dependency.
