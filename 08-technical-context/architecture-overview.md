# Architecture Overview

High-level system architecture for the intelligent calendar product.

---

## Design Philosophy

**Lightweight but scalable** — Start simple, add complexity only when validated by user demand.

Priorities:
- Fast time-to-market for MVP
- Low operational overhead for a small team
- Clear upgrade paths as we scale
- Support for AI-driven features without over-engineering

---

## System Layers

### Client Layer

- **Web App** — Next.js (React), primary interface
- **Mobile Apps** — React Native, iOS/Android (Phase 2)
- **Browser Extension** — TypeScript, quick capture and overlay

### API Layer

- **API Gateway** — Next.js API Routes initially, extract later if needed
- **Calendar API** — Node.js/TypeScript, CRUD for events and calendars
- **Scheduling API** — Node.js/TypeScript, availability and booking
- **AI Services** — Python (FastAPI), predictions and smart features

### Data Layer

- **Primary Database** — PostgreSQL for events, users, settings
- **Cache/Queue** — Redis for sessions, jobs, real-time sync
- **Object Storage** — S3-compatible for files and exports

---

## Key Architectural Decisions

### Monolith-First

Start with a single deployable unit. Split into services only when:
- A component has different scaling needs
- Team grows and needs ownership boundaries
- Performance bottlenecks require isolation

### Edge-First for Calendar Data

Calendar reads are frequent and latency-sensitive:
- Cache aggressively at CDN edge
- Use optimistic updates on client
- Sync in background, resolve conflicts server-side

### AI as a Separate Service

Keep AI/ML logic in Python service:
- Different runtime requirements (Python ML libraries)
- Easier to iterate on models independently
- Can scale separately from main application
- Clear API contract with main app

### Event Sourcing for Calendar Changes

Store calendar changes as events, not just current state:
- Enables undo/redo functionality
- Supports sync conflict resolution
- Provides audit trail
- Powers AI learning from user patterns

---

## Integration Points

### External Calendar Sync

- Google Calendar, Microsoft Outlook, Apple Calendar
- CalDAV/OAuth for calendar providers
- Two-way sync with conflict resolution
- Queue-based processing for reliability

### Payment Integration

- Stripe for subscriptions and payments
- Webhook-driven status updates
- Minimal payment logic in core app

---

## Scaling Phases

### Phase 1: MVP (0-10K users)

- Single region deployment
- Managed PostgreSQL (Supabase, Neon, or RDS)
- Serverless functions acceptable
- No dedicated AI infrastructure

### Phase 2: Growth (10K-100K users)

- Add database read replicas
- Dedicated Redis instance
- Consider multi-region for latency
- Move AI to dedicated compute

### Phase 3: Scale (100K+ users)

- Evaluate service extraction
- Database sharding by user
- CDN for all static assets
- Dedicated ML infrastructure

---

## Technology Stack

| Layer | Technology | Rationale |
|-------|------------|-----------|
| Frontend | Next.js 14+, TypeScript, Tailwind | Fast iteration, type safety |
| Backend | Node.js/TypeScript (main), Python (AI) | Async I/O, ML ecosystem |
| Database | PostgreSQL | Reliable, JSON support |
| Cache | Redis | Versatile, pub/sub |
| Hosting | Vercel (frontend), Railway/Render (backend) | Low ops burden |
| Auth | NextAuth.js or Clerk | Reduce complexity |

---

## Limitations

### What This Architecture Handles Well

- Fast initial development
- Low operational complexity
- Clear upgrade paths
- Good developer experience

### What This Architecture Does NOT Handle

- Very high write throughput (1000s events/second)
- Complex multi-tenant enterprise features
- Offline-first mobile (would need local DB)
- Real-time collaboration (would need WebSocket infrastructure)

### Future Upgrades If Needed

- **Better mobile offline** — Add SQLite sync layer
- **Real-time collaboration** — Add WebSocket service
- **Enterprise multi-tenancy** — Re-evaluate data model
- **High-frequency writes** — Consider event streaming (Kafka)

---

## Questions for Architects

Before implementing any feature, consider:

1. Does this feature need real-time updates?
2. How does this interact with external calendar sync?
3. What happens when the user is offline?
4. Is this a candidate for AI enhancement?
5. How does this affect mobile clients?
