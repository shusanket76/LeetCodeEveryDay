# link = "https://leetcode.com/problems/longest-repeating-character-replacement/"
# s = "ABAB", k = 2
def characterReplacement(s, k):
    hasmap={}
    l=0
    r=0
    res = 0
    while r<len(s):
        hasmap[s[r]]= hasmap.get(s[r],0)+1
        while((r-l+1)-max(hasmap.values())>k):
            hasmap[s[l]] = hasmap.get(s[l],0)-1
            l=l+1
        res = max(res,r-l+1)
        r=r+1
    return res
        
a = characterReplacement("ABABABCD",4)
# s = "ABAB", k = 2
print(a)