# Usage Data

This folder contains quantitative product analytics, usage patterns, and data-driven insights.

## Purpose

Usage data answers critical questions:
- What are users actually doing in the product (not what they say they do)?
- Where do users get stuck, drop off, or experience friction?
- Which features are adopted, ignored, or causing frustration?

**How this complements User Research:**
- [User Research](../04-user-research/) captures the *why*—qualitative insights from interviews, surveys, and direct conversations
- Usage Data captures the *what*—quantitative behavioral data showing actual product usage at scale
- Together they provide a complete picture: what users say vs. what they do

## About This Section

**Why this section differs from others:**
- Other folders contain internal documentation (strategy, specs, decisions, research)
- This section references **3rd-party analytics tools** where the actual tracking data lives
- The repository stores only configuration, queries, exports, and analysis scripts—not the raw data
- Dashboards and real-time analytics are managed in the external tool's UI

**Compatible analytics tools:**
- **FullStory** - Session replay, heatmaps, frustration signals (example used in this folder)
- **Amplitude** - Product analytics, cohort analysis, funnel tracking
- **Mixpanel** - Event tracking, user flows, retention analysis
- **Heap** - Auto-captured events, behavioral analytics
- **PostHog** - Open-source product analytics, feature flags
- **Google Analytics** - Web traffic, acquisition, basic event tracking

## Contents

- [api/](./api/) - API references and Postman collections for data export
- [python-analysis/](./python-analysis/) - Scripts and notebooks for local analysis
- [queries/](./queries/) - Saved search queries and segment definitions
- [reports/](./reports/) - Regular usage reports (`YYYY-MM-usage-report.md`)
- [data-insights/](./data-insights/) - Insights derived from analysis
- [exports/](./exports/) - Local storage for exported data (CSV, JSON)

## Data Export Workflow

- **Analytics tool** collects user tracking data (sessions, events, signals)
- Data is exported via the tool's **Export API** or **Postman collection**
- Exports are saved locally as **CSV or JSON files** in [exports/](./exports/)
- **Python scripts** in [python-analysis/](./python-analysis/) process the data for insights

## Data Governance

- Analytics tool access is managed via admin settings
- API keys are stored securely (never commit to repo)
- See `.env.example` in [python-analysis/](./python-analysis/) for required environment variables
- PII should be masked in session replays
- Data retention is configured in the analytics tool settings
- Metrics definitions will be added to `03-goals-metrics/` once dashboards are configured

---

## Related Folders

- [User Research](../04-user-research/) — Qualitative insights complement quantitative usage data
- [Goals & Metrics](../03-goals-metrics/) — Usage data feeds into OKR tracking and success metrics
- [Experiments & Tests](../07-experiments-tests/) — Analytics data validates experiment results
- [Customer Feedback](../12-customer-feedback/) — Correlate feedback with behavioral patterns
