import math
class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x
        mid= 0
        while l<=r:
            mid= int((l+r)/2)
            if math.floor(mid*mid) == x:
                return mid
            elif math.floor(mid*mid)>x:
                r = mid-1
            else:
                l=mid+1
        return l-1
        