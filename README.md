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

### From [conda-forge][conda-forge]

#### With [Pixi][pixi]

```bash
pixi add norwegianblue
```

#### With [conda][conda]

```bash
conda install --channel conda-forge norwegianblue
```

[conda-forge]: https://github.com/conda-forge/norwegianblue-feedstock
[pixi]: https://pixi.sh/
[conda]: https://docs.conda.io/projects/conda/

### With [`pixi global`][pixi-global]

```bash
pixi global install norwegianblue
```

[pixi-global]: https://pixi.sh/latest/global_tools/introduction/

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
┌───────┬────────────┬─────────┬────────────────┬────────────┬────────────┬──────────┐
│ cycle │  release   │ latest  │ latest release │  support   │    eol     │   pep    │
├───────┼────────────┼─────────┼────────────────┼────────────┼────────────┼──────────┤
│ 3.14  │ 2025-10-07 │ 3.14.6  │   2026-06-10   │ 2027-10-01 │ 2030-10-31 │ PEP-0745 │
│ 3.13  │ 2024-10-07 │ 3.13.14 │   2026-06-10   │ 2026-10-01 │ 2029-10-31 │ PEP-0719 │
│ 3.12  │ 2023-10-02 │ 3.12.13 │   2026-03-03   │ 2025-04-02 │ 2028-10-31 │ PEP-0693 │
│ 3.11  │ 2022-10-24 │ 3.11.15 │   2026-03-03   │ 2024-04-01 │ 2027-10-31 │ PEP-0664 │
│ 3.10  │ 2021-10-04 │ 3.10.20 │   2026-03-03   │ 2023-04-05 │ 2026-10-31 │ PEP-0619 │
│ 3.9   │ 2020-10-05 │ 3.9.25  │   2025-10-31   │ 2022-05-17 │ 2025-10-31 │ PEP-0596 │
│ 3.8   │ 2019-10-14 │ 3.8.20  │   2024-09-06   │ 2021-05-03 │ 2024-10-07 │ PEP-0569 │
│ 3.7   │ 2018-06-27 │ 3.7.17  │   2023-06-05   │ 2020-06-27 │ 2023-06-27 │ PEP-0537 │
│ 3.6   │ 2016-12-23 │ 3.6.15  │   2021-09-03   │ 2018-12-24 │ 2021-12-23 │ PEP-0494 │
│ 3.5   │ 2015-09-13 │ 3.5.10  │   2020-09-05   │   False    │ 2020-09-30 │ PEP-0478 │
│ 3.4   │ 2014-03-16 │ 3.4.10  │   2019-03-18   │   False    │ 2019-03-18 │ PEP-0429 │
│ 3.3   │ 2012-09-29 │ 3.3.7   │   2017-09-19   │   False    │ 2017-09-29 │ PEP-0398 │
│ 3.2   │ 2011-02-20 │ 3.2.6   │   2014-10-12   │   False    │ 2016-02-20 │ PEP-0392 │
│ 2.7   │ 2010-07-03 │ 2.7.18  │   2020-04-19   │   False    │ 2020-01-01 │ PEP-0373 │
│ 3.1   │ 2009-06-27 │ 3.1.5   │   2012-04-06   │   False    │ 2012-04-09 │ PEP-0375 │
│ 3.0   │ 2008-12-03 │ 3.0.1   │   2009-02-12   │   False    │ 2009-06-27 │ PEP-0361 │
│ 2.6   │ 2008-10-01 │ 2.6.9   │   2013-10-29   │   False    │ 2013-10-29 │ PEP-0361 │
└───────┴────────────┴─────────┴────────────────┴────────────┴────────────┴──────────┘
```

<!-- [[[end]]] -->

You can format in Markdown, ready for pasting in GitHub issues and PRs:

<!-- [[[cog
run("eol python --md", with_console=False)
]]] -->

| cycle |  release   | latest  | latest release |  support   |    eol     |   pep    |
| :---- | :--------: | :------ | :------------: | :--------: | :--------: | :------: |
| 3.14  | 2025-10-07 | 3.14.6  |   2026-06-10   | 2027-10-01 | 2030-10-31 | PEP-0745 |
| 3.13  | 2024-10-07 | 3.13.14 |   2026-06-10   | 2026-10-01 | 2029-10-31 | PEP-0719 |
| 3.12  | 2023-10-02 | 3.12.13 |   2026-03-03   | 2025-04-02 | 2028-10-31 | PEP-0693 |
| 3.11  | 2022-10-24 | 3.11.15 |   2026-03-03   | 2024-04-01 | 2027-10-31 | PEP-0664 |
| 3.10  | 2021-10-04 | 3.10.20 |   2026-03-03   | 2023-04-05 | 2026-10-31 | PEP-0619 |
| 3.9   | 2020-10-05 | 3.9.25  |   2025-10-31   | 2022-05-17 | 2025-10-31 | PEP-0596 |
| 3.8   | 2019-10-14 | 3.8.20  |   2024-09-06   | 2021-05-03 | 2024-10-07 | PEP-0569 |
| 3.7   | 2018-06-27 | 3.7.17  |   2023-06-05   | 2020-06-27 | 2023-06-27 | PEP-0537 |
| 3.6   | 2016-12-23 | 3.6.15  |   2021-09-03   | 2018-12-24 | 2021-12-23 | PEP-0494 |
| 3.5   | 2015-09-13 | 3.5.10  |   2020-09-05   |   False    | 2020-09-30 | PEP-0478 |
| 3.4   | 2014-03-16 | 3.4.10  |   2019-03-18   |   False    | 2019-03-18 | PEP-0429 |
| 3.3   | 2012-09-29 | 3.3.7   |   2017-09-19   |   False    | 2017-09-29 | PEP-0398 |
| 3.2   | 2011-02-20 | 3.2.6   |   2014-10-12   |   False    | 2016-02-20 | PEP-0392 |
| 2.7   | 2010-07-03 | 2.7.18  |   2020-04-19   |   False    | 2020-01-01 | PEP-0373 |
| 3.1   | 2009-06-27 | 3.1.5   |   2012-04-06   |   False    | 2012-04-09 | PEP-0375 |
| 3.0   | 2008-12-03 | 3.0.1   |   2009-02-12   |   False    | 2009-06-27 | PEP-0361 |
| 2.6   | 2008-10-01 | 2.6.9   |   2013-10-29   |   False    | 2013-10-29 | PEP-0361 |

<!-- [[[end]]] -->

Or in other formats such as reStructuredText:

<!-- [[[cog
run("eol python --rst")
]]] -->

```console
$ eol python --rst
+-------+------------+---------+----------------+------------+------------+----------+
| cycle |  release   | latest  | latest release |  support   |    eol     |   pep    |
+=======+============+=========+================+============+============+==========+
| 3.14  | 2025-10-07 | 3.14.6  |   2026-06-10   | 2027-10-01 | 2030-10-31 | PEP-0745 |
+-------+------------+---------+----------------+------------+------------+----------+
| 3.13  | 2024-10-07 | 3.13.14 |   2026-06-10   | 2026-10-01 | 2029-10-31 | PEP-0719 |
+-------+------------+---------+----------------+------------+------------+----------+
| 3.12  | 2023-10-02 | 3.12.13 |   2026-03-03   | 2025-04-02 | 2028-10-31 | PEP-0693 |
+-------+------------+---------+----------------+------------+------------+----------+
| 3.11  | 2022-10-24 | 3.11.15 |   2026-03-03   | 2024-04-01 | 2027-10-31 | PEP-0664 |
+-------+------------+---------+----------------+------------+------------+----------+
| 3.10  | 2021-10-04 | 3.10.20 |   2026-03-03   | 2023-04-05 | 2026-10-31 | PEP-0619 |
+-------+------------+---------+----------------+------------+------------+----------+
| 3.9   | 2020-10-05 | 3.9.25  |   2025-10-31   | 2022-05-17 | 2025-10-31 | PEP-0596 |
+-------+------------+---------+----------------+------------+------------+----------+
| 3.8   | 2019-10-14 | 3.8.20  |   2024-09-06   | 2021-05-03 | 2024-10-07 | PEP-0569 |
+-------+------------+---------+----------------+------------+------------+----------+
| 3.7   | 2018-06-27 | 3.7.17  |   2023-06-05   | 2020-06-27 | 2023-06-27 | PEP-0537 |
+-------+------------+---------+----------------+------------+------------+----------+
| 3.6   | 2016-12-23 | 3.6.15  |   2021-09-03   | 2018-12-24 | 2021-12-23 | PEP-0494 |
+-------+------------+---------+----------------+------------+------------+----------+
| 3.5   | 2015-09-13 | 3.5.10  |   2020-09-05   |   False    | 2020-09-30 | PEP-0478 |
+-------+------------+---------+----------------+------------+------------+----------+
| 3.4   | 2014-03-16 | 3.4.10  |   2019-03-18   |   False    | 2019-03-18 | PEP-0429 |
+-------+------------+---------+----------------+------------+------------+----------+
| 3.3   | 2012-09-29 | 3.3.7   |   2017-09-19   |   False    | 2017-09-29 | PEP-0398 |
+-------+------------+---------+----------------+------------+------------+----------+
| 3.2   | 2011-02-20 | 3.2.6   |   2014-10-12   |   False    | 2016-02-20 | PEP-0392 |
+-------+------------+---------+----------------+------------+------------+----------+
| 2.7   | 2010-07-03 | 2.7.18  |   2020-04-19   |   False    | 2020-01-01 | PEP-0373 |
+-------+------------+---------+----------------+------------+------------+----------+
| 3.1   | 2009-06-27 | 3.1.5   |   2012-04-06   |   False    | 2012-04-09 | PEP-0375 |
+-------+------------+---------+----------------+------------+------------+----------+
| 3.0   | 2008-12-03 | 3.0.1   |   2009-02-12   |   False    | 2009-06-27 | PEP-0361 |
+-------+------------+---------+----------------+------------+------------+----------+
| 2.6   | 2008-10-01 | 2.6.9   |   2013-10-29   |   False    | 2013-10-29 | PEP-0361 |
+-------+------------+---------+----------------+------------+------------+----------+
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
