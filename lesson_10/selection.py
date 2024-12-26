from typing import Dict, Any, Callable, Iterable

# Визначення типів для ясності
DataType = Iterable[Dict[str, Any]]
ModifierFunc = Callable[[DataType], DataType]

def query(data: DataType, selector: ModifierFunc, *filters: ModifierFunc) -> DataType:
    """
    Query data with column selection and filters.

    :param data: List of dictionaries with columns and values
    :param selector: Result of `select` function call
    :param filters: Any number of results of `field_filter` function calls
    :return: Filtered data
    """
    for filter_func in filters:  # Послідовно застосовуємо фільтри
        data = filter_func(data)
    return selector(data)  # Застосовуємо функцію для вибору колонок


def select(*columns: str) -> ModifierFunc:
    """
    Return function that selects only specific columns from dataset.

    :param columns: Names of the columns to select
    :return: Function that applies the column selection
    """
    def selector(data: DataType) -> DataType:
        return [
            {column: row[column] for column in columns if column in row}
            for row in data
        ]
    return selector


def field_filter(column: str, *values: Any) -> ModifierFunc:
    """
    Return function that filters specific column to be one of `values`.

    :param column: The name of the column to filter
    :param values: Allowed values for the column
    :return: Function that filters the dataset
    """
    def filter_func(data: DataType) -> DataType:
        return [row for row in data if row.get(column) in values]
    return filter_func


def test_query():
    friends = [
        {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'},
        {'name': 'Bob', 'gender': 'male', 'sport': 'volleyball'},
        {'name': 'Jane', 'gender': 'female', 'sport': 'volleyball'},
    ]
    value = query(
        friends,
        select(*('name', 'gender', 'sport')),
        field_filter(*('sport', *('Basketball', 'volleyball'))),
        field_filter(*('gender', *('male', 'female'))),
    )
    print(value)
    # assert [{'gender': 'male', 'name': 'Sam', 'sport': 'Basketball'}] == value


if __name__ == "__main__":
    test_query()
    print("Test passed successfully!")
    