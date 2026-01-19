# Feature Spec: Time Analytics Dashboard

## Overview

Freelancers need to demonstrate clear value over free calendar alternatives like Google Calendar. Research shows users are willing to pay $25/month for a tool that saves 2+ hours weekly—but they need visibility into that time savings. A time-saved metrics dashboard provides tangible proof of value.

This feature enables:
- Visual breakdown of time spent across categories
- Trends and comparisons over time
- Focus time vs meeting time ratio tracking
- Exportable reports for client billing or personal review

### Scope Boundaries
- In scope: Time categorization, weekly/monthly views, focus vs meetings breakdown, basic charts, CSV export
- Out of scope: Client-level time tracking, invoicing integration (separate feature), team analytics, real-time tracking

---

## User Stories

### End Users (Freelancers)
- [US-001] As a freelancer, I want to see how my time was distributed this week, so that I understand where my hours went.
- [US-002] As a freelancer, I want to compare this week's schedule to previous weeks, so that I can identify trends.
- [US-003] As a freelancer, I want to see my focus time vs meeting time ratio, so that I can ensure I'm protecting deep work.
- [US-004] As a freelancer, I want to categorize events (client work, admin, personal), so that I can see time by category.
- [US-005] As a freelancer, I want to export my time data, so that I can use it for billing or personal records.

### Developers
- [US-006] As a developer, I want event categorization to be AI-assisted based on event titles, so that users don't have to manually tag everything.
- [US-007] As a developer, I want analytics computed from event-sourced data, so that historical views are accurate even after edits.

---

## Definition of Done

### Time Breakdown View (US-001, US-004)
- [ ] Dashboard displays time distribution as visual chart (pie or bar)
- [ ] Events auto-categorized by type (meetings, focus, travel, personal)
- [ ] User can manually override or create custom categories
- [ ] Category colors consistent across all calendar views

### Trends & Comparisons (US-002, US-003)
- [ ] Weekly view shows comparison to prior week (% change)
- [ ] Monthly view shows week-over-week trend line
- [ ] Focus time ratio displayed prominently (e.g., "42% of your week was focus time")
- [ ] Insights highlight significant changes (e.g., "Meetings up 25% this week")

### Export & Reporting (US-005)
- [ ] CSV export includes date, event, duration, category
- [ ] Date range selector for custom export periods
- [ ] Export respects user's timezone for timestamps

### AI Categorization (US-006, US-007)
- [ ] New events auto-categorized based on title keywords
- [ ] User corrections improve future suggestions
- [ ] Categorization works on synced external calendar events
