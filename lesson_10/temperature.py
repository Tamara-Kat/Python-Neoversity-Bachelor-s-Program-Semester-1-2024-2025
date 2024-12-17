from numbers import Number  
from typing import Dict, Union, List, Any
from copy import deepcopy

# Типи даних для вхідних і відфільтрованих записів
RawDataRecord = Dict[Any, Union[Number, str, None]]  # Словник, що містить будь-які ключі і значення типу Number, str або None
FilteredDataRecord = Dict[Any, Union[Number, str]]  # Словник, що містить будь-які ключі і значення типу Number або str


def temp_map(mapped_data: List[FilteredDataRecord]) -> List[FilteredDataRecord]:
    """ Перетворення всіх значень у відповідний тип """
    new_mapped_data = []  # Створюємо список для результатів
    
    for item in mapped_data:  # Ітеруємося по кожному запису у вхідних даних
        try:
            # Створюємо копію словника для роботи
            new_item = deepcopy(item)
            
            # Якщо ключ є рядком, перетворюємо його на ціле число
            if isinstance(new_item['key'], str):
                new_item['key'] = int(new_item['key'])
            
            # Перетворюємо значення температури
            if isinstance(new_item["value"], str):
                new_item["value"] = float(str(new_item["value"]).lstrip("+"))
            
            # Додаємо оброблений запис до списку результатів
            new_mapped_data.append(new_item)
        
        except (ValueError, TypeError):  # Ігноруємо записи, якщо трапляються помилки перетворення
            continue
    
    return new_mapped_data  # Повертаємо оброблені дані


def temp_filter(raw_data: List[RawDataRecord]) -> List[FilteredDataRecord]:
    """ Відфільтровуємо записи з відсутніми або некоректними полями """
    filtered_data = []  # Список для збереження відфільтрованих даних
    
    for item in raw_data:  # Ітеруємося по кожному запису у вхідних даних
        # Перевіряємо, чи існує часовий штамп і чи метрика є 'temp'
        if item['timestamp'] is not None and item['metric'] == 'temp':
            filtered_data.append(item)  # Додаємо запис до списку, якщо умови виконані
    
    return filtered_data  # Повертаємо відфільтровані дані


def temp_reduce(mapped_data: List[FilteredDataRecord], default: Number) -> Number:
    """ Обчислення середньої температури """
    if not mapped_data:  # Якщо список порожній, повертаємо значення за замовчуванням
        return default
    
    # Підсумовуємо всі значення температури
    total = sum(item['value'] for item in mapped_data)
    
    # Повертаємо середнє значення
    return total / len(mapped_data)


def validate_and_calculate(raw_data, default: Number = 0):
    """ 
    Нормалізуємо набір даних: перетворюємо всі значення у відповідний тип, 
    видаляємо записи з некоректними значеннями та обчислюємо середню температуру.
    """
    # Відфільтровуємо, перетворюємо та обчислюємо середнє значення
    return temp_reduce(temp_map(temp_filter(raw_data)), default)


# Вхідні дані для прикладу
raw_data = [
    {"key": 1, "timestamp": 1234567, "metric": "temp", "value": "+12"},  # Коректний запис
    {"key": 2, "timestamp": None, "metric": "temp", "value": "+10"},  # Відсутній timestamp, запис буде видалено
    {"key": 3, "timestamp": 1234569, "metric": "temp", "value": 11},  # Коректний запис
    {"key": "4", "timestamp": 1234570, "metric": "", "value": "88"},  # Некоректна метрика, запис буде видалено
]

# Виконуємо валідацію та обчислення середньої температури
r = validate_and_calculate(raw_data)

# Виводимо результат
print(r)  # Вивід: середнє значення температури серед коректних записів
