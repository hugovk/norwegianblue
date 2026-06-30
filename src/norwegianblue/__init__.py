"""
Python interface to endoflife.date API
https://endoflife.date/docs/api/
"""

from __future__ import annotations

import datetime as dt
import sys
from functools import cache

from termcolor import colored

from . import _version

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

__version__ = _version.__version__

__all__ = ["__version__"]

BASE_URL = "https://endoflife.date/api/"

_verbose = False


def _print_verbose(*args: Any, **kwargs: Any) -> None:
    """Print to stderr if verbose"""
    if _verbose:
        print(*args, file=sys.stderr, **kwargs)


def error_404_text(product: str, suggestion: str) -> str:
    return f"Product '{product}' not found, run 'eol all' for list." + (
        f" Did you mean: '{suggestion}'?" if suggestion else ""
    )


def norwegianblue(
    product: str = "all",
    format: str | None = "pretty",
    color: str = "yes",
    show_title: bool = False,
) -> str | list[dict]:
    """Call the API and return result"""
    if format == "md":
        format = "markdown"
    if product == "norwegianblue":
        from ._data import prefix, res
    else:
        from . import _cache

        url = BASE_URL + product.lower() + ".json"
        cache_file = _cache.filename(url)
        _print_verbose(f"Human URL:\thttps://endoflife.date/{product.lower()}")
        _print_verbose(f"API URL:\t{url}")
        _print_verbose(
            "Source URL:\thttps://github.com/endoflife-date/endoflife.date/"
            f"blob/master/products/{product.lower()}.md",
        )
        _print_verbose(f"Cache file:\t{cache_file}")

        res = []
        if cache_file.is_file():
            _print_verbose("Cache file exists")
            res = _cache.load(cache_file)

    if not res:
        # No cache, or couldn't load cache
        import json

        import urllib3

        r = urllib3.request(
            "GET",
            url,
            headers={"User-Agent": f"norwegianblue/{__version__}"},
            redirect=True,
        )

        _print_verbose("HTTP status code:", r.status)
        if r.status == 404:
            suggestion = suggest_product(product)
            msg = error_404_text(product, suggestion)
            raise ValueError(msg)

        # Raise if we made a bad request
        # (4XX client error or 5XX server error response)
        if r.status >= 400:
            msg = f"HTTP {r.status} error for url: {url}"
            raise urllib3.exceptions.HTTPError(msg)

        res = json.loads(r.data.decode("utf-8"))

        _cache.save(cache_file, res)

    if format == "json":
        import json

        return json.dumps(res)

    data: list[dict] = list(res)

    if format is None:
        return data

    if product == "all":
        return "\n".join(data)  # type: ignore[arg-type]

    data = _ltsify(data)
    if color != "no" and format != "yaml":
        data = _colourify(data, is_html=format == "html")

    if format in ("pretty", "markdown", "rst", "html"):
        data = linkify(data, format)

    output = _tabulate(data, format, color, product if show_title else None)
    _print_verbose("")

    if product == "norwegianblue":
        return prefix + output

    return output


def linkify(data: list[dict], format_: str) -> list[dict]:
    """If a cycle has a link, add a hyperlink and remove the link column"""
    for cycle in data:
        if "link" in cycle:
            if cycle["link"]:
                if format_ == "pretty":
                    cycle["cycle"] = (
                        f"\033]8;;{cycle['link']}\033\\{cycle['cycle']}\033]8;;\033\\"
                    )
                elif format_ == "markdown":
                    cycle["cycle"] = f"[{cycle['cycle']}]({cycle['link']})"
                elif format_ == "rst":
                    cycle["cycle"] = f"`{cycle['cycle']} <{cycle['link']}>`__"
                elif format_ == "html":
                    cycle["cycle"] = f'<a href="{cycle["link"]}">{cycle["cycle"]}</a>'

            cycle.pop("link")

    return data


def all_products() -> list[str]:
    """Get all known products from the API or cache"""
    result = norwegianblue("all")
    assert isinstance(result, str)
    return result.splitlines()


@cache
def suggest_product(product: str) -> str:
    """Provide the best suggestion based on a typed product"""
    import difflib

    # Find the closest match
    result = difflib.get_close_matches(product, all_products(), n=1)
    _print_verbose("Suggestion:", result[0] if result else "")
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
    six_months_from_now = now + dt.timedelta(days=180)

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

    if format_ == "yaml":
        return _yaml(headers, data, title)
    else:
        return _prettytable(headers, data, format_, color, title)


def _prettytable(
    headers: list[str],
    data: list[dict],
    format_: str,
    color: str = "yes",
    title: str | None = None,
) -> str:
    import csv

    from prettytable import PrettyTable, TableStyle

    table = PrettyTable()
    if format_ == "html":
        table.border = False
    elif format_ == "markdown":
        table.set_style(TableStyle.MARKDOWN)
    elif format_ == "pretty":
        table.set_style(TableStyle.SINGLE_BORDER)
    elif format_ == "rst":
        table.set_style(TableStyle.RST)
    do_color = color != "no" and format_ == "pretty"

    for header in headers:
        left_align = header in ("cycle", "latest", "link")
        display_header = colored(header, attrs=["bold"]) if do_color else header
        col_data = [row[header] if header in row else "" for row in data]
        table.add_column(display_header, col_data)

        if left_align:
            table.align[display_header] = "l"

    if format_ == "html":
        return table.get_html_string(title=title, format=True, escape_data=False)
    if format_ == "csv":
        return table.get_csv_string(quoting=csv.QUOTE_ALL)
    if format_ == "tsv":
        return table.get_csv_string(quoting=csv.QUOTE_ALL, delimiter="\t")

    title_prefix = ""
    if title:
        if format_ == "markdown":
            title_prefix = f"## {title}\n\n"
        else:
            table.title = colored(title, attrs=["bold"]) if do_color else title

    return title_prefix + table.get_string()


def _yaml(headers: list[str], data: list[dict], title: str | None = None) -> str:
    import yaml

    rows = [{header: row.get(header, "") for header in headers} for row in data]
    obj = {title: rows} if title else rows
    return yaml.dump(obj, allow_unicode=True, default_flow_style=False)
