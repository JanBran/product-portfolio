# Feature Spec: Daily Digest & Notifications

## Overview

Without daily engagement triggers, product adoption fails. To achieve our target of 40% weekly active users, users need consistent touchpoints that provide value without adding noise. The completed experiment on signup flow showed users who engage early are 3x more likely to return.

This feature enables:
- Daily schedule digest via email or push notification
- Configurable notification timing and channels
- Upcoming event reminders with smart defaults
- Weekly review prompts with schedule insights

### Scope Boundaries
- In scope: Daily digest email, push notifications, reminder settings, weekly summary, notification preferences
- Out of scope: In-app notification center (Phase 2), SMS notifications, calendar widget for mobile home screen

---

## User Stories

### End Users (Freelancers)
- [US-001] As a freelancer, I want a daily digest of my schedule each morning, so that I start the day knowing what's ahead.
- [US-002] As a freelancer, I want to choose when I receive my daily digest (morning vs night before), so that it fits my planning routine.
- [US-003] As a freelancer, I want reminders before meetings, so that I'm not caught off-guard by upcoming commitments.
- [US-004] As a freelancer, I want a weekly summary of how I spent my time, so that I can reflect and adjust my schedule.
- [US-005] As a freelancer, I want to control which notifications I receive and how, so that I'm not overwhelmed by alerts.

### Developers
- [US-006] As a developer, I want notification preferences stored per-user, so that settings persist across sessions and devices.
- [US-007] As a developer, I want email delivery tracking, so that I can monitor digest engagement and deliverability.

---

## Definition of Done

### Daily Digest (US-001, US-002, US-007)
- [ ] Daily email sent at user-configured time (default: 7am local)
- [ ] Digest includes today's events, focus blocks, and free time summary
- [ ] User can switch between morning delivery and night-before delivery
- [ ] Email open rates tracked for engagement analysis

### Event Reminders (US-003)
- [ ] Default reminder set to 15 minutes before events
- [ ] User can customize reminder timing per event or globally
- [ ] Reminders delivered via email and/or push (based on preference)
- [ ] Focus blocks trigger "focus starting" notification if enabled

### Weekly Summary (US-004)
- [ ] Weekly email sent on Sunday evening or Monday morning (configurable)
- [ ] Summary includes: meetings count, focus hours, busiest day, trends vs prior week
- [ ] Insights highlight schedule patterns (e.g., "You had 40% more meetings this week")

### Notification Preferences (US-005, US-006)
- [ ] Settings page allows toggle for each notification type
- [ ] Channel preference (email, push, both, none) configurable per type
- [ ] Quiet hours setting suppresses non-urgent notifications
- [ ] Preferences sync across devices via user account
