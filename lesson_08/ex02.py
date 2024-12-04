try:
    file = open("test.txt", "w", encoding="utf-8")
    file.write("Hello, world!\n")
    file.write("Hello Python\n")
    file.write("Женя хоче оператор with\n")
except OSError:
    print("Помилка доступу до файлу")
finally:
    file.close()


file = open("test.txt", "r", encoding="utf-8")
# file.read() - all

# for line in file:
#     print(line) - line by line

result = [line.strip() for line in file.readlines()]  # remove '\n'
print(result)  # ['Hello, world!', 'Hello Python', 'Женя хоче оператор with']
file.close()
