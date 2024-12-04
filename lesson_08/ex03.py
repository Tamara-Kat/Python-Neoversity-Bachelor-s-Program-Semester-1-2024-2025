try:
    with open("test.txt", "w", encoding="utf-8") as file:
        file.write("Hello, world!\n")
        file.write("Hello Python\n")
        file.write("Женя хоче оператор with\n")
        file.write("Hello, world!\n")
except OSError:
    print("Помилка доступу до файлу")


with open("test.txt", "r", encoding="utf-8") as file:
    # file.read() - all

    # for line in file:
    #     print(line) - line by line

    result = [line.strip() for line in file.readlines()]  # remove '\n'
    print(result)  # ['Hello, world!', 'Hello Python', 'Женя хоче оператор with']
