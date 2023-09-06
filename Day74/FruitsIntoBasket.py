class Solution:
    def totalFruit(self, fruits) -> int:
        hasmap = {}
        l = 0
        r = 0
        res = 0 
        while r<len(fruits):
            hasmap[fruits[r]] = hasmap.get(fruits[r], 0)+1
            if len(hasmap)>2:
                while len(hasmap)!=2:
                    hasmap[fruits[l]] = hasmap.get(fruits[l], 0)-1
                    if hasmap[fruits[l]]==0:
                        hasmap.pop(fruits[l])
                    l+=1
            res= max(res, r-l+1)
            r+=1
        return(res)
            