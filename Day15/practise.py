from collections import deque

queue = deque()
queue.append(12)
queue.append(14)
queue.append(11)
print(queue)
queue.popleft()
print(queue)