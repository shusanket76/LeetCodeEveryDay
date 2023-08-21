class Solution:
    def containsNearbyDuplicate(self, nums:[int], k: int) -> bool:
        hasmap = {}
        for x in range(len(nums)):
            if nums[x] in hasmap:
                if abs(x-hasmap[nums[x]])<=k:
                    return True
                hasmap[nums[x]] =x
            else:
                hasmap[nums[x]] = x

        return False