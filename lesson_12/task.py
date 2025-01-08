from collections import deque

tasks = [
    {"type": "fast", "title": "Помити посуд"},
    {"type": "slow", "title": "Пограти в КС"},
    {"type": "fast", "title": "Вигуляти собаку"},
    {"type": "slow", "title": "Подивитись серіал"},
]

work_queue = deque()

for task in tasks:
    if task["type"] == "fast":
        work_queue.appendleft(task)
        print(f"Added {task['title']} to the front of the queue")
    else:
        work_queue.append(task)
        print(f"Added {task['title']} to the back of the queue")


while work_queue:
    task = work_queue.popleft()
    print(f"Working on {task['title']}")
