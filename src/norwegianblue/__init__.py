"""
Python interface to endoflife.date API
https://endoflife.date/docs/api/
"""
from __future__ import annotations

import datetime as dt
import importlib.metadata
import json
import logging
from functools import lru_cache

from dateutil.relativedelta import relativedelta
from rich import print
from termcolor import colored

from norwegianblue import _cache

__version__ = importlib.metadata.version(__name__)


__all__ = ["__version__"]

# BASE_URL = "https://endoflife.date/api/"
BASE_URL = "https://deploy-preview-2080--endoflife-date.netlify.app/api/v1/"
USER_AGENT = f"norwegianblue/{__version__}"
ERROR_404_TEXT = "Product '{}' not found, run 'eol all' for list. Did you mean: '{}'?"


def norwegianblue(
    product: str = "all",
    format: str = "pretty",
    color: str = "yes",
    show_title: bool = False,
) -> str:
    """Call the API and return result"""
    if format == "md":
        format = "markdown"
    if product == "norwegianblue":
        from ._data import prefix, res
    else:
        url = BASE_URL + "products/" + product.lower()
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
            suggestion = suggest_product(product)
            msg = ERROR_404_TEXT.format(product, suggestion)
            raise ValueError(msg)

        # Raise if we made a bad request
        # (4XX client error or 5XX server error response)
        r.raise_for_status()

        res = r.json()

        _cache.save(cache_file, res)

    if format == "json":
        return json.dumps(res)

    data: list[dict] = list(res["result"]["cycles"])

    if product == "all":
        return "\n".join(data)

    # data = _ltsify(data)  # TODO remove
    if color != "no" and format not in ("html", "yaml"):
        data = _colourify(data)

    output = _tabulate(data, format, color, product if show_title else None)
    logging.info("")

    if product == "norwegianblue":
        return prefix + output

    return output


@lru_cache(maxsize=None)
def suggest_product(product: str) -> str:
    import warnings

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=UserWarning)
        from thefuzz import process

    # Get all known products from the API or cache
    all_products = norwegianblue("all").splitlines()

    # Find the closest match
    result = process.extractOne(product, all_products)
    logging.info("Suggestion:\t%s (score: %d)", *result)
    return result[0]


def _ltsify(data: list[dict]) -> list[dict]:
    """If a cycle is LTS, append LTS to the cycle version and remove the LTS column"""
    for cycle in data:
        if "lts" in cycle:
            if cycle["lts"]:
                cycle["name"] = f"{cycle['name']} LTS"
            cycle.pop("lts")
    return data


def _colourify(data: list[dict]) -> list[dict]:
    """Add colour to dates:
    red: in the past
    yellow: will pass in six months
    green: will pass after six months
    """
    # TODO use isActiveSupportOver and isEol etc
    now = dt.datetime.now(dt.timezone.utc)
    six_months_from_now = now + relativedelta(months=+6)

    for cycle in data:
        for property_ in ("activeSupportUntil", "eolFrom", "discontinuedFrom"):
            if property_ not in cycle:
                continue

            # Handle Boolean
            if isinstance(cycle[property_], bool):
                if property_ == "activeSupportUntil":
                    colour = "green" if cycle["activeSupportUntil"] else "red"
                else:  # "eolFrom" and "discontinuedFrom"
                    colour = "red" if cycle[property_] else "green"
                cycle[property_] = colored(cycle[property_], colour)
                continue

            # Handle date
            date_str = cycle[property_]
            if not date_str:
                cycle[property_] = colored(date_str, "green")
                continue

            # Convert "2020-01-01" string to datetime
            date_datetime = dt.datetime.strptime(date_str, "%Y-%m-%d").replace(
                tzinfo=dt.timezone.utc
            )
            if date_datetime < now:
                cycle[property_] = colored(date_str, "red")
            elif date_datetime < six_months_from_now:
                cycle[property_] = colored(date_str, "yellow")
            else:
                cycle[property_] = colored(date_str, "green")
    return data


