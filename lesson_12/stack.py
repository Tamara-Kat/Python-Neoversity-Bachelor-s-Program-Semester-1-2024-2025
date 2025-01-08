def create_stack():
  stack = []
  return stack

def is_empty(stack):
  return len(stack) == 0

def push(stack, item):
  stack.append(item)
  print(item + " pushed to stack")

def pop(stack):
  if (is_empty(stack)):
    return "stack is empty"
  return stack.pop()

def peek(stack):
  if (is_empty(stack)):
    return "stack is empty"
  return stack[-1]


stack = create_stack()
push(stack, "a")
push(stack, "b")
push(stack, "c")

print(peek(stack))

print(pop(stack))
print(pop(stack))
print(pop(stack))
print(pop(stack))

print(peek(stack))