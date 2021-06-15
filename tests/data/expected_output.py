EXPECTED_HTML = """
<table>
    <thead>
        <tr>
            <th>cycle</th>
            <th>latest</th>
            <th>release</th>
            <th>support</th>
            <th>eol</th>
            <th>cycleShortHand</th>
            <th>link</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="left">21.04 LTS</td>
            <td align="left">21.04</td>
            <td align="left">2021-04-22</td>
            <td align="left">2022-01-01</td>
            <td align="left">2022-01-01</td>
            <td align="left">HirsuteHippo</td>
            <td align="left">https://wiki.ubuntu.com/HirsuteHippo/ReleaseNotes/</td>
        </tr>
        <tr>
            <td align="left">20.10 LTS</td>
            <td align="left">20.10</td>
            <td align="left">2020-10-22</td>
            <td align="left">2021-07-07</td>
            <td align="left">2021-07-07</td>
            <td align="left">GroovyGorilla</td>
            <td align="left">https://wiki.ubuntu.com/GroovyGorilla/ReleaseNotes/</td>
        </tr>
        <tr>
            <td align="left">20.04 LTS</td>
            <td align="left">20.04.2</td>
            <td align="left">2020-04-23</td>
            <td align="left">2022-10-01</td>
            <td align="left">2025-04-02</td>
            <td align="left">FocalFossa</td>
            <td align="left"></td>
        </tr>
        <tr>
            <td align="left">19.10</td>
            <td align="left">19.10</td>
            <td align="left">2019-10-17</td>
            <td align="left">2020-07-06</td>
            <td align="left">2020-07-06</td>
            <td align="left"></td>
            <td align="left"></td>
        </tr>
        <tr>
            <td align="left">18.04 LTS</td>
            <td align="left">18.04.5</td>
            <td align="left">2018-04-26</td>
            <td align="left">2020-09-30</td>
            <td align="left">2023-04-02</td>
            <td align="left">BionicBeaver</td>
            <td align="left"></td>
        </tr>
        <tr>
            <td align="left">16.04 LTS</td>
            <td align="left">16.04.7</td>
            <td align="left">2016-04-21</td>
            <td align="left">2018-10-01</td>
            <td align="left">2021-04-02</td>
            <td align="left">XenialXerus</td>
            <td align="left"></td>
        </tr>
        <tr>
            <td align="left">14.04 LTS</td>
            <td align="left">14.04.6</td>
            <td align="left">2014-04-17</td>
            <td align="left">2016-09-30</td>
            <td align="left">2019-04-02</td>
            <td align="left">TrustyTahr</td>
            <td align="left"></td>
        </tr>
    </tbody>
</table>
"""

EXPECTED_MD = """
|   cycle   | latest  |  release   |  support   |    eol     | cycleShortHand |                        link                         |
| --------- | ------- | ---------- | ---------- | ---------- | -------------- | --------------------------------------------------- |
| 21.04 LTS | 21.04   | 2021-04-22 | 2022-01-01 | 2022-01-01 | HirsuteHippo   | https://wiki.ubuntu.com/HirsuteHippo/ReleaseNotes/  |
| 20.10 LTS | 20.10   | 2020-10-22 | 2021-07-07 | 2021-07-07 | GroovyGorilla  | https://wiki.ubuntu.com/GroovyGorilla/ReleaseNotes/ |
| 20.04 LTS | 20.04.2 | 2020-04-23 | 2022-10-01 | 2025-04-02 | FocalFossa     |                                                     |
| 19.10     | 19.10   | 2019-10-17 | 2020-07-06 | 2020-07-06 |                |                                                     |
| 18.04 LTS | 18.04.5 | 2018-04-26 | 2020-09-30 | 2023-04-02 | BionicBeaver   |                                                     |
| 16.04 LTS | 16.04.7 | 2016-04-21 | 2018-10-01 | 2021-04-02 | XenialXerus    |                                                     |
| 14.04 LTS | 14.04.6 | 2014-04-17 | 2016-09-30 | 2019-04-02 | TrustyTahr     |                                                     |
"""  # noqa: E501


EXPECTED_RST = """
.. table:: 

    ===========  =========  ============  ============  ============  ================  =====================================================
       cycle      latest      release       support         eol        cycleShortHand                           link                         
    ===========  =========  ============  ============  ============  ================  =====================================================
     21.04 LTS    21.04      2021-04-22    2022-01-01    2022-01-01    HirsuteHippo      https://wiki.ubuntu.com/HirsuteHippo/ReleaseNotes/  
     20.10 LTS    20.10      2020-10-22    2021-07-07    2021-07-07    GroovyGorilla     https://wiki.ubuntu.com/GroovyGorilla/ReleaseNotes/ 
     20.04 LTS    20.04.2    2020-04-23    2022-10-01    2025-04-02    FocalFossa                                                            
     19.10        19.10      2019-10-17    2020-07-06    2020-07-06                                                                          
     18.04 LTS    18.04.5    2018-04-26    2020-09-30    2023-04-02    BionicBeaver                                                          
     16.04 LTS    16.04.7    2016-04-21    2018-10-01    2021-04-02    XenialXerus                                                           
     14.04 LTS    14.04.6    2014-04-17    2016-09-30    2019-04-02    TrustyTahr                                                            
    ===========  =========  ============  ============  ============  ================  =====================================================
"""  # noqa: E501 W291

EXPECTED_TSV = """
"cycle"	"latest"	"release"	"support"	"eol"	"cycleShortHand"	"link"
"21.04 LTS"	"21.04"	"2021-04-22"	"2022-01-01"	"2022-01-01"	"HirsuteHippo"	"https://wiki.ubuntu.com/HirsuteHippo/ReleaseNotes/"
"20.10 LTS"	"20.10"	"2020-10-22"	"2021-07-07"	"2021-07-07"	"GroovyGorilla"	"https://wiki.ubuntu.com/GroovyGorilla/ReleaseNotes/"
"20.04 LTS"	"20.04.2"	"2020-04-23"	"2022-10-01"	"2025-04-02"	"FocalFossa"	
"19.10"	"19.10"	"2019-10-17"	"2020-07-06"	"2020-07-06"		
"18.04 LTS"	"18.04.5"	"2018-04-26"	"2020-09-30"	"2023-04-02"	"BionicBeaver"	
"16.04 LTS"	"16.04.7"	"2016-04-21"	"2018-10-01"	"2021-04-02"	"XenialXerus"	
"14.04 LTS"	"14.04.6"	"2014-04-17"	"2016-09-30"	"2019-04-02"	"TrustyTahr"	
"""  # noqa: E501 W291
