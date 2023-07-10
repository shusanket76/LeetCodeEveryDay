# link="https://leetcode.com/problems/maximum-product-subarray/"
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=max(nums)
        currMax=1
        currMin=1
        for x in nums:
            if x==0:
                currMax=1
                currMin=1
                continue
            temp=currMax*x

            currMax=max(x*currMax, x*currMin, x)
            currMin=min(temp, x*currMin, x)
            res = max(currMax,res,currMin)
        return res