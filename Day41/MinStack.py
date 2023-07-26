class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minVal = []
        
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        val = min(val, self.minVal[-1] if self.minVal else val)
        self.minVal.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop(-1)
        self.minVal.pop(-1)
        
        

    def top(self):
        """
        :rtype: int
        """
        
        return self.stack[-1]
    def getMin(self):
        """
        :rtype: int
        """
        return self.minVal[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()