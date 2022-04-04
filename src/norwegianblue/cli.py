#!/usr/bin/env python3
"""
CLI to show end-of-life dates for a number of products, from https://endoflife.date

For example:

* `eol python` to see Python EOLs
* `eol ubuntu` to see Ubuntu EOLs
* `eol centos fedora` to see CentOS and Fedora EOLs
* `eol all` to list all available products

Something missing? Please contribute! https://endoflife.date/contribute
"""
import argparse
import atexit
import sys

import norwegianblue
from norwegianblue import _cache


class Formatter(
    argparse.ArgumentDefaultsHelpFormatter,
    argparse.RawDescriptionHelpFormatter,
):
    pass


atexit.register(_cache.clear)


def main():
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
        default="markdown",
        choices=("html", "json", "markdown", "rst", "tsv"),
        help="The format of output",
    )
    parser.add_argument(
        "-c",
        "--color",
        default="auto",
        choices=("yes", "no", "auto"),
        help="color terminal output",
    )
    parser.add_argument(
        "--clear-cache", action="store_true", help="Clear cache before running"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Print debug messages to stderr"
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"%(prog)s {norwegianblue.__version__}",
    )
    args = parser.parse_args()
    if args.clear_cache:
        _cache.clear(clear_all=True)

    for product in args.product:
        output = norwegianblue.norwegianblue(
            product=product, format=args.format, color=args.color, verbose=args.verbose
        )
        if output == norwegianblue.ERROR_404_TEXT:
            sys.exit(output)
        print(output)
        print()


if __name__ == "__main__":
    main()
