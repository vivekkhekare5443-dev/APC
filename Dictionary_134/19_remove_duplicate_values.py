data = {"a": 10, "b": 20, "c": 10, "d": 30, "e": 20}
result = {}
seen = set()
for key, value in data.items():
    if value not in seen:
        result[key] = value
        seen.add(value)
print(result)
