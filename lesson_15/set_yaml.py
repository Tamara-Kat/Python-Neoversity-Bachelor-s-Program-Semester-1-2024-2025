import yaml

students = [
  {"name": "Oleksandr", "age": 21, "gender": "male"},
  {"name": "Volodymyr", "age": 22, "gender": "male"},
  {"name": "Denys", "age": 23, "gender": "male"},
  {"name": "Тамара", "age": 16, "gender": "female"},
]

# serialized = yaml.dump(students)
# print(serialized)
# result = yaml.load(serialized, Loader=yaml.FullLoader)
# print(result)

with open("students.yaml", "w", encoding="utf-8") as f:
  yaml.dump({"students":students}, f, allow_unicode=True)

with open("students.yaml", "r", encoding="utf-8") as f:
  result = yaml.load(f, Loader=yaml.FullLoader)
  print(result.get("students"))
