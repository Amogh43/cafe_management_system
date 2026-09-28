"""Sets up logging so every important action is written to logs/cafe.log."""
import logging
import os
from cafe.config import LOG_DIR, LOG_FILE


def setup_logger():
    os.makedirs(LOG_DIR, exist_ok=True)
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )
    return logging.getLogger("cafe")
