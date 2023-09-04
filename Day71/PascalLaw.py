class Solution:
    def generate(self, numRows):
        last = [1]
        res = [[1]]
        new=[]
        for x in range(2,numRows+1):
            a = 0
            while a<x:
                if a-1<0:
                    first = 0
                else:
                    first = last[a-1]
                if a>=len(last):
                    second = 0
                else:
                    second = last[a]
                new.append(first+second)
                a+=1
            res.append(new)
            last = new
            new = []
        return res
