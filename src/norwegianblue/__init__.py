#!/usr/bin/env python3
"""
Python interface to endoflife.date API
https://endoflife.date/docs/api/
"""
from __future__ import annotations

import datetime as dt
import json
import logging
import os
import sys

from dateutil.relativedelta import relativedelta
from termcolor import colored

from norwegianblue import _cache

from ._version import version as __version__

BASE_URL = "https://endoflife.date/api/"
USER_AGENT = f"norwegianblue/{__version__}"
ERROR_404_TEXT = "Product not found, run 'eol all' for list"


def norwegianblue(
    product: str = "all", format: str = "markdown", color: str = "yes"
) -> str:
    """Call the API and return result"""
    if product == "norwegianblue":
        from ._data import prefix, res
    else:
        url = BASE_URL + product.lower() + ".json"
        cache_file = _cache.filename(url)
        logging.info("Human URL:\thttps://endoflife.date/%s", product.lower())
        logging.info("API URL:\t%s", url)
        logging.info(
            "Source URL:\thttps://github.com/endoflife-date/endoflife.date/"
            "blob/master/products/%s.md",
            product.lower(),
        )
        logging.info("Cache file:\t%s", cache_file)

        res = {}
        if cache_file.is_file():
            logging.info("Cache file exists")
            res = _cache.load(cache_file)

    if res == {}:
        # No cache, or couldn't load cache
        import httpx

        r = httpx.get(url, follow_redirects=True, headers={"User-Agent": USER_AGENT})

        logging.info("HTTP status code: %d", r.status_code)
        if r.status_code == 404:
            return ERROR_404_TEXT

        # Raise if we made a bad request
        # (4XX client error or 5XX server error response)
        r.raise_for_status()

        res = r.json()

        _cache.save(cache_file, res)

    if format == "json":
        return json.dumps(res)

    data: list[dict] = list(res)

    if product == "all":
        return "\n".join(data)

    data = _ltsify(data)
    if color != "no" and format != "html" and _can_do_colour():
        data = _colourify(data)

    output = _tabulate(data, format)
    logging.info("")

    if product == "norwegianblue":
        return prefix + output

    return output


def _ltsify(data: list[dict]) -> list[dict]:
    """If a cycle is LTS, append LTS to the cycle version and remove the LTS column"""
    for cycle in data:
        if "lts" in cycle:
            if cycle["lts"]:
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

    # Rename some headers
    for row in data:
        if "releaseDate" in row:
            row["release"] = row.pop("releaseDate")
        if "latestReleaseDate" in row:
            row["latest release"] = row.pop("latestReleaseDate")

    headers = sorted(set().union(*(d.keys() for d in data)))

    # Skip some headers, only used internally at https://endoflife.date
    for header in ("cycleShortHand", "latestShortHand"):
        if header in headers:
            headers.remove(header)

    # Put headers in preferred order, with the rest at the end
    new_headers = []
    for preferred in (
        "cycle",
        "release",
        "latest",
        "latest release",
        "support",
        "discontinued",
        "eol",
    ):
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
            x.align[header] = "l"

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
