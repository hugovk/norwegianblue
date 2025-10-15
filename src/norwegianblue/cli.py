# PYTHON_ARGCOMPLETE_OK
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

from termcolor import colored

try:
    import argcomplete
except ImportError:
    argcomplete = None

import norwegianblue
from norwegianblue import _cache

atexit.register(_cache.clear)


def product_completer(**kwargs):
    """The list of all products to feed autocompletion"""
    return norwegianblue.all_products()


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    # Added in Python 3.14
    parser.suggest_on_error = True
    parser.add_argument(
        "product",
        nargs="*",
        default=["all"],
        help="product to check, or 'all' to list all available (default: 'all')",
    ).completer = product_completer
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
        "--show-title",
        default="auto",
        choices=("yes", "no", "auto"),
        help="show or hide product title, 'auto' to show title "
        "only for multiple products (default: auto)",
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
    if argcomplete:
        argcomplete.autocomplete(parser)
    args = parser.parse_args()

    logging.basicConfig(level=args.loglevel, format="%(message)s")
    if args.clear_cache:
        _cache.clear(clear_all=True)

    multiple_products = len(args.product) >= 2
    show_title = (args.show_title == "yes") or (
        multiple_products and args.show_title != "no"
    )
    for product in args.product:
        try:
            output = norwegianblue.norwegianblue(
                product=product,
                format=args.formatter,
                color=args.color,
                show_title=show_title,
            )
        except ValueError as e:
            suggestion = norwegianblue.suggest_product(product)

            prompt = f"{e}{' [Y/n] ' if suggestion else ''}"
            if args.color != "no":
                prompt = colored(prompt, "yellow")
            if not suggestion:
                print(prompt)
                print()
                continue
            answer = input(prompt)
            if answer not in ("", "y", "Y"):
                print()
                continue
            output = norwegianblue.norwegianblue(
                product=suggestion,
                format=args.formatter,
                color=args.color,
                show_title=show_title,
            )
        print(output)
        print()
        if args.web:
            import webbrowser

            webbrowser.open_new_tab(f"https://endoflife.date/{product.lower()}")


if __name__ == "__main__":
    main()
