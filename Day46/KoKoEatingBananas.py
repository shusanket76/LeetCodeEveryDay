import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxFromArray = max(piles)
       
        l=1
        res = maxFromArray
        r=maxFromArray
        while l<=r:
           
            mid = int((l+r)/2)
            hour = 0
            for a in piles:
                hour+=math.ceil(a/mid)
            if hour<= h:
                res = min(res,mid)
                r=mid-1
        

            else:
                l=mid+1
        return res
        