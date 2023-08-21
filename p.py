from collections import deque

stack = deque()
stack.append(1)
stack.append(5)
stack.append(4)
stack.append(3)
stack.append(2)
print(stack[-2])
print(stack)