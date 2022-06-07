"""
Unit tests for norwegianblue
"""
import json
import os
from pathlib import Path
from unittest import mock

import pytest
import respx
from freezegun import freeze_time

import norwegianblue
from norwegianblue import _cache

from .data.expected_output import (
    EXPECTED_HTML,
    EXPECTED_MD,
    EXPECTED_MD_COLOUR,
    EXPECTED_RST,
    EXPECTED_TSV,
)

SAMPLE_RESPONSE_JSON = """
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

SAMPLE_RESPONSE_ALL_JSON = """
[
    "alpine",
    "amazon-linux",
    "android",
    "bootstrap",
    "centos"
]
"""


def stub__cache_filename(*args):
    return Path("/this/does/not/exist")


def stub__save_cache(*args) -> None:
    pass


class TestNorwegianBlue:
    def setup_method(self) -> None:
        # Stub caching. Caches are tested in another class.
        self.original__cache_filename = _cache.filename
        self.original__save_cache = _cache.save
        _cache.filename = stub__cache_filename
        _cache.save = stub__save_cache

    def teardown_method(self) -> None:
        # Unstub caching
        _cache.filename = self.original__cache_filename
        _cache.save = self.original__save_cache

    @respx.mock
    @pytest.mark.parametrize(
        "test_format, expected",
        [
            pytest.param("html", EXPECTED_HTML, id="html"),
            pytest.param("markdown", EXPECTED_MD, id="markdown"),
            pytest.param("rst", EXPECTED_RST, id="rst"),
            pytest.param("tsv", EXPECTED_TSV, id="tsv"),
        ],
    )
    def test_norwegianblue(self, test_format: str, expected: str) -> None:
        # Arrange
        mocked_url = "https://endoflife.date/api/ubuntu.json"
        mocked_response = SAMPLE_RESPONSE_JSON

        # Act
        respx.get(mocked_url).respond(content=mocked_response)
        output = norwegianblue.norwegianblue(product="ubuntu", format=test_format)

        # Assert
        assert output.strip() == expected.strip()

    @mock.patch.dict(os.environ, {"NO_COLOR": "TRUE"})
    @respx.mock
    def test_norwegianblue_no_color(self) -> None:
        # Arrange
        mocked_url = "https://endoflife.date/api/ubuntu.json"
        mocked_response = SAMPLE_RESPONSE_JSON
        expected = EXPECTED_MD

        # Act
        respx.get(mocked_url).respond(content=mocked_response)
        output = norwegianblue.norwegianblue(product="ubuntu")

        # Assert
        assert output.strip() == expected.strip()

    @freeze_time("2021-09-13")
    @mock.patch.dict(os.environ, {"FORCE_COLOR": "TRUE"})
    @respx.mock
    def test_norwegianblue_force_color(self) -> None:
        # Arrange
        mocked_url = "https://endoflife.date/api/ubuntu.json"
        mocked_response = SAMPLE_RESPONSE_JSON
        expected = EXPECTED_MD_COLOUR

        # Act
        respx.get(mocked_url).respond(content=mocked_response)
        output = norwegianblue.norwegianblue(product="ubuntu")

        # Assert
        assert output.strip() == expected.strip()

    @respx.mock
    def test_norwegianblue_json(self) -> None:
        # Arrange
        mocked_url = "https://endoflife.date/api/ubuntu.json"
        mocked_response = SAMPLE_RESPONSE_JSON

        # Act
        respx.get(mocked_url).respond(content=mocked_response)
        output = norwegianblue.norwegianblue(product="ubuntu", format="json")

        # Assert
        assert json.loads(output) == json.loads(SAMPLE_RESPONSE_JSON)

    @freeze_time("2021-06-15")
    def test__colourify(self) -> None:
        # Arrange
        data = [
            {
                "cycle": "21.04 LTS",
                "release": "2021-04-22",
                "support": "2022-01-01",
                "eol": "2022-01-01",
            },
            {
                "cycle": "20.10 LTS",
                "release": "2020-10-22",
                "support": "2021-07-07",
                "eol": "2021-07-07",
            },
            {
                "cycle": "19.10",
                "release": "2019-10-17",
                "support": "2020-07-06",
                "eol": "2020-07-06",
            },
            {
                "cycle": "18.04 LTS",
                "release": "2018-04-26",
                "support": "2020-09-30",
                "eol": "2023-04-02",
            },
        ]
        expected = [
            {
                "cycle": "21.04 LTS",
                "release": "2021-04-22",
                "support": "\x1b[32m2022-01-01\x1b[0m",  # green
                "eol": "\x1b[32m2022-01-01\x1b[0m",  # green
            },
            {
                "cycle": "20.10 LTS",
                "release": "2020-10-22",
                "support": "\x1b[33m2021-07-07\x1b[0m",  # yellow
                "eol": "\x1b[33m2021-07-07\x1b[0m",  # yellow
            },
            {
                "cycle": "19.10",
                "release": "2019-10-17",
                "support": "\x1b[31m2020-07-06\x1b[0m",  # red
                "eol": "\x1b[31m2020-07-06\x1b[0m",  # red
            },
            {
                "cycle": "18.04 LTS",
                "release": "2018-04-26",
                "support": "\x1b[31m2020-09-30\x1b[0m",  # red
                "eol": "\x1b[32m2023-04-02\x1b[0m",  # green
            },
        ]

        # Act
        output = norwegianblue._colourify(data)

        # Assert
        assert output == expected

    @freeze_time("2021-06-16")
    def test__colourify_boolean_support(self) -> None:
        # Arrange
        data = [
            {
                "cycle": "5.x",
                "eol": False,
                "support": True,
            },
            {
                "cycle": "4.x",
                "eol": "2022-11-01",
                "support": False,
            },
            {
                "cycle": "3.x",
                "eol": "2019-07-24",
                "support": False,
            },
        ]
        expected = [
            {
                "cycle": "5.x",
                "eol": "\x1b[32mFalse\x1b[0m",  # green
                "support": "\x1b[32mTrue\x1b[0m",  # green
            },
            {
                "cycle": "4.x",
                "eol": "\x1b[32m2022-11-01\x1b[0m",  # green
                "support": "\x1b[31mFalse\x1b[0m",  # red
            },
            {
                "cycle": "3.x",
                "eol": "\x1b[31m2019-07-24\x1b[0m",  # red
                "support": "\x1b[31mFalse\x1b[0m",  # red
            },
        ]

        # Act
        output = norwegianblue._colourify(data)

        # Assert
        assert output == expected

    def test__colourify_boolean_eol(self) -> None:
        # Arrange
        data = [
            {"cycle": "1.15", "release": "2020-08-11", "eol": False},
            {"cycle": "1.14", "release": "2020-02-25", "eol": True},
        ]
        expected = [
            # green
            {"cycle": "1.15", "release": "2020-08-11", "eol": "\x1b[32mFalse\x1b[0m"},
            # red
            {"cycle": "1.14", "release": "2020-02-25", "eol": "\x1b[31mTrue\x1b[0m"},
        ]

        # Act
        output = norwegianblue._colourify(data)

        # Assert
        assert output == expected

    def test__colourify_boolean_discontinued(self) -> None:
        # Arrange
        data = [
            {
                "cycle": "iPhone 5C",
                "discontinued": "2025-09-09",
                "eol": True,
            },
            {
                "cycle": "iPhone 5S",
                "discontinued": "2016-03-21",
                "eol": True,
            },
            {
                "cycle": "iPhone 6S / 6S Plus",
                "discontinued": "2018-09-12",
                "eol": False,
            },
            {
                "cycle": "iPhone XR",
                "discontinued": False,
                "eol": False,
            },
            {
                "cycle": "iPhone 11 Pro / 11 Pro Max",
                "discontinued": "2020-10-13",
                "eol": False,
            },
            {
                "cycle": "iPhone 12 Mini / 12 Pro Max",
                "discontinued": True,
                "eol": False,
            },
        ]

        expected = [
            {
                "cycle": "iPhone 5C",
                "discontinued": "\x1b[32m2025-09-09\x1b[0m",  # green
                "eol": "\x1b[31mTrue\x1b[0m",  # red
            },
            {
                "cycle": "iPhone 5S",
                "discontinued": "\x1b[31m2016-03-21\x1b[0m",  # red
                "eol": "\x1b[31mTrue\x1b[0m",  # red
            },
            {
                "cycle": "iPhone 6S / 6S Plus",
                "discontinued": "\x1b[31m2018-09-12\x1b[0m",  # red
                "eol": "\x1b[32mFalse\x1b[0m",  # green
            },
            {
                "cycle": "iPhone XR",
                "discontinued": "\x1b[32mFalse\x1b[0m",  # red
                "eol": "\x1b[32mFalse\x1b[0m",  # green
            },
            {
                "cycle": "iPhone 11 Pro / 11 Pro Max",
                "discontinued": "\x1b[31m2020-10-13\x1b[0m",  # red
                "eol": "\x1b[32mFalse\x1b[0m",  # green
            },
            {
                "cycle": "iPhone 12 Mini / 12 Pro Max",
                "discontinued": "\x1b[31mTrue\x1b[0m",  # red
                "eol": "\x1b[32mFalse\x1b[0m",  # green
            },
        ]

        # Act
        output = norwegianblue._colourify(data)

        # Assert
        assert output == expected

    @mock.patch.dict(os.environ, {"NO_COLOR": "TRUE"})
    def test_no_color(self) -> None:
        assert norwegianblue._can_do_colour() is False

    @mock.patch.dict(os.environ, {"FORCE_COLOR": "TRUE"})
    def test_force_color(self) -> None:
        assert norwegianblue._can_do_colour() is True

    @respx.mock
    def test_all_products(self) -> None:
        # Arrange
        mocked_url = "https://endoflife.date/api/all.json"
        mocked_response = SAMPLE_RESPONSE_ALL_JSON
        expected = """alpine\namazon-linux\nandroid\nbootstrap\ncentos"""

        # Act
        respx.get(mocked_url).respond(content=mocked_response)
        output = norwegianblue.norwegianblue(product="all")

        # Assert
        assert output == expected

    @respx.mock
    def test_404(self) -> None:
        # Arrange
        mocked_url = "https://endoflife.date/api/this-product-not-found.json"

        # Act
        respx.get(mocked_url).respond(status_code=404)
        output = norwegianblue.norwegianblue(product="this-product-not-found")

        # Assert
        assert output.strip() == norwegianblue.ERROR_404_TEXT

    def test_norwegianblue_norwegianblue(self) -> None:
        # Act
        output = norwegianblue.norwegianblue(product="norwegianblue")

        # Assert
        assert "Norwegian Blue" in output

    def test__ltsify(self) -> None:
        # Arrange
        data = [
            {"cycle": "5.3", "eol": "2022-01-01", "lts": False},
            {"cycle": "4.4", "eol": "2023-11-21", "lts": True},
            {"cycle": "4.3", "eol": "2020-07-01", "lts": False},
            {"cycle": "3.4", "eol": "2021-11-01", "lts": True},
        ]
        expected = [
            {"cycle": "5.3", "eol": "2022-01-01"},
            {"cycle": "4.4 LTS", "eol": "2023-11-21"},
            {"cycle": "4.3", "eol": "2020-07-01"},
            {"cycle": "3.4 LTS", "eol": "2021-11-01"},
        ]

        # Act
        output = norwegianblue._ltsify(data)

        # Assert
        assert output == expected
