from __future__ import annotations

EXPECTED_HTML = """
<table>
    <thead>
        <tr>
            <th>cycle</th>
            <th>codename</th>
            <th>release</th>
            <th>latest</th>
            <th>support</th>
            <th>eol</th>
            <th>link</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="left">22.04 LTS</td>
            <td align="left">Jammy Jellyfish</td>
            <td align="left">2022-04-21</td>
            <td align="left">22.04</td>
            <td align="left"><font color="green">2027-04-02</font></td>
            <td align="left"><font color="green">2032-04-01</font></td>
            <td align="left">https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes/</td>
        </tr>
        <tr>
            <td align="left">21.10</td>
            <td align="left">Impish Indri</td>
            <td align="left">2021-10-14</td>
            <td align="left">21.10</td>
            <td align="left"><font color="red">2022-07-31</font></td>
            <td align="left"><font color="red">2022-07-31</font></td>
            <td align="left">https://wiki.ubuntu.com/ImpishIndri/ReleaseNotes/</td>
        </tr>
        <tr>
            <td align="left">21.04</td>
            <td align="left">Hirsute Hippo</td>
            <td align="left">2021-04-22</td>
            <td align="left">21.04</td>
            <td align="left"><font color="red">2022-01-20</font></td>
            <td align="left"><font color="red">2022-01-20</font></td>
            <td align="left">https://wiki.ubuntu.com/HirsuteHippo/ReleaseNotes/</td>
        </tr>
        <tr>
            <td align="left">20.10</td>
            <td align="left">Groovy Gorilla</td>
            <td align="left">2020-10-22</td>
            <td align="left">20.10</td>
            <td align="left"><font color="red">2021-07-22</font></td>
            <td align="left"><font color="red">2021-07-22</font></td>
            <td align="left"></td>
        </tr>
        <tr>
            <td align="left">20.04 LTS</td>
            <td align="left">Focal Fossa</td>
            <td align="left">2020-04-23</td>
            <td align="left">20.04.4</td>
            <td align="left"><font color="green">2025-04-02</font></td>
            <td align="left"><font color="green">2030-04-01</font></td>
            <td align="left"></td>
        </tr>
        <tr>
            <td align="left">19.10</td>
            <td align="left">Karmic Koala</td>
            <td align="left">2019-10-17</td>
            <td align="left">19.10</td>
            <td align="left"><font color="red">2020-07-06</font></td>
            <td align="left"><font color="red">2020-07-06</font></td>
            <td align="left"></td>
        </tr>
        <tr>
            <td align="left">18.04 LTS</td>
            <td align="left">Bionic Beaver</td>
            <td align="left">2018-04-26</td>
            <td align="left">18.04.6</td>
            <td align="left"><font color="red">2023-04-02</font></td>
            <td align="left"><font color="green">2028-04-01</font></td>
            <td align="left">https://wiki.ubuntu.com/BionicBeaver/ReleaseNotes</td>
        </tr>
        <tr>
            <td align="left">16.04 LTS</td>
            <td align="left">Xenial Xerus</td>
            <td align="left">2016-04-21</td>
            <td align="left">16.04.7</td>
            <td align="left"><font color="red">2021-04-02</font></td>
            <td align="left"><font color="green">2026-04-01</font></td>
            <td align="left"></td>
        </tr>
        <tr>
            <td align="left">14.04 LTS</td>
            <td align="left">Trusty Tahr</td>
            <td align="left">2014-04-17</td>
            <td align="left">14.04.6</td>
            <td align="left"><font color="red">2019-04-02</font></td>
            <td align="left"><font color="yellow">2024-04-01</font></td>
            <td align="left"></td>
        </tr>
    </tbody>
</table>
"""

