from collections import deque
class Solution:
    def asteroidCollision(self, asteroids):
        stack = deque()
        r = 0
        while r<len(asteroids):
            if len(stack)!=0:
                while r<len(asteroids) and len(stack)!=0 and (asteroids[r]<0 and stack[-1]>0):
                    if abs(asteroids[r])==abs(stack[-1]):
                        stack.pop()
                        r+=1
                    elif abs(asteroids[r])>abs(stack[-1]):
                        stack.pop()
                    else:
                        r+=1
                if r<len(asteroids):
                    stack.append(asteroids[r])        
            


            else:    
                stack.append(asteroids[r])
            r+=1
        return stack