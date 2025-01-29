import csv

with open("students.csv", "w", encoding="utf-8", newline="") as f:
    column_names = ["name", "age", "gender", "married"]
    writer = csv.DictWriter(f, fieldnames=column_names)
    # writer.writeheader()
    writer.writerow({"name": "Oleksandr", "age": 21, "gender": "male", "married": True})
    writer.writerow(
        {"name": "Volodymyr", "age": 22, "gender": "male", "married": False}
    )
    writer.writerow({"name": "Denys", "age": 23, "gender": "male", "married": False})
    writer.writerow({"name": "Тамара", "age": 16, "gender": "female", "married": False})
