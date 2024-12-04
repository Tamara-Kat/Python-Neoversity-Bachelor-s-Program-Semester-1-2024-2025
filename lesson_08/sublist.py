data = [1, 2, 3]  # Початковий список

sublists = [[]]
for length in range(1, len(data) + 1):
    for i in range(0, len(data) - length + 1):
        sublists.append(data[i : i + length])

print(sublists)
