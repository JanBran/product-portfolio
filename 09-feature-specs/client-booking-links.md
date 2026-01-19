> **Status:** MOVED TO DEVELOPMENT
> **GitHub Issue:** [#2 - Client Booking Links](https://github.com/JanBran/product-portfolio/issues/2)
> **Date:** 2026-01-19

# Feature Spec: Client Booking Links

## Overview

Freelancers spend significant time on back-and-forth scheduling with clients. 78% spend 3+ hours weekly on client status communication alone. Competitors like Calendly dominate this space at $16/month, but our target users need a simpler, more affordable solution integrated with their unified calendar.

This feature enables:
- Shareable booking links for client scheduling
- Availability windows based on real calendar data
- Automatic meeting creation with video conferencing links
- Client-friendly booking experience without account creation

### Scope Boundaries
- In scope: Personal booking page, availability rules, Zoom/Meet auto-links, email confirmations, buffer time settings
- Out of scope: Team scheduling, round-robin assignment, paid appointments, custom branding (Phase 2)

---

## User Stories

### End Users (Freelancers)
- [US-001] As a freelancer, I want a personal booking link I can share with clients, so that they can schedule time without email back-and-forth.
- [US-002] As a freelancer, I want to set my available hours for bookings, so that clients only see times I'm free. (requires: US-001)
- [US-003] As a freelancer, I want buffer time automatically added between meetings, so that I have transition time. (requires: US-001)
- [US-004] As a freelancer, I want Zoom/Google Meet links auto-generated for booked meetings, so that I don't have to manually create them. (requires: US-001)
- [US-005] As a freelancer, I want to create different booking types (15min call, 1hr consultation), so that clients can choose the appropriate meeting length.

### Clients (External Users)
- [US-006] As a client, I want to book time without creating an account, so that scheduling is frictionless.
- [US-007] As a client, I want to receive an email confirmation with meeting details, so that I have a record of the booking.
- [US-008] As a client, I want to reschedule or cancel via the confirmation email, so that I can adjust if plans change.

---

## Definition of Done

### Booking Link Setup (US-001, US-002, US-005)
- [ ] User can generate a unique booking URL (e.g., app.com/book/username)
- [ ] Availability rules can be set (days, hours, timezone)
- [ ] Multiple booking types can be created with different durations
- [ ] Real-time calendar data prevents double-booking

### Meeting Creation (US-003, US-004)
- [ ] Booked meetings appear on user's calendar automatically
- [ ] Configurable buffer time (5/10/15/30 min) between meetings
- [ ] Zoom or Google Meet link auto-generated if integration enabled
- [ ] Meeting details include client name, email, and any intake questions

### Client Experience (US-006, US-007, US-008)
- [ ] Booking page loads without authentication requirement
- [ ] Available slots display in client's local timezone
- [ ] Confirmation email sent immediately upon booking
- [ ] Reschedule/cancel links work within configured policy window
