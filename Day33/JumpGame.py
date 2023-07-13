class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        gap=1
        r=len(nums)-2
        while r>=0:
            if nums[r]>=gap:
                gap=0
            gap+=1
            r=r-1
        if gap==0 or gap==1:
            return True
        return False