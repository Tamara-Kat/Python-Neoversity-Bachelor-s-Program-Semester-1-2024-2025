from collections import deque
MAX_LEN_QUEUE = 5

fifo = deque(maxlen=MAX_LEN_QUEUE)

fifo.append("Maksym")
fifo.append("Marta")
fifo.append("Hikita")
fifo.append("Ostap")

print(fifo)
name = fifo.popleft()
print(name)