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
    assert (
        result.stderr == "10 rows in museums\n10 rows in cities\n10 rows in countries\n"
    )
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
