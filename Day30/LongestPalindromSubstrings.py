class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=0
        resStr=""
        for x in range(len(s)):
            #oddpalindromic
            ol=x
            oor=x
            while ol>=0 and oor<=len(s)-1 and s[ol]==s[oor]:
                if res<(oor-ol+1):
                    resStr = s[ol:oor+1]
                    res=oor-ol+1
                ol-=1
                oor+=1
            rl=x
            rr=x+1
            # EVEN
            while rl>=0 and rr<=len(s)-1 and s[rl]==s[rr]:
                if res<(rr-rl+1):
                    res=rr-rl+1
                    resStr=s[rl:rr+1]
                rl-=1
                rr+=1
        return resStr