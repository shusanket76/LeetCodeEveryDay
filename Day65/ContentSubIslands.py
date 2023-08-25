class Solution:
    def countSubIslands(self, grid1, grid2):
        path = set()
        count = 0
        def dfs(x,y):
            if (x>=0 and y>=0 and x<len(grid2) and y<len(grid2[0]) and grid2[x][y]==1 and (x,y) not in path):
                if grid1[x][y]!=1:
                    return 0
                path.add((x,y))
                a = dfs(x-1,y)
                b = dfs(x+1,y)
                c = dfs(x,y-1)
                d = dfs(x,y+1)
                if a==0 or b==0 or c==0 or d==0:
                    return False
                return True
            else:
                return -1
        for x in range(len(grid2)):
            for y in range(len(grid2[0])):
                if grid2[x][y]==1:
                    if dfs(x,y) is True:
                        count+=1
        return(count)


        