# link="https://leetcode.com/problems/group-anagrams/"

from collections import defaultdict


def groupAnagrams(strs):
    hasmap=defaultdict(list)
    for x in strs:
        count = [0]*26
        for y in x:
            order = ord(y)-ord("a")
            count[order]+=1
        hasmap[tuple(count)].append(x)
        # list cannot be keys in hasmap
    return hasmap.values()
    