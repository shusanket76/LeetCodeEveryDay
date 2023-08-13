class Solution:
    def isHappy(self, n: int) -> bool:
        hasmap={}

        def dfs(n):
            an = str(n)
            if len(an)==1 and n==1:
                return True
            if an in hasmap:
                return False
            res = 0
            hasmap[an]=True
            for x in an:
                res+=int(x)**2
            return dfs(res)
        return dfs(n)