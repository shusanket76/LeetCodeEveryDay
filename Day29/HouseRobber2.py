# link="https://leetcode.com/problems/house-robber-ii/submissions/988227546/"
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def houseRobber1(nums):
            rob1,rob2=0,0
            for n in nums:
                temp = max(n+rob1,rob2)
                rob1=rob2
                rob2=temp
            return rob2

        return max(nums[0],houseRobber1(nums[1:]), houseRobber1(nums[:-1]))