EXPECTED_MD = """
| cycle     |     codename    |  release   | latest  |  support   |    eol     | link                                                 |
|:----------|:---------------:|:----------:|:--------|:----------:|:----------:|:-----------------------------------------------------|
| 22.04 LTS | Jammy Jellyfish | 2022-04-21 | 22.04   | 2027-04-02 | 2032-04-01 | https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes/ |
| 21.10     |   Impish Indri  | 2021-10-14 | 21.10   | 2022-07-31 | 2022-07-31 | https://wiki.ubuntu.com/ImpishIndri/ReleaseNotes/    |
| 21.04     |  Hirsute Hippo  | 2021-04-22 | 21.04   | 2022-01-20 | 2022-01-20 | https://wiki.ubuntu.com/HirsuteHippo/ReleaseNotes/   |
| 20.10     |  Groovy Gorilla | 2020-10-22 | 20.10   | 2021-07-22 | 2021-07-22 |                                                      |
| 20.04 LTS |   Focal Fossa   | 2020-04-23 | 20.04.4 | 2025-04-02 | 2030-04-01 |                                                      |
| 19.10     |   Karmic Koala  | 2019-10-17 | 19.10   | 2020-07-06 | 2020-07-06 |                                                      |
| 18.04 LTS |  Bionic Beaver  | 2018-04-26 | 18.04.6 | 2023-04-02 | 2028-04-01 | https://wiki.ubuntu.com/BionicBeaver/ReleaseNotes    |
| 16.04 LTS |   Xenial Xerus  | 2016-04-21 | 16.04.7 | 2021-04-02 | 2026-04-01 |                                                      |
| 14.04 LTS |   Trusty Tahr   | 2014-04-17 | 14.04.6 | 2019-04-02 | 2024-04-01 |                                                      |
"""  # noqa: E501


EXPECTED_MD_COLOUR = """
| cycle     |     codename    |  release   | latest  |  support   |    eol     | link                                                 |
|:----------|:---------------:|:----------:|:--------|:----------:|:----------:|:-----------------------------------------------------|
| 22.04 LTS | Jammy Jellyfish | 2022-04-21 | 22.04   | \x1b[32m2027-04-02\x1b[0m | \x1b[32m2032-04-01\x1b[0m | https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes/ |
| 21.10     |   Impish Indri  | 2021-10-14 | 21.10   | \x1b[32m2022-07-31\x1b[0m | \x1b[32m2022-07-31\x1b[0m | https://wiki.ubuntu.com/ImpishIndri/ReleaseNotes/    |
| 21.04     |  Hirsute Hippo  | 2021-04-22 | 21.04   | \x1b[33m2022-01-20\x1b[0m | \x1b[33m2022-01-20\x1b[0m | https://wiki.ubuntu.com/HirsuteHippo/ReleaseNotes/   |
| 20.10     |  Groovy Gorilla | 2020-10-22 | 20.10   | \x1b[31m2021-07-22\x1b[0m | \x1b[31m2021-07-22\x1b[0m |                                                      |
| 20.04 LTS |   Focal Fossa   | 2020-04-23 | 20.04.4 | \x1b[32m2025-04-02\x1b[0m | \x1b[32m2030-04-01\x1b[0m |                                                      |
| 19.10     |   Karmic Koala  | 2019-10-17 | 19.10   | \x1b[31m2020-07-06\x1b[0m | \x1b[31m2020-07-06\x1b[0m |                                                      |
| 18.04 LTS |  Bionic Beaver  | 2018-04-26 | 18.04.6 | \x1b[32m2023-04-02\x1b[0m | \x1b[32m2028-04-01\x1b[0m | https://wiki.ubuntu.com/BionicBeaver/ReleaseNotes    |
| 16.04 LTS |   Xenial Xerus  | 2016-04-21 | 16.04.7 | \x1b[31m2021-04-02\x1b[0m | \x1b[32m2026-04-01\x1b[0m |                                                      |
| 14.04 LTS |   Trusty Tahr   | 2014-04-17 | 14.04.6 | \x1b[31m2019-04-02\x1b[0m | \x1b[32m2024-04-01\x1b[0m |                                                      |
"""  # noqa: E501

EXPECTED_PRETTY_REMAINDER = """
│ cycle     │     codename    │  release   │ latest  │  support   │    eol     │ link                                                 │
├───────────┼─────────────────┼────────────┼─────────┼────────────┼────────────┼──────────────────────────────────────────────────────┤
│ 22.04 LTS │ Jammy Jellyfish │ 2022-04-21 │ 22.04   │ 2027-04-02 │ 2032-04-01 │ https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes/ │
│ 21.10     │   Impish Indri  │ 2021-10-14 │ 21.10   │ 2022-07-31 │ 2022-07-31 │ https://wiki.ubuntu.com/ImpishIndri/ReleaseNotes/    │
│ 21.04     │  Hirsute Hippo  │ 2021-04-22 │ 21.04   │ 2022-01-20 │ 2022-01-20 │ https://wiki.ubuntu.com/HirsuteHippo/ReleaseNotes/   │
│ 20.10     │  Groovy Gorilla │ 2020-10-22 │ 20.10   │ 2021-07-22 │ 2021-07-22 │                                                      │
│ 20.04 LTS │   Focal Fossa   │ 2020-04-23 │ 20.04.4 │ 2025-04-02 │ 2030-04-01 │                                                      │
│ 19.10     │   Karmic Koala  │ 2019-10-17 │ 19.10   │ 2020-07-06 │ 2020-07-06 │                                                      │
│ 18.04 LTS │  Bionic Beaver  │ 2018-04-26 │ 18.04.6 │ 2023-04-02 │ 2028-04-01 │ https://wiki.ubuntu.com/BionicBeaver/ReleaseNotes    │
│ 16.04 LTS │   Xenial Xerus  │ 2016-04-21 │ 16.04.7 │ 2021-04-02 │ 2026-04-01 │                                                      │
│ 14.04 LTS │   Trusty Tahr   │ 2014-04-17 │ 14.04.6 │ 2019-04-02 │ 2024-04-01 │                                                      │
└───────────┴─────────────────┴────────────┴─────────┴────────────┴────────────┴──────────────────────────────────────────────────────┘
"""  # noqa: E501

