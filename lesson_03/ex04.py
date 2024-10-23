number = int(input("Введіть чотирьох значне число: "))  # 2345 -> (2 + 3 + 4+ 5) / 4

# 2345 % 10 = 5

n4 = number % 10
print(n4)

n3 = number // 10 % 10  # 2345 // 10 -> 234 % 10 -> 4
print(n3)

n2 = number // 100 % 10
n1 = number // 1000

avg = (n1 + n2 + n3 + n4) / 4
print(f"Average: {avg}")
