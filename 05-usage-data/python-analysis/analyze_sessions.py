"""
Session Analysis Script

Analyzes exported FullStory session data and produces basic statistics.

Usage:
    python analyze_sessions.py --input ../exports/sessions.csv
    python analyze_sessions.py --input ../exports/events.json --format json
"""

import argparse
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime


def load_data(file_path: str, format: str = "auto") -> pd.DataFrame:
    """Load data from CSV or JSON file."""
    path = Path(file_path)

    if format == "auto":
        format = path.suffix.lower().replace(".", "")

    if format == "csv":
        return pd.read_csv(path)
    elif format == "json":
        return pd.read_json(path, lines=True)
    else:
        raise ValueError(f"Unsupported format: {format}")


def analyze_sessions(df: pd.DataFrame) -> dict:
    """
    Perform basic session analysis.

    Returns dict with analysis results.
    """
    results = {}

    # Basic counts
    results["total_records"] = len(df)
    print(f"\n📊 Total records: {len(df):,}")

    # Identify date column (common names)
    date_cols = [
        "session_start",
        "timestamp",
        "created_at",
        "date",
        "event_time",
        "SessionStart",
    ]
    date_col = None
    for col in date_cols:
        if col in df.columns:
            date_col = col
            break

    if date_col:
        df["_date"] = pd.to_datetime(df[date_col]).dt.date
        daily_counts = df.groupby("_date").size()

        results["date_range"] = {
            "start": str(daily_counts.index.min()),
            "end": str(daily_counts.index.max()),
        }
        results["daily_average"] = daily_counts.mean()

        print(f"\n📅 Date range: {results['date_range']['start']} to {results['date_range']['end']}")
        print(f"📈 Average records per day: {results['daily_average']:.1f}")

        # Plot daily trend
        plt.figure(figsize=(12, 4))
        daily_counts.plot(kind="line", marker="o", markersize=3)
        plt.title("Records per Day")
        plt.xlabel("Date")
        plt.ylabel("Count")
        plt.tight_layout()
        plt.savefig("daily_trend.png", dpi=100)
        print("\n💾 Saved daily_trend.png")

    # User analysis
    user_cols = ["user_id", "userId", "uid", "UserID"]
    user_col = None
    for col in user_cols:
        if col in df.columns:
            user_col = col
            break

    if user_col:
        unique_users = df[user_col].nunique()
        results["unique_users"] = unique_users
        print(f"\n👥 Unique users: {unique_users:,}")

    # Session duration (if available)
    duration_cols = ["session_duration", "duration", "SessionDuration", "duration_ms"]
    for col in duration_cols:
        if col in df.columns:
            # Convert to seconds if milliseconds
            duration = df[col]
            if duration.mean() > 10000:  # Likely milliseconds
                duration = duration / 1000

            results["avg_session_duration_seconds"] = duration.mean()
            results["median_session_duration_seconds"] = duration.median()

            print(f"\n⏱️  Average session duration: {duration.mean():.1f}s")
            print(f"⏱️  Median session duration: {duration.median():.1f}s")
            break

    # Page analysis (if available)
    page_cols = ["page_url", "url", "PageUrl", "page"]
    for col in page_cols:
        if col in df.columns:
            top_pages = df[col].value_counts().head(10)
            results["top_pages"] = top_pages.to_dict()

            print("\n📄 Top 10 pages:")
            for page, count in top_pages.items():
                print(f"   {count:,} - {page[:60]}...")
            break

    # Event type analysis (if available)
    event_cols = ["event_type", "eventType", "type", "EventType", "event_name"]
    for col in event_cols:
        if col in df.columns:
            event_counts = df[col].value_counts()
            results["event_types"] = event_counts.to_dict()

            print(f"\n🎯 Event types:")
            for event, count in event_counts.head(10).items():
                print(f"   {count:,} - {event}")
            break

    # Frustration signals (if available)
    frustration_types = ["rage_click", "dead_click", "error_click", "thrashed_cursor"]
    if "event_type" in df.columns or "signal_type" in df.columns:
        col = "event_type" if "event_type" in df.columns else "signal_type"
        frustration = df[df[col].isin(frustration_types)]
        if len(frustration) > 0:
            print(f"\n😤 Frustration signals found: {len(frustration):,}")
            print(frustration[col].value_counts())
            results["frustration_signals"] = len(frustration)

    return results


def main():
    parser = argparse.ArgumentParser(description="Analyze FullStory session data")
    parser.add_argument(
        "--input",
        "-i",
        required=True,
        help="Path to input file (CSV or JSON)",
    )
    parser.add_argument(
        "--format",
        "-f",
        choices=["csv", "json", "auto"],
        default="auto",
        help="Input file format (default: auto-detect)",
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Path to save results JSON (optional)",
    )

    args = parser.parse_args()

    print(f"Loading data from {args.input}...")
    df = load_data(args.input, args.format)

    print(f"\nColumns found: {', '.join(df.columns[:10])}")
    if len(df.columns) > 10:
        print(f"  ... and {len(df.columns) - 10} more")

    results = analyze_sessions(df)

    if args.output:
        import json

        with open(args.output, "w") as f:
            json.dump(results, f, indent=2, default=str)
        print(f"\n💾 Results saved to {args.output}")

    print("\n✅ Analysis complete!")


if __name__ == "__main__":
    main()
