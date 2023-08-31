class Solution:
    def shuffle(self, nums, n):
        sec = nums[n:]
        newar = []
        for x in range(len(sec)):
            newar.append(nums[x])
            newar.append(sec[x])
        return newar