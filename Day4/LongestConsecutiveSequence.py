# link="https://leetcode.com/problems/longest-consecutive-sequence/"
def longestConsecutive(nums):
    charset= set(nums)
    longest=0
    for x in charset:
        if x-1 not in charset:
            a = 0
            while x+a in charset:
                a=a+1
            longest=max(longest,a)
    return longest
            