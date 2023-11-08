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

from termcolor import colored

import norwegianblue
from norwegianblue import _cache

atexit.register(_cache.clear)


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "product",
        nargs="*",
        default=["all"],
        help="product to check, or 'all' to list all available (default: 'all')",
    )
    parser.add_argument(
        "-f",
        "--format",
        choices=(
            "html",
            "json",
            "md",
            "markdown",
            "pretty",
            "rst",
            "csv",
            "tsv",
            "yaml",
        ),
        help="deprecated: use direct options instead: "
        "--html, --json, --md, --pretty, --rst, --csv, --tsv or --yaml.",
    )
    parser.add_argument(
        "-c",
        "--color",
        default="auto",
        choices=("yes", "no", "auto"),
        help="colour the output (default: auto)",
    )
    parser.add_argument(
        "--clear-cache", action="store_true", help="clear cache before running"
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_const",
        dest="loglevel",
        const=logging.INFO,
        default=logging.WARNING,
        help="print extra messages to stderr",
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"%(prog)s {norwegianblue.__version__} "
        f"(Python {platform.python_version()})",
    )
    parser.add_argument(
        "-w", "--web", action="store_true", help="open product page in web browser"
    )

    format_group = parser.add_argument_group("formatters")
    format_group = format_group.add_mutually_exclusive_group()

    for name, help_text in (
        ("pretty", "pretty (default)"),
        ("md", "Markdown"),
        ("rst", "reStructuredText"),
        ("json", "JSON"),
        ("csv", "CSV"),
        ("tsv", "TSV"),
        ("html", "HTML"),
        ("yaml", "YAML"),
    ):
        format_group.add_argument(
            f"--{name}",
            action="store_const",
            const=name,
            dest="formatter",
            help=f"output in {help_text}",
        )
    parser.set_defaults(formatter="pretty")

    args = parser.parse_args()

    if args.format:
        from termcolor import cprint

        cprint(
            "The -f/--format option is deprecated, use direct options instead: "
            "--html, --json, --md, --pretty, --rst, --csv, --tsv or --yaml.",
            "yellow",
            file=sys.stderr,
        )
        args.formatter = args.format

    logging.basicConfig(level=args.loglevel, format="%(message)s")
    if args.clear_cache:
        _cache.clear(clear_all=True)

    multiple_products = len(args.product) >= 2
    for product in args.product:
        try:
            output = norwegianblue.norwegianblue(
                product=product,
                format=args.formatter,
                color=args.color,
                show_title=multiple_products,
            )
        except ValueError as e:
            prompt = f"{e} [Y/n] "
            if args.color != "no":
                prompt = colored(prompt, "yellow")
            answer = input(prompt)
            if answer not in ("", "y", "Y"):
                sys.exit()
            suggestion = norwegianblue.suggest_product(product)
            output = norwegianblue.norwegianblue(
                product=suggestion,
                format=args.format,
                color=args.color,
                show_title=multiple_products,
            )
        print(output)
        print()
        if args.web:
            import webbrowser

            webbrowser.open_new_tab(f"https://endoflife.date/{product.lower()}")


if __name__ == "__main__":
    main()
