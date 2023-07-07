# link = "https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/"
def findMin(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        res = nums[0]
        r=len(nums)-1
        while l<=r:
            if nums[l]<nums[r]:
                res = min(res,nums[l])
                return res
                
            m = int((l+r)/2)
            res = min(res,nums[m])
            if nums[m]>=nums[l]:
                l=m+1
            else:
                r=m-1
        return res
