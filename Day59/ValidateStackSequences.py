from collections import deque

class Solution:
    def validateStackSequences(self, pushed: [int], popped:[int]) -> bool:
        stack = deque()
        r=0
        newarr = []
        for x in pushed:
            stack.append(x)
            if x==popped[r]:
                while len(stack)!=0 and  stack[-1]==popped[r]:
                    newarr.append(stack.pop())
                    r+=1
        return newarr == popped