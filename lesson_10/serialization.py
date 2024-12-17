from typing import Any 

# Функція для серіалізації Python-об'єктів у кастомний текстовий формат
def marshal(obj):
    if isinstance(obj, bool):  # Якщо об'єкт булевий
        return f"b:{'true' if obj else 'false'}"  # Повертаємо 'b:true' або 'b:false'
    elif isinstance(obj, int):  # Якщо об'єкт ціле число
        return f"i:{obj}"  # Повертаємо 'i:<число>'
    elif isinstance(obj, str):  # Якщо об'єкт рядок
        return f"s:{obj}"  # Повертаємо 's:<рядок>'
    elif isinstance(obj, list):  # Якщо об'єкт список
        return f"l:[{','.join(marshal(item) for item in obj)}]"  # Рекурсивно серіалізуємо елементи списку
    elif isinstance(obj, tuple):  # Якщо об'єкт кортеж
        return f"t:({','.join(marshal(item) for item in obj)})"  # Рекурсивно серіалізуємо елементи кортежу
    elif isinstance(obj, dict):  # Якщо об'єкт словник
        # Серіалізуємо пари ключ-значення, викликаючи marshal для кожного
        items = ",".join(f"{marshal(key)}:{marshal(value)}" for key, value in obj.items())
        return f"d:{{{items}}}"  # Обгортаємо результати у 'd:{...}'
    else:
        raise ValueError(f"Unsupported type: {type(obj)}")  # Викликаємо помилку, якщо тип не підтримується

# Функція для десеріалізації кастомного текстового формату у Python-об'єкт
def unmarshal(serialized_obj: str) -> Any:
    # Вкладена функція для розбору контейнерів (списків, кортежів, словників)
    def parse_container(data: str) -> tuple[list, str]:
        result = []  # Список для збереження елементів
        current = ""  # Поточний оброблюваний елемент
        nesting = 0  # Лічильник рівнів вкладеності
        
        for char in data[1:]:  # Ітеруємося по символах, пропускаючи перший (start_char)
            if char in '{[(':  # Якщо відкриваючий символ контейнера
                nesting += 1  # Збільшуємо рівень вкладеності
                current += char  # Додаємо символ до поточного елемента
            elif char in '}])':  # Якщо закриваючий символ контейнера
                if nesting == 0:  # Якщо це вихід із поточного контейнера
                    if current:  # Додаємо останній елемент, якщо є
                        result.append(current)
                    return result  # Повертаємо список 
                nesting -= 1  # Зменшуємо рівень вкладеності
                current += char  # Додаємо символ до поточного елемента
            elif char == ',' and nesting == 0:  # Якщо це роздільник на верхньому рівні
                if current:  # Додаємо поточний елемент до результату
                    result.append(current)
                current = ""  # Очищаємо поточний елемент
            else:  # Всі інші символи додаємо до поточного елемента
                current += char
                
        raise ValueError("Неправильний формат даних")  # Помилка, якщо не знайдено закриваючого символу

    type_prefix = serialized_obj[0]  # Отримуємо префікс типу (перший символ)
    data = serialized_obj[2:]  # Видаляємо префікс і двокрапку

    if type_prefix == 'i':  # Якщо ціле число
        return int(data)  # Повертаємо int
    elif type_prefix == 'b':  # Якщо булеве значення
        return data.lower() == 'true'  # Повертаємо True або False
    elif type_prefix == 's':  # Якщо рядок
        return data  # Повертаємо рядок
    elif type_prefix == 'l':  # Якщо список
        items = parse_container(data)  # Парсимо список
        return [unmarshal(item) for item in items]  # Рекурсивно десеріалізуємо елементи
    elif type_prefix == 't':  # Якщо кортеж
        items = parse_container(data)  # Парсимо кортеж
        return tuple(unmarshal(item) for item in items)  # Рекурсивно десеріалізуємо елементи
    elif type_prefix == 'd':  # Якщо словник
        items = parse_container(data)  # Парсимо словник
        dict_result = {}  # Порожній словник для результату
        for item in items:  # Ітеруємося по кожній парі ключ-значення
            # Знаходимо індекс першої і другої двокрапки
            type_end = item.index(':') + 1  # Кінець префіксу ключа
            next_colon = item.index(':', type_end)  # Індекс двокрапки між ключем і значенням
            
            # Розділяємо рядок на ключ і значення
            key = item[:next_colon]  # Частина до двокрапки — ключ
            value = item[next_colon + 1:]  # Частина після двокрапки — значення
            
            dict_result[unmarshal(key)] = unmarshal(value)  # Десеріалізуємо ключ і значення, додаємо до словника
        return dict_result  # Повертаємо словник
        
    raise ValueError(f"Невідомий тип: {type_prefix}")  # Помилка для невідомих типів

# Приклад використання
data = {"key": "value", "number": 123, "test": [1, 2, 3, [4, 5]]}
serialized = marshal(data)  # Серіалізуємо словник
print(serialized)  # Вивід: d:{s:key:s:value,s:number:i:123}
deserialized = unmarshal(serialized)  # Десеріалізуємо назад у словник
print(deserialized)  # Вивід: {'key': 'value', 'number': 123}
