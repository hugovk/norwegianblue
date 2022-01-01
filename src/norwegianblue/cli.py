#!/usr/bin/env python3
"""
CLI to show end-of-life dates for a number of products, from https://endoflife.date

For example:

* `eol python` to see Python EOLs
* `eol ubuntu` to see Ubuntu EOLs
* `eol all` to list all available products

Something missing? Please contribute! https://endoflife.date/contribute
"""
import argparse
import sys

import norwegianblue


class Formatter(
    argparse.ArgumentDefaultsHelpFormatter,
    argparse.RawDescriptionHelpFormatter,
):
    pass


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=Formatter)
    parser.add_argument(
        "product",
        nargs="?",
        default="all",
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
    parser.add_argument("--chart", action="store_true", help="Chart the EOLs")
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
    output = norwegianblue.norwegianblue(
        product=args.product,
        format=args.format,
        color=args.color,
        verbose=args.verbose,
        clear_cache=args.clear_cache,
        chart=args.chart,
    )
    if output == norwegianblue.ERROR_404_TEXT:
        sys.exit(output)
    print(output)


if __name__ == "__main__":
    main()
