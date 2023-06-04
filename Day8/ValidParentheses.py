# link = "https://leetcode.com/problems/valid-parentheses/"
from collections import deque
def isValid(self, s):
        stack = deque()
        hasmap={"]":"[","}":"{",")":"("}
        for x in s:
            if x not in hasmap:
                stack.append(x)
            else:
                if stack:
                    a = stack.pop()
                    if hasmap[x]!=a:
                        return False
                else:
                    return False
        return len(stack)==0