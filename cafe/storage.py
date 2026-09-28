"""Reading and writing JSON files safely (persistent storage)."""
import copy
import json
import logging
import os

log = logging.getLogger("cafe")


def load_json(filepath, default):
    """Return data from a JSON file, or a copy of `default` if missing/corrupt."""
    if not os.path.exists(filepath):
        return copy.deepcopy(default)
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError) as error:
        log.error("Could not read %s: %s", filepath, error)
        return copy.deepcopy(default)


def save_json(filepath, data):
    """Write data to a JSON file. Returns True on success."""
    try:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        return True
    except OSError as error:
        log.error("Could not save %s: %s", filepath, error)
        return False
