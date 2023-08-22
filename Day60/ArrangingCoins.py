import math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        l=1
        r=n
        res = 0
        while l<=r:
            mid = int((l+r)/2)
            a =  math.floor((mid+1)*(mid)/2)
            if a>n:
                r=mid-1

            else:
                l=mid+1
                res = max(res, mid)
        return res