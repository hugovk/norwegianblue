# norwegianblue

[![PyPI version](https://img.shields.io/pypi/v/norwegianblue.svg?logo=pypi&logoColor=FFE873)](https://pypi.org/project/norwegianblue/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/norwegianblue.svg?logo=python&logoColor=FFE873)](https://pypi.org/project/norwegianblue/)
[![PyPI downloads](https://img.shields.io/pypi/dm/norwegianblue.svg)](https://pypistats.org/packages/norwegianblue)
[![Test](https://github.com/hugovk/norwegianblue/actions/workflows/test.yml/badge.svg)](https://github.com/hugovk/norwegianblue/actions)
[![codecov](https://codecov.io/gh/hugovk/norwegianblue/branch/main/graph/badge.svg)](https://codecov.io/gh/hugovk/norwegianblue)
[![GitHub](https://img.shields.io/github/license/hugovk/norwegianblue.svg)](LICENSE.txt)
[![Code style: Black](https://img.shields.io/badge/code%20style-Black-000000.svg)](https://github.com/psf/black)

Python 3.7+ interface to [endoflife.date](https://endoflife.date/docs/api/) to show
end-of-life dates for a number of products.

## Installation

### From PyPI

```bash
python -m pip install --upgrade norwegianblue
```

### From source

```bash
git clone https://github.com/hugovk/norwegianblue
cd norwegianblue
pip install .
```

## Example command-line use

Run `norwegianblue` or `eol`, they do the same thing.

Top-level help:

```console
$ eol --help
usage: eol [-h] [-f {html,json,markdown,rst,tsv}] [-c {yes,no,auto}] [-v] [-V]
           [product]

CLI to show end-of-life dates for a number of products.

positional arguments:
  product               Product to check, or 'all' to list all available
                        (default: all)

optional arguments:
  -h, --help            show this help message and exit
  -f {html,json,markdown,rst,tsv}, --format {html,json,markdown,rst,tsv}
                        The format of output (default: markdown)
  -c {yes,no,auto}, --color {yes,no,auto}
                        color terminal output (default: auto)
  -v, --verbose         Print debug messages to stderr (default: False)
  -V, --version         show program's version number and exit
```

List all available products with end-of-life dates:

```console
$ # eol all
$ # or:
$ eol
alpine
amazon-linux
android
bootstrap
centos
...
```

Show end-of-life dates:

```console
$ norwegianblue python
| cycle | latest |  release   |    eol     |                                 link                                 |
| ----- | ------ | ---------- | ---------- | -------------------------------------------------------------------- |
| 3.9   | 3.9.6  | 2020-10-05 | 2025-10-05 | https://www.python.org/downloads/release/python-396/                 |
| 3.8   | 3.8.11 | 2019-10-14 | 2024-10-14 | https://www.python.org/downloads/release/python-3811/                |
| 3.7   | 3.7.11 | 2018-06-27 | 2023-06-27 | https://www.python.org/downloads/release/python-3711/                |
| 3.6   | 3.6.14 | 2016-12-23 | 2021-12-23 | https://www.python.org/downloads/release/python-3614/                |
| 3.5   | 3.5.10 | 2015-09-30 | 2020-09-13 | https://www.python.org/downloads/release/python-3510/                |
| 3.4   | 3.4.10 | 2014-03-16 | 2019-03-18 | https://www.python.org/downloads/release/python-3410/                |
| 3.3   | 3.3.7  | 2012-09-29 | 2017-09-29 | https://www.python.org/downloads/release/python-337/                 |
| 2.7   | 2.7.18 | 2010-07-03 | 2020-01-01 | https://github.com/python/cpython/blob/2.7/Misc/NEWS.d/2.7.18rc1.rst |
```

The table is Markdown, ready for pasting in GitHub issues and PRs:

| cycle | latest | release    | eol        | link                                                                 |
| ----- | ------ | ---------- | ---------- | -------------------------------------------------------------------- |
| 3.9   | 3.9.6  | 2020-10-05 | 2025-10-05 | https://www.python.org/downloads/release/python-396/                 |
| 3.8   | 3.8.11 | 2019-10-14 | 2024-10-14 | https://www.python.org/downloads/release/python-3811/                |
| 3.7   | 3.7.11 | 2018-06-27 | 2023-06-27 | https://www.python.org/downloads/release/python-3711/                |
| 3.6   | 3.6.14 | 2016-12-23 | 2021-12-23 | https://www.python.org/downloads/release/python-3614/                |
| 3.5   | 3.5.10 | 2015-09-30 | 2020-09-13 | https://www.python.org/downloads/release/python-3510/                |
| 3.4   | 3.4.10 | 2014-03-16 | 2019-03-18 | https://www.python.org/downloads/release/python-3410/                |
| 3.3   | 3.3.7  | 2012-09-29 | 2017-09-29 | https://www.python.org/downloads/release/python-337/                 |
| 2.7   | 2.7.18 | 2010-07-03 | 2020-01-01 | https://github.com/python/cpython/blob/2.7/Misc/NEWS.d/2.7.18rc1.rst |

With options:

```console
$ eol ubuntu --format rst
.. table::

    ===========  =========  ============  ============  ============  =====================================================
       cycle      latest      release       support         eol                               link
    ===========  =========  ============  ============  ============  =====================================================
     21.04 LTS    21.04      2021-04-22    2022-01-01    2022-01-01    https://wiki.ubuntu.com/HirsuteHippo/ReleaseNotes/
     20.10 LTS    20.10      2020-10-22    2021-07-07    2021-07-07    https://wiki.ubuntu.com/GroovyGorilla/ReleaseNotes/
     20.04 LTS    20.04.2    2020-04-23    2022-10-01    2025-04-02
     19.10        19.10      2019-10-17    2020-07-06    2020-07-06
     18.04 LTS    18.04.5    2018-04-26    2020-09-30    2023-04-02
     16.04 LTS    16.04.7    2016-04-21    2018-10-01    2021-04-02
     14.04 LTS    14.04.6    2014-04-17    2016-09-30    2019-04-02
    ===========  =========  ============  ============  ============  =====================================================
```

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
