class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x= len(s)-1
        while x>=0:
            print(s[x])
            a = 0
            first = False
            while x>=0 and  s[x]!=" ":
                a+=1
                x-=1
                first = True
            if first:
                return a

            x-=1