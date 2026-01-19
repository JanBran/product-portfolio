"""
FullStory API Client

A simple wrapper for the FullStory API to fetch and export data.
"""

import os
import time
import requests
from datetime import datetime
from typing import Optional
from dotenv import load_dotenv

load_dotenv()


class FullStoryClient:
    """Client for interacting with the FullStory API."""

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the FullStory client.

        Args:
            api_key: FullStory API key. If not provided, reads from FULLSTORY_API_KEY env var.
        """
        self.api_key = api_key or os.getenv("FULLSTORY_API_KEY")
        if not self.api_key:
            raise ValueError(
                "API key required. Set FULLSTORY_API_KEY env var or pass api_key parameter."
            )

        self.base_url = os.getenv("FULLSTORY_API_URL", "https://api.fullstory.com")
        self.session = requests.Session()
        self.session.auth = (self.api_key, "")
        self.session.headers.update({"Content-Type": "application/json"})

    def _request(self, method: str, endpoint: str, **kwargs) -> dict:
        """Make an API request."""
        url = f"{self.base_url}{endpoint}"
        response = self.session.request(method, url, **kwargs)
        response.raise_for_status()
        return response.json() if response.content else {}

    # -------------------------------------------------------------------------
    # Segments
    # -------------------------------------------------------------------------

    def list_segments(self) -> list:
        """
        List all available segments.

        Returns:
            List of segment objects with id, name, and userCount.
        """
        result = self._request("GET", "/v2/segments")
        return result.get("segments", [])

    # -------------------------------------------------------------------------
    # Data Export
    # -------------------------------------------------------------------------

    def create_export(
        self,
        segment_id: str,
        start_date: str,
        end_date: str,
        export_type: str = "EVENT",
        format: str = "JSON",
    ) -> dict:
        """
        Create a new data export job.

        Args:
            segment_id: The segment ID to export.
            start_date: Start date in YYYY-MM-DD format.
            end_date: End date in YYYY-MM-DD format.
            export_type: "EVENT" or "SESSION".
            format: "JSON" or "CSV".

        Returns:
            Export job object with id and status.
        """
        payload = {
            "type": export_type,
            "format": format,
            "start": f"{start_date}T00:00:00Z",
            "end": f"{end_date}T23:59:59Z",
        }
        return self._request("POST", f"/v2/segments/{segment_id}/exports", json=payload)

    def get_export_status(self, export_id: str) -> dict:
        """
        Check the status of an export job.

        Args:
            export_id: The export job ID.

        Returns:
            Export status object with id, status, and downloadUrl (if completed).
        """
        return self._request("GET", f"/v2/exports/{export_id}")

    def wait_for_export(
        self, export_id: str, poll_interval: int = 10, max_wait: int = 600
    ) -> dict:
        """
        Wait for an export to complete.

        Args:
            export_id: The export job ID.
            poll_interval: Seconds between status checks.
            max_wait: Maximum seconds to wait.

        Returns:
            Final export status.

        Raises:
            TimeoutError: If export doesn't complete within max_wait.
            RuntimeError: If export fails.
        """
        start_time = time.time()
        while time.time() - start_time < max_wait:
            status = self.get_export_status(export_id)
            if status["status"] == "COMPLETED":
                return status
            if status["status"] == "FAILED":
                raise RuntimeError(f"Export failed: {status}")
            print(f"Export status: {status['status']}. Waiting...")
            time.sleep(poll_interval)
        raise TimeoutError(f"Export did not complete within {max_wait} seconds")

    def download_export(self, download_url: str, output_path: str) -> str:
        """
        Download an export file.

        Args:
            download_url: The download URL from export status.
            output_path: Local path to save the file.

        Returns:
            The output path.
        """
        response = requests.get(download_url, stream=True)
        response.raise_for_status()
        with open(output_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        return output_path

    # -------------------------------------------------------------------------
    # Sessions
    # -------------------------------------------------------------------------

    def search_sessions(
        self,
        filters: dict,
        start: str,
        end: str,
        limit: int = 100,
    ) -> list:
        """
        Search for sessions matching criteria.

        Args:
            filters: Filter object (see API docs for structure).
            start: Start date in YYYY-MM-DD format.
            end: End date in YYYY-MM-DD format.
            limit: Maximum sessions to return.

        Returns:
            List of session objects.
        """
        payload = {
            "filter": filters,
            "start": f"{start}T00:00:00Z",
            "end": f"{end}T23:59:59Z",
            "limit": limit,
        }
        result = self._request("POST", "/v2/sessions/search", json=payload)
        return result.get("sessions", [])

    def search_rage_click_sessions(
        self, start: str, end: str, limit: int = 50
    ) -> list:
        """
        Find sessions with rage clicks.

        Args:
            start: Start date in YYYY-MM-DD format.
            end: End date in YYYY-MM-DD format.
            limit: Maximum sessions to return.

        Returns:
            List of session objects with rage clicks.
        """
        filters = {"type": "FRUSTRATION_SIGNAL", "signalType": "rage_click"}
        return self.search_sessions(filters, start, end, limit)

    def search_sessions_by_page(
        self, url_contains: str, start: str, end: str, limit: int = 100
    ) -> list:
        """
        Find sessions that visited a specific page.

        Args:
            url_contains: Substring to match in page URLs.
            start: Start date in YYYY-MM-DD format.
            end: End date in YYYY-MM-DD format.
            limit: Maximum sessions to return.

        Returns:
            List of session objects.
        """
        filters = {
            "type": "EVENT",
            "eventType": "page",
            "properties": {"url": {"contains": url_contains}},
        }
        return self.search_sessions(filters, start, end, limit)

    # -------------------------------------------------------------------------
    # Users
    # -------------------------------------------------------------------------

    def get_user(self, user_id: str) -> dict:
        """
        Get user details.

        Args:
            user_id: The user ID.

        Returns:
            User object with properties.
        """
        return self._request("GET", f"/v2/users/{user_id}")

    def update_user(self, user_id: str, properties: dict) -> dict:
        """
        Update user properties.

        Args:
            user_id: The user ID.
            properties: Dictionary of properties to set.

        Returns:
            Updated user object.
        """
        return self._request("POST", f"/v2/users/{user_id}", json=properties)

    def send_event(
        self,
        user_id: str,
        event_name: str,
        properties: Optional[dict] = None,
        timestamp: Optional[str] = None,
    ) -> dict:
        """
        Send a custom event for a user.

        Args:
            user_id: The user ID.
            event_name: Name of the event.
            properties: Optional event properties.
            timestamp: Optional ISO 8601 timestamp (defaults to now).

        Returns:
            Response object.
        """
        payload = {
            "name": event_name,
            "timestamp": timestamp or datetime.utcnow().isoformat() + "Z",
        }
        if properties:
            payload["properties"] = properties
        return self._request("POST", f"/v2/users/{user_id}/events", json=payload)


# -----------------------------------------------------------------------------
# CLI usage
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    # Example usage
    client = FullStoryClient()

    print("Fetching segments...")
    segments = client.list_segments()
    for seg in segments[:5]:
        print(f"  - {seg['name']} ({seg['id']}): {seg.get('userCount', 'N/A')} users")
