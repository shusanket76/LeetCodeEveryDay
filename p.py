import math
def minEatingSpeed(piles, h: int) -> int:
        maxFromArray = max(piles)
        newarray = [x+1 for x in range(maxFromArray)]
        l=0 
        res = float("inf")
        r=len(newarray)-1
        while l<r:
           
            mid = int((l+r)/2)
            hour = 0
            for a in piles:
                hour+=math.ceil(a/newarray[mid])
            if hour<= h:
                res = min(res,newarray[mid])
                r=mid-1
                hour=0

            else:
                l=mid+1
        return res

piles = [3,6,7,11]
h = 8
a = minEatingSpeed(piles, h)
print(a)
