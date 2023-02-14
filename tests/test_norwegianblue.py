"""
Unit tests for norwegianblue
"""
from __future__ import annotations

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
    EXPECTED_CSV,
    EXPECTED_HTML,
    EXPECTED_MD,
    EXPECTED_MD_COLOUR,
    EXPECTED_MD_LOG4J,
    EXPECTED_MD_PYTHON,
    EXPECTED_PRETTY,
    EXPECTED_PRETTY_WITH_TITLE,
    EXPECTED_RST,
    EXPECTED_TSV,
)
from .data.sample_response import (
    SAMPLE_RESPONSE_ALL_JSON,
    SAMPLE_RESPONSE_JSON_LOG4J,
    SAMPLE_RESPONSE_JSON_PYTHON,
    SAMPLE_RESPONSE_JSON_UBUNTU,
)

EXPECTED_HTML_WITH_TITLE = EXPECTED_HTML.replace(
    "<table>",
    '<table id="ubuntu">\n    <caption>ubuntu</caption>',
)
EXPECTED_RST_WITH_TITLE = EXPECTED_RST.replace(".. table::", ".. table:: ubuntu")
EXPECTED_MD_WITH_TITLE = "## ubuntu\n" + EXPECTED_MD


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
        "test_format, test_show_title, expected",
        [
            pytest.param("csv", False, EXPECTED_CSV, id="csv"),
            pytest.param("csv", True, EXPECTED_CSV, id="csv"),
            pytest.param("html", False, EXPECTED_HTML, id="html"),
            pytest.param("html", True, EXPECTED_HTML_WITH_TITLE, id="html"),
            pytest.param("markdown", False, EXPECTED_MD, id="markdown"),
            pytest.param("markdown", True, EXPECTED_MD_WITH_TITLE, id="markdown"),
            pytest.param("pretty", False, EXPECTED_PRETTY, id="pretty"),
            pytest.param("pretty", True, EXPECTED_PRETTY_WITH_TITLE, id="pretty"),
            pytest.param("rst", False, EXPECTED_RST, id="rst"),
            pytest.param("rst", True, EXPECTED_RST_WITH_TITLE, id="rst"),
            pytest.param("tsv", False, EXPECTED_TSV, id="tsv"),
            pytest.param("tsv", True, EXPECTED_TSV, id="tsv"),
        ],
    )
    def test_norwegianblue_formats(
        self, test_format: str, test_show_title: bool, expected: str
    ) -> None:
        # Arrange
        mocked_url = "https://endoflife.date/api/ubuntu.json"
        mocked_response = SAMPLE_RESPONSE_JSON_UBUNTU

        # Act
        respx.get(mocked_url).respond(content=mocked_response)
        output = norwegianblue.norwegianblue(
            product="ubuntu", format=test_format, show_title=test_show_title
        )

        # Assert
        assert output.strip() == expected.strip()

    @respx.mock
    @pytest.mark.parametrize(
        "test_product, sample_response, expected",
        [
            pytest.param(
                "log4j", SAMPLE_RESPONSE_JSON_LOG4J, EXPECTED_MD_LOG4J, id="log4j"
            ),
            pytest.param(
                "python", SAMPLE_RESPONSE_JSON_PYTHON, EXPECTED_MD_PYTHON, id="python"
            ),
        ],
    )
    def test_norwegianblue_products(
        self, test_product: str, sample_response: str, expected: str
    ) -> None:
        """Test other headers not present in Ubuntu:
        * rename of releaseDate and latestReleaseDate headers (Python)
        * skip of cycleShortHand (Log4j)"""
        # Arrange
        mocked_url = f"https://endoflife.date/api/{test_product}.json"
        mocked_response = sample_response

        # Act
        respx.get(mocked_url).respond(content=mocked_response)
        output = norwegianblue.norwegianblue(product=test_product, format="markdown")

        # Assert
        assert output.strip() == expected.strip()

    @mock.patch.dict(os.environ, {"NO_COLOR": "TRUE"})
    @respx.mock
    def test_norwegianblue_no_color(self) -> None:
        # Arrange
        mocked_url = "https://endoflife.date/api/ubuntu.json"
        mocked_response = SAMPLE_RESPONSE_JSON_UBUNTU
        expected = EXPECTED_MD

        # Act
        respx.get(mocked_url).respond(content=mocked_response)
        output = norwegianblue.norwegianblue(product="ubuntu", format="markdown")

        # Assert
        assert output.strip() == expected.strip()

    @freeze_time("2021-09-13")
    @mock.patch.dict(os.environ, {"FORCE_COLOR": "TRUE"})
    @respx.mock
    def test_norwegianblue_force_color(self) -> None:
        # Arrange
        mocked_url = "https://endoflife.date/api/ubuntu.json"
        mocked_response = SAMPLE_RESPONSE_JSON_UBUNTU
        expected = EXPECTED_MD_COLOUR

        # Act
        respx.get(mocked_url).respond(content=mocked_response)
        output = norwegianblue.norwegianblue(product="ubuntu", format="md")

        # Assert
        assert output.strip() == expected.strip()

    @respx.mock
    def test_norwegianblue_json(self) -> None:
        # Arrange
        mocked_url = "https://endoflife.date/api/ubuntu.json"
        mocked_response = SAMPLE_RESPONSE_JSON_UBUNTU

        # Act
        respx.get(mocked_url).respond(content=mocked_response)
        output = norwegianblue.norwegianblue(product="ubuntu", format="json")

        # Assert
        assert json.loads(output) == json.loads(SAMPLE_RESPONSE_JSON_UBUNTU)

    @freeze_time("2021-06-15")
    @mock.patch.dict(os.environ, {"FORCE_COLOR": "TRUE"})
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
    @mock.patch.dict(os.environ, {"FORCE_COLOR": "TRUE"})
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

    @mock.patch.dict(os.environ, {"FORCE_COLOR": "TRUE"})
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

    @mock.patch.dict(os.environ, {"FORCE_COLOR": "TRUE"})
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
        mocked_url = "https://endoflife.date/api/androd.json"
        respx.get(mocked_url).respond(status_code=404)

        mocked_url = "https://endoflife.date/api/all.json"
        mocked_response = SAMPLE_RESPONSE_ALL_JSON
        respx.get(mocked_url).respond(content=mocked_response)

        # Act / Assert
        with pytest.raises(
            ValueError,
            match=r"Product 'androd' not found, run 'eol all' for list\. "
            r"Did you mean: 'android'?",
        ):
            norwegianblue.norwegianblue(product="androd")

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
