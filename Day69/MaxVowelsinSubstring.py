class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l= 0 
        r=0
        num = 0
        tempnum = 0
        haset = set()
        haset.add("a")
        haset.add("e")
        haset.add("i")
        haset.add("o")
        haset.add("u")
        while r<len(s):
            if s[r] in haset:
                tempnum+=1
            if (r-l+1)==k:
                num = max(num, tempnum)
                if s[l] in haset:
                    tempnum -=1
                l+=1
            r+=1
        return num
                 