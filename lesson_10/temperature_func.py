from numbers import Number
from typing import Dict, Union, List, Any
from functools import reduce
from copy import deepcopy

RawDataRecord = Dict[Any, Union[Number, str, None]]
FilteredDataRecord = Dict[Any, Union[Number, str]]


def convert_value(item: FilteredDataRecord) -> FilteredDataRecord:

    try:
        new_item = deepcopy(item)

        # Конвертуємо ключ
        if isinstance(new_item["key"], str):
            new_item["key"] = int(new_item["key"])

        # Конвертуємо значення
        if isinstance(new_item["value"], str):
            new_item["value"] = float(str(new_item["value"]).lstrip("+"))

        return new_item
    except (ValueError, TypeError):
        return None


def is_valid_record(item: RawDataRecord) -> bool:
    return item["timestamp"] is not None and item["metric"] == "temp"


def calculate_average(acc: tuple, item: FilteredDataRecord) -> tuple:
    total, count = acc
    return (total + item["value"], count + 1)


def temp_map(mapped_data: List[FilteredDataRecord]) -> List[FilteredDataRecord]:
    return list(filter(None, map(convert_value, mapped_data)))


def temp_filter(raw_data: List[RawDataRecord]) -> List[FilteredDataRecord]:
    return list(filter(is_valid_record, raw_data))


def temp_reduce(mapped_data: List[FilteredDataRecord], default: Number) -> Number:
    if not mapped_data:
        return default

    total, count = reduce(calculate_average, mapped_data, (0, 0))
    return total / count


def validate_and_calculate(
    raw_data: List[RawDataRecord], default: Number = 0
) -> Number:
    """Робить набір даних консистентним та обчислює середню температуру."""
    return temp_reduce(temp_map(temp_filter(raw_data)), default)


raw_data = [
    {"key": 1, "timestamp": 1234567, "metric": "temp", "value": "+12"},
    {"key": 2, "timestamp": None, "metric": "temp", "value": "+10"},
    {"key": 3, "timestamp": 1234569, "metric": "temp", "value": 11},
    {"key": "4", "timestamp": 1234570, "metric": "", "value": "88"},
]

r = validate_and_calculate(raw_data)

print(r)

print(temp_filter(raw_data))

print(temp_map(temp_filter(raw_data)))