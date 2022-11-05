from __future__ import annotations

EXPECTED_HTML = """
<table>
    <thead>
        <tr>
            <th>cycle</th>
            <th>release</th>
            <th>latest</th>
            <th>support</th>
            <th>eol</th>
            <th>codename</th>
            <th>link</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="left">22.04 LTS</td>
            <td align="left">2022-04-21</td>
            <td align="left">22.04</td>
            <td align="left">2027-04-02</td>
            <td align="left">2032-04-01</td>
            <td align="left">Jammy Jellyfish</td>
            <td align="left">https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes/</td>
        </tr>
        <tr>
            <td align="left">21.10</td>
            <td align="left">2021-10-14</td>
            <td align="left">21.10</td>
            <td align="left">2022-07-31</td>
            <td align="left">2022-07-31</td>
            <td align="left">Impish Indri</td>
            <td align="left">https://wiki.ubuntu.com/ImpishIndri/ReleaseNotes/</td>
        </tr>
        <tr>
            <td align="left">21.04</td>
            <td align="left">2021-04-22</td>
            <td align="left">21.04</td>
            <td align="left">2022-01-20</td>
            <td align="left">2022-01-20</td>
            <td align="left">Hirsute Hippo</td>
            <td align="left">https://wiki.ubuntu.com/HirsuteHippo/ReleaseNotes/</td>
        </tr>
        <tr>
            <td align="left">20.10</td>
            <td align="left">2020-10-22</td>
            <td align="left">20.10</td>
            <td align="left">2021-07-22</td>
            <td align="left">2021-07-22</td>
            <td align="left">Groovy Gorilla</td>
            <td align="left"></td>
        </tr>
        <tr>
            <td align="left">20.04 LTS</td>
            <td align="left">2020-04-23</td>
            <td align="left">20.04.4</td>
            <td align="left">2025-04-02</td>
            <td align="left">2030-04-01</td>
            <td align="left">Focal Fossa</td>
            <td align="left"></td>
        </tr>
        <tr>
            <td align="left">19.10</td>
            <td align="left">2019-10-17</td>
            <td align="left">19.10</td>
            <td align="left">2020-07-06</td>
            <td align="left">2020-07-06</td>
            <td align="left">Karmic Koala</td>
            <td align="left"></td>
        </tr>
        <tr>
            <td align="left">18.04 LTS</td>
            <td align="left">2018-04-26</td>
            <td align="left">18.04.6</td>
            <td align="left">2023-04-02</td>
            <td align="left">2028-04-01</td>
            <td align="left">Bionic Beaver</td>
            <td align="left">https://wiki.ubuntu.com/BionicBeaver/ReleaseNotes</td>
        </tr>
        <tr>
            <td align="left">16.04 LTS</td>
            <td align="left">2016-04-21</td>
            <td align="left">16.04.7</td>
            <td align="left">2021-04-02</td>
            <td align="left">2026-04-01</td>
            <td align="left">Xenial Xerus</td>
            <td align="left"></td>
        </tr>
        <tr>
            <td align="left">14.04 LTS</td>
            <td align="left">2014-04-17</td>
            <td align="left">14.04.6</td>
            <td align="left">2019-04-02</td>
            <td align="left">2024-04-01</td>
            <td align="left">Trusty Tahr</td>
            <td align="left"></td>
        </tr>
    </tbody>
</table>
"""

