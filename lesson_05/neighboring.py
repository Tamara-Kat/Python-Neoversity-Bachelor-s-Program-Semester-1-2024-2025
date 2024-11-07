"""
 
Напишіть функцію, яка приймає рядки і підраховує кількість символів, що йдуть підряд. Поверніть найдовшу послідовність символів, що йдуть підряд, і кількість разів, коли цей символ зустрічається.
Результатом має бути кортеж, першим елементом якого є символ, а за ним - кількість його зустрічей у рядку.

For example:

>>> longest_neighboring(“daadbbcccdd”)
(“c”, 3)

Explanation:
 
Символ 'a' зустрічається не більше двох разів підряд. Символ 'b' зустрічається не більше двох разів підряд. Символ 'c' зустрічається не більше трьох разів підряд. Символ 'd' зустрічається не більше двох разів підряд. Оскільки потрібно повернути найдовший набір символів, що йдуть підряд, то відповіддю буде 3.


For example:

>>> longest_neighboring(“daadbcd”)
(“a”, 2)
"""


def longest_neighboring(string):
    if not string:
        return ("", 0)

    max_char = string[0]
    max_count = 1

    current_char = string[0]
    current_count = 1

    for i in range(1, len(string)):
        if string[i] == current_char:
            current_count += 1
        else:
            if current_count > max_count:
                max_char = current_char
                max_count = current_count
            current_char = string[i]
            current_count = 1

    if current_count > max_count:
        max_char = current_char
        max_count = current_count

    return (max_char, max_count)


result = longest_neighboring("daadbbcccdd")
print(result)
result = longest_neighboring("daadbcd")
print(result)
