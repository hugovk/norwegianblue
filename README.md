# pypistats

[![PyPI version](https://img.shields.io/pypi/v/pypistats.svg)](https://pypi.org/project/pypistats/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/pypistats.svg)](https://pypi.org/project/pypistats/)
[![PyPI downloads](https://img.shields.io/pypi/dm/pypistats.svg)](https://pypistats.org/packages/pypistats)
[![Build Status](https://travis-ci.org/hugovk/pypistats.svg?branch=master)](https://travis-ci.org/hugovk/pypistats)
[![Build Status](https://dev.azure.com/hugovk/hugovk/_apis/build/status/hugovk.pypistats?branchName=master)](https://dev.azure.com/hugovk/hugovk/_build/latest?definitionId=1?branchName=master)
[![Actions Status](https://github.com/hugovk/pypistats/workflows/test/badge.svg)](https://github.com/hugovk/pypistats/actions)
[![codecov](https://codecov.io/gh/hugovk/pypistats/branch/master/graph/badge.svg)](https://codecov.io/gh/hugovk/pypistats)
[![GitHub](https://img.shields.io/github/license/hugovk/pypistats.svg)](LICENSE.txt)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Python 3.6+ interface to [PyPI Stats API](https://pypistats.org/api) to get aggregate
download statistics on Python packages on the Python Package Index without having to
execute queries directly against Google BigQuery.

## Installation

### From PyPI

```bash
pip install --upgrade pypistats
```

### From source

```bash
git clone https://github.com/hugovk/pypistats
cd pypistats
pip install .
```

## Example command-line use

Run `pypistats` with a subcommand (corresponding to [PyPI Stats endpoints](https://pypistats.org/api/#endpoints)),
then options for that subcommand.

Top-level help:

```console
$ pypistats --help
usage: pypistats [-h] [-V]
                 {recent,overall,python_major,python_minor,system} ...

positional arguments:
  {recent,overall,python_major,python_minor,system}

optional arguments:
  -h, --help            show this help message and exit
  -V, --version         show program's version number and exit
  ```

Help for a subcommand:

```console
$ pypistats recent --help
usage: pypistats recent [-h] [-p {day,week,month}]
                        [-f {json,markdown,rst,html}] [-j] [-v]
                        package

Retrieve the aggregate download quantities for the last day/week/month

positional arguments:
  package

optional arguments:
  -h, --help            show this help message and exit
  -p {day,week,month}, --period {day,week,month}
  -f {json,markdown,rst,html}, --format {json,markdown,rst,html}
                        The format of output (default: markdown)
  -j, --json            Shortcut for "-f json" (default: False)
  -v, --verbose         Print debug messages to stderr (default: False)
```

Get recent downloads:

```console
$ pypistats recent pillow
| last_day | last_month | last_week |
|---------:|-----------:|----------:|
|  280,842 |  7,065,928 | 1,709,689 |
```

Help for another subcommand:

```console
$ pypistats python_minor --help
usage: pypistats python_minor [-h] [-V VERSION] [-f {json,markdown,rst,html}]
                              [-j] [-sd yyyy-mm[-dd]|name]
                              [-ed yyyy-mm[-dd]|name] [-m yyyy-mm|name] [-l]
                              [-t] [-d] [--monthly] [-v]
                              package

Retrieve the aggregate daily download time series by Python minor version
number

positional arguments:
  package

optional arguments:
  -h, --help            show this help message and exit
  -V VERSION, --version VERSION
                        eg. 2.7 or 3.6 (default: None)
  -f {json,markdown,rst,html}, --format {json,markdown,rst,html}
                        The format of output (default: markdown)
  -j, --json            Shortcut for "-f json" (default: False)
  -sd yyyy-mm[-dd]|name, --start-date yyyy-mm[-dd]|name
                        Start date (default: None)
  -ed yyyy-mm[-dd]|name, --end-date yyyy-mm[-dd]|name
                        End date (default: None)
  -m yyyy-mm|name, --month yyyy-mm|name
                        Shortcut for -sd & -ed for a single month (default:
                        None)
  -l, --last-month      Shortcut for -sd & -ed for last month (default: False)
  -t, --this-month      Shortcut for -sd for this month (default: False)
  -d, --daily           Show daily downloads (default: False)
  --monthly             Show monthly downloads (default: False)
  -v, --verbose         Print debug messages to stderr (default: False)
```

Get version downloads:

```console
$ pypistats python_minor pillow --last-month
| category | percent | downloads |
|----------|--------:|----------:|
| 2.7      |  35.94% | 2,189,327 |
| 3.6      |  31.83% | 1,938,870 |
| 3.7      |  18.71% | 1,139,642 |
| 3.5      |  11.29% |   687,782 |
| 3.4      |   1.23% |    74,673 |
| null     |   0.94% |    57,476 |
| 3.8      |   0.04% |     2,147 |
| 2.6      |   0.01% |       826 |
| 3.3      |   0.00% |       212 |
| 3.2      |   0.00% |        28 |
| 2.4      |   0.00% |         6 |
| 3.9      |   0.00% |         5 |
| 2.8      |   0.00% |         1 |
| Total    |         | 6,090,995 |
```

The table is Markdown, ready for pasting in GitHub issues and PRs:

| category | percent | downloads |
|----------|--------:|----------:|
| 2.7      |  35.94% | 2,189,327 |
| 3.6      |  31.83% | 1,938,870 |
| 3.7      |  18.71% | 1,139,642 |
| 3.5      |  11.29% |   687,782 |
| 3.4      |   1.23% |    74,673 |
| null     |   0.94% |    57,476 |
| 3.8      |   0.04% |     2,147 |
| 2.6      |   0.01% |       826 |
| 3.3      |   0.00% |       212 |
| 3.2      |   0.00% |        28 |
| 2.4      |   0.00% |         6 |
| 3.9      |   0.00% |         5 |
| 2.8      |   0.00% |         1 |
| Total    |         | 6,090,995 |

These are equivalent (in May 2019):

```sh
pypistats python_major pip --last-month
pypistats python_major pip --month april
pypistats python_major pip --month apr
pypistats python_major pip --month 2019-04
```

And:

```sh
pypistats python_major pip --start-date december --end-date january
pypistats python_major pip --start-date dec      --end-date jan
pypistats python_major pip --start-date 2018-12  --end-date 2019-01
```

## Example programmatic use

Return values are from the JSON responses documented in the API:
https://pypistats.org/api/

```python
import pypistats
from pprint import pprint

# Call the API
print(pypistats.recent("pillow"))
print(pypistats.recent("pillow", "day", format="markdown"))
print(pypistats.recent("pillow", "week", format="rst"))
print(pypistats.recent("pillow", "month", format="html"))
pprint(pypistats.recent("pillow", "week", format="json"))
print(pypistats.recent("pillow", "day"))

print(pypistats.overall("pillow"))
print(pypistats.overall("pillow", mirrors=True, format="markdown"))
print(pypistats.overall("pillow", mirrors=False, format="rst"))
print(pypistats.overall("pillow", mirrors=True, format="html"))
pprint(pypistats.overall("pillow", mirrors=False, format="json"))

print(pypistats.python_major("pillow"))
print(pypistats.python_major("pillow", version=2, format="markdown"))
print(pypistats.python_major("pillow", version=3, format="rst"))
print(pypistats.python_major("pillow", version="2", format="html"))
pprint(pypistats.python_major("pillow", version="3", format="json"))

print(pypistats.python_minor("pillow"))
print(pypistats.python_minor("pillow", version=2.7, format="markdown"))
print(pypistats.python_minor("pillow", version="2.7", format="rst"))
print(pypistats.python_minor("pillow", version=3.7, format="html"))
pprint(pypistats.python_minor("pillow", version="3.7", format="json"))

print(pypistats.system("pillow"))
print(pypistats.system("pillow", os="darwin", format="markdown"))
print(pypistats.system("pillow", os="linux", format="rst"))
print(pypistats.system("pillow", os="darwin", format="html"))
pprint(pypistats.system("pillow", os="linux", format="json"))
```

### Numpy and Pandas

Return pre-formatted code to create NumPy arrays or Pandas DataFrames
leveraging the [`pytablewriter`](https://github.com/thombashi/pytablewriter)
package. Use the `table_name` argument to specify the variable name of the
array/DataFrame.

```python
import pypistats
import pandas as pd
import numpy as np

print(pypistats.overall("pyvista", total=True,
                       format="pandas",
                       table_name="downloads"))
```
```
downloads = pd.DataFrame([
    [ "with_mirrors" ,  "54.39%" ,  22408 ],
    [ "without_mirrors" ,  "45.61%" ,  18789 ],
    [ "Total" ,  None ,  41197 ],
], columns=["category", "percent", "downloads"])
```

Instead of printing the result, call `exec()` to make the `table_name` variable
live in the active Python session:

```python
exec(pypistats.overall("pyvista",
                       format="pandas",
                       table_name="downloads"))
downloads.head()
```
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>category</th>
      <th>percent</th>
      <th>downloads</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>with_mirrors</td>
      <td>54.39%</td>
      <td>22408</td>
    </tr>
    <tr>
      <th>1</th>
      <td>without_mirrors</td>
      <td>45.61%</td>
      <td>18789</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Total</td>
      <td>None</td>
      <td>41197</td>
    </tr>
  </tbody>
</table>
</div>
