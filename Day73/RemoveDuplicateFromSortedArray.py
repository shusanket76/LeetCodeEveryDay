class Solution:
    def removeDuplicates(self, nums) -> int:
        l=0
        r=len(nums)-1
        hasmap={}
        while l<=r:
            if nums[l] in hasmap:
                nums.pop(l)
                r-=1
            else:
                hasmap[nums[l]]=True
                l+=1
        return len(nums)

        