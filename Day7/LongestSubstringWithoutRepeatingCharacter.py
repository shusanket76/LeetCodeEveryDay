# link = "https://leetcode.com/problems/longest-substring-without-repeating-characters/"
def lengthOfLongestSubstring( s):
    l=0
    r=0
    charset = set()
    res = 0
    while r<len(s):
        if s[r] in charset:
            charset.remove(s[l])
            l=l+1
        else:
            charset.add(s[r])
            r=r+1
        res = max(res,r-l)
    return res
s = "abcabcabcabcabcdabc"
b = lengthOfLongestSubstring(s)
print(b)