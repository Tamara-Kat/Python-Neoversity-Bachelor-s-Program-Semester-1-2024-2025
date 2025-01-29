import json

test = [{"test": 1}, {"test": 2}, {"тест": 3}]
serialized = json.dumps(test, ensure_ascii=False)

print(type(serialized))

parse = json.loads(serialized)
print(type(parse))

with open("test.json", "w", encoding="utf-8") as f:
  json.dump(test, f, ensure_ascii=False)

