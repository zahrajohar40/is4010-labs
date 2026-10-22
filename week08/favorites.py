"""Favorites manager: stores named locations in a JSON file."""

import json
import os


class FavoritesManager:
    """Save and look up favorite locations by (case-insensitive) name."""

    def __init__(self, filename):
        self.filename = filename
        self._favorites = self._load()

    # ---------- persistence ----------
    def _load(self):
        """Return the saved favorites, or {} if the file is missing/corrupted."""
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (OSError, ValueError):  # missing file, bad JSON, bad encoding
            return {}
        if not isinstance(data, dict):
            return {}
        # Keep only well-formed entries: string name -> string location
        return {
            str(k).lower(): v
            for k, v in data.items()
            if isinstance(v, str)
        }

    def _save(self):
        folder = os.path.dirname(self.filename)
        if folder:
            os.makedirs(folder, exist_ok=True)
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self._favorites, f, indent=2)

    # ---------- public API ----------
    def add(self, name, location):
        """Add a favorite. Return True if added, False if the name exists."""
        key = name.strip().lower()
        if key in self._favorites:
            return False
        self._favorites[key] = location
        self._save()
        return True

    def remove(self, name):
        """Remove a favorite. Return True if removed, False if not found."""
        key = name.strip().lower()
        if key not in self._favorites:
            return False
        del self._favorites[key]
        self._save()
        return True

    def list_all(self):
        """Return a copy of all favorites as {name: location}."""
        return dict(self._favorites)

    def get_location(self, name):
        """Return the location for a name, or None if it is not saved."""
        return self._favorites.get(name.strip().lower())