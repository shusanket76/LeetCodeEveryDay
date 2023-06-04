# link="https://leetcode.com/problems/two-sum/"

def twoSum(nums,target):
    hasmap={}
    for x in range(len(nums)):
        weneed = target-nums[x]
        if weneed in hasmap:
            return [hasmap[weneed], x]
        else:
            hasmap[nums[x]]=x
            