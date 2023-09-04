class Solution:
    def removeElement(self, nums, val):
        k = 0
        for x in range(len(nums)):
            if nums[x]!=val:
                nums[k] = nums[x]
                k+=1
        return k
