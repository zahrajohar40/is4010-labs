"""Command-line weather application."""

import argparse
import importlib
import os
import sys

try:  # imported as a package (pytest: from week08 import weather)
    from week08.favorites import FavoritesManager
    from week08.weather_api import WeatherAPI, format_current_weather, format_forecast
except ImportError:  # run as a script (python week08/weather.py)
    from favorites import FavoritesManager
    from weather_api import WeatherAPI, format_current_weather, format_forecast

FAVORITES_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "favorites.json"
)


def load_api_key():
    """Return the API key from WEATHER_API_KEY, else from config.py, else None."""
    key = os.environ.get("WEATHER_API_KEY")
    if key:
        return key
        config = None
    for module_name in ("week08.config", "config"):
        try:
            config = importlib.import_module(module_name)
            break
        except ImportError:
            continue
    if config is None:
        return None
    for attr in ("WEATHER_API_KEY", "API_KEY", "api_key"):
        value = getattr(config, attr, None)
        if value:
            return value
    return None


def build_parser():
    """Build the argparse parser with current/forecast/favorites commands."""
    parser = argparse.ArgumentParser(description="Weather CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    current = sub.add_parser("current", help="show current weather")
    current.add_argument("location", help="city or saved favorite name")

    forecast = sub.add_parser("forecast", help="show forecast")
    forecast.add_argument("location", help="city or saved favorite name")
    forecast.add_argument("--days", type=int, default=3, help="days (1-3)")

    fav = sub.add_parser("favorites", help="manage favorite locations")
    fav_sub = fav.add_subparsers(dest="favorites_command", required=True)

    fav_add = fav_sub.add_parser("add", help="add a favorite")
    fav_add.add_argument("name")
    fav_add.add_argument("location")

    fav_sub.add_parser("list", help="list favorites")

    fav_remove = fav_sub.add_parser("remove", help="remove a favorite")
    fav_remove.add_argument("name")

    return parser


def _error(message):
    print(message, file=sys.stderr)
    return 1


def _handle_favorites(args, favorites):
    if args.favorites_command == "add":
        if favorites.add(args.name, args.location):
            print(f"Added favorite: {args.name} -> {args.location}")
            return 0
        return _error(f"Error: favorite '{args.name}' already exists.")

    if args.favorites_command == "remove":
        if favorites.remove(args.name):
            print(f"Removed favorite: {args.name}")
            return 0
        return _error(f"Error: favorite '{args.name}' not found.")

    # list
    items = favorites.list_all()
    if not items:
        print("No favorites saved.")
    else:
        for name, location in sorted(items.items()):
            print(f"{name}: {location}")
    return 0


def main(argv=None):
    """Run the CLI. Return 0 on success, 1 on errors."""
    args = build_parser().parse_args(argv)
    favorites = FavoritesManager(FAVORITES_FILE)

    if args.command == "favorites":
        return _handle_favorites(args, favorites)

    api_key = load_api_key()
    if not api_key:
        return _error(
            "Error: no API key found. Set WEATHER_API_KEY or add it to "
            "week08/config.py."
        )

    # A saved favorite name can stand in for a location.
    location = favorites.get_location(args.location) or args.location
    api = WeatherAPI(api_key)

    if args.command == "current":
        data = api.get_current_weather(location)
        if data is None:
            return _error("Error: could not retrieve current weather.")
        print(format_current_weather(data))
        return 0

    # forecast
    try:
        data = api.get_forecast(location, args.days)
    except ValueError as exc:
        return _error(f"Error: {exc}")
    if data is None:
        return _error("Error: could not retrieve forecast.")
    print(format_forecast(data))
    return 0


if __name__ == "__main__":
    sys.exit(main())