# FullStory Search Queries

This file contains reusable FullStory search queries and segment definitions.

> **Note:** FullStory uses a visual search builder, not SQL. These are documented as search criteria you can recreate in the FullStory UI or use via the Search API.

---

## Common Searches

### Sessions with Errors

Find sessions where JavaScript errors occurred.

**Search Criteria:**
```
Event Type: Console Error
Time Range: Last 30 days
```

**API Filter:**
```json
{
  "filter": {
    "type": "EVENT",
    "eventType": "console_error"
  }
}
```

---

### Sessions with Rage Clicks

Find sessions with frustrated clicking behavior.

**Search Criteria:**
```
Frustration Signal: Rage Click
Rage Click Count: >= 1
Time Range: Last 30 days
```

**API Filter:**
```json
{
  "filter": {
    "type": "FRUSTRATION_SIGNAL",
    "signalType": "rage_click"
  }
}
```

---

### Sessions on Specific Page

Find sessions that visited a specific page (e.g., checkout).

**Search Criteria:**
```
Event: Page View
URL contains: /checkout
Time Range: Last 30 days
```

**API Filter:**
```json
{
  "filter": {
    "type": "EVENT",
    "eventType": "page",
    "properties": {
      "url": {
        "contains": "/checkout"
      }
    }
  }
}
```

---

### Long Sessions (Engaged Users)

Find sessions longer than 5 minutes.

**Search Criteria:**
```
Session Duration: > 300 seconds
Time Range: Last 30 days
```

---

### Short Sessions (Bounces)

Find sessions shorter than 30 seconds (potential bounces).

**Search Criteria:**
```
Session Duration: < 30 seconds
Page Count: = 1
Time Range: Last 30 days
```

---

### Sessions with Form Abandonment

Find sessions where users started but didn't submit a form.

**Search Criteria:**
```
Frustration Signal: Form Abandonment
Form Name contains: [your form identifier]
Time Range: Last 30 days
```

---

### Mobile Sessions

Find sessions from mobile devices.

**Search Criteria:**
```
Device Type: Mobile
Time Range: Last 30 days
```

---

### Sessions with Dead Clicks

Find sessions where users clicked on non-interactive elements.

**Search Criteria:**
```
Frustration Signal: Dead Click
Dead Click Count: >= 2
Time Range: Last 30 days
```

---

## Segment Definitions

### Power Users

Users with high engagement.

**Criteria:**
```
Sessions in last 30 days: >= 10
Total session time: >= 60 minutes
```

---

### New Users

Users first seen recently.

**Criteria:**
```
First Seen: Last 7 days
```

---

### Churned Users

Users who haven't returned.

**Criteria:**
```
Last Seen: > 30 days ago
Total Sessions: >= 3 (were active before)
```

---

### Frustrated Users

Users experiencing UX issues.

**Criteria:**
```
Rage Clicks in last 30 days: >= 3
OR
Dead Clicks in last 30 days: >= 5
OR
Sessions with errors: >= 2
```

---

### Converters

Users who completed a key action.

**Criteria:**
```
Custom Event: [your conversion event]
Time Range: Last 30 days
```

---

## Funnel Definitions

### Signup Funnel

Track conversion through signup flow.

**Steps:**
1. Page: `/signup`
2. Event: `form_submitted` (signup form)
3. Page: `/onboarding` OR `/dashboard`
4. Custom Event: `first_action_completed`

---

### Checkout Funnel

Track e-commerce checkout flow.

**Steps:**
1. Page: `/cart`
2. Page: `/checkout`
3. Event: `payment_info_entered`
4. Page: `/confirmation` OR Event: `purchase_completed`

---

### Feature Adoption Funnel

Track adoption of a specific feature.

**Steps:**
1. Page: `/dashboard` (any page with feature access)
2. Event: `feature_[name]_clicked`
3. Event: `feature_[name]_used`
4. Event: `feature_[name]_completed` (if applicable)

---

## API Search Examples

### Search via Python

```python
from fullstory_client import FullStoryClient

client = FullStoryClient()

# Find rage click sessions
sessions = client.search_sessions(
    filters={
        "type": "FRUSTRATION_SIGNAL",
        "signalType": "rage_click"
    },
    start="2024-01-01",
    end="2024-01-31",
    limit=50
)
```

### Search via Postman

Use the "Search Sessions" requests in the [Postman Collection](../api/postman/).

---

## Tips

1. **Save frequently-used searches** as Segments in FullStory
2. **Combine filters** with AND/OR logic for complex queries
3. **Watch sessions** from search results to understand behavior
4. **Export results** for offline analysis via the Data Export API
5. **Create alerts** on segments for proactive monitoring

---

## Related Files

- [FullStory API Reference](../api/fullstory-api-reference.md)
- [Python Analysis Scripts](../python-analysis/)
