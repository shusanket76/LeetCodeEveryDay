from collections import deque
class Solution:
    def evalRPN(self, tokens):
        hasset = set()
        hasset.add("*")
        hasset.add("+")
        hasset.add("-")
        hasset.add("/")
        stack = deque()
        c=0
        for x in tokens:
            
            if x in hasset:
                a = int(stack.pop())
                b=int(stack.pop())
                if x=="+":
                    c = int(a)+int(b)
                elif x=="-":
                    c=int(b)-int(a)
                elif x=="/":
                    c=int(b)/int(a)
                else:
                    c=int(a)*int(b)
                stack.append(c)
            else:
                stack.append(x)
        
        if len(stack)!=0:
            return int(stack.pop())
        return c 
