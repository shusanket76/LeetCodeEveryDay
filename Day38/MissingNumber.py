class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        a=0
        print(nums)
        for x in range(len(nums)):
            print(nums[x],a)
            if nums[x]!=a:
                break
            
            a=a+1
        return a