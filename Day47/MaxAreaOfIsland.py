class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = [0]
        haset = set()
        def dfs(a,b,c):
            if a>=0 and b>=0 and a<len(grid) and b<len(grid[0]) and grid[a][b]==1 and (a,b) not in haset:
                haset.add((a,b))
                return 1+dfs(a-1,b,c+1)+dfs(a+1,b,c+1)+dfs(a,b-1,c+1)+dfs(a,b+1,c+1)
            else:
                return 0
                


            

        for a in range(len(grid)):
            for b in range(len(grid[0])):
                if grid[a][b] ==1:
                    c = 0
                    res[0] = max(res[0], dfs(a,b,c))
        return res[0]
        