EXPECTED_MD = """
| cycle     |  release   | latest  |  support   |    eol     |     codename    | link                                                 |
|:----------|:----------:|:--------|:----------:|:----------:|:---------------:|:-----------------------------------------------------|
| 22.04 LTS | 2022-04-21 | 22.04   | 2027-04-02 | 2032-04-01 | Jammy Jellyfish | https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes/ |
| 21.10     | 2021-10-14 | 21.10   | 2022-07-31 | 2022-07-31 |   Impish Indri  | https://wiki.ubuntu.com/ImpishIndri/ReleaseNotes/    |
| 21.04     | 2021-04-22 | 21.04   | 2022-01-20 | 2022-01-20 |  Hirsute Hippo  | https://wiki.ubuntu.com/HirsuteHippo/ReleaseNotes/   |
| 20.10     | 2020-10-22 | 20.10   | 2021-07-22 | 2021-07-22 |  Groovy Gorilla |                                                      |
| 20.04 LTS | 2020-04-23 | 20.04.4 | 2025-04-02 | 2030-04-01 |   Focal Fossa   |                                                      |
| 19.10     | 2019-10-17 | 19.10   | 2020-07-06 | 2020-07-06 |   Karmic Koala  |                                                      |
| 18.04 LTS | 2018-04-26 | 18.04.6 | 2023-04-02 | 2028-04-01 |  Bionic Beaver  | https://wiki.ubuntu.com/BionicBeaver/ReleaseNotes    |
| 16.04 LTS | 2016-04-21 | 16.04.7 | 2021-04-02 | 2026-04-01 |   Xenial Xerus  |                                                      |
| 14.04 LTS | 2014-04-17 | 14.04.6 | 2019-04-02 | 2024-04-01 |   Trusty Tahr   |                                                      |
"""  # noqa: E501


EXPECTED_MD_COLOUR = """
| cycle     |  release   | latest  |  support   |    eol     |     codename    | link                                                 |
|:----------|:----------:|:--------|:----------:|:----------:|:---------------:|:-----------------------------------------------------|
| 22.04 LTS | 2022-04-21 | 22.04   | [32m2027-04-02[0m | [32m2032-04-01[0m | Jammy Jellyfish | https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes/ |
| 21.10     | 2021-10-14 | 21.10   | [32m2022-07-31[0m | [32m2022-07-31[0m |   Impish Indri  | https://wiki.ubuntu.com/ImpishIndri/ReleaseNotes/    |
| 21.04     | 2021-04-22 | 21.04   | [33m2022-01-20[0m | [33m2022-01-20[0m |  Hirsute Hippo  | https://wiki.ubuntu.com/HirsuteHippo/ReleaseNotes/   |
| 20.10     | 2020-10-22 | 20.10   | [31m2021-07-22[0m | [31m2021-07-22[0m |  Groovy Gorilla |                                                      |
| 20.04 LTS | 2020-04-23 | 20.04.4 | [32m2025-04-02[0m | [32m2030-04-01[0m |   Focal Fossa   |                                                      |
| 19.10     | 2019-10-17 | 19.10   | [31m2020-07-06[0m | [31m2020-07-06[0m |   Karmic Koala  |                                                      |
| 18.04 LTS | 2018-04-26 | 18.04.6 | [32m2023-04-02[0m | [32m2028-04-01[0m |  Bionic Beaver  | https://wiki.ubuntu.com/BionicBeaver/ReleaseNotes    |
| 16.04 LTS | 2016-04-21 | 16.04.7 | [31m2021-04-02[0m | [32m2026-04-01[0m |   Xenial Xerus  |                                                      |
| 14.04 LTS | 2014-04-17 | 14.04.6 | [31m2019-04-02[0m | [32m2024-04-01[0m |   Trusty Tahr   |                                                      |
"""  # noqa: E501


