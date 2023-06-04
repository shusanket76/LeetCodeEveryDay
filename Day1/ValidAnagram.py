# link="https://leetcode.com/problems/valid-anagram/"

def isAnagram(s,t):
    hasmap={}
    for x in s:
        hasmap[x] = hasmap.get(x,0)+1
        
    for y in t:
        hasmap[y] = hasmap.get(y,0)-1
    return(max(hasmap.values())==min(hasmap.values())==0)