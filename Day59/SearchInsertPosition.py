class Solution:
    def searchInsert(self, nums:[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            mid = int((l+r)/2)
            if nums[mid] == target:
                return mid
            if nums[mid]<target:
                l+=1
            else:
                r-=1
        return l
