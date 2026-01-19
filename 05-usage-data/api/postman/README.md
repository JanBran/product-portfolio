# FullStory Postman Collection

This folder contains a Postman collection and environment for interacting with the FullStory API.

## Files

| File | Description |
|------|-------------|
| `fullstory-api.postman_collection.json` | API collection with all endpoints |
| `fullstory-environment.postman_environment.json` | Environment template with variables |

## Setup Instructions

### 1. Import Collection

1. Open Postman
2. Click **Import** (top left)
3. Drag both JSON files or click **Upload Files**
4. Select both `fullstory-api.postman_collection.json` and `fullstory-environment.postman_environment.json`

### 2. Configure Environment

1. Click the **Environments** tab (left sidebar)
2. Select **FullStory Environment**
3. Set the `api_key` variable to your FullStory API key
4. Click **Save**

### 3. Activate Environment

1. In the top-right corner, click the environment dropdown
2. Select **FullStory Environment**

## Getting Your API Key

1. Log in to [FullStory](https://app.fullstory.com)
2. Go to **Settings** > **API Keys**
3. Click **Create API Key**
4. Select required scopes:
   - `data_export:read` - For data exports
   - `server:write` - For custom events
5. Copy the generated key

## Collection Structure

```
FullStory API/
├── Data Export/
│   ├── List Segments
│   ├── Create Event Export
│   ├── Create Session Export
│   ├── Get Export Status
│   └── List Exports
├── Sessions/
│   ├── Search Sessions
│   ├── Search Sessions with Rage Clicks
│   ├── Search Sessions by Page URL
│   └── Get Session Details
├── Users/
│   ├── Get User
│   ├── Update User Properties
│   └── Send Custom Event
└── Metrics/
    ├── Get Active Users Count
    └── Get Session Metrics
```

## Common Workflows

### Export Event Data

1. Run **List Segments** to get available segment IDs
2. Copy a `segment_id` to environment variables
3. Run **Create Event Export** with desired date range
4. Copy the returned `export_id` to environment variables
5. Run **Get Export Status** until status is `COMPLETED`
6. Download from the provided `downloadUrl`

### Find Frustration Sessions

1. Run **Search Sessions with Rage Clicks**
2. Review returned session IDs
3. Use **Get Session Details** or view in FullStory UI

### Track Custom Events

1. Set the `user_id` variable
2. Modify the **Send Custom Event** body with your event data
3. Send the request

## Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `base_url` | FullStory API base URL | `https://api.fullstory.com` |
| `api_key` | Your FullStory API key | `fskey_xxx...` |
| `segment_id` | Segment ID for exports | `segment_abc123` |
| `export_id` | Export job ID | `export_xyz789` |
| `session_id` | Session ID for lookups | `12345678:67890` |
| `user_id` | User ID for events | `user_123` |

## Tips

- Use **Collection Runner** to execute multiple requests in sequence
- Save responses as examples for documentation
- Use **Pre-request Scripts** to auto-generate timestamps
- Check **Console** (View > Show Postman Console) for debugging
