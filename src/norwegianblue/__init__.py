#!/usr/bin/env python3
"""
Python interface to endoflife.date API
https://endoflife.date/docs/api/
"""
from __future__ import annotations

import atexit
import datetime as dt
import json
import os
import sys
from pathlib import Path

import httpx
from dateutil.relativedelta import relativedelta
from platformdirs import user_cache_dir
from slugify import slugify
from termcolor import colored

from ._version import version as __version__

BASE_URL = "https://endoflife.date/api/"
CACHE_DIR = Path(user_cache_dir("norwegianblue"))
USER_AGENT = f"norwegianblue/{__version__}"
ERROR_404_TEXT = "Product not found, run 'eol all' for list"


def _print_verbose(verbose, *args, **kwargs):
    """Print if verbose"""
    if verbose:
        _print_stderr(*args, **kwargs)


def _print_stderr(*args, **kwargs):
    """Print to stderr"""
    print(*args, file=sys.stderr, **kwargs)


def _cache_filename(url):
    """yyyy-mm-dd-url-slug.json"""
    today = dt.datetime.utcnow().strftime("%Y-%m-%d")
    slug = slugify(url)
    filename = CACHE_DIR / f"{today}-{slug}.json"

    return filename


def _load_cache(cache_file):
    if not cache_file.exists():
        return {}

    with cache_file.open("r") as f:
        try:
            data = json.load(f)
        except json.decoder.JSONDecodeError:
            return {}

    return data


def _save_cache(cache_file, data):
    try:
        if not CACHE_DIR.exists():
            CACHE_DIR.mkdir(parents=True)

        with cache_file.open("w") as f:
            json.dump(data, f)

    except OSError:
        pass


def _clear_cache():
    """Delete old cache files, run as last task"""
    cache_files = CACHE_DIR.glob("**/*.json")
    today = dt.datetime.utcnow().strftime("%Y-%m-%d")
    for cache_file in cache_files:
        if not cache_file.name.startswith(today):
            cache_file.unlink()


atexit.register(_clear_cache)


def norwegianblue(
    product: str = "all",
    format: str = "markdown",
    color: str = "yes",
    verbose: bool = False,
) -> str:
    """Call the API and return result"""
    if product == "norwegianblue":
        from ._data import prefix, res
    else:
        url = BASE_URL + product.lower() + ".json"
        cache_file = _cache_filename(url)
        _print_verbose(verbose, f"Human URL:\thttps://endoflife.date/{product.lower()}")
        _print_verbose(verbose, f"API URL:\t{url}")
        _print_verbose(verbose, f"Cache file:\t{cache_file}")

        res = {}
        if cache_file.is_file():
            _print_verbose(verbose, "Cache file exists")
            res = _load_cache(cache_file)

    if res == {}:
        # No cache, or couldn't load cache
        r = httpx.get(url, headers={"User-Agent": USER_AGENT})

        _print_verbose(verbose, "HTTP status code:", r.status_code)
        if r.status_code == 404:
            return ERROR_404_TEXT

        # Raise if we made a bad request
        # (4XX client error or 5XX server error response)
        r.raise_for_status()

        res = r.json()

        _save_cache(cache_file, res)

    if format == "json":
        return json.dumps(res)

    data: list[dict] = list(res)

    if product == "all":
        return "\n".join(data)

    data = _ltsify(data)
    if color != "no" and format != "html" and _can_do_colour():
        data = _colourify(data)

    output = _tabulate(data, format)
    _print_verbose(verbose, "")

    if product == "norwegianblue":
        return prefix + output

    return output


def _ltsify(data: list[dict]) -> list[dict]:
    """If a cycle is LTS, append LTS to the cycle version and remove the LTS column"""
    for cycle in data:
        if "lts" in cycle:
            cycle["cycle"] = f"{cycle['cycle']} LTS"
            cycle.pop("lts")
    return data


def _can_do_colour() -> bool:
    """Check https://no-color.org env vars and for dumb terminal"""
    if "NO_COLOR" in os.environ:
        return False
    if "FORCE_COLOR" in os.environ:
        return True
    return (
        hasattr(sys.stdout, "isatty")
        and sys.stdout.isatty()
        and os.environ.get("TERM") != "dumb"
    )


def _colourify(data: list[dict]) -> list[dict]:
    """Add colour to dates:
    red: in the past
    yellow: will pass in six months
    green: will pass after six months
    """
    now = dt.datetime.utcnow()
    six_months_from_now = now + relativedelta(months=+6)

    for cycle in data:
        for property_ in ("support", "eol", "discontinued"):
            if property_ not in cycle:
                continue

            # Handle Boolean
            if isinstance(cycle[property_], bool):
                if property_ == "support":
                    colour = "green" if cycle["support"] else "red"
                else:  # "eol" and "discontinued"
                    colour = "red" if cycle[property_] else "green"
                cycle[property_] = colored(cycle[property_], colour)
                continue

            # Handle date
            date_str = cycle[property_]
            # Convert "2020-01-01" string to datetime
            date_datetime = dt.datetime.strptime(date_str, "%Y-%m-%d")
            if date_datetime < now:
                cycle[property_] = colored(date_str, "red")
            elif date_datetime < six_months_from_now:
                cycle[property_] = colored(date_str, "yellow")
            else:
                cycle[property_] = colored(date_str, "green")
    return data


def _tabulate(data: list[dict], format: str = "markdown") -> str:
    """Return data in specified format"""

    headers = sorted(set().union(*(d.keys() for d in data)))

    # Skip some headers, only used internally at https://endoflife.date
    for header in ("cycleShortHand", "latestShortHand"):
        if header in headers:
            headers.remove(header)

    # Put headers in preferred order, with the rest at the end
    new_headers = []
    for preferred in ("cycle", "latest", "release", "support", "discontinued", "eol"):
        if preferred in headers:
            new_headers.append(preferred)
            headers.remove(preferred)
    headers = new_headers + headers

    if format == "markdown":
        return _prettytable(headers, data)
    else:
        return _pytablewriter(headers, data, format)


def _prettytable(headers: list[str], data: list[dict]) -> str:
    from prettytable import MARKDOWN, PrettyTable

    x = PrettyTable()
    x.set_style(MARKDOWN)

    for header in headers:
        col_data = [row[header] if header in row else "" for row in data]
        x.add_column(header, col_data)
        if header in ("cycle", "latest", "link"):
            x.align = "l"

    return x.get_string()


def _pytablewriter(headers: list[str], data: list[dict], format: str) -> str:
    from pytablewriter import (
        HtmlTableWriter,
        RstSimpleTableWriter,
        String,
        TsvTableWriter,
    )
    from pytablewriter.style import Align, Style

    format_writers = {
        "html": HtmlTableWriter,
        "rst": RstSimpleTableWriter,
        "tsv": TsvTableWriter,
    }
    writer = format_writers[format]()
    if format != "html":
        writer.margin = 1
    writer.headers = headers
    writer.value_matrix = data

    # Custom alignment and format
    column_styles = []
    type_hints = []

    for header in headers:
        align = Align.AUTO
        type_hint = None
        if header in ("cycle", "latest"):
            type_hint = String
        style = Style(align=align)
        column_styles.append(style)
        type_hints.append(type_hint)

        writer.column_styles = column_styles
        writer.type_hints = type_hints

    return writer.dumps()