EXPECTED_PRETTY = (
    """
┌───────────┬─────────────────┬────────────┬─────────┬────────────┬────────────┬──────────────────────────────────────────────────────┐
""".rstrip()
    + EXPECTED_PRETTY_REMAINDER
)

EXPECTED_PRETTY_WITH_TITLE = (
    """
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                                ubuntu                                                               │
├───────────┬─────────────────┬────────────┬─────────┬────────────┬────────────┬──────────────────────────────────────────────────────┤
""".rstrip()  # noqa: E501
    + EXPECTED_PRETTY_REMAINDER
)

EXPECTED_RST = """
.. table::

    ===========  =================  ============  =========  ============  ============  ======================================================
       cycle         codename         release      latest      support         eol                                link                         
    ===========  =================  ============  =========  ============  ============  ======================================================
     22.04 LTS    Jammy Jellyfish    2022-04-21    22.04      2027-04-02    2032-04-01    https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes/ 
     21.10        Impish Indri       2021-10-14    21.10      2022-07-31    2022-07-31    https://wiki.ubuntu.com/ImpishIndri/ReleaseNotes/    
     21.04        Hirsute Hippo      2021-04-22    21.04      2022-01-20    2022-01-20    https://wiki.ubuntu.com/HirsuteHippo/ReleaseNotes/   
     20.10        Groovy Gorilla     2020-10-22    20.10      2021-07-22    2021-07-22                                                         
     20.04 LTS    Focal Fossa        2020-04-23    20.04.4    2025-04-02    2030-04-01                                                         
     19.10        Karmic Koala       2019-10-17    19.10      2020-07-06    2020-07-06                                                         
     18.04 LTS    Bionic Beaver      2018-04-26    18.04.6    2023-04-02    2028-04-01    https://wiki.ubuntu.com/BionicBeaver/ReleaseNotes    
     16.04 LTS    Xenial Xerus       2016-04-21    16.04.7    2021-04-02    2026-04-01                                                         
     14.04 LTS    Trusty Tahr        2014-04-17    14.04.6    2019-04-02    2024-04-01                                                         
    ===========  =================  ============  =========  ============  ============  ======================================================
"""  # noqa: E501 W291

EXPECTED_CSV = """
"cycle","codename","release","latest","support","eol","link"
"22.04 LTS","Jammy Jellyfish","2022-04-21","22.04","2027-04-02","2032-04-01","https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes/"
"21.10","Impish Indri","2021-10-14","21.10","2022-07-31","2022-07-31","https://wiki.ubuntu.com/ImpishIndri/ReleaseNotes/"
"21.04","Hirsute Hippo","2021-04-22","21.04","2022-01-20","2022-01-20","https://wiki.ubuntu.com/HirsuteHippo/ReleaseNotes/"
"20.10","Groovy Gorilla","2020-10-22","20.10","2021-07-22","2021-07-22",
"20.04 LTS","Focal Fossa","2020-04-23","20.04.4","2025-04-02","2030-04-01",
"19.10","Karmic Koala","2019-10-17","19.10","2020-07-06","2020-07-06",
"18.04 LTS","Bionic Beaver","2018-04-26","18.04.6","2023-04-02","2028-04-01","https://wiki.ubuntu.com/BionicBeaver/ReleaseNotes"
"16.04 LTS","Xenial Xerus","2016-04-21","16.04.7","2021-04-02","2026-04-01",
"14.04 LTS","Trusty Tahr","2014-04-17","14.04.6","2019-04-02","2024-04-01",
"""

