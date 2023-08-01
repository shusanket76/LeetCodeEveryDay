class Solution:
    def findDuplicate(self, nums: [int]) -> int:
        fast = 0
        slow = 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast==slow:
                break
        
        slow2=0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow==slow2:
                return slow