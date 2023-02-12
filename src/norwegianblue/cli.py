#!/usr/bin/env python3
"""
CLI to show end-of-life dates for a number of products, from https://endoflife.date

For example:

* `eol python` to see Python EOLs
* `eol ubuntu` to see Ubuntu EOLs
* `eol centos fedora` to see CentOS and Fedora EOLs
* `eol all` or `eol` to list all available products

Something missing? Please contribute! https://endoflife.date/contribute
"""
from __future__ import annotations

import argparse
import atexit
import logging
import platform
import sys

import norwegianblue
from norwegianblue import _cache


class Formatter(
    argparse.ArgumentDefaultsHelpFormatter,
    argparse.RawDescriptionHelpFormatter,
):
    pass


atexit.register(_cache.clear)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=Formatter)
    parser.add_argument(
        "product",
        nargs="*",
        default=["all"],
        help="Product to check, or 'all' to list all available",
    )
    parser.add_argument(
        "-f",
        "--format",
        default="pretty",
        choices=("html", "json", "md", "markdown", "pretty", "rst", "csv", "tsv"),
        help="The format of output",
    )
    parser.add_argument(
        "-c",
        "--color",
        default="auto",
        choices=("yes", "no", "auto"),
        help="Color the terminal output",
    )
    parser.add_argument(
        "--clear-cache", action="store_true", help="Clear cache before running"
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_const",
        dest="loglevel",
        const=logging.INFO,
        default=logging.WARNING,
        help="Print extra messages to stderr",
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"%(prog)s {norwegianblue.__version__} "
        f"(Python {platform.python_version()})",
    )
    args = parser.parse_args()

    logging.basicConfig(level=args.loglevel, format="%(message)s")
    if args.clear_cache:
        _cache.clear(clear_all=True)

    multiple_products = len(args.product) >= 2
    for product in args.product:
        try:
            output = norwegianblue.norwegianblue(
                product=product,
                format=args.format,
                color=args.color,
                show_title=multiple_products,
            )
        except ValueError as e:
            sys.exit(e)
        print(output)
        print()


if __name__ == "__main__":
    main()
