import pandas as pd
import pytest

from csv_tools import (
    load_dataset,
    inspect_dataset,
    calculate_statistics,
)


def test_load_valid_csv(tmp_path):
    path = tmp_path / "sales.csv"
    path.write_text(
        "month,sales\nJanuary,100\nFebruary,200\n",
        encoding="utf-8",
    )

    dataframe = load_dataset(path)

    assert dataframe.shape == (2, 2)
    assert dataframe["sales"].tolist() == [100, 200]


def test_inspect_missing_values():
    dataframe = pd.DataFrame({
        "sales": [100, None, 300],
        "customers": [10, 20, 30],
    })

    result = inspect_dataset(dataframe)

    assert result["row_count"] == 3
    assert result["column_count"] == 2
    assert result["missing_values"] == {
        "sales": 1,
        "customers": 0,
    }


def test_statistics_ignore_missing_values():
    dataframe = pd.DataFrame({
        "sales": [100, 200, 300, None],
    })

    result = calculate_statistics(dataframe, "sales")

    assert result == {
        "column": "sales",
        "count": 3,
        "missing": 1,
        "mean": 200.0,
        "median": 200.0,
        "min": 100.0,
        "max": 300.0,
        "sum": 600.0,
    }


def test_unknown_column():
    dataframe = pd.DataFrame({"sales": [100, 200]})

    with pytest.raises(ValueError, match="не найден"):
        calculate_statistics(dataframe, "profit")


def test_text_column():
    dataframe = pd.DataFrame({"month": ["January", "February"]})

    with pytest.raises(ValueError, match="числовым"):
        calculate_statistics(dataframe, "month")


def test_all_missing_column():
    dataframe = pd.DataFrame({
        "sales": pd.Series([None, None], dtype="float64"),
    })

    with pytest.raises(ValueError, match="нет числовых"):
        calculate_statistics(dataframe, "sales")


def test_empty_csv(tmp_path):
    path = tmp_path / "empty.csv"
    path.write_text("", encoding="utf-8")

    with pytest.raises(pd.errors.EmptyDataError):
        load_dataset(path)


def test_header_only_csv(tmp_path):
    path = tmp_path / "header.csv"
    path.write_text("month,sales\n", encoding="utf-8")

    with pytest.raises(ValueError, match="нет строк"):
        load_dataset(path)