# link="https://leetcode.com/explore/interview/card/microsoft/47/sorting-and-searching/193/"
# INSERTION SORT


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for x in range(1,len(nums)):
            anchor = nums[x]
            j=x-1
            while j>=0 and nums[j]>anchor:
                nums[j+1]=nums[j]
                j=j-1
            nums[j+1]=anchor