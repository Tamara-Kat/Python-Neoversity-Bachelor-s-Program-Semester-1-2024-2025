a_b = "1/3"
c_b = "5/3"

a, b = a_b.split("/")
c, b = c_b.split("/")

top_sum = int(a) + int(c)

print(f"{a_b} + {c_b} = {top_sum}/{b}")
