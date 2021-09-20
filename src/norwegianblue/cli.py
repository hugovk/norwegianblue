#!/usr/bin/env python3
"""
CLI to show end-of-life dates for a number of products, from https://endoflife.date
"""
import argparse
import sys

import norwegianblue


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
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
    )
    if output == norwegianblue.ERROR_404_TEXT:
        sys.exit(output)
    print(output)


if __name__ == "__main__":
    main()
