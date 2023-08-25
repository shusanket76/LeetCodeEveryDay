class Solution:
    def combine(self, n: int, k: int):
        res=[]
        def dfs(pointer, curr):
            if len(curr)==k:
                res.append(curr[:])
                return 
            for x in range(pointer+1, n+1):
                curr.append(x)
                dfs(x, curr)
                curr.pop(-1)
    


        pointer = 0
        curr=[]
        dfs(pointer, curr)
        return(res)