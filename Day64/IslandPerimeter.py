class Solution:
    def islandPerimeter(self, grid):
        count = [0]
        path=set()
        def dfs(x,y,path):
            if (x,y) in path:
                return True
            if (x>=0 and y>=0 and x<len(grid) and y<len(grid[0]) and grid[x][y]==1):
                path.add((x,y))
                count[0]+=4
                if dfs(x-1,y,path) is True:
                    count[0]-=1
                if dfs(x+1,y,path) is True:
                    count[0]-=1
                if dfs(x,y-1,path) is True:
                    count[0]-=1
                if dfs(x,y+1,path) is True:
                    count[0]-=1
                return True
            else:
                return False


        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]==1:
                    dfs(x,y, path)
              
                    
                    break
        return(count[0])