EXPECTED_TSV = """
"cycle"\t"codename"\t"release"\t"latest"\t"support"\t"eol"\t"link"
"22.04 LTS"\t"Jammy Jellyfish"\t"2022-04-21"\t"22.04"\t"2027-04-02"\t"2032-04-01"\t"https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes/"
"21.10"\t"Impish Indri"\t"2021-10-14"\t"21.10"\t"2022-07-31"\t"2022-07-31"\t"https://wiki.ubuntu.com/ImpishIndri/ReleaseNotes/"
"21.04"\t"Hirsute Hippo"\t"2021-04-22"\t"21.04"\t"2022-01-20"\t"2022-01-20"\t"https://wiki.ubuntu.com/HirsuteHippo/ReleaseNotes/"
"20.10"\t"Groovy Gorilla"\t"2020-10-22"\t"20.10"\t"2021-07-22"\t"2021-07-22"\t
"20.04 LTS"\t"Focal Fossa"\t"2020-04-23"\t"20.04.4"\t"2025-04-02"\t"2030-04-01"\t
"19.10"\t"Karmic Koala"\t"2019-10-17"\t"19.10"\t"2020-07-06"\t"2020-07-06"\t
"18.04 LTS"\t"Bionic Beaver"\t"2018-04-26"\t"18.04.6"\t"2023-04-02"\t"2028-04-01"\t"https://wiki.ubuntu.com/BionicBeaver/ReleaseNotes"
"16.04 LTS"\t"Xenial Xerus"\t"2016-04-21"\t"16.04.7"\t"2021-04-02"\t"2026-04-01"\t
"14.04 LTS"\t"Trusty Tahr"\t"2014-04-17"\t"14.04.6"\t"2019-04-02"\t"2024-04-01"\t
"""

EXPECTED_MD_LOG4J = """
| cycle |  release   | latest |    eol     |
|:------|:----------:|:-------|:----------:|
| 2     | 2014-07-12 | 2.17.2 |   False    |
| 2.12  | 2019-06-23 | 2.12.4 | 2021-12-14 |
| 2.3   | 2015-05-09 | 2.3.2  | 2015-09-20 |
| 1     | 2001-01-08 | 1.2.17 | 2015-10-15 |
"""

EXPECTED_MD_PYTHON = """
| cycle |  release   | latest | latest release |    eol     |
|:------|:----------:|:-------|:--------------:|:----------:|
| 3.10  | 2021-10-04 | 3.10.5 |   2022-06-06   | 2026-10-04 |
| 3.9   | 2020-10-05 | 3.9.13 |   2022-05-17   | 2025-10-05 |
| 3.8   | 2019-10-14 | 3.8.13 |   2022-03-16   | 2024-10-14 |
| 3.7   | 2018-06-26 | 3.7.13 |   2022-03-16   | 2023-06-27 |
| 3.6   | 2016-12-22 | 3.6.15 |   2021-09-03   | 2021-12-23 |
| 3.5   | 2015-09-12 | 3.5.10 |   2020-09-05   | 2020-09-13 |
| 3.4   | 2014-03-15 | 3.4.10 |   2019-03-18   | 2019-03-18 |
| 3.3   | 2012-09-29 | 3.3.7  |   2017-09-19   | 2017-09-29 |
| 2.7   | 2010-07-03 | 2.7.18 |   2020-04-19   | 2020-01-01 |
"""

EXPECTED_MD_RHEL = """
| cycle |  release   | latest | latest release |  support   |    eol     | extended support |
|:------|:----------:|:-------|:--------------:|:----------:|:----------:|:----------------:|
| 9 LTS | 2022-05-17 | 9.3    |   2023-11-07   | 2027-05-31 | 2032-05-31 |    2035-05-31    |
| 8 LTS | 2019-05-07 | 8.9    |   2023-11-14   | 2024-05-31 | 2029-05-31 |    2032-05-31    |
| 7 LTS | 2013-12-11 | 7.9    |   2020-09-29   | 2019-08-06 | 2024-06-30 |    2028-06-30    |
| 6 LTS | 2010-11-09 | 6.10   |   2018-06-19   | 2016-05-10 | 2020-11-30 |    2024-06-30    |
| 5 LTS | 2007-03-15 | 5.11   |   2014-09-16   | 2013-01-08 | 2017-03-31 |    2020-11-30    |
| 4     | 2005-02-15 | 4.9    |   2011-02-16   | 2009-03-31 | 2012-02-29 |    2017-03-31    |
"""
