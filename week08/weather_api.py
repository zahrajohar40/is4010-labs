"""WeatherAPI.com client and output formatters."""

import requests


class WeatherAPI:
    """Small client for the WeatherAPI.com current and forecast endpoints."""

    def __init__(self, api_key, base_url="https://api.weatherapi.com/v1"):
        self.api_key = api_key
        self.base_url = base_url

    def _get(self, endpoint, params):
        """GET an endpoint and return parsed JSON, or None on any error."""
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.get(url, params=params, timeout=10)
            raise_for_status = getattr(response, "raise_for_status", None)
            if callable(raise_for_status):
                raise_for_status()
            return response.json()
        except (requests.exceptions.RequestException, ValueError):
            # RequestException: network/HTTP problems
            # ValueError: invalid JSON in the response body
            return None

    def get_current_weather(self, location):
        """Return current weather JSON for a location, or None on error."""
        params = {"key": self.api_key, "q": location}
        return self._get("current.json", params)

    def get_forecast(self, location, days=3):
        """Return forecast JSON for 1-3 days, or None on error."""
        if not isinstance(days, int) or isinstance(days, bool) or not 1 <= days <= 3:
            raise ValueError("days must be between 1 and 3")
        params = {"key": self.api_key, "q": location, "days": days}
        return self._get("forecast.json", params)


def format_current_weather(data):
    """Format as 'CITY, COUNTRY: TEMP°F, CONDITION'."""
    location = data["location"]
    current = data["current"]
    return (
        f"{location['name']}, {location['country']}: "
        f"{current['temp_f']}°F, {current['condition']['text']}"
    )


def format_forecast(data):
    """Format each day as 'DATE: high TEMP°F, low TEMP°F, CONDITION'."""
    lines = []
    for entry in data["forecast"]["forecastday"]:
        day = entry["day"]
        lines.append(
            f"{entry['date']}: high {day['maxtemp_f']}°F, "
            f"low {day['mintemp_f']}°F, {day['condition']['text']}"
        )
    return "\n".join(lines)