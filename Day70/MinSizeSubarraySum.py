class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        l = 0 
        r = 0
        su = 0
        res = len(nums)
        found = False
        while r<len(nums):
            su +=nums[r]
            
            while su >=target:
                found = True
                res = min(res, r-l+1)
                su-=nums[l]
                l+=1
            r+=1
        if found:
            return res
        else:
            return 0
