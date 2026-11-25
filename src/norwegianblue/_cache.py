"""
Cache functions
"""

from __future__ import annotations

import datetime as dt
from pathlib import Path

from platformdirs import user_cache_dir

CACHE_DIR = Path(user_cache_dir("norwegianblue"))


def _slugify(text: str) -> str:
    """Lowercase, replace runs of non-alphanumerics with a dash, trim dashes"""
    import re

    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def filename(product: str) -> Path:
    """yyyy-mm-dd-product.json"""
    today = dt.datetime.now(dt.UTC).strftime("%Y-%m-%d")
    return CACHE_DIR / f"{today}-{_slugify(product)}.json"


def load(cache_file: Path):
    """Load data from cache_file"""
    if not cache_file.exists():
        return {}

    import json

    with cache_file.open("r") as f:
        try:
            data = json.load(f)
        except json.decoder.JSONDecodeError:
            return {}

    return data


def save(cache_file: Path, data) -> None:
    """Save data to cache_file"""
    import json

    try:
        if not CACHE_DIR.exists():
            CACHE_DIR.mkdir(parents=True)

        with cache_file.open("w") as f:
            json.dump(data, f)

    except OSError:
        pass


def clear(clear_all: bool = False) -> None:
    """Delete all or old cache files"""
    if not CACHE_DIR.is_dir():
        return
    # Flat directory: iterdir() avoids importing glob (~3 ms) on every run
    today = dt.datetime.now(dt.UTC).strftime("%Y-%m-%d")
    for cache_file in CACHE_DIR.iterdir():
        if cache_file.suffix != ".json":
            continue
        if clear_all or not cache_file.name.startswith(today):
            cache_file.unlink()
