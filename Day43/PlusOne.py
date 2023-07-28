class Solution:
    def plusOne(self, digits: List[int]):
        num = ""
        for x in digits:
            num+=str(x)
        num = int(num)
        newNum = num+1
        a=[]
        newNum2=str(newNum)
        
        for b in newNum2:
            print(b)
            a.append(int(b))
        return a
