from decimal import Decimal, getcontext, ROUND_HALF_UP, ROUND_HALF_EVEN


getcontext().prec = 10

print(0.1 + 0.2)

print(Decimal('0.1') + Decimal('0.2'))

print(Decimal('0.1') + Decimal('0.2') == Decimal('0.3'))
print(type(Decimal('0.3')))
print(type(0.3))

# 0 = equal
# 1 = greater
# -1 = less
#
print((Decimal('0.1') + Decimal('0.2')).compare(Decimal('0.3')))  

pi = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
num = Decimal(pi)

print(num.quantize(Decimal('1.000000'), rounding=ROUND_HALF_EVEN))


