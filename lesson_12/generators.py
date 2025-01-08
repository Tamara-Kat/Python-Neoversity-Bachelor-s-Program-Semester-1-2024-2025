def simple_generator():
    yield 1
    yield 2


g = simple_generator()
# print(next(g))
# print(next(g))
# print(next(g))

for i in g:
    print(i)

for num in range(5):
    print(num, end=" ")


def my_range(limit):
    value = 0
    while value < limit:
        yield value
        value += 1


print()

for num in my_range(5):
    print(num, end=" ")

print()
gen = my_range(5)
while True:
    try:
        print(next(gen))
    except StopIteration:
        break

sq_gen = (i**2 for i in range(10))
data = list(sq_gen)
print(data)
print(data)
