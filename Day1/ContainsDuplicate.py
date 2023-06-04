# link = "https://leetcode.com/problems/contains-duplicate/"



def containsDuplicate(self,nums):
    hasmap={}
    for x in nums:
        if x in hasmap:
            return True
        else:
            hasmap[x] = True
    return False