def _tabulate(
    data: list[dict], format_: str = "markdown", color: str = "yes", title: str = None
) -> str:
    """Return data in specified format"""

    # Flatten: "latest": {"name": "x", "date": "y", "link": "z"}
    for row in data:
        if "latest" in row:
            if "name" in row["latest"]:
                row["latest.name"] = row["latest"]["name"]
            if "date" in row["latest"]:
                row["latest.date"] = row["latest"]["date"]
            if "link" in row["latest"]:
                row["latest.link"] = row["latest"]["link"]
        row.pop("latest")

    # Rename some headers
    for row in data:
        if "latest.date" in row:
            row["latest release"] = row.pop("latest.date")
        if "latest.name" in row:
            row["latest"] = row.pop("latest.name")
        if "latest.link" in row:
            row["link"] = row.pop("latest.link")
        if "date" in row:
            row["release"] = row.pop("date")
        if "eolFrom" in row:
            row["eol"] = row.pop("eolFrom")
        if "activeSupportUntil" in row:
            row["support"] = row.pop("activeSupportUntil")
        if "discontinuedFrom" in row:
            row["discontinued"] = row.pop("discontinuedFrom")

    print(data)
    headers = sorted(set().union(*(d.keys() for d in data)))

    # Skip some headers (TODO some temporarily)
    for header in (
        "name",
        "codename",
        "isEol",
        "isExtendedSupportOver",
        "isLts",
        "isMaintained",
        "activeSupportUntil",
        "discontinued",  # TODO?
        "extendedSupportUntil",
        "isActiveSupportOver",
        "isDiscontinued",
        "ltsFrom",
    ):
        if header in headers:
            headers.remove(header)

    # Put headers in preferred order, with the rest at the end
    new_headers = []
    for preferred in (
        "label",
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

    if format_ in ("markdown", "pretty"):
        return _prettytable(headers, data, format_, color, title)
    else:
        return _pytablewriter(headers, data, format_, title)


def _prettytable(
    headers: list[str],
    data: list[dict],
    format_: str,
    color: str = "yes",
    title: str = None,
) -> str:
    from prettytable import MARKDOWN, SINGLE_BORDER, PrettyTable

    x = PrettyTable()
    x.set_style(MARKDOWN if format_ == "markdown" else SINGLE_BORDER)
    do_color = color != "no" and format_ == "pretty"

    for header in headers:
        left_align = header in ("label", "latest", "link")
        display_header = colored(header, attrs=["bold"]) if do_color else header
        col_data = [row[header] if header in row else "" for row in data]
        x.add_column(display_header, col_data)

        if left_align:
            x.align[display_header] = "l"

    title_prefix = ""
    if title:
        if format_ == "pretty":
            x.title = colored(title, attrs=["bold"]) if do_color else title
        else:
            title_prefix = f"## {title}\n\n"

    return title_prefix + x.get_string()


def _pytablewriter(
    headers: list[str], data: list[dict], format_: str, title: str = None
) -> str:
    from pytablewriter import (
        CsvTableWriter,
        HtmlTableWriter,
        RstSimpleTableWriter,
        String,
        TsvTableWriter,
        YamlTableWriter,
    )
    from pytablewriter.style import Align, Style

    format_writers = {
        "csv": CsvTableWriter,
        "html": HtmlTableWriter,
        "rst": RstSimpleTableWriter,
        "tsv": TsvTableWriter,
        "yaml": YamlTableWriter,
    }

    writer = format_writers[format_]()
    if format_ != "html":
        writer.margin = 1

    writer.table_name = title
    writer.headers = headers
    writer.value_matrix = data

    # Custom alignment and format
    column_styles = []
    type_hints = []

    for header in headers:
        align = Align.AUTO
        type_hint = None
        if header in ("name", "latest"):
            type_hint = String
        style = Style(align=align)
        column_styles.append(style)
        type_hints.append(type_hint)

        writer.column_styles = column_styles
        writer.type_hints = type_hints

    return writer.dumps()
