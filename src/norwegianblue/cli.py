#!/usr/bin/env python3
"""
CLI to show end-of-life dates for tools and technologies.
"""
import argparse

import norwegianblue


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("tool", nargs="?", default="python", help="Tool to check")
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
    print(
        norwegianblue.norwegianblue(
            tool=args.tool, format=args.format, color=args.color, verbose=args.verbose
        )
    )


if __name__ == "__main__":
    main()
