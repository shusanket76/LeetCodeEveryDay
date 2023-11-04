from collections import deque

a = deque()
a.appendleft(12)
a.appendleft(122)
a.appendleft(1222)
a.pop()
print(a)