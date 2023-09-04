class Solution:
    def removeDuplicates(self, nums) -> int:
        hasmap = {}
        l=0
        r=len(nums)-1
        while l<=r:
            if nums[l] in hasmap and hasmap[nums[l]]==2:
                nums.pop(l)
                r-=1
            else:
                hasmap[nums[l]]=hasmap.get(nums[l], 0)+1
                l+=1
        return len(nums)
        