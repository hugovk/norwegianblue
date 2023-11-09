# norwegianblue

[![PyPI version](https://img.shields.io/pypi/v/norwegianblue.svg?logo=pypi&logoColor=FFE873)](https://pypi.org/project/norwegianblue/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/norwegianblue.svg?logo=python&logoColor=FFE873)](https://pypi.org/project/norwegianblue/)
[![PyPI downloads](https://img.shields.io/pypi/dm/norwegianblue.svg)](https://pypistats.org/packages/norwegianblue)
[![Test](https://github.com/hugovk/norwegianblue/actions/workflows/test.yml/badge.svg)](https://github.com/hugovk/norwegianblue/actions)
[![codecov](https://codecov.io/gh/hugovk/norwegianblue/branch/main/graph/badge.svg)](https://codecov.io/gh/hugovk/norwegianblue)
[![Licence](https://img.shields.io/github/license/hugovk/norwegianblue.svg)](LICENSE.txt)
[![Code style: Black](https://img.shields.io/badge/code%20style-Black-000000.svg)](https://github.com/psf/black)

<p align="center"><img src="https://raw.githubusercontent.com/hugovk/norwegianblue/main/img/eol-python.png" width="370" height="225"></p>

Python interface to [endoflife.date](https://endoflife.date/docs/api/) to show
end-of-life dates for a number of products.

## Installation

### From PyPI

```bash
python3 -m pip install --upgrade norwegianblue
```

#### Using [`pipx`](https://pypa.github.io/pipx/)

```bash
pipx install norwegianblue
```

### From source

```bash
git clone https://github.com/hugovk/norwegianblue
cd norwegianblue
python3 -m pip install .
```

## Example command-line use

Run `norwegianblue` or `eol`, they do the same thing.

Top-level help:

<!-- [[[cog
from scripts.run_command import run
run("eol --help")
]]] -->

```console
$ eol --help
usage: eol [-h] [-f {html,json,md,markdown,pretty,rst,csv,tsv,yaml}] [-c {yes,no,auto}] [--clear-cache] [-v] [-V] [-w]
           [--pretty | --md | --rst | --json | --csv | --tsv | --html | --yaml]
           [product ...]

CLI to show end-of-life dates for a number of products, from https://endoflife.date

For example:

* `eol python` to see Python EOLs
* `eol ubuntu` to see Ubuntu EOLs
* `eol centos fedora` to see CentOS and Fedora EOLs
* `eol all` or `eol` to list all available products

Something missing? Please contribute! https://endoflife.date/contribute

positional arguments:
  product               product to check, or 'all' to list all available (default: 'all')

options:
  -h, --help            show this help message and exit
  -f {html,json,md,markdown,pretty,rst,csv,tsv,yaml}, --format {html,json,md,markdown,pretty,rst,csv,tsv,yaml}
                        deprecated: use direct options instead: --html, --json, --md, --pretty, --rst, --csv, --tsv or
                        --yaml
  -c {yes,no,auto}, --color {yes,no,auto}
                        colour the output (default: auto)
  --clear-cache         clear cache before running
  -v, --verbose         print extra messages to stderr
  -V, --version         show program's version number and exit
  -w, --web             open product page in web browser

formatters:
  --pretty              output in pretty (default)
  --md                  output in Markdown
  --rst                 output in reStructuredText
  --json                output in JSON
  --csv                 output in CSV
  --tsv                 output in TSV
  --html                output in HTML
  --yaml                output in YAML
```

<!-- [[[end]]] -->

List all available products with end-of-life dates:

```console
$ # eol all
$ # or:
```

<!-- [[[cog
run("eol", line_limit=5)
]]] -->

```console
$ eol
akeneo-pim
alibaba-dragonwell
almalinux
alpine
amazon-cdk
...
```

<!-- [[[end]]] -->

Show end-of-life dates:

<!-- [[[cog
run("norwegianblue python")
]]] -->

```console
$ norwegianblue python
┌───────┬────────────┬─────────┬────────────────┬────────────┬────────────┐
│ cycle │  release   │ latest  │ latest release │  support   │    eol     │
├───────┼────────────┼─────────┼────────────────┼────────────┼────────────┤
│ 3.12  │ 2023-10-02 │ 3.12.0  │   2023-10-02   │ 2025-04-02 │ 2028-10-02 │
│ 3.11  │ 2022-10-24 │ 3.11.6  │   2023-10-02   │ 2024-04-01 │ 2027-10-24 │
│ 3.10  │ 2021-10-04 │ 3.10.13 │   2023-08-24   │ 2023-04-05 │ 2026-10-04 │
│ 3.9   │ 2020-10-05 │ 3.9.18  │   2023-08-24   │ 2022-05-17 │ 2025-10-05 │
│ 3.8   │ 2019-10-14 │ 3.8.18  │   2023-08-24   │ 2021-05-03 │ 2024-10-14 │
│ 3.7   │ 2018-06-26 │ 3.7.17  │   2023-06-05   │ 2020-06-27 │ 2023-06-27 │
│ 3.6   │ 2016-12-22 │ 3.6.15  │   2021-09-03   │ 2018-12-24 │ 2021-12-23 │
│ 3.5   │ 2015-09-12 │ 3.5.10  │   2020-09-05   │   False    │ 2020-09-13 │
│ 3.4   │ 2014-03-15 │ 3.4.10  │   2019-03-18   │   False    │ 2019-03-18 │
│ 3.3   │ 2012-09-29 │ 3.3.7   │   2017-09-19   │   False    │ 2017-09-29 │
│ 2.7   │ 2010-07-03 │ 2.7.18  │   2020-04-19   │   False    │ 2020-01-01 │
│ 2.6   │ 2008-10-01 │ 2.6.9   │   2013-10-29   │   False    │ 2013-10-29 │
└───────┴────────────┴─────────┴────────────────┴────────────┴────────────┘
```

<!-- [[[end]]] -->

You can format in Markdown, ready for pasting in GitHub issues and PRs:

<!-- [[[cog
run("eol python --md", with_console=False)
]]] -->

| cycle |  release   | latest  | latest release |  support   |    eol     |
| :---- | :--------: | :------ | :------------: | :--------: | :--------: |
| 3.12  | 2023-10-02 | 3.12.0  |   2023-10-02   | 2025-04-02 | 2028-10-02 |
| 3.11  | 2022-10-24 | 3.11.6  |   2023-10-02   | 2024-04-01 | 2027-10-24 |
| 3.10  | 2021-10-04 | 3.10.13 |   2023-08-24   | 2023-04-05 | 2026-10-04 |
| 3.9   | 2020-10-05 | 3.9.18  |   2023-08-24   | 2022-05-17 | 2025-10-05 |
| 3.8   | 2019-10-14 | 3.8.18  |   2023-08-24   | 2021-05-03 | 2024-10-14 |
| 3.7   | 2018-06-26 | 3.7.17  |   2023-06-05   | 2020-06-27 | 2023-06-27 |
| 3.6   | 2016-12-22 | 3.6.15  |   2021-09-03   | 2018-12-24 | 2021-12-23 |
| 3.5   | 2015-09-12 | 3.5.10  |   2020-09-05   |   False    | 2020-09-13 |
| 3.4   | 2014-03-15 | 3.4.10  |   2019-03-18   |   False    | 2019-03-18 |
| 3.3   | 2012-09-29 | 3.3.7   |   2017-09-19   |   False    | 2017-09-29 |
| 2.7   | 2010-07-03 | 2.7.18  |   2020-04-19   |   False    | 2020-01-01 |
| 2.6   | 2008-10-01 | 2.6.9   |   2013-10-29   |   False    | 2013-10-29 |

<!-- [[[end]]] -->

With options:

<!-- [[[cog
run("eol nodejs --rst")
]]] -->

```console
$ eol nodejs --rst
.. table::

    ========  ============  ==========  ================  ============  ============  ======================================================================================
     cycle      release       latest     latest release     support         eol                                                link
    ========  ============  ==========  ================  ============  ============  ======================================================================================
     21        2023-10-17    21.1.0      2023-10-24        2024-04-01    2024-06-01
     20 LTS    2023-04-18    20.9.0      2023-10-24        2024-10-22    2026-04-30
     19        2022-10-18    19.9.0      2023-04-10        2023-04-01    2023-06-01
     18 LTS    2022-04-19    18.18.2     2023-10-13        2023-10-18    2025-04-30
     17        2021-10-19    17.9.1      2022-06-01        2022-04-01    2022-06-01
     16 LTS    2021-04-20    16.20.2     2023-08-09        2022-10-18    2023-09-11
     15        2020-10-20    15.14.0     2021-04-06        2021-04-01    2021-06-01
     14 LTS    2020-04-21    14.21.3     2023-02-16        2021-10-19    2023-04-30
     13        2019-10-22    13.14.0     2020-04-29        2020-04-01    2020-06-01
     12 LTS    2019-04-23    12.22.12    2022-04-05        2020-10-20    2022-04-30
     11        2018-10-23    11.15.0     2019-04-30        2019-04-01    2019-06-30
     10 LTS    2018-04-24    10.24.1     2021-04-06        2020-05-19    2021-04-30
     9         2017-10-31    9.11.2      2018-06-12        2018-06-30    2018-06-30
     8 LTS     2017-05-30    8.17.0      2019-12-17        2019-01-01    2019-12-31
     7         2016-10-25    7.10.1      2017-07-11        2017-06-30    2017-06-30
     6 LTS     2016-04-26    6.17.1      2019-04-03        2018-04-30    2019-04-30
     5         2015-10-30    5.12.0      2016-06-23        2016-06-30    2016-06-30
     4 LTS     2015-09-09    4.9.1       2018-03-29        2017-04-01    2018-04-30
     3         2015-08-04    3.3.1       2015-09-15        False         True          https://github.com/nodejs/node/blob/main/doc/changelogs/CHANGELOG_IOJS.md#__LATEST__
     2         2015-05-04    2.5.0       2015-07-28        False         True          https://github.com/nodejs/node/blob/main/doc/changelogs/CHANGELOG_IOJS.md#__LATEST__
     1         2015-01-20    1.8.4       2015-07-09        False         True          https://github.com/nodejs/node/blob/main/doc/changelogs/CHANGELOG_IOJS.md#__LATEST__
    ========  ============  ==========  ================  ============  ============  ======================================================================================
```

<!-- [[[end]]] -->

## Example programmatic use

Return values are from the JSON responses documented in the API:
https://endoflife.date/docs/api/

```python
import norwegianblue

# Call the API
print(norwegianblue.norwegianblue())
print(norwegianblue.norwegianblue(product="ubuntu"))
print(norwegianblue.norwegianblue(format="json"))
```

## Why "Norwegian Blue"?

[The Norwegian Blue has reached end-of-life.](https://youtu.be/vnciwwsvNcc)
