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
from termcolor import colored

from norwegianblue import _cache

__version__ = importlib.metadata.version(__name__)


__all__ = ["__version__"]

BASE_URL = "https://endoflife.date/api/"
USER_AGENT = f"norwegianblue/{__version__}"


def error_404_text(product: str, suggestion: str) -> str:
    return f"Product '{product}' not found, run 'eol all' for list." + (
        f" Did you mean: '{suggestion}'?" if suggestion else ""
    )


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
            suggestion = suggest_product(product)
            msg = error_404_text(product, suggestion)
            raise ValueError(msg)

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
    if color != "no" and format != "yaml":
        data = _colourify(data, is_html=format == "html")

    output = _tabulate(data, format, color, product if show_title else None)
    logging.info("")

    if product == "norwegianblue":
        return prefix + output

    return output


@lru_cache(maxsize=None)
def suggest_product(product: str) -> str:
    import difflib

    # Get all known products from the API or cache
    all_products = norwegianblue("all").splitlines()

    # Find the closest match
    result = difflib.get_close_matches(product, all_products, n=1)
    logging.info("Suggestion:\t%s (score: %d)", *result)
    return result[0] if result else ""


def _ltsify(data: list[dict]) -> list[dict]:
    """If a cycle is LTS, append LTS to the cycle version and remove the LTS column"""
    for cycle in data:
        if "lts" in cycle:
            if cycle["lts"]:
                cycle["cycle"] = f"{cycle['cycle']} LTS"
            cycle.pop("lts")
    return data


def _colourify(data: list[dict], *, is_html: bool = False) -> list[dict]:
    """Add colour to dates:
    red: in the past
    yellow: will pass in six months
    green: will pass after six months
    """
    now = dt.datetime.now(dt.timezone.utc)
    six_months_from_now = now + relativedelta(months=+6)

    for cycle in data:
        for property_ in ("discontinued", "support", "eol", "extendedSupport"):
            if property_ not in cycle:
                continue

            # Handle Boolean
            if isinstance(cycle[property_], bool):
                if property_ in ("support", "extendedSupport"):
                    colour = "green" if cycle[property_] else "red"
                else:  # "discontinued" or "eol"
                    colour = "red" if cycle[property_] else "green"

                cycle[property_] = _apply_colour(
                    cycle[property_], colour, is_html=is_html
                )
                continue

            # Handle date
            date_str = cycle[property_]
            # Convert "2020-01-01" string to datetime
            date_datetime = dt.datetime.strptime(date_str, "%Y-%m-%d").replace(
                tzinfo=dt.timezone.utc
            )
            if date_datetime < now:
                cycle[property_] = _apply_colour(date_str, "red", is_html=is_html)
            elif date_datetime < six_months_from_now:
                cycle[property_] = _apply_colour(date_str, "yellow", is_html=is_html)
            else:
                cycle[property_] = _apply_colour(date_str, "green", is_html=is_html)
    return data


def _apply_colour(text: str, colour: str, *, is_html: bool = False) -> str:
    if is_html:
        return f'<font color="{colour}">{text}</font>'

    return colored(text, colour)


def _tabulate(
    data: list[dict],
    format_: str = "markdown",
    color: str = "yes",
    title: str | None = None,
) -> str:
    """Return data in specified format"""

    # Rename some headers
    for row in data:
        if "releaseDate" in row:
            row["release"] = row.pop("releaseDate")
        if "latestReleaseDate" in row:
            row["latest release"] = row.pop("latestReleaseDate")
        if "extendedSupport" in row:
            row["extended support"] = row.pop("extendedSupport")

    headers = sorted(set().union(*(d.keys() for d in data)))

    # Skip some headers, only used internally at https://endoflife.date
    for header in ("cycleShortHand", "latestShortHand", "releaseLabel"):
        if header in headers:
            headers.remove(header)

    # Put headers in preferred order, with the rest at the end
    new_headers = []
    for preferred in (
        "cycle",
        "codename",
        "release",
        "latest",
        "latest release",
        "discontinued",
        "support",
        "eol",
        "extended support",
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
    title: str | None = None,
) -> str:
    from prettytable import MARKDOWN, SINGLE_BORDER, PrettyTable

    x = PrettyTable()
    x.set_style(MARKDOWN if format_ == "markdown" else SINGLE_BORDER)
    do_color = color != "no" and format_ == "pretty"

    for header in headers:
        left_align = header in ("cycle", "latest", "link")
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
    headers: list[str], data: list[dict], format_: str, title: str | None = None
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
        if header in ("cycle", "latest"):
            type_hint = String
        style = Style(align=align)
        column_styles.append(style)
        type_hints.append(type_hint)

        writer.column_styles = column_styles
        writer.type_hints = type_hints

    return writer.dumps()
