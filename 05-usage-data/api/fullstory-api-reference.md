# FullStory API Reference

This document provides a reference for the FullStory APIs used for data export and analysis.

## Overview

FullStory provides several APIs for accessing session and event data:

| API | Purpose | Documentation |
|-----|---------|---------------|
| Data Export API | Bulk export of events and sessions | [Docs](https://developer.fullstory.com/data-export) |
| Server API | Custom events & user properties | [Docs](https://developer.fullstory.com/server/v2/introduction) |
| Webhooks | Real-time event notifications | [Docs](https://developer.fullstory.com/webhooks) |

---

## Authentication

### API Key Setup

1. Navigate to **Settings > API Keys** in FullStory
2. Click **Create API Key**
3. Select the appropriate scopes:
   - `data_export:read` - For Data Export API
   - `server:write` - For Server API (custom events)
4. Copy and securely store the API key

### Using the API Key

Include the API key in the `Authorization` header:

```
Authorization: Basic <base64-encoded-api-key>
```

For Postman, use:
- **Type**: Basic Auth
- **Username**: Your API key
- **Password**: (leave empty)

---

## Data Export API

### Base URL
```
https://api.fullstory.com/v2
```

### Endpoints

#### 1. Create Data Export

Creates a new data export job.

```http
POST /segments/{segment_id}/exports
```

**Request Body:**
```json
{
  "type": "EVENT",
  "format": "JSON",
  "start": "2024-01-01T00:00:00Z",
  "end": "2024-01-31T23:59:59Z"
}
```

**Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `type` | string | `EVENT` or `SESSION` |
| `format` | string | `JSON` or `CSV` |
| `start` | ISO 8601 | Start date for export |
| `end` | ISO 8601 | End date for export |

**Response:**
```json
{
  "id": "export_abc123",
  "status": "PENDING",
  "created": "2024-01-15T10:30:00Z"
}
```

#### 2. Get Export Status

Check the status of an export job.

```http
GET /exports/{export_id}
```

**Response:**
```json
{
  "id": "export_abc123",
  "status": "COMPLETED",
  "downloadUrl": "https://storage.fullstory.com/exports/...",
  "expires": "2024-01-22T10:30:00Z"
}
```

**Status Values:**
- `PENDING` - Export job queued
- `PROCESSING` - Export in progress
- `COMPLETED` - Ready for download
- `FAILED` - Export failed

#### 3. List Segments

Get available segments for export.

```http
GET /segments
```

**Response:**
```json
{
  "segments": [
    {
      "id": "segment_123",
      "name": "Active Users",
      "userCount": 15420
    },
    {
      "id": "segment_456",
      "name": "Churned Users",
      "userCount": 3200
    }
  ]
}
```

---

## Server API (Custom Events)

### Send Custom Event

Track custom events from your backend.

```http
POST /v2/users/{user_id}/events
```

**Request Body:**
```json
{
  "name": "Subscription_Upgraded",
  "timestamp": "2024-01-15T14:30:00Z",
  "properties": {
    "plan": "enterprise",
    "previousPlan": "pro",
    "revenue": 299.00
  }
}
```

### Set User Properties

Update user properties (variables).

```http
POST /v2/users/{user_id}
```

**Request Body:**
```json
{
  "displayName": "Jane Smith",
  "email": "jane@example.com",
  "properties": {
    "accountType": "enterprise",
    "companySize": 500,
    "industry": "technology"
  }
}
```

---

## Search API (Sessions)

### Search Sessions

Find sessions matching specific criteria.

```http
POST /v2/sessions/search
```

**Request Body:**
```json
{
  "filter": {
    "type": "AND",
    "filters": [
      {
        "type": "EVENT",
        "eventType": "page",
        "properties": {
          "url": {
            "contains": "/checkout"
          }
        }
      },
      {
        "type": "FRUSTRATION_SIGNAL",
        "signalType": "rage_click"
      }
    ]
  },
  "start": "2024-01-01T00:00:00Z",
  "end": "2024-01-31T23:59:59Z",
  "limit": 100
}
```

---

## Common Event Types

### Standard Events (Auto-captured)

| Event Type | Description | Key Properties |
|------------|-------------|----------------|
| `page` | Page view | `url`, `title`, `referrer` |
| `click` | User click | `element`, `text`, `selector` |
| `input` | Form input | `element`, `field_name` |
| `scroll` | Page scroll | `depth`, `direction` |
| `navigate` | Navigation | `from_url`, `to_url` |

### Frustration Signals

| Signal | Description |
|--------|-------------|
| `rage_click` | Multiple rapid clicks on same element |
| `dead_click` | Click on non-interactive element |
| `error_click` | Click followed by JS error |
| `thrashed_cursor` | Erratic mouse movement |
| `form_abandonment` | User started but didn't submit form |

---

## Rate Limits

| API | Rate Limit |
|-----|------------|
| Data Export | 10 requests/minute |
| Server API | 1000 requests/minute |
| Search API | 100 requests/minute |

---

## Error Handling

### Common Error Codes

| Code | Description | Resolution |
|------|-------------|------------|
| 401 | Unauthorized | Check API key |
| 403 | Forbidden | Verify API key scopes |
| 404 | Not Found | Check resource ID |
| 429 | Too Many Requests | Implement backoff |
| 500 | Server Error | Retry with exponential backoff |

### Error Response Format

```json
{
  "error": {
    "code": "INVALID_REQUEST",
    "message": "The 'start' parameter is required",
    "details": {
      "field": "start"
    }
  }
}
```

---

## Useful Links

- [FullStory Developer Portal](https://developer.fullstory.com/)
- [API Changelog](https://developer.fullstory.com/changelog)
- [Data Export Guide](https://help.fullstory.com/hc/en-us/articles/360020828113)
- [Server API Reference](https://developer.fullstory.com/server/v2/introduction)

---

## Related Files

- [Postman Collection](./postman/fullstory-api.postman_collection.json)
- [Python Analysis Scripts](../python-analysis/)
- [Export Data Directory](../exports/)
