class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        final=nums[0]
        l=0
        r=0
        while r<len(nums):
            res += nums[r]
            final =max(res,final)
            if res<0:
                l=r
                r=l+1
                res=0
            else:
                r+=1
        return final