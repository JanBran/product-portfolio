# Python Analysis Setup

This folder contains Python scripts for analyzing exported FullStory data.

## Quick Start

### 1. Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

### 2. Setup Virtual Environment

```bash
# Navigate to this directory
cd 05-usage-data/python-analysis

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Copy the example environment file and add your API key:

```bash
cp .env.example .env
```

Edit `.env` and add your FullStory API key:

```
FULLSTORY_API_KEY=your_api_key_here
```

### 4. Run Analysis

```bash
# Basic analysis on exported data
python analyze_sessions.py

# Or use Jupyter notebooks
jupyter notebook
```

---

## Project Structure

```
python-analysis/
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── .env.example             # Environment variables template
├── .gitignore               # Git ignore rules
├── analyze_sessions.py      # Main analysis script
├── fullstory_client.py      # FullStory API wrapper
└── notebooks/
    └── exploratory_analysis.ipynb  # Jupyter notebook for exploration
```

---

## Exporting Data from FullStory

### Option 1: Manual Export (UI)

1. Go to [FullStory Search](https://app.fullstory.com/ui/search)
2. Create a search with your desired filters
3. Click **Export** → **Download CSV**
4. Save to `../exports/` directory

### Option 2: API Export (Automated)

Use the included scripts or Postman collection:

```python
from fullstory_client import FullStoryClient

client = FullStoryClient()

# Create an export job
export = client.create_export(
    segment_id="your_segment_id",
    start_date="2024-01-01",
    end_date="2024-01-31",
    export_type="EVENT",
    format="JSON"
)

# Check status and download when ready
status = client.get_export_status(export['id'])
if status['status'] == 'COMPLETED':
    client.download_export(status['downloadUrl'], '../exports/events.json')
```

### Option 3: Postman Export

1. Use the [Postman Collection](../api/postman/)
2. Run **Create Event Export** request
3. Poll **Get Export Status** until completed
4. Download from the provided URL

---

## Data Files

Place exported data files in `../exports/`:

| File Pattern | Description |
|--------------|-------------|
| `events_YYYY-MM-DD.json` | Event data export |
| `sessions_YYYY-MM-DD.csv` | Session data export |
| `users_YYYY-MM-DD.json` | User data export |

---

## Available Scripts

### analyze_sessions.py

Basic session analysis:

```bash
python analyze_sessions.py --input ../exports/sessions.csv
```

Outputs:
- Session count by day
- Average session duration
- Top pages by visits
- Frustration signal summary

### fullstory_client.py

API client for programmatic access:

```python
from fullstory_client import FullStoryClient

client = FullStoryClient()

# List segments
segments = client.list_segments()

# Search sessions
sessions = client.search_sessions(
    filters={"type": "FRUSTRATION_SIGNAL", "signalType": "rage_click"},
    start="2024-01-01",
    end="2024-01-31"
)
```

---

## Notebooks

### exploratory_analysis.ipynb

Interactive notebook for data exploration:

1. Load exported data
2. Basic statistics
3. Visualizations (session trends, funnel analysis)
4. Cohort retention analysis

To run:

```bash
jupyter notebook notebooks/exploratory_analysis.ipynb
```

---

## Common Analysis Examples

### Session Count Over Time

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../exports/sessions.csv')
df['date'] = pd.to_datetime(df['session_start']).dt.date

daily_sessions = df.groupby('date').size()
daily_sessions.plot(kind='line', title='Daily Sessions')
plt.show()
```

### Frustration Signal Analysis

```python
df = pd.read_json('../exports/events.json', lines=True)

frustration_events = df[df['event_type'].isin([
    'rage_click', 'dead_click', 'error_click'
])]

print(frustration_events['event_type'].value_counts())
```

### Funnel Conversion

```python
# Define funnel steps
funnel_steps = ['page_home', 'page_signup', 'user_created', 'first_action']

def calculate_funnel(df, steps):
    results = {}
    for step in steps:
        count = df[df['event_name'] == step]['user_id'].nunique()
        results[step] = count
    return results

funnel = calculate_funnel(df, funnel_steps)
print(funnel)
```

---

## Troubleshooting

### "Module not found" error

Make sure you've activated the virtual environment:

```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### API authentication error

1. Check your API key in `.env`
2. Verify the key has correct scopes in FullStory settings
3. Ensure the key hasn't expired

### Large file handling

For files > 100MB:

```python
# Read in chunks
chunks = pd.read_csv('large_file.csv', chunksize=10000)
for chunk in chunks:
    process(chunk)
```

---

## Related Resources

- [FullStory API Reference](../api/fullstory-api-reference.md)
- [Postman Collection](../api/postman/)
- [pandas Documentation](https://pandas.pydata.org/docs/)
- [matplotlib Documentation](https://matplotlib.org/stable/contents.html)
