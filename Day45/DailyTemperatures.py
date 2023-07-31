from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]):
        stack = deque()
        l=r=0
        res=[0 for x in range(len(temperatures))]
        while r<len(temperatures):
            while stack and temperatures[stack[-1]]<temperatures[r]:
                res[stack[-1]] = r-stack[-1]
                stack.pop()
            stack.append(r)
            r+=1
        while stack:
            res[stack.pop()] = 0
        return res


        
        