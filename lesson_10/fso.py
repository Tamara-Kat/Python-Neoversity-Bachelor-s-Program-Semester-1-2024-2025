from typing import Dict, List, Union, Set


def is_valid_file_system(fs: Dict) -> bool:
    """
    Перевіряє коректність структури файлової системи.
    Рекурсивно перевіряє кожен рівень на відповідність вимогам.
    """

    def is_valid_node(node: Dict, depth: int = 0) -> bool:
        # Перевіряємо, чи вузол є словником
        if not isinstance(node, dict):
            return False
        # Перевіряємо наявність ключа 'owner' та його тип
        if "owner" not in node or not isinstance(node["owner"], str):
            return False
        # Перевіряємо наявність ключа 'access' та його тип
        if "access" not in node or not isinstance(node["access"], list):
            return False

        # Перевіряємо чи всі права доступу є валідними
        valid_permissions = {"read", "write", "execute"}
        if not all(perm in valid_permissions for perm in node["access"]):
            return False

        # Якщо це файл (немає ключа 'contents')
        if "contents" not in node:
            return True

        # Перевіряємо обмеження на глибину для папок
        if depth >= 3:
            return False

        # Перевіряємо, чи 'contents' є словником
        if not isinstance(node["contents"], dict):
            return False

        # Рекурсивно перевіряємо кожен елемент вмісту
        return all(is_valid_node(item, depth + 1) for item in node["contents"].values())

    # Перевіряємо, чи файлову систему задано коректно
    if not fs or "root" not in fs:
        return False
    # Починаємо перевірку з кореневої папки
    return is_valid_node(fs["root"])


def change_owner(fs: Dict, path: str, new_owner: str) -> int:
    """
    Змінює власника для вказаного шляху та всіх вкладених елементів.
    Повертає статус операції.
    """

    def find_and_change(current: Dict, path_parts: List[str]) -> bool:
        # Якщо шлях закінчився, вважаємо успішним виконання
        if not path_parts:
            return True

        current_part = path_parts[0]  # Поточна частина шляху
        # Перевіряємо, чи є 'contents' і чи існує цільова частина шляху
        if "contents" not in current or current_part not in current["contents"]:
            return False

        if len(path_parts) == 1:  # Якщо це остання частина шляху
            target = current["contents"][current_part]  # Знаходимо цільовий елемент
            target["owner"] = new_owner  # Змінюємо власника

            # Якщо це папка, рекурсивно змінюємо власника для всіх вкладених елементів
            if "contents" in target:
                for item in target["contents"].values():
                    item["owner"] = new_owner
                    if "contents" in item:
                        for subitem in item["contents"].values():
                            subitem["owner"] = new_owner
            return True

        # Рекурсивно спускаємося по шляху
        return find_and_change(current["contents"][current_part], path_parts[1:])

    # Перевіряємо коректність файлової системи
    if not is_valid_file_system(fs):
        return 2  # Код 2: некоректна файлова система

    # Розбиваємо шлях на частини
    path_parts = path.split("/")
    if path_parts[0] != "root":  # Шлях має починатися з кореня
        return 1  # Код 1: шлях некоректний

    # Змінюємо власника
    return 0 if find_and_change(fs["root"], path_parts[1:]) else 1  # Код 0: успіх


def change_permissions(fs: Dict, path: str, mode: int, *permissions: str) -> int:
    """
    Змінює права доступу для вказаного шляху та всіх вкладених елементів.
    Повертає статус операції.
    """
    valid_permissions = {"read", "write", "execute"}  # Множина валідних прав доступу

    # Перевіряємо коректність режиму (додавання або видалення)
    if mode not in {1, -1}:
        return 3  # Код 3: некоректний режим
    # Перевіряємо, чи всі передані права доступу є валідними
    if not all(perm in valid_permissions for perm in permissions):
        return 4  # Код 4: некоректні права

    # Допоміжна функція для модифікації прав
    def modify_permissions(access_list: List[str], to_modify: Set[str]) -> List[str]:
        if mode == 1:  # Додавання прав
            return list(set(access_list) | to_modify)
        else:  # Видалення прав
            return [p for p in access_list if p not in to_modify]

    def find_and_change(current: Dict, path_parts: List[str]) -> bool:
        # Якщо шлях закінчився, вважаємо успішним виконання
        if not path_parts:
            return True

        current_part = path_parts[0]  # Поточна частина шляху
        # Перевіряємо, чи є 'contents' і чи існує цільова частина шляху
        if "contents" not in current or current_part not in current["contents"]:
            return False

        if len(path_parts) == 1:  # Якщо це остання частина шляху
            target = current["contents"][current_part]  # Знаходимо цільовий елемент
            # Змінюємо права доступу
            target["access"] = modify_permissions(target["access"], set(permissions))

            # Якщо це папка, рекурсивно змінюємо права для вмісту
            if "contents" in target:
                for item in target["contents"].values():
                    item["access"] = modify_permissions(
                        item["access"], set(permissions)
                    )
                    if "contents" in item:
                        for subitem in item["contents"].values():
                            subitem["access"] = modify_permissions(
                                subitem["access"], set(permissions)
                            )
            return True

        # Рекурсивно спускаємося по шляху
        return find_and_change(current["contents"][current_part], path_parts[1:])

    # Перевіряємо коректність файлової системи
    if not is_valid_file_system(fs):
        return 2  # Код 2: некоректна файлова система

    # Розбиваємо шлях на частини
    path_parts = path.split("/")
    if path_parts[0] != "root":  # Шлях має починатися з кореня
        return 1  # Код 1: шлях некоректний

    # Змінюємо права доступу
    return 0 if find_and_change(fs["root"], path_parts[1:]) else 1  # Код 0: успіх


# Приклад файлової системи
file_system = {
    "root": {  # Коренева папка
        "owner": "admin",
        "access": ["read", "write", "execute"],
        "contents": {
            "folder1": {  # Папка
                "owner": "admin",
                "access": ["read", "write"],
                "contents": {
                    "subfolder1": {  # Підпапка
                        "owner": "user1",
                        "access": ["read", "write"],
                        "contents": {
                            "file1.txt": {  # Файл
                                "owner": "user1",
                                "access": ["read", "write"],
                            }
                        },
                    }
                },
            },
            "file0.txt": {"owner": "user1", "access": ["read", "write"]},  # Файл
        },
    }
}

print(is_valid_file_system(file_system))
print(is_valid_file_system({}))
# Перевірка прав доступу
print(
    file_system["root"]["contents"]["folder1"]["contents"]["subfolder1"]["contents"][
        "file1.txt"
    ]["access"]
)
# Додаємо право виконання
r = change_permissions(file_system, "root/folder1/subfolder1/file1.txt", 1, "execute")
print(r)
print(
    file_system["root"]["contents"]["folder1"]["contents"]["subfolder1"]["contents"][
        "file1.txt"
    ]["access"]
)
# Тест з некоректним режимом
r = change_permissions(file_system, "root/folder1/subfolder1/file1.txt", 3, "execute")
print(r)

r = change_owner(
    file_system, "root/folder1", "new_admin"
)  # Статуси 0, 1, 2 відповідно для успішного, некоректного шляху та некоректної файлової системи
print(r)
print(file_system["root"]["contents"]["folder1"]["owner"])
