# norwegianblue

[![PyPI version](https://img.shields.io/pypi/v/norwegianblue.svg?logo=pypi&logoColor=FFE873)](https://pypi.org/project/norwegianblue/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/norwegianblue.svg?logo=python&logoColor=FFE873)](https://pypi.org/project/norwegianblue/)
[![PyPI downloads](https://img.shields.io/pypi/dm/norwegianblue.svg)](https://pypistats.org/packages/norwegianblue)
[![GitHub Actions status](https://github.com/hugovk/norwegianblue/actions/workflows/test.yml/badge.svg)](https://github.com/hugovk/norwegianblue/actions)
[![Codecov](https://codecov.io/gh/hugovk/norwegianblue/branch/main/graph/badge.svg)](https://codecov.io/gh/hugovk/norwegianblue)
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

### With [pipx][pipx]

```bash
pipx install norwegianblue
```

[pipx]: https://github.com/pypa/pipx

### From source

```bash
git clone https://github.com/hugovk/norwegianblue
cd norwegianblue
python3 -m pip install .
```

To install tab completion on supported Linux and macOS shells, see
https://kislyuk.github.io/argcomplete/

## Example command-line use

Run `norwegianblue` or `eol`, they do the same thing.

Top-level help:

<!-- [[[cog
from scripts.run_command import run
run("eol --help")
]]] -->

```console
$ eol --help
usage: eol [-h] [-c {yes,no,auto}] [--clear-cache] [--show-title {yes,no,auto}] [-v] [-V] [-w]
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
  -c, --color {yes,no,auto}
                        colour the output (default: auto)
  --clear-cache         clear cache before running
  --show-title {yes,no,auto}
                        show or hide product title, 'auto' to show title only for multiple products (default: auto)
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
adonisjs
akeneo-pim
alibaba-ack
alibaba-dragonwell
almalinux
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
│ 3.14  │ 2025-10-07 │ 3.14.0  │   2025-10-07   │ 2027-10-01 │ 2030-10-31 │
│ 3.13  │ 2024-10-07 │ 3.13.9  │   2025-10-14   │ 2026-10-01 │ 2029-10-31 │
│ 3.12  │ 2023-10-02 │ 3.12.12 │   2025-10-09   │ 2025-04-02 │ 2028-10-31 │
│ 3.11  │ 2022-10-24 │ 3.11.14 │   2025-10-09   │ 2024-04-01 │ 2027-10-31 │
│ 3.10  │ 2021-10-04 │ 3.10.19 │   2025-10-09   │ 2023-04-05 │ 2026-10-31 │
│ 3.9   │ 2020-10-05 │ 3.9.24  │   2025-10-09   │ 2022-05-17 │ 2025-10-31 │
│ 3.8   │ 2019-10-14 │ 3.8.20  │   2024-09-06   │ 2021-05-03 │ 2024-10-07 │
│ 3.7   │ 2018-06-27 │ 3.7.17  │   2023-06-05   │ 2020-06-27 │ 2023-06-27 │
│ 3.6   │ 2016-12-23 │ 3.6.15  │   2021-09-03   │ 2018-12-24 │ 2021-12-23 │
│ 3.5   │ 2015-09-13 │ 3.5.10  │   2020-09-05   │   False    │ 2020-09-30 │
│ 3.4   │ 2014-03-16 │ 3.4.10  │   2019-03-18   │   False    │ 2019-03-18 │
│ 3.3   │ 2012-09-29 │ 3.3.7   │   2017-09-19   │   False    │ 2017-09-29 │
│ 3.2   │ 2011-02-20 │ 3.2.6   │   2014-10-12   │   False    │ 2016-02-20 │
│ 2.7   │ 2010-07-03 │ 2.7.18  │   2020-04-19   │   False    │ 2020-01-01 │
│ 3.1   │ 2009-06-27 │ 3.1.5   │   2012-04-06   │   False    │ 2012-04-09 │
│ 3.0   │ 2008-12-03 │ 3.0.1   │   2009-02-12   │   False    │ 2009-06-27 │
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
| 3.14  | 2025-10-07 | 3.14.0  |   2025-10-07   | 2027-10-01 | 2030-10-31 |
| 3.13  | 2024-10-07 | 3.13.9  |   2025-10-14   | 2026-10-01 | 2029-10-31 |
| 3.12  | 2023-10-02 | 3.12.12 |   2025-10-09   | 2025-04-02 | 2028-10-31 |
| 3.11  | 2022-10-24 | 3.11.14 |   2025-10-09   | 2024-04-01 | 2027-10-31 |
| 3.10  | 2021-10-04 | 3.10.19 |   2025-10-09   | 2023-04-05 | 2026-10-31 |
| 3.9   | 2020-10-05 | 3.9.24  |   2025-10-09   | 2022-05-17 | 2025-10-31 |
| 3.8   | 2019-10-14 | 3.8.20  |   2024-09-06   | 2021-05-03 | 2024-10-07 |
| 3.7   | 2018-06-27 | 3.7.17  |   2023-06-05   | 2020-06-27 | 2023-06-27 |
| 3.6   | 2016-12-23 | 3.6.15  |   2021-09-03   | 2018-12-24 | 2021-12-23 |
| 3.5   | 2015-09-13 | 3.5.10  |   2020-09-05   |   False    | 2020-09-30 |
| 3.4   | 2014-03-16 | 3.4.10  |   2019-03-18   |   False    | 2019-03-18 |
| 3.3   | 2012-09-29 | 3.3.7   |   2017-09-19   |   False    | 2017-09-29 |
| 3.2   | 2011-02-20 | 3.2.6   |   2014-10-12   |   False    | 2016-02-20 |
| 2.7   | 2010-07-03 | 2.7.18  |   2020-04-19   |   False    | 2020-01-01 |
| 3.1   | 2009-06-27 | 3.1.5   |   2012-04-06   |   False    | 2012-04-09 |
| 3.0   | 2008-12-03 | 3.0.1   |   2009-02-12   |   False    | 2009-06-27 |
| 2.6   | 2008-10-01 | 2.6.9   |   2013-10-29   |   False    | 2013-10-29 |

<!-- [[[end]]] -->

With options:

<!-- [[[cog
run("eol nodejs --rst")
]]] -->

```console
$ eol nodejs --rst
.. table::

    ==============================================================================================  ============  ==========  ================  ============  ============  ==================
                                                cycle                                                 release       latest     latest release     support         eol        extended support
    ==============================================================================================  ============  ==========  ================  ============  ============  ==================
     24 LTS                                                                                          2025-05-06    24.10.0     2025-10-08        2026-10-20    2028-04-30    False
     23                                                                                              2024-10-16    23.11.1     2025-05-14        2025-04-01    2025-06-01    False
     22 LTS                                                                                          2024-04-24    22.20.0     2025-09-24        2025-10-21    2027-04-30    False
     21                                                                                              2023-10-17    21.7.3      2024-04-10        2024-04-01    2024-06-01    False
     20 LTS                                                                                          2023-04-18    20.19.5     2025-09-03        2024-10-22    2026-04-30    False
     19                                                                                              2022-10-18    19.9.0      2023-04-10        2023-04-01    2023-06-01    False
     18 LTS                                                                                          2022-04-19    18.20.8     2025-03-27        2023-10-18    2025-04-30    True
     17                                                                                              2021-10-19    17.9.1      2022-06-01        2022-04-01    2022-06-01    False
     16 LTS                                                                                          2021-04-20    16.20.2     2023-08-09        2022-10-18    2023-09-11    True
     15                                                                                              2020-10-20    15.14.0     2021-04-06        2021-04-01    2021-06-01    False
     14 LTS                                                                                          2020-04-21    14.21.3     2023-02-16        2021-10-19    2023-04-30    True
     13                                                                                              2019-10-22    13.14.0     2020-04-29        2020-04-01    2020-06-01    False
     12 LTS                                                                                          2019-04-23    12.22.12    2022-04-05        2020-10-20    2022-04-30    True
     11                                                                                              2018-10-23    11.15.0     2019-04-30        2019-04-01    2019-06-30    False
     10 LTS                                                                                          2018-04-24    10.24.1     2021-04-06        2020-05-19    2021-04-30    False
     9                                                                                               2017-10-31    9.11.2      2018-06-12        2018-06-30    2018-06-30    False
     8 LTS                                                                                           2017-05-30    8.17.0      2019-12-17        2019-01-01    2019-12-31    False
     7                                                                                               2016-10-25    7.10.1      2017-07-11        2017-06-30    2017-06-30    False
     6 LTS                                                                                           2016-04-26    6.17.1      2019-04-03        2018-04-30    2019-04-30    False
     5                                                                                               2015-10-30    5.12.0      2016-06-23        2016-06-30    2016-06-30    False
     4 LTS                                                                                           2015-09-09    4.9.1       2018-03-29        2017-04-01    2018-04-30    False
     `3 <https://github.com/nodejs/node/blob/main/doc/changelogs/CHANGELOG_IOJS.md#__LATEST__>`__    2015-08-04    3.3.1       2015-09-15        False         True          False
     `2 <https://github.com/nodejs/node/blob/main/doc/changelogs/CHANGELOG_IOJS.md#__LATEST__>`__    2015-05-04    2.5.0       2015-07-28        False         True          False
     `1 <https://github.com/nodejs/node/blob/main/doc/changelogs/CHANGELOG_IOJS.md#__LATEST__>`__    2015-01-20    1.8.4       2015-07-09        False         True          False
    ==============================================================================================  ============  ==========  ================  ============  ============  ==================
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
