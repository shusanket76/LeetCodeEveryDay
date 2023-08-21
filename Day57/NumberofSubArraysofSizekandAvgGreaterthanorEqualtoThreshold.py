class Solution:
    def numOfSubarrays(self, arr: [int], k: int, threshold: int) -> int:
        l=0
        r= 0
        res = 0
        avg = 0
        while r<len(arr):
            avg+=arr[r]
            if (r-l+1)==k:
                if (avg/k)>=threshold:
                    res+=1
                avg-=arr[l]
                l+=1
            r+=1
        return res
