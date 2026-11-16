from pathlib import Path

import pandas as pd


def load_dataset(file_path):
    """Загружает CSV и проверяет размер таблицы."""
    path = Path(file_path)

    if path.suffix.lower() != ".csv":
        raise ValueError("Выбери файл с расширением .csv")

    if path.stat().st_size > 5 * 1024 * 1024:
        raise ValueError("Размер файла превышает 5 МБ")

    dataframe = pd.read_csv(
        path,
        encoding="utf-8-sig",
        nrows=50001,
    )

    if dataframe.empty:
        raise ValueError("В таблице нет строк с данными")

    if len(dataframe) > 50000:
        raise ValueError("В таблице больше 50 000 строк")

    return dataframe


def inspect_dataset(dataframe):
    """Возвращает описание таблицы."""
    return {
        "row_count": len(dataframe),
        "column_count": len(dataframe.columns),
        "columns": dataframe.columns.tolist(),
        "data_types": {
            column: str(dtype)
            for column, dtype in dataframe.dtypes.items()
        },
        "missing_values": {
            column: int(count)
            for column, count in dataframe.isna().sum().items()
        },
    }
def calculate_statistics(dataframe, column):
    """Рассчитывает статистики числового столбца."""
    if column not in dataframe.columns:
        raise ValueError(f"Столбец '{column}' не найден")

    values = dataframe[column]

    if not pd.api.types.is_numeric_dtype(values):
        raise ValueError(f"Столбец '{column}' должен быть числовым")

    valid_values = values.dropna()

    if valid_values.empty:
        raise ValueError(f"В столбце '{column}' нет числовых значений")

    return {
        "column": column,
        "count": int(valid_values.count()),
        "missing": int(values.isna().sum()),
        "mean": float(valid_values.mean()),
        "median": float(valid_values.median()),
        "min": float(valid_values.min()),
        "max": float(valid_values.max()),
        "sum": float(valid_values.sum()),
    }

def main():
    file_path = (
        Path(__file__).resolve().parent
        / "data"
        / "test_sales.csv"
    )

    try:
        dataframe = load_dataset(file_path)
        information = inspect_dataset(dataframe)

        print("Таблица:")
        print(dataframe.to_string(index=False))

        print("\nКоличество строк:", information["row_count"])
        print("Количество столбцов:", information["column_count"])
        print("Столбцы:", information["columns"])
        print("Типы данных:", information["data_types"])
        print("Пропуски:", information["missing_values"])
        statistics = calculate_statistics(dataframe, "sales")

        print("\nСтатистика продаж:")
        for name, value in statistics.items():
            print(f"{name}: {value}")
    except (OSError, ValueError, pd.errors.ParserError) as error:
        print("Ошибка загрузки:", error)


if __name__ == "__main__":
    main()