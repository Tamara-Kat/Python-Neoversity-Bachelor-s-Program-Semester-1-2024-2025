"""
r - read
w - write
a - append
b - binary
+ - update
"""

file = open("sublist.py", "r", encoding="utf-8")
text = file.read()
print(text)
file.close()
