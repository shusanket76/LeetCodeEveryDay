class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        for x in range(len(s)):
            # oddpalindrome
            lo=x
            lr=x
            while lo>=0 and lr<=len(s)-1 and s[lo]==s[lr]:
                res+=1
                lo-=1
                lr+=1
            # evenpalindrome
            rl=x
            rr=x+1
            while rl>=0 and rr<=len(s)-1 and s[rl]==s[rr]:
                res+=1
                rl-=1
                rr+=1
        return res