from collections import deque

stack = deque(maxlen=3)

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

print(stack)
print(stack[-1])

print(stack.pop())
print(stack.pop())

stack = deque()

stack.appendleft(1)
stack.appendleft(2)
stack.appendleft(3)

print(stack)
print(stack[0])

print(stack.popleft())
print(stack.popleft())