EXPECTED_RST = """
.. table::

    ===========  ============  =========  ============  ============  =================  ======================================================
       cycle       release      latest      support         eol           codename                                link                         
    ===========  ============  =========  ============  ============  =================  ======================================================
     22.04 LTS    2022-04-21    22.04      2027-04-02    2032-04-01    Jammy Jellyfish    https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes/ 
     21.10        2021-10-14    21.10      2022-07-31    2022-07-31    Impish Indri       https://wiki.ubuntu.com/ImpishIndri/ReleaseNotes/    
     21.04        2021-04-22    21.04      2022-01-20    2022-01-20    Hirsute Hippo      https://wiki.ubuntu.com/HirsuteHippo/ReleaseNotes/   
     20.10        2020-10-22    20.10      2021-07-22    2021-07-22    Groovy Gorilla                                                          
     20.04 LTS    2020-04-23    20.04.4    2025-04-02    2030-04-01    Focal Fossa                                                             
     19.10        2019-10-17    19.10      2020-07-06    2020-07-06    Karmic Koala                                                            
     18.04 LTS    2018-04-26    18.04.6    2023-04-02    2028-04-01    Bionic Beaver      https://wiki.ubuntu.com/BionicBeaver/ReleaseNotes    
     16.04 LTS    2016-04-21    16.04.7    2021-04-02    2026-04-01    Xenial Xerus                                                            
     14.04 LTS    2014-04-17    14.04.6    2019-04-02    2024-04-01    Trusty Tahr                                                             
    ===========  ============  =========  ============  ============  =================  ======================================================
"""  # noqa: E501 W291

EXPECTED_CSV = """
"cycle","release","latest","support","eol","codename","link"
"22.04 LTS","2022-04-21","22.04","2027-04-02","2032-04-01","Jammy Jellyfish","https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes/"
"21.10","2021-10-14","21.10","2022-07-31","2022-07-31","Impish Indri","https://wiki.ubuntu.com/ImpishIndri/ReleaseNotes/"
"21.04","2021-04-22","21.04","2022-01-20","2022-01-20","Hirsute Hippo","https://wiki.ubuntu.com/HirsuteHippo/ReleaseNotes/"
"20.10","2020-10-22","20.10","2021-07-22","2021-07-22","Groovy Gorilla",
"20.04 LTS","2020-04-23","20.04.4","2025-04-02","2030-04-01","Focal Fossa",
"19.10","2019-10-17","19.10","2020-07-06","2020-07-06","Karmic Koala",
"18.04 LTS","2018-04-26","18.04.6","2023-04-02","2028-04-01","Bionic Beaver","https://wiki.ubuntu.com/BionicBeaver/ReleaseNotes"
"16.04 LTS","2016-04-21","16.04.7","2021-04-02","2026-04-01","Xenial Xerus",
"14.04 LTS","2014-04-17","14.04.6","2019-04-02","2024-04-01","Trusty Tahr",
"""  # noqa: E501 W291

EXPECTED_TSV = """
"cycle"	"release"	"latest"	"support"	"eol"	"codename"	"link"
"22.04 LTS"	"2022-04-21"	"22.04"	"2027-04-02"	"2032-04-01"	"Jammy Jellyfish"	"https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes/"
"21.10"	"2021-10-14"	"21.10"	"2022-07-31"	"2022-07-31"	"Impish Indri"	"https://wiki.ubuntu.com/ImpishIndri/ReleaseNotes/"
"21.04"	"2021-04-22"	"21.04"	"2022-01-20"	"2022-01-20"	"Hirsute Hippo"	"https://wiki.ubuntu.com/HirsuteHippo/ReleaseNotes/"
"20.10"	"2020-10-22"	"20.10"	"2021-07-22"	"2021-07-22"	"Groovy Gorilla"	
"20.04 LTS"	"2020-04-23"	"20.04.4"	"2025-04-02"	"2030-04-01"	"Focal Fossa"	
"19.10"	"2019-10-17"	"19.10"	"2020-07-06"	"2020-07-06"	"Karmic Koala"	
"18.04 LTS"	"2018-04-26"	"18.04.6"	"2023-04-02"	"2028-04-01"	"Bionic Beaver"	"https://wiki.ubuntu.com/BionicBeaver/ReleaseNotes"
"16.04 LTS"	"2016-04-21"	"16.04.7"	"2021-04-02"	"2026-04-01"	"Xenial Xerus"	
"14.04 LTS"	"2014-04-17"	"14.04.6"	"2019-04-02"	"2024-04-01"	"Trusty Tahr"	
"""  # noqa: E501 W291

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
