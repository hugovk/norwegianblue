"""
Unit tests for norwegianblue cache
"""
from __future__ import annotations

import tempfile
from pathlib import Path

from freezegun import freeze_time

from norwegianblue import _cache


class TestNorwegianBlueCache:
    def setup_method(self) -> None:
        # Choose a new cache dir that doesn't exist
        self.original_cache_dir = _cache.CACHE_DIR
        self.temp_dir = tempfile.TemporaryDirectory()
        _cache.CACHE_DIR = Path(self.temp_dir.name) / "norwegianblue"

    def teardown_method(self) -> None:
        # Reset original
        _cache.CACHE_DIR = self.original_cache_dir

    @freeze_time("2018-12-26")
    def test_cache_filename(self) -> None:
        # Arrange
        url = "https://endoflife.date/api/python.json"

        # Act
        out = _cache.filename(url)

        # Assert
        assert str(out).endswith("2018-12-26-https-endoflife-date-api-python-json.json")

    def test_load_cache_not_exist(self) -> None:
        # Arrange
        filename = Path("file-does-not-exist")

        # Act
        data = _cache.load(filename)

        # Assert
        assert data == {}

    def test_load_cache_bad_data(self) -> None:
        # Arrange
        with tempfile.NamedTemporaryFile(delete=False) as f:
            f.write(b"Invalid JSON!")

        # Act
        data = _cache.load(Path(f.name))

        # Assert
        assert data == {}

    def test_cache_round_trip(self) -> None:
        # Arrange
        filename = _cache.CACHE_DIR / "test_cache_round_trip.json"
        data = "test data"

        # Act
        _cache.save(filename, data)
        new_data = _cache.load(filename)

        # Tidy up
        filename.unlink()

        # Assert
        assert new_data == data

    @freeze_time("2021-10-25")
    def test_cache_clear_all(self) -> None:
        # Arrange
        # Create old cache file
        cache_file_old = _cache.CACHE_DIR / "2021-10-24-old-cache-file.json"
        cache_file_new = _cache.CACHE_DIR / "2021-10-25-new-cache-file.json"
        _cache.save(cache_file_old, data={})
        _cache.save(cache_file_new, data={})
        assert cache_file_new.exists()
        assert cache_file_old.exists()

        # Act
        _cache.clear(clear_all=True)

        # Assert
        assert not cache_file_old.exists()
        assert not cache_file_new.exists()

    @freeze_time("2021-10-25")
    def test_cache_clear(self) -> None:
        # Arrange
        # Create old cache file
        cache_file_old = _cache.CACHE_DIR / "2021-10-24-old-cache-file.json"
        cache_file_new = _cache.CACHE_DIR / "2021-10-25-new-cache-file.json"
        _cache.save(cache_file_old, data={})
        _cache.save(cache_file_new, data={})
        assert cache_file_new.exists()
        assert cache_file_old.exists()

        # Act
        _cache.clear()

        # Assert
        assert not cache_file_old.exists()
        assert cache_file_new.exists()
