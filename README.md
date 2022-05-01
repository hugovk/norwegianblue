# norwegianblue

[![PyPI version](https://img.shields.io/pypi/v/norwegianblue.svg?logo=pypi&logoColor=FFE873)](https://pypi.org/project/norwegianblue/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/norwegianblue.svg?logo=python&logoColor=FFE873)](https://pypi.org/project/norwegianblue/)
[![PyPI downloads](https://img.shields.io/pypi/dm/norwegianblue.svg)](https://pypistats.org/packages/norwegianblue)
[![Test](https://github.com/hugovk/norwegianblue/actions/workflows/test.yml/badge.svg)](https://github.com/hugovk/norwegianblue/actions)
[![codecov](https://codecov.io/gh/hugovk/norwegianblue/branch/main/graph/badge.svg)](https://codecov.io/gh/hugovk/norwegianblue)
[![GitHub](https://img.shields.io/github/license/hugovk/norwegianblue.svg)](LICENSE.txt)
[![Code style: Black](https://img.shields.io/badge/code%20style-Black-000000.svg)](https://github.com/psf/black)

<p align="center"><img src="https://raw.githubusercontent.com/hugovk/norwegianblue/main/img/eol-python.png" width="319" height="197"></p>

Python interface to [endoflife.date](https://endoflife.date/docs/api/) to show
end-of-life dates for a number of products.

## Installation

### From PyPI

```bash
python3 -m pip install --upgrade norwegianblue
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
usage: eol [-h] [-f {html,json,markdown,rst,tsv}] [-c {yes,no,auto}]
           [--clear-cache] [-v] [-V]
           [product ...]

CLI to show end-of-life dates for a number of products, from https://endoflife.date

For example:

* `eol python` to see Python EOLs
* `eol ubuntu` to see Ubuntu EOLs
* `eol centos fedora` to see CentOS and Fedora EOLs
* `eol all` to list all available products

Something missing? Please contribute! https://endoflife.date/contribute

positional arguments:
  product               Product to check, or 'all' to list all available
                        (default: ['all'])

options:
  -h, --help            show this help message and exit
  -f {html,json,markdown,rst,tsv}, --format {html,json,markdown,rst,tsv}
                        The format of output (default: markdown)
  -c {yes,no,auto}, --color {yes,no,auto}
                        color terminal output (default: auto)
  --clear-cache         Clear cache before running (default: False)
  -v, --verbose         Print debug messages to stderr (default: False)
  -V, --version         show program's version number and exit
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
almalinux
alpine
amazon-eks
amazon-linux
android
...
```

<!-- [[[end]]] -->

Show end-of-life dates:

<!-- [[[cog
run("norwegianblue python")
]]] -->

```console
$ norwegianblue python
| cycle | latest |  release   |    eol     |
|:------|:-------|:----------:|:----------:|
| 3.10  | 3.10.4 | 2021-10-04 | 2026-10-04 |
| 3.9   | 3.9.12 | 2020-10-05 | 2025-10-05 |
| 3.8   | 3.8.13 | 2019-10-14 | 2024-10-14 |
| 3.7   | 3.7.13 | 2018-06-27 | 2023-06-27 |
| 3.6   | 3.6.15 | 2016-12-23 | 2021-12-23 |
| 3.5   | 3.5.10 | 2015-09-13 | 2020-09-13 |
| 3.4   | 3.4.10 | 2014-03-16 | 2019-03-18 |
| 3.3   | 3.3.7  | 2012-09-29 | 2017-09-29 |
| 2.7   | 2.7.18 | 2010-07-03 | 2020-01-01 |
```

<!-- [[[end]]] -->

The table is Markdown, ready for pasting in GitHub issues and PRs:

<!-- [[[cog
run("norwegianblue python", with_console=False)
]]] -->

| cycle | latest |  release   |    eol     |
| :---- | :----- | :--------: | :--------: |
| 3.10  | 3.10.4 | 2021-10-04 | 2026-10-04 |
| 3.9   | 3.9.12 | 2020-10-05 | 2025-10-05 |
| 3.8   | 3.8.13 | 2019-10-14 | 2024-10-14 |
| 3.7   | 3.7.13 | 2018-06-27 | 2023-06-27 |
| 3.6   | 3.6.15 | 2016-12-23 | 2021-12-23 |
| 3.5   | 3.5.10 | 2015-09-13 | 2020-09-13 |
| 3.4   | 3.4.10 | 2014-03-16 | 2019-03-18 |
| 3.3   | 3.3.7  | 2012-09-29 | 2017-09-29 |
| 2.7   | 2.7.18 | 2010-07-03 | 2020-01-01 |

<!-- [[[end]]] -->

With options:

<!-- [[[cog
run("eol nodejs --format rst")
]]] -->

```console
$ eol nodejs --format rst
.. table::

    ========  ==========  ============  ============  ============
     cycle      latest      release       support         eol
    ========  ==========  ============  ============  ============
     17        17.8.0      2021-10-19    2022-04-01    2022-06-01
     16 LTS    16.14.2     2021-04-20    2022-10-18    2024-04-30
     15        15.14.0     2020-10-20    2021-04-01    2021-06-01
     14 LTS    14.19.1     2020-04-21    2021-10-19    2023-04-30
     12 LTS    12.22.11    2019-04-23    2020-10-20    2022-04-30
     10 LTS    10.24.1     2018-04-24    2020-05-19    2021-04-30
    ========  ==========  ============  ============  ============
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
