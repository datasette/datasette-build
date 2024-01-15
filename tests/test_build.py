from datasette_build.cli import cli
from click.testing import CliRunner
import pathlib
import pytest
import sqlite_utils

DEMO_DIR = pathlib.Path(__file__).parent / "demo"


@pytest.fixture(scope="session")
def demo_db(tmp_path_factory):
    tmpdir = tmp_path_factory.mktemp("built")
    db_path = str(tmpdir / "demo.db")
    runner = CliRunner(mix_stderr=False)
    result = runner.invoke(
        cli, [str(tmpdir / "demo.db"), str(DEMO_DIR)], catch_exceptions=False
    )
    assert result.exit_code == 0
    expected_lines = [
        "10 rows in museums",
        "10 rows in cities",
        "10 rows in countries",
    ]
    for line in expected_lines:
        assert line in result.stderr
    return sqlite_utils.Database(db_path)


def test_demo_db_tables(demo_db):
    assert set(demo_db.table_names()) == {"cities", "countries", "museums"}


def test_demo_db_tsv(demo_db):
    assert demo_db["countries"].count == 10
    assert demo_db["countries"].columns_dict == {
        "id": str,
        "name": str,
        "population": int,
    }
    # Spot check
    assert next(demo_db["countries"].rows_where("id = 'US'")) == {
        "id": "US",
        "name": "United States",
        "population": 331002651,
    }
    assert next(demo_db["countries"].rows_where("id = 'EG'")) == {
        "id": "EG",
        "name": "Egypt",
        "population": 102334404,
    }


def test_demo_db_csv(demo_db):
    cities = demo_db["cities"]
    assert cities.count == 10
    assert cities.columns_dict == {
        "id": str,
        "name": str,
        "latitude": float,
        "longitude": float,
        "country": str,
    }
    # Spot check
    assert next(cities.rows_where("id = 'nyc'")) == {
        "id": "nyc",
        "name": "New York City",
        "latitude": 40.7128,
        "longitude": -74.006,
        "country": "US",
    }
    assert next(cities.rows_where("id = 'syd'")) == {
        "id": "syd",
        "name": "Sydney",
        "latitude": -33.8688,
        "longitude": 151.2093,
        "country": "AU",
    }


def test_demo_db_json(demo_db):
    museums = demo_db["museums"]
    assert museums.count == 10
    assert museums.columns_dict == {
        "id": int,
        "name": str,
        "city_id": str,
    }
    # Spot check
    assert next(museums.rows_where("id = 1")) == {
        "id": 1,
        "name": "Metropolitan Museum of Art",
        "city_id": "nyc",
    }
    assert next(museums.rows_where("id = 10")) == {
        "id": 10,
        "name": "Chhatrapati Shivaji Maharaj Vastu Sangrahalaya",
        "city_id": "mum",
    }
