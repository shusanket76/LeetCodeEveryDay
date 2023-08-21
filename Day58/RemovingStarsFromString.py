from collections import deque
class Solution:
    def removeStars(self, s: str) -> str:
        stack = deque()
        for x in s:
            if x=="*":
                stack.pop()
            else:
                stack.append(x)
        s = ""
        for a in stack:
            s+=a
        return s