class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        first = 0
        second = 0
        while first<len(t):
            if second==len(s):
                return True
            if s[second] == t[first]:
                second+=1
                first+=1
            else:
                first+=1
        return  second == len(s)

