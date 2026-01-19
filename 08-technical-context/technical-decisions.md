# Technical Decisions

Key technical choices and their rationale. Reference this before proposing alternatives.

---

## Active Decisions

### TD-001: Next.js as Primary Framework

**Status**: Decided
**Date**: 2025-01

**Decision**: Use Next.js 14+ with App Router for web application.

**Why**:
- Full-stack framework reduces infrastructure complexity
- Server-side rendering improves SEO and initial load
- API routes eliminate need for separate backend initially
- Strong TypeScript support
- Large ecosystem and community

**Trade-offs**:
- Vendor coupling to Vercel ecosystem (mitigated: can self-host)
- App Router still maturing (acceptable for our use case)

**Alternatives Considered**:
- Remix — Similar benefits, smaller ecosystem
- SvelteKit — Less TypeScript maturity
- Separate React + Express — More flexibility, more ops overhead

---

### TD-002: PostgreSQL as Primary Database

**Status**: Decided
**Date**: 2025-01

**Decision**: Use PostgreSQL for all persistent data.

**Why**:
- Proven reliability at scale
- Strong JSON support for flexible schemas
- Full-text search built-in
- Wide hosting options (Supabase, Neon, RDS, self-hosted)
- Team familiarity

**Trade-offs**:
- Single database type limits polyglot options (acceptable at current scale)
- Requires careful schema design for calendar-specific queries

**Alternatives Considered**:
- MongoDB — Better for unstructured data, weaker for relationships
- MySQL — Similar capabilities, less JSON flexibility
- SQLite — Great for local-first, harder to scale

---

### TD-003: Python for AI/ML Services

**Status**: Decided
**Date**: 2025-01

**Decision**: Use Python (FastAPI) for AI and ML functionality, separate from main Node.js app.

**Why**:
- Best-in-class ML libraries (scikit-learn, PyTorch, etc.)
- FastAPI provides async performance and auto-generated docs
- Clear separation of concerns
- Can scale independently
- Easier to iterate on models

**Trade-offs**:
- Two runtimes to maintain
- Network overhead for AI calls
- Deployment complexity (mitigated: containerization)

**Alternatives Considered**:
- Node.js with TensorFlow.js — Limited model support
- Calling external AI APIs only — Less control, higher latency
- Go — Excellent performance, immature ML ecosystem

---

### TD-004: Redis for Caching and Queues

**Status**: Decided
**Date**: 2025-01

**Decision**: Use Redis for session cache, job queues, and real-time features.

**Why**:
- Versatile: cache, queue, pub/sub in one
- Low latency
- Managed options widely available
- Simple to operate at small scale

**Trade-offs**:
- Memory-bound (cost increases with data size)
- Single point of failure without clustering

**Alternatives Considered**:
- Memcached — Simpler, but no pub/sub or persistence
- RabbitMQ — Better for complex queuing, more operational overhead
- In-memory only — Not durable, can't share across instances

---

### TD-005: Event Sourcing for Calendar Data

**Status**: Decided
**Date**: 2025-01

**Decision**: Store calendar changes as an event log alongside current state.

**Why**:
- Enables undo/redo functionality
- Simplifies sync conflict resolution
- Provides complete audit history
- Powers AI learning from user patterns
- Supports analytics on user behavior

**Trade-offs**:
- More storage required
- Queries require projection or materialized views
- Eventual consistency in some views

**Alternatives Considered**:
- CRUD only — Simpler, but loses history
- Full event sourcing (no state table) — More complex reconstruction

---

### TD-006: Monorepo Structure

**Status**: Decided
**Date**: 2025-01

**Decision**: Use monorepo for all application code (web, mobile, API, AI service).

**Why**:
- Atomic changes across packages
- Shared types and utilities
- Simplified dependency management
- Better for small team

**Trade-offs**:
- Build times can grow
- Requires tooling (Turborepo or Nx)

**Alternatives Considered**:
- Polyrepo — Better isolation, more coordination overhead
- Monolith with no package structure — Simpler initially, harder to extract later

---

## Pending Decisions

### TD-007: Authentication Provider

**Status**: Under evaluation
**Options**:
- NextAuth.js — Flexible, self-hosted, more setup
- Clerk — Managed, fast to implement, vendor lock-in
- Auth0 — Enterprise-grade, potentially overkill

**Criteria for decision**:
- Time to implement
- Cost at scale
- Feature requirements (SSO, MFA)
- Vendor risk tolerance

---

### TD-008: Mobile Development Approach

**Status**: Under evaluation
**Options**:
- React Native — Code sharing with web, good performance
- Expo — Faster development, some limitations
- Native iOS/Android — Best performance, highest cost
- PWA only — Lowest cost, limited capabilities

**Criteria for decision**:
- Timeline for mobile launch
- Feature parity requirements
- Offline requirements

---

## Decision Log Format

When adding new decisions:

```
### TD-XXX: [Title]

**Status**: Proposed | Under evaluation | Decided | Superseded
**Date**: YYYY-MM

**Decision**: [What was decided]

**Why**: [Reasons for the decision]

**Trade-offs**: [What we're giving up]

**Alternatives Considered**: [Other options and why rejected]
```
