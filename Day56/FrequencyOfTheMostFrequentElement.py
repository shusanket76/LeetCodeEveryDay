class Solution:
    def maxFrequency(self, nums:[int], k: int) -> int:
        l = 0
        res = 0
        r= 0
        total = 0
        nums.sort()
        print(nums)
        while r<len(nums):
            total+=nums[r]
            while nums[r]*(r-l+1)>total+k:
                total-=nums[l]
                l+=1
            res = max(res, r-l+1)
            r+=1
        return res

