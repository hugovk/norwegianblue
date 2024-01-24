from __future__ import annotations

SAMPLE_RESPONSE_ALL_JSON = """
[
    "alpine",
    "amazon-linux",
    "android",
    "bootstrap",
    "centos"
]
"""


SAMPLE_RESPONSE_JSON_LOG4J = """
[
  {
    "cycle": "2",
    "cycleShortHand": 299,
    "eol": false,
    "latest": "2.17.2",
    "releaseDate": "2014-07-12"
  },
  {
    "cycle": "2.12",
    "cycleShortHand": 212,
    "eol": "2021-12-14",
    "latest": "2.12.4",
    "releaseDate": "2019-06-23"
  },
  {
    "cycle": "2.3",
    "cycleShortHand": 203,
    "eol": "2015-09-20",
    "latest": "2.3.2",
    "releaseDate": "2015-05-09"
  },
  {
    "cycle": "1",
    "cycleShortHand": 100,
    "eol": "2015-10-15",
    "latest": "1.2.17",
    "releaseDate": "2001-01-08"
  }
]
"""

SAMPLE_RESPONSE_JSON_PYTHON = """
[
  {
    "cycle": "3.10",
    "eol": "2026-10-04",
    "latest": "3.10.5",
    "latestReleaseDate": "2022-06-06",
    "releaseDate": "2021-10-04"
  },
  {
    "cycle": "3.9",
    "eol": "2025-10-05",
    "latest": "3.9.13",
    "latestReleaseDate": "2022-05-17",
    "releaseDate": "2020-10-05"
  },
  {
    "cycle": "3.8",
    "eol": "2024-10-14",
    "latest": "3.8.13",
    "latestReleaseDate": "2022-03-16",
    "releaseDate": "2019-10-14"
  },
  {
    "cycle": "3.7",
    "eol": "2023-06-27",
    "latest": "3.7.13",
    "latestReleaseDate": "2022-03-16",
    "releaseDate": "2018-06-26"
  },
  {
    "cycle": "3.6",
    "eol": "2021-12-23",
    "latest": "3.6.15",
    "latestReleaseDate": "2021-09-03",
    "releaseDate": "2016-12-22"
  },
  {
    "cycle": "3.5",
    "eol": "2020-09-13",
    "latest": "3.5.10",
    "latestReleaseDate": "2020-09-05",
    "releaseDate": "2015-09-12"
  },
  {
    "cycle": "3.4",
    "eol": "2019-03-18",
    "latest": "3.4.10",
    "latestReleaseDate": "2019-03-18",
    "releaseDate": "2014-03-15"
  },
  {
    "cycle": "3.3",
    "eol": "2017-09-29",
    "latest": "3.3.7",
    "latestReleaseDate": "2017-09-19",
    "releaseDate": "2012-09-29"
  },
  {
    "cycle": "2.7",
    "eol": "2020-01-01",
    "latest": "2.7.18",
    "latestReleaseDate": "2020-04-19",
    "releaseDate": "2010-07-03"
  }
]
"""

SAMPLE_RESPONSE_JSON_RHEL = """
[
  {
    "cycle": "9",
    "releaseDate": "2022-05-17",
    "support": "2027-05-31",
    "eol": "2032-05-31",
    "lts": "2032-05-31",
    "extendedSupport": "2035-05-31",
    "latest": "9.3",
    "latestReleaseDate": "2023-11-07"
  },
  {
    "cycle": "8",
    "releaseDate": "2019-05-07",
    "support": "2024-05-31",
    "eol": "2029-05-31",
    "lts": "2029-05-31",
    "extendedSupport": "2032-05-31",
    "latest": "8.9",
    "latestReleaseDate": "2023-11-14"
  },
  {
    "cycle": "7",
    "releaseDate": "2013-12-11",
    "support": "2019-08-06",
    "eol": "2024-06-30",
    "lts": "2024-06-30",
    "extendedSupport": "2028-06-30",
    "latest": "7.9",
    "latestReleaseDate": "2020-09-29"
  },
  {
    "cycle": "6",
    "releaseDate": "2010-11-09",
    "support": "2016-05-10",
    "eol": "2020-11-30",
    "lts": "2020-11-30",
    "extendedSupport": "2024-06-30",
    "latest": "6.10",
    "latestReleaseDate": "2018-06-19"
  },
  {
    "cycle": "5",
    "releaseDate": "2007-03-15",
    "support": "2013-01-08",
    "eol": "2017-03-31",
    "lts": "2017-03-31",
    "extendedSupport": "2020-11-30",
    "latest": "5.11",
    "latestReleaseDate": "2014-09-16"
  },
  {
    "cycle": "4",
    "releaseDate": "2005-02-15",
    "support": "2009-03-31",
    "eol": "2012-02-29",
    "extendedSupport": "2017-03-31",
    "latest": "4.9",
    "latestReleaseDate": "2011-02-16",
    "lts": false
  }
]
"""

SAMPLE_RESPONSE_JSON_UBUNTU = """
[
  {
    "cycle": "22.04",
    "codename": "Jammy Jellyfish",
    "support": "2027-04-02",
    "eol": "2032-04-01",
    "lts": true,
    "latest": "22.04",
    "link": "https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes/",
    "releaseDate": "2022-04-21"
  },
  {
    "cycle": "21.10",
    "codename": "Impish Indri",
    "support": "2022-07-31",
    "eol": "2022-07-31",
    "latest": "21.10",
    "link": "https://wiki.ubuntu.com/ImpishIndri/ReleaseNotes/",
    "releaseDate": "2021-10-14"
  },
  {
    "cycle": "21.04",
    "codename": "Hirsute Hippo",
    "support": "2022-01-20",
    "eol": "2022-01-20",
    "latest": "21.04",
    "link": "https://wiki.ubuntu.com/HirsuteHippo/ReleaseNotes/",
    "releaseDate": "2021-04-22"
  },
  {
    "cycle": "20.10",
    "codename": "Groovy Gorilla",
    "support": "2021-07-22",
    "eol": "2021-07-22",
    "latest": "20.10",
    "releaseDate": "2020-10-22"
  },
  {
    "cycle": "20.04",
    "codename": "Focal Fossa",
    "lts": true,
    "support": "2025-04-02",
    "eol": "2030-04-01",
    "latest": "20.04.4",
    "releaseDate": "2020-04-23"
  },
  {
    "cycle": "19.10",
    "codename": "Karmic Koala",
    "support": "2020-07-06",
    "eol": "2020-07-06",
    "latest": "19.10",
    "releaseDate": "2019-10-17"
  },
  {
    "cycle": "18.04",
    "codename": "Bionic Beaver",
    "lts": true,
    "support": "2023-04-02",
    "eol": "2028-04-01",
    "latest": "18.04.6",
    "link": "https://wiki.ubuntu.com/BionicBeaver/ReleaseNotes",
    "releaseDate": "2018-04-26"
  },
  {
    "cycle": "16.04",
    "codename": "Xenial Xerus",
    "lts": true,
    "support": "2021-04-02",
    "eol": "2026-04-01",
    "latest": "16.04.7",
    "releaseDate": "2016-04-21"
  },
  {
    "cycle": "14.04",
    "codename": "Trusty Tahr",
    "lts": true,
    "support": "2019-04-02",
    "eol": "2024-04-01",
    "latest": "14.04.6",
    "releaseDate": "2014-04-17"
  }
]
"""
