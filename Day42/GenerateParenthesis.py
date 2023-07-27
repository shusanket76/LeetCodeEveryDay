class Solution:
    def generateParenthesis(self, n: int):
        res = []
        def dfs(o,c, n, s):
            if o==n and c==n:
                res.append(s)
            if o==c:
                s+="("
                dfs(o+1,c,n,s)
            elif o>c:
                if o>n:
                    return 
                s+="("
                dfs(o+1,c,n,s)
                s=s[:len(s)-1]
                s+=")"
                dfs(o,c+1,n,s)
            return 
            




        dfs(0,0,n,"")
        return res
