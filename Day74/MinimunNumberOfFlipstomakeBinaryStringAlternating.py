class Solution:
    def minFlips(self, s: str) -> int:
        lens1 = len(s)-1
        s+=s
        lens = len(s)-1
        l = 0
        r = 0
        diff1 = 0
        diff2 = 0 
        arr1 = [x%2 for x in range(lens)]
        arr2 = [x%2 for x in range(1,lens+1)]
        res = len(s)
        while r<lens:
            if int(s[r])!=arr1[r]:
                diff1+=1
            if int(s[r])!=arr2[r]:
                diff2+=1
            if (r-l) == lens1:
                res = min(res, diff1, diff2)
                if int(s[l])!=arr1[l]:
                    diff1-=1
                if int(s[l])!=arr2[l]:
                    diff2-=1
                
                l+=1
            r+=1
        return(res)
