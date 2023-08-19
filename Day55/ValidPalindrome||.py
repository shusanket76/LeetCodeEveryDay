class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while l<r:
            if s[l]!=s[r]:
                if s[l+1:r] == s[r:l+1:-1]:
                    return True
                if s[l:r-1] == s[r-1:l:-1]:
                    return True
                return False
            l+=1
            r-=1
        return True