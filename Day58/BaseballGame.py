from collections import deque
class Solution:
    def calPoints(self, operations: [str]) -> int:
        stack = deque()
        hasset = ("D", "C", "+")
        for x in operations:
            if x in hasset:
                if x=="C":
                    stack.pop()
                elif x=="D":
                    a = stack[-1]
                    stack.append(a*2)
                elif x=="+":
                    a = stack[-1]
                    b=stack[-2]
                
                    stack.append(a+b)
            else:
                stack.append(int(x))
        res = 0        
        for y in stack:
            res+=y
        return res

        