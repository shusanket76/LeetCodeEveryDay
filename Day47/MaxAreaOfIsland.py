class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        res = -(len(grid)*len(grid[0]))

        path=set()
        def dfs(x,y,path,count):
            if (x>=0 and y>=0 and x<len(grid) and y<len(grid[0]) and (x,y) not in path and grid[x][y]==1):
                path.add((x,y))
                count+=1
                count= dfs(x-1,y,path, count)
                count =dfs(x+1,y,path, count)
                count = dfs(x,y+1,path, count)
                count = dfs(x,y-1,path, count)
            return count
            
            
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]==1:
                    count = 0
                    res = max(res, dfs(x,y,path, count))
        if res<0:
            return 0
        
        return res
    