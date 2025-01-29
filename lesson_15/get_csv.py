import csv

with open("students.csv", "r", encoding="utf-8") as f:
  reader = csv.DictReader(f)
  for row in reader:
